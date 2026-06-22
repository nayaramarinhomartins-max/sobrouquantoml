"""gen5.py — Lote 5: 22 páginas SEO (produtos, anúncios, SEO interno ML)"""
import os, json
from datetime import date

BASE = os.path.join(os.path.dirname(__file__), "public")
SITE = "https://sobrouquantoml.prospectia.space"
TODAY = date.today()
DATE_BR  = TODAY.strftime("%d/%m/%Y")
DATE_ISO = TODAY.isoformat()
SUPABASE_URL = "https://wyqnqiowxhamvxtzedth.supabase.co/functions/v1/capture-lead"

PAGES = [
    {
        "slug":  "produto-mais-vendido-mercado-livre",
        "title": "Produto Mais Vendido no Mercado Livre 2025 | Categorias e Nichos",
        "h1":    "Produtos Mais Vendidos no Mercado Livre em 2025",
        "tag":   "Produtos",
        "desc":  "Descubra quais são os produtos mais vendidos no Mercado Livre em 2025. Categorias líderes, nichos em crescimento e como escolher o produto certo.",
        "lead":  "Saber o que mais vende no Mercado Livre é o primeiro passo — mas o que realmente importa é encontrar produtos com alta demanda E boa margem. Volume sem margem não paga as contas.",
        "cta_title": "Saiba Se Seu Produto Está Dando Lucro",
        "cta_desc":  "Sobrou Quanto ML calcula a margem real de cada produto vendido na sua loja — automático e integrado com o ML.",
        "links": ["como-escolher-produto-mercado-livre","produtos-mais-lucrativos-mercado-livre","nichos-lucrativos-mercado-livre","como-validar-produto-mercado-livre"],
        "faq": [
            ("Quais categorias mais vendem no ML?", "Eletrônicos, moda, casa e jardim, beleza e saúde, e eletrodomésticos consistentemente lideram em volume no ML."),
            ("Produto mais vendido é o mais lucrativo?", "Não necessariamente. Eletrônicos vendem muito mas têm margens apertadas. Acessórios e nicho vendem menos mas com margens maiores."),
            ("Como descobrir o que está em alta no ML?", "Use a busca do ML e observe o número de vendas nos anúncios concorrentes. Ferramentas de análise como Olist e Nuvem Shop publicam rankings periódicos."),
            ("Vale a pena vender o mesmo que todo mundo?", "Apenas se você tiver diferencial: preço melhor, envio mais rápido ou produto com variação exclusiva."),
            ("Como entrar em uma categoria saturada?", "Nicho dentro da categoria. Em vez de 'fone de ouvido', foque em 'fone para home office com cancelamento de ruído'."),
        ],
        "content": """
<h2>Categorias Mais Vendidas no ML (2025)</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Categoria</th><th>Volume</th><th>Margem típica</th><th>Concorrência</th></tr></thead>
<tbody>
<tr><td>Eletrônicos</td><td>Muito alto</td><td>5-12%</td><td>Muito alta</td></tr>
<tr><td>Moda e Acessórios</td><td>Alto</td><td>20-40%</td><td>Alta</td></tr>
<tr><td>Casa e Jardim</td><td>Alto</td><td>12-25%</td><td>Média</td></tr>
<tr><td>Beleza e Saúde</td><td>Alto</td><td>20-35%</td><td>Média</td></tr>
<tr><td>Brinquedos</td><td>Médio</td><td>15-30%</td><td>Média</td></tr>
<tr><td>Peças automotivas</td><td>Médio</td><td>15-30%</td><td>Baixa</td></tr>
</tbody>
</table>
</div>
<div class="callout">
<p><strong>Melhor estratégia:</strong> Escolha categorias com margem acima de 15% e concorrência média — e nicho dentro delas. Você não precisa ser o maior, precisa ser o mais lucrativo.</p>
</div>
<h2>Tendências de Produtos em Alta</h2>
<p>Produtos sustentáveis, itens para home office, suplementos naturais e acessórios para pets estão em crescimento consistente. Para validar antes de investir em estoque, veja <a href="/como-validar-produto-mercado-livre/">Como Validar Produto no ML</a>.</p>
"""
    },
    {
        "slug":  "como-organizar-financas-mercado-livre",
        "title": "Como Organizar as Finanças da Loja no Mercado Livre | 2025",
        "h1":    "Como Organizar as Finanças da Sua Loja no Mercado Livre",
        "tag":   "Finanças",
        "desc":  "Guia prático para organizar as finanças da sua loja no Mercado Livre. Conta PJ, DRE, fluxo de caixa e controle de estoque explicados de forma simples.",
        "lead":  "Organizar as finanças da loja no ML não precisa ser complicado. Com uma estrutura básica, você sabe exatamente quanto está ganhando e onde está perdendo.",
        "cta_title": "Finanças Organizadas em Minutos",
        "cta_desc":  "Sobrou Quanto ML organiza automaticamente DRE, fluxo de caixa e conciliação da sua loja — conectado ao ML.",
        "links": ["controle-financeiro-mercado-livre","separar-financas-pessoais-empresariais","gestao-financeira-vendedor-mercado-livre","fluxo-de-caixa-mercado-livre"],
        "faq": [
            ("Por onde começar a organizar as finanças?", "Primeiro passo: conta bancária PJ separada. Segundo: registrar todas as entradas e saídas. Terceiro: DRE mensal."),
            ("Preciso de sistema caro para organizar?", "Não. Uma planilha bem estruturada resolve no início. Ferramentas integradas com o ML valem quando o volume crescer."),
            ("Como separar o salário do lucro?", "Defina um pró-labore fixo mensal (o que você pagaria a um funcionário no seu lugar). O que sobrar é lucro da empresa."),
            ("O que fazer com o lucro da loja?", "Reserve 30% para impostos e obrigações, 30% para reinvestir em estoque e 40% pode ser retirado como pró-labore ou dividendo."),
            ("Com que frequência revisar as finanças?", "Fluxo de caixa: semanal. DRE e margem por produto: mensal."),
        ],
        "content": """
<h2>Estrutura Financeira em 4 Passos</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">🏦</div><h4>1. Conta PJ</h4><p>Separe completamente do pessoal — base de tudo</p></div>
<div class="benefit-card"><div class="b-icon">📋</div><h4>2. Registre tudo</h4><p>Cada compra, cada despesa, cada repasse do ML</p></div>
<div class="benefit-card"><div class="b-icon">📊</div><h4>3. DRE mensal</h4><p>Fecha o mês: receita, custos, resultado</p></div>
<div class="benefit-card"><div class="b-icon">🔄</div><h4>4. Conciliação</h4><p>Cruzar vendas ML com repasses recebidos</p></div>
</div>
<h2>Distribuição Saudável do Faturamento</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Destino</th><th>% recomendado</th></tr></thead>
<tbody>
<tr><td>Reposição de estoque (CMV)</td><td>40-50%</td></tr>
<tr><td>Impostos e obrigações</td><td>8-12%</td></tr>
<tr><td>Despesas operacionais</td><td>10-15%</td></tr>
<tr><td>Pró-labore do dono</td><td>15-20%</td></tr>
<tr><td>Lucro / reinvestimento</td><td>10-20%</td></tr>
</tbody>
</table>
</div>
<div class="callout callout-warn">
<p><strong>Erro comum:</strong> retirar o pró-labore antes de pagar fornecedores e impostos. Sempre pague obrigações primeiro — o dono recebe o que sobrar dentro do limite planejado.</p>
</div>
"""
    },
    {
        "slug":  "como-calcular-custo-produto-mercado-livre",
        "title": "Como Calcular o Custo do Produto no Mercado Livre | 2025",
        "h1":    "Como Calcular o Custo Real do Produto Para Vender no Mercado Livre",
        "tag":   "Cálculo",
        "desc":  "Aprenda a calcular o custo real do produto (CMV) para precificar corretamente no Mercado Livre. Inclua frete de compra, embalagem e outros custos ocultos.",
        "lead":  "O custo do produto não é só o que você pagou ao fornecedor. Frete de compra, embalagem, perdas e custo de oportunidade do estoque parado fazem parte do CMV real.",
        "cta_title": "Calcule Seu CMV Real e Precifique Corretamente",
        "cta_desc":  "Sobrou Quanto ML usa o CMV real de cada produto para calcular a margem exata de cada venda.",
        "links": ["precificacao-mercado-livre","como-calcular-lucro-mercado-livre","calculadora-margem-mercado-livre","produto-no-prejuizo-mercado-livre"],
        "faq": [
            ("O que compõe o custo do produto?", "Preço de compra + frete de compra + embalagem + custo de perdas/avarias estimado + custo de armazenagem se aplicável."),
            ("Frete de compra entra no CMV?", "Sim. Se você paga R$500 de frete para receber 100 unidades, cada unidade tem R$5 de custo de frete embutido."),
            ("Como calcular CMV de produtos importados?", "Custo CIF (produto + frete + seguro) + impostos de importação (II, IPI, PIS, COFINS) + despesas aduaneiras + frete nacional."),
            ("Como tratar variações de preço do fornecedor?", "Use o custo médio ponderado: (qtd anterior × custo anterior + qtd nova × custo novo) ÷ total de unidades."),
            ("Embalagem entra no CMV?", "Sim. Caixa, plástico bolha, lacre e etiqueta são custos diretos do produto e devem entrar no CMV."),
        ],
        "content": """
<h2>Fórmula do CMV Completo</h2>
<div class="callout callout-green">
<p><strong>CMV = Preço de compra + Frete de compra por unidade + Embalagem + Perdas estimadas (%) + Armazenagem</strong></p>
</div>
<h3>Exemplo Prático</h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Componente</th><th>Valor por unidade</th></tr></thead>
<tbody>
<tr><td>Preço de compra (fornecedor)</td><td>R$35,00</td></tr>
<tr><td>Frete de compra (R$300 ÷ 60 un)</td><td>R$5,00</td></tr>
<tr><td>Embalagem (caixa + lacre)</td><td>R$2,50</td></tr>
<tr><td>Perdas e avarias (2%)</td><td>R$0,85</td></tr>
<tr><td><strong>CMV Real</strong></td><td><strong>R$43,35</strong></td></tr>
</tbody>
</table>
</div>
<p>Quem usa apenas R$35,00 como CMV está subprecificando em R$8,35 por unidade — e nem percebe que está vendendo com margem menor do que pensa.</p>
<h2>CMV em Produtos Importados</h2>
<p>Importação direta tem custos muito maiores: II (imposto de importação), IPI, PIS/COFINS, ICMS, despacho aduaneiro e frete internacional. Um produto de US$10 pode chegar custando R$80+ após todos os tributos e despesas. Sempre calcule o custo final antes de fechar o pedido.</p>
"""
    },
    {
        "slug":  "como-escolher-produto-mercado-livre",
        "title": "Como Escolher Produto Para Vender no Mercado Livre | 2025",
        "h1":    "Como Escolher o Produto Certo Para Vender no Mercado Livre",
        "tag":   "Produtos",
        "desc":  "Critérios práticos para escolher produtos lucrativos para vender no Mercado Livre. Como avaliar demanda, margem, concorrência e risco antes de comprar estoque.",
        "lead":  "Escolher o produto errado é o erro mais caro no ML. Você compra estoque, cria anúncio, vende no prejuízo e descobre tarde demais. Os critérios certos evitam esse ciclo.",
        "cta_title": "Valide a Margem Antes de Comprar Estoque",
        "cta_desc":  "Com Sobrou Quanto ML você simula a margem de qualquer produto antes de anunciar, com dados reais de taxas e impostos.",
        "links": ["produto-mais-vendido-mercado-livre","como-validar-produto-mercado-livre","nichos-lucrativos-mercado-livre","produtos-mais-lucrativos-mercado-livre"],
        "faq": [
            ("Quais critérios usar para escolher produto?", "Margem mínima de 15%, demanda comprovada (concorrentes com vendas), baixo risco de devolução e fornecedor confiável."),
            ("Como saber se tem demanda pelo produto?", "Busque no ML e veja quantas vendas os anúncios concorrentes têm. Mais de 50 vendas/mês indica demanda real."),
            ("Produto barato ou caro é melhor no ML?", "Ticket de R$50 a R$300 tem melhor equilíbrio entre volume e margem. Abaixo de R$30 o frete compromete a margem; acima de R$500 o ciclo de giro é lento."),
            ("Como avaliar a concorrência antes de entrar?", "Veja preço, número de vendas, reputação dos top vendedores e se há espaço para competir com margem positiva."),
            ("Vale mais focar em poucos ou muitos produtos?", "Para iniciante: foco em 3 a 5 produtos bem escolhidos. Escalar com muitos SKUs exige mais capital e operação."),
        ],
        "content": """
<h2>Checklist de Seleção de Produto</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Critério</th><th>Mínimo aceitável</th><th>Ideal</th></tr></thead>
<tbody>
<tr><td>Margem líquida estimada</td><td>10%</td><td>&gt;20%</td></tr>
<tr><td>Vendas dos top concorrentes</td><td>30/mês</td><td>&gt;100/mês</td></tr>
<tr><td>Ticket médio</td><td>R$30</td><td>R$80 a R$300</td></tr>
<tr><td>Taxa de devolução histórica</td><td>&lt;5%</td><td>&lt;2%</td></tr>
<tr><td>Fornecedores disponíveis</td><td>2</td><td>3 ou mais</td></tr>
<tr><td>Sazonalidade</td><td>Moderada</td><td>Pouca ou previsível</td></tr>
</tbody>
</table>
</div>
<div class="callout callout-warn">
<p><strong>Evite no início:</strong> eletrônicos de alta concorrência, produtos pesados (&gt;5kg), itens com alto risco de falsificação e produtos sujeitos a regulamentação ANVISA sem experiência no setor.</p>
</div>
<h2>Como Testar Antes de Comprar Estoque Grande</h2>
<p>Compre 5 a 10 unidades, crie o anúncio, meça a conversão por 30 dias. Se o produto vender bem com margem positiva, aí sim amplie o estoque. Nunca aposte o capital total em um produto não validado. Veja mais em <a href="/como-validar-produto-mercado-livre/">Como Validar Produto no ML</a>.</p>
"""
    },
    {
        "slug":  "produtos-mais-lucrativos-mercado-livre",
        "title": "Produtos Mais Lucrativos no Mercado Livre 2025 | Nichos e Margens",
        "h1":    "Produtos Mais Lucrativos Para Vender no Mercado Livre em 2025",
        "tag":   "Produtos",
        "desc":  "Descubra quais produtos têm maior margem de lucro no Mercado Livre. Nichos com alta rentabilidade e como encontrar oportunidades pouco exploradas.",
        "lead":  "Os produtos mais vendidos no ML não são necessariamente os mais lucrativos. A real oportunidade está nos nichos com boa demanda, menor concorrência e margem acima de 25%.",
        "cta_title": "Calcule a Lucratividade Real de Cada Produto",
        "cta_desc":  "Sobrou Quanto ML mostra a margem exata de cada SKU vendido na sua loja — sem estimativa, com dados reais.",
        "links": ["nichos-lucrativos-mercado-livre","como-escolher-produto-mercado-livre","margem-ideal-mercado-livre","como-calcular-lucro-mercado-livre"],
        "faq": [
            ("Qual nicho tem maior lucro no ML?", "Acessórios premium, cosméticos de nicho, produtos para pets de raça específica e itens artesanais costumam ter margens acima de 30%."),
            ("Por que produtos caros nem sempre são mais lucrativos?", "Eletrônicos têm ticket alto mas margem de 5-10%. Um acessório de R$50 com margem de 35% pode gerar mais lucro absoluto."),
            ("Como encontrar nichos pouco explorados?", "Pesquise termos específicos no ML e veja se há poucos vendedores com muitas vendas. Isso indica demanda com baixa oferta."),
            ("Produto de marca própria é mais lucrativo?", "Geralmente sim — você controla o preço e não compete diretamente. Mas exige mais investimento inicial."),
            ("Vale a pena vender produto artesanal no ML?", "Se a escala permitir, sim. A margem costuma ser alta, mas o gargalo é a capacidade de produção."),
        ],
        "content": """
<h2>Nichos Com Alta Lucratividade no ML</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Nicho</th><th>Margem típica</th><th>Concorrência</th></tr></thead>
<tbody>
<tr><td>Acessórios para celular (premium)</td><td>30-50%</td><td>Alta — mas nichos específicos têm espaço</td></tr>
<tr><td>Produtos para pets (raças específicas)</td><td>25-45%</td><td>Média</td></tr>
<tr><td>Suplementos naturais e fitoterápicos</td><td>30-50%</td><td>Média</td></tr>
<tr><td>Ferramentas especializadas</td><td>20-35%</td><td>Baixa a média</td></tr>
<tr><td>Artigos para hobbies (RC, cosplay, etc)</td><td>25-40%</td><td>Baixa</td></tr>
<tr><td>Papelaria premium e planejadores</td><td>35-55%</td><td>Baixa</td></tr>
</tbody>
</table>
</div>
<div class="callout">
<p><strong>Princípio do nicho:</strong> É melhor ser o vendedor número 1 de "organizador para mochila de ciclismo" do que o 50º vendedor de "organizador genérico". Nicho específico = menos concorrência + cliente mais disposto a pagar.</p>
</div>
<h2>Como Calcular Se o Produto é Realmente Lucrativo</h2>
<p>Margem aparente (preço - CMV) costuma ser o dobro da margem real após comissão, frete e imposto. Antes de apostar em qualquer nicho, simule o lucro líquido real. Veja a fórmula completa em <a href="/como-calcular-lucro-mercado-livre/">Como Calcular Lucro no ML</a>.</p>
"""
    },
    {
        "slug":  "nichos-lucrativos-mercado-livre",
        "title": "Nichos Lucrativos no Mercado Livre 2025 | Oportunidades e Estratégias",
        "h1":    "Nichos Lucrativos no Mercado Livre: Como Encontrar e Explorar",
        "tag":   "Nicho",
        "desc":  "Descubra como encontrar nichos lucrativos no Mercado Livre em 2025. Metodologia de pesquisa, critérios de escolha e exemplos de nichos pouco explorados.",
        "lead":  "Nicho lucrativo não é o que todo mundo está vendendo — é o que tem demanda real, poucos vendedores de qualidade e margem suficiente para sustentar o negócio.",
        "cta_title": "Valide Seu Nicho Com Dados Reais",
        "cta_desc":  "Sobrou Quanto ML calcula se o nicho que você escolheu é financeiramente viável com base nas taxas reais do ML.",
        "links": ["produtos-mais-lucrativos-mercado-livre","como-escolher-produto-mercado-livre","como-validar-produto-mercado-livre","o-que-vender-mercado-livre"],
        "faq": [
            ("O que é nicho no contexto do ML?", "É um segmento específico do mercado com demanda própria. Em vez de 'calçado', o nicho seria 'tênis para corrida em trilha feminino'."),
            ("Como pesquisar nichos no ML?", "Use a barra de busca do ML com termos específicos. Produtos com 50-500 vendas/mês e poucos vendedores indicam nicho com espaço."),
            ("Nicho pequeno vale a pena?", "Sim, se a margem compensar. Um nicho de 200 vendas/mês com 40% de margem pode ser mais lucrativo que um de 2.000 vendas com 5%."),
            ("Como escapar da guerra de preços?", "Nicho específico, diferencial claro (embalagem, kit exclusivo, atendimento rápido) e conteúdo melhor que o concorrente."),
            ("Quando expandir para outros nichos?", "Quando o nicho atual estiver saturado (margem caindo) ou quando você tiver capital e operação para mais um SKU bem gerido."),
        ],
        "content": """
<h2>Metodologia Para Encontrar Nicho Lucrativo</h2>
<ol>
<li><strong>Escolha uma categoria ampla</strong> que você conhece ou tem fornecedor</li>
<li><strong>Busque no ML</strong> termos específicos dentro dessa categoria</li>
<li><strong>Filtre por mais vendidos</strong> e analise o número de vendas dos top 5</li>
<li><strong>Calcule a margem estimada</strong> para o preço praticado</li>
<li><strong>Avalie a qualidade dos concorrentes</strong> — há espaço para entrar melhor?</li>
<li><strong>Valide com pequeno estoque</strong> antes de escalar</li>
</ol>
<div class="callout callout-green">
<p><strong>Sinal de nicho com oportunidade:</strong> top vendedor tem mais de 100 vendas/mês mas avaliações mediocres (3-4 estrelas). Significa demanda real com execução ruim — espaço para entrar com qualidade.</p>
</div>
<h2>Exemplos de Nichos Subexplorados em 2025</h2>
<ul>
<li>Acessórios para van-life e camping minimalista</li>
<li>Produtos de organização para home office compacto</li>
<li>Itens de costura e bordado (comunidade crescente)</li>
<li>Acessórios para instrumentos musicais específicos</li>
<li>Produtos para raças de pets menos comuns</li>
</ul>
"""
    },
    {
        "slug":  "o-que-vender-mercado-livre",
        "title": "O Que Vender no Mercado Livre em 2025 | Guia de Produtos",
        "h1":    "O Que Vender no Mercado Livre: Guia Para Escolher Seus Produtos",
        "tag":   "Produtos",
        "desc":  "Descubra o que vender no Mercado Livre em 2025. Critérios de seleção, produtos em alta, nichos com oportunidade e como validar antes de comprar estoque.",
        "lead":  "A resposta para o que vender no ML não está numa lista pronta — está na intersecção entre demanda do mercado, sua capacidade de fornecimento e a margem que o produto proporciona.",
        "cta_title": "Calcule o Potencial de Lucro Antes de Vender",
        "cta_desc":  "Sobrou Quanto ML simula o lucro real de qualquer produto considerando as taxas reais do ML e seu regime tributário.",
        "links": ["como-escolher-produto-mercado-livre","produtos-mais-lucrativos-mercado-livre","nichos-lucrativos-mercado-livre","como-validar-produto-mercado-livre"],
        "faq": [
            ("O que está em alta para vender no ML?", "Produtos para home office, saúde e bem-estar, sustentabilidade, pets e tecnologia portátil estão em crescimento consistente."),
            ("O que não vender no ML?", "Produtos falsificados (proibido), itens com restrição regulatória sem habilitação, e produtos com margem negativa após calcular todos os custos."),
            ("Precisa ter CNPJ para vender qualquer produto?", "Não para a maioria. Mas alguns produtos (alimentos, cosméticos, remédios) exigem habilitação específica independente do CNPJ."),
            ("Vale vender produto usado no ML?", "Sim, o ML tem categoria específica para usados. A margem pode ser alta, mas o volume e a padronização são desafios."),
            ("Como começar do zero sem muito capital?", "Comece com dropshipping nacional ou produtos de baixo custo e giro rápido. O foco inicial é aprender a operação, não o volume."),
        ],
        "content": """
<h2>Framework de Decisão: O Que Vender</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">📊</div><h4>Tem demanda?</h4><p>Concorrentes com 50+ vendas/mês confirmam que existe mercado</p></div>
<div class="benefit-card"><div class="b-icon">💰</div><h4>Tem margem?</h4><p>Margem líquida acima de 15% após todos os custos do ML</p></div>
<div class="benefit-card"><div class="b-icon">🏭</div><h4>Tem fornecedor?</h4><p>Pelo menos 2 fontes confiáveis com preço e prazo previsíveis</p></div>
<div class="benefit-card"><div class="b-icon">⚡</div><h4>Tem diferencial?</h4><p>Algo que te separa dos 50 concorrentes que já vendem o mesmo</p></div>
</div>
<h2>Produtos Para Evitar Como Iniciante</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Tipo</th><th>Por que evitar</th></tr></thead>
<tbody>
<tr><td>Eletrônicos premium</td><td>Margem apertada, alto risco de devolução por defeito</td></tr>
<tr><td>Produtos pesados (&gt;10kg)</td><td>Frete alto compromete margem</td></tr>
<tr><td>Moda sem diferencial</td><td>Guerra de preço intensa, devolução alta</td></tr>
<tr><td>Produtos sazonais puros</td><td>Estoque parado 10 meses no ano</td></tr>
</tbody>
</table>
</div>
"""
    },
    {
        "slug":  "como-validar-produto-mercado-livre",
        "title": "Como Validar Produto Antes de Vender no Mercado Livre | 2025",
        "h1":    "Como Validar Um Produto Antes de Comprar Estoque no Mercado Livre",
        "tag":   "Validação",
        "desc":  "Aprenda como validar um produto no Mercado Livre antes de investir em estoque. Metodologia simples, métricas e como evitar prejuízo com produto errado.",
        "lead":  "Comprar estoque sem validar é o erro mais caro no ML. A validação correta leva menos de 30 dias e custa uma fração do que um estoque parado.",
        "cta_title": "Valide Com Dados Reais de Margem",
        "cta_desc":  "Sobrou Quanto ML calcula a margem real do produto antes mesmo de você criar o anúncio — use os dados para decidir.",
        "links": ["como-escolher-produto-mercado-livre","produtos-mais-lucrativos-mercado-livre","calculadora-margem-mercado-livre","simulador-lucro-mercado-livre"],
        "faq": [
            ("O que é validar um produto?", "É testar se o produto vende com margem positiva antes de comprar estoque grande. Começa com poucas unidades e mede resultado real."),
            ("Quanto tempo leva a validação?", "30 dias são suficientes para saber se o produto tem demanda. 60 dias para entender sazonalidade e taxa de devolução real."),
            ("Como validar sem estoque inicial?", "Dropshipping com fornecedor nacional permite anunciar sem estoque. Mas atenção: prazo de entrega maior pode impactar reputação."),
            ("Que métricas acompanhar durante validação?", "Cliques no anúncio, taxa de conversão (pedidos ÷ visitas), margem real por venda e taxa de devolução."),
            ("Quando escalar após validação?", "Quando tiver pelo menos 30 vendas com margem positiva consistente e taxa de devolução abaixo de 4%."),
        ],
        "content": """
<h2>Processo de Validação em 4 Etapas</h2>
<h3>Etapa 1 — Pesquisa (1 semana)</h3>
<p>Busque o produto no ML. Analise os top 5 anúncios: preço, número de vendas, avaliações. Calcule a margem estimada para o preço de mercado. Se a margem for abaixo de 10%, pare aqui.</p>
<h3>Etapa 2 — Teste mínimo (2-4 semanas)</h3>
<p>Compre 5 a 15 unidades. Crie o anúncio com qualidade (fotos boas, título otimizado). Anuncie pelo preço de mercado — sem tentar ser o mais barato.</p>
<h3>Etapa 3 — Análise (ao final do período)</h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Métrica</th><th>Sinal verde</th><th>Sinal vermelho</th></tr></thead>
<tbody>
<tr><td>Vendas em 30 dias</td><td>&gt;10 unidades</td><td>&lt;3 unidades</td></tr>
<tr><td>Margem real por venda</td><td>&gt;15%</td><td>&lt;8%</td></tr>
<tr><td>Taxa de devolução</td><td>&lt;3%</td><td>&gt;6%</td></tr>
<tr><td>Avaliações recebidas</td><td>4+ estrelas</td><td>Muitas reclamações</td></tr>
</tbody>
</table>
</div>
<h3>Etapa 4 — Decisão</h3>
<p>Sinal verde em todas as métricas: compre estoque maior. Sinal misto: ajuste e reteste. Sinal vermelho: encerre sem expandir.</p>
"""
    },
    {
        "slug":  "como-criar-anuncio-mercado-livre",
        "title": "Como Criar Anúncio no Mercado Livre 2025 | Guia Completo",
        "h1":    "Como Criar um Anúncio no Mercado Livre Que Vende de Verdade",
        "tag":   "Anúncio",
        "desc":  "Guia completo para criar anúncios no Mercado Livre que aparecem nos primeiros resultados e convertem visitantes em compradores.",
        "lead":  "Criar um anúncio no ML é simples. Criar um anúncio que aparece no topo e converte é uma combinação de título otimizado, fotos de qualidade e precificação correta.",
        "cta_title": "Anúncio Lucrativo Começa Com Margem Correta",
        "cta_desc":  "Sobrou Quanto ML garante que o preço do seu anúncio cobre todos os custos. Conecte e veja a margem real antes de publicar.",
        "links": ["como-otimizar-anuncio-mercado-livre","titulo-perfeito-anuncio-mercado-livre","seo-mercado-livre","precificacao-mercado-livre"],
        "faq": [
            ("Qual a estrutura de um bom anúncio no ML?", "Título com keyword principal + características, fotos profissionais, descrição completa, categoria correta e preço competitivo com margem positiva."),
            ("Quantas fotos colocar no anúncio?", "Mínimo 6: frente, verso, lateral, detalhe, em uso e embalagem. Anúncios com mais fotos têm maior taxa de conversão."),
            ("Como escolher a categoria correta?", "Categorias erradas cobram comissão diferente e reduzem visibilidade. Use a sugestão do ML mas confirme manualmente."),
            ("Devo usar vídeo no anúncio?", "Sim, quando possível. Vídeos aumentam o tempo de permanência na página e a taxa de conversão, especialmente para produtos com demonstração."),
            ("Como calcular o preço do anúncio?", "Nunca de forma intuitiva. Use a fórmula: CMV ÷ (1 - comissão - frete - imposto - margem desejada). Veja em como precificar produto ML."),
        ],
        "content": """
<h2>Anatomia de um Anúncio de Alta Conversão</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">📝</div><h4>Título</h4><p>Keyword principal + marca + modelo + característica — máximo 60 caracteres relevantes</p></div>
<div class="benefit-card"><div class="b-icon">📸</div><h4>Fotos</h4><p>Fundo branco, alta resolução, mínimo 6 ângulos — sem texto sobreposto</p></div>
<div class="benefit-card"><div class="b-icon">📋</div><h4>Descrição</h4><p>Especificações completas, para que serve, o que inclui — sem erros de português</p></div>
<div class="benefit-card"><div class="b-icon">💰</div><h4>Preço</h4><p>Competitivo mas com margem calculada — nunca abaixo do preço mínimo viável</p></div>
</div>
<h2>Erros Que Destroem um Anúncio</h2>
<ul>
<li>Título genérico sem keyword de busca</li>
<li>Foto de baixa qualidade ou com marca d'água</li>
<li>Categoria errada (paga comissão errada + perde visibilidade)</li>
<li>Descrição copiada de outro anúncio (ML pode penalizar)</li>
<li>Preço abaixo do custo por não calcular corretamente</li>
</ul>
<div class="callout">
<p>Para o título perfeito, veja: <a href="/titulo-perfeito-anuncio-mercado-livre/">Título Perfeito Para Anúncio no ML</a>.</p>
</div>
"""
    },
    {
        "slug":  "como-otimizar-anuncio-mercado-livre",
        "title": "Como Otimizar Anúncio no Mercado Livre 2025 | Apareça no Topo",
        "h1":    "Como Otimizar Seu Anúncio no Mercado Livre Para Aparecer no Topo",
        "tag":   "Otimização",
        "desc":  "Aprenda como otimizar anúncios no Mercado Livre para melhorar o posicionamento, aumentar conversão e vender mais sem reduzir preço.",
        "lead":  "Otimizar um anúncio no ML não é só adicionar mais palavras no título. É um processo que envolve dados de conversão, análise da concorrência e melhorias contínuas baseadas em resultado.",
        "cta_title": "Otimize Seus Anúncios Com Dados Reais",
        "cta_desc":  "Sobrou Quanto ML mostra quais anúncios têm menor margem e maior devolução — para você priorizar a otimização certa.",
        "links": ["como-criar-anuncio-mercado-livre","seo-mercado-livre","titulo-perfeito-anuncio-mercado-livre","como-aparecer-primeiro-mercado-livre"],
        "faq": [
            ("O que o algoritmo do ML considera para ranking?", "Histórico de vendas, taxa de conversão, reputação do vendedor, preço competitivo, tempo de resposta e qualidade do anúncio."),
            ("Devo criar anúncio novo ou otimizar o existente?", "Otimize o existente se ele já tem histórico de vendas. Criar novo zera o histórico e prejudica o ranking no início."),
            ("Mudar o título prejudica o anúncio?", "Mudanças pequenas e frequentes podem ajudar. Mudança radical de título pode reduzir temporariamente o posicionamento."),
            ("Product Ads melhora o posicionamento orgânico?", "Não diretamente. Mas se o anúncio patrocinado gera mais vendas, o histórico de conversão melhora o ranking orgânico."),
            ("Com que frequência otimizar?", "Revise os anúncios de maior volume mensalmente. Anúncios estagnados (sem vendas em 15 dias) precisam de análise imediata."),
        ],
        "content": """
<h2>O Que Otimizar e Em Que Ordem</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Elemento</th><th>Impacto</th><th>Como otimizar</th></tr></thead>
<tbody>
<tr><td>Título</td><td>Alto</td><td>Keyword exata no início, características relevantes</td></tr>
<tr><td>Fotos</td><td>Alto</td><td>Profissional, múltiplos ângulos, em uso</td></tr>
<tr><td>Preço</td><td>Alto</td><td>Competitivo mas dentro da margem mínima</td></tr>
<tr><td>Reputação</td><td>Alto</td><td>Resposta rápida, envio no prazo, embalagem adequada</td></tr>
<tr><td>Estoque</td><td>Médio</td><td>Manter &gt;5 unidades — abaixo disso perde posição</td></tr>
<tr><td>Descrição</td><td>Médio</td><td>Completa, sem erros, com especificações técnicas</td></tr>
</tbody>
</table>
</div>
<div class="callout callout-green">
<p><strong>Prioridade:</strong> Se o anúncio tem poucas visitas, o problema é título ou categoria. Se tem visitas mas pouca conversão, o problema é foto, preço ou descrição.</p>
</div>
<h2>Análise de Concorrência Para Otimização</h2>
<p>Analise os 3 primeiros resultados da busca para sua keyword. Veja o que eles têm de diferente: preço, fotos, título. Seu objetivo não é copiar — é fazer melhor em pelo menos 2 desses pontos.</p>
"""
    },
    {
        "slug":  "seo-mercado-livre",
        "title": "SEO no Mercado Livre 2025 | Como Aparecer Nos Primeiros Resultados",
        "h1":    "SEO no Mercado Livre: Como Funciona e Como Usar a Seu Favor",
        "tag":   "SEO",
        "desc":  "Entenda como funciona o SEO do Mercado Livre e como otimizar seus anúncios para aparecer nos primeiros resultados de busca da plataforma.",
        "lead":  "O ML tem seu próprio algoritmo de busca — e entender como ele funciona é a diferença entre aparecer na primeira página ou na décima. Não é sobre pagar mais, é sobre relevância.",
        "cta_title": "Venda Mais Com Anúncios Bem Posicionados",
        "cta_desc":  "Sobrou Quanto ML ajuda você a identificar quais produtos merecem mais investimento em otimização com base na margem real.",
        "links": ["como-aparecer-primeiro-mercado-livre","como-otimizar-anuncio-mercado-livre","titulo-perfeito-anuncio-mercado-livre","como-melhorar-ranking-mercado-livre"],
        "faq": [
            ("O ML tem SEO como o Google?", "Sim, mas com critérios diferentes. O ML prioriza: histórico de vendas, conversão, preço competitivo e reputação do vendedor."),
            ("Keyword no título realmente ajuda?", "Sim. O algoritmo do ML usa o título para indexar o anúncio. Keyword exata no início do título aumenta a chance de aparecer na busca."),
            ("Pagar Product Ads melhora o SEO orgânico?", "Indiretamente. Mais vendas via patrocinado aumentam o histórico, que melhora o ranking orgânico."),
            ("Quantas keywords colocar no título?", "1 principal + 1 ou 2 complementares. Não encha o título de keywords — o ML pode penalizar anúncios com títulos sem sentido."),
            ("SEO do ML muda com frequência?", "Sim. O algoritmo é atualizado periodicamente. Acompanhe as comunicações oficiais do ML para vendedores."),
        ],
        "content": """
<h2>Os Fatores de Ranking do ML</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Fator</th><th>Peso</th><th>Como melhorar</th></tr></thead>
<tbody>
<tr><td>Histórico de vendas</td><td>Muito alto</td><td>Mais vendas = mais visibilidade (ciclo virtuoso)</td></tr>
<tr><td>Taxa de conversão</td><td>Alto</td><td>Fotos, preço e título que convertem visitantes</td></tr>
<tr><td>Reputação do vendedor</td><td>Alto</td><td>Verde = vantagem; Amarelo/vermelho = desvantagem</td></tr>
<tr><td>Relevância do título</td><td>Alto</td><td>Keyword exata do que o comprador busca</td></tr>
<tr><td>Preço vs concorrência</td><td>Médio</td><td>Competitivo — não necessariamente o menor</td></tr>
<tr><td>Tempo de envio</td><td>Médio</td><td>Full e envio rápido têm vantagem</td></tr>
</tbody>
</table>
</div>
<div class="callout">
<p><strong>O ciclo virtuoso do SEO no ML:</strong> Bom título → mais cliques → mais vendas → histórico maior → melhor posição → mais cliques. Entrar nesse ciclo é o objetivo.</p>
</div>
<h2>SEO no Título: Como Estruturar</h2>
<p>[Keyword principal] + [Marca/Modelo] + [Característica 1] + [Característica 2]</p>
<p>Exemplo ruim: "Fone Bluetooth Bom Barato Promoção"<br>
Exemplo bom: "Fone Bluetooth JBL Tune 510 Sem Fio 40h Bateria"</p>
"""
    },
    {
        "slug":  "como-aparecer-primeiro-mercado-livre",
        "title": "Como Aparecer Primeiro no Mercado Livre 2025 | Guia de Ranking",
        "h1":    "Como Aparecer Primeiro nos Resultados do Mercado Livre",
        "tag":   "Ranking",
        "desc":  "Aprenda as estratégias mais eficazes para aparecer nos primeiros resultados do Mercado Livre e aumentar suas vendas organicamente.",
        "lead":  "Aparecer primeiro no ML não é questão de sorte. É o resultado de um conjunto de fatores que o algoritmo avalia — e que você pode trabalhar sistematicamente.",
        "cta_title": "Identifique Quais Anúncios Merecem Mais Foco",
        "cta_desc":  "Sobrou Quanto ML mostra quais produtos têm maior margem e deveriam estar no topo das suas otimizações.",
        "links": ["seo-mercado-livre","como-otimizar-anuncio-mercado-livre","como-melhorar-ranking-mercado-livre","buy-box-mercado-livre"],
        "faq": [
            ("Dá para aparecer primeiro sem pagar Product Ads?", "Sim. O posicionamento orgânico depende de histórico de vendas, conversão e reputação — não de anúncio pago."),
            ("Quanto tempo leva para aparecer no topo?", "Com otimizações corretas e vendas consistentes, entre 30 e 90 dias para subir significativamente no ranking."),
            ("Produto novo pode aparecer no topo?", "No início é difícil — não há histórico. Use Product Ads no início para gerar as primeiras vendas e construir histórico."),
            ("Ser o mais barato garante primeiro lugar?", "Não. O ML equilibra preço com qualidade do anúncio e reputação. Ser levemente mais caro que o mais barato mas com anúncio melhor pode render melhor posição."),
            ("Como a reputação afeta o posicionamento?", "Reputação verde tem vantagem de ranking. Amarela e vermelha são penalizadas no algoritmo de busca."),
        ],
        "content": """
<h2>Estratégia Para Subir No Ranking</h2>
<h3>Fase 1 — Fundação (primeiras 2 semanas)</h3>
<ul>
<li>Título com keyword exata que os compradores buscam</li>
<li>Fotos profissionais — mínimo 6</li>
<li>Preço dentro da faixa competitiva (não precisa ser o menor)</li>
<li>Estoque mínimo de 10 unidades para não perder posição</li>
</ul>
<h3>Fase 2 — Aceleração (semanas 2 a 8)</h3>
<ul>
<li>Ativar Product Ads para gerar vendas iniciais</li>
<li>Responder perguntas em menos de 2 horas</li>
<li>Enviar no prazo em 100% dos pedidos</li>
<li>Solicitar avaliação após entrega confirmada</li>
</ul>
<div class="callout callout-green">
<p><strong>Foco no que mais importa:</strong> as primeiras 50 vendas de um produto são as mais difíceis e mais importantes. Invista em Product Ads nessa fase — o retorno é o histórico que coloca o anúncio no topo organicamente.</p>
</div>
"""
    },
    {
        "slug":  "como-melhorar-ranking-mercado-livre",
        "title": "Como Melhorar o Ranking no Mercado Livre 2025 | Estratégias Práticas",
        "h1":    "Como Melhorar o Ranking dos Seus Anúncios no Mercado Livre",
        "tag":   "Ranking",
        "desc":  "Estratégias práticas para melhorar o ranking dos seus anúncios no Mercado Livre. Otimização de título, conversão, reputação e outros fatores de posicionamento.",
        "lead":  "Melhorar o ranking no ML é um processo contínuo — não existe uma única ação que coloca você no topo para sempre. É a soma de vários fatores bem executados.",
        "cta_title": "Foque Nas Otimizações Que Aumentam Lucro",
        "cta_desc":  "Sobrou Quanto ML identifica quais produtos têm melhor margem para você priorizar os esforços de otimização.",
        "links": ["seo-mercado-livre","como-aparecer-primeiro-mercado-livre","como-otimizar-anuncio-mercado-livre","reputacao-mercado-livre"],
        "faq": [
            ("O que mais prejudica o ranking no ML?", "Reputação abaixo de verde, alta taxa de cancelamento, devolução acima da média e anúncio sem vendas por mais de 30 dias."),
            ("Deletar e criar anúncio novo melhora ranking?", "Não — você perde o histórico. Otimize o anúncio existente sempre que possível."),
            ("Promoção temporária melhora ranking?", "Sim. Um burst de vendas durante uma promoção pode melhorar o histórico e sustentar melhor posição após o fim da promoção."),
            ("Responder mais rápido afeta ranking?", "Tempo de resposta a perguntas é fator de reputação, que afeta indiretamente o ranking. Resposta rápida = melhor reputação = melhor posição."),
            ("Como saber se meu ranking melhorou?", "Busque sua keyword no ML como comprador e veja em qual posição seu anúncio aparece. Compare semana a semana."),
        ],
        "content": """
<h2>Ações de Maior Impacto no Ranking</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Ação</th><th>Impacto</th><th>Prazo para resultado</th></tr></thead>
<tbody>
<tr><td>Melhorar taxa de conversão</td><td>Alto</td><td>2-4 semanas</td></tr>
<tr><td>Manter reputação verde</td><td>Alto</td><td>Contínuo</td></tr>
<tr><td>Aumentar volume de vendas</td><td>Alto</td><td>4-8 semanas</td></tr>
<tr><td>Otimizar título com keyword</td><td>Médio-alto</td><td>1-2 semanas</td></tr>
<tr><td>Melhorar fotos</td><td>Médio</td><td>1-3 semanas</td></tr>
<tr><td>Aumentar estoque disponível</td><td>Médio</td><td>Imediato</td></tr>
</tbody>
</table>
</div>
<div class="callout callout-warn">
<p><strong>O que NÃO fazer:</strong> comprar avaliações, usar titles com spam de keywords, criar múltiplos anúncios do mesmo produto. Essas práticas violam as políticas do ML e podem resultar em suspensão.</p>
</div>
"""
    },
    {
        "slug":  "titulo-perfeito-anuncio-mercado-livre",
        "title": "Título Perfeito Para Anúncio no Mercado Livre 2025 | Como Criar",
        "h1":    "Como Criar o Título Perfeito Para Seu Anúncio no Mercado Livre",
        "tag":   "Anúncio",
        "desc":  "Aprenda a estrutura do título perfeito para anúncios no Mercado Livre. Como incluir keywords, características e o que evitar para ranquear melhor.",
        "lead":  "O título é o elemento mais importante do anúncio no ML para o algoritmo de busca. Errar o título significa não ser encontrado — independente de ter o melhor produto ao melhor preço.",
        "cta_title": "Anúncio Certo, Margem Calculada",
        "cta_desc":  "Sobrou Quanto ML garante que o preço do seu anúncio está cobrindo todos os custos. Otimize o título e a margem juntos.",
        "links": ["seo-mercado-livre","como-criar-anuncio-mercado-livre","como-otimizar-anuncio-mercado-livre","como-aparecer-primeiro-mercado-livre"],
        "faq": [
            ("Qual o limite de caracteres no título do ML?", "O ML permite até 60 caracteres no título. Use todos — cada caractere relevante ajuda na indexação."),
            ("Devo colocar marca no título?", "Sim, se for uma marca conhecida que os compradores buscam. Se for marca própria sem reconhecimento, priorize a descrição do produto."),
            ("Palavras promocionais (grátis, barato) ajudam?", "Não. O ML não indexa essas palavras como keywords de produto e podem prejudicar a credibilidade do anúncio."),
            ("Como descobrir a keyword certa para o título?", "Busque o produto no ML como comprador e veja quais termos os anúncios de maior venda usam no início do título."),
            ("Usar vírgulas e símbolos no título prejudica?", "Evite símbolos. Use espaços entre características. Títulos limpos e legíveis têm melhor desempenho."),
        ],
        "content": """
<h2>A Estrutura do Título Vencedor</h2>
<div class="callout callout-green">
<p><strong>Fórmula:</strong> [Produto] + [Marca] + [Modelo/Versão] + [Característica principal] + [Característica secundária]</p>
<p><strong>Exemplo:</strong> "Tênis Masculino Nike Air Max 270 Corrida Academia Preto"</p>
</div>
<h2>Comparativo: Títulos Fracos vs Fortes</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Título fraco</th><th>Por que não funciona</th><th>Título forte</th></tr></thead>
<tbody>
<tr><td>Tênis Barato Promoção</td><td>Sem keyword, sem especificação</td><td>Tênis Masculino Running Leve Amortecimento Corrida</td></tr>
<tr><td>Fone Top Qualidade</td><td>Genérico, sem busca</td><td>Fone Bluetooth Over-ear 30h Bateria Cancelamento Ruído</td></tr>
<tr><td>Capa Celular</td><td>Sem modelo do celular</td><td>Capa iPhone 15 Pro Silicone Antichoque Proteção Câmera</td></tr>
</tbody>
</table>
</div>
<h2>Como Pesquisar as Melhores Keywords</h2>
<ol>
<li>Busque o produto no ML como comprador — veja os termos dos top anúncios</li>
<li>Observe as sugestões automáticas de busca do ML</li>
<li>Analise os títulos dos 3 primeiros resultados com mais vendas</li>
<li>Identifique a keyword comum que todos usam no início</li>
</ol>
"""
    },
    {
        "slug":  "descricao-produto-mercado-livre",
        "title": "Descrição Perfeita de Produto no Mercado Livre 2025 | Como Criar",
        "h1":    "Como Criar a Descrição Perfeita de Produto no Mercado Livre",
        "tag":   "Anúncio",
        "desc":  "Aprenda a escrever descrições de produto que vendem no Mercado Livre. Estrutura, o que incluir, como reduzir devolução e melhorar conversão.",
        "lead":  "A descrição do produto no ML não é só texto de preenchimento — é a última chance de convencer o comprador e a primeira linha de defesa contra devoluções por produto diferente do anunciado.",
        "cta_title": "Menos Devolução, Mais Lucro",
        "cta_desc":  "Sobrou Quanto ML mostra quais produtos têm maior taxa de devolução para você priorizar a melhoria da descrição.",
        "links": ["como-criar-anuncio-mercado-livre","titulo-perfeito-anuncio-mercado-livre","devolucoes-mercado-livre","como-otimizar-anuncio-mercado-livre"],
        "faq": [
            ("O que deve ter na descrição?", "Especificações técnicas completas, dimensões, materiais, para que serve, o que está incluso na embalagem e instruções básicas de uso."),
            ("Descrição longa é melhor?", "Completa é melhor que longa. Organize em tópicos curtos — compradores escaneiam, não leem. Bullet points funcionam melhor que parágrafos."),
            ("Fotos substituem a descrição?", "Complementam, mas não substituem. A descrição indexa keywords adicionais e protege contra disputas ('o produto está descrito exatamente como vendido')."),
            ("Como reduzir devolução com a descrição?", "Seja preciso nas dimensões e cores. Inclua comparação de tamanho com objeto cotidiano. Avise sobre limitações do produto claramente."),
            ("Copiar descrição de concorrente é problema?", "Sim. O ML pode penalizar conteúdo duplicado. Escreva a descrição original, mesmo que o produto seja igual."),
        ],
        "content": """
<h2>Estrutura da Descrição Que Converte</h2>
<ol>
<li><strong>Benefício principal</strong> — primeira linha: o que o produto faz pelo comprador</li>
<li><strong>Especificações técnicas</strong> — dimensões, peso, material, voltagem</li>
<li><strong>O que está incluso</strong> — lista completa do que vem na embalagem</li>
<li><strong>Como usar / Indicações</strong> — para quem é e para que serve</li>
<li><strong>O que NÃO está incluso</strong> — evita reclamação "não veio o X"</li>
<li><strong>Informações de compatibilidade</strong> — modelos, tamanhos, versões</li>
</ol>
<div class="callout callout-warn">
<p><strong>Proteção jurídica:</strong> Uma descrição precisa e completa protege o vendedor em disputas na plataforma. "Está descrito que não inclui adaptador" é argumento válido para reverter reclamação.</p>
</div>
<h2>Erros Que Causam Devolução</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Erro na descrição</th><th>Consequência</th></tr></thead>
<tbody>
<tr><td>Cor diferente da foto</td><td>Devolução por "produto diferente"</td></tr>
<tr><td>Dimensão imprecisa</td><td>Devolução por "não serve"</td></tr>
<tr><td>Compatibilidade não informada</td><td>Devolução por "não funciona no meu aparelho"</td></tr>
<tr><td>Itens da embalagem não listados</td><td>Reclamação de "veio incompleto"</td></tr>
</tbody>
</table>
</div>
"""
    },
    {
        "slug":  "como-ter-mais-visitas-mercado-livre",
        "title": "Como Ter Mais Visitas no Mercado Livre 2025 | Aumente o Tráfego",
        "h1":    "Como Ter Mais Visitas nos Seus Anúncios do Mercado Livre",
        "tag":   "Tráfego",
        "desc":  "Estratégias para aumentar as visitas nos seus anúncios do Mercado Livre. Como melhorar o ranking, usar publicidade e atrair mais compradores.",
        "lead":  "Mais visitas sem conversão não serve para nada. Mas sem visitas não há vendas. O equilíbrio está em atrair o público certo — compradores com intenção real de compra.",
        "cta_title": "Mais Visitas + Margem Controlada = Crescimento Real",
        "cta_desc":  "Sobrou Quanto ML garante que cada venda gerada pelo aumento de tráfego está sendo lucrativa.",
        "links": ["seo-mercado-livre","como-aparecer-primeiro-mercado-livre","como-melhorar-ranking-mercado-livre","como-ter-mais-vendas-mercado-livre"],
        "faq": [
            ("Como aumentar visitas no anúncio do ML?", "Título com keyword correta, posicionamento no topo (ranking), Product Ads e compartilhamento externo (redes sociais, links)."),
            ("Product Ads garante mais visitas?", "Sim, imediatamente — mas com custo. Calcule se o aumento de vendas paga o custo de publicidade (ROAS)."),
            ("Dá para trazer tráfego externo para o ML?", "Sim. Links diretos para o anúncio em redes sociais, WhatsApp e e-mail marketing direcionam tráfego externo."),
            ("Visitas sem venda indica qual problema?", "Preço acima do mercado, foto ruim, descrição incompleta ou produto errado para o público que está buscando."),
            ("Como calcular a taxa de conversão?", "Pedidos ÷ visitas × 100. Uma boa taxa de conversão no ML fica entre 1% e 5% dependendo da categoria."),
        ],
        "content": """
<h2>Fontes de Tráfego Para Seus Anúncios</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">🔍</div><h4>Busca orgânica ML</h4><p>Comprador busca no ML e encontra seu anúncio — melhor qualidade de tráfego</p></div>
<div class="benefit-card"><div class="b-icon">📢</div><h4>Product Ads</h4><p>Patrocinado dentro do ML — pago por clique, resultado imediato</p></div>
<div class="benefit-card"><div class="b-icon">📱</div><h4>Redes sociais</h4><p>Links diretos para o anúncio via Instagram, WhatsApp, TikTok</p></div>
<div class="benefit-card"><div class="b-icon">📧</div><h4>E-mail marketing</h4><p>Base de compradores anteriores — maior taxa de conversão</p></div>
</div>
<h2>Visitas vs Conversão: O Que Priorizar</h2>
<p>Antes de investir em tráfego pago, certifique-se que a taxa de conversão orgânica está boa. Se o anúncio converte 0,5%, dobrar o tráfego vai gerar 1% de vendas. Se converter 3%, o mesmo investimento em tráfego traz 6x mais resultado.</p>
<div class="callout">
<p>Regra: optimize a conversão primeiro, depois escale o tráfego. Investir em tráfego para anúncio que não converte é jogar dinheiro fora.</p>
</div>
"""
    },
    {
        "slug":  "como-ter-mais-vendas-mercado-livre",
        "title": "Como Ter Mais Vendas no Mercado Livre 2025 | Estratégias Comprovadas",
        "h1":    "Como Ter Mais Vendas no Mercado Livre: Estratégias Que Funcionam",
        "tag":   "Vendas",
        "desc":  "Aprenda estratégias comprovadas para aumentar as vendas no Mercado Livre sem necessariamente reduzir preço ou aumentar investimento em publicidade.",
        "lead":  "Mais vendas no ML vêm de três fontes: mais tráfego, melhor conversão e maior ticket médio. Trabalhar os três simultaneamente é a forma mais eficiente de crescer.",
        "cta_title": "Cresça Com Margem Controlada",
        "cta_desc":  "Sobrou Quanto ML garante que o crescimento de vendas está gerando mais lucro — não apenas mais faturamento.",
        "links": ["como-vender-mais-mercado-livre","escalar-vendas-mercado-livre","ticket-medio-mercado-livre","reputacao-mercado-livre"],
        "faq": [
            ("Qual a forma mais rápida de aumentar vendas?", "Product Ads nos anúncios com maior margem. Resultado imediato, mas tem custo. Calcule o ROAS mínimo antes de ativar."),
            ("Dar desconto é a melhor estratégia?", "Geralmente não. Desconto reduz margem e pode virar guerra de preço. Invista em qualidade do anúncio antes de reduzir preço."),
            ("Como aproveitar datas sazonais?", "Prepare estoque com antecedência, atualize fotos e títulos, e ative Product Ads 1 semana antes das datas comemorativas."),
            ("Kits e combos aumentam vendas?", "Sim e com margem melhor. Um kit de R$150 tem menos frete proporcional que dois pedidos de R$75 separados."),
            ("Como recuperar vendas estagnadas?", "Revise título, fotos e preço em relação aos concorrentes. Se nada mudar, considere pausar e criar anúncio novo com melhorias."),
        ],
        "content": """
<h2>As 3 Alavancas de Vendas no ML</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Alavanca</th><th>Como ativar</th><th>Impacto na margem</th></tr></thead>
<tbody>
<tr><td>Mais tráfego</td><td>SEO + Product Ads</td><td>Neutro (custo de ads pode reduzir)</td></tr>
<tr><td>Melhor conversão</td><td>Fotos + título + preço</td><td>Positivo — mesmo custo, mais vendas</td></tr>
<tr><td>Maior ticket médio</td><td>Kits + combos + upsell</td><td>Positivo — dilui frete e custo fixo</td></tr>
</tbody>
</table>
</div>
<div class="callout callout-green">
<p><strong>Estratégia de maior ROI:</strong> Melhore a conversão antes de pagar por mais tráfego. Um anúncio que converte 4% com 1.000 visitas vende 40 itens. O mesmo tráfego com conversão de 1% vende só 10 — e você pagaria 4x mais em ads para o mesmo resultado.</p>
</div>
<h2>Crescer com Margem ou Crescer no Prejuízo</h2>
<p>Vendas mais não é sinônimo de lucro mais. Sempre monitore a margem líquida enquanto escala. Se as vendas aumentam mas a margem cai, há um vazamento financeiro a identificar — geralmente em frete, devolução ou imposto que subiu de faixa. Veja mais em <a href="/como-calcular-lucro-mercado-livre/">Como Calcular Lucro no ML</a>.</p>
"""
    },
    {
        "slug":  "ideias-produtos-mercado-livre",
        "title": "Ideias de Produtos Para Vender no Mercado Livre 2025 | 20 Nichos",
        "h1":    "20 Ideias de Produtos Para Vender no Mercado Livre em 2025",
        "tag":   "Produtos",
        "desc":  "Lista com 20 ideias de produtos para vender no Mercado Livre em 2025. Nichos em crescimento, margem estimada e como validar antes de comprar estoque.",
        "lead":  "Mais do que uma lista de produtos, o que você precisa é de um método para avaliar se qualquer ideia é viável para o seu contexto — capital, fornecedor e operação.",
        "cta_title": "Calcule Se a Ideia é Financeiramente Viável",
        "cta_desc":  "Sobrou Quanto ML simula o lucro real de qualquer produto com as taxas reais do ML e seu regime tributário.",
        "links": ["nichos-lucrativos-mercado-livre","como-escolher-produto-mercado-livre","como-validar-produto-mercado-livre","produtos-mais-lucrativos-mercado-livre"],
        "faq": [
            ("Como transformar uma ideia em produto viável?", "Pesquise demanda no ML, calcule a margem estimada, encontre fornecedor e valide com pequeno estoque antes de escalar."),
            ("Copiar o que concorrente vende é estratégia válida?", "Entrar em mercados validados é estratégia — mas você precisa de diferencial. Produto igual ao concorrente sem diferencial vira guerra de preço."),
            ("Como saber se a ideia já é saturada?", "Se os top 10 vendedores têm centenas de avaliações e o menor preço já está na margem mínima, o nicho está saturado para iniciantes."),
            ("Vale a pena vender produtos sazonais?", "Sim se você planejou o estoque. O risco é comprar muito e não vender fora da temporada."),
            ("Onde buscar ideias de produtos?", "Pinterest trends, Google Trends, TikTok, grupos de compradores no Facebook e própria busca do ML com filtro 'mais vendidos'."),
        ],
        "content": """
<h2>20 Nichos Com Potencial em 2025</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Nicho</th><th>Margem estimada</th><th>Dificuldade de entrada</th></tr></thead>
<tbody>
<tr><td>Organizadores de home office</td><td>30-45%</td><td>Média</td></tr>
<tr><td>Acessórios para pets de raça</td><td>25-40%</td><td>Baixa</td></tr>
<tr><td>Produtos para jardim vertical</td><td>25-35%</td><td>Baixa</td></tr>
<tr><td>Kits de costura e bordado</td><td>35-50%</td><td>Baixa</td></tr>
<tr><td>Acessórios para ciclismo urbano</td><td>20-35%</td><td>Média</td></tr>
<tr><td>Papelaria funcional / planejadores</td><td>35-55%</td><td>Baixa</td></tr>
<tr><td>Produtos para fermentação caseira</td><td>30-45%</td><td>Baixa</td></tr>
<tr><td>Itens para acampamento leve</td><td>25-40%</td><td>Média</td></tr>
<tr><td>Acessórios para músicos amadores</td><td>25-40%</td><td>Baixa</td></tr>
<tr><td>Produtos de skincare coreano</td><td>30-50%</td><td>Média</td></tr>
</tbody>
</table>
</div>
<div class="callout">
<p><strong>Como usar essa lista:</strong> não compre estoque baseado nessa lista. Use como ponto de partida para pesquisa. Valide demanda real no ML antes de qualquer investimento.</p>
</div>
"""
    },
]

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
    .links-block ul { list-style: none; padding: 0; margin: 0; }
    .links-block li { margin-bottom: 6px; }
    .links-block a { color: var(--blue); text-decoration: none; font-size: .9rem; }
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
    .breadcrumb {{ max-width: 800px; margin: 0 auto; padding: 14px 24px 0; font-size: .78rem; color: var(--muted); display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }}
    .breadcrumb a {{ color: var(--blue); text-decoration: none; }}
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
    .footer-logo {{ color: #fff; font-weight: 700; font-size: .95rem; margin-bottom: 4px; }}
    .footer-logo em {{ color: var(--blue); font-style: normal; }}
    @media (max-width: 600px) {{ .page-wrapper {{ padding: 24px 16px 60px; }} .cta-box {{ padding: 28px 20px; }} }}
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
    <a href="{site}/">Inicio</a><span>&rsaquo;</span><span>{h1}</span>
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
    <article class="article-content">{content}</article>
    <div class="lead-section">
      <h3 class="lead-title">Receba Dicas Exclusivas Para Vendedores do ML</h3>
      <p class="lead-sub">Conteudo pratico sobre financas, impostos e precificacao. Sem spam.</p>
      <form class="lead-form" id="leadForm" onsubmit="submitLead(event)">
        <input type="email" id="leadEmail" placeholder="seu@email.com" required class="lead-input" />
        <button type="submit" class="lead-btn">Quero receber</button>
      </form>
      <p class="lead-ok" id="leadOk" style="display:none">Inscrito com sucesso!</p>
      <p class="lead-err" id="leadErr" style="display:none">Erro ao enviar. Tente novamente.</p>
    </div>
    <script>
    function submitLead(e) {{
      e.preventDefault();
      var email = document.getElementById('leadEmail').value;
      fetch('{supabase_url}', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{email: email, source: window.location.pathname}})
      }}).then(function(r) {{
        document.getElementById('leadForm').style.display = 'none';
        if (r.ok) {{ document.getElementById('leadOk').style.display = 'block'; }}
        else {{ document.getElementById('leadErr').style.display = 'block'; }}
      }}).catch(function() {{
        document.getElementById('leadForm').style.display = 'none';
        document.getElementById('leadErr').style.display = 'block';
      }});
    }}
    </script>
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
    <p><a href="{site}/">Home</a> &middot; <a href="{site}/politica.html">Politica de privacidade</a></p>
    <p>2026 Sobrou Quanto ML &middot; by ProspectIA &middot; Todos os direitos reservados.</p>
  </footer>
</body>
</html>
"""

def build_faq_html(faq_list):
    items = "".join(f'<div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)" aria-expanded="false">{q}</button><div class="faq-a" hidden><p>{a}</p></div></div>' for q,a in faq_list)
    return f'<div class="faq-block"><h2>Perguntas Frequentes</h2>{items}</div><script>function toggleFaq(b){{var d=b.nextElementSibling,o=b.getAttribute("aria-expanded")==="true";b.setAttribute("aria-expanded",String(!o));if(o){{d.setAttribute("hidden","")}}else{{d.removeAttribute("hidden")}}}}</script>'

def build_links_html(slugs):
    lis = "".join(f'<li><a href="/{s}/">{s.replace("-"," ").title()}</a></li>' for s in slugs[:5])
    return f'<div class="links-block"><h3>Leia Tambem</h3><ul>{lis}</ul></div>'

def build_schemas(p):
    art = json.dumps({"@context":"https://schema.org","@type":"Article","headline":p["h1"],"description":p["desc"],"url":f"{SITE}/{p['slug']}/","datePublished":DATE_ISO,"dateModified":DATE_ISO,"author":{"@type":"Organization","name":"Sobrou Quanto ML"},"publisher":{"@type":"Organization","name":"Sobrou Quanto ML","url":f"{SITE}/"}}, ensure_ascii=False)
    faq = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]}, ensure_ascii=False)
    bc  = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":p["h1"],"item":f"{SITE}/{p['slug']}/"}]}, ensure_ascii=False)
    return art, faq, bc

def generate_page(p):
    out_dir = os.path.join(BASE, p["slug"])
    os.makedirs(out_dir, exist_ok=True)
    art, faq_s, bc = build_schemas(p)
    rt = max(3, round(len(p["content"].split()) / 250))
    html = PAGE_TEMPLATE.format(
        site=SITE, slug=p["slug"], title=p["title"], h1=p["h1"],
        desc=p["desc"], tag=p["tag"], lead_text=p["lead"],
        date_br=DATE_BR, read_time=rt, content=p["content"],
        supabase_url=SUPABASE_URL,
        faq_html=build_faq_html(p["faq"]),
        links_html=build_links_html(p.get("links",[])),
        cta_title=p["cta_title"], cta_desc=p["cta_desc"],
        schema_article=art, schema_faq=faq_s, schema_breadcrumb=bc,
        lead_css=LEAD_CSS,
    )
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  [OK] /{p['slug']}/")

def update_sitemap(slugs):
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, encoding="utf-8") as f:
        content = f.read()
    added = 0
    for s in slugs:
        url = f"{SITE}/{s}/"
        if url not in content:
            entry = f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{DATE_ISO}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>"
            content = content.replace("</urlset>", entry + "\n</urlset>")
            added += 1
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] sitemap.xml (+{added} URLs)")

if __name__ == "__main__":
    print(f"\nGerando {len(PAGES)} paginas (Lote 5)...")
    for p in PAGES:
        generate_page(p)
    print("\nAtualizando sitemap...")
    update_sitemap([p["slug"] for p in PAGES])
    print(f"\nPronto! {len(PAGES)} paginas geradas.")
