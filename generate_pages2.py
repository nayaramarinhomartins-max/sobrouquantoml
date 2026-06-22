# -*- coding: utf-8 -*-
"""
generate_pages2.py  —  Lote 2: mais 24 paginas SEO
Uso: python generate_pages2.py
"""
import os
from datetime import date

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
TEMPLATE   = os.path.join(BASE_DIR, "public", "template-seo.html")
OUTPUT_DIR = os.path.join(BASE_DIR, "public")
SITE_URL   = "https://sobrouquantoml.prospectia.space"
TODAY_ISO  = date.today().strftime("%Y-%m-%d")
TODAY_BR   = date.today().strftime("%d/%m/%Y")

PAGES = [

  {
    "slug": "erros-precificacao-mercado-livre",
    "title": "7 Erros de Precificacao no Mercado Livre que destroem sua margem",
    "desc": "Descubra os erros mais comuns de precificacao no ML e como corrigi-los antes de continuar vendendo no prejuizo sem saber.",
    "tag": "Precificacao",
    "h1": "7 erros de precificacao no Mercado Livre que estao destruindo sua margem",
    "lead": "A maioria dos vendedores que perde dinheiro no ML nao tem problema de volume — tem problema de precificacao. Esses 7 erros aparecem em quase todo negocio que comeca a escalar sem controle financeiro.",
    "read_time": "6",
    "cta_title": "Veja se algum produto seu esta com margem negativa agora",
    "cta_desc": "Importe o relatorio do ML e identifique em segundos quais produtos estao sendo vendidos abaixo do custo real.",
    "content": """
<h2>Erro 1: Nao incluir o frete no calculo</h2>
<p>O erro mais comum. Ao ativar frete gratis, o custo de envio e descontado diretamente do seu repasse. Um produto de R$60 com frete de R$18 perdeu 30% da receita antes de qualquer outro desconto.</p>
<p>Correto: sempre estime o custo medio de frete como percentual do preco e inclua na formula de precificacao.</p>

<h2>Erro 2: Usar a comissao errada</h2>
<p>A comissao varia por categoria — de 10% a 16%. Muitos vendedores usam um numero generico de "12%" para tudo. Em categorias de moda (16%) ou beleza (16%), isso gera uma diferenca de 4 pontos percentuais direto na margem.</p>
<p>Correto: verifique a comissao exata da categoria de cada produto no painel do ML.</p>

<h2>Erro 3: Ignorar o custo do parcelamento</h2>
<p>Quando o comprador parcela em 12x, o ML cobra do vendedor o custo financeiro desse parcelamento — tipicamente 10% a 13% adicionais. Em produtos de ticket alto com muitos parcelamentos, isso pode ser o maior custo da operacao.</p>
<p>Correto: estime o percentual medio de parcelamento com base no historico de vendas e inclua na formula.</p>

<h2>Erro 4: Calcular imposto sobre o lucro em vez do faturamento</h2>
<p>No Simples Nacional e no Lucro Presumido, o imposto incide sobre a receita bruta — nao sobre o lucro. Muitos vendedores calculam o imposto como se fosse sobre o lucro e ficam surpresos com o DAS.</p>
<p>Correto: aplique a aliquota efetiva do seu regime diretamente sobre o valor de venda.</p>

<h2>Erro 5: Nao considerar devolucoes e cancelamentos</h2>
<p>Cada devolucao consome custo do produto + eventual frete de retorno sem receita. Em categorias com taxa de devolucao de 8% a 15% (moda, eletronicos), ignorar isso pode tirar 2 a 4 pontos percentuais da margem media.</p>
<p>Correto: calcule a taxa historica de devolucao por produto e adicione como custo na precificacao.</p>

<h2>Erro 6: Copiar o preco do concorrente sem calcular o proprio custo</h2>
<p>O concorrente pode ter um CMV diferente, comprar em volume maior, estar num regime tributario mais favoravel ou simplesmente estar vendendo no prejuizo. Copiar o preco dele sem calcular o proprio custo e uma armadilha.</p>
<p>Correto: calcule sempre o preco minimo do seu produto antes de olhar para a concorrencia.</p>

<h2>Erro 7: Nunca revisar a precificacao apos mudancas de custo</h2>
<p>O custo do produto muda a cada lote de estoque. A comissao do ML pode mudar. O frete aumenta periodicamente. Um preco que era lucravel ha 6 meses pode estar no prejuizo hoje.</p>
<p>Correto: revise a precificacao de todos os produtos pelo menos uma vez por trimestre com base nos custos atuais.</p>

<div class="callout callout-warn">
  <p><strong>Resumo dos erros mais caros:</strong> frete ignorado + parcelamento nao calculado + imposto sobre lucro em vez de faturamento. Esses tres sozinhos podem transformar uma margem de 25% em prejuizo.</p>
</div>
"""
  },

  {
    "slug": "produto-no-prejuizo-mercado-livre",
    "title": "Como identificar produtos vendidos no prejuizo no Mercado Livre",
    "desc": "Aprenda a identificar produtos com margem negativa no ML antes que o prejuizo se acumule. Sinais de alerta e como agir.",
    "tag": "Gestao Financeira",
    "h1": "Como identificar produtos vendidos no prejuizo no Mercado Livre",
    "lead": "Ter um produto que vende bem no ML nao significa que ele e lucravel. Muitos vendedores descobrem tardiamente que seus produtos mais populares sao exatamente os que mais drenam o caixa.",
    "read_time": "5",
    "cta_title": "Identifique produtos no prejuizo no seu negocio agora",
    "cta_desc": "O Advisor com IA do Sobrou Quanto ML lê seus dados reais e alerta sobre produtos com margem negativa antes que o dano se acumule.",
    "content": """
<h2>Por que produtos populares podem ser os mais perigosos</h2>
<p>Um produto que vende 200 unidades por mes com prejuizo de R$5 por venda acumula R$1.000 de prejuizo mensal — silenciosamente. Quanto maior o volume, maior o buraco.</p>
<p>Isso acontece especialmente quando o preco foi definido para competir, sem calcular o custo real de cada venda.</p>

<h2>Sinais de que um produto pode estar no prejuizo</h2>
<ul>
  <li><strong>Vende muito mas o saldo nao cresce</strong> — volume alto com caixa estagnado e sinal classico</li>
  <li><strong>Preco proximo ao dos concorrentes em produto com frete caro</strong> — frete come a margem</li>
  <li><strong>Produto pesado ou volumoso vendido com frete gratis</strong> — custo de envio provavelmente alto</li>
  <li><strong>Alta taxa de parcelamento</strong> — se a maioria compra parcelado, o desconto de parcelamento e significativo</li>
  <li><strong>CMV subiu mas preco nao foi reajustado</strong> — inflacao de custo sem repasse</li>
</ul>

<h2>Como calcular se um produto esta no prejuizo</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Verificacao</th><th>O que analisar</th></tr></thead>
    <tbody>
      <tr><td>Repasse liquido</td><td>Valor recebido por venda apos desconto do ML</td></tr>
      <tr><td>CMV atual</td><td>Custo de compra do produto no ultimo lote</td></tr>
      <tr><td>Frete real</td><td>Custo medio de envio nos ultimos 30 dias</td></tr>
      <tr><td>Imposto</td><td>Aliquota efetiva sobre o valor vendido</td></tr>
      <tr><td>Resultado</td><td>Repasse - CMV - Frete - Imposto = lucro ou prejuizo</td></tr>
    </tbody>
  </table>
</div>

<h2>O que fazer quando encontrar um produto no prejuizo</h2>
<ol>
  <li><strong>Calcule o preco minimo lucravel</strong> e compare com o mercado</li>
  <li>Se o mercado comporta o preco certo — reajuste imediatamente</li>
  <li>Se nao comporta — avalie descontinuar o produto ou reduzir o custo (negociar com fornecedor, mudar embalagem, etc.)</li>
  <li>Nunca mantenha produto no prejuizo esperando que "o volume vai compensar" — nao vai</li>
</ol>

<div class="callout callout-warn">
  <p><strong>Atencao especial:</strong> Produtos com alta taxa de devolucao tem prejuizo amplificado. Cada devolucao consome CMV + frete de retorno sem receita correspondente. Monitore a taxa de devolucao por produto separadamente.</p>
</div>
"""
  },

  {
    "slug": "capital-de-giro-mercado-livre",
    "title": "Capital de Giro para Vendedores do Mercado Livre: como calcular",
    "desc": "Entenda como calcular e gerenciar o capital de giro para quem vende no ML. Evite ficar sem estoque antes do repasse cair.",
    "tag": "Gestao Financeira",
    "h1": "Capital de giro no Mercado Livre: quanto voce precisa para nao travar",
    "lead": "O prazo de repasse do ML cria um gap entre o momento da venda e o momento do recebimento. Sem capital de giro adequado, o negocio para — literalmente — porque falta produto para vender enquanto o dinheiro nao chega.",
    "read_time": "5",
    "cta_title": "Controle seu caixa com dados reais do ML",
    "cta_desc": "Importe o relatorio do ML e veja entradas, saidas e saldo projetado do mes para tomar decisoes de capital de giro com dados reais.",
    "content": """
<h2>O problema do prazo de repasse do ML</h2>
<p>No Mercado Livre, o repasse demora entre 7 e 21 dias uteis apos a confirmacao de entrega. Isso significa que uma venda feita hoje so vai resultar em dinheiro na conta em 2 a 4 semanas.</p>
<p>Para quem precisa repor estoque constantemente, esse gap cria uma necessidade de capital que muitos vendedores subestimam ao comecar.</p>

<h2>Formula para calcular o capital de giro necessario</h2>
<div class="callout callout-green">
  <p><strong>Capital de giro minimo = (Custo mensal de estoque / 30) x Prazo medio de repasse em dias</strong></p>
</div>
<p>Exemplo: voce gasta R$20.000/mes em estoque e o prazo medio de repasse e 14 dias.<br/>
Capital de giro necessario = (R$20.000 / 30) x 14 = <strong>R$9.333</strong></p>
<p>Esse e o minimo para nao depender de antecipacao ou credito em nenhum momento.</p>

<h2>Reserva de seguranca adicional</h2>
<p>Alem do capital de giro operacional, mantenha uma reserva de seguranca de <strong>30% a 50% sobre o capital de giro</strong> para cobrir:</p>
<ul>
  <li>Picos de devolucao que atrasam repassess</li>
  <li>Aumento repentino de volume (oportunidade de estoque)</li>
  <li>Atrasos excepcionais no repasse do ML</li>
  <li>Impostos trimestrais</li>
</ul>

<h2>Antecipacao do ML: quando usar e quando evitar</h2>
<p>O Mercado Livre oferece antecipacao de recebiveis para vendedores qualificados. O custo tipico e de 2% a 4% ao mes sobre o valor antecipado.</p>
<p><strong>Use antecipacao quando:</strong> ha oportunidade de compra de estoque com desconto maior que o custo da antecipacao.</p>
<p><strong>Evite antecipacao quando:</strong> for para cobrir operacao corrente — isso sinaliza que o capital de giro e insuficiente e a antecipacao vira dependencia permanente.</p>

<h2>Sazonalidade e capital de giro</h2>
<p>Na Black Friday e no Natal, o volume de vendas pode triplicar. Isso significa que o capital de giro necessario tambem triplica. Planejar a captacao ou reserva para esses periodos com 60 a 90 dias de antecedencia e o que separa quem aproveita a sazonalidade de quem fica sem produto no pico.</p>
"""
  },

  {
    "slug": "impostos-vendedor-mercado-livre",
    "title": "Impostos para Vendedores do Mercado Livre: guia completo 2026",
    "desc": "Quais impostos um vendedor do Mercado Livre precisa pagar em 2026? MEI, Simples Nacional e Lucro Presumido explicados de forma simples.",
    "tag": "Fiscal e Tributario",
    "h1": "Impostos para vendedores do Mercado Livre em 2026: o que voce precisa saber",
    "lead": "Muitos vendedores do ML operam informalmente ou sem entender os impostos devidos. Conhecer as obrigacoes fiscais do seu regime tributario nao e so questao de conformidade — e tambem uma forma de proteger a margem e evitar surpresas.",
    "read_time": "7",
    "cta_title": "Veja o impacto real dos impostos no seu DRE",
    "cta_desc": "Importe o relatorio do ML e veja o DRE completo com impostos calculados automaticamente para MEI, Simples Nacional e Lucro Presumido.",
    "content": """
<h2>Vender no ML sem CNPJ: o risco que muitos ignoram</h2>
<p>Pessoa fisica pode vender no ML, mas ha limites. A Receita Federal monitora movimentacoes e o ML informa ao Fisco as receitas dos vendedores. Acima de R$28.559,70 anuais (valor de referencia 2026), a Receita pode questionar a origem da renda na declaracao do IR.</p>
<p>Com CNPJ, o negocio fica regularizado, a carga tributaria geralmente cai e voce pode emitir nota fiscal — obrigatoria para vender para PJ e para alguns marketplaces.</p>

<h2>MEI — Microempreendedor Individual</h2>
<p><strong>Limite:</strong> R$81.000/ano (R$6.750/mes)<br/>
<strong>Imposto:</strong> DAS fixo mensal (~R$71,60 para comercio em 2026)<br/>
<strong>Vantagens:</strong> custo fixo baixo, abertura simples, acesso a credito bancario<br/>
<strong>Limitacoes:</strong> nao pode ter socio, nao emite nota fiscal de produto industrializado com ICMS completo, limite de faturamento baixo</p>

<h2>Simples Nacional — ME e EPP</h2>
<p><strong>Limite:</strong> ate R$4,8 milhoes/ano<br/>
<strong>Imposto:</strong> aliquota sobre faturamento, varia de 4% a 19% por faixa (Anexo I — comercio)<br/>
<strong>Vantagens:</strong> unifica varios impostos, aliquota progressiva, simples de apurar<br/>
<strong>Atencao:</strong> a aliquota incide sobre a receita bruta, mesmo em meses de margem baixa</p>

<h2>Lucro Presumido</h2>
<p><strong>Limite:</strong> ate R$78 milhoes/ano<br/>
<strong>Imposto:</strong> IRPJ + CSLL sobre lucro presumido + PIS/COFINS sobre faturamento (~5,93% base no comercio)<br/>
<strong>Adequado para:</strong> empresas com faturamento alto e margem acima de 10% que saem do Simples<br/>
<strong>Complexidade:</strong> exige contabilidade mais robusta e apuracoes trimestrais</p>

<h2>Comparativo de carga tributaria para um faturamento de R$50.000/mes</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Regime</th><th>Imposto estimado/mes</th><th>% sobre faturamento</th></tr></thead>
    <tbody>
      <tr><td>MEI (acima do limite — irregular)</td><td>R$ 71,60</td><td>0,14% — mas ilegal acima de R$6.750/mes</td></tr>
      <tr><td>Simples Nacional (faixa 3)</td><td>~R$ 3.750</td><td>~7,5%</td></tr>
      <tr><td>Lucro Presumido</td><td>~R$ 2.965</td><td>~5,93%</td></tr>
    </tbody>
  </table>
</div>

<div class="callout callout-warn">
  <p><strong>Atencao:</strong> Essas informacoes sao de carater educacional. A escolha do regime tributario ideal para o seu negocio deve ser feita com um contador, considerando estado de operacao, tipo de produto, margem e volume.</p>
</div>

<h2>O ML informa a Receita Federal?</h2>
<p>Sim. O Mercado Livre, como toda plataforma de pagamentos, e obrigado a informar a Receita Federal as movimentacoes financeiras dos vendedores. Quem opera acima dos limites de cada regime sem CNPJ adequado esta sujeito a autuacao e cobranca retroativa de impostos.</p>
"""
  },

  {
    "slug": "simples-nacional-ou-mei",
    "title": "MEI ou Simples Nacional para vender no Mercado Livre: qual escolher",
    "desc": "Compare MEI e Simples Nacional para vendedores do Mercado Livre. Quando cada regime compensa e como a escolha afeta sua margem.",
    "tag": "Fiscal e Tributario",
    "h1": "MEI ou Simples Nacional para vender no ML: qual regime compensa mais",
    "lead": "A escolha entre MEI e Simples Nacional tem impacto direto na sua margem e no limite de crescimento do negocio. A decisao errada pode custar caro — ou limitar artificialmente o crescimento.",
    "read_time": "5",
    "cta_title": "Veja o impacto do regime tributario no seu DRE",
    "cta_desc": "Importe o relatorio do ML e compare como diferentes regimes tributarios afetam sua margem liquida real.",
    "content": """
<h2>Quando o MEI e suficiente</h2>
<p>O MEI e ideal para vendedores que faturam consistentemente abaixo de R$6.750/mes (R$81.000/ano). Nessa faixa, o DAS fixo (~R$71,60 para comercio) representa uma aliquota efetiva muito baixa — de 1% a 2% do faturamento, dependendo do volume.</p>
<p>Para quem esta comecando no ML com vendas moderadas, o MEI e o caminho mais simples e barato.</p>

<h2>Quando e hora de migrar para o Simples Nacional</h2>
<p>Tres situacoes exigem a migracao para ME/Simples:</p>
<ol>
  <li><strong>Faturamento consistentemente acima de R$5.000/mes</strong> — proximo do teto anual de R$81.000</li>
  <li><strong>Necessidade de emitir NF-e completa</strong> — para vender para pessoas juridicas ou para alguns estados que exigem nota</li>
  <li><strong>Contratacao de funcionario</strong> — MEI so pode ter 1 funcionario; mais que isso exige ME</li>
</ol>

<h2>Comparativo financeiro por faixa de faturamento</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Faturamento mensal</th><th>MEI (DAS fixo)</th><th>Simples (aliquota efetiva)</th><th>Melhor opcao</th></tr></thead>
    <tbody>
      <tr><td>R$ 3.000</td><td>R$ 71,60 (2,4%)</td><td>—</td><td>MEI</td></tr>
      <tr><td>R$ 5.000</td><td>R$ 71,60 (1,4%)</td><td>~R$ 200 (4%)</td><td>MEI</td></tr>
      <tr><td>R$ 8.000</td><td>Irregular (acima do limite)</td><td>~R$ 440 (5,5%)</td><td>Simples</td></tr>
      <tr><td>R$ 20.000</td><td>Irregular</td><td>~R$ 1.200 (6%)</td><td>Simples</td></tr>
      <tr><td>R$ 50.000</td><td>Irregular</td><td>~R$ 3.750 (7,5%)</td><td>Simples ou Presumido</td></tr>
    </tbody>
  </table>
</div>

<h2>O risco de permanecer no MEI alem do limite</h2>
<p>Ultrapassar o faturamento anual do MEI sem migrar resulta em reenquadramento retroativo no Simples Nacional — com pagamento dos impostos da diferenca mais multa de 75% e juros. Em 2026, a multa minima e de R$165,74.</p>
<p>Monitore o faturamento acumulado todo mes. Quando estiver proximo de R$60.000 no ano (em torno de agosto/setembro), inicie o processo de migracao para ME.</p>

<div class="callout">
  <p><strong>Dica pratica:</strong> A migracao de MEI para ME pode ser feita online pelo Portal do Empreendedor sem custo. O processo leva poucos dias e pode ser feito com antecedencia antes de atingir o limite.</p>
</div>
"""
  },

  {
    "slug": "relatorio-mercado-livre-como-exportar",
    "title": "Como exportar o relatorio de vendas do Mercado Livre: passo a passo",
    "desc": "Aprenda como exportar o relatorio de vendas do Mercado Livre em formato XLSX. Guia completo passo a passo para acessar seus dados reais.",
    "tag": "Tutorial",
    "h1": "Como exportar o relatorio de vendas do Mercado Livre: guia passo a passo",
    "lead": "O relatorio de vendas do ML e o documento mais importante para entender sua operacao financeira. Exportar e usar corretamente esse arquivo e o ponto de partida para qualquer analise de lucro, margem ou DRE.",
    "read_time": "4",
    "cta_title": "Ja tem o relatorio? Importe e veja o DRE em segundos",
    "cta_desc": "Faca o upload do relatorio .xlsx do ML e veja lucro, margem e DRE completo calculados automaticamente.",
    "content": """
<h2>Onde encontrar o relatorio de vendas no ML</h2>
<p>O relatorio de vendas esta disponivel no painel do vendedor. O caminho e:</p>
<ol>
  <li>Acesse <strong>mercadolivre.com.br</strong> e entre na sua conta de vendedor</li>
  <li>Va em <strong>Vendas</strong> no menu principal</li>
  <li>Clique em <strong>Relatorios</strong></li>
  <li>Selecione <strong>Relatorio de Vendas</strong></li>
</ol>

<h2>Como configurar o relatorio antes de exportar</h2>
<p>Antes de exportar, configure corretamente o periodo e os campos:</p>
<ul>
  <li><strong>Periodo:</strong> selecione o mes completo desejado (ex: 01/03/2026 a 31/03/2026)</li>
  <li><strong>Formato:</strong> sempre exporte em <strong>.xlsx</strong> (Excel) — e o formato mais completo</li>
  <li><strong>Campos incluidos:</strong> o relatorio padrao ja inclui todos os dados necessarios: valor da venda, comissao, frete, parcelamento, dados do produto e do comprador</li>
</ul>

<h2>O que o relatorio contem</h2>
<p>O arquivo .xlsx exportado tem as seguintes colunas principais:</p>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Coluna</th><th>O que representa</th></tr></thead>
    <tbody>
      <tr><td>Data da venda</td><td>Data e hora da transacao</td></tr>
      <tr><td>Valor da venda</td><td>Preco pago pelo comprador</td></tr>
      <tr><td>Comissao ML</td><td>Taxa cobrada pelo Mercado Livre</td></tr>
      <tr><td>Custo de envio</td><td>Frete descontado (quando frete gratis ativo)</td></tr>
      <tr><td>Taxa de parcelamento</td><td>Custo do parcelamento repassado ao vendedor</td></tr>
      <tr><td>Valor liquido</td><td>Repasse efetivo apos todos os descontos</td></tr>
      <tr><td>Titulo do anuncio</td><td>Nome do produto vendido</td></tr>
      <tr><td>SKU / codigo</td><td>Identificador do produto</td></tr>
    </tbody>
  </table>
</div>

<h2>Limite de periodo por exportacao</h2>
<p>O ML permite exportar no maximo 3 meses por vez. Para analises anuais, exporte em blocos de 3 meses e consolide.</p>

<div class="callout">
  <p><strong>Dica:</strong> Exporte o relatorio sempre no primeiro dia do mes seguinte, quando todas as vendas do mes anterior ja foram processadas e os repasses confirmados. Isso garante dados completos e sem pendencias.</p>
</div>

<h2>Por que o relatorio .xlsx e mais confiavel que a API</h2>
<p>Algumas ferramentas usam a API do ML para buscar dados automaticamente. O relatorio .xlsx tem uma vantagem importante: ele e o mesmo documento oficial que o ML usa internamente, sem limitacoes de historico ou possiveis inconsistencias de API durante picos de acesso.</p>
<p>Os numeros do relatorio sao os numeros definitivos — sem estimativa, sem dado defasado.</p>
"""
  },

  {
    "slug": "cmv-mercado-livre",
    "title": "CMV no Mercado Livre: o que e e como calcular corretamente",
    "desc": "Entenda o que e CMV (Custo da Mercadoria Vendida) para quem vende no ML, como calcular e por que e o numero mais importante da operacao.",
    "tag": "Gestao Financeira",
    "h1": "CMV no Mercado Livre: o que e, como calcular e por que importa tanto",
    "lead": "O CMV — Custo da Mercadoria Vendida — e o primeiro e maior custo de qualquer negocio de revenda no ML. Calcular errado o CMV distorce toda a analise de margem e pode levar a decisoes completamente equivocadas.",
    "read_time": "5",
    "cta_title": "Calcule o CMV e a margem real de cada produto",
    "cta_desc": "Importe o relatorio do ML e cadastre o CMV de cada produto. O sistema calcula a margem real de cada venda automaticamente.",
    "content": """
<h2>O que e CMV</h2>
<p>CMV (Custo da Mercadoria Vendida) e o custo direto de aquisicao ou producao dos produtos que foram efetivamente vendidos em um periodo. Nao e o custo do estoque total — so o custo do que foi vendido.</p>
<p>Para um revendedor no ML: se voce comprou 100 unidades por R$40 cada e vendeu 60 no mes, o CMV do mes e R$40 x 60 = R$2.400.</p>

<h2>Como calcular o CMV corretamente</h2>
<p>Ha tres metodos principais para calcular o CMV. O mais adequado depende de como voce gerencia o estoque:</p>

<h3>Metodo PEPS (Primeiro que Entra, Primeiro que Sai)</h3>
<p>O custo das primeiras unidades compradas e atribuido as primeiras vendas. Recomendado para produtos pereciveis ou com variacao frequente de preco de compra.</p>

<h3>Metodo Custo Medio</h3>
<p>O custo de cada unidade vendida e a media ponderada de todas as compras do produto. Mais simples e muito usado por revendedores no ML.</p>
<div class="callout callout-green">
  <p><strong>Custo medio = Total investido no estoque do produto / Total de unidades em estoque</strong></p>
</div>

<h3>Custo especifico</h3>
<p>Cada unidade tem seu custo individual rastreado. Valido para produtos de alto valor com numero de serie ou identificacao unica.</p>

<h2>Componentes do CMV para revendedores</h2>
<p>O CMV nao e so o preco de compra do fornecedor. Inclui todos os custos para ter o produto disponivel para venda:</p>
<ul>
  <li>Preco de compra ao fornecedor</li>
  <li>Frete de entrada (da fabrica/distribuidor ate voce)</li>
  <li>ICMS na entrada (para empresas no Lucro Presumido)</li>
  <li>Embalagem especifica do produto (quando personalizada)</li>
  <li>Custo de inspecao ou preparo do produto</li>
</ul>

<h2>CMV variavel: o risco de cada novo lote</h2>
<p>Revendedores no ML frequentemente compram de diferentes fornecedores ou em diferentes momentos, com precos variados. Isso significa que o CMV muda a cada lote de estoque.</p>
<p>Se voce comprou 100 unidades em janeiro por R$35 e mais 100 em marco por R$42 (apos reajuste do fornecedor), o custo medio atual e diferente do que voce usou na precificacao original. Sem atualizar, a margem calculada e ficticia.</p>

<div class="callout callout-warn">
  <p><strong>Impacto pratico:</strong> Um aumento de 10% no CMV sem reajuste de preco pode eliminar toda a margem de lucro em produtos que ja operavam com margem apertada.</p>
</div>
"""
  },

  {
    "slug": "devolucoes-mercado-livre",
    "title": "Devolucoes no Mercado Livre: impacto financeiro e como gerenciar",
    "desc": "Entenda o impacto financeiro das devolucoes no ML na sua margem e DRE. Como calcular a taxa de devolucao e gerenciar o prejuizo.",
    "tag": "Gestao Financeira",
    "h1": "Devolucoes no Mercado Livre: o impacto financeiro que poucos calculam",
    "lead": "Cada devolucao no ML representa uma venda que virou custo puro. Produto retornado + frete + tempo de processamento — sem receita correspondente. Em categorias com alta taxa de devolucao, esse impacto pode ser o que diferencia um negocio lucravel de um no vermelho.",
    "read_time": "5",
    "cta_title": "Veja o impacto real das devolucoes no seu DRE",
    "cta_desc": "O Sobrou Quanto ML calcula automaticamente o impacto de cancelamentos e devolucoes no seu resultado mensal.",
    "content": """
<h2>O custo real de uma devolucao</h2>
<p>Uma devolucao nao e simplesmente "a venda nao aconteceu". Os custos incluem:</p>
<ul>
  <li><strong>Custo do produto:</strong> o item saiu do estoque e voltou (potencialmente danificado)</li>
  <li><strong>Frete de saida:</strong> ja foi pago e nao e reembolsado em todos os casos</li>
  <li><strong>Frete de retorno:</strong> dependendo do motivo, pode ser custo do vendedor</li>
  <li><strong>Tempo de processamento:</strong> inspecao, reestoque ou descarte</li>
  <li><strong>Impacto na reputacao:</strong> devolucoes afetam o indicador de reclamacoes</li>
</ul>

<h2>Taxa de devolucao por categoria: referencias do mercado</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Categoria</th><th>Taxa media de devolucao</th></tr></thead>
    <tbody>
      <tr><td>Eletronicos</td><td>3% a 8%</td></tr>
      <tr><td>Moda e vestuario</td><td>8% a 20%</td></tr>
      <tr><td>Calcados</td><td>10% a 18%</td></tr>
      <tr><td>Casa e decoracao</td><td>2% a 6%</td></tr>
      <tr><td>Ferramentas</td><td>2% a 5%</td></tr>
      <tr><td>Beleza e saude</td><td>1% a 4%</td></tr>
    </tbody>
  </table>
</div>

<h2>Como calcular o impacto das devolucoes na margem</h2>
<div class="callout callout-green">
  <p><strong>Custo total de devolucoes = (Taxa de devolucao%) x (CMV medio + Frete medio)</strong></p>
  <p>Esse valor deve ser subtraido da margem calculada por produto.</p>
</div>
<p>Exemplo: produto com CMV de R$50, frete de R$15, taxa de devolucao de 8%.<br/>
Custo de devolucao por unidade vendida = 8% x (R$50 + R$15) = <strong>R$5,20 por venda</strong><br/>
Isso e como se cada produto vendido ficasse R$5,20 mais caro.</p>

<h2>Como reduzir devolucoes no ML</h2>
<ul>
  <li><strong>Fotos reais e precisas:</strong> a maioria das devolucoes e por "nao era o que esperava" — fotos profissionais e descritivas reduzem isso</li>
  <li><strong>Descricao completa com medidas e especificacoes:</strong> especialmente em moda e eletronicos</li>
  <li><strong>Embalagem adequada:</strong> danos no transporte geram devolucao por defeito</li>
  <li><strong>Controle de qualidade no despacho:</strong> verificar o produto antes de embalar</li>
</ul>

<h2>Devolucoes e o DRE: como lancar corretamente</h2>
<p>No DRE, devolucoes entram como deducao da receita bruta, antes do calculo da margem. Isso significa que o imposto Simples ou Presumido pode ser recalculado excluindo as vendas devolvidas — o que representa economia tributaria que muitos nao aproveitam.</p>
"""
  },

  {
    "slug": "frete-gratis-mercado-livre",
    "title": "Frete Gratis no Mercado Livre: quando compensa e quando prejudica",
    "desc": "Descubra quando o frete gratis no Mercado Livre aumenta suas vendas com lucro — e quando ele esta destruindo sua margem silenciosamente.",
    "tag": "Estrategia",
    "h1": "Frete gratis no Mercado Livre: quando compensa e quando destroi sua margem",
    "lead": "Frete gratis aumenta conversao — mas o custo sai do seu bolso. Para alguns produtos, e estrategia inteligente. Para outros, e o caminho mais rapido para vender no prejuizo sem perceber.",
    "read_time": "5",
    "cta_title": "Calcule se o frete gratis esta compensando nos seus produtos",
    "cta_desc": "Veja o impacto real do frete em cada produto com o relatorio completo do ML — sem estimativa, com os numeros reais.",
    "content": """
<h2>Como funciona o frete gratis no ML</h2>
<p>Quando voce ativa frete gratis em um anuncio, o Mercado Livre desconta o custo do envio diretamente do seu repasse. O comprador nao paga nada — mas o valor do frete sai da sua receita.</p>
<p>O ML incentiva fortemente o frete gratis porque aumenta a taxa de conversao dos anuncios. Produtos com frete gratis aparecem melhor nos resultados de busca e tem maior probabilidade de ganhar o Buy Box.</p>

<h2>Quando o frete gratis compensa</h2>
<p>O frete gratis e estrategico quando:</p>
<ul>
  <li><strong>O produto tem ticket alto</strong> — o frete representa um percentual pequeno do valor (abaixo de 8% a 10%)</li>
  <li><strong>O produto e leve e compacto</strong> — custo de envio baixo absoluto</li>
  <li><strong>A concorrencia toda oferece frete gratis</strong> — nao oferecer pode eliminar o anuncio da competicao</li>
  <li><strong>A margem suporta</strong> — calculada com o frete incluido, a margem ainda e saudavel</li>
</ul>

<h2>Quando o frete gratis destroi a margem</h2>
<p>Evite frete gratis quando:</p>
<ul>
  <li><strong>Produto pesado ou volumoso com preco baixo</strong> — o frete pode ser maior que a margem bruta</li>
  <li><strong>Vendas para regioes distantes</strong> (Norte e Nordeste) — frete mais caro que para SP/RJ</li>
  <li><strong>A margem ja e apertada (abaixo de 15%)</strong> — qualquer adicional de custo coloca no vermelho</li>
</ul>

<h2>O calculo do break-even do frete gratis</h2>
<div class="callout callout-green">
  <p><strong>Frete gratis so compensa se:</strong><br/>
  (Aumento em % de conversao x Receita adicional) &gt; Custo total do frete do periodo</p>
</div>
<p>Na pratica, voce precisa de dados historicos para comparar periodos com e sem frete gratis. Mas uma regra pratica: se o frete representa mais de 12% do preco de venda, o risco de prejudicar a margem e alto.</p>

<div class="table-wrapper">
  <table>
    <thead><tr><th>Preco do produto</th><th>Frete estimado</th><th>% do preco</th><th>Recomendacao</th></tr></thead>
    <tbody>
      <tr><td>R$ 30</td><td>R$ 15</td><td>50%</td><td>Nunca frete gratis</td></tr>
      <tr><td>R$ 80</td><td>R$ 18</td><td>22%</td><td>Muito arriscado</td></tr>
      <tr><td>R$ 150</td><td>R$ 20</td><td>13%</td><td>Calcular com cuidado</td></tr>
      <tr><td>R$ 300</td><td>R$ 22</td><td>7%</td><td>Geralmente viavel</td></tr>
      <tr><td>R$ 600</td><td>R$ 25</td><td>4%</td><td>Frete gratis recomendado</td></tr>
    </tbody>
  </table>
</div>
"""
  },

  {
    "slug": "ponto-de-equilibrio-mercado-livre",
    "title": "Ponto de Equilibrio para Vendedores do Mercado Livre: como calcular",
    "desc": "Aprenda a calcular o ponto de equilibrio do seu negocio no ML. Descubra quantas vendas voce precisa fazer para cobrir todos os custos.",
    "tag": "Gestao Financeira",
    "h1": "Ponto de equilibrio no Mercado Livre: quantas vendas voce precisa para nao ter prejuizo",
    "lead": "O ponto de equilibrio e o numero minimo de vendas que cobre todos os custos fixos e variaveis. Conhecer esse numero e o que permite saber se o mes foi lucravel ou nao — antes de olhar para o saldo.",
    "read_time": "5",
    "cta_title": "Veja se seu negocio ML passou do ponto de equilibrio este mes",
    "cta_desc": "Com o DRE automatico do Sobrou Quanto ML, voce ve em segundos se o mes foi lucravel e quanto sobrou apos todos os custos.",
    "content": """
<h2>O que e ponto de equilibrio</h2>
<p>Ponto de equilibrio (break-even) e o momento em que a receita total iguala os custos totais — antes disso ha prejuizo, depois ha lucro. Conhecer esse ponto permite saber com antecedencia se o volume de vendas do mes vai ser suficiente para cobrir os custos.</p>

<h2>Tipos de custo para calcular o ponto de equilibrio</h2>
<p><strong>Custos fixos:</strong> nao variam com o volume de vendas</p>
<ul>
  <li>DAS / imposto fixo (MEI)</li>
  <li>Ferramentas e plataformas (assinaturas mensais)</li>
  <li>Salario proprio ou de funcionarios</li>
  <li>Aluguel (se houver deposito ou escritorio)</li>
</ul>
<p><strong>Custos variaveis:</strong> crescem proporcionalmente com as vendas</p>
<ul>
  <li>CMV (custo do produto)</li>
  <li>Comissao ML</li>
  <li>Frete</li>
  <li>Imposto sobre faturamento (Simples/Presumido)</li>
  <li>Embalagem</li>
</ul>

<h2>Formula do ponto de equilibrio</h2>
<div class="callout callout-green">
  <p><strong>Ponto de equilibrio (R$) = Custos fixos / Margem de contribuicao (%)</strong><br/><br/>
  <strong>Margem de contribuicao = (Preco de venda - Custos variaveis) / Preco de venda</strong></p>
</div>

<h2>Exemplo pratico</h2>
<p>Vendedor com produto a R$200, custos variaveis de R$140 por venda e custos fixos de R$3.000/mes:</p>
<ul>
  <li>Margem de contribuicao = (R$200 - R$140) / R$200 = 30%</li>
  <li>Ponto de equilibrio = R$3.000 / 30% = <strong>R$10.000 de faturamento</strong></li>
  <li>Em unidades: R$10.000 / R$200 = <strong>50 vendas/mes</strong></li>
</ul>
<p>Abaixo de 50 vendas: prejuizo. Acima: lucro. Simples assim.</p>

<h2>Como usar o ponto de equilibrio no dia a dia</h2>
<p>Acompanhe o faturamento acumulado ao longo do mes. Quando passar do ponto de equilibrio (R$10.000 no exemplo), cada venda adicional gera lucro puro na margem de contribuicao definida.</p>
<p>Isso ajuda a tomar decisoes como: vale a pena fazer uma promocao no meio do mes para acelerar o volume? Com o ponto de equilibrio definido, a resposta e quantificavel.</p>
"""
  },

  {
    "slug": "separar-financas-pessoais-empresariais",
    "title": "Como separar financas pessoais e empresariais no Mercado Livre",
    "desc": "Por que misturar financas pessoais e do negocio no ML e perigoso e como separar corretamente para ter clareza financeira real.",
    "tag": "Gestao Financeira",
    "h1": "Separar financas pessoais e do negocio no ML: por que e como fazer",
    "lead": "Misturar dinheiro pessoal com dinheiro do negocio e o erro mais basico — e mais comum — de quem vende no ML. Sem essa separacao, voce nunca sabe realmente quanto o negocio esta lucrando ou perdendo.",
    "read_time": "4",
    "cta_title": "Veja o resultado real do seu negocio separado das suas financas pessoais",
    "cta_desc": "O DRE automatico do Sobrou Quanto ML mostra so o resultado do negocio ML — sem misturar com despesas pessoais.",
    "content": """
<h2>Por que misturar e um erro tao comum</h2>
<p>Quando o negocio e pequeno e o proprio vendedor e quem compra, vende e despacha, parece natural usar a mesma conta bancaria e o mesmo cartao para tudo. Mas essa pratica cria um cego financeiro completo: voce nao sabe se esta retirando mais do que o negocio gera, nem se o negocio esta subsidiando suas despesas pessoais.</p>

<h2>Os problemas concretos de misturar</h2>
<ul>
  <li><strong>DRE impossivel:</strong> nao da para saber o lucro real do negocio se despesas pessoais estao no mesmo extrato</li>
  <li><strong>Imposto errado:</strong> despesas pessoais nao sao dedutiveis — lan-las como custo do negocio e irregularidade fiscal</li>
  <li><strong>Decisoes de escala erradas:</strong> voce pode achar que o negocio e mais lucrativo do que e (ou menos)</li>
  <li><strong>Dificuldade de conseguir credito:</strong> bancos e financiadoras analisam a movimentacao da conta PJ separada</li>
</ul>

<h2>Como separar na pratica</h2>
<ol>
  <li><strong>Abra uma conta PJ</strong> — MEI e ME podem abrir conta PJ gratuita em varios bancos digitais (Nubank PJ, Inter PJ, Mercado Pago PJ, C6 PJ)</li>
  <li><strong>Configure o ML para repassar para a conta PJ</strong> — altere a conta de recebimento nas configuracoes financeiras do ML</li>
  <li><strong>Defina um pro-labore fixo</strong> — um valor mensal que voce transfere da conta PJ para a pessoal como seu "salario"</li>
  <li><strong>Nao use o cartao da empresa para gastos pessoais</strong> — mesmo que seja so um cafe</li>
</ol>

<h2>Pro-labore: quanto retirar sem comprometer o negocio</h2>
<p>O pro-labore e o salario que o dono retira do negocio. Uma referencia saudavel: retirar no maximo <strong>50% do lucro liquido</strong> do mes anterior, reinvestindo o restante em estoque, capital de giro ou reserva.</p>
<p>Se o negocio ainda esta crescendo, retirar menos e reinvestir mais acelera o crescimento. Se ja esta maduro, pode-se retirar uma parcela maior.</p>

<div class="callout">
  <p><strong>Conta PJ gratuita para MEI/ME:</strong> Nubank PJ, Mercado Pago, Inter PJ e Banco do Brasil oferecem conta PJ sem mensalidade. Nao ha motivo para misturar contas.</p>
</div>
"""
  },

  {
    "slug": "reserva-financeira-vendedor-ml",
    "title": "Reserva Financeira para Vendedores do Mercado Livre: quanto guardar",
    "desc": "Quanto um vendedor do ML deve ter de reserva financeira e como construir essa reserva de forma progressiva.",
    "tag": "Gestao Financeira",
    "h1": "Reserva financeira para vendedores do ML: quanto guardar e como construir",
    "lead": "Todo negocio tem oscilacoes — meses ruins, devolucoes acima do normal, queda repentina no volume. Sem reserva financeira, qualquer imprevisto pode paralisar a operacao. Para quem vende no ML, construir essa reserva e uma prioridade desde o primeiro mes lucravel.",
    "read_time": "4",
    "cta_title": "Monitore o lucro liquido mensal para alimentar sua reserva",
    "cta_desc": "Com o DRE automatico do Sobrou Quanto ML, voce sabe exatamente quanto sobrou em cada mes para separar para reserva.",
    "content": """
<h2>Por que a reserva e essencial para vendedores ML</h2>
<p>O negocio no ML tem oscilacoes naturais: sazonalidade, mudancas de algoritmo, produtos que saem de moda, concorrentes que entram com preco mais baixo. Sem reserva, qualquer dessas situacoes pode forcar uma decisao ruim — vender abaixo do custo para girar estoque, por exemplo.</p>

<h2>Tres tipos de reserva para construir</h2>
<h3>1. Reserva de emergencia operacional (3 meses de custo fixo)</h3>
<p>Cobre os custos fixos do negocio (imposto, ferramentas, eventual funcionario) por 3 meses sem nenhuma venda. E o colchao minimo para nao precisar fechar se o volume cair.</p>

<h3>2. Reserva de capital de giro (equivalente a 3-4 semanas de estoque)</h3>
<p>Cobre a reposicao de estoque enquanto os repasses do mes anterior ainda nao cairaem. Impede a ruptura de estoque em momentos de alta demanda.</p>

<h3>3. Reserva para oportunidades (flexivel)</h3>
<p>Para aproveitar compras oportunistas do fornecedor, liquidacoes de estoque ou expansao para novas categorias. Nao e urgente, mas diferencia quem cresce de quem estagna.</p>

<h2>Quanto guardar por mes</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Fase do negocio</th><th>% do lucro liquido para reserva</th></tr></thead>
    <tbody>
      <tr><td>Iniciando (primeiros 6 meses)</td><td>50% — prioridade maxima em construir o colchao</td></tr>
      <tr><td>Crescendo (reserva parcialmente formada)</td><td>20% a 30%</td></tr>
      <tr><td>Maduro (reservas adequadas formadas)</td><td>10% a 15% (manutencao)</td></tr>
    </tbody>
  </table>
</div>

<h2>Onde guardar a reserva</h2>
<ul>
  <li><strong>CDB com liquidez diaria:</strong> rendimento acima da poupanca, saque imediato quando necessario</li>
  <li><strong>Tesouro Selic:</strong> seguro, liquido, rende a taxa Selic</li>
  <li><strong>Conta remunerada PJ:</strong> alguns bancos digitais remuneram saldo em conta PJ automaticamente</li>
</ul>
<p>Evite deixar a reserva parada em conta corrente sem rendimento — e dinheiro perdendo valor para a inflacao todos os dias.</p>
"""
  },

  {
    "slug": "escalar-vendas-mercado-livre",
    "title": "Como escalar vendas no Mercado Livre sem destruir a margem",
    "desc": "Estrategias para escalar as vendas no ML mantendo margem saudavel. O que monitorar antes, durante e depois de escalar.",
    "tag": "Estrategia de Negocio",
    "h1": "Como escalar vendas no Mercado Livre sem destruir a margem no processo",
    "lead": "Escalar vendas no ML sem controle financeiro e como acelerar em direcao a um precipicio. Cada erro de margem que passa despercebido com 100 vendas vira 10x pior com 1.000 vendas. Escalar certo exige dados antes de movimento.",
    "read_time": "6",
    "cta_title": "Veja a margem de cada produto antes de escalar",
    "cta_desc": "Importe o relatorio do ML e identifique quais produtos tem margem suficiente para escalar — e quais vao prejudicar o resultado se escalados.",
    "content": """
<h2>A regra de ouro antes de escalar</h2>
<p>Voce so deve escalar um produto se ele ja tem margem positiva confirmada com dados reais — nao estimativa. Escalar um produto com margem negativa ou indefinida so amplifica o prejuizo.</p>
<p>Antes de aumentar o volume de qualquer produto, saiba:</p>
<ul>
  <li>Lucro liquido por unidade vendida (com todos os custos)</li>
  <li>Taxa de devolucao historica do produto</li>
  <li>CMV atualizado com o lote atual de estoque</li>
  <li>Capacidade de capital de giro para suportar mais estoque</li>
</ul>

<h2>Quais produtos escalar primeiro</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Criterio</th><th>Produto ideal para escalar</th></tr></thead>
    <tbody>
      <tr><td>Margem liquida</td><td>Acima de 20%</td></tr>
      <tr><td>Taxa de devolucao</td><td>Abaixo de 5%</td></tr>
      <tr><td>Tendencia de busca</td><td>Estavel ou crescente</td></tr>
      <tr><td>Concorrencia</td><td>Nao acirrada a ponto de comprimir preco</td></tr>
      <tr><td>Facilidade de reposicao</td><td>Fornecedor confiavel com estoque disponivel</td></tr>
    </tbody>
  </table>
</div>

<h2>O que monitorar ao escalar</h2>
<p>Quando voce aumenta volume, alguns indicadores precisam ser acompanhados de perto:</p>
<ul>
  <li><strong>CMV medio:</strong> comprar mais pode mudar o custo medio se o fornecedor oferece desconto por volume — ou aumentar se voce precisar de fontes alternativas</li>
  <li><strong>Taxa de devolucao:</strong> pode subir se a logistica nao acompanhar o volume</li>
  <li><strong>Prazo de reputacao:</strong> atrasos de entrega ao escalar podem prejudicar a reputacao e, consequentemente, a comissao</li>
  <li><strong>Capital de giro:</strong> mais volume = mais estoque = mais capital imobilizado antes do repasse</li>
</ul>

<h2>Escalar via anuncio Premium: quando vale</h2>
<p>Ativar anuncio Premium aumenta visibilidade mas adiciona custo por venda (1% a 2%). A conta so fecha se o aumento de conversao gerar receita adicional maior que o custo do Premium.</p>
<p>Teste sempre com um produto de cada vez, por pelo menos 30 dias, comparando margem antes e depois do Premium.</p>

<h2>O erro mais comum ao escalar no ML</h2>
<p>Aumentar estoque de produtos sem margem confirmada, movido pela empolgacao com volume de vendas. Resultado: muito produto vendido, caixa vazio, e descoberta tardia que o produto estava no prejuizo.</p>
<p>A sequencia correta: <strong>1) Confirmar margem → 2) Testar volume pequeno → 3) Analisar resultado → 4) Escalar</strong></p>
"""
  },

  {
    "slug": "reputacao-mercado-livre",
    "title": "Reputacao no Mercado Livre: como afeta custos e o que fazer",
    "desc": "Entenda como a reputacao no ML afeta seu prazo de repasse, visibilidade e custos. E o que fazer para manter ou recuperar a reputacao.",
    "tag": "Estrategia",
    "h1": "Reputacao no Mercado Livre: como ela afeta seus custos e o que fazer para proteger",
    "lead": "A reputacao no ML nao e so uma questao de imagem — ela afeta diretamente o prazo de repasse, a visibilidade dos anuncios e o custo efetivo da operacao. Vendedor com reputacao ruim paga mais para operar no mesmo canal.",
    "read_time": "5",
    "cta_title": "Gerencie seu resultado financeiro para crescer com reputacao",
    "cta_desc": "Veja lucro e margem por produto para identificar quais geraram reclamacoes e devolucoes — antes que prejudiquem sua reputacao.",
    "content": """
<h2>Como a reputacao e calculada no ML</h2>
<p>O Mercado Livre calcula a reputacao com base nas ultimas 60 vendas (ou ultimos 60 dias, o que incluir mais vendas). Os indicadores principais sao:</p>
<ul>
  <li><strong>Reclamacoes:</strong> percentual de vendas com reclamacao aberta</li>
  <li><strong>Vendas canceladas:</strong> percentual de vendas canceladas pelo vendedor</li>
  <li><strong>Entregas atrasadas:</strong> percentual de entregas alem do prazo prometido</li>
</ul>

<h2>Cores da reputacao e impacto financeiro</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Cor</th><th>Prazo de repasse</th><th>Visibilidade</th></tr></thead>
    <tbody>
      <tr><td>Verde (otima)</td><td>7 dias uteis</td><td>Maxima — Buy Box favorecido</td></tr>
      <tr><td>Amarela (boa)</td><td>14 dias uteis</td><td>Reduzida nos resultados</td></tr>
      <tr><td>Laranja (regular)</td><td>14 a 21 dias uteis</td><td>Prejudicada</td></tr>
      <tr><td>Vermelha (ruim)</td><td>21+ dias uteis</td><td>Muito prejudicada</td></tr>
    </tbody>
  </table>
</div>
<p>A diferenca entre reputacao verde e vermelha e de ate 14 dias no prazo de repasse. Para um negocio que fatura R$30.000/mes, isso representa R$30.000 a mais imobilizados — com impacto direto no capital de giro.</p>

<h2>O impacto financeiro invisivel da reputacao ruim</h2>
<p>Alem do prazo de repasse, reputacao ruim reduz a visibilidade nos resultados de busca — o que diminui o volume de vendas sem que o vendedor perceba claramente a causa. Menos vendas com os mesmos custos fixos = margem comprimida.</p>

<h2>Como proteger a reputacao</h2>
<ul>
  <li><strong>Despachar no prazo:</strong> use Mercado Envios para prazo calculado automaticamente e mais confiavel</li>
  <li><strong>Responder perguntas e reclamacoes rapido:</strong> resolucao rapida evita que reclamacoes se tornem metricas negativas</li>
  <li><strong>Manter estoque atualizado:</strong> vender produto sem estoque leva a cancelamento — o pior indicador para reputacao</li>
  <li><strong>Qualidade da embalagem:</strong> produto danificado na entrega gera reclamacao automatica</li>
</ul>
"""
  },

  {
    "slug": "mercado-pago-taxas",
    "title": "Taxas do Mercado Pago 2026: o que o vendedor ML precisa saber",
    "desc": "Entenda as taxas do Mercado Pago aplicadas nas vendas do ML. Como o processamento de pagamento afeta o repasse e a margem do vendedor.",
    "tag": "Taxas e Custos",
    "h1": "Taxas do Mercado Pago nas vendas do ML: o que afeta seu repasse",
    "lead": "O Mercado Pago processa todos os pagamentos do Mercado Livre. Entender como as taxas de processamento e parcelamento funcionam e essencial para calcular o repasse real de cada venda.",
    "read_time": "4",
    "cta_title": "Veja o repasse liquido real de cada venda no ML",
    "cta_desc": "Importe o relatorio do ML e veja o repasse liquido real de cada venda, com todas as taxas do Mercado Pago incluidas.",
    "content": """
<h2>Como o Mercado Pago se relaciona com o ML</h2>
<p>O Mercado Pago e a plataforma de pagamentos do ecossistema Mercado Livre. Toda venda no ML e processada pelo Mercado Pago — e as taxas de processamento ja estao incluidas na comissao cobrada do vendedor.</p>
<p>Isso significa que, para o vendedor, nao ha taxa separada de "processamento de pagamento" — ela esta embutida na comissao de categoria.</p>

<h2>O que o Mercado Pago cobra separadamente</h2>
<p>A principal taxa separada e o <strong>custo de parcelamento</strong>. Quando o comprador parcela, o Mercado Pago adianta o valor total para o vendedor (ou repassa conforme o calendario), mas cobra o custo financeiro desse adiantamento.</p>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Parcelamento</th><th>Custo aproximado ao vendedor</th></tr></thead>
    <tbody>
      <tr><td>1x (a vista)</td><td>Sem custo adicional</td></tr>
      <tr><td>2x a 3x</td><td>~3% a 5%</td></tr>
      <tr><td>4x a 6x</td><td>~5% a 8%</td></tr>
      <tr><td>7x a 12x</td><td>~9% a 13%</td></tr>
      <tr><td>13x a 18x</td><td>~14% a 18%</td></tr>
    </tbody>
  </table>
</div>

<h2>Calendario de repasse do Mercado Pago</h2>
<p>O repasse do Mercado Pago para o vendedor segue este fluxo:</p>
<ol>
  <li>Venda realizada — valor fica retido</li>
  <li>Entrega confirmada (rastreio ou prazo maximo)</li>
  <li>Prazo de protecao ao comprador (geralmente 2 dias)</li>
  <li>Repasse disponivel na conta ML</li>
  <li>Transferencia para conta bancaria (imediata ou agendada)</li>
</ol>
<p>O prazo total entre a venda e o dinheiro na conta bancaria varia de 7 a 21 dias, dependendo da reputacao do vendedor.</p>

<h2>Antecipacao de recebiveis no Mercado Pago</h2>
<p>Vendedores elegíveis podem solicitar antecipacao dos recebiveis antes do calendario normal. O custo varia tipicamente de 1,99% a 3,99% ao mes sobre o valor antecipado.</p>
<p>Use a antecipacao com criterio: e vantajosa quando o custo do capital e menor que o ganho gerado pelo uso imediato do dinheiro (reposicao de estoque com desconto, por exemplo).</p>
"""
  },

  {
    "slug": "quanto-ganhar-mercado-livre",
    "title": "Quanto da para ganhar vendendo no Mercado Livre em 2026",
    "desc": "Descubra quanto e realista ganhar vendendo no Mercado Livre. Margens tipicas, volumes e o que separa vendedores que lucram dos que nao lucram.",
    "tag": "Estrategia de Negocio",
    "h1": "Quanto da para ganhar vendendo no Mercado Livre em 2026: a resposta honesta",
    "lead": "A resposta honesta: depende inteiramente de como voce gerencia a operacao. Existem vendedores com R$5.000/mes de lucro liquido e vendedores com R$100.000 de faturamento no vermelho. A diferenca nao e o volume — e o controle.",
    "read_time": "6",
    "cta_title": "Descubra o que realmente esta sobrando no seu ML",
    "cta_desc": "Importe o relatorio do ML e veja lucro liquido real, margem por produto e DRE completo. Sem achismo — so dados.",
    "content": """
<h2>A verdade sobre faturamento vs lucro no ML</h2>
<p>O Mercado Livre e cheio de historias de vendedores que faturam R$50k, R$100k, R$500k por mes. O que raramente aparece: qual e o lucro liquido desses vendedores.</p>
<p>Com as taxas do ML (12% a 16% de comissao + frete + parcelamento), impostos e custo do produto, e completamente possivel faturar muito e lucrar pouco — ou nada.</p>

<h2>Margens tipicas por categoria no ML</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Categoria</th><th>Margem bruta tipica</th><th>Margem liquida tipica</th></tr></thead>
    <tbody>
      <tr><td>Eletronicos e informatica</td><td>15% a 25%</td><td>5% a 12%</td></tr>
      <tr><td>Moda e vestuario</td><td>40% a 60%</td><td>15% a 30%</td></tr>
      <tr><td>Casa e decoracao</td><td>35% a 55%</td><td>15% a 28%</td></tr>
      <tr><td>Beleza e saude</td><td>40% a 65%</td><td>18% a 35%</td></tr>
      <tr><td>Ferramentas</td><td>30% a 50%</td><td>12% a 25%</td></tr>
      <tr><td>Brinquedos</td><td>35% a 55%</td><td>14% a 28%</td></tr>
    </tbody>
  </table>
</div>

<h2>Exemplos de lucro liquido por faturamento</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Faturamento mensal</th><th>Margem 10%</th><th>Margem 20%</th><th>Margem 30%</th></tr></thead>
    <tbody>
      <tr><td>R$ 10.000</td><td>R$ 1.000</td><td>R$ 2.000</td><td>R$ 3.000</td></tr>
      <tr><td>R$ 30.000</td><td>R$ 3.000</td><td>R$ 6.000</td><td>R$ 9.000</td></tr>
      <tr><td>R$ 80.000</td><td>R$ 8.000</td><td>R$ 16.000</td><td>R$ 24.000</td></tr>
      <tr><td>R$ 200.000</td><td>R$ 20.000</td><td>R$ 40.000</td><td>R$ 60.000</td></tr>
    </tbody>
  </table>
</div>

<h2>O que diferencia quem lucra de quem nao lucra</h2>
<p>Nos anos de experiencia do mercado, o padrao e claro. Vendedores que lucram consistentemente no ML tem em comum:</p>
<ul>
  <li><strong>Conhecem o CMV real de cada produto</strong> — nao estimam</li>
  <li><strong>Calculam a precificacao com todos os custos</strong> — incluindo frete e parcelamento</li>
  <li><strong>Monitoram margem por produto mensalmente</strong> — e descontinuam o que nao tem margem</li>
  <li><strong>Separam financas pessoais e do negocio</strong> — sabem exatamente o que o negocio gera</li>
  <li><strong>Tem capital de giro adequado</strong> — nao dependem de antecipacao permanente</li>
</ul>

<div class="callout callout-green">
  <p><strong>Conclusao:</strong> Dar para ganhar muito bem no ML. Mas o lucro vem de gestao financeira rigorosa, nao de volume de vendas. Faturamento e vaidade. Lucro e o que paga as contas.</p>
</div>
"""
  },

  {
    "slug": "vale-a-pena-vender-mercado-livre",
    "title": "Vale a Pena Vender no Mercado Livre em 2026? A resposta com dados",
    "desc": "Analise honesta de quando vale a pena vender no Mercado Livre em 2026: vantagens, desvantagens, taxas e o que determina o sucesso.",
    "tag": "Estrategia de Negocio",
    "h1": "Vale a pena vender no Mercado Livre em 2026? A resposta honesta com dados",
    "lead": "Com comissoes de ate 16%, frete, parcelamento e concorrencia intensa, muitos vendedores se perguntam se ainda vale a pena o ML em 2026. A resposta depende da categoria, da margem do produto e da qualidade da gestao financeira.",
    "read_time": "6",
    "cta_title": "Descubra se seu negocio ML e lucravel com dados reais",
    "cta_desc": "Importe o relatorio do ML e veja o lucro real do seu negocio. Se for lucravel, voce vai querer escalar. Se nao for, melhor descobrir agora.",
    "content": """
<h2>As vantagens reais do Mercado Livre</h2>
<ul>
  <li><strong>Audiencia massiva:</strong> mais de 80 milhoes de usuarios ativos no Brasil — nenhum outro marketplace chega perto</li>
  <li><strong>Infraestrutura pronta:</strong> pagamento, logistica, atendimento ao comprador — tudo resolvido pela plataforma</li>
  <li><strong>Acesso a credito:</strong> Mercado Credito para capital de giro baseado no historico de vendas</li>
  <li><strong>Full commerce:</strong> opcao de estoque e logistica gerida pelo ML (Mercado Envios Full)</li>
  <li><strong>Baixa barreira de entrada:</strong> qualquer pessoa com CNPJ pode comecar a vender hoje</li>
</ul>

<h2>As desvantagens que poucos calculam</h2>
<ul>
  <li><strong>Taxas acumuladas altas:</strong> comissao + frete + parcelamento pode chegar a 28% a 35% do valor da venda</li>
  <li><strong>Dependencia da plataforma:</strong> mudancas no algoritmo ou nas politicas do ML afetam o negocio diretamente</li>
  <li><strong>Concorrencia de preco intensa:</strong> mercado muito transparente tende a comprimir margens em categorias populares</li>
  <li><strong>Prazo de repasse:</strong> dinheiro fica retido de 7 a 21 dias — exige capital de giro</li>
</ul>

<h2>Quando vale muito a pena</h2>
<p>O ML e excelente para:</p>
<ul>
  <li>Produtos com margem bruta acima de 40% (espaco para absorver as taxas)</li>
  <li>Produtos exclusivos ou de nicho com pouca concorrencia direta</li>
  <li>Revendedores com acesso a fornecedor exclusivo ou preco muito competitivo</li>
  <li>Fabricantes que vendem diretamente sem intermediario (D2C)</li>
</ul>

<h2>Quando pode nao compensar</h2>
<p>Cuidado ao entrar no ML com:</p>
<ul>
  <li>Produtos commoditizados com margem bruta abaixo de 25% — as taxas vao comer tudo</li>
  <li>Produtos pesados ou volumosos com frete caro relativo ao preco</li>
  <li>Categorias com taxa de devolucao muito alta sem diferencial de produto claro</li>
</ul>

<h2>A conclusao pratica</h2>
<p>O ML vale a pena quando a margem suporta as taxas e ainda gera lucro. Para saber se o SEU negocio no ML vale a pena, ha um caminho simples: calcule o lucro liquido real do ultimo mes com todos os custos incluidos.</p>
<p>Se for positivo e sustentavel — vale muito. Se for perto de zero ou negativo — e hora de ajustar precificacao, produto ou modelo antes de continuar investindo tempo e capital.</p>
"""
  },

  {
    "slug": "anuncio-full-mercado-livre",
    "title": "Mercado Envios Full: custos, vantagens e quando compensa",
    "desc": "Entenda como funciona o Mercado Envios Full, quais sao os custos reais e quando ele compensa para o vendedor do ML.",
    "tag": "Logistica e Operacao",
    "h1": "Mercado Envios Full: custos reais e quando compensa para o seu negocio",
    "lead": "O Full e o servico de fulfillment do Mercado Livre — voce manda o estoque para o deposito do ML e eles cuidam de tudo. Conveniente, mas com custos que precisam ser calculados com precisao antes de migrar.",
    "read_time": "5",
    "cta_title": "Calcule se o Full esta impactando positivamente sua margem",
    "cta_desc": "Com o relatorio do ML importado no Sobrou Quanto, voce ve a margem real das vendas Full separadas das vendas normais.",
    "content": """
<h2>Como funciona o Mercado Envios Full</h2>
<p>No Mercado Envios Full, o vendedor envia seu estoque para os centros de distribuicao do ML. Quando uma venda acontece, o proprio ML embala, despacha e entrega o produto. O vendedor nao precisa se preocupar com logistica de saida.</p>
<p>Vantagens operacionais: entrega em 1 a 2 dias, acesso ao selo "Full" que aumenta conversao, e menor carga operacional para o vendedor.</p>

<h2>Custos do Full que precisam entrar no DRE</h2>
<ul>
  <li><strong>Taxa de armazenagem:</strong> cobrada por unidade armazenada por dia, varia por categoria e tamanho do produto</li>
  <li><strong>Taxa de picking e packing:</strong> cobrada por pedido processado</li>
  <li><strong>Frete de entrada:</strong> custo de enviar o estoque do vendedor para o deposito do ML</li>
  <li><strong>Taxa por produto devolvido:</strong> quando o comprador devolve, ha custo de reprocessamento</li>
</ul>

<h2>Quando o Full compensa financeiramente</h2>
<p>O Full tende a compensar quando:</p>
<ul>
  <li>O produto tem alto giro — estoque que rotaciona rapido tem baixo custo de armazenagem relativo</li>
  <li>O vendedor tem dificuldade operacional para manter despacho rapido com a propria logistica</li>
  <li>O ticket medio e suficientemente alto para absorver as taxas adicionais</li>
  <li>O selo Full aumenta significativamente a conversao e o volume de vendas</li>
</ul>

<h2>Quando o Full pode nao compensar</h2>
<ul>
  <li>Produtos com baixo giro ficam armazenados por muito tempo, acumulando taxa de armazenagem</li>
  <li>Produtos sazonais que passam meses parados entre as datas de pico</li>
  <li>Produtos com muita variacao (tamanho, cor) que exigem gestao complexa de estoque fracionado</li>
</ul>

<div class="callout">
  <p><strong>Calculo essencial:</strong> Compare a margem de uma venda Full (com todas as taxas adicionais) com a margem da venda pelo seu proprio despacho. Se o aumento de volume gerado pelo Full mais do que compensar o custo adicional — vale. Se nao — talvez nao.</p>
</div>
"""
  },

  {
    "slug": "ticket-medio-mercado-livre",
    "title": "Como aumentar o Ticket Medio no Mercado Livre e melhorar a margem",
    "desc": "Estrategias para aumentar o ticket medio no ML e por que isso melhora a margem de cada venda. Calculos e exemplos praticos.",
    "tag": "Estrategia de Negocio",
    "h1": "Como aumentar o ticket medio no Mercado Livre para melhorar sua margem",
    "lead": "Aumentar o ticket medio — o valor medio de cada venda — e uma das formas mais eficientes de melhorar a margem no ML. Certos custos sao fixos por venda (frete, processamento), entao vender mais caro por transacao dilui esses custos.",
    "read_time": "5",
    "cta_title": "Veja o ticket medio e a margem atual do seu negocio",
    "cta_desc": "Importe o relatorio do ML e veja o ticket medio por produto e como ele afeta a margem liquida do seu negocio.",
    "content": """
<h2>Por que ticket medio alto melhora a margem</h2>
<p>Alguns custos de cada venda no ML sao relativamente fixos — o frete, por exemplo, nao dobra so porque o produto custa o dobro. Isso cria uma economia de escala por transacao: quanto mais caro o produto, menor o percentual do frete sobre o valor da venda.</p>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Preco do produto</th><th>Frete (R$18)</th><th>% do frete sobre preco</th></tr></thead>
    <tbody>
      <tr><td>R$ 60</td><td>R$ 18</td><td>30%</td></tr>
      <tr><td>R$ 120</td><td>R$ 18</td><td>15%</td></tr>
      <tr><td>R$ 250</td><td>R$ 20</td><td>8%</td></tr>
      <tr><td>R$ 500</td><td>R$ 22</td><td>4,4%</td></tr>
    </tbody>
  </table>
</div>

<h2>Estrategias para aumentar o ticket medio</h2>
<h3>Kit e bundle de produtos</h3>
<p>Vender varios produtos juntos em um unico anuncio aumenta o ticket medio sem aumentar o numero de transacoes — e portanto sem multiplicar os custos fixos por venda.</p>
<p>Exemplo: em vez de vender uma caneca por R$25 (margem apertada com frete), vender um kit com 4 canecas por R$90 — o frete e o mesmo, mas a receita e quase 4x maior.</p>

<h3>Linha premium do mesmo produto</h3>
<p>Oferecer uma versao de maior valor do mesmo produto captura compradores dispostos a pagar mais. A comissao do ML sobe proporcionalmente, mas o frete e outros custos fixos nao sobem na mesma proporcao.</p>

<h3>Venda adicional no anuncio</h3>
<p>Anuncios que mencionam acessorios, complementos ou garantia estendida no titulo ou descricao podem aumentar o ticket do item principal.</p>

<h2>Produtos de baixo ticket: o problema estrutural</h2>
<p>Produtos com preco abaixo de R$50 sao muito dificeis de manter lucratives no ML, especialmente com frete gratis. A comissao + frete juntos podem representar 40% a 60% do valor da venda.</p>
<p>Se sua categoria naturalmente tem ticket baixo, considere:</p>
<ul>
  <li>Vender sempre em kits ou multiplos</li>
  <li>Cobrar frete (o comprador paga) para produtos abaixo de um valor de referencia</li>
  <li>Avaliar se a categoria e viavel com as taxas atuais do ML</li>
</ul>
"""
  },

  {
    "slug": "sazonalidade-mercado-livre",
    "title": "Sazonalidade no Mercado Livre: como planejar o ano para maximizar lucro",
    "desc": "Calendario de sazonalidade do Mercado Livre com as principais datas de pico e como planejar estoque, capital e precificacao para cada periodo.",
    "tag": "Estrategia de Negocio",
    "h1": "Sazonalidade no Mercado Livre: calendario de datas e como planejar o ano",
    "lead": "O faturamento no ML nao e linear ao longo do ano. Datas como Black Friday, Natal e Dia das Maes podem representar 3x a 5x o volume normal — e quem nao planeja com antecedencia perde oportunidade ou fica sem produto no pico.",
    "read_time": "5",
    "cta_title": "Analise a sazonalidade do seu negocio com dados reais",
    "cta_desc": "Compare o DRE de diferentes meses do ano com o Sobrou Quanto ML e identifique seus picos de faturamento e margem.",
    "content": """
<h2>Calendario de datas relevantes no ML</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Data</th><th>Periodo</th><th>Impacto tipico</th></tr></thead>
    <tbody>
      <tr><td>Dia das Maes</td><td>2a semana de maio</td><td>Alto — especialmente moda, beleza, presentes</td></tr>
      <tr><td>Dia dos Namorados</td><td>12 de junho</td><td>Medio-alto — joias, eletronicos, flores</td></tr>
      <tr><td>Dia dos Pais</td><td>2o domingo de agosto</td><td>Medio-alto — ferramentas, eletronicos, roupas</td></tr>
      <tr><td>Dia das Criancas</td><td>12 de outubro</td><td>Alto — brinquedos, games, roupas infantis</td></tr>
      <tr><td>Black Friday</td><td>Ultima semana de novembro</td><td>Muito alto — todas as categorias</td></tr>
      <tr><td>Natal</td><td>Dezembro inteiro</td><td>Muito alto — pico do ano para a maioria</td></tr>
      <tr><td>Volta as aulas</td><td>Janeiro a fevereiro</td><td>Alto — material escolar, mochilas, eletronicos</td></tr>
    </tbody>
  </table>
</div>

<h2>Como planejar o estoque para datas de pico</h2>
<p>Para cada data relevante para sua categoria, planeje:</p>
<ul>
  <li><strong>60 a 90 dias antes:</strong> negociar e comprar estoque adicional com o fornecedor</li>
  <li><strong>30 dias antes:</strong> conferir se o estoque chegou e esta disponivel no anuncio</li>
  <li><strong>15 dias antes:</strong> preparar anuncios com copy especifica para a data</li>
  <li><strong>Durante o pico:</strong> monitorar estoque diariamente para nao zerar</li>
</ul>

<h2>Capital de giro na sazonalidade</h2>
<p>Picos de vendas exigem mais capital de giro. Se voce vende R$30.000 normalmente e pretende vender R$90.000 na Black Friday, precisa ter capital para financiar R$90.000 em estoque — mesmo antes de receber os repasses.</p>
<p>Calcule o capital de giro adicional necessario e providencie com antecedencia (propria reserva, antecipacao do ML, ou credito PJ).</p>

<h2>Nao tente competir em preco durante os picos</h2>
<p>A tentacao e baixar o preco para converter mais durante a Black Friday. Mas com volume alto, cada real de margem sacrificado multiplica. Mantenha a margem e otimize conversao com fotos, descricao e reputacao — nao com preco.</p>
"""
  },

  {
    "slug": "estoque-mercado-livre",
    "title": "Gestao de Estoque para Vendedores do Mercado Livre",
    "desc": "Como gerenciar o estoque para vender no ML sem ruptura e sem capital imobilizado em excesso. Indicadores essenciais e boas praticas.",
    "tag": "Logistica e Operacao",
    "h1": "Gestao de estoque no Mercado Livre: como evitar ruptura e excesso",
    "lead": "Estoque demais paralisa capital. Estoque de menos perde venda e prejudica reputacao. Encontrar o ponto certo e um dos maiores desafios operacionais de quem vende no ML — e ele muda todo mes.",
    "read_time": "5",
    "cta_title": "Monitore o resultado de cada produto para otimizar o estoque",
    "cta_desc": "Veja quais produtos geram mais lucro e qual o volume de vendas mensal real para calcular o estoque ideal com dados concretos.",
    "content": """
<h2>Os dois problemas do estoque mal gerenciado</h2>
<h3>Estoque excessivo — capital morto</h3>
<p>Produto parado no estoque e capital imobilizado que nao gera retorno. Alem disso, produtos parados por muito tempo tem risco de obsolescencia, dano fisico ou necessidade de liquidacao abaixo do custo.</p>

<h3>Ruptura de estoque — venda perdida e reputacao danificada</h3>
<p>Anuncio pausado por falta de produto perde posicao no ranking. Pior: se a venda foi realizada e voce nao tem o produto para despachar, gera cancelamento — o indicador que mais prejudica a reputacao no ML.</p>

<h2>Indicadores essenciais de estoque</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Indicador</th><th>Calculo</th><th>Para que serve</th></tr></thead>
    <tbody>
      <tr><td>Giro de estoque</td><td>CMV / Estoque medio</td><td>Quantas vezes o estoque "girou" no periodo</td></tr>
      <tr><td>Dias de estoque</td><td>Estoque atual / Venda media diaria</td><td>Quantos dias o estoque atual dura</td></tr>
      <tr><td>Estoque de seguranca</td><td>Venda diaria media x Prazo do fornecedor</td><td>Quantidade minima para nao ter ruptura</td></tr>
      <tr><td>Ponto de pedido</td><td>Estoque de seguranca + Consumo no prazo de reposicao</td><td>Quando pedir mais ao fornecedor</td></tr>
    </tbody>
  </table>
</div>

<h2>Como calcular o estoque ideal por produto</h2>
<ol>
  <li>Calcule a venda media diaria do produto nos ultimos 30 a 60 dias</li>
  <li>Multiplique pelo prazo de reposicao do fornecedor (em dias)</li>
  <li>Adicione um buffer de seguranca de 20% a 30% para oscilacoes</li>
  <li>Esse e o estoque minimo que voce deve ter sempre disponivel</li>
</ol>
<p>Exemplo: produto com 5 vendas/dia, fornecedor com prazo de 10 dias. Estoque minimo = 5 x 10 x 1,25 = <strong>62 unidades</strong>.</p>

<h2>Produtos lentos: o que fazer</h2>
<p>Se um produto tem giro muito baixo (menos de uma venda por semana), avalie:</p>
<ul>
  <li>Reducao de preco para acelerar a saida (dentro dos limites da margem)</li>
  <li>Combo com produto de alto giro para criar bundle</li>
  <li>Cancelamento do produto — liberar o capital para produtos com melhor performance</li>
</ul>
"""
  },

  {
    "slug": "buy-box-mercado-livre",
    "title": "Buy Box no Mercado Livre: o que e e como ganhar sem sacrificar margem",
    "desc": "Entenda o que e o Buy Box do Mercado Livre, como e calculado e como ganhar posicao sem entrar em guerra de preco que destroi a margem.",
    "tag": "Estrategia",
    "h1": "Buy Box no Mercado Livre: como ganhar posicao sem entrar em guerra de preco",
    "lead": "O Buy Box e a posicao privilegiada de compra no ML — quem ganha aparece primeiro e converte muito mais. Mas ganhar o Buy Box cortando preco pode ser mais prejudicial do que nao telo.",
    "read_time": "5",
    "cta_title": "Calcule se a estrategia de preco atual esta sendo lucravel",
    "cta_desc": "Importe o relatorio do ML e veja se os produtos que ganharam Buy Box estao gerando margem positiva ou negativa.",
    "content": """
<h2>O que e o Buy Box e por que importa</h2>
<p>Quando varios vendedores oferecem o mesmo produto no ML, o sistema escolhe um para aparecer no botao principal de compra — isso e o Buy Box. Quem esta no Buy Box recebe a grande maioria das vendas daquele produto.</p>
<p>Ganhar o Buy Box pode multiplicar o volume de vendas. Perder o Buy Box pode praticamente zerar as vendas de um produto.</p>

<h2>Fatores que determinam o Buy Box</h2>
<p>O algoritmo do ML considera multiplos fatores — nao so o preco:</p>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Fator</th><th>Peso</th></tr></thead>
    <tbody>
      <tr><td>Preco competitivo</td><td>Alto</td></tr>
      <tr><td>Reputacao do vendedor (cor)</td><td>Alto</td></tr>
      <tr><td>Qualidade do anuncio (fotos, descricao)</td><td>Medio-alto</td></tr>
      <tr><td>Prazo de entrega</td><td>Medio-alto</td></tr>
      <tr><td>Estoque disponivel</td><td>Medio</td></tr>
      <tr><td>Tipo de anuncio (Premium)</td><td>Medio</td></tr>
      <tr><td>Historico de vendas</td><td>Medio</td></tr>
    </tbody>
  </table>
</div>

<h2>A armadilha da guerra de preco pelo Buy Box</h2>
<p>A tentacao e ir baixando o preco ate ganhar o Buy Box do concorrente. O problema: o concorrente pode ter um CMV menor, estar no prejuizo intencionalmente para crescer, ou simplesmente nao estar calculando os custos corretamente.</p>
<p>Entrar nessa guerra pode resultar em: ganhar o Buy Box e vender no prejuizo — o pior dos dois mundos.</p>

<h2>Como competir sem guerra de preco</h2>
<ul>
  <li><strong>Melhore a reputacao:</strong> vendedor verde com preco ligeiramente acima de um laranja pode ganhar o Buy Box</li>
  <li><strong>Melhore o anuncio:</strong> fotos profissionais e descricao completa aumentam o score do anuncio</li>
  <li><strong>Use Mercado Envios Full:</strong> entrega mais rapida e um fator forte no algoritmo</li>
  <li><strong>Responda perguntas rapidamente:</strong> tempo de resposta afeta o score do anuncio</li>
</ul>

<h2>Preco minimo antes de competir</h2>
<p>Antes de qualquer decisao de preco para competir pelo Buy Box, calcule o preco minimo que garante margem positiva. Esse e o floor — abaixo dele, nao ha Buy Box que justifique vender.</p>
"""
  },

  {
    "slug": "planilha-controle-mercado-livre",
    "title": "Planilha de Controle Financeiro para Mercado Livre: o que precisa ter",
    "desc": "O que uma planilha de controle financeiro para vendedores do ML precisa ter — e por que a planilha manual sempre falha em algum momento.",
    "tag": "Controle Financeiro",
    "h1": "Planilha de controle financeiro para o Mercado Livre: o que incluir e quando ela para de ser suficiente",
    "lead": "A planilha e o primeiro recurso de quem comeca a tentar controlar as financas do ML. Funciona no inicio — mas tem um limite claro de escala e confiabilidade que todo vendedor enfrenta em algum momento.",
    "read_time": "5",
    "cta_title": "Va alem da planilha com DRE automatico do relatorio ML",
    "cta_desc": "Importe o relatorio do Mercado Livre e veja DRE, margem e lucro por produto em segundos — sem montar nada manualmente.",
    "content": """
<h2>O que uma boa planilha de controle ML precisa ter</h2>
<p>Se voce vai montar uma planilha de controle, ela precisa incluir pelo menos:</p>
<ul>
  <li><strong>Registro de vendas:</strong> data, produto, quantidade, preco de venda</li>
  <li><strong>CMV por produto:</strong> custo de aquisicao atualizado por lote</li>
  <li><strong>Deducoes do ML:</strong> comissao, frete, parcelamento — por venda</li>
  <li><strong>Impostos:</strong> aliquota efetiva aplicada sobre a receita bruta</li>
  <li><strong>Despesas fixas:</strong> ferramentas, embalagem, eventual pessoal</li>
  <li><strong>DRE mensal:</strong> consolidacao de receita, custos e lucro liquido</li>
  <li><strong>Margem por produto:</strong> para identificar o que escalar e o que cortar</li>
</ul>

<h2>Por que a planilha manual sempre tem problemas</h2>
<h3>Problema 1: preenchimento manual gera erros</h3>
<p>Com dezenas ou centenas de vendas por mes, digitar cada venda manualmente e inviavel — e sujeito a erros de digitacao que distorcem o DRE inteiro.</p>

<h3>Problema 2: o relatorio do ML tem formato diferente da planilha</h3>
<p>O relatorio do ML exporta em formato .xlsx com dezenas de colunas no padrao deles. Copiar e colar para a planilha de controle exige tratamento manual dos dados toda vez.</p>

<h3>Problema 3: CMV desatualizado</h3>
<p>Se o CMV nao e atualizado a cada lote de estoque, toda a analise de margem fica errada. Na planilha manual, e facil esquecer de atualizar.</p>

<h3>Problema 4: nao escala com o negocio</h3>
<p>Com 10 vendas por mes, a planilha e ok. Com 300 vendas por mes e 50 SKUs diferentes, ela vira um pesadelo — lento, sujeito a erros e que ninguem mais consegue manter atualizado.</p>

<h2>Quando e hora de ir alem da planilha</h2>
<p>Alguns sinais de que a planilha chegou no limite:</p>
<ul>
  <li>Voce fica semanas sem atualizar porque e trabalhoso</li>
  <li>Encontra erros de formula que nao sabe quando aconteceram</li>
  <li>Leva mais de 2 horas para fechar o DRE do mes</li>
  <li>Nao consegue ver margem por produto rapidamente</li>
</ul>
"""
  },

  {
    "slug": "calcular-imposto-simples-mercado-livre",
    "title": "Como Calcular o Imposto do Simples Nacional para Vendas no ML",
    "desc": "Passo a passo para calcular o imposto do Simples Nacional sobre as vendas no Mercado Livre. Formula da aliquota efetiva com exemplos praticos.",
    "tag": "Fiscal e Tributario",
    "h1": "Como calcular o imposto do Simples Nacional para vendas no Mercado Livre",
    "lead": "Calcular o Simples Nacional corretamente nao e complicado, mas tem detalhes que fazem diferenca na hora de apurar o DAS. Entender a formula da aliquota efetiva e saber como aplicar sobre a receita do ML vai evitar surpresas no fechamento do mes.",
    "read_time": "6",
    "cta_title": "Veja o DRE com imposto Simples calculado automaticamente",
    "cta_desc": "Importe o relatorio do ML e veja o DRE completo com o imposto Simples Nacional calculado sobre a receita real do mes.",
    "content": """
<h2>Como funciona o calculo do Simples Nacional</h2>
<p>O Simples Nacional nao usa simplesmente a aliquota da tabela. A aliquota que voce realmente paga — a <strong>aliquota efetiva</strong> — e calculada com uma formula que considera o faturamento dos ultimos 12 meses (RBT12) e uma parcela de deducao fixa por faixa.</p>
<div class="callout callout-green">
  <p><strong>Aliquota efetiva = [(RBT12 x Aliquota nominal) - Parcela a deduzir] / RBT12</strong></p>
</div>

<h2>Tabela do Simples Nacional — Anexo I (Comercio) 2026</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Faixa</th><th>Faturamento 12 meses</th><th>Aliquota nominal</th><th>Parcela a deduzir</th></tr></thead>
    <tbody>
      <tr><td>1a</td><td>Ate R$ 180.000</td><td>4,00%</td><td>R$ 0,00</td></tr>
      <tr><td>2a</td><td>R$ 180.001 a R$ 360.000</td><td>7,30%</td><td>R$ 5.940,00</td></tr>
      <tr><td>3a</td><td>R$ 360.001 a R$ 720.000</td><td>9,50%</td><td>R$ 13.860,00</td></tr>
      <tr><td>4a</td><td>R$ 720.001 a R$ 1.800.000</td><td>10,70%</td><td>R$ 22.500,00</td></tr>
      <tr><td>5a</td><td>R$ 1.800.001 a R$ 3.600.000</td><td>14,30%</td><td>R$ 87.300,00</td></tr>
      <tr><td>6a</td><td>R$ 3.600.001 a R$ 4.800.000</td><td>19,00%</td><td>R$ 378.000,00</td></tr>
    </tbody>
  </table>
</div>

<h2>Exemplo pratico de calculo</h2>
<p>Empresa com faturamento acumulado dos ultimos 12 meses de R$280.000 (2a faixa). Faturamento do mes atual: R$25.000.</p>
<ol>
  <li>RBT12 = R$ 280.000 (esta na 2a faixa)</li>
  <li>Aliquota efetiva = [(R$280.000 x 7,3%) - R$5.940] / R$280.000</li>
  <li>= [R$20.440 - R$5.940] / R$280.000</li>
  <li>= R$14.500 / R$280.000 = <strong>5,18%</strong></li>
  <li>DAS do mes = R$25.000 x 5,18% = <strong>R$1.295,00</strong></li>
</ol>

<h2>A base de calculo: receita bruta inclui tudo</h2>
<p>O Simples e calculado sobre a receita bruta — que no ML corresponde ao valor total das vendas, antes dos descontos do ML. Isso e importante: voce paga imposto sobre o valor que o comprador pagou, mesmo que o ML tenha descontado a comissao antes de te repassar.</p>

<div class="callout callout-warn">
  <p><strong>Deducao de devolucoes:</strong> Vendas canceladas ou devolvidas podem ser deduzidas da base de calculo do Simples do mes. Mantenha o registro das devolucoes para reduzir corretamente a base de apuracao.</p>
</div>

<h2>Quando o DAS vence</h2>
<p>O DAS do Simples Nacional vence no dia 20 do mes seguinte ao periodo de apuracao. Para vendas de marco, o DAS vence em 20 de abril. Atrasos geram multa de 0,33% ao dia ate 20% + juros Selic.</p>
"""
  },

  {
    "slug": "nota-fiscal-mercado-livre",
    "title": "Nota Fiscal para Vendas no Mercado Livre: quando e obrigatorio",
    "desc": "Entenda quando e obrigatorio emitir nota fiscal nas vendas do Mercado Livre e o que acontece se voce nao emitir.",
    "tag": "Fiscal e Tributario",
    "h1": "Nota fiscal nas vendas do Mercado Livre: quando e obrigatorio e como funciona",
    "lead": "A emissao de nota fiscal nas vendas do ML depende do seu regime tributario, do estado e do tipo de comprador. Ignorar essa obrigacao pode resultar em multas e problemas fiscais que complicam o negocio.",
    "read_time": "5",
    "cta_title": "Mantenha o controle financeiro e fiscal do seu negocio ML",
    "cta_desc": "Com o DRE automatico do Sobrou Quanto ML, voce tem a base para o controle fiscal correto das suas vendas mensais.",
    "content": """
<h2>MEI: quando e obrigatorio emitir NF</h2>
<p>O MEI e dispensado de emitir nota fiscal para vendas a pessoas fisicas (CPF). Porem, e <strong>obrigado</strong> a emitir nota fiscal quando vende para pessoas juridicas (CNPJ) — independentemente do valor.</p>
<p>O MEI emite NFS-e (Nota Fiscal de Servicos Eletronico) para servicos e NF-e (Nota Fiscal Eletronica) para comercio. Muitos estados exigem que o MEI se cadastre na prefeitura ou Sefaz para emitir.</p>

<h2>Simples Nacional: NF-e obrigatoria em varias situacoes</h2>
<p>Para empresas no Simples Nacional que vendem produtos, a emissao de NF-e e obrigatoria em geral — exceto em estados que possuem regime especial para MEI e microempresas em determinadas categorias.</p>
<p>A NF-e contem o ICMS, que varia por estado e produto. Empresas no Simples tem o ICMS ja incluido no DAS — mas a nota precisa ser emitida com o codigo de tributacao correto.</p>

<h2>O que o ML exige do vendedor</h2>
<p>O Mercado Livre nao obriga o vendedor a emitir nota fiscal em todas as vendas — mas permite que o comprador solicite a nota e disponibiliza um campo especifico para isso no processo de compra.</p>
<p>Vendedores que nao emitem nota quando solicitado pelo comprador podem receber reclamacoes que prejudicam a reputacao.</p>

<h2>O risco de nao emitir NF quando obrigatorio</h2>
<p>Vender sem emitir nota fiscal quando ha obrigacao legal sujeita o vendedor a:</p>
<ul>
  <li>Multa da Receita Federal ou Sefaz estadual</li>
  <li>Apreensao de mercadoria em transito (em alguns estados, a NF acompanha a mercadoria)</li>
  <li>Irregularidade que pode levar ao cancelamento do CNPJ</li>
</ul>

<div class="callout callout-warn">
  <p><strong>Recomendacao:</strong> Consulte um contador sobre as obrigacoes de emissao de NF especificas para o seu estado, regime e categoria de produto. As regras variam e mudam com frequencia.</p>
</div>

<h2>Emissao de NF e custo operacional</h2>
<p>Emitir nota fiscal para cada venda com volume alto exige um sistema de emissao. Existem plataformas com integracao ao ML que emitem NF automaticamente apos a confirmacao da venda — o custo mensal varia de R$50 a R$200 dependendo do volume.</p>
"""
  },

]

def load_template():
    with open(TEMPLATE, encoding="utf-8") as f:
        return f.read()

def generate_page(tpl, page):
    html = tpl
    for key, val in page.items():
        html = html.replace("{{" + key.upper() + "}}", str(val))
    html = html.replace("{{DATE_ISO}}", TODAY_ISO)
    html = html.replace("{{DATE_BR}}", TODAY_BR)
    return html

def append_sitemap(entries):
    sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(sitemap_path, encoding="utf-8") as f:
        current = f.read()
    block = "\n".join([f"""
  <url>
    <loc>{SITE_URL}/{p['slug']}/</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""" for p in entries])
    updated = current.replace("</urlset>", block + "\n\n</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(updated)

def main():
    tpl = load_template()
    generated = []
    for page in PAGES:
        folder = os.path.join(OUTPUT_DIR, page["slug"])
        os.makedirs(folder, exist_ok=True)
        html = generate_page(tpl, page)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(page["slug"])
        print(f"  [OK] /{page['slug']}/index.html")

    append_sitemap(PAGES)
    print(f"\n  [OK] sitemap.xml atualizado")
    print(f"\nTotal lote 2: {len(generated)} paginas")

if __name__ == "__main__":
    main()
