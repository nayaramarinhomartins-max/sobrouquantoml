"""
ml_sync_tabelas.py
------------------
Sincroniza comissões, frete e custo fixo do Mercado Livre para o Supabase.

CONFIGURAÇÃO:
  Edite as 3 variáveis abaixo com seus dados do Supabase.

USO:
  pip install requests
  python ml_sync_tabelas.py
"""

import requests
import json
from datetime import datetime, timezone, timedelta

# ============================================================
# ✏️  CONFIGURE AQUI
# ============================================================
SUPABASE_URL    = "https://xouelriibnorzgzltyua.supabase.co"
SUPABASE_KEY    = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhvdWVscmlpYm5vcnpnemx0eXVhIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3OTg1MjMzMiwiZXhwIjoyMDk1NDI4MzMyfQ.T-vthIgssa5rI96R90X_Jgi7kMHgavmfJOp9x6OYR2I"
ML_USER_ID      = "486592381"
ML_CLIENT_ID    = "3946066402619314"
ML_CLIENT_SECRET= "YUXQKCJBo0YkKP9NrjyUQZjJas8c7PwB"
# ============================================================

SUPABASE_HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
}
 
# Mapeamento: nome da categoria no seu código → ID da categoria no ML
# IDs validados via GET /sites/MLB/categories em 13/03/2026
CATEGORIAS_ML = {
    "Acessórios para Veículos":   "MLB5672",
    "Agro":                        "MLB271599",
    "Alimentos e Bebidas":         "MLB1403",
    "Antiguidades e coleções":     "MLB1367",
    "Arte, Papelaria e Armarinho": "MLB1368",
    "Bebês":                       "MLB1384",
    "Beleza e Cuidado Pessoal":    "MLB1246",
    "Brinquedos e Hobbies":        "MLB1132",
    "Calçados, Roupas e Bolsas":   "MLB1430",
    "Câmeras e Acessórios":        "MLB1039",
    "Casa, Móveis e Decoração":    "MLB1574",
    "Celulares e Telefones":       "MLB1051",
    "Computação":                  "MLB1648",
    "Construção":                  "MLB1500",
    "Eletrodomésticos":            "MLB5726",
    "Eletrônicos, Áudio e Vídeo":  "MLB1000",
    "Esportes e Fitness":          "MLB1276",
    "Ferramentas":                 "MLB263532",
    "Games":                       "MLB1144",
    "Indústria e Escritório":      "MLB1499",
    "Instrumentos Musicais":       "MLB1182",
    "Joalheria e Relógios":        "MLB3937",
    "Livros, Revistas e Comics":   "MLB1196",
    "Música, Filmes e Seriados":   "MLB1168",
    "Saúde":                       "MLB264586",
    "Supermercado":                "MLB1403",
    "Outros":                      "MLB1953",
}
 
# Tabela de frete — Envios Full, Coleta e Agências ML
# Fonte: tabela oficial ML Brasil (Fev/Mar 2026)
# Inclui desconto de até 70% por reputação
# Faixas de peso em gramas, faixas de preço em R$
#
# FAIXAS DE PREÇO:
#   0-18.99      → produtos até R$18,99 (max 50% do preço)
#   19-48.99     → R$19 a R$48,99
#   49-78.99     → R$49 a R$78,99
#   79-99.99     → R$79 a R$99,99
#   100-119.99   → R$100 a R$119,99
#   120-149.99   → R$120 a R$149,99
#   150-199.99   → R$150 a R$199,99
#   200+         → a partir de R$200
#
# FAIXAS DE PESO em gramas:
#   0-300 / 300-500 / 500-1000 / 1000-1500 / 1500-2000 /
#   2000-3000 / 3000-4000 / 4000-5000 / 5000-6000 / 6000-7000 /
#   7000-8000 / 8000-9000 / 9000-11000 / 11000-13000 / 13000-15000 /
#   15000-17000 / 17000-20000 / 20000-25000 / 25000-30000 /
#   30000-40000 / 40000-50000 / 50000-60000 / 60000-70000 /
#   70000-80000 / 80000-90000 / 90000-100000 / 100000-125000 /
#   125000-150000 / 150000+
 
FRETE_TABELA = {
    "0-18.99": {
        # Produtos abaixo de R$19 pagam no máximo metade do preço
        # Valor fixo usado como referência — cálculo real é min(valor, preco/2)
        "0-300":5.65,"300-500":5.95,"500-1000":6.05,"1000-1500":6.15,
        "1500-2000":6.25,"2000-3000":6.35,"3000-4000":6.45,"4000-5000":6.55,
        "5000-6000":6.65,"6000-7000":6.75,"7000-8000":6.85,"8000-9000":6.95,
        "9000-11000":7.05,"11000-13000":7.15,"13000-15000":7.25,"15000-17000":7.35,
        "17000-20000":7.45,"20000-25000":7.65,"25000-30000":7.75,"30000-40000":7.85,
        "40000-50000":7.95,"50000-60000":8.05,"60000-70000":8.15,"70000-80000":8.25,
        "80000-90000":8.35,"90000-100000":8.45,"100000-125000":8.55,
        "125000-150000":8.65,"150000+":8.75
    },
    "19-48.99": {
        "0-300":6.55,"300-500":6.65,"500-1000":6.75,"1000-1500":6.85,
        "1500-2000":6.95,"2000-3000":7.95,"3000-4000":8.15,"4000-5000":8.35,
        "5000-6000":8.55,"6000-7000":8.75,"7000-8000":8.95,"8000-9000":9.15,
        "9000-11000":9.55,"11000-13000":9.95,"13000-15000":10.15,"15000-17000":10.35,
        "17000-20000":10.55,"20000-25000":10.95,"25000-30000":11.15,"30000-40000":11.35,
        "40000-50000":11.55,"50000-60000":11.75,"60000-70000":11.95,"70000-80000":12.15,
        "80000-90000":12.35,"90000-100000":12.55,"100000-125000":12.75,
        "125000-150000":12.75,"150000+":12.95
    },
    "49-78.99": {
        "0-300":7.75,"300-500":7.85,"500-1000":7.95,"1000-1500":8.05,
        "1500-2000":8.15,"2000-3000":8.55,"3000-4000":8.95,"4000-5000":9.75,
        "5000-6000":9.95,"6000-7000":10.15,"7000-8000":10.35,"8000-9000":10.55,
        "9000-11000":10.95,"11000-13000":11.35,"13000-15000":11.55,"15000-17000":11.75,
        "17000-20000":11.95,"20000-25000":12.15,"25000-30000":12.35,"30000-40000":12.55,
        "40000-50000":12.75,"50000-60000":12.95,"60000-70000":13.15,"70000-80000":13.35,
        "80000-90000":13.55,"90000-100000":13.75,"100000-125000":13.95,
        "125000-150000":14.15,"150000+":14.35
    },
    "79-99.99": {
        "0-300":12.35,"300-500":13.25,"500-1000":13.85,"1000-1500":14.15,
        "1500-2000":14.45,"2000-3000":15.75,"3000-4000":17.05,"4000-5000":18.45,
        "5000-6000":25.45,"6000-7000":27.05,"7000-8000":28.85,"8000-9000":29.65,
        "9000-11000":41.25,"11000-13000":42.15,"13000-15000":45.05,"15000-17000":48.55,
        "17000-20000":54.75,"20000-25000":64.05,"25000-30000":65.95,"30000-40000":67.75,
        "40000-50000":70.25,"50000-60000":74.95,"60000-70000":80.25,"70000-80000":83.95,
        "80000-90000":93.25,"90000-100000":106.55,"100000-125000":119.25,
        "125000-150000":126.55,"150000+":166.15
    },
    "100-119.99": {
        "0-300":14.35,"300-500":15.45,"500-1000":16.15,"1000-1500":16.45,
        "1500-2000":16.85,"2000-3000":18.35,"3000-4000":19.85,"4000-5000":21.55,
        "5000-6000":28.55,"6000-7000":31.05,"7000-8000":33.65,"8000-9000":34.55,
        "9000-11000":48.05,"11000-13000":49.25,"13000-15000":52.45,"15000-17000":56.05,
        "17000-20000":63.85,"20000-25000":75.05,"25000-30000":75.45,"30000-40000":78.95,
        "40000-50000":81.05,"50000-60000":86.45,"60000-70000":92.95,"70000-80000":97.05,
        "80000-90000":107.45,"90000-100000":123.95,"100000-125000":138.05,
        "125000-150000":146.15,"150000+":192.45
    },
    "120-149.99": {
        "0-300":16.45,"300-500":17.65,"500-1000":18.45,"1000-1500":18.85,
        "1500-2000":19.25,"2000-3000":21.05,"3000-4000":22.65,"4000-5000":24.65,
        "5000-6000":32.65,"6000-7000":36.05,"7000-8000":38.45,"8000-9000":39.55,
        "9000-11000":54.95,"11000-13000":56.25,"13000-15000":59.95,"15000-17000":63.55,
        "17000-20000":72.95,"20000-25000":84.75,"25000-30000":85.55,"30000-40000":88.95,
        "40000-50000":92.05,"50000-60000":98.15,"60000-70000":105.05,"70000-80000":109.85,
        "80000-90000":122.05,"90000-100000":139.55,"100000-125000":156.05,
        "125000-150000":165.65,"150000+":217.55
    },
    "150-199.99": {
        "0-300":18.45,"300-500":19.85,"500-1000":20.75,"1000-1500":21.15,
        "1500-2000":21.65,"2000-3000":23.65,"3000-4000":25.55,"4000-5000":27.75,
        "5000-6000":35.75,"6000-7000":40.05,"7000-8000":43.25,"8000-9000":44.45,
        "9000-11000":61.75,"11000-13000":63.25,"13000-15000":67.45,"15000-17000":70.75,
        "17000-20000":82.05,"20000-25000":95.35,"25000-30000":96.25,"30000-40000":99.15,
        "40000-50000":102.55,"50000-60000":109.35,"60000-70000":117.15,"70000-80000":122.45,
        "80000-90000":136.05,"90000-100000":155.55,"100000-125000":173.95,
        "125000-150000":184.65,"150000+":242.55
    },
    "200+": {
        "0-300":20.95,"300-500":22.55,"500-1000":23.65,"1000-1500":24.65,
        "1500-2000":24.65,"2000-3000":26.25,"3000-4000":28.35,"4000-5000":30.75,
        "5000-6000":39.75,"6000-7000":44.05,"7000-8000":48.05,"8000-9000":49.35,
        "9000-11000":68.65,"11000-13000":70.25,"13000-15000":74.95,"15000-17000":78.65,
        "17000-20000":91.15,"20000-25000":105.95,"25000-30000":106.95,"30000-40000":107.05,
        "40000-50000":110.75,"50000-60000":118.15,"60000-70000":126.55,"70000-80000":132.25,
        "80000-90000":146.95,"90000-100000":167.95,"100000-125000":187.95,
        "125000-150000":199.45,"150000+":261.95
    }
}
 
# Custo fixo por tipo de categoria
CUSTO_FIXO = [
    # tipo,          preco_min, preco_max, valor,  percentual
    ("livros",        0,        6,         0,      True),   # 50% do preço
    ("livros",        6,        29,        3.0,    False),
    ("livros",        29,       50,        3.5,    False),
    ("livros",        50,       79,        4.0,    False),
    ("livros",        79,       None,      0,      False),
    ("supermercado",  0,        8,         0,      False),
    ("supermercado",  8,        12.5,      0,      True),   # 50% do preço
    ("supermercado",  12.5,     29,        3.0,    False),
    ("supermercado",  29,       50,        3.5,    False),
    ("supermercado",  50,       79,        4.0,    False),
    ("supermercado",  79,       199,       6.0,    False),
    ("supermercado",  199,      None,      0,      False),
    ("geral",         0,        12.5,      0,      True),   # 50% do preço
    ("geral",         12.5,     29,        6.25,   False),
    ("geral",         29,       50,        6.5,    False),
    ("geral",         50,       79,        6.75,   False),
    ("geral",         79,       None,      0,      False),
]
 
 
# ============================================================
# FUNÇÕES
# ============================================================
 
def supabase_get(table, params=""):
    r = requests.get(
        f"{SUPABASE_URL}/rest/v1/{table}?{params}",
        headers=SUPABASE_HEADERS
    )
    return r.json()
 
def supabase_upsert(table, data):
    headers = {**SUPABASE_HEADERS, "Prefer": "resolution=merge-duplicates"}
    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/{table}",
        headers=headers,
        json=data
    )
    return r.status_code
 
def get_token():
    """Lê token do Supabase e renova se estiver vencido."""
    rows = supabase_get("ml_tokens", f"user_id=eq.{ML_USER_ID}")
    if not rows:
        raise Exception("❌ Token não encontrado no Supabase. Execute o INSERT primeiro.")
 
    row = rows[0]
    expires_at = datetime.fromisoformat(row["expires_at"].replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
 
    if now >= expires_at - timedelta(minutes=5):
        print("🔄 Token expirado, renovando...")
        r = requests.post(
            "https://api.mercadolibre.com/oauth/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "refresh_token",
                "client_id": ML_CLIENT_ID,
                "client_secret": ML_CLIENT_SECRET,
                "refresh_token": row["refresh_token"]
            }
        )
        data = r.json()
        if "access_token" not in data:
            raise Exception(f"❌ Erro ao renovar token: {data}")
 
        new_expires = datetime.now(timezone.utc) + timedelta(seconds=data["expires_in"])
        supabase_upsert("ml_tokens", {
            "user_id": ML_USER_ID,
            "access_token": data["access_token"],
            "refresh_token": data["refresh_token"],
            "expires_at": new_expires.isoformat()
        })
        print(f"✅ Token renovado. Novo refresh: {data['refresh_token'][:30]}...")
        return data["access_token"]
 
    print("✅ Token válido.")
    return row["access_token"]
 
 
def sync_comissoes(token):
    """
    Consulta ML para cada categoria e salva no Supabase.
 
    LÓGICA DE COBRANÇA:
      - Clássico (gold_special): cobra comissão % sobre a venda. Frete pago pelo comprador.
      - Premium (gold_premium):  cobra comissão = clássico + 5% (confirmado ML Brasil 2026).
        A API retorna 0 para gold_premium, mas o ML cobra clássico+5% na prática.
        Além disso, o vendedor paga o frete (frete grátis pro comprador).
    """
    print("\n📦 Sincronizando comissões...")
    print("   ℹ️  Premium = Clássico + 5% (ex: clássico 11.5% → premium 16.5%)\n")
    headers = {"Authorization": f"Bearer {token}"}
    registros = []
 
    for categoria, cat_id in CATEGORIAS_ML.items():
        row = {
            "categoria": categoria,
            "atualizado_em": datetime.now(timezone.utc).isoformat()
        }
 
        # --- Clássico: busca % de comissão na API ---
        url_classico = (
            f"https://api.mercadolibre.com/sites/MLB/listing_prices"
            f"?price=200&category_id={cat_id}&listing_type_id=gold_special"
        )
        r = requests.get(url_classico, headers=headers)
        data = r.json()
        pct_classico = data.get("sale_fee_details", {}).get("percentage_fee", 0)
        row["classico"] = pct_classico
 
        # --- Premium: clássico + 5% (API retorna 0, mas ML cobra +5% na prática) ---
        pct_premium = round(pct_classico + 5, 2)
        row["premium"] = pct_premium
 
        print(f"  {categoria[:35]:<35} clássico: {pct_classico}%  |  premium: {pct_premium}%")
        registros.append(row)
 
    status = supabase_upsert("ml_comissoes", registros)
    print(f"\n✅ Comissões salvas no Supabase (status {status})")
 
 
def sync_frete():
    """Salva tabela de frete no Supabase."""
    print("\n🚚 Sincronizando frete...")
    registros = []
    for faixa_preco, pesos in FRETE_TABELA.items():
        for faixa_peso, valor in pesos.items():
            registros.append({
                "faixa_preco": faixa_preco,
                "faixa_peso": faixa_peso,
                "valor": valor,
                "atualizado_em": datetime.now(timezone.utc).isoformat()
            })
 
    status = supabase_upsert("ml_frete", registros)
    print(f"✅ {len(registros)} registros de frete salvos (status {status})")
 
 
def sync_custo_fixo():
    """Salva regras de custo fixo no Supabase."""
    print("\n💰 Sincronizando custo fixo...")
    registros = []
    for tipo, pmin, pmax, valor, percentual in CUSTO_FIXO:
        registros.append({
            "categoria_tipo": tipo,
            "preco_min": pmin,
            "preco_max": pmax,
            "valor": valor,
            "percentual": percentual,
            "atualizado_em": datetime.now(timezone.utc).isoformat()
        })
 
    status = supabase_upsert("ml_custo_fixo", registros)
    print(f"✅ {len(registros)} regras de custo fixo salvas (status {status})")
 
 
# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  ML SYNC — Sincronização de Tabelas")
    print("=" * 50)
 
    token = get_token()
    sync_comissoes(token)
    sync_frete()
    sync_custo_fixo()
 
    print("\n🎉 Sincronização concluída!")
    print("   Supabase atualizado com comissões, frete e custo fixo.")
    print("")
    print("   RESUMO DA LÓGICA DE CÁLCULO:")
    print("   • Clássico → desconta comissão % + frete pago pelo comprador")
    print("   • Premium  → SEM comissão %, mas vendedor paga o frete (já em ml_frete)")