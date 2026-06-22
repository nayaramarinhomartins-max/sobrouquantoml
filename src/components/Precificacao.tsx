import React, { useState, useEffect } from 'react';
import { supabase } from '../lib/supabase';
import * as XLSX from 'xlsx';
import { Plus, Trash2, Download, Calculator, RefreshCw } from 'lucide-react';

// ─────────────────────────────────────────────
// TIPOS
// ─────────────────────────────────────────────
interface Produto {
  id: string;          // UUID gerado no cliente — chave primária real
  mlb: string; name: string; custo: number; acos: number; preco: number;
  desconto: number; frete: number; fretePersonalizado: boolean;
  pesoReferencia: number; imposto: number; categoria: string;
  tipoAnuncio: 'classico' | 'premium'; comissaoPersonalizada: boolean;
  comissao: number; custoFixo: number; g: number; j: number; k: number; l: string;
}

interface ComissaoRow  { categoria: string; classico: number; premium: number; }
interface FreteRow     { faixa_preco: string; faixa_peso: string; valor: number; }
interface CustoFixoRow { categoria_tipo: string; preco_min: number; preco_max: number | null; valor: number; percentual: boolean; }

// Gera UUID v4 simples no cliente
const uuid = () => 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
  const r = Math.random() * 16 | 0;
  return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
});

const pesoMedio: { [k: string]: number } = {
  'Acessórios para Veículos':1500,'Agro':2000,'Alimentos e Bebidas':500,
  'Antiguidades e coleções':1000,'Arte, Papelaria e Armarinho':300,'Bebês':800,
  'Beleza e Cuidado Pessoal':200,'Brinquedos e Hobbies':600,'Calçados, Roupas e Bolsas':400,
  'Câmeras e Acessórios':500,'Casa, Móveis e Decoração':2000,'Celulares e Telefones':200,
  'Computação':1000,'Construção':3000,'Eletrodomésticos':5000,'Eletrônicos, Áudio e Vídeo':800,
  'Esportes e Fitness':1000,'Ferramentas':1500,'Games':300,'Indústria e Escritório':1000,
  'Instrumentos Musicais':2000,'Joalheria e Relógios':100,'Livros, Revistas e Comics':400,
  'Música, Filmes e Seriados':200,'Saúde':300,'Supermercado':500,'Outros':1000
};
const categorias = Object.keys(pesoMedio);

const statusColor = (k: number) => k > 10 ? 'var(--green)' : k > 5 ? 'var(--yellow)' : k > 1 ? 'var(--orange)' : 'var(--red)';
const statusBg    = (k: number) => k > 10 ? 'var(--green-bg)' : k > 5 ? 'var(--yellow-bg)' : k > 1 ? 'var(--orange-bg)' : 'var(--red-bg)';

function getFaixaPreco(p: number) {
  if (p < 19)  return '0-18.99';
  if (p < 49)  return '19-48.99';
  if (p < 79)  return '49-78.99';
  if (p < 100) return '79-99.99';
  if (p < 120) return '100-119.99';
  if (p < 150) return '120-149.99';
  if (p < 200) return '150-199.99';
  return '200+';
}
function getFaixaPeso(w: number) {
  if (w<=300)    return '0-300';
  if (w<=500)    return '300-500';
  if (w<=1000)   return '500-1000';
  if (w<=1500)   return '1000-1500';
  if (w<=2000)   return '1500-2000';
  if (w<=3000)   return '2000-3000';
  if (w<=4000)   return '3000-4000';
  if (w<=5000)   return '4000-5000';
  if (w<=6000)   return '5000-6000';
  if (w<=7000)   return '6000-7000';
  if (w<=8000)   return '7000-8000';
  if (w<=9000)   return '8000-9000';
  if (w<=11000)  return '9000-11000';
  if (w<=13000)  return '11000-13000';
  if (w<=15000)  return '13000-15000';
  if (w<=17000)  return '15000-17000';
  if (w<=20000)  return '17000-20000';
  if (w<=25000)  return '20000-25000';
  if (w<=30000)  return '25000-30000';
  if (w<=40000)  return '30000-40000';
  if (w<=50000)  return '40000-50000';
  if (w<=60000)  return '50000-60000';
  if (w<=70000)  return '60000-70000';
  if (w<=80000)  return '70000-80000';
  if (w<=90000)  return '80000-90000';
  if (w<=100000) return '90000-100000';
  if (w<=125000) return '100000-125000';
  if (w<=150000) return '125000-150000';
  return '150000+';
}

// ─────────────────────────────────────────────
// COMPONENTE
// ─────────────────────────────────────────────
export const Precificacao = ({ userId }: { userId?: string }) => {
  const [produtos, setProdutos]         = useState<Produto[]>([]);
  const [comissoesDB, setComissoesDB]   = useState<ComissaoRow[]>([]);
  const [freteDB, setFreteDB]           = useState<FreteRow[]>([]);
  const [custoFixoDB, setCustoFixoDB]   = useState<CustoFixoRow[]>([]);
  const [carregandoDB, setCarregandoDB] = useState(true);

  // ── Carrega tabelas do Supabase ──────────────
  useEffect(() => {
    async function carregarTabelas() {
      setCarregandoDB(true);
      const [{ data: com }, { data: fre }, { data: cuf }] = await Promise.all([
        supabase.from('ml_comissoes').select('*'),
        supabase.from('ml_frete').select('*'),
        supabase.from('ml_custo_fixo').select('*'),
      ]);
      if (com) setComissoesDB(com);
      if (fre) setFreteDB(fre);
      if (cuf) setCustoFixoDB(cuf);
      setCarregandoDB(false);
    }
    carregarTabelas();
  }, []);

  // ── Carrega produtos do usuário ──────────────
  useEffect(() => {
    if (!userId) return;
    supabase.from('sobra_quanto_precificacao')
      .select('*')
      .eq('user_id', userId)
      .order('criado_em', { ascending: true })
      .then(({ data }) => {
        if (data && data.length > 0) {
          setProdutos(data.map((d: any) => ({
            id:   d.id,
            mlb:  d.mlb || '',
            name: d.nome || '',
            custo:   Number(d.custo),
            acos:    Number(d.acos),
            preco:   Number(d.preco),
            desconto: Number(d.desconto),
            frete:   Number(d.frete),
            fretePersonalizado: d.frete_personalizado || false,
            pesoReferencia: pesoMedio[d.categoria] || 1000,
            imposto:  Number(d.imposto),
            categoria: d.categoria || 'Outros',
            tipoAnuncio: d.tipo_anuncio || 'classico',
            comissaoPersonalizada: false,
            comissao:  Number(d.comissao),
            custoFixo: Number(d.custo_fixo),
            g: Number(d.custo_fixo) + Number(d.frete),
            j: Number(d.lucro_calculado),
            k: Number(d.margem_calculada),
            l: d.status_margem || '',
          })));
        }
        // Sem fallback localStorage — se não tem no Supabase, começa vazio
      });
  }, [userId]);

  const getComissao = (categoria: string, tipo: 'classico' | 'premium'): number => {
    const row = comissoesDB.find(r => r.categoria === categoria)
             || comissoesDB.find(r => r.categoria === 'Outros');
    if (!row) return tipo === 'premium' ? 17 : 12;
    return tipo === 'premium' ? Number(row.premium) : Number(row.classico);
  };

  const calcFrete = (preco: number, peso: number): number => {
    const row = freteDB.find(r => r.faixa_preco === getFaixaPreco(preco) && r.faixa_peso === getFaixaPeso(peso));
    return row ? Number(row.valor) : 0;
  };

  const calcCustoFixo = (preco: number, cat: string): number => {
    const tipo = cat === 'Livros, Revistas e Comics' ? 'livros'
               : cat === 'Supermercado'              ? 'supermercado'
               : 'geral';
    const regras = custoFixoDB
      .filter(r => r.categoria_tipo === tipo)
      .sort((a, b) => a.preco_min - b.preco_min);
    for (const r of regras) {
      if (preco >= r.preco_min && (r.preco_max === null || preco < r.preco_max))
        return r.percentual ? preco / 2 : Number(r.valor);
    }
    return 0;
  };

  const calcularLucro = (p: Produto) => {
    const pe = p.preco * (1 - p.desconto / 100);
    const lucro = pe - p.custo - (pe * p.acos / 100) - (pe * p.imposto / 100) - (pe * p.comissao / 100) - p.g;
    const margem = pe > 0 ? (lucro / pe * 100) : 0;
    const status = margem > 10 ? 'ÓTIMA MARGEM' : margem > 5 ? 'MARGEM BOA' : margem > 1 ? 'MARGEM BAIXA' : 'PREJUÍZO';
    return { lucro, margem, status };
  };

  // ── Salvar no Supabase — sempre usa id como chave ──
  const salvarProduto = async (p: Produto) => {
    if (!userId) return;
    await supabase.from('sobra_quanto_precificacao').upsert({
      id: p.id,
      user_id: userId,
      mlb: p.mlb, nome: p.name, custo: p.custo, acos: p.acos,
      preco: p.preco, desconto: p.desconto, frete: p.frete,
      frete_personalizado: p.fretePersonalizado, imposto: p.imposto,
      categoria: p.categoria, tipo_anuncio: p.tipoAnuncio,
      comissao: p.comissao, custo_fixo: p.custoFixo,
      lucro_calculado: p.j, margem_calculada: p.k, status_margem: p.l,
      atualizado_em: new Date().toISOString(),
    }, { onConflict: 'id' });
  };

  const deletarProduto = async (id: string) => {
    if (!userId) return;
    await supabase.from('sobra_quanto_precificacao')
      .delete().eq('user_id', userId).eq('id', id);
  };

  const novoProduto = (): Produto => ({
    id: uuid(),   // UUID gerado agora — nunca vai colidir
    mlb: '', name: '', custo: 0, acos: 0, preco: 0, desconto: 0, frete: 0,
    fretePersonalizado: false, pesoReferencia: 1000, imposto: 0,
    categoria: 'Outros', tipoAnuncio: 'classico', comissaoPersonalizada: false,
    comissao: getComissao('Outros', 'classico'), custoFixo: 0, g: 0, j: 0, k: 0, l: '',
  });

  const add = () => {
    const novo = novoProduto();
    setProdutos(p => [...p, novo]);
    salvarProduto(novo); // salva imediatamente com campos zerados
  };

  const del = (i: number) => {
    const id = produtos[i]?.id;
    setProdutos(p => p.filter((_, idx) => idx !== i));
    if (id) deletarProduto(id);
  };

  const upd = (index: number, field: keyof Produto, value: any) => {
    setProdutos(prev => {
      const next = [...prev];
      next[index] = { ...next[index], [field]: value };
      const p = next[index];

      if (field === 'categoria')
        p.pesoReferencia = pesoMedio[p.categoria] || 1000;

      if ((field === 'categoria' || field === 'tipoAnuncio') && !p.comissaoPersonalizada)
        p.comissao = getComissao(p.categoria, p.tipoAnuncio);

      if ((field === 'preco' || field === 'desconto' || field === 'categoria') && !p.fretePersonalizado) {
        const pe = p.preco * (1 - p.desconto / 100);
        p.frete = calcFrete(pe, p.pesoReferencia);
      }

      const pe = p.preco * (1 - p.desconto / 100);
      p.custoFixo = calcCustoFixo(pe, p.categoria);
      p.g = p.frete + p.custoFixo;

      const { lucro, margem, status } = calcularLucro(p);
      p.j = lucro; p.k = margem; p.l = status;

      // Sempre salva no Supabase — sem fallback localStorage
      salvarProduto(next[index]);

      return next;
    });
  };

  const exportar = () => {
    if (!produtos.length) return;
    const data = produtos.map(p => ({
      MLB: p.mlb, Produto: p.name, 'Custo (R$)': p.custo,
      'ACOS (%)': p.acos, 'Preço (R$)': p.preco, 'Desconto (%)': p.desconto,
      'Preço Efetivo (R$)': (p.preco * (1 - p.desconto / 100)).toFixed(2),
      'Frete (R$)': p.frete, 'Custo Fixo (R$)': p.custoFixo,
      'Taxa Total (R$)': p.g, 'Imposto (%)': p.imposto, 'Comissão (%)': p.comissao,
      'Lucro (R$)': p.j.toFixed(2), 'Margem (%)': p.k.toFixed(2),
      Status: p.l, Categoria: p.categoria, 'Tipo Anúncio': p.tipoAnuncio,
    }));
    const ws = XLSX.utils.json_to_sheet(data);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Precificação');
    XLSX.writeFile(wb, 'SobraQuantoML_Precificacao.xlsx');
  };

  const fmt2 = (v: number) => v.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  const CSS = `
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    .prec-wrap{font-family:'Inter',system-ui,sans-serif}
    .prec-toolbar{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;gap:12px;flex-wrap:wrap}
    .prec-title{font-size:15px;font-weight:700;color:var(--tx);display:flex;align-items:center;gap:8px}
    .prec-actions{display:flex;gap:8px;align-items:center}
    .prec-btn-add{display:flex;align-items:center;gap:6px;height:34px;padding:0 14px;background:#2563EB;color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;font-family:inherit;transition:background .14s}
    .prec-btn-add:hover{background:#1D4ED8}
    .prec-btn-exp{display:flex;align-items:center;gap:6px;height:34px;padding:0 14px;background:var(--surface-2);color:var(--tx-2);border:1.5px solid var(--border);border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;font-family:inherit;transition:all .14s}
    .prec-btn-exp:hover{border-color:var(--green);color:var(--green)}
    .prec-btn-exp:disabled{opacity:.4;cursor:not-allowed}
    .prec-loading{display:flex;align-items:center;gap:6px;font-size:11px;color:var(--tx-4);padding:2px 8px}
    .prec-loading svg{animation:spin 1s linear infinite}
    @keyframes spin{to{transform:rotate(360deg)}}
    .prec-tbl-wrap{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);overflow:hidden}
    .prec-tbl{width:100%;border-collapse:collapse;font-size:12px}
    .prec-tbl th{padding:10px 12px;text-align:left;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--tx-3);background:var(--surface-2);border-bottom:1px solid var(--border);white-space:nowrap}
    .prec-tbl th.r{text-align:right}
    .prec-tbl td{padding:8px 12px;border-bottom:1px solid var(--border);color:var(--tx-2);vertical-align:middle}
    .prec-tbl tr:last-child td{border-bottom:none}
    .prec-tbl tbody tr{transition:background .1s}
    .prec-tbl tbody tr:hover{background:var(--surface-2)}
    .prec-inp{background:transparent;border:none;border-bottom:1.5px solid var(--border);outline:none;width:100%;color:var(--tx);font-size:12px;font-family:inherit;padding:2px 0;transition:border-color .14s}
    .prec-inp:focus{border-color:#2563EB}
    .prec-inp.r{text-align:right}
    .prec-inp::placeholder{color:var(--tx-4)}
    .prec-sel{background:var(--surface-2);border:1.5px solid var(--border);border-radius:6px;color:var(--tx);font-size:11px;padding:4px 6px;outline:none;font-family:inherit;width:100%;cursor:pointer;transition:border-color .14s}
    .prec-sel:focus{border-color:#2563EB}
    .prec-chk{display:flex;align-items:center;gap:4px;font-size:10px;color:var(--tx-4);cursor:pointer;margin-top:4px;white-space:nowrap}
    .prec-chk input{accent-color:#2563EB}
    .prec-frete-detail{font-size:10px;color:var(--tx-4);margin-bottom:2px}
    .prec-frete-inp{background:var(--surface-2);border:1.5px solid var(--border);border-radius:6px;color:var(--tx);font-size:11px;padding:3px 6px;outline:none;font-family:inherit;width:80px;text-align:right;margin-top:4px;transition:border-color .14s}
    .prec-frete-inp:focus{border-color:#2563EB}
    .prec-badge{display:inline-flex;padding:2px 8px;border-radius:99px;font-size:10px;font-weight:700;white-space:nowrap}
    .prec-del{background:none;border:none;cursor:pointer;color:var(--tx-4);transition:color .14s;padding:2px;display:flex;align-items:center}
    .prec-del:hover{color:var(--red)}
    .prec-empty{padding:48px 24px;text-align:center;color:var(--tx-4);font-size:13px}
    .prec-empty svg{margin:0 auto 12px;opacity:.3;display:block}
    input::-webkit-outer-spin-button,input::-webkit-inner-spin-button{-webkit-appearance:none}
    input[type=number]{-moz-appearance:textfield}
  `;

  return (
    <div className="prec-wrap">
      <style>{CSS}</style>

      <div className="prec-toolbar">
        <div className="prec-title">
          <Calculator size={16} style={{color:'#2563EB'}}/> Precificação de Produtos
        </div>
        <div className="prec-actions">
          {carregandoDB && (
            <div className="prec-loading">
              <RefreshCw size={12}/> Carregando tabelas ML...
            </div>
          )}
          <button className="prec-btn-add" onClick={add} disabled={carregandoDB}>
            <Plus size={14}/> Adicionar Produto
          </button>
          <button className="prec-btn-exp" onClick={exportar} disabled={!produtos.length}>
            <Download size={14}/> Exportar Excel
          </button>
        </div>
      </div>

      <div className="prec-tbl-wrap">
        <div style={{overflowX:'auto'}}>
          <table className="prec-tbl">
            <thead>
              <tr>
                <th>MLB</th>
                <th style={{minWidth:200}}>Produto</th>
                <th className="r" style={{minWidth:90}}>Custo (R$)</th>
                <th className="r" style={{minWidth:70}}>ACOS (%)</th>
                <th className="r" style={{minWidth:90}}>Preço (R$)</th>
                <th className="r" style={{minWidth:80}}>Desc. (%)</th>
                <th className="r" style={{minWidth:120}}>Taxa/Frete (R$)</th>
                <th className="r" style={{minWidth:80}}>Imp. (%)</th>
                <th className="r" style={{minWidth:100}}>Comissão (%)</th>
                <th className="r" style={{minWidth:90}}>Lucro (R$)</th>
                <th className="r" style={{minWidth:80}}>Margem</th>
                <th style={{minWidth:110}}>Status</th>
                <th style={{minWidth:160}}>Categoria</th>
                <th style={{minWidth:100}}>Anúncio</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {produtos.map((p, i) => (
                <tr key={p.id}>
                  <td>
                    <input className="prec-inp" style={{width:100}} placeholder="MLB..."
                      value={p.mlb} onChange={e => upd(i,'mlb',e.target.value)}/>
                  </td>
                  <td>
                    <input className="prec-inp" style={{width:180}} placeholder="Nome do produto..."
                      value={p.name} onChange={e => upd(i,'name',e.target.value)}/>
                  </td>
                  <td>
                    <input className="prec-inp r" type="number" placeholder="0"
                      value={p.custo||''} onChange={e => upd(i,'custo',parseFloat(e.target.value)||0)}/>
                  </td>
                  <td>
                    <input className="prec-inp r" type="number" placeholder="0"
                      value={p.acos||''} onChange={e => upd(i,'acos',parseFloat(e.target.value)||0)}/>
                  </td>
                  <td>
                    <input className="prec-inp r" type="number" placeholder="0"
                      value={p.preco||''} onChange={e => upd(i,'preco',parseFloat(e.target.value)||0)}/>
                  </td>
                  <td>
                    <input className="prec-inp r" type="number" placeholder="0"
                      value={p.desconto||''} onChange={e => upd(i,'desconto',parseFloat(e.target.value)||0)}/>
                  </td>
                  <td style={{textAlign:'right'}}>
                    <div style={{fontWeight:600,color:'var(--tx)'}}>{fmt2(p.g)}</div>
                    <div className="prec-frete-detail">F: {fmt2(p.frete)} + Fixo: {fmt2(p.custoFixo)}</div>
                    <label className="prec-chk">
                      <input type="checkbox" checked={p.fretePersonalizado}
                        onChange={e => upd(i,'fretePersonalizado',e.target.checked)}/>
                      Frete manual
                    </label>
                    {p.fretePersonalizado && (
                      <input className="prec-frete-inp" type="number" placeholder="0"
                        value={p.frete||''} onChange={e => upd(i,'frete',parseFloat(e.target.value)||0)}/>
                    )}
                  </td>
                  <td>
                    <input className="prec-inp r" type="number" placeholder="0"
                      value={p.imposto||''} onChange={e => upd(i,'imposto',parseFloat(e.target.value)||0)}/>
                  </td>
                  <td style={{textAlign:'right'}}>
                    {p.comissaoPersonalizada ? (
                      <input className="prec-inp r" type="number" step="0.1"
                        value={p.comissao||''} onChange={e => upd(i,'comissao',parseFloat(e.target.value)||0)}/>
                    ) : (
                      <span style={{fontWeight:600,color:'var(--tx)'}}>{fmt2(p.comissao)}%</span>
                    )}
                    <label className="prec-chk" style={{justifyContent:'flex-end'}}>
                      <input type="checkbox" checked={p.comissaoPersonalizada}
                        onChange={e => {
                          upd(i,'comissaoPersonalizada',e.target.checked);
                          if (!e.target.checked) upd(i,'comissao', getComissao(p.categoria, p.tipoAnuncio));
                        }}/>
                      Manual
                    </label>
                  </td>
                  <td style={{textAlign:'right',fontWeight:700,color: p.j>=0 ? 'var(--green)' : 'var(--red)'}}>
                    {fmt2(p.j)}
                  </td>
                  <td style={{textAlign:'right',fontWeight:700,color:statusColor(p.k)}}>
                    {fmt2(p.k)}%
                  </td>
                  <td>
                    <span className="prec-badge" style={{color:statusColor(p.k),background:statusBg(p.k)}}>
                      {p.l || '—'}
                    </span>
                  </td>
                  <td>
                    <select className="prec-sel" value={p.categoria}
                      onChange={e => upd(i,'categoria',e.target.value)}>
                      {categorias.map(c => <option key={c} value={c}>{c}</option>)}
                    </select>
                  </td>
                  <td>
                    <select className="prec-sel" value={p.tipoAnuncio}
                      onChange={e => upd(i,'tipoAnuncio',e.target.value as any)}>
                      <option value="classico">Clássico</option>
                      <option value="premium">Premium</option>
                    </select>
                  </td>
                  <td>
                    <button className="prec-del" onClick={() => del(i)}><Trash2 size={14}/></button>
                  </td>
                </tr>
              ))}
              {!produtos.length && (
                <tr>
                  <td colSpan={15} className="prec-empty">
                    <Calculator size={32}/>
                    {carregandoDB ? 'Carregando tabelas do Mercado Livre...' : 'Adicione um produto para começar a precificação'}
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};