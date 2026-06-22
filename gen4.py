"""gen4.py — Lote 4: 20 páginas SEO (vendas, taxas, frete, margem)"""
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
        "slug":  "como-vender-mais-mercado-livre",
        "title": "Como Vender Mais no Mercado Livre em 2025 | 10 Estratégias",
        "h1":    "Como Vender Mais no Mercado Livre: 10 Estratégias Que Funcionam",
        "tag":   "Estratégia",
        "desc":  "Aprenda 10 estratégias práticas para aumentar suas vendas no Mercado Livre sem reduzir preço. Otimize anúncios, melhore reputação e escale com margem.",
        "lead":  "Vender mais no Mercado Livre não significa necessariamente vender mais barato. As lojas que mais crescem combinam bom posicionamento, anúncio otimizado e gestão financeira sólida.",
        "cta_title": "Venda Mais Com Margem Controlada",
        "cta_desc":  "Sobrou Quanto ML mostra em tempo real quais produtos estão gerando lucro e quais estão puxando sua margem para baixo.",
        "links": ["escalar-vendas-mercado-livre","precificacao-mercado-livre","reputacao-mercado-livre","buy-box-mercado-livre"],
        "faq": [
            ("Como aumentar vendas sem baixar preço?", "Melhore fotos, título, descrição, reputação e tempo de envio. Esses fatores aumentam conversão sem mexer na margem."),
            ("Qual o melhor horário para anunciar no ML?", "Anúncios no ML são sempre visíveis. O que muda é o algoritmo — produtos com mais cliques e conversão sobem no ranking naturalmente."),
            ("Vale a pena usar Product Ads para vender mais?", "Sim, se a margem suportar o custo. Calcule o ROAS mínimo necessário antes de ativar. Nunca use Product Ads em produtos com margem abaixo de 15%."),
            ("Como o estoque afeta as vendas?", "Anúncios com estoque baixo (menos de 3 unidades) perdem posicionamento no ML. Mantenha estoque mínimo nos produtos de maior giro."),
            ("Reputação verde aumenta vendas?", "Sim, diretamente. Lojas com reputação verde têm vantagem no algoritmo de busca e maior taxa de conversão dos visitantes."),
        ],
        "content": """
<h2>Por Que Muitos Vendedores Não Conseguem Crescer</h2>
<p>O erro mais comum é focar apenas em preço. Reduzir preço aumenta volume, mas destrói margem — e uma loja sem margem não tem capital para crescer. As estratégias abaixo aumentam vendas preservando o resultado financeiro.</p>

<h3>As 10 Estratégias</h3>
<div class="table-wrapper">
<table>
<thead><tr><th>Estratégia</th><th>Impacto</th><th>Esforço</th></tr></thead>
<tbody>
<tr><td>Otimizar título com keyword principal</td><td>Alto</td><td>Baixo</td></tr>
<tr><td>Fotos profissionais (fundo branco + detalhes)</td><td>Alto</td><td>Médio</td></tr>
<tr><td>Responder perguntas em menos de 1h</td><td>Alto</td><td>Médio</td></tr>
<tr><td>Ativar Mercado Envios Full nos top SKUs</td><td>Alto</td><td>Alto</td></tr>
<tr><td>Manter reputação verde</td><td>Alto</td><td>Contínuo</td></tr>
<tr><td>Criar variações (kit, combo)</td><td>Médio</td><td>Baixo</td></tr>
<tr><td>Product Ads nos produtos com maior margem</td><td>Médio</td><td>Baixo</td></tr>
<tr><td>Precificar competitivo sem ser o menor</td><td>Médio</td><td>Baixo</td></tr>
<tr><td>Publicar novos anúncios regularmente</td><td>Médio</td><td>Médio</td></tr>
<tr><td>Analisar concorrentes semanalmente</td><td>Médio</td><td>Médio</td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p><strong>Regra de ouro:</strong> Antes de aplicar qualquer estratégia de crescimento, certifique-se de que sua margem atual é positiva. Crescer no prejuízo acelera a falência. Veja <a href="/como-calcular-lucro-mercado-livre/">Como Calcular Lucro no ML</a>.</p>
</div>

<h2>O Que o Algoritmo do ML Valoriza</h2>
<p>O Mercado Livre ordena os resultados por relevância e conversão. Produtos com mais cliques, menos devoluções, envio rápido e boa reputação do vendedor aparecem antes. Você não precisa ser o mais barato — precisa ser o mais confiável.</p>
"""
    },
    {
        "slug":  "como-abrir-loja-mercado-livre",
        "title": "Como Abrir Loja no Mercado Livre 2025 | Passo a Passo Completo",
        "h1":    "Como Abrir uma Loja no Mercado Livre: Guia Passo a Passo",
        "tag":   "Iniciante",
        "desc":  "Aprenda como abrir sua loja no Mercado Livre do zero. Cadastro, configuração, primeiros anúncios, taxas e como organizar as finanças desde o início.",
        "lead":  "Abrir uma loja no Mercado Livre é gratuito e rápido. A diferença entre quem cresce e quem desiste em 6 meses está na estrutura financeira montada desde o início.",
        "cta_title": "Comece Com as Finanças Organizadas",
        "cta_desc":  "Sobrou Quanto ML ajuda vendedores iniciantes a entender o lucro real de cada venda desde o primeiro pedido.",
        "links": ["guia-iniciante-mercado-livre","taxas-mercado-livre","precificacao-mercado-livre","separar-financas-pessoais-empresariais"],
        "faq": [
            ("Precisa pagar para abrir loja no ML?", "Não. O cadastro e a criação de anúncios são gratuitos. O ML cobra apenas comissão quando a venda acontece."),
            ("Pessoa física pode vender no ML?", "Sim, mas há limites de faturamento e a carga tributária pode ser maior. Recomenda-se abrir MEI para formalizar o negócio."),
            ("Qual o limite de anúncios gratuitos?", "No plano gratuito há limitações. Com o Mercado Livre Pago (assinatura) você tem mais benefícios de posicionamento."),
            ("Quanto tempo leva para a primeira venda?", "Depende da categoria e do preço. Com anúncio bem feito e preço competitivo, a primeira venda pode acontecer em dias."),
            ("Como receber o dinheiro das vendas?", "O ML repassa via Mercado Pago. Você pode transferir para conta bancária após o prazo de liberação (varia por reputação)."),
        ],
        "content": """
<h2>Passo a Passo Para Abrir Sua Loja</h2>
<ol>
<li><strong>Crie uma conta no ML</strong> — use e-mail de preferência vinculado ao CNPJ</li>
<li><strong>Configure sua conta como vendedor</strong> — preencha dados bancários e fiscais</li>
<li><strong>Abra MEI se ainda não tiver</strong> — portal.gov.br/registrobr, gratuito, 5 minutos</li>
<li><strong>Abra conta PJ separada</strong> — nunca misture com conta pessoal</li>
<li><strong>Calcule o custo total de cada produto</strong> — antes de criar o primeiro anúncio</li>
<li><strong>Crie os primeiros anúncios</strong> — fotos boas, título com keyword, descrição completa</li>
<li><strong>Configure endereço de origem</strong> — impacta o cálculo de frete</li>
</ol>

<div class="callout callout-warn">
<p><strong>Erro do iniciante:</strong> Criar anúncios sem calcular o preço mínimo lucrativo. Defina primeiro: CMV + comissão + frete + imposto + margem = preço de venda. Nunca ao contrário.</p>
</div>

<h2>Estrutura Financeira Mínima Para Começar</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">🏦</div><h4>Conta PJ</h4><p>Separada da pessoal — obrigatório para gestão saudável</p></div>
<div class="benefit-card"><div class="b-icon">📊</div><h4>Planilha básica</h4><p>Controle de CMV, vendas e despesas desde o primeiro mês</p></div>
<div class="benefit-card"><div class="b-icon">💰</div><h4>Capital de giro</h4><p>Tenha pelo menos 2x o custo do estoque inicial em reserva</p></div>
<div class="benefit-card"><div class="b-icon">📋</div><h4>MEI ativo</h4><p>DAS mensal em dia desde o primeiro faturamento</p></div>
</div>
"""
    },
    {
        "slug":  "como-calcular-lucro-mercado-livre",
        "title": "Como Calcular o Lucro no Mercado Livre 2025 | Fórmula Completa",
        "h1":    "Como Calcular o Lucro Real no Mercado Livre",
        "tag":   "Cálculo",
        "desc":  "Fórmula completa para calcular o lucro real de cada venda no Mercado Livre. Inclua todos os custos e descubra se sua loja está realmente no lucro.",
        "lead":  "Calcular o lucro no Mercado Livre vai muito além de subtrair o custo do produto do preço de venda. Comissão, frete, imposto e devoluções precisam entrar na conta.",
        "cta_title": "Veja Seu Lucro Calculado Automaticamente",
        "cta_desc":  "Sobrou Quanto ML conecta na sua conta ML e calcula o lucro real de cada pedido — sem planilha, sem estimativa.",
        "links": ["margem-de-lucro-mercado-livre","calculadora-margem-mercado-livre","como-saber-se-estou-lucrando-mercado-livre","produto-no-prejuizo-mercado-livre"],
        "faq": [
            ("Qual a fórmula do lucro no ML?", "Lucro = Preço de venda - CMV - comissão ML - frete - imposto - devolução estimada - despesas fixas proporcionais."),
            ("Como calcular o CMV corretamente?", "CMV = valor pago pelo produto + frete de compra + embalagem. Não use o preço de tabela, use o que você pagou de fato."),
            ("Devo incluir despesas fixas no lucro por produto?", "Sim. Divida suas despesas fixas mensais pelo número de pedidos para ter o custo fixo por pedido."),
            ("Como tratar devoluções no cálculo?", "Use sua taxa histórica de devolução (ex: 2%) como custo percentual em cada venda. Isso distribui o risco uniformemente."),
            ("Lucro bruto é o mesmo que lucro líquido?", "Não. Lucro bruto = receita - CMV. Lucro líquido = lucro bruto - todas as despesas operacionais."),
        ],
        "content": """
<h2>A Fórmula Completa</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Componente</th><th>Onde encontrar</th><th>Exemplo R$100</th></tr></thead>
<tbody>
<tr><td>Preço de venda</td><td>Anúncio</td><td>100,00</td></tr>
<tr><td>(-) CMV</td><td>Nota fiscal de compra</td><td>-40,00</td></tr>
<tr><td>(-) Comissão ML</td><td>Extrato financeiro ML</td><td>-16,00</td></tr>
<tr><td>(-) Frete</td><td>Extrato financeiro ML</td><td>-9,00</td></tr>
<tr><td>(-) Imposto</td><td>DAS / DARF</td><td>-6,00</td></tr>
<tr><td>(-) Devolução (2%)</td><td>Histórico de devoluções</td><td>-2,00</td></tr>
<tr><td>(-) Custo fixo/pedido</td><td>Despesas fixas ÷ pedidos</td><td>-5,00</td></tr>
<tr><td><strong>= Lucro Líquido</strong></td><td></td><td><strong>22,00 (22%)</strong></td></tr>
</tbody>
</table>
</div>

<div class="callout callout-green">
<p><strong>Margem saudável:</strong> acima de 15% de lucro líquido é considerado bom para marketplace. Abaixo de 8%, o risco de operar no prejuízo em meses com mais devoluções é alto.</p>
</div>

<h2>Lucro por Produto vs Lucro da Loja</h2>
<p>O lucro da loja é a soma dos lucros individuais menos os custos fixos totais. Um produto lucrativo pode estar sendo anulado por outro com margem negativa. Analise sempre produto a produto antes de olhar o total. Veja mais em <a href="/produto-no-prejuizo-mercado-livre/">Produto no Prejuízo no ML</a>.</p>
"""
    },
    {
        "slug":  "calculadora-taxas-mercado-livre",
        "title": "Calculadora de Taxas do Mercado Livre 2025 | Calcule Agora",
        "h1":    "Calculadora de Taxas do Mercado Livre: Quanto Você Realmente Paga",
        "tag":   "Calculadora",
        "desc":  "Use a calculadora de taxas do Mercado Livre para saber exatamente quanto paga em comissão, frete e impostos em cada venda.",
        "lead":  "Antes de precificar qualquer produto no Mercado Livre, é essencial saber exatamente quais taxas serão cobradas. A soma de comissão, frete e imposto pode representar 30% a 40% do preço de venda.",
        "cta_title": "Calcule Suas Taxas Automaticamente",
        "cta_desc":  "Sobrou Quanto ML integra com sua conta ML e mostra todas as taxas cobradas em cada venda, por produto e por período.",
        "links": ["taxas-mercado-livre","comissao-mercado-livre","quanto-mercado-livre-cobra","como-calcular-comissao-mercado-livre"],
        "faq": [
            ("Quais taxas o ML cobra?", "Comissão por categoria (8-18%), frete subsidiado (variável), taxa de parcelamento (Mercado Pago) e, se usar Full, taxa de fulfillment."),
            ("O ML cobra taxa sobre o frete pago pelo comprador?", "Não. A comissão incide sobre o preço do produto, não sobre o frete."),
            ("Como saber a taxa exata da minha categoria?", "Acesse sua conta ML > Central de Ajuda > Taxas e comissões, ou analise o extrato financeiro de vendas anteriores."),
            ("A taxa muda com o volume de vendas?", "Não automaticamente. O ML não reduz comissões por volume como outras plataformas. O desconto é via programas especiais para grandes contas."),
            ("Full tem taxa adicional?", "Sim. Além da comissão Premium obrigatória, há custo de armazenagem e picking por unidade, variando por tamanho e peso."),
        ],
        "content": """
<h2>Resumo de Todas as Taxas do ML</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Taxa</th><th>Quem paga</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Comissão Clássico</td><td>Vendedor</td><td>8% a 12%</td></tr>
<tr><td>Comissão Premium</td><td>Vendedor</td><td>14% a 18%</td></tr>
<tr><td>Frete Mercado Envios</td><td>Vendedor (parcial)</td><td>Variável por peso/região</td></tr>
<tr><td>Fulfillment Full</td><td>Vendedor</td><td>R$5 a R$25 por unidade</td></tr>
<tr><td>Parcelamento Mercado Pago</td><td>Vendedor</td><td>Varia por parcelas</td></tr>
<tr><td>Anúncios patrocinados</td><td>Vendedor (opcional)</td><td>CPC variável</td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p><strong>Como calcular o total:</strong> Some comissão + frete estimado + taxa de parcelamento média. Para um produto de R$100 no Premium, espere pagar entre R$24 e R$32 só em taxas — antes de descontar CMV e imposto.</p>
</div>

<h2>Como Reduzir o Impacto das Taxas</h2>
<p>Não é possível negociar taxas diretamente com o ML, mas você pode escolher o tipo de anúncio por produto, aumentar o ticket médio para diluir o custo fixo de frete e focar em categorias com menor comissão. Veja detalhes em <a href="/como-reduzir-taxas-mercado-livre/">Como Reduzir Taxas no ML</a>.</p>
"""
    },
    {
        "slug":  "tabela-taxas-mercado-livre",
        "title": "Tabela de Taxas do Mercado Livre 2025 | Atualizada Por Categoria",
        "h1":    "Tabela Completa de Taxas do Mercado Livre 2025",
        "tag":   "Taxas",
        "desc":  "Tabela atualizada com todas as taxas e comissões do Mercado Livre por categoria. Clássico, Premium, Full e Mercado Pago em uma visão completa.",
        "lead":  "As taxas do Mercado Livre variam por categoria, tipo de anúncio e modalidade de envio. Esta tabela consolida as principais informações para você calcular antes de precificar.",
        "cta_title": "Monitore Suas Taxas Reais Automaticamente",
        "cta_desc":  "Sobrou Quanto ML cruza os dados do seu extrato ML e mostra as taxas reais pagas por produto e categoria.",
        "links": ["taxas-mercado-livre","calculadora-taxas-mercado-livre","comissao-mercado-livre","quanto-mercado-livre-cobra"],
        "faq": [
            ("As taxas do ML mudam com frequência?", "Sim, o ML pode alterar as tabelas. Sempre consulte a tabela oficial antes de precificar novos produtos."),
            ("Qual categoria tem menor taxa?", "Livros e materiais educativos (8%). Suplementos e alimentos também costumam ter taxas menores."),
            ("Qual categoria tem maior taxa?", "Eletrodomésticos e eletrônicos no Premium chegam a 18%."),
            ("A taxa do Full inclui a comissão?", "Não. Full cobra a taxa de fulfillment separada da comissão do anúncio Premium (obrigatório no Full)."),
            ("Existe taxa de cancelamento?", "Se o vendedor cancela a venda, pode haver penalidade na reputação. Não há taxa financeira específica para cancelamento."),
        ],
        "content": """
<h2>Taxas por Categoria — Anúncio Clássico vs Premium</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Categoria</th><th>Clássico</th><th>Premium</th></tr></thead>
<tbody>
<tr><td>Livros e Educação</td><td>8%</td><td>8%</td></tr>
<tr><td>Suplementos e Saúde</td><td>10%</td><td>14%</td></tr>
<tr><td>Informática</td><td>10%</td><td>16%</td></tr>
<tr><td>Eletrônicos</td><td>10%</td><td>16%</td></tr>
<tr><td>Celulares</td><td>10%</td><td>16%</td></tr>
<tr><td>Moda e Acessórios</td><td>10%</td><td>16%</td></tr>
<tr><td>Casa e Jardim</td><td>10%</td><td>16%</td></tr>
<tr><td>Brinquedos</td><td>10%</td><td>16%</td></tr>
<tr><td>Eletrodomésticos</td><td>10%</td><td>18%</td></tr>
<tr><td>Peças automotivas</td><td>10%</td><td>14%</td></tr>
</tbody>
</table>
</div>

<div class="callout callout-warn">
<p><strong>Atenção:</strong> Esta tabela é uma referência geral. As taxas exatas dependem da subcategoria específica do produto. Sempre confirme no painel do vendedor antes de precificar.</p>
</div>

<h2>Taxas do Mercado Pago (Parcelamento)</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Parcelas</th><th>Taxa estimada</th></tr></thead>
<tbody>
<tr><td>À vista</td><td>~2,5% a 3,5%</td></tr>
<tr><td>2x a 6x</td><td>~5% a 10%</td></tr>
<tr><td>7x a 12x</td><td>~11% a 18%</td></tr>
</tbody>
</table>
</div>
<p>O vendedor absorve a taxa de parcelamento ou repassa no preço. Para produtos com ticket alto onde o parcelamento é comum, inclua essa taxa na precificação.</p>
"""
    },
    {
        "slug":  "diferenca-mercado-envios-e-fulfillment",
        "title": "Mercado Envios vs Fulfillment Full: Qual a Diferença? | 2025",
        "h1":    "Mercado Envios vs Full: Diferenças, Custos e Quando Usar Cada Um",
        "tag":   "Logística",
        "desc":  "Entenda a diferença entre Mercado Envios e Mercado Envios Full. Custos, vantagens, desvantagens e quando migrar para Full.",
        "lead":  "Mercado Envios e Full são dois modelos de logística do ML — mas têm custos, operação e impacto na margem completamente diferentes. Escolher errado pode destruir sua lucratividade.",
        "cta_title": "Calcule Se o Full Compensa Para Você",
        "cta_desc":  "Sobrou Quanto ML simula o impacto do Full na sua margem com base no histórico real de vendas.",
        "links": ["anuncio-full-mercado-livre","frete-gratis-mercado-livre","custo-envio-mercado-livre","taxas-mercado-livre"],
        "faq": [
            ("Qual a principal diferença entre Envios e Full?", "No Envios normal você envia os pedidos da sua casa/estoque. No Full você estoca no armazém do ML e eles fazem o envio."),
            ("Full é obrigatoriamente Premium?", "Sim. Produtos no Full só podem ter anúncio Premium, com comissão mais alta."),
            ("Full é mais caro ou mais barato?", "Depende do volume. Para produtos de alto giro, o Full pode ser mais barato que enviar individualmente. Para baixo giro, é mais caro."),
            ("O Full melhora o posicionamento no ML?", "Sim. Produtos Full têm tag de entrega rápida e tendem a ter melhor posicionamento no algoritmo."),
            ("Como calcular se o Full compensa?", "Compare: (custo envio atual × volume) vs (taxa Full × volume + custo de armazenagem). Se a conversão aumentar, some o ganho em receita."),
        ],
        "content": """
<h2>Comparativo: Envios Normal vs Full</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Característica</th><th>Mercado Envios</th><th>Full (Fulfillment)</th></tr></thead>
<tbody>
<tr><td>Quem embala e envia</td><td>Vendedor</td><td>ML</td></tr>
<tr><td>Onde fica o estoque</td><td>Com o vendedor</td><td>Centro de distribuição ML</td></tr>
<tr><td>Tipo de anúncio</td><td>Clássico ou Premium</td><td>Somente Premium</td></tr>
<tr><td>Prazo de entrega</td><td>2 a 5 dias úteis</td><td>No mesmo dia ou 1 dia</td></tr>
<tr><td>Custo extra</td><td>Apenas frete</td><td>Frete + armazenagem + picking</td></tr>
<tr><td>Controle do estoque</td><td>Total</td><td>Parcial (via painel)</td></tr>
<tr><td>Risco de avaria</td><td>Vendedor</td><td>ML assume</td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p><strong>Regra prática:</strong> Use Full para produtos com mais de 30 vendas/mês, margem acima de 20% e que se beneficiam da tag de entrega rápida (eletrônicos, moda, acessórios). Para produtos pesados ou de baixo giro, Envios normal costuma ser mais econômico.</p>
</div>

<h2>Impacto do Full na Margem</h2>
<p>O Full pode aumentar a conversão em 20% a 40% — mas adiciona custo de fulfillment de R$5 a R$25 por unidade dependendo do tamanho. Faça a conta: se um produto de R$80 tem margem de R$16 e o Full custa R$10 por unidade, a margem cai para R$6 (7,5%). Só vale se o volume aumentar proporcionalmente.</p>
"""
    },
    {
        "slug":  "como-funciona-mercado-envios",
        "title": "Como Funciona o Mercado Envios 2025 | Guia Completo",
        "h1":    "Como Funciona o Mercado Envios: Tudo Que o Vendedor Precisa Saber",
        "tag":   "Logística",
        "desc":  "Entenda como funciona o Mercado Envios, como o frete é calculado, quem paga e como isso impacta sua margem de lucro.",
        "lead":  "O Mercado Envios é o sistema de logística integrado do ML. Entender como ele funciona evita surpresas com custos de frete que corroem sua margem.",
        "cta_title": "Veja o Impacto do Frete na Sua Margem",
        "cta_desc":  "Sobrou Quanto ML calcula automaticamente quanto você pagou de frete em cada venda e como isso afeta seu resultado.",
        "links": ["diferenca-mercado-envios-e-fulfillment","como-calcular-frete-mercado-livre","custo-envio-mercado-livre","frete-gratis-mercado-livre"],
        "faq": [
            ("O que é Mercado Envios?", "É o sistema logístico do ML que gera etiquetas de envio, rastreia pedidos e calcula automaticamente o frete para o comprador."),
            ("Quem paga o frete no Mercado Envios?", "Depende do anúncio. No Premium, parte do frete é subsidiada pelo ML e parte pode ser absorvida pelo vendedor via desconto na comissão."),
            ("O vendedor escolhe a transportadora?", "Não. O ML seleciona automaticamente. Correios, Loggi, Total Express e outras são usadas conforme região e tamanho do produto."),
            ("Como o ML calcula o frete?", "Com base no CEP de origem (seu endereço), CEP de destino do comprador, peso e dimensões do produto."),
            ("Posso usar minha própria transportadora?", "Sim, existe a opção de envio próprio, mas você perde a integração automática de rastreamento e a proteção do ML."),
        ],
        "content": """
<h2>Como o Mercado Envios Funciona na Prática</h2>
<ol>
<li>Venda realizada → ML gera etiqueta de envio automaticamente</li>
<li>Vendedor imprime a etiqueta e embala o produto</li>
<li>Leva ao ponto de coleta ou aguarda coleta (depende da transportadora)</li>
<li>ML rastreia o envio e atualiza o comprador</li>
<li>Entrega confirmada → ML libera o repasse financeiro</li>
</ol>

<h2>Como o Custo de Frete Impacta a Margem</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Produto</th><th>Preço</th><th>Frete médio</th><th>% do preço</th></tr></thead>
<tbody>
<tr><td>Produto leve &lt;500g</td><td>R$50</td><td>R$8</td><td>16%</td></tr>
<tr><td>Produto médio 1-2kg</td><td>R$120</td><td>R$18</td><td>15%</td></tr>
<tr><td>Produto pesado &gt;5kg</td><td>R$300</td><td>R$45</td><td>15%</td></tr>
</tbody>
</table>
</div>

<div class="callout callout-warn">
<p><strong>Atenção:</strong> O frete estimado no momento da criação do anúncio pode ser diferente do cobrado na venda real — especialmente para destinos distantes. Sempre use uma média baseada no histórico real.</p>
</div>
"""
    },
    {
        "slug":  "como-calcular-frete-mercado-livre",
        "title": "Como Calcular o Frete no Mercado Livre 2025 | Fórmula e Dicas",
        "h1":    "Como Calcular o Frete no Mercado Livre Antes de Precificar",
        "tag":   "Frete",
        "desc":  "Aprenda a calcular o custo real de frete no Mercado Livre para incluir na precificação. Evite surpresas que destroem sua margem.",
        "lead":  "O frete é uma das maiores surpresas negativas para vendedores iniciantes. Calcular o custo médio de envio por produto antes de precificar é essencial para não vender no prejuízo.",
        "cta_title": "Veja o Custo Real de Frete Por Produto",
        "cta_desc":  "Sobrou Quanto ML analisa seu histórico e mostra o custo médio de frete por produto — para você precificar com dados reais.",
        "links": ["como-funciona-mercado-envios","custo-envio-mercado-livre","precificacao-mercado-livre","simulador-frete-mercado-livre"],
        "faq": [
            ("Como calcular o frete antes de anunciar?", "Use o simulador de frete do ML com o peso e dimensões do produto + seu CEP de origem. Simule para 3 CEPs destino diferentes e use a média."),
            ("O frete grátis é realmente grátis para o vendedor?", "Não. No anúncio Premium com frete grátis, o ML desconta parte do custo da sua comissão, mas o restante é absorvido pelo vendedor."),
            ("Como o peso afeta o custo de frete?", "Peso e dimensões definem o 'peso cubado'. Um produto volumoso mas leve pode ser mais caro de enviar que um produto denso."),
            ("Frete para Norte e Nordeste é mais caro?", "Sim. Envios para regiões distantes custam significativamente mais. Use a média ponderada pelo volume de vendas por região."),
            ("Como incluir o frete na precificação?", "Calcule o frete médio histórico (ou estimado para regiões principais) e inclua como custo fixo por produto na fórmula de precificação."),
        ],
        "content": """
<h2>Calculando o Frete Médio Por Produto</h2>
<p>O frete varia por destino. A melhor abordagem é calcular uma média ponderada considerando as regiões onde você mais vende:</p>
<div class="table-wrapper">
<table>
<thead><tr><th>Região</th><th>% vendas típico</th><th>Frete estimado 1kg</th></tr></thead>
<tbody>
<tr><td>Sudeste</td><td>50%</td><td>R$8 a R$15</td></tr>
<tr><td>Sul</td><td>20%</td><td>R$10 a R$18</td></tr>
<tr><td>Centro-Oeste</td><td>15%</td><td>R$12 a R$20</td></tr>
<tr><td>Nordeste</td><td>10%</td><td>R$15 a R$28</td></tr>
<tr><td>Norte</td><td>5%</td><td>R$20 a R$40</td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p><strong>Dica prática:</strong> Após 30 vendas, extraia do extrato do ML o custo total de frete e divida pelo número de pedidos. Esse é seu custo médio real — muito mais preciso que qualquer estimativa.</p>
</div>

<h2>Peso Cubado: O Que É e Por Que Importa</h2>
<p>Transportadoras cobram pelo maior valor entre peso real e peso cubado (C × L × A ÷ 6.000). Um produto de 200g em uma caixa de 30×20×20cm tem peso cubado de 2kg — e você paga pelo cubado. Embalagens menores reduzem custos de frete diretamente.</p>
"""
    },
    {
        "slug":  "como-funciona-mercado-envios-full",
        "title": "Como Funciona o Mercado Envios Full 2025 | Guia Completo",
        "h1":    "Como Funciona o Mercado Envios Full: Guia Para Vendedores",
        "tag":   "Full",
        "desc":  "Entenda como funciona o Mercado Envios Full, quais são os custos, como enviar estoque e quando vale a pena ativar para seus produtos.",
        "lead":  "O Mercado Envios Full é o serviço de fulfillment do ML — você envia o estoque para o armazém deles e o ML faz todo o processo de separação e entrega. Mas tem custos específicos que precisam ser calculados.",
        "cta_title": "Calcule Se o Full Vale Para Seus Produtos",
        "cta_desc":  "Sobrou Quanto ML simula a margem com e sem Full usando seu histórico real de vendas.",
        "links": ["diferenca-mercado-envios-e-fulfillment","anuncio-full-mercado-livre","taxas-mercado-livre","calculadora-taxas-mercado-livre"],
        "faq": [
            ("Como enviar produtos para o Full?", "Você cria um plano de envio no painel do ML, imprime etiquetas e envia para o centro de distribuição. O ML organiza o estoque ao receber."),
            ("Qual o custo de armazenagem no Full?", "Há uma taxa diária por unidade armazenada que varia por tamanho. Produtos parados por mais de 60 dias têm taxa adicional."),
            ("Posso misturar Full e Envios Normal?", "Sim. Você pode ter parte do catálogo no Full e parte em Envios Normal. Cada anúncio tem sua configuração independente."),
            ("O Full garante entrega no mesmo dia?", "Em grandes capitais, sim para pedidos feitos até certo horário. Em regiões menores, a entrega costuma ser no dia seguinte."),
            ("O que acontece se o ML estragar meu produto?", "O ML tem política de ressarcimento para avarias ocorridas no armazém ou durante o envio Full."),
        ],
        "content": """
<h2>O Fluxo do Full Para o Vendedor</h2>
<ol>
<li><strong>Cadastre o produto no Full</strong> — dimensões e peso precisos são obrigatórios</li>
<li><strong>Crie um plano de envio</strong> — informe a quantidade a enviar</li>
<li><strong>Embale por SKU</strong> — cada unidade com etiqueta do ML</li>
<li><strong>Envie para o CD</strong> — ML fornece etiqueta de transporte</li>
<li><strong>Aguarde confirmação</strong> — ML confere e disponibiliza o estoque</li>
<li><strong>Vendas automáticas</strong> — ML separa, embala e envia cada pedido</li>
</ol>

<h2>Custos Detalhados do Full</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Custo</th><th>Descrição</th></tr></thead>
<tbody>
<tr><td>Comissão Premium</td><td>Obrigatório (14% a 18% por categoria)</td></tr>
<tr><td>Taxa de fulfillment</td><td>R$5 a R$25 por unidade (peso e tamanho)</td></tr>
<tr><td>Armazenagem</td><td>Taxa diária por unidade após 30 dias</td></tr>
<tr><td>Envio para o CD</td><td>Por conta do vendedor</td></tr>
</tbody>
</table>
</div>

<div class="callout callout-warn">
<p><strong>Cuidado com estoque parado:</strong> Produtos no Full que não vendem geram custo de armazenagem crescente. Migre para Full apenas produtos com giro comprovado.</p>
</div>
"""
    },
    {
        "slug":  "custo-envio-mercado-livre",
        "title": "Custo de Envio no Mercado Livre 2025 | Quanto Você Paga de Frete",
        "h1":    "Custo de Envio no Mercado Livre: O Que Você Paga de Frete em Cada Venda",
        "tag":   "Frete",
        "desc":  "Descubra quanto você paga de frete em cada venda no Mercado Livre. Como o custo de envio é calculado e como incluí-lo corretamente na precificação.",
        "lead":  "O custo de envio é frequentemente subestimado por vendedores do ML. Em produtos de baixo valor, o frete pode representar 15% a 25% do preço — tornando a venda inviável se não for considerado na precificação.",
        "cta_title": "Veja Quanto Pagou de Frete No Último Mês",
        "cta_desc":  "Sobrou Quanto ML extrai do seu extrato ML o custo total de frete por produto e período — em segundos.",
        "links": ["como-calcular-frete-mercado-livre","simulador-frete-mercado-livre","frete-gratis-mercado-livre","diferenca-mercado-envios-e-fulfillment"],
        "faq": [
            ("Quem paga o frete no ML?", "Depende do tipo de anúncio. No Premium com frete grátis, o ML subsidia parte e o vendedor absorve o restante via desconto na comissão."),
            ("Como ver quanto paguei de frete?", "No extrato financeiro do ML, cada venda mostra o valor de frete cobrado separadamente da comissão."),
            ("Frete grátis aumenta conversão?", "Sim, significativamente. Mas só ative se o preço de venda já incluir o custo do frete na margem."),
            ("Produto pesado compensa vender no ML?", "Com margem adequada, sim. Mas produtos acima de 10kg têm frete muito alto que pode inviabilizar a venda. Calcule antes."),
            ("Como reduzir custo de envio?", "Use embalagens menores (reduz peso cubado), consolide envios quando possível e compare tipos de anúncio para o mesmo produto."),
        ],
        "content": """
<h2>Quanto Custa o Frete Por Tipo de Produto</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Tipo de produto</th><th>Peso médio</th><th>Frete médio SP→SP</th><th>Frete médio SP→PA</th></tr></thead>
<tbody>
<tr><td>Acessório pequeno</td><td>&lt;200g</td><td>R$6 a R$10</td><td>R$15 a R$25</td></tr>
<tr><td>Produto médio</td><td>500g a 1kg</td><td>R$10 a R$18</td><td>R$22 a R$35</td></tr>
<tr><td>Produto grande</td><td>2 a 5kg</td><td>R$20 a R$40</td><td>R$45 a R$80</td></tr>
<tr><td>Produto pesado</td><td>&gt;10kg</td><td>R$60 a R$150</td><td>R$120 a R$250</td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p><strong>Regra prática:</strong> O custo de frete deve representar no máximo 10% do preço de venda para que a margem se mantenha saudável. Se o frete for maior que isso, revise o preço ou a embalagem.</p>
</div>

<h2>Estratégia de Preço Mínimo Considerando Frete</h2>
<p>Preço mínimo viável = CMV ÷ (1 - comissão% - frete% - imposto% - margem mínima%). O frete percentual é calculado dividindo o custo médio de frete pelo preço de venda. Para um produto com frete de R$12 vendido a R$80: 12÷80 = 15% de custo de frete.</p>
"""
    },
    {
        "slug":  "simulador-frete-mercado-livre",
        "title": "Simulador de Frete Mercado Livre 2025 | Como Calcular Antes de Vender",
        "h1":    "Simulador de Frete no Mercado Livre: Como Usar e Interpretar",
        "tag":   "Simulador",
        "desc":  "Aprenda a usar o simulador de frete do Mercado Livre para calcular o custo de envio antes de precificar seus produtos.",
        "lead":  "Simular o frete antes de criar o anúncio é um passo que muitos vendedores pulam — e depois se surpreendem com custos de envio que destroem a margem.",
        "cta_title": "Use Dados Reais de Frete Na Precificação",
        "cta_desc":  "Sobrou Quanto ML usa o histórico real de fretes da sua loja para calcular o custo médio por produto com precisão.",
        "links": ["como-calcular-frete-mercado-livre","custo-envio-mercado-livre","precificacao-mercado-livre","calculadora-taxas-mercado-livre"],
        "faq": [
            ("Onde fica o simulador de frete do ML?", "No painel do vendedor, ao criar ou editar um anúncio, há uma calculadora de frete que estima o custo para diferentes CEPs."),
            ("O simulador é preciso?", "É uma estimativa. O frete real pode variar por promoções do ML ou mudanças de tabela. Use como referência, não como valor exato."),
            ("Como simular para regiões distantes?", "Use CEPs de Manaus (69000-000), Belém (66000-000) e Fortaleza (60000-000) para estimar o pior cenário de frete."),
            ("Devo simular com peso real ou cubado?", "Use sempre o peso cubado se ele for maior. Calcule: C×L×A÷6000 e compare com o peso real."),
            ("Simulador de frete substitui o cálculo real?", "Não. Após 30 vendas, use o extrato real do ML para calcular o frete médio. É muito mais preciso que qualquer simulação."),
        ],
        "content": """
<h2>Como Usar o Simulador de Frete do ML</h2>
<ol>
<li>Acesse Minha Conta > Vendas > Criar anúncio</li>
<li>Preencha as dimensões e peso do produto</li>
<li>Na seção de envio, clique em "Ver custos de frete"</li>
<li>Insira CEPs de destino de referência</li>
<li>Compare os custos por transportadora</li>
</ol>

<div class="callout">
<p><strong>Simule pelo menos 3 CEPs:</strong> um na sua região, um no Sudeste e um no Nordeste. Calcule a média ponderada pelo percentual de vendas de cada região.</p>
</div>

<h2>Interpretando os Resultados</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Resultado</th><th>O que significa</th><th>Ação</th></tr></thead>
<tbody>
<tr><td>Frete &lt; 8% do preço</td><td>Saudável</td><td>Prosseguir</td></tr>
<tr><td>Frete 8-15% do preço</td><td>Aceitável</td><td>Incluir na precificação</td></tr>
<tr><td>Frete &gt; 15% do preço</td><td>Risco alto</td><td>Revisar preço ou embalagem</td></tr>
<tr><td>Frete &gt; 25% do preço</td><td>Inviável</td><td>Não anunciar nesse preço</td></tr>
</tbody>
</table>
</div>
"""
    },
    {
        "slug":  "como-ter-margem-mercado-livre",
        "title": "Como Ter Margem de Lucro no Mercado Livre 2025 | Guia Prático",
        "h1":    "Como Ter Margem de Lucro Real no Mercado Livre",
        "tag":   "Margem",
        "desc":  "Aprenda como garantir margem de lucro positiva nas suas vendas do Mercado Livre. Estratégias práticas de precificação, controle de custos e análise por produto.",
        "lead":  "Ter margem no Mercado Livre não é sorte — é resultado de precificação correta, controle de custos e análise contínua. Veja como estruturar isso.",
        "cta_title": "Monitore Sua Margem em Tempo Real",
        "cta_desc":  "Sobrou Quanto ML calcula a margem real de cada produto automaticamente, integrado com sua conta ML.",
        "links": ["margem-de-lucro-mercado-livre","calculadora-margem-mercado-livre","como-calcular-margem-mercado-livre","margem-ideal-mercado-livre"],
        "faq": [
            ("O que é margem de lucro no ML?", "É o percentual do preço de venda que sobra após pagar todos os custos: produto, comissão, frete, imposto e despesas operacionais."),
            ("Qual margem mínima aceitar no ML?", "Abaixo de 8% de margem líquida o risco é alto. Entre 10% e 20% é saudável. Acima de 25% é ótimo para marketplace."),
            ("Como aumentar minha margem sem aumentar preço?", "Reduza CMV negociando com fornecedor, diminua devolução com melhor descrição, e use embalagens menores para reduzir frete."),
            ("Por que minha margem muda mês a mês?", "Frete varia por região de destino, devoluções são imprevisíveis e promoções do ML podem alterar taxas temporariamente."),
            ("Como calcular margem mínima por produto?", "Margem mínima = (todas as deduções) ÷ preço de venda × 100. Qualquer margem abaixo desse ponto é prejuízo."),
        ],
        "content": """
<h2>Os 3 Pilares da Margem Saudável</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">💰</div><h4>CMV baixo</h4><p>Negociar bem com fornecedor é a alavanca mais poderosa de margem</p></div>
<div class="benefit-card"><div class="b-icon">📦</div><h4>Frete otimizado</h4><p>Embalagens menores e produtos de maior valor diluem o custo de envio</p></div>
<div class="benefit-card"><div class="b-icon">📉</div><h4>Devolução baixa</h4><p>Cada 1% a menos de devolução representa 1%+ de margem recuperada</p></div>
</div>

<h2>Precificar Para Garantir Margem</h2>
<p>A única forma de garantir margem é precificar com ela embutida — não esperar sobrar. Use a fórmula reversa:</p>

<div class="callout callout-green">
<p><strong>Preço mínimo = CMV ÷ (1 - comissão% - frete% - imposto% - margem desejada%)</strong><br>
Exemplo: CMV R$40, custos totais 45%, margem desejada 20%<br>
Preço = 40 ÷ (1 - 0,45 - 0,20) = 40 ÷ 0,35 = <strong>R$ 114,28</strong></p>
</div>

<h2>Monitoramento Contínuo</h2>
<p>A margem muda. Frete de fornecedor aumenta, taxas do ML são revisadas, devoluções oscilam. Revise a margem de cada produto mensalmente e ajuste o preço quando necessário. Veja a margem ideal para ML em <a href="/margem-ideal-mercado-livre/">Margem Ideal no Mercado Livre</a>.</p>
"""
    },
    {
        "slug":  "como-calcular-margem-mercado-livre",
        "title": "Como Calcular a Margem no Mercado Livre 2025 | Passo a Passo",
        "h1":    "Como Calcular a Margem de Lucro no Mercado Livre: Passo a Passo",
        "tag":   "Cálculo",
        "desc":  "Guia passo a passo para calcular a margem de lucro real no Mercado Livre. Fórmulas, exemplos práticos e como automatizar o cálculo.",
        "lead":  "Calcular a margem no Mercado Livre exige incluir todos os custos — não apenas o produto. Veja o passo a passo completo com fórmulas e exemplos reais.",
        "cta_title": "Calcule Sua Margem Automaticamente",
        "cta_desc":  "Sobrou Quanto ML faz esse cálculo por você — integrado com sua conta ML, sem planilha.",
        "links": ["calculadora-margem-mercado-livre","margem-de-lucro-mercado-livre","como-ter-margem-mercado-livre","margem-ideal-mercado-livre"],
        "faq": [
            ("Qual a fórmula da margem bruta?", "Margem bruta = (Preço de venda - CMV) ÷ Preço de venda × 100. Não inclui taxas do ML."),
            ("Qual a fórmula da margem líquida?", "Margem líquida = (Preço - CMV - comissão - frete - imposto - despesas) ÷ Preço × 100."),
            ("Margem bruta de 50% é boa no ML?", "Depende. Com comissão de 16% + frete 10% + imposto 6%, você parte de 50% de margem bruta e chega a ~18% de margem líquida."),
            ("Como calcular margem no Excel?", "=(preço-CMV-comissão-frete-imposto-despesas)/preço. Multiplique por 100 para obter o percentual."),
            ("Qual a diferença entre markup e margem?", "Markup é aplicado sobre o custo: preço = CMV × (1 + markup%). Margem é calculada sobre o preço de venda. São cálculos inversos e não equivalentes."),
        ],
        "content": """
<h2>Passo 1: Levante Todos os Custos</h2>
<ul>
<li><strong>CMV:</strong> custo da mercadoria (nota fiscal + frete de compra)</li>
<li><strong>Comissão ML:</strong> percentual da categoria × preço de venda</li>
<li><strong>Frete:</strong> custo médio real por pedido (extrair do extrato ML)</li>
<li><strong>Imposto:</strong> DAS/mês ÷ número de pedidos, ou alíquota × faturamento</li>
<li><strong>Devolução:</strong> taxa histórica × preço (ex: 2% × R$100 = R$2)</li>
<li><strong>Custo fixo/pedido:</strong> despesas fixas mensais ÷ número de pedidos</li>
</ul>

<h2>Passo 2: Aplique a Fórmula</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Margem</th><th>Fórmula</th></tr></thead>
<tbody>
<tr><td>Margem Bruta</td><td>(Preço - CMV) ÷ Preço × 100</td></tr>
<tr><td>Margem Operacional</td><td>(Preço - CMV - comissão - frete) ÷ Preço × 100</td></tr>
<tr><td>Margem Líquida</td><td>(Preço - todos os custos) ÷ Preço × 100</td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p><strong>Use sempre a margem líquida</strong> para decisões de negócio. A margem bruta ilude — parece boa mas esconde custos que comem o resultado.</p>
</div>
"""
    },
    {
        "slug":  "margem-ideal-mercado-livre",
        "title": "Margem Ideal no Mercado Livre 2025 | Quanto Você Deve Lucrar",
        "h1":    "Qual é a Margem de Lucro Ideal Para Vender no Mercado Livre",
        "tag":   "Margem",
        "desc":  "Descubra qual é a margem de lucro ideal para vendedores do Mercado Livre. Referências por categoria e como saber se sua loja está saudável.",
        "lead":  "Não existe uma margem única ideal para todos os vendedores do ML — mas existem referências por categoria e modelo de negócio que ajudam a avaliar se você está bem posicionado.",
        "cta_title": "Compare Sua Margem Com a Referência do Setor",
        "cta_desc":  "Sobrou Quanto ML calcula sua margem real por categoria e produto para você comparar com os benchmarks do mercado.",
        "links": ["margem-de-lucro-mercado-livre","como-calcular-margem-mercado-livre","como-ter-margem-mercado-livre","como-aumentar-lucro-mercado-livre"],
        "faq": [
            ("Qual a margem mínima para ser saudável no ML?", "10% de margem líquida é o mínimo recomendado. Abaixo disso, qualquer variação (devolução, promoção) pode gerar prejuízo."),
            ("Qual categoria tem maior margem no ML?", "Produtos de nicho, acessórios, cosméticos artesanais e infoprodutos físicos costumam ter margens acima de 30%."),
            ("Qual categoria tem menor margem?", "Eletrônicos e eletrodomésticos têm as menores margens no ML — geralmente entre 5% e 12% de líquida."),
            ("Minha margem de 8% é boa?", "Depende da categoria. Para eletrônicos pode ser razoável. Para moda ou acessórios é muito baixo."),
            ("Como saber se minha margem está dentro do esperado?", "Compare com o benchmark da sua categoria específica. Em geral: &lt;8% baixo, 8-15% aceitável, 15-25% bom, &gt;25% excelente."),
        ],
        "content": """
<h2>Benchmark de Margem Por Categoria</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Categoria</th><th>Margem Líquida Típica</th><th>Considerado Bom</th></tr></thead>
<tbody>
<tr><td>Eletrônicos e Informática</td><td>5% a 12%</td><td>&gt;10%</td></tr>
<tr><td>Eletrodomésticos</td><td>4% a 10%</td><td>&gt;8%</td></tr>
<tr><td>Moda e Acessórios</td><td>20% a 40%</td><td>&gt;25%</td></tr>
<tr><td>Casa e Jardim</td><td>12% a 25%</td><td>&gt;18%</td></tr>
<tr><td>Saúde e Beleza</td><td>20% a 35%</td><td>&gt;22%</td></tr>
<tr><td>Livros</td><td>15% a 30%</td><td>&gt;20%</td></tr>
<tr><td>Peças automotivas</td><td>15% a 30%</td><td>&gt;20%</td></tr>
</tbody>
</table>
</div>

<div class="callout callout-warn">
<p><strong>Atenção:</strong> Esses percentuais são médias do setor. Sua margem real depende do seu CMV, do seu regime tributário e do tipo de anúncio que usa. Use estas referências como orientação, não como meta absoluta.</p>
</div>

<h2>Quando Aceitar Margem Menor</h2>
<p>Produtos âncora (que atraem tráfego para a loja), liquidação de estoque parado ou novos produtos para ganhar reputação podem justificar margem menor temporariamente. Mas sempre com prazo definido e acompanhamento — nunca como padrão permanente.</p>
"""
    },
    {
        "slug":  "como-evitar-prejuizo-mercado-livre",
        "title": "Como Evitar Prejuízo no Mercado Livre 2025 | 8 Medidas Essenciais",
        "h1":    "Como Evitar Prejuízo no Mercado Livre: 8 Medidas Que Todo Vendedor Deve Adotar",
        "tag":   "Gestão",
        "desc":  "Aprenda como evitar prejuízo nas suas vendas do Mercado Livre. Erros mais comuns, como identificar produtos no vermelho e o que fazer para reverter.",
        "lead":  "O prejuízo no Mercado Livre raramente acontece de uma vez — ele se acumula silenciosamente em cada venda com margem mal calculada. Essas 8 medidas evitam que isso aconteça.",
        "cta_title": "Detecte Prejuízo Antes Que Seja Tarde",
        "cta_desc":  "Sobrou Quanto ML identifica automaticamente os produtos e períodos com resultado negativo na sua loja.",
        "links": ["produto-no-prejuizo-mercado-livre","como-saber-se-estou-lucrando-mercado-livre","precificacao-mercado-livre","erros-precificacao-mercado-livre"],
        "faq": [
            ("Quais são os principais motivos de prejuízo no ML?", "Precificação incorreta, devolução acima da média, frete subestimado, imposto não considerado e custo fixo não rateado."),
            ("Como identificar um produto no prejuízo?", "Calcule: preço - CMV - comissão - frete - imposto - despesas. Se o resultado for negativo, está no prejuízo."),
            ("O que fazer quando identificar produto no prejuízo?", "Ajuste o preço para o mínimo viável, renegocie com fornecedor ou pause o anúncio. Nunca continue vendendo no vermelho esperando melhorar."),
            ("Promoções do ML podem causar prejuízo?", "Sim. O ML sugere descontos que podem levar o produto abaixo do preço mínimo. Sempre defina um preço mínimo nos anúncios."),
            ("Com que frequência revisar os produtos para evitar prejuízo?", "Mensalmente para produtos estáveis. Semanalmente para produtos em promoção ou com alta volatilidade de custo."),
        ],
        "content": """
<h2>As 8 Medidas Para Evitar Prejuízo</h2>

<h3>1. Calcule o Preço Mínimo de Cada Produto</h3>
<p>Antes de anunciar, defina o preço abaixo do qual você nunca vai vender. Configure esse limite no ML para que promoções automáticas não ultrapassem.</p>

<h3>2. Atualize o CMV Mensalmente</h3>
<p>Custo de produto muda. Reajuste de fornecedor, câmbio ou frete de compra alterado — se o CMV sobe e o preço não, a margem encolhe silenciosamente.</p>

<h3>3. Monitore a Taxa de Devolução Por Produto</h3>
<p>Um produto com 8% de devolução consome 8% da margem em devoluções — além do custo operacional de cada retorno.</p>

<h3>4. Inclua Imposto na Precificação</h3>
<p>MEI paga fixo (ok). Simples Nacional: se sua alíquota subiu com o crescimento do faturamento, recalcule todos os preços.</p>

<div class="callout callout-warn">
<p><strong>Armadilha comum:</strong> Vender muito e ver a alíquota do Simples subir de 6% para 11% sem ajustar os preços. Esse salto de 5% pode transformar margem positiva em prejuízo.</p>
</div>

<h3>5 a 8: Controle Contínuo</h3>
<ul>
<li>Revise o custo de frete após mudanças de tabela das transportadoras</li>
<li>Mantenha reserva financeira para absorver meses negativos</li>
<li>Analise o DRE mensalmente — não só o extrato do ML</li>
<li>Pause imediatamente produtos com margem negativa confirmada</li>
</ul>
"""
    },
    {
        "slug":  "controle-financeiro-mercado-livre",
        "title": "Controle Financeiro Para Vendedores do Mercado Livre | 2025",
        "h1":    "Controle Financeiro Para Vendedores do Mercado Livre: Como Organizar",
        "tag":   "Finanças",
        "desc":  "Aprenda a montar um controle financeiro eficiente para sua loja no Mercado Livre. DRE, fluxo de caixa, conciliação e ferramentas recomendadas.",
        "lead":  "Sem controle financeiro, vender no Mercado Livre é como dirigir no escuro. Você vê o faturamento crescer, mas não sabe se está lucrando — até que o caixa fica negativo.",
        "cta_title": "Controle Financeiro Automático Para Sua Loja",
        "cta_desc":  "Sobrou Quanto ML organiza DRE, fluxo de caixa e conciliação automaticamente — conectado à sua conta ML.",
        "links": ["gestao-financeira-vendedor-mercado-livre","fluxo-de-caixa-mercado-livre","conciliacao-mercado-livre","planilha-controle-mercado-livre"],
        "faq": [
            ("O que é controle financeiro para loja no ML?", "É o registro e análise de todas as entradas (vendas), saídas (custos) e resultado (lucro/prejuízo) do período."),
            ("Por onde começar o controle financeiro?", "Comece pelo mais simples: planilha com entradas e saídas. Depois evolua para DRE mensal e conciliação."),
            ("Qual a diferença entre controle financeiro e contabilidade?", "Controle financeiro é interno e gerencial. Contabilidade é formal e legal. Ambos são necessários, mas o controle financeiro é feito pelo próprio vendedor."),
            ("Com que frequência atualizar o controle?", "Semanalmente para fluxo de caixa. Mensalmente para DRE e conciliação."),
            ("Precisa de contador para ter controle financeiro?", "Não. O controle financeiro gerencial é feito pelo vendedor. O contador cuida das obrigações fiscais."),
        ],
        "content": """
<h2>Os 3 Relatórios do Controle Financeiro</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">📊</div><h4>DRE Mensal</h4><p>Receitas menos custos = lucro ou prejuízo. Visão do resultado do período.</p></div>
<div class="benefit-card"><div class="b-icon">💵</div><h4>Fluxo de Caixa</h4><p>Entradas e saídas reais de dinheiro. Evita falta de capital.</p></div>
<div class="benefit-card"><div class="b-icon">🔄</div><h4>Conciliação</h4><p>Vendas do ML vs repasses recebidos. Detecta cobranças erradas.</p></div>
</div>

<h2>Rotina Mínima de Controle</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>Frequência</th><th>Atividade</th></tr></thead>
<tbody>
<tr><td>Diário</td><td>Conferir repasses do Mercado Pago</td></tr>
<tr><td>Semanal</td><td>Registrar compras de estoque e despesas</td></tr>
<tr><td>Mensal</td><td>Fechar DRE, conciliar extrato ML, calcular CMV real</td></tr>
<tr><td>Trimestral</td><td>Revisar margens por produto, renegociar fornecedores</td></tr>
</tbody>
</table>
</div>

<div class="callout">
<p>Para automatizar todo esse processo, conecte sua conta ML no <strong>Sobrou Quanto ML</strong> — gera DRE, conciliação e controle de margem automaticamente.</p>
</div>
"""
    },
    {
        "slug":  "relatorio-financeiro-mercado-livre",
        "title": "Relatório Financeiro do Mercado Livre 2025 | Como Gerar e Analisar",
        "h1":    "Como Gerar e Analisar o Relatório Financeiro do Mercado Livre",
        "tag":   "Relatório",
        "desc":  "Aprenda a gerar e interpretar o relatório financeiro do Mercado Livre. Entenda cada linha, como cruzar dados e o que as métricas significam para seu negócio.",
        "lead":  "O relatório financeiro do ML mostra vendas e repasses — mas não o lucro. Para chegar no resultado real, você precisa cruzar esse relatório com CMV, impostos e despesas externas.",
        "cta_title": "Relatório Financeiro Completo e Automático",
        "cta_desc":  "Sobrou Quanto ML gera o relatório financeiro completo da sua loja — com lucro líquido, margem e conciliação automáticos.",
        "links": ["relatorio-mensal-mercado-livre","conciliacao-mercado-livre","planilha-dre-mercado-livre","gestao-financeira-vendedor-mercado-livre"],
        "faq": [
            ("Onde gerar o relatório financeiro no ML?", "Acesse Minha conta > Dinheiro > Extratos e relatórios. Você pode exportar por período em CSV ou PDF."),
            ("O que mostra o extrato financeiro do ML?", "Vendas realizadas, comissões cobradas, fretes, devoluções processadas e repasses efetuados."),
            ("O relatório do ML mostra o lucro?", "Não. Mostra receita bruta e algumas deduções, mas não inclui CMV nem impostos. Você precisa complementar externamente."),
            ("Com que frequência exportar o relatório?", "Mensalmente para fechar o DRE. Semanalmente se quiser acompanhar o fluxo de caixa mais de perto."),
            ("Como cruzar o relatório do ML com o banco?", "Compare o total de repasses do extrato ML com os créditos na conta bancária. Diferenças indicam repasses pendentes ou erros."),
        ],
        "content": """
<h2>O Que o Relatório do ML Mostra (e o Que Não Mostra)</h2>
<div class="table-wrapper">
<table>
<thead><tr><th>O ML mostra</th><th>O ML não mostra</th></tr></thead>
<tbody>
<tr><td>Faturamento bruto por período</td><td>Custo do produto (CMV)</td></tr>
<tr><td>Comissão cobrada por venda</td><td>Imposto (DAS, DARF)</td></tr>
<tr><td>Custo de frete por envio</td><td>Despesas fixas operacionais</td></tr>
<tr><td>Devoluções processadas</td><td>Lucro líquido real</td></tr>
<tr><td>Repasses efetuados</td><td>Margem por produto</td></tr>
</tbody>
</table>
</div>

<h2>Como Transformar o Relatório do ML em DRE</h2>
<ol>
<li>Exporte o extrato financeiro do período</li>
<li>Extraia: receita bruta, comissões, fretes, devoluções</li>
<li>Adicione externamente: CMV, imposto do período, despesas fixas</li>
<li>Calcule: receita líquida → lucro bruto → lucro líquido</li>
</ol>

<div class="callout">
<p><strong>Atalho:</strong> Ferramentas como o Sobrou Quanto ML conectam diretamente na API do ML e montam o DRE automaticamente — sem precisar exportar e cruzar manualmente.</p>
</div>
"""
    },
    {
        "slug":  "como-controlar-vendas-mercado-livre",
        "title": "Como Controlar as Vendas do Mercado Livre 2025 | Guia Prático",
        "h1":    "Como Controlar as Vendas do Mercado Livre de Forma Profissional",
        "tag":   "Controle",
        "desc":  "Aprenda como controlar suas vendas do Mercado Livre com eficiência. Métricas essenciais, relatórios e como automatizar o acompanhamento.",
        "lead":  "Controlar vendas vai além de contar pedidos. Um controle profissional acompanha faturamento, margem, devolução e crescimento — e usa esses dados para tomar decisões.",
        "cta_title": "Controle de Vendas Automático e Integrado",
        "cta_desc":  "Sobrou Quanto ML integra com sua conta ML e controla vendas, margem e lucro em um painel unificado.",
        "links": ["controle-financeiro-mercado-livre","gestao-financeira-vendedor-mercado-livre","relatorio-mensal-mercado-livre","fluxo-de-caixa-mercado-livre"],
        "faq": [
            ("Quais métricas acompanhar nas vendas do ML?", "Número de pedidos, faturamento bruto, ticket médio, taxa de conversão, taxa de devolução e margem por produto."),
            ("Como controlar vendas de muitos produtos?", "Agrupe por categoria e analise o Pareto: 20% dos produtos geralmente representam 80% do faturamento. Foque nesses."),
            ("Preciso de ERP para controlar vendas no ML?", "Para até 200 pedidos/mês, uma planilha bem estruturada resolve. Acima disso, considere integração via API."),
            ("Como controlar estoque junto com as vendas?", "Registre entradas (compras) e saídas (vendas) em tempo real. A diferença é o estoque atual."),
            ("Com que frequência analisar as métricas de vendas?", "Vendas diárias: acompanhe o total. Métricas de margem e devolução: semanalmente ou mensalmente."),
        ],
        "content": """
<h2>Dashboard Mínimo de Controle de Vendas</h2>
<div class="benefit-grid">
<div class="benefit-card"><div class="b-icon">📈</div><h4>Pedidos / dia</h4><p>Volume de vendas diário — identifica sazonalidade e campanhas</p></div>
<div class="benefit-card"><div class="b-icon">💰</div><h4>Faturamento / mês</h4><p>Base para calcular imposto e comparar com meses anteriores</p></div>
<div class="benefit-card"><div class="b-icon">🎯</div><h4>Ticket médio</h4><p>Faturamento ÷ pedidos — monitore se está subindo ou caindo</p></div>
<div class="benefit-card"><div class="b-icon">↩️</div><h4>Taxa devolução</h4><p>Devoluções ÷ pedidos — acima de 4% exige ação imediata</p></div>
</div>

<h2>Análise Pareto das Suas Vendas</h2>
<p>Ordene seus produtos por faturamento. Os top 20% provavelmente respondem por 80% da receita. Foque o controle e a otimização nesses produtos — eles têm mais impacto no resultado final.</p>

<div class="callout">
<p><strong>Identifique os "sugadores de lucro":</strong> produtos com alto volume de pedidos mas margem negativa. Eles inflam o número de pedidos mas prejudicam o resultado. Veja <a href="/produto-no-prejuizo-mercado-livre/">Produto no Prejuízo no ML</a>.</p>
</div>
"""
    },
    {
        "slug":  "controle-caixa-mercado-livre",
        "title": "Controle de Caixa Para Vendedores do Mercado Livre | 2025",
        "h1":    "Controle de Caixa no Mercado Livre: Como Fazer e Por Que É Essencial",
        "tag":   "Caixa",
        "desc":  "Aprenda como fazer o controle de caixa da sua loja no Mercado Livre. Diferença entre DRE e fluxo de caixa, e como evitar falta de capital.",
        "lead":  "Loja lucrativa no DRE mas sem dinheiro no caixa — isso é mais comum do que parece no ML. O controle de caixa resolve esse paradoxo.",
        "cta_title": "Controle Seu Caixa Automaticamente",
        "cta_desc":  "Sobrou Quanto ML integra o fluxo de caixa com os repasses do Mercado Pago — sem planilha manual.",
        "links": ["fluxo-de-caixa-mercado-livre","controle-financeiro-mercado-livre","capital-de-giro-mercado-livre","separar-financas-pessoais-empresariais"],
        "faq": [
            ("Por que minha loja lucra mas não tem dinheiro?", "Porque lucro (DRE) e caixa (fluxo) são diferentes. Você pode lucrar em competência mas ter o dinheiro preso em estoque ou aguardando repasse."),
            ("Quando o ML repassa o dinheiro?", "Após a confirmação de entrega pelo comprador. O prazo varia de 7 a 30 dias dependendo da reputação e do tipo de venda."),
            ("Como controlar o caixa no ML?", "Registre as entradas quando o Mercado Pago efetivamente libera o dinheiro — não quando a venda acontece."),
            ("Como evitar falta de capital para comprar estoque?", "Planeje as compras com base no ciclo de repasse do ML. Se o repasse demora 15 dias, mantenha capital suficiente para 15 dias de compras."),
            ("Controle de caixa é o mesmo que DRE?", "Não. DRE registra por competência (quando a venda ocorre). Fluxo de caixa registra por caixa (quando o dinheiro entra/sai de fato)."),
        ],
        "content": """
<h2>DRE vs Fluxo de Caixa: A Diferença Que Importa</h2>
<div class="table-wrapper">
<table>
<thead><tr><th></th><th>DRE</th><th>Fluxo de Caixa</th></tr></thead>
<tbody>
<tr><td>Quando registra</td><td>Na venda (competência)</td><td>No repasse efetivo (caixa)</td></tr>
<tr><td>Mostra</td><td>Se a loja é lucrativa</td><td>Se a loja tem dinheiro</td></tr>
<tr><td>Inclui estoque</td><td>Sim (CMV)</td><td>Só quando comprado</td></tr>
<tr><td>Frequência</td><td>Mensal</td><td>Semanal ou diário</td></tr>
</tbody>
</table>
</div>

<div class="callout callout-warn">
<p><strong>Cenário real:</strong> Você vende R$50.000 em dezembro (DRE positivo), mas o ML só repassa em janeiro. Em dezembro você precisa comprar estoque para janeiro — sem o dinheiro que está retido. Sem reserva de caixa, você trava.</p>
</div>

<h2>Como Montar o Controle de Caixa do ML</h2>
<ol>
<li>Registre entradas: repasses efetivos do Mercado Pago na conta bancária</li>
<li>Registre saídas: compras de estoque, despesas fixas, impostos pagos</li>
<li>Calcule saldo: entradas - saídas = saldo do período</li>
<li>Projete os próximos 30 dias: repasses esperados vs despesas previstas</li>
</ol>
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
    items = ""
    for q, a in faq_list:
        items += f'<div class="faq-item"><button class="faq-q" onclick="toggleFaq(this)" aria-expanded="false">{q}</button><div class="faq-a" hidden><p>{a}</p></div></div>'
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
    print(f"\nGerando {len(PAGES)} paginas (Lote 4)...")
    for p in PAGES:
        generate_page(p)
    print("\nAtualizando sitemap...")
    update_sitemap([p["slug"] for p in PAGES])
    print(f"\nPronto! {len(PAGES)} paginas geradas.")
