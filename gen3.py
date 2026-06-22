"""
Lote 3 — 16 páginas SEO + hub /guia-mercado-livre/
FAQ blocks, lead forms, links internos, schemas completos
"""
import os, json
from datetime import date

BASE = os.path.join(os.path.dirname(__file__), "public")
SITE = "https://sobrouquantoml.prospectia.space"
TODAY = date.today()
DATE_BR  = TODAY.strftime("%d/%m/%Y")
DATE_ISO = TODAY.isoformat()
SUPABASE_URL = "https://wyqnqiowxhamvxtzedth.supabase.co/functions/v1/capture-lead"

# ── todos os slugs anteriores (para links internos) ──────────────────────────
LOTE1 = [
    "taxas-mercado-livre","comissao-mercado-livre","lucro-real-mercado-livre",
    "dre-para-mei","dre-simples-nacional","dre-lucro-presumido",
    "precificacao-mercado-livre","quanto-mercado-livre-cobra",
    "conciliacao-mercado-livre","fluxo-de-caixa-mercado-livre",
    "margem-de-lucro-mercado-livre",
]
LOTE2 = [
    "erros-precificacao-mercado-livre","produto-no-prejuizo-mercado-livre",
    "capital-de-giro-mercado-livre","impostos-vendedor-mercado-livre",
    "simples-nacional-ou-mei","relatorio-mercado-livre-como-exportar",
    "cmv-mercado-livre","devolucoes-mercado-livre","frete-gratis-mercado-livre",
    "ponto-de-equilibrio-mercado-livre","separar-financas-pessoais-empresariais",
    "reserva-financeira-vendedor-ml","escalar-vendas-mercado-livre",
    "reputacao-mercado-livre","mercado-pago-taxas","quanto-ganhar-mercado-livre",
    "vale-a-pena-vender-mercado-livre","anuncio-full-mercado-livre",
    "ticket-medio-mercado-livre","sazonalidade-mercado-livre",
    "estoque-mercado-livre","buy-box-mercado-livre",
    "planilha-controle-mercado-livre","calcular-imposto-simples-mercado-livre",
    "nota-fiscal-mercado-livre",
]

PAGES = [
    {
        "slug":  "calculadora-margem-mercado-livre",
        "title": "Calculadora de Margem Mercado Livre 2025 | Sobrou Quanto ML",
        "h1":    "Como Calcular a Margem de Lucro no Mercado Livre",
        "tag":   "Calculadora",
        "desc":  "Aprenda a calcular corretamente a margem de lucro nas suas vendas do Mercado Livre. Veja a fórmula, exemplos práticos e como usar uma ferramenta gratuita.",
        "lead":  "Muitos vendedores do Mercado Livre acreditam que estão lucrando, mas na prática estão pagando para vender. Entender a margem de lucro real é o primeiro passo para um negócio sustentável.",
        "cta_title": "Calcule Sua Margem em Segundos",
        "cta_desc":  "Sobrou Quanto ML faz esse cálculo automaticamente. Conecte sua conta e veja quanto sobra de verdade em cada venda.",
        "links": ["taxas-mercado-livre","comissao-mercado-livre","precificacao-mercado-livre","margem-de-lucro-mercado-livre"],
        "faq": [
            ("O que é margem de lucro?", "Margem de lucro é o percentual que sobra do preço de venda após deduzir todos os custos: produto, frete, taxas, impostos e despesas operacionais."),
            ("Qual é uma boa margem de lucro no ML?", "Para produtos de marketplace, uma margem líquida entre 10% e 20% já é considerada saudável. Abaixo de 8% o risco é alto."),
            ("Como calcular a margem bruta?", "Margem bruta = (Preço de venda - CMV) ÷ Preço de venda × 100. Mas atenção: a margem bruta não desconta taxas do ML nem impostos."),
            ("Por que minha margem aparece positiva mas não tenho dinheiro?", "Porque muitos vendedores calculam apenas o custo do produto. É preciso incluir comissão ML, frete, impostos, devoluções e despesas fixas."),
            ("Como melhorar minha margem de lucro no ML?", "Negocie melhor com fornecedores, revise o preço de venda, reduza devoluções e use anúncios apenas quando o ROAS justificar."),
        ],
        "content": """
<h2>Por Que Calcular a Margem no Mercado Livre é Diferente</h2>
<p>Vender no Mercado Livre envolve custos que não existem em outros canais: comissão por categoria (entre 10% e 18%), frete subsidiado, taxa de parcelamento e, nos anúncios Full, custo de fulfillment. Ignorar qualquer um desses itens distorce completamente o resultado.</p>

<h3>A Fórmula Completa da Margem Líquida</h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Componente</th><th>Exemplo (R$)</th></tr></thead>
<tbody>
<tr><td>Preço de venda</td><td>100,00</td></tr>
<tr><td>(-) Comissão ML (16%)</td><td>-16,00</td></tr>
<tr><td>(-) Frete (subsidiado)</td><td>-8,00</td></tr>
<tr><td>(-) Custo do produto (CMV)</td><td>-40,00</td></tr>
<tr><td>(-) Imposto (Simples 6%)</td><td>-6,00</td></tr>
<tr><td>(-) Devolução estimada (2%)</td><td>-2,00</td></tr>
<tr><td><strong>= Margem líquida</strong></td><td><strong>28,00 (28%)</strong></td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p><strong>Dica:</strong> Calcule sempre a margem <em>por SKU</em>, não pela média da loja. Um produto com margem negativa pode estar destruindo o lucro dos outros.</p>
</div>

<h2>Erro Comum: Confundir Faturamento com Lucro</h2>
<p>Faturar R$ 50.000/mês no Mercado Livre não significa lucrar R$ 50.000. Depois de todas as deduções, o lucro líquido de um vendedor típico fica entre 8% e 15% do faturamento bruto. Saiba mais em <a href="/diferenca-faturamento-lucro-mercado-livre/">Diferença entre Faturamento e Lucro</a>.</p>

<h2>Como Automatizar o Cálculo</h2>
<p>Fazer esse cálculo manualmente em cada produto é inviável quando o catálogo cresce. Ferramentas como o Sobrou Quanto ML integram direto com sua conta do Mercado Livre e calculam a margem real de cada venda automaticamente, considerando variações de frete, devoluções e impostos do período.</p>

<h3>Margem por Tipo de Anúncio</h3>
<ul>
<li><strong>Clássico:</strong> menor comissão, menor exposição — ideal para produtos de alta margem</li>
<li><strong>Premium:</strong> maior comissão, melhor posicionamento — exige margem mínima de 18%</li>
<li><strong>Full:</strong> adiciona custo de armazenagem e fulfillment — calcule o break-even antes de migrar</li>
</ul>
"""
    },
    {
        "slug":  "simulador-lucro-mercado-livre",
        "title": "Simulador de Lucro Mercado Livre 2025 | Sobrou Quanto ML",
        "h1":    "Simulador de Lucro para Vendedores do Mercado Livre",
        "tag":   "Simulador",
        "desc":  "Simule o lucro real de qualquer produto antes de anunciar no Mercado Livre. Entenda como taxas, frete e impostos impactam seu resultado final.",
        "lead":  "Antes de anunciar um produto no Mercado Livre, todo vendedor deveria simular o lucro líquido. Uma simulação mal feita é o principal motivo de vendedores lucrarem menos do que imaginam.",
        "cta_title": "Simule o Lucro de Toda Sua Loja",
        "cta_desc":  "Com o Sobrou Quanto ML você tem o simulador completo integrado ao seu histórico de vendas. Veja o que realmente sobra em cada pedido.",
        "links": ["precificacao-mercado-livre","taxas-mercado-livre","calculadora-margem-mercado-livre","quanto-mercado-livre-cobra"],
        "faq": [
            ("Como simular o lucro antes de anunciar?", "Some o custo do produto + frete + comissão ML + imposto estimado + margem de devolução. O que sobrar é seu lucro líquido."),
            ("Qual taxa usar para simular?", "Depende da categoria. Eletrônicos pagam 16%, moda 16%, livros 8%. Verifique a tabela oficial do Mercado Livre para sua categoria."),
            ("Devo incluir o custo do anúncio no simulador?", "Sim, se usar Product Ads ou outros formatos pagos. O custo de publicidade pode reduzir a margem em 3% a 8%."),
            ("Como calcular o imposto na simulação?", "Se for MEI, use 5% sobre o lucro. Simples Nacional varia de 4% a 19,5% dependendo da faixa de faturamento."),
            ("Vale a pena usar Full no simulador?", "Adicione R$ 5 a R$ 15 por unidade para armazenagem e picking. O Full compensa quando o aumento na conversão superar esse custo."),
        ],
        "content": """
<h2>Variáveis Essenciais para uma Boa Simulação</h2>
<p>Uma simulação confiável precisa de pelo menos seis variáveis: custo do produto, frete (origem e destino médio), comissão do ML pela categoria, imposto sobre a receita, taxa de devolução histórica e custo de publicidade se aplicável.</p>

<h3>Planilha Mental de Simulação</h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Item</th><th>% sobre preço</th><th>Exemplo R$100</th></tr></thead>
<tbody>
<tr><td>Preço de venda</td><td>100%</td><td>100,00</td></tr>
<tr><td>Custo do produto</td><td>35-50%</td><td>42,00</td></tr>
<tr><td>Comissão ML</td><td>10-18%</td><td>16,00</td></tr>
<tr><td>Frete</td><td>5-12%</td><td>9,00</td></tr>
<tr><td>Imposto</td><td>4-10%</td><td>6,00</td></tr>
<tr><td>Devolução estimada</td><td>1-4%</td><td>2,00</td></tr>
<tr><td><strong>Lucro líquido</strong></td><td><strong>~25%</strong></td><td><strong>25,00</strong></td></tr>
</tbody>
</table>
</div>

<div class="callout callout-warn">
<p><strong>Atenção:</strong> Frete grátis obrigatório em muitas categorias não é "grátis" para o vendedor — o ML desconta parte do custo da sua comissão. Veja mais em <a href="/frete-gratis-mercado-livre/">Frete Grátis no Mercado Livre</a>.</p>
</div>

<h2>Simulação por Regime Tributário</h2>
<p>O imposto impacta diretamente o lucro. Um MEI paga R$ 75/mês fixo (até R$ 81.000/ano), enquanto no Simples Nacional as alíquotas variam conforme o faturamento acumulado dos últimos 12 meses.</p>

<h2>Quando Recusar um Produto com Base na Simulação</h2>
<p>Se a margem simulada ficar abaixo de 8%, o produto oferece pouco espaço para oscilações. Uma promoção inesperada, um aumento no frete ou uma devolução podem tornar o mês negativo. Use a simulação como filtro antes de comprar estoque.</p>
"""
    },
    {
        "slug":  "como-calcular-comissao-mercado-livre",
        "title": "Como Calcular a Comissão do Mercado Livre 2025 | Guia Completo",
        "h1":    "Como Calcular a Comissão do Mercado Livre em Cada Venda",
        "tag":   "Taxas",
        "desc":  "Entenda como o Mercado Livre cobra comissões por categoria e tipo de anúncio. Calcule exatamente quanto você paga antes de precificar.",
        "lead":  "A comissão do Mercado Livre varia entre 8% e 18% dependendo da categoria. Calcular errado significa precificar errado — e perder dinheiro em cada venda.",
        "cta_title": "Veja Suas Comissões Reais Automaticamente",
        "cta_desc":  "Sobrou Quanto ML mostra exatamente quanto o ML deduziu em cada pedido, agrupado por categoria e mês.",
        "links": ["taxas-mercado-livre","quanto-mercado-livre-cobra","precificacao-mercado-livre","conciliacao-mercado-livre"],
        "faq": [
            ("Como o ML cobra comissão?", "A comissão é calculada sobre o preço de venda do produto e debitada automaticamente no momento do pagamento pelo ML."),
            ("Quais categorias têm menor comissão?", "Livros e materiais educativos têm 8%. Eletrodomésticos, eletrônicos e moda ficam entre 14% e 18%."),
            ("A comissão inclui o frete?", "Não. A comissão é sobre o preço do produto. O frete tem cobrança separada e depende do tipo de envio."),
            ("Anúncio Clássico tem comissão menor?", "Sim, o Clássico cobra 10% na maioria das categorias, enquanto o Premium cobra de 14% a 18%."),
            ("Como saber a comissão exata da minha categoria?", "Acesse a central de ajuda do ML ou use o relatório de vendas que mostra o valor deduzido por pedido."),
        ],
        "content": """
<h2>Tabela de Comissões por Categoria (2025)</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Categoria</th><th>Clássico</th><th>Premium</th></tr></thead>
<tbody>
<tr><td>Livros e Educação</td><td>8%</td><td>8%</td></tr>
<tr><td>Informática</td><td>10%</td><td>16%</td></tr>
<tr><td>Eletrônicos</td><td>10%</td><td>16%</td></tr>
<tr><td>Moda e Acessórios</td><td>10%</td><td>16%</td></tr>
<tr><td>Casa e Jardim</td><td>10%</td><td>16%</td></tr>
<tr><td>Saúde e Beleza</td><td>10%</td><td>16%</td></tr>
<tr><td>Eletrodomésticos</td><td>10%</td><td>18%</td></tr>
<tr><td>Veículos e Peças</td><td>10%</td><td>14%</td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p><strong>Importante:</strong> As comissões podem ser alteradas pelo ML. Sempre consulte a tabela oficial antes de precificar um novo produto.</p>
</div>

<h2>Comissão do Full (Mercado Envios Full)</h2>
<p>Produtos no Full pagam a comissão normal do anúncio Premium (por ser obrigatório) mais uma taxa de armazenagem e picking que varia por tamanho e peso do produto. Calcule esse custo no simulador antes de migrar SKUs para Full.</p>

<h2>Como Acompanhar as Comissões Cobradas</h2>
<p>O relatório de conciliação do ML mostra, por ordem, o valor bruto e o valor líquido após comissão. Mas esse relatório tem limitações — não cruza com dados fiscais nem calcula margem. Para isso, use uma ferramenta de conciliação como o Sobrou Quanto ML. Veja como em <a href="/conciliacao-mercado-livre/">Conciliação no Mercado Livre</a>.</p>
"""
    },
    {
        "slug":  "quanto-custa-vender-mercado-livre",
        "title": "Quanto Custa Vender no Mercado Livre em 2025 | Todos os Custos",
        "h1":    "Quanto Custa Realmente Vender no Mercado Livre",
        "tag":   "Custos",
        "desc":  "Descubra todos os custos de vender no Mercado Livre: comissão, frete, imposto, anúncios e taxas ocultas. Calcule o custo total antes de precificar.",
        "lead":  "Vender no Mercado Livre envolve muito mais do que a comissão da plataforma. Existe o frete, o imposto, o custo do produto, o risco de devolução e o custo de oportunidade do capital parado em estoque.",
        "cta_title": "Veja Seu Custo Real por Venda",
        "cta_desc":  "Sobrou Quanto ML consolida todos os custos automaticamente e mostra o lucro líquido de cada pedido.",
        "links": ["taxas-mercado-livre","comissao-mercado-livre","frete-gratis-mercado-livre","impostos-vendedor-mercado-livre"],
        "faq": [
            ("Quais são todos os custos de vender no ML?", "Comissão (8-18%), frete subsidiado (5-12%), imposto (4-10%), devolução (1-4%), anúncios patrocinados (opcional 3-8%) e custo do produto."),
            ("Tem mensalidade no ML?", "Não há mensalidade fixa para vender no Mercado Livre. Os custos são proporcionais às vendas realizadas."),
            ("Quanto custa o Mercado Envios?", "Depende do peso, tamanho e distância. O ML subsidia parte do frete no Premium; o vendedor cobre a diferença automaticamente."),
            ("O Mercado Pago cobra taxa?", "Sim, há taxa de parcelamento quando o comprador parcela. Pagamentos à vista têm dedução menor."),
            ("Tem custo para criar anúncio?", "Criar o anúncio é gratuito. A cobrança acontece apenas quando a venda é realizada."),
        ],
        "content": """
<h2>Mapa Completo de Custos no Mercado Livre</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">💳</div><h4>Comissão</h4><p>8% a 18% sobre o preço de venda, cobrada por categoria e tipo de anúncio</p></div>
<div class="benefit-card"><div class="b-icon">🚚</div><h4>Frete</h4><p>5% a 12% do preço — varia por região, peso e tipo de envio</p></div>
<div class="benefit-card"><div class="b-icon">📊</div><h4>Imposto</h4><p>4% a 19,5% dependendo do regime tributário e faixa de faturamento</p></div>
<div class="benefit-card"><div class="b-icon">↩️</div><h4>Devoluções</h4><p>1% a 5% do faturamento em devolução — custo direto e custo operacional</p></div>
</div>

<h2>Custo Total Estimado por Produto</h2>
<p>Para um produto vendido a R$ 100, considerando todos os custos exceto o CMV, o vendedor típico paga entre R$ 28 e R$ 40 em deduções. Isso significa que o produto precisa ter CMV máximo de R$ 60 para não operar no prejuízo.</p>

<div class="callout callout-green">
<p><strong>Boas práticas:</strong> Mapeie todos os custos antes de negociar com o fornecedor. O preço de compra máximo é: Preço de venda × (1 - % total de custos) - margem desejada.</p>
</div>

<h2>Custos Ocultos que Todo Vendedor Ignora</h2>
<ul>
<li><strong>Capital em estoque:</strong> dinheiro parado que poderia render em outras aplicações</li>
<li><strong>Tempo de atendimento:</strong> perguntas, reclamações, mediações — valorize seu tempo</li>
<li><strong>Embalagem:</strong> caixa, lacre e etiqueta representam R$ 2 a R$ 8 por pedido</li>
<li><strong>Fraude e contestação:</strong> chargebacks e fraudes impactam 0,5% a 1,5% das vendas</li>
</ul>
"""
    },
    {
        "slug":  "como-aumentar-lucro-mercado-livre",
        "title": "Como Aumentar o Lucro no Mercado Livre em 2025 | 12 Estratégias",
        "h1":    "Como Aumentar o Lucro no Mercado Livre: 12 Estratégias Práticas",
        "tag":   "Estratégia",
        "desc":  "Aprenda 12 estratégias comprovadas para aumentar o lucro nas suas vendas do Mercado Livre sem necessariamente aumentar o faturamento.",
        "lead":  "Faturar mais não é a única forma de lucrar mais. Com as estratégias certas, é possível aumentar o lucro do Mercado Livre reduzindo custos, melhorando o mix de produtos e automatizando processos.",
        "cta_title": "Descubra Onde Está Perdendo Lucro",
        "cta_desc":  "Sobrou Quanto ML identifica os produtos e períodos com menor margem e ajuda você a tomar decisões baseadas em dados.",
        "links": ["margem-de-lucro-mercado-livre","precificacao-mercado-livre","produto-no-prejuizo-mercado-livre","escalar-vendas-mercado-livre"],
        "faq": [
            ("Como aumentar lucro sem aumentar vendas?", "Negocie custos com fornecedores, revise precificação, elimine produtos com margem negativa e reduza devolução."),
            ("Qual categoria tem maior margem no ML?", "Acessórios eletrônicos, cosméticos e produtos de nicho costumam ter margens mais altas (25-40%) do que eletrônicos."),
            ("Vale a pena vender barato para girar estoque?", "Apenas se o estoque estiver parado há mais de 60 dias. Vender no prejuízo para liberar capital pode ser estratégico em casos específicos."),
            ("Como o buy box afeta o lucro?", "Ganhar o buy box aumenta conversão sem aumentar custo — melhora o volume com a mesma margem. Veja mais em buy box ML."),
            ("Devo focar em poucos produtos com alta margem ou muitos com baixa?", "Depende do seu modelo. Menos SKUs com alta margem são mais fáceis de gerir. Muitos SKUs exigem mais capital e operação."),
        ],
        "content": """
<h2>12 Estratégias Para Aumentar o Lucro no ML</h2>

<h3>1. Elimine Produtos com Margem Negativa</h3>
<p>Antes de qualquer otimização, identifique quais produtos estão no prejuízo. Um único SKU vendendo muito com margem negativa pode estar destruindo meses de lucro dos outros. Use relatórios de conciliação para essa análise.</p>

<h3>2. Renegocie com Fornecedores Anualmente</h3>
<p>Fornecedores esperam renegociação. Apresente volume acumulado e peça desconto progressivo. Uma redução de 5% no CMV pode dobrar a margem de produtos com custo alto.</p>

<h3>3. Revise a Precificação Por Categoria</h3>
<p>Categorias com menor comissão permitem preços mais competitivos. Se você vende em múltiplas categorias, priorize as que deixam mais margem.</p>

<h3>4. Reduza a Taxa de Devolução</h3>
<p>Cada devolução custa duplamente: o produto volta (às vezes danificado) e você não recebe. Fotos detalhadas, descrição precisa e embalagem adequada reduzem devoluções em até 40%.</p>

<h3>5. Melhore o Ticket Médio</h3>
<p>Kits e combos aumentam o ticket com custo marginal menor. Um kit de R$ 150 tem menos custo de envio proporcional do que dois pedidos de R$ 75.</p>

<div class="callout">
<p><strong>Leitura relacionada:</strong> Veja <a href="/ticket-medio-mercado-livre/">Como Aumentar o Ticket Médio no ML</a> para estratégias detalhadas.</p>
</div>

<h3>6 a 12: Automatize, Analise e Escale</h3>
<ul>
<li>Use reprecificador automático para manter margens em períodos de promoção</li>
<li>Analise sazonalidade e compre estoque com antecedência para preços melhores</li>
<li>Consolide o DRE mensal para visualizar tendências de margem</li>
<li>Migre produtos de alto giro para Full (pode aumentar conversão sem reduzir margem se o volume compensar)</li>
<li>Reduza custos de embalagem comprando em volume</li>
<li>Automatize atendimento de perguntas frequentes para reduzir custo operacional</li>
<li>Analise o ROI de cada campanha de Product Ads mensalmente</li>
</ul>
"""
    },
    {
        "slug":  "receita-liquida-mercado-livre",
        "title": "Receita Líquida no Mercado Livre: O Que É e Como Calcular | 2025",
        "h1":    "Receita Líquida no Mercado Livre: Como Calcular Corretamente",
        "tag":   "Financeiro",
        "desc":  "Entenda a diferença entre receita bruta e receita líquida no Mercado Livre e saiba como calcular o valor correto para seu DRE e gestão financeira.",
        "lead":  "Receita bruta e receita líquida são conceitos diferentes — e confundi-los é um dos erros mais comuns em gestão financeira de vendedores do Mercado Livre.",
        "cta_title": "DRE Automático com Receita Líquida Calculada",
        "cta_desc":  "Sobrou Quanto ML gera seu DRE com receita bruta, deduções e receita líquida separadas — tudo integrado com sua conta ML.",
        "links": ["dre-para-mei","dre-simples-nacional","faturamento-mercado-livre","diferenca-faturamento-lucro-mercado-livre"],
        "faq": [
            ("O que é receita líquida?", "Receita líquida = receita bruta - devoluções - abatimentos - impostos incidentes sobre a venda (como PIS/COFINS no Lucro Presumido)."),
            ("Qual usar no DRE: bruta ou líquida?", "O DRE começa pela receita bruta e deduz itens até chegar na líquida. Ambas aparecem no demonstrativo."),
            ("Como calcular receita líquida no ML?", "Receita bruta (total de vendas) menos devoluções, menos impostos sobre receita (PIS/COFINS se aplicável) = receita líquida."),
            ("No Simples Nacional existe PIS/COFINS?", "No Simples, PIS/COFINS são incluídos na alíquota unificada do DAS. Então a receita bruta já é a base do cálculo simplificado."),
            ("Por que minha receita líquida é menor que esperado?", "Pode ser por alto índice de devolução, descontos em campanhas do ML ou erros na conciliação. Revise o relatório financeiro."),
        ],
        "content": """
<h2>Estrutura do DRE: Da Receita Bruta ao Lucro Líquido</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Linha do DRE</th><th>Descrição</th></tr></thead>
<tbody>
<tr><td>Receita Bruta</td><td>Total de vendas pelo preço cheio</td></tr>
<tr><td>(-) Devoluções</td><td>Pedidos cancelados e reembolsados</td></tr>
<tr><td>(-) Abatimentos</td><td>Descontos concedidos em disputas</td></tr>
<tr><td>(-) Impostos s/ receita</td><td>PIS/COFINS (Presumido) ou parcela DAS (Simples)</td></tr>
<tr><td><strong>= Receita Líquida</strong></td><td><strong>Base para cálculo do resultado operacional</strong></td></tr>
<tr><td>(-) CMV</td><td>Custo das mercadorias vendidas</td></tr>
<tr><td><strong>= Lucro Bruto</strong></td><td></td></tr>
<tr><td>(-) Despesas operacionais</td><td>Comissão ML, frete, salários, aluguel</td></tr>
<tr><td><strong>= EBITDA / Lucro Operacional</strong></td><td></td></tr>
</tbody>
</table>
</div>

<h2>Regime Tributário e Receita Líquida</h2>
<p>No <strong>Lucro Presumido</strong>, PIS (0,65%) e COFINS (3%) incidem sobre a receita bruta e devem ser deduzidos para chegar na líquida. No <strong>Simples Nacional</strong>, esses tributos fazem parte da alíquota do DAS, então a dinâmica é diferente. Para MEI, não há DRE formal obrigatório, mas organizar as receitas facilita a gestão.</p>

<div class="callout callout-green">
<p>Quer entender o DRE completo para cada regime? Veja: <a href="/dre-para-mei/">DRE para MEI</a>, <a href="/dre-simples-nacional/">DRE Simples Nacional</a> e <a href="/dre-lucro-presumido/">DRE Lucro Presumido</a>.</p>
</div>
"""
    },
    {
        "slug":  "gestao-financeira-vendedor-mercado-livre",
        "title": "Gestão Financeira para Vendedores do Mercado Livre 2025 | Guia",
        "h1":    "Gestão Financeira para Vendedores do Mercado Livre: Guia Completo",
        "tag":   "Gestão",
        "desc":  "Aprenda a organizar as finanças da sua loja no Mercado Livre. DRE, fluxo de caixa, conciliação e controle de estoque em um guia prático.",
        "lead":  "A maioria dos vendedores do Mercado Livre gerencia as finanças de cabeça ou em planilhas improvisadas. Com uma gestão estruturada, fica muito mais fácil crescer com segurança.",
        "cta_title": "Gestão Financeira Automatizada Para Sua Loja",
        "cta_desc":  "Sobrou Quanto ML integra com sua conta ML e organiza DRE, fluxo de caixa e conciliação automaticamente.",
        "links": ["fluxo-de-caixa-mercado-livre","dre-para-mei","conciliacao-mercado-livre","separar-financas-pessoais-empresariais"],
        "faq": [
            ("Por onde começar a gestão financeira?", "Comece separando conta bancária PJ, depois monte o fluxo de caixa básico e por fim implante o DRE mensal."),
            ("Com que frequência revisar as finanças?", "Fluxo de caixa: semanal. DRE: mensal. Conciliação: depois de cada período de repasse do ML."),
            ("Preciso de contador para vender no ML?", "MEI não precisa, mas é recomendável. Simples Nacional e Presumido precisam de contador para obrigações fiscais."),
            ("Como saber se minha loja está crescendo de forma saudável?", "Acompanhe margem líquida, capital de giro, giro de estoque e inadimplência (devoluções). Crescimento com margem estável é saudável."),
            ("Qual ferramenta usar para gestão financeira do ML?", "Planilha para começar, mas migre para uma ferramenta integrada com o ML quando o volume de pedidos superar 50/mês."),
        ],
        "content": """
<h2>Os 4 Pilares da Gestão Financeira no ML</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">📊</div><h4>DRE Mensal</h4><p>Receitas, custos e despesas organizados — mostra se a loja lucrou no período</p></div>
<div class="benefit-card"><div class="b-icon">💰</div><h4>Fluxo de Caixa</h4><p>Quando o dinheiro entra e sai — evita falta de capital para comprar estoque</p></div>
<div class="benefit-card"><div class="b-icon">🔄</div><h4>Conciliação</h4><p>Cruzamento das vendas do ML com os repasses recebidos — detecta erros e cobranças indevidas</p></div>
<div class="benefit-card"><div class="b-icon">📦</div><h4>Controle de Estoque</h4><p>CMV correto e giro de estoque — evita capital parado e ruptura de vendas</p></div>
</div>

<h2>Rotina Financeira Recomendada</h2>
<h3>Semanal</h3>
<ul>
<li>Conferir repasses recebidos do Mercado Pago</li>
<li>Registrar compras de estoque e despesas operacionais</li>
<li>Monitorar devoluções abertas</li>
</ul>

<h3>Mensal</h3>
<ul>
<li>Fechar o DRE do mês anterior</li>
<li>Conciliar todas as vendas com os extratos do ML</li>
<li>Calcular CMV real (não estimado)</li>
<li>Revisar margem por produto e categoria</li>
<li>Emitir DAS (Simples) ou recolher outros tributos</li>
</ul>

<div class="callout">
<p><strong>Leitura recomendada:</strong> <a href="/separar-financas-pessoais-empresariais/">Por que Separar Finanças Pessoais e Empresariais</a> — o primeiro passo para uma gestão profissional.</p>
</div>

<h2>Automação da Gestão Financeira</h2>
<p>Quando o volume de pedidos cresce, gerenciar tudo manualmente se torna inviável. Uma ferramenta que integre diretamente com o Mercado Livre e gere DRE, fluxo de caixa e conciliação automaticamente economiza horas por semana e reduz erros.</p>
"""
    },
    {
        "slug":  "faturamento-mercado-livre",
        "title": "Faturamento no Mercado Livre: Como Calcular e Aumentar em 2025",
        "h1":    "Faturamento no Mercado Livre: Tudo que Você Precisa Saber",
        "tag":   "Faturamento",
        "desc":  "Entenda como calcular, acompanhar e aumentar o faturamento da sua loja no Mercado Livre. Dicas práticas e métricas essenciais para vendedores.",
        "lead":  "Faturamento é a métrica mais visível no Mercado Livre, mas não é a mais importante. Entender como ele é composto ajuda a tomar decisões mais precisas de crescimento.",
        "cta_title": "Acompanhe Seu Faturamento com Precisão",
        "cta_desc":  "Sobrou Quanto ML mostra faturamento bruto, líquido e lucro em um painel unificado — conectado à sua conta ML.",
        "links": ["receita-liquida-mercado-livre","diferenca-faturamento-lucro-mercado-livre","escalar-vendas-mercado-livre","dre-para-mei"],
        "faq": [
            ("O que compõe o faturamento no ML?", "Faturamento bruto = soma de todos os pedidos aprovados pelo preço de venda. Não desconta devoluções ou taxas."),
            ("Faturamento do ML conta para o limite do MEI?", "Sim. Todo faturamento do ML conta para o teto de R$ 81.000/ano do MEI. Ao superar, precisa migrar para Simples Nacional."),
            ("Como aumentar faturamento sem reduzir preço?", "Aumente o mix de produtos, melhore as fotos, otimize títulos, use kits e combos, e ative anúncios patrocinados estrategicamente."),
            ("Faturamento no ML é receita bruta ou líquida?", "O relatório do ML mostra o valor bruto dos pedidos. A receita líquida só aparece após deduzir comissões e devoluções."),
            ("Como acompanhar faturamento em tempo real?", "Use o painel do vendedor ML ou integre com uma ferramenta de BI que consuma a API do Mercado Livre."),
        ],
        "content": """
<h2>Faturamento vs Receita Líquida vs Lucro</h2>
<p>Esses três números são completamente diferentes. Muitos vendedores comemoram o faturamento sem perceber que a receita líquida — depois de devoluções e impostos — é bem menor, e o lucro pode ser uma fração disso.</p>

<div class="table-wrapper">
<table>
<thead><tr><th>Métrica</th><th>O que é</th><th>Exemplo</th></tr></thead>
<tbody>
<tr><td>Faturamento Bruto</td><td>Total de vendas aprovadas</td><td>R$ 50.000</td></tr>
<tr><td>Receita Líquida</td><td>Bruto - devoluções - impostos diretos</td><td>R$ 45.000</td></tr>
<tr><td>Lucro Bruto</td><td>Líquida - CMV</td><td>R$ 22.500</td></tr>
<tr><td>Lucro Líquido</td><td>Bruto - todas as despesas operacionais</td><td>R$ 7.500</td></tr>
</tbody>
</table>
</div>

<h2>Teto de Faturamento por Regime</h2>
<ul>
<li><strong>MEI:</strong> até R$ 81.000/ano — ultrapassar obriga migração para Simples</li>
<li><strong>Simples Nacional:</strong> até R$ 4,8 milhões/ano</li>
<li><strong>Lucro Presumido:</strong> até R$ 78 milhões/ano</li>
</ul>

<div class="callout callout-warn">
<p><strong>Atenção MEI:</strong> O ML repassa o faturamento para o Mercado Pago. Esse valor conta 100% para o limite anual do MEI, mesmo que parte seja devolvida depois. Monitore mensalmente para não extrapolar sem planejamento.</p>
</div>

<h2>Estratégias Para Crescer o Faturamento de Forma Sustentável</h2>
<p>Crescer faturamento sem crescer a margem é armadilha. Foque em aumentar o faturamento dos produtos com maior margem, usando dados do DRE para identificar quais produtos merecem mais investimento em publicidade. Para mais detalhes, veja <a href="/escalar-vendas-mercado-livre/">Como Escalar Vendas no ML</a>.</p>
"""
    },
    {
        "slug":  "guia-iniciante-mercado-livre",
        "title": "Guia do Iniciante no Mercado Livre 2025 | Comece a Vender Certo",
        "h1":    "Guia do Iniciante para Vender no Mercado Livre em 2025",
        "tag":   "Iniciante",
        "desc":  "Guia completo para quem está começando a vender no Mercado Livre. Aprenda sobre taxas, precificação, frete, impostos e como organizar as finanças.",
        "lead":  "Começar a vender no Mercado Livre é simples, mas começar de forma financeiramente estruturada faz toda a diferença entre uma loja que escala e uma que fecha nos primeiros seis meses.",
        "cta_title": "Comece Com as Finanças Organizadas",
        "cta_desc":  "Sobrou Quanto ML foi criado para vendedores do ML que querem saber exatamente quanto sobra de cada venda. 7 dias grátis.",
        "links": ["taxas-mercado-livre","precificacao-mercado-livre","impostos-vendedor-mercado-livre","separar-financas-pessoais-empresariais"],
        "faq": [
            ("Precisa de CNPJ para vender no ML?", "Não para começar. Você pode vender como pessoa física, mas há limites de faturamento e a carga tributária é maior. Recomenda-se abrir MEI."),
            ("Qual o valor mínimo para começar a vender?", "Não há valor mínimo de cadastro. Mas para operar de forma estruturada, planeje ter capital inicial de pelo menos 2x o custo do estoque inicial."),
            ("Como evitar os erros mais comuns de iniciantes?", "Não precificar considerando todos os custos, não separar conta PJ, não monitorar devoluções e não ter reserva financeira são os erros mais frequentes."),
            ("Quando migrar de MEI para Simples Nacional?", "Quando o faturamento anual ultrapassar R$ 81.000 ou quando precisar emitir nota fiscal de produto (MEI não pode para todos os casos)."),
            ("Como escolher os primeiros produtos para vender?", "Priorize produtos com margem acima de 20%, giro rápido, baixo risco de devolução e fornecedor confiável. Evite eletrônicos no início."),
        ],
        "content": """
<h2>O Que Você Precisa Saber Antes de Anunciar</h2>
<p>Antes de criar o primeiro anúncio, entenda os custos. Muitos iniciantes precificam olhando apenas para o custo do produto e a comissão do ML, ignorando frete, impostos, devoluções e capital de giro.</p>

<h3>Checklist do Vendedor Iniciante</h3>
<ul>
<li>Abrir conta PJ (MEI é suficiente no início)</li>
<li>Abrir conta bancária separada para a loja</li>
<li>Calcular o custo total por produto (CMV + frete + comissão + imposto)</li>
<li>Definir margem mínima aceitável (recomendo pelo menos 15%)</li>
<li>Montar planilha básica de fluxo de caixa</li>
<li>Cadastrar produtos com fotos de qualidade e título otimizado</li>
</ul>

<h2>Entendendo as Taxas do ML Para Iniciantes</h2>
<p>O Mercado Livre cobra comissão apenas quando a venda acontece. Não há mensalidade. As taxas variam por categoria e tipo de anúncio. Para uma visão completa, veja <a href="/taxas-mercado-livre/">Taxas do Mercado Livre</a>.</p>

<div class="callout">
<p><strong>Erro clássico do iniciante:</strong> calcular o preço como "custo + 30% = preço de venda". Na prática, 30% de margem bruta vira 5% de lucro líquido depois de todas as deduções. Sempre calcule de trás para frente: comece pela margem desejada e determine o preço mínimo de venda.</p>
</div>

<h2>Quando Contratar Ajuda Profissional</h2>
<p>No início, MEI consegue gerenciar sozinho. Mas quando o faturamento superar R$ 40.000/mês, considere contratar um contador especializado em e-commerce para evitar problemas com Receita Federal e otimizar a carga tributária.</p>
"""
    },
    {
        "slug":  "como-saber-se-estou-lucrando-mercado-livre",
        "title": "Como Saber Se Estou Lucrando no Mercado Livre | Guia 2025",
        "h1":    "Como Saber Se Está Realmente Lucrando no Mercado Livre",
        "tag":   "Diagnóstico",
        "desc":  "Descubra como identificar se sua loja no Mercado Livre está dando lucro de verdade. Métricas, sinais de alerta e como calcular o resultado real.",
        "lead":  "Muitos vendedores do Mercado Livre têm a sensação de que estão ganhando dinheiro, mas quando calculam tudo, descobrem que o caixa nunca cresce. Esse guia explica como diagnosticar o resultado real.",
        "cta_title": "Descubra Agora Se Está Lucrando",
        "cta_desc":  "Sobrou Quanto ML conecta na sua conta e mostra o resultado real de cada mês — sem planilha, sem estimativa.",
        "links": ["margem-de-lucro-mercado-livre","produto-no-prejuizo-mercado-livre","fluxo-de-caixa-mercado-livre","gestao-financeira-vendedor-mercado-livre"],
        "faq": [
            ("Como saber se estou no lucro ou no prejuízo?", "Some todas as entradas do mês e subtraia: CMV, comissões, frete, impostos, devoluções e despesas operacionais. O resultado é seu lucro ou prejuízo."),
            ("Por que vendo muito mas não tenho dinheiro?", "Pode ser capital de giro mal dimensionado, reinvestimento constante em estoque ou margem muito apertada. Analise o fluxo de caixa, não só o DRE."),
            ("Quais sinais indicam que estou no prejuízo?", "Conta bancária não crescendo, precisar de dinheiro pessoal para comprar estoque, dívidas com fornecedores crescendo."),
            ("Com que frequência devo calcular o lucro?", "Mensalmente no mínimo. Semanalmente se o volume for alto ou a margem apertada."),
            ("Como separar meu salário do lucro da loja?", "Defina um pró-labore fixo (o que você 'pagaria' a um funcionário no seu lugar). O que sobrar depois disso é lucro real da empresa."),
        ],
        "content": """
<h2>Sintomas de Uma Loja Que Não Está Lucrando</h2>
<ul>
<li>O saldo da conta bancária fica igual ou diminui mesmo com vendas crescendo</li>
<li>Você precisa de dinheiro pessoal para reabastecer estoque</li>
<li>Não consegue se pagar um salário da loja</li>
<li>Qualquer promoção ou devolução "quebra" o mês</li>
</ul>

<h2>O Teste do Lucro Real</h2>
<p>Faça esse cálculo para o mês anterior:</p>
<div class="table-wrapper">
<table>
<thead><tr><th>Item</th><th>Como calcular</th></tr></thead>
<tbody>
<tr><td>Receita bruta</td><td>Total de vendas pagas pelo ML</td></tr>
<tr><td>(-) Devoluções</td><td>Valor devolvido no período</td></tr>
<tr><td>(-) Comissão ML</td><td>Ver extrato do ML</td></tr>
<tr><td>(-) Frete cobrado</td><td>Ver extrato do ML</td></tr>
<tr><td>(-) CMV</td><td>Custo das mercadorias vendidas no mês</td></tr>
<tr><td>(-) Impostos</td><td>DAS emitido ou imposto pago</td></tr>
<tr><td>(-) Despesas fixas</td><td>Aluguel, internet, salários, ferramentas</td></tr>
<tr><td><strong>= Lucro ou Prejuízo</strong></td><td><strong>Se negativo, há um problema a resolver</strong></td></tr>
</tbody>
</table>
</div>

<div class="callout callout-warn">
<p><strong>Cuidado com o Mercado Pago:</strong> O repasse do ML não é imediato. Seu caixa pode parecer positivo enquanto ainda há pedidos a conciliar. Sempre cruze o extrato do ML com as vendas do período.</p>
</div>

<h2>Próximos Passos se Estiver no Prejuízo</h2>
<p>Identificou prejuízo? O primeiro passo é descobrir onde está o "vazamento": produto com margem negativa, frete acima do esperado, devolução acima da média ou custo fixo desproporcional. Leia <a href="/produto-no-prejuizo-mercado-livre/">Produto no Prejuízo no ML</a> para uma análise detalhada.</p>
"""
    },
    {
        "slug":  "quanto-sobra-venda-mercado-livre",
        "title": "Quanto Sobra de Cada Venda no Mercado Livre? | Cálculo Real 2025",
        "h1":    "Quanto Sobra de Cada Venda no Mercado Livre?",
        "tag":   "Cálculo",
        "desc":  "Descubra quanto realmente sobra de cada venda no Mercado Livre após deduzir comissão, frete, imposto e custo do produto. Exemplos práticos por categoria.",
        "lead":  "A resposta honesta: depende. Para um produto de R$ 100 em eletrônicos, pode sobrar entre R$ 8 e R$ 25. Para acessórios de moda, entre R$ 20 e R$ 40. Entenda os fatores que fazem essa diferença.",
        "cta_title": "Calcule o Que Sobra em Cada Pedido",
        "cta_desc":  "Sobrou Quanto ML faz esse cálculo automaticamente para todas as suas vendas. Conecte e veja o resultado real.",
        "links": ["margem-de-lucro-mercado-livre","calculadora-margem-mercado-livre","taxas-mercado-livre","conciliacao-mercado-livre"],
        "faq": [
            ("Quanto sobra em média de uma venda no ML?", "Em média, entre 10% e 25% do preço de venda — dependendo da categoria, regime tributário e eficiência operacional."),
            ("Por que às vezes não sobra nada?", "Geralmente por precificação incorreta que não considera todos os custos, ou por frete acima do estimado em vendas para regiões distantes."),
            ("Como aumentar o que sobra por venda?", "Reduza CMV negociando com fornecedor, escolha categorias com menor comissão, reduza devoluções e controle despesas fixas."),
            ("O frete consome muito da margem?", "Sim, especialmente para produtos leves ou de baixo valor. Um produto de R$ 30 pode ter R$ 8 de frete — 27% só nisso."),
            ("Como calcular quanto sobra antes de anunciar?", "Fórmula: Preço - (CMV + comissão ML + frete estimado + imposto + % devolução) = O que sobra."),
        ],
        "content": """
<h2>Exemplos Reais: Quanto Sobra Por Categoria</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Categoria</th><th>Preço</th><th>Comissão</th><th>Frete</th><th>CMV</th><th>Imposto</th><th>Sobra</th></tr></thead>
<tbody>
<tr><td>Eletrônicos</td><td>R$200</td><td>R$32</td><td>R$15</td><td>R$110</td><td>R$12</td><td><strong>R$31 (15%)</strong></td></tr>
<tr><td>Moda</td><td>R$80</td><td>R$13</td><td>R$8</td><td>R$25</td><td>R$5</td><td><strong>R$29 (36%)</strong></td></tr>
<tr><td>Casa e Jardim</td><td>R$120</td><td>R$19</td><td>R$12</td><td>R$55</td><td>R$7</td><td><strong>R$27 (22%)</strong></td></tr>
<tr><td>Livros</td><td>R$50</td><td>R$4</td><td>R$7</td><td>R$20</td><td>R$3</td><td><strong>R$16 (32%)</strong></td></tr>
</tbody>
</table>
</div>

<p><em>Valores estimados para anúncio Premium + Simples Nacional + frete para região sudeste.</em></p>

<h2>O Que Mais Impacta o Que Sobra</h2>
<ul>
<li><strong>Categoria:</strong> comissão varia de 8% a 18% — a maior diferença unitária</li>
<li><strong>Regime tributário:</strong> MEI paga fixo; Simples varia; Presumido pode ser alto</li>
<li><strong>Peso do produto:</strong> produtos pesados têm frete maior, corroendo mais margem</li>
<li><strong>Taxa de devolução:</strong> cada 1% de devolução reduz a margem efetiva em 1%+</li>
</ul>

<div class="callout">
<p>Quer ver exatamente quanto sobrou em cada venda do mês passado? Conecte sua conta no <strong>Sobrou Quanto ML</strong> e veja o relatório completo.</p>
</div>
"""
    },
    {
        "slug":  "como-reduzir-taxas-mercado-livre",
        "title": "Como Reduzir as Taxas do Mercado Livre em 2025 | Guia Prático",
        "h1":    "Como Reduzir as Taxas do Mercado Livre Legalmente",
        "tag":   "Taxas",
        "desc":  "Aprenda estratégias legais para reduzir as taxas pagas ao Mercado Livre e aumentar sua margem de lucro. Dicas práticas de vendedores experientes.",
        "lead":  "Não é possível negociar as taxas diretamente com o Mercado Livre, mas existem estratégias legítimas para reduzir o impacto das comissões na sua margem.",
        "cta_title": "Monitore Suas Taxas em Tempo Real",
        "cta_desc":  "Sobrou Quanto ML mostra exatamente quanto você paga em taxas por produto, categoria e mês — para que você possa tomar decisões baseadas em dados.",
        "links": ["taxas-mercado-livre","comissao-mercado-livre","quanto-custa-vender-mercado-livre","precificacao-mercado-livre"],
        "faq": [
            ("Dá para negociar taxas com o ML?", "Não diretamente. Mas grandes vendedores podem ter acesso a programas especiais. A maioria das otimizações vem da escolha de categoria e tipo de anúncio."),
            ("Anúncio Clássico sempre compensa?", "Não. O Premium tem maior visibilidade e conversão. Compare o custo extra (6-8%) com o ganho em volume para decidir."),
            ("Como o frete grátis impacta as taxas?", "O frete grátis obrigatório em Premium aumenta o custo total. Em alguns produtos, compensar o frete eleva o preço e reduz conversão."),
            ("Usar Full aumenta ou reduz taxas totais?", "Aumenta a taxa absoluta (Full obriga Premium + fulfillment), mas pode reduzir o custo unitário se o aumento de conversão for suficiente."),
            ("Categorizar errado aumenta taxa?", "Sim. Se você categorizar um produto em uma categoria mais cara por engano, paga comissão maior. Revise a categoria de cada anúncio."),
        ],
        "content": """
<h2>Estratégias Para Reduzir o Impacto das Taxas</h2>

<h3>1. Escolha o Tipo de Anúncio Correto</h3>
<p>Anúncios Clássicos pagam entre 10% e 12% de comissão. Premium paga de 14% a 18%. Analise se a diferença de conversão justifica o custo adicional por SKU.</p>

<h3>2. Revise a Categoria de Cada Produto</h3>
<p>Muitos vendedores deixam o ML categorizar automaticamente — o que pode resultar em comissões incorretas. Verifique manualmente os produtos com maior volume.</p>

<h3>3. Otimize o Preço Para o Frete Grátis</h3>
<p>Em vez de absorver o frete como custo, inclua-o no preço de venda quando possível. Em categorias com frete grátis obrigatório, o preço mínimo viável sobe proporcionalmente.</p>

<div class="callout">
<p><strong>Dica:</strong> Use a ferramenta de simulação do ML para comparar o custo de Clássico vs Premium antes de mudar o tipo do anúncio em produtos de alto volume.</p>
</div>

<h3>4. Controle as Devoluções</h3>
<p>Cada devolução "devolve" a comissão paga, mas você também perde o frete e às vezes o produto. O impacto real é maior que a comissão devolvida. Investir em descrições melhores e embalagens adequadas reduz devoluções diretamente.</p>

<h3>5. Foque no Ticket Médio</h3>
<p>A comissão é percentual, mas o frete tem uma parte fixa. Um pedido de R$ 200 paga comissão proporcionalmente igual a dois pedidos de R$ 100, mas paga frete uma única vez. Aumentar o ticket médio dilui o custo fixo de frete. Veja mais em <a href="/ticket-medio-mercado-livre/">Ticket Médio no ML</a>.</p>
"""
    },
    {
        "slug":  "diferenca-faturamento-lucro-mercado-livre",
        "title": "Diferença Entre Faturamento e Lucro no Mercado Livre | 2025",
        "h1":    "Faturamento vs Lucro no Mercado Livre: Qual a Diferença Real?",
        "tag":   "Conceitos",
        "desc":  "Entenda a diferença entre faturamento e lucro para vendedores do Mercado Livre. Por que faturar R$ 100 mil não significa lucrar R$ 100 mil.",
        "lead":  "Faturamento é o total de vendas. Lucro é o que sobra depois de pagar tudo. No Mercado Livre, a diferença entre os dois pode ser enorme — e ignorar isso é o erro financeiro mais comum.",
        "cta_title": "Veja Seu Lucro Real (Não Só o Faturamento)",
        "cta_desc":  "Sobrou Quanto ML separa automaticamente faturamento bruto, receita líquida e lucro real em um painel unificado.",
        "links": ["receita-liquida-mercado-livre","margem-de-lucro-mercado-livre","faturamento-mercado-livre","dre-para-mei"],
        "faq": [
            ("Qual a diferença entre faturamento e lucro?", "Faturamento é o total de vendas. Lucro é o que sobra após pagar CMV, impostos, comissões, frete e despesas operacionais."),
            ("Por que meu faturamento cresceu mas meu lucro não?", "Pode ser expansão de custos proporcionalmente maior, queda de margem por competição de preço ou aumento de despesas fixas."),
            ("O que é margem líquida?", "Margem líquida = lucro líquido ÷ faturamento × 100. Indica quanto de cada real faturado se converte em lucro."),
            ("Faturamento importa mais que lucro?", "Para investidores externos e bancos, faturamento é relevante. Para a saúde do negócio, lucro e fluxo de caixa são mais importantes."),
            ("Como calcular o lucro real no ML?", "Faturamento - comissão ML - frete - CMV - impostos - despesas fixas = lucro líquido."),
        ],
        "content": """
<h2>O Mito dos R$ 100 Mil de Faturamento</h2>
<p>Um vendedor que fatura R$ 100.000/mês no Mercado Livre, em categorias típicas, tem aproximadamente:</p>
<div class="table-wrapper">
<table>
<thead><tr><th>Dedução</th><th>% médio</th><th>Valor (R$)</th></tr></thead>
<tbody>
<tr><td>Custo do produto (CMV)</td><td>45%</td><td>-45.000</td></tr>
<tr><td>Comissão ML</td><td>15%</td><td>-15.000</td></tr>
<tr><td>Frete</td><td>8%</td><td>-8.000</td></tr>
<tr><td>Impostos (Simples 6%)</td><td>6%</td><td>-6.000</td></tr>
<tr><td>Despesas fixas</td><td>5%</td><td>-5.000</td></tr>
<tr><td>Devoluções e perdas</td><td>3%</td><td>-3.000</td></tr>
<tr><td><strong>Lucro líquido estimado</strong></td><td><strong>18%</strong></td><td><strong>+18.000</strong></td></tr>
</tbody>
</table>
</div>

<div class="callout callout-green">
<p>18% de margem líquida é um bom resultado. Muitos vendedores operam com 5% a 10% — o que significa que faturar R$ 100 mil gera apenas R$ 5.000 a R$ 10.000 de lucro real.</p>
</div>

<h2>Por Que Crescer o Faturamento Pode Reduzir o Lucro</h2>
<p>Em regimes como o Simples Nacional, o aumento de faturamento acumulado pode elevar a alíquota aplicável na faixa seguinte. Um salto de R$ 720 mil para R$ 900 mil/ano pode aumentar a alíquota de 8,45% para 10,45% — reduzindo a margem mesmo com mais vendas.</p>

<p>Para planejar o crescimento correto, veja <a href="/simples-nacional-ou-mei/">Simples Nacional ou MEI: Qual Escolher</a>.</p>
"""
    },
    {
        "slug":  "planilha-dre-mercado-livre",
        "title": "Planilha DRE para Mercado Livre Grátis 2025 | Download e Guia",
        "h1":    "Planilha DRE para Mercado Livre: Como Montar e Usar",
        "tag":   "DRE",
        "desc":  "Aprenda como montar uma planilha DRE para sua loja do Mercado Livre. Estrutura completa, fórmulas e como automatizar com ferramentas integradas.",
        "lead":  "Uma planilha DRE bem estruturada é o primeiro passo para entender se sua loja no Mercado Livre é realmente lucrativa. Veja como montar do zero ou automatizar.",
        "cta_title": "DRE Automático — Sem Planilha",
        "cta_desc":  "Sobrou Quanto ML gera o DRE da sua loja automaticamente, conectado à sua conta ML. Sem copiar dados, sem fórmula manual.",
        "links": ["dre-para-mei","dre-simples-nacional","dre-lucro-presumido","relatorio-mercado-livre-como-exportar"],
        "faq": [
            ("O que deve ter na planilha DRE?", "Receita bruta, devoluções, receita líquida, CMV, lucro bruto, despesas operacionais (por tipo) e lucro líquido. Pelo menos mensalmente."),
            ("Qual ferramenta usar para DRE?", "Google Sheets ou Excel para começar. Ferramentas integradas com o ML poupam tempo quando o volume cresce."),
            ("Como preencher o CMV na planilha?", "CMV = estoque inicial + compras do período - estoque final. Ou use o custo unitário × unidades vendidas no período."),
            ("Com que frequência atualizar a planilha?", "Mensalmente no mínimo. Fechamentos semanais ajudam a detectar problemas mais cedo."),
            ("O DRE substitui o fluxo de caixa?", "Não. O DRE mostra resultado por competência; o fluxo de caixa mostra entradas e saídas reais de dinheiro. Ambos são necessários."),
        ],
        "content": """
<h2>Estrutura da Planilha DRE para ML</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Linha</th><th>Descrição</th><th>Fonte dos Dados</th></tr></thead>
<tbody>
<tr><td>1</td><td>Receita Bruta</td><td>Relatório de vendas do ML</td></tr>
<tr><td>2</td><td>(-) Devoluções</td><td>Relatório de devoluções</td></tr>
<tr><td>3</td><td>= Receita Líquida</td><td>Linha 1 - Linha 2</td></tr>
<tr><td>4</td><td>(-) CMV</td><td>NF de compra / controle de estoque</td></tr>
<tr><td>5</td><td>= Lucro Bruto</td><td>Linha 3 - Linha 4</td></tr>
<tr><td>6</td><td>(-) Comissão ML</td><td>Extrato financeiro do ML</td></tr>
<tr><td>7</td><td>(-) Frete</td><td>Extrato financeiro do ML</td></tr>
<tr><td>8</td><td>(-) Impostos</td><td>DAS emitido / DARF</td></tr>
<tr><td>9</td><td>(-) Despesas fixas</td><td>Extratos bancários</td></tr>
<tr><td>10</td><td>= Lucro Líquido</td><td>Linha 5 - Linhas 6 a 9</td></tr>
</tbody>
</table>
</div>

<h2>Limitações da Planilha Manual</h2>
<p>A planilha funciona bem até aproximadamente 100 pedidos/mês. Acima disso, preencher manualmente torna-se trabalhoso e sujeito a erros. Além disso, o relatório do ML não exporta todos os dados necessários (como custo de frete por pedido) em um único arquivo.</p>

<div class="callout callout-warn">
<p><strong>Atenção:</strong> O relatório de vendas do ML mostra o valor bruto dos pedidos. Para o DRE, você precisa do extrato financeiro (que mostra as deduções) e cruzar com as notas de compra do estoque.</p>
</div>

<h2>Automatizando o DRE</h2>
<p>Ferramentas como o Sobrou Quanto ML conectam diretamente com a API do Mercado Livre e puxam automaticamente: vendas, comissões, fretes, devoluções e repasses. Com o CMV cadastrado por produto, o DRE é gerado automaticamente a cada fechamento. Veja também <a href="/relatorio-mercado-livre-como-exportar/">Como Exportar Relatórios do ML</a>.</p>
"""
    },
    {
        "slug":  "como-precificar-produto-mercado-livre",
        "title": "Como Precificar Produto no Mercado Livre 2025 | Fórmula Completa",
        "h1":    "Como Precificar Produtos no Mercado Livre: Fórmula e Estratégias",
        "tag":   "Precificação",
        "desc":  "Aprenda a fórmula completa de precificação para o Mercado Livre. Inclua todos os custos e defina o preço mínimo lucrativo antes de anunciar.",
        "lead":  "Precificar para o Mercado Livre exige uma fórmula que considere comissão, frete, imposto e margem desejada — não apenas o custo do produto. Veja como fazer isso corretamente.",
        "cta_title": "Precifique Com Dados Reais da Sua Loja",
        "cta_desc":  "Sobrou Quanto ML usa seu histórico real de custos para calcular o preço mínimo de cada produto. Conecte e otimize sua precificação.",
        "links": ["precificacao-mercado-livre","erros-precificacao-mercado-livre","calculadora-margem-mercado-livre","como-calcular-comissao-mercado-livre"],
        "faq": [
            ("Qual a fórmula de precificação para o ML?", "Preço = CMV ÷ (1 - % comissão ML - % frete - % imposto - % margem desejada). Substitua os percentuais pelos reais da sua categoria."),
            ("Como calcular o preço mínimo de venda?", "É o preço onde o lucro é zero. Preço mínimo = CMV ÷ (1 - % comissão - % frete - % imposto). Abaixo disso, você vende no prejuízo."),
            ("Devo precificar igual ao concorrente?", "Não obrigatoriamente. Se sua margem não suporta o preço do concorrente, vender mais barato só aumenta o prejuízo."),
            ("Como precificar com frete grátis obrigatório?", "Inclua o custo médio de frete na fórmula como um custo fixo por produto. O preço de venda precisa cobrir esse custo."),
            ("Como ajustar preço para promoções do ML?", "Calcule o preço mínimo com antecedência. Nunca aceite oferta abaixo do mínimo — mesmo que o ML sugira."),
        ],
        "content": """
<h2>A Fórmula Mark-up Reversa</h2>
<p>Em vez de somar custos ao CMV (mark-up tradicional), use a fórmula reversa que garante a margem desejada:</p>

<div class="callout callout-green">
<p><strong>Fórmula:</strong> Preço de venda = CMV ÷ (1 - comissão ML% - frete% - imposto% - margem desejada%)</p>
<p><strong>Exemplo:</strong> CMV = R$40, comissão = 16%, frete = 8%, imposto = 6%, margem = 15%<br>
Preço = 40 ÷ (1 - 0,16 - 0,08 - 0,06 - 0,15) = 40 ÷ 0,55 = <strong>R$ 72,72</strong></p>
</div>

<h2>Erros Comuns de Precificação</h2>
<ul>
<li>Usar mark-up simples (CMV × 2) sem considerar comissão do ML</li>
<li>Não incluir o custo de frete (pensa que o ML paga)</li>
<li>Ignorar o imposto na fórmula</li>
<li>Não incluir % de devolução (cada devolução tem custo real)</li>
<li>Precificar igual ao menor concorrente sem verificar se a margem suporta</li>
</ul>

<h2>Precificação Dinâmica</h2>
<p>Para vendedores com alto volume, reprecificadores automáticos ajustam o preço em tempo real baseando-se no buy box e no estoque. Mas atenção: configure sempre um preço mínimo para que a automação nunca venda abaixo do custo. Leia mais em <a href="/erros-precificacao-mercado-livre/">Erros de Precificação no ML</a>.</p>
"""
    },
    {
        "slug":  "relatorio-mensal-mercado-livre",
        "title": "Relatório Mensal do Mercado Livre: Como Fazer e Analisar | 2025",
        "h1":    "Como Fazer o Relatório Mensal da Sua Loja no Mercado Livre",
        "tag":   "Relatório",
        "desc":  "Aprenda a montar e analisar o relatório mensal da sua loja no Mercado Livre. Métricas essenciais, como exportar dados e tomar decisões baseadas em números.",
        "lead":  "Um relatório mensal bem estruturado transforma dados brutos em decisões. Veja quais métricas acompanhar, como exportar do ML e como automatizar esse processo.",
        "cta_title": "Relatório Mensal Automático",
        "cta_desc":  "Sobrou Quanto ML gera o relatório completo da sua loja automaticamente — DRE, margem por produto, comparativo mensal e muito mais.",
        "links": ["gestao-financeira-vendedor-mercado-livre","planilha-dre-mercado-livre","relatorio-mercado-livre-como-exportar","conciliacao-mercado-livre"],
        "faq": [
            ("Quais métricas incluir no relatório mensal?", "Faturamento bruto e líquido, número de pedidos, ticket médio, margem líquida, devoluções, CMV e custo operacional total."),
            ("Como exportar os dados do ML para o relatório?", "No painel do vendedor ML, vá em Vendas > Relatórios. Você pode exportar por período em CSV ou Excel."),
            ("Com que frequência fazer o relatório?", "Mensalmente fechado até o dia 10 do mês seguinte. Relatórios semanais rápidos ajudam a detectar problemas antes de fechar o mês."),
            ("O relatório do ML já mostra o lucro?", "Não. O ML mostra faturamento e alguns custos, mas não o CMV, não as despesas fixas e não o imposto. Você precisa complementar externamente."),
            ("Qual a diferença entre relatório de vendas e extrato financeiro?", "Relatório de vendas mostra pedidos. Extrato financeiro mostra os repasses efetivos. Ambos são necessários para um relatório completo."),
        ],
        "content": """
<h2>Estrutura do Relatório Mensal Ideal</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">📈</div><h4>Resultado Financeiro</h4><p>Faturamento, receita líquida, lucro bruto e lucro líquido do mês</p></div>
<div class="benefit-card"><div class="b-icon">📦</div><h4>Análise de Produtos</h4><p>Top 10 por faturamento, top 10 por margem, piores margens</p></div>
<div class="benefit-card"><div class="b-icon">↩️</div><h4>Devoluções</h4><p>Taxa de devolução por produto, valor devolvido, principais motivos</p></div>
<div class="benefit-card"><div class="b-icon">🔄</div><h4>Conciliação</h4><p>Vendas vs repasses recebidos — identifica diferenças e cobranças indevidas</p></div>
</div>

<h2>Passo a Passo Para Montar o Relatório</h2>
<ol>
<li>Exporte o relatório de vendas do ML (período: mês completo)</li>
<li>Exporte o extrato financeiro (repasses e deduções)</li>
<li>Importe os dados no seu DRE ou planilha</li>
<li>Adicione o CMV a partir do controle de estoque</li>
<li>Insira as despesas fixas do período</li>
<li>Calcule as métricas-chave e compare com o mês anterior</li>
</ol>

<div class="callout">
<p>Para detalhes sobre como exportar cada relatório do ML, veja: <a href="/relatorio-mercado-livre-como-exportar/">Como Exportar Relatórios do Mercado Livre</a>.</p>
</div>

<h2>Automatizando o Relatório Mensal</h2>
<p>Fazer esse processo manualmente consome de 3 a 8 horas por mês. Ferramentas que integram diretamente com a API do ML eliminam a exportação manual e geram o relatório em segundos. O Sobrou Quanto ML faz exatamente isso — conecte sua conta e tenha o relatório completo com um clique.</p>
"""
    },
]

# ── HTML template (sem innerHTML em nenhum JS) ────────────────────────────────
def build_lead_form():
    return f"""
<div class="lead-section">
  <h3 class="lead-title">Receba Dicas Exclusivas Para Vendedores do ML</h3>
  <p class="lead-sub">Conteúdo prático sobre finanças, impostos e precificação. Sem spam.</p>
  <form class="lead-form" id="leadForm" onsubmit="submitLead(event)">
    <input type="email" id="leadEmail" placeholder="seu@email.com" required class="lead-input" />
    <button type="submit" class="lead-btn">Quero receber</button>
  </form>
  <p class="lead-ok" id="leadOk" style="display:none">Inscrito com sucesso! Verifique seu e-mail.</p>
  <p class="lead-err" id="leadErr" style="display:none">Erro ao enviar. Tente novamente.</p>
</div>
<script>
function submitLead(e) {{
  e.preventDefault();
  var email = document.getElementById('leadEmail').value;
  fetch('{SUPABASE_URL}', {{
    method: 'POST',
    headers: {{'Content-Type': 'application/json'}},
    body: JSON.stringify({{email: email, source: window.location.pathname}})
  }}).then(function(r) {{
    document.getElementById('leadForm').style.display = 'none';
    if (r.ok) {{
      document.getElementById('leadOk').style.display = 'block';
    }} else {{
      document.getElementById('leadErr').style.display = 'block';
    }}
  }}).catch(function() {{
    document.getElementById('leadForm').style.display = 'none';
    document.getElementById('leadErr').style.display = 'block';
  }});
}}
</script>
"""

def build_faq_html(faq_list):
    items = ""
    for q, a in faq_list:
        items += f"""
  <div class="faq-item">
    <button class="faq-q" onclick="toggleFaq(this)" aria-expanded="false">{q}</button>
    <div class="faq-a" hidden><p>{a}</p></div>
  </div>"""
    return f"""
<div class="faq-block">
  <h2>Perguntas Frequentes</h2>
  {items}
</div>
<script>
function toggleFaq(btn) {{
  var ans = btn.nextElementSibling;
  var open = btn.getAttribute('aria-expanded') === 'true';
  btn.setAttribute('aria-expanded', String(!open));
  if (open) {{ ans.setAttribute('hidden', ''); }} else {{ ans.removeAttribute('hidden'); }}
}}
</script>
"""

def build_links_html(slugs):
    lis = ""
    for s in slugs[:6]:
        label = s.replace("-", " ").title()
        lis += f'<li><a href="/{s}/">{label}</a></li>\n'
    return f"""
<div class="links-block">
  <h3>Leia Também</h3>
  <ul>{lis}</ul>
</div>
"""

def build_faq_schema(faq_list, slug):
    entries = [{"@type": "Question", "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}}
               for q, a in faq_list]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                        "mainEntity": entries}, ensure_ascii=False)

def build_article_schema(p):
    return json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": p["h1"], "description": p["desc"],
        "url": f"{SITE}/{p['slug']}/",
        "datePublished": DATE_ISO, "dateModified": DATE_ISO,
        "author": {"@type": "Organization", "name": "Sobrou Quanto ML"},
        "publisher": {"@type": "Organization", "name": "Sobrou Quanto ML",
                      "url": f"{SITE}/"}
    }, ensure_ascii=False)

def build_breadcrumb_schema(p):
    return json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": p["h1"],
             "item": f"{SITE}/{p['slug']}/"}
        ]
    }, ensure_ascii=False)

READ_TIME_WORDS = 250

def read_time(content):
    words = len(content.split())
    return max(3, round(words / READ_TIME_WORDS))

LEAD_CSS = """
    .lead-section { background: var(--blue-bg); border: 1px solid var(--blue-soft); border-radius: 14px; padding: 28px 24px; margin: 40px 0; text-align: center; }
    .lead-title { font-size: 1.1rem; font-weight: 700; color: var(--dark); margin-bottom: 6px; }
    .lead-sub { font-size: .88rem; color: var(--muted); margin-bottom: 18px; }
    .lead-form { display: flex; gap: 10px; max-width: 420px; margin: 0 auto; flex-wrap: wrap; justify-content: center; }
    .lead-input { flex: 1; min-width: 220px; padding: 11px 16px; border: 1px solid var(--border); border-radius: 8px; font-size: .95rem; outline: none; }
    .lead-input:focus { border-color: var(--blue); }
    .lead-btn { background: var(--blue); color: #fff; border: none; border-radius: 8px; padding: 11px 22px; font-weight: 600; cursor: pointer; font-size: .95rem; transition: background .2s; }
    .lead-btn:hover { background: var(--blue-dark); }
    .lead-ok { color: var(--green); font-weight: 600; margin-top: 12px; }
    .lead-err { color: #DC2626; font-weight: 600; margin-top: 12px; }

    .faq-block { margin: 40px 0; }
    .faq-block h2 { font-size: 1.3rem; font-weight: 700; color: var(--dark); margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid var(--blue-soft); }
    .faq-item { border-bottom: 1px solid var(--border); }
    .faq-q { width: 100%; text-align: left; background: none; border: none; padding: 16px 0; font-size: .97rem; font-weight: 600; color: var(--dark); cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .faq-q::after { content: '+'; font-size: 1.2rem; color: var(--blue); flex-shrink: 0; margin-left: 12px; }
    .faq-q[aria-expanded='true']::after { content: '-'; }
    .faq-a { padding: 0 0 16px; }
    .faq-a p { margin: 0; color: #374151; font-size: .94rem; }

    .links-block { margin: 32px 0; padding: 20px; background: var(--gray-light); border-radius: 12px; border: 1px solid var(--border); }
    .links-block h3 { font-size: 1rem; font-weight: 700; margin-bottom: 12px; color: var(--dark); }
    .links-block ul { margin: 0; padding-left: 20px; }
    .links-block li { margin-bottom: 6px; font-size: .9rem; }
    .links-block a { color: var(--blue); text-decoration: none; }
    .links-block a:hover { text-decoration: underline; }
"""

PAGE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{site}/{slug}/" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{site}/{slug}/" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:locale" content="pt_BR" />
  <meta property="og:site_name" content="Sobrou Quanto ML" />
  <script type="application/ld+json">{schema_article}</script>
  <script type="application/ld+json">{schema_faq}</script>
  <script type="application/ld+json">{schema_breadcrumb}</script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --blue:#2563EB; --blue-dark:#1D4ED8; --blue-deep:#162035;
      --blue-bg:#EFF6FF; --blue-soft:#DBEAFE; --green:#10B981;
      --dark:#0f111a; --muted:#6A82A8; --border:#E2E8F0;
      --gray-light:#F8FAFC; --white:#ffffff;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Inter', sans-serif; color: var(--dark); background: var(--white); line-height: 1.7; }}
    nav {{ position: sticky; top: 0; z-index: 100; background: rgba(255,255,255,.96); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; }}
    .nav-logo {{ display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--dark); font-weight: 700; font-size: 1rem; }}
    .nav-logo-icon {{ width: 32px; height: 32px; border-radius: 8px; background: var(--blue); display: flex; align-items: center; justify-content: center; color: #fff; font-size: .85rem; font-weight: 800; }}
    .nav-logo em {{ color: var(--blue); font-style: normal; }}
    .nav-logo small {{ font-weight: 400; color: var(--muted); font-size: .72rem; margin-left: 4px; }}
    .nav-cta {{ background: var(--blue); color: #fff; border: none; border-radius: 8px; padding: 8px 20px; font-size: .875rem; font-weight: 600; cursor: pointer; text-decoration: none; transition: background .2s; }}
    .nav-cta:hover {{ background: var(--blue-dark); }}
    .breadcrumb {{ max-width: 800px; margin: 0 auto; padding: 14px 24px 0; font-size: .78rem; color: var(--muted); display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }}
    .breadcrumb a {{ color: var(--blue); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .page-wrapper {{ max-width: 800px; margin: 0 auto; padding: 32px 24px 80px; }}
    .article-tag {{ display: inline-block; background: var(--blue-bg); color: var(--blue); font-size: .72rem; font-weight: 700; padding: 4px 12px; border-radius: 20px; margin-bottom: 16px; text-transform: uppercase; letter-spacing: .06em; }}
    .article-hero h1 {{ font-size: clamp(1.55rem, 4vw, 2.1rem); font-weight: 800; line-height: 1.25; color: var(--dark); margin-bottom: 16px; }}
    .article-hero .lead {{ font-size: 1.05rem; color: #374151; line-height: 1.75; margin-bottom: 18px; }}
    .article-meta {{ font-size: .78rem; color: var(--muted); display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 40px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }}
    .article-content h2 {{ font-size: 1.3rem; font-weight: 700; color: var(--dark); margin: 36px 0 14px; padding-bottom: 8px; border-bottom: 2px solid var(--blue-soft); }}
    .article-content h3 {{ font-size: 1.05rem; font-weight: 600; color: var(--dark); margin: 26px 0 10px; }}
    .article-content p {{ color: #374151; margin-bottom: 16px; font-size: .97rem; }}
    .article-content strong {{ color: var(--dark); }}
    .article-content ul, .article-content ol {{ margin: 12px 0 20px 22px; color: #374151; }}
    .article-content li {{ margin-bottom: 8px; font-size: .97rem; }}
    .table-wrapper {{ overflow-x: auto; margin: 24px 0; border-radius: 12px; border: 1px solid var(--border); }}
    table {{ width: 100%; border-collapse: collapse; font-size: .88rem; }}
    thead {{ background: var(--blue-deep); color: #fff; }}
    thead th {{ padding: 12px 16px; text-align: left; font-weight: 600; font-size: .78rem; text-transform: uppercase; letter-spacing: .04em; }}
    tbody tr {{ border-bottom: 1px solid var(--border); }}
    tbody tr:last-child {{ border-bottom: none; }}
    tbody tr:nth-child(even) {{ background: var(--gray-light); }}
    tbody td {{ padding: 11px 16px; color: #374151; }}
    tbody td strong {{ color: var(--dark); }}
    .callout {{ background: var(--blue-bg); border-left: 4px solid var(--blue); border-radius: 0 10px 10px 0; padding: 18px 20px; margin: 28px 0; }}
    .callout p {{ margin: 0; color: #1E3A8A; font-size: .94rem; }}
    .callout-warn {{ background: #FEF3C7; border-left-color: #F59E0B; }}
    .callout-warn p {{ color: #78350F; }}
    .callout-green {{ background: #F0FDF4; border-left-color: var(--green); }}
    .callout-green p {{ color: #14532D; }}
    .benefit-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; margin: 24px 0; }}
    .benefit-card {{ background: var(--gray-light); border: 1px solid var(--border); border-radius: 12px; padding: 18px; }}
    .benefit-card .b-icon {{ font-size: 1.3rem; margin-bottom: 8px; }}
    .benefit-card h4 {{ font-size: .92rem; font-weight: 700; margin-bottom: 5px; color: var(--dark); }}
    .benefit-card p {{ font-size: .83rem; color: var(--muted); margin: 0; }}
    .cta-box {{ background: linear-gradient(135deg, var(--blue-deep) 0%, #0C1523 100%); border-radius: 16px; padding: 40px 32px; text-align: center; margin: 52px 0 0; border: 1px solid #1F2E47; }}
    .cta-box .cta-label {{ font-size: .72rem; font-weight: 700; color: #60A5FA; text-transform: uppercase; letter-spacing: .09em; margin-bottom: 12px; }}
    .cta-box h2 {{ font-size: 1.5rem; font-weight: 800; color: #fff; margin-bottom: 10px; line-height: 1.3; border: none; padding: 0; }}
    .cta-box p {{ color: #94A3B8; font-size: .94rem; margin-bottom: 24px; max-width: 480px; margin-left: auto; margin-right: auto; }}
    .btn-primary {{ display: inline-block; background: var(--blue); color: #fff; font-weight: 700; font-size: 1rem; padding: 14px 34px; border-radius: 10px; text-decoration: none; transition: background .2s, transform .15s; }}
    .btn-primary:hover {{ background: var(--blue-dark); transform: translateY(-2px); }}
    .cta-sub {{ margin-top: 12px; font-size: .78rem; color: #64748B; }}
    footer {{ background: var(--dark); color: #94A3B8; text-align: center; padding: 32px 24px; font-size: .82rem; line-height: 2; }}
    footer a {{ color: #60A5FA; text-decoration: none; }}
    footer a:hover {{ text-decoration: underline; }}
    .footer-logo {{ color: #fff; font-weight: 700; font-size: .95rem; margin-bottom: 4px; }}
    .footer-logo em {{ color: var(--blue); font-style: normal; }}
    @media (max-width: 600px) {{ .page-wrapper {{ padding: 24px 16px 60px; }} .cta-box {{ padding: 28px 20px; }} .cta-box h2 {{ font-size: 1.25rem; }} }}
    {lead_css}
  </style>
</head>
<body>
  <nav>
    <a href="{site}/" class="nav-logo">
      <div class="nav-logo-icon">$</div>
      <span>Sobrou<em>Quanto</em>ML<small>by ProspectIA</small></span>
    </a>
    <a href="{site}/" class="nav-cta">Comecar gratis</a>
  </nav>
  <div class="breadcrumb">
    <a href="{site}/">Inicio</a>
    <span>&rsaquo;</span>
    <span>{h1}</span>
  </div>
  <main class="page-wrapper">
    <header class="article-hero">
      <div class="article-tag">{tag}</div>
      <h1>{h1}</h1>
      <p class="lead">{lead_text}</p>
      <div class="article-meta">
        <span>Atualizado em {date_br}</span>
        <span>&middot; {read_time} min de leitura</span>
      </div>
    </header>
    <article class="article-content">
      {content}
    </article>
    {lead_form}
    {faq_html}
    {links_html}
    <div class="cta-box">
      <div class="cta-label">Sobrou Quanto ML</div>
      <h2>{cta_title}</h2>
      <p>{cta_desc}</p>
      <a href="{site}/" class="btn-primary">Comecar 7 dias gratis</a>
      <div class="cta-sub">Sem cartao de credito &middot; Cancele quando quiser</div>
    </div>
  </main>
  <footer>
    <div class="footer-logo">Sobrou<em>Quanto</em>ML</div>
    <p>
      <a href="{site}/">Home</a> &middot;
      <a href="{site}/politica.html">Politica de privacidade</a>
    </p>
    <p>2026 Sobrou Quanto ML &middot; by ProspectIA &middot; Todos os direitos reservados.</p>
  </footer>
</body>
</html>
"""

def generate_page(p):
    slug = p["slug"]
    out_dir = os.path.join(BASE, slug)
    os.makedirs(out_dir, exist_ok=True)

    faq_html    = build_faq_html(p["faq"])
    links_html  = build_links_html(p.get("links", []))
    lead_form   = build_lead_form()
    rt          = read_time(p["content"])

    html = PAGE_TEMPLATE.format(
        site=SITE, slug=slug, title=p["title"], h1=p["h1"],
        desc=p["desc"], tag=p["tag"], lead_text=p["lead"],
        date_br=DATE_BR, read_time=rt,
        content=p["content"],
        lead_form=lead_form, faq_html=faq_html, links_html=links_html,
        cta_title=p["cta_title"], cta_desc=p["cta_desc"],
        schema_article=build_article_schema(p),
        schema_faq=build_faq_schema(p["faq"], slug),
        schema_breadcrumb=build_breadcrumb_schema(p),
        lead_css=LEAD_CSS,
    )

    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [OK] /{slug}/")


# ── Hub page /guia-mercado-livre/ ────────────────────────────────────────────
ALL_SLUGS = LOTE1 + LOTE2 + [p["slug"] for p in PAGES]

CATEGORIES = {
    "Taxas e Comissoes": [
        "taxas-mercado-livre","comissao-mercado-livre","quanto-mercado-livre-cobra",
        "como-calcular-comissao-mercado-livre","quanto-custa-vender-mercado-livre",
        "como-reduzir-taxas-mercado-livre","mercado-pago-taxas",
    ],
    "Precificacao": [
        "precificacao-mercado-livre","erros-precificacao-mercado-livre",
        "como-precificar-produto-mercado-livre","calculadora-margem-mercado-livre",
        "simulador-lucro-mercado-livre","ponto-de-equilibrio-mercado-livre",
    ],
    "Lucro e Margens": [
        "margem-de-lucro-mercado-livre","lucro-real-mercado-livre",
        "quanto-sobra-venda-mercado-livre","diferenca-faturamento-lucro-mercado-livre",
        "receita-liquida-mercado-livre","faturamento-mercado-livre",
        "produto-no-prejuizo-mercado-livre","como-saber-se-estou-lucrando-mercado-livre",
        "como-aumentar-lucro-mercado-livre",
    ],
    "Impostos e Regime Tributario": [
        "dre-para-mei","dre-simples-nacional","dre-lucro-presumido",
        "impostos-vendedor-mercado-livre","simples-nacional-ou-mei",
        "calcular-imposto-simples-mercado-livre","nota-fiscal-mercado-livre",
    ],
    "Gestao Financeira": [
        "gestao-financeira-vendedor-mercado-livre","fluxo-de-caixa-mercado-livre",
        "conciliacao-mercado-livre","capital-de-giro-mercado-livre",
        "separar-financas-pessoais-empresariais","reserva-financeira-vendedor-ml",
        "planilha-controle-mercado-livre","planilha-dre-mercado-livre",
        "relatorio-mercado-livre-como-exportar","relatorio-mensal-mercado-livre",
    ],
    "Operacoes e Logistica": [
        "frete-gratis-mercado-livre","devolucoes-mercado-livre",
        "anuncio-full-mercado-livre","buy-box-mercado-livre",
        "estoque-mercado-livre","cmv-mercado-livre",
    ],
    "Crescimento e Estrategia": [
        "escalar-vendas-mercado-livre","ticket-medio-mercado-livre",
        "sazonalidade-mercado-livre","reputacao-mercado-livre",
        "quanto-ganhar-mercado-livre","vale-a-pena-vender-mercado-livre",
        "guia-iniciante-mercado-livre",
    ],
}

def build_hub():
    cats_html = ""
    for cat, slugs in CATEGORIES.items():
        lis = ""
        for s in slugs:
            label = s.replace("-mercado-livre","").replace("-ml","").replace("-"," ").title()
            lis += f'<li><a href="/{s}/">{label}</a></li>\n'
        cats_html += f"""
<div class="hub-cat">
  <h2>{cat}</h2>
  <ul>{lis}</ul>
</div>
"""

    hub_schema = json.dumps({
        "@context": "https://schema.org", "@type": "CollectionPage",
        "name": "Guia Financeiro para Vendedores do Mercado Livre",
        "description": "Guia completo com artigos sobre taxas, precificacao, impostos, DRE e gestao financeira para vendedores do Mercado Livre.",
        "url": f"{SITE}/guia-mercado-livre/",
        "publisher": {"@type": "Organization", "name": "Sobrou Quanto ML", "url": f"{SITE}/"}
    }, ensure_ascii=False)

    hub_html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Guia Financeiro Completo para Vendedores do Mercado Livre | Sobrou Quanto ML</title>
  <meta name="description" content="Guia com mais de 50 artigos sobre taxas, precificacao, DRE, impostos e gestao financeira para vendedores do Mercado Livre." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{SITE}/guia-mercado-livre/" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{SITE}/guia-mercado-livre/" />
  <meta property="og:title" content="Guia Financeiro para Vendedores do Mercado Livre" />
  <meta property="og:locale" content="pt_BR" />
  <script type="application/ld+json">{hub_schema}</script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    :root {{ --blue:#2563EB; --blue-dark:#1D4ED8; --blue-deep:#162035; --blue-bg:#EFF6FF; --blue-soft:#DBEAFE; --green:#10B981; --dark:#0f111a; --muted:#6A82A8; --border:#E2E8F0; --gray-light:#F8FAFC; --white:#ffffff; }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Inter', sans-serif; color: var(--dark); background: var(--white); line-height: 1.7; }}
    nav {{ position: sticky; top: 0; z-index: 100; background: rgba(255,255,255,.96); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; }}
    .nav-logo {{ display: flex; align-items: center; gap: 10px; text-decoration: none; color: var(--dark); font-weight: 700; font-size: 1rem; }}
    .nav-logo-icon {{ width: 32px; height: 32px; border-radius: 8px; background: var(--blue); display: flex; align-items: center; justify-content: center; color: #fff; font-size: .85rem; font-weight: 800; }}
    .nav-logo em {{ color: var(--blue); font-style: normal; }}
    .nav-logo small {{ font-weight: 400; color: var(--muted); font-size: .72rem; margin-left: 4px; }}
    .nav-cta {{ background: var(--blue); color: #fff; border: none; border-radius: 8px; padding: 8px 20px; font-size: .875rem; font-weight: 600; cursor: pointer; text-decoration: none; transition: background .2s; }}
    .nav-cta:hover {{ background: var(--blue-dark); }}
    .page-wrapper {{ max-width: 960px; margin: 0 auto; padding: 40px 24px 80px; }}
    .hub-hero {{ text-align: center; margin-bottom: 48px; }}
    .hub-hero h1 {{ font-size: clamp(1.7rem, 4vw, 2.4rem); font-weight: 800; line-height: 1.2; margin-bottom: 14px; }}
    .hub-hero p {{ font-size: 1.05rem; color: #374151; max-width: 560px; margin: 0 auto; }}
    .hub-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; }}
    .hub-cat {{ background: var(--gray-light); border: 1px solid var(--border); border-radius: 14px; padding: 22px 20px; }}
    .hub-cat h2 {{ font-size: 1rem; font-weight: 700; color: var(--dark); margin-bottom: 14px; padding-bottom: 10px; border-bottom: 2px solid var(--blue-soft); }}
    .hub-cat ul {{ list-style: none; padding: 0; margin: 0; }}
    .hub-cat li {{ margin-bottom: 8px; }}
    .hub-cat a {{ color: var(--blue); text-decoration: none; font-size: .9rem; }}
    .hub-cat a:hover {{ text-decoration: underline; }}
    .cta-box {{ background: linear-gradient(135deg, var(--blue-deep) 0%, #0C1523 100%); border-radius: 16px; padding: 40px 32px; text-align: center; margin: 52px 0 0; border: 1px solid #1F2E47; }}
    .cta-box .cta-label {{ font-size: .72rem; font-weight: 700; color: #60A5FA; text-transform: uppercase; letter-spacing: .09em; margin-bottom: 12px; }}
    .cta-box h2 {{ font-size: 1.5rem; font-weight: 800; color: #fff; margin-bottom: 10px; }}
    .cta-box p {{ color: #94A3B8; font-size: .94rem; margin-bottom: 24px; max-width: 480px; margin-left: auto; margin-right: auto; }}
    .btn-primary {{ display: inline-block; background: var(--blue); color: #fff; font-weight: 700; font-size: 1rem; padding: 14px 34px; border-radius: 10px; text-decoration: none; transition: background .2s, transform .15s; }}
    .btn-primary:hover {{ background: var(--blue-dark); transform: translateY(-2px); }}
    .cta-sub {{ margin-top: 12px; font-size: .78rem; color: #64748B; }}
    footer {{ background: var(--dark); color: #94A3B8; text-align: center; padding: 32px 24px; font-size: .82rem; line-height: 2; }}
    footer a {{ color: #60A5FA; text-decoration: none; }}
    .footer-logo {{ color: #fff; font-weight: 700; font-size: .95rem; margin-bottom: 4px; }}
    .footer-logo em {{ color: var(--blue); font-style: normal; }}
  </style>
</head>
<body>
  <nav>
    <a href="{SITE}/" class="nav-logo">
      <div class="nav-logo-icon">$</div>
      <span>Sobrou<em>Quanto</em>ML<small>by ProspectIA</small></span>
    </a>
    <a href="{SITE}/" class="nav-cta">Comecar gratis</a>
  </nav>
  <main class="page-wrapper">
    <div class="hub-hero">
      <h1>Guia Financeiro para Vendedores do Mercado Livre</h1>
      <p>Mais de 50 artigos sobre taxas, precificacao, impostos, DRE e gestao financeira para quem vende no ML.</p>
    </div>
    <div class="hub-grid">
      {cats_html}
    </div>
    <div class="cta-box">
      <div class="cta-label">Sobrou Quanto ML</div>
      <h2>Calcule o Lucro Real da Sua Loja</h2>
      <p>Conecte sua conta do Mercado Livre e veja automaticamente quanto sobra em cada venda.</p>
      <a href="{SITE}/" class="btn-primary">Comecar 7 dias gratis</a>
      <div class="cta-sub">Sem cartao de credito &middot; Cancele quando quiser</div>
    </div>
  </main>
  <footer>
    <div class="footer-logo">Sobrou<em>Quanto</em>ML</div>
    <p><a href="{SITE}/">Home</a> &middot; <a href="{SITE}/politica.html">Politica de privacidade</a></p>
    <p>2026 Sobrou Quanto ML &middot; by ProspectIA &middot; Todos os direitos reservados.</p>
  </footer>
</body>
</html>
"""
    hub_dir = os.path.join(BASE, "guia-mercado-livre")
    os.makedirs(hub_dir, exist_ok=True)
    with open(os.path.join(hub_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(hub_html)
    print("  [OK] /guia-mercado-livre/")


# ── sitemap update ────────────────────────────────────────────────────────────
def update_sitemap(new_slugs):
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, encoding="utf-8") as f:
        content = f.read()

    for slug in new_slugs:
        url = f"{SITE}/{slug}/"
        if url not in content:
            entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{DATE_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>"""
            content = content.replace("</urlset>", entry + "\n</urlset>")

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] sitemap.xml (+{len(new_slugs)} URLs)")


# ── main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nGerando {len(PAGES)} paginas (Lote 3)...")
    for p in PAGES:
        generate_page(p)

    print("\nGerando hub /guia-mercado-livre/...")
    build_hub()

    new_slugs = [p["slug"] for p in PAGES] + ["guia-mercado-livre"]
    print("\nAtualizando sitemap.xml...")
    update_sitemap(new_slugs)

    print(f"\nPronto! {len(PAGES)} paginas + hub gerados com sucesso.")
    print(f"Total de paginas SEO: {len(ALL_SLUGS) + 1} (incluindo hub)")
