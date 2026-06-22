# -*- coding: utf-8 -*-
"""
generate_pages.py
Gera paginas SEO estaticas para o Sobrou Quanto ML.
Saida: public/[slug]/index.html  (copiado pelo Vite para dist/)
Uso:   python generate_pages.py
"""

import os
import re
from datetime import date

# ── CONFIG ────────────────────────────────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
TEMPLATE    = os.path.join(BASE_DIR, "public", "template-seo.html")
OUTPUT_DIR  = os.path.join(BASE_DIR, "public")
SITE_URL    = "https://sobrouquantoml.prospectia.space"
TODAY_ISO   = date.today().strftime("%Y-%m-%d")
TODAY_BR    = date.today().strftime("%d/%m/%Y")

# ── DADOS DAS PAGINAS ─────────────────────────────────────────────────────────
PAGES = [

  # ── 1. TAXAS MERCADO LIVRE ────────────────────────────────────────────────
  {
    "slug": "taxas-mercado-livre",
    "title": "Taxas do Mercado Livre 2026: tabela completa por categoria",
    "desc": "Veja todas as taxas cobradas pelo Mercado Livre em 2026: comissao por categoria, frete, parcelamento e desconto total real por venda.",
    "tag": "Financas ML",
    "h1": "Taxas do Mercado Livre 2026: quanto voce paga em cada venda",
    "lead": "Comissao, frete, parcelamento, imposto — o Mercado Livre desconta varias taxas antes de repassar o dinheiro. Entender cada uma e o primeiro passo para saber se voce esta realmente lucrando.",
    "read_time": "6",
    "cta_title": "Veja o total descontado em cada uma das suas vendas",
    "cta_desc": "Importe o relatorio do ML e veja automaticamente quanto foi descontado em taxas, frete e impostos em cada venda do mes.",
    "content": """
<h2>Como funcionam as taxas do Mercado Livre</h2>
<p>O Mercado Livre cobra uma serie de taxas que sao descontadas diretamente do valor da venda antes do repasse. Muitos vendedores olham apenas para a comissao principal e ignoram os outros descontos — e e ai que a margem desaparece.</p>
<p>As principais taxas sao:</p>
<ul>
  <li><strong>Comissao por venda</strong> — percentual sobre o valor do produto, varia por categoria</li>
  <li><strong>Taxa de parcelamento</strong> — cobrada quando o comprador parcela em mais de 1x</li>
  <li><strong>Frete Mercado Envios</strong> — quando o vendedor oferece frete gratis, o custo e descontado</li>
  <li><strong>Taxa de anuncio</strong> — Classico (gratis) ou Premium (pago por clique)</li>
</ul>

<h2>Tabela de comissao por categoria em 2026</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Categoria</th><th>Comissao (%)</th><th>Observacao</th></tr></thead>
    <tbody>
      <tr><td>Eletronicos e tecnologia</td><td><strong>12%</strong></td><td>Celulares, notebooks, tablets</td></tr>
      <tr><td>Informatica</td><td><strong>12%</strong></td><td>Perifericos, componentes</td></tr>
      <tr><td>Moda e vestuario</td><td><strong>16%</strong></td><td>Roupas, calcados, acessorios</td></tr>
      <tr><td>Casa e decoracao</td><td><strong>13%</strong></td><td>Moveis, utensilios, organizacao</td></tr>
      <tr><td>Esportes e fitness</td><td><strong>14%</strong></td><td>Equipamentos e acessorios</td></tr>
      <tr><td>Brinquedos e jogos</td><td><strong>15%</strong></td><td>Jogos, bonecas, educational</td></tr>
      <tr><td>Beleza e saude</td><td><strong>16%</strong></td><td>Cosmeticos, higiene, suplementos</td></tr>
      <tr><td>Ferramentas</td><td><strong>13%</strong></td><td>Ferramentas manuais e eletricas</td></tr>
      <tr><td>Automotivo</td><td><strong>13%</strong></td><td>Pecas, acessorios, som automotivo</td></tr>
      <tr><td>Livros e musica</td><td><strong>10%</strong></td><td>Menor taxa da plataforma</td></tr>
    </tbody>
  </table>
</div>

<div class="callout">
  <p><strong>Importante:</strong> As taxas podem variar conforme o nivel de reputacao do vendedor, tipo de anuncio (Classico ou Premium) e promocoes sazonais do ML. Verifique sempre no painel do vendedor.</p>
</div>

<h2>Taxa de parcelamento: o desconto que pouca gente calcula</h2>
<p>Quando o comprador parcela a compra, o Mercado Livre repassa o custo financeiro para o vendedor. A logica e simples: o ML antecipa o dinheiro para voce, mas desconta o custo desse adiantamento.</p>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Parcelas</th><th>Taxa cobrada do vendedor</th></tr></thead>
    <tbody>
      <tr><td>1x (a vista)</td><td><strong>Sem taxa adicional</strong></td></tr>
      <tr><td>2x a 6x</td><td><strong>~4% a 8%</strong> sobre o valor</td></tr>
      <tr><td>7x a 12x</td><td><strong>~9% a 13%</strong> sobre o valor</td></tr>
      <tr><td>13x a 18x</td><td><strong>~14% a 18%</strong> sobre o valor</td></tr>
    </tbody>
  </table>
</div>
<p>Na pratica, uma venda de R$1.000 parcelada em 12x pode gerar um desconto adicional de R$100 a R$130 — fora a comissao da categoria.</p>

<h2>Frete Mercado Envios: quando vira desconto na sua venda</h2>
<p>O Mercado Livre incentiva fortemente o uso do Mercado Envios com frete gratis para o comprador. Quando voce ativa essa opcao, o custo do frete e descontado direto no repasse — e o valor varia bastante por peso, dimensao e regiao de entrega.</p>
<p>Um produto de 1kg enviado para outra regiao pode custar entre R$15 e R$40 de frete. Se voce vendeu por R$80 com frete gratis, ja perdeu ate 50% da receita bruta antes de considerar qualquer outro custo.</p>

<div class="callout callout-warn">
  <p><strong>Erro comum:</strong> Precificar o produto sem incluir o custo do frete na conta. Produtos leves e baratos com frete gratis frequentemente geram prejuizo sem que o vendedor perceba.</p>
</div>

<h2>A conta completa de uma venda tipica</h2>
<p>Veja como ficam os descontos em uma venda de R$200 em uma categoria com 14% de comissao, parcelada em 6x, com frete gratis:</p>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Item</th><th>Valor</th></tr></thead>
    <tbody>
      <tr><td>Valor da venda</td><td><strong>R$ 200,00</strong></td></tr>
      <tr><td>Comissao ML (14%)</td><td>- R$ 28,00</td></tr>
      <tr><td>Taxa parcelamento 6x (~6%)</td><td>- R$ 12,00</td></tr>
      <tr><td>Frete Mercado Envios</td><td>- R$ 18,00</td></tr>
      <tr><td><strong>Repasse liquido</strong></td><td><strong>R$ 142,00</strong></td></tr>
    </tbody>
  </table>
</div>
<p>De R$200 faturados, apenas R$142 chegam na sua conta — e ainda faltam descontar o custo do produto e os impostos.</p>

<h2>Como acompanhar todas as taxas sem se perder</h2>
<p>O relatorio do Mercado Livre tem todas essas informacoes, mas em formato bruto que e dificil de analisar manualmente. Cada linha de venda traz dezenas de colunas — e encontrar o total real de taxas exige cruzar varios campos.</p>
<p>A forma mais eficiente e importar o relatorio em uma ferramenta que faz esse trabalho automaticamente, mostrando receita bruta, total de taxas, CMV e lucro liquido por produto.</p>

<div class="benefit-grid">
  <div class="benefit-card">
    <div class="b-icon">$</div>
    <h4>Conciliacao automatica</h4>
    <p>Cada venda com todos os descontos calculados e separados por tipo de taxa.</p>
  </div>
  <div class="benefit-card">
    <div class="b-icon">%</div>
    <h4>Margem real por produto</h4>
    <p>Veja qual produto absorve mais taxas e ajuste a precificacao com dados reais.</p>
  </div>
  <div class="benefit-card">
    <div class="b-icon">DRE</div>
    <h4>DRE mensal automatico</h4>
    <p>Receita, custos, taxas e lucro liquido em um demonstrativo profissional.</p>
  </div>
</div>
"""
  },

  # ── 2. COMISSAO MERCADO LIVRE ─────────────────────────────────────────────
  {
    "slug": "comissao-mercado-livre",
    "title": "Comissao do Mercado Livre 2026: tabela completa por categoria",
    "desc": "Tabela atualizada com a comissao cobrada pelo Mercado Livre em cada categoria. Entenda como o percentual impacta sua margem real.",
    "tag": "Taxas e Comissoes",
    "h1": "Comissao do Mercado Livre 2026: tabela por categoria e impacto na margem",
    "lead": "A comissao e o maior custo fixo de quem vende no Mercado Livre — e ela varia significativamente por categoria. Entender esse numero e essencial para precificar certo e proteger sua margem.",
    "read_time": "5",
    "cta_title": "Veja o impacto real da comissao nas suas margens",
    "cta_desc": "Importe o relatorio do ML e descubra quanto voce pagou de comissao por produto no mes. Sem API, sem integracao — so o relatorio oficial.",
    "content": """
<h2>O que e a comissao do Mercado Livre</h2>
<p>A comissao e o percentual sobre o valor de cada venda que o Mercado Livre retém como pagamento pelo uso da plataforma. Ela cobre o acesso aos compradores, o processamento do pagamento e a infraestrutura de vendas.</p>
<p>Esse percentual nao e fixo — varia por categoria de produto, e em alguns casos tambem pelo tipo de anuncio (Classico ou Premium) e pelo nivel de reputacao do vendedor.</p>

<h2>Tabela de comissoes por categoria 2026</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Categoria</th><th>Comissao</th><th>Exemplo: venda R$500</th></tr></thead>
    <tbody>
      <tr><td>Livros, revistas e comics</td><td><strong>10%</strong></td><td>- R$ 50,00</td></tr>
      <tr><td>Eletronicos, celulares e tecnologia</td><td><strong>12%</strong></td><td>- R$ 60,00</td></tr>
      <tr><td>Informatica</td><td><strong>12%</strong></td><td>- R$ 60,00</td></tr>
      <tr><td>Ferramentas e construcao</td><td><strong>13%</strong></td><td>- R$ 65,00</td></tr>
      <tr><td>Automotivo</td><td><strong>13%</strong></td><td>- R$ 65,00</td></tr>
      <tr><td>Casa, moveis e jardim</td><td><strong>13%</strong></td><td>- R$ 65,00</td></tr>
      <tr><td>Esportes e fitness</td><td><strong>14%</strong></td><td>- R$ 70,00</td></tr>
      <tr><td>Brinquedos e games</td><td><strong>15%</strong></td><td>- R$ 75,00</td></tr>
      <tr><td>Moda, roupas e calcados</td><td><strong>16%</strong></td><td>- R$ 80,00</td></tr>
      <tr><td>Beleza, saude e cuidado pessoal</td><td><strong>16%</strong></td><td>- R$ 80,00</td></tr>
      <tr><td>Alimentos e bebidas</td><td><strong>16%</strong></td><td>- R$ 80,00</td></tr>
      <tr><td>Bebes</td><td><strong>16%</strong></td><td>- R$ 80,00</td></tr>
    </tbody>
  </table>
</div>

<div class="callout">
  <p><strong>Dica:</strong> Se voce vende em mais de uma categoria, a comissao media do seu negocio pode ser muito diferente da comissao de cada produto individualmente. Calcule sempre produto a produto.</p>
</div>

<h2>Comissao nao e o unico desconto — a conta real</h2>
<p>Muitos vendedores calculam a margem descontando apenas a comissao. Mas na pratica, o ML desconta varios outros valores antes do repasse:</p>
<ul>
  <li><strong>Taxa de parcelamento:</strong> quando o cliente compra parcelado, o custo financeiro e do vendedor</li>
  <li><strong>Frete Mercado Envios:</strong> quando o frete e gratis para o comprador, o valor e descontado da venda</li>
  <li><strong>Anuncio Premium:</strong> cobrado por clique, pode representar custo adicional significativo</li>
</ul>
<p>Somando tudo, o desconto total sobre o valor da venda pode chegar facilmente a 25% a 35% — antes de considerar o custo do produto e o imposto.</p>

<h2>Como a comissao impacta a precificacao</h2>
<p>Para que um produto seja lucrativo, o preco de venda precisa cobrir: custo do produto (CMV) + comissao + frete + imposto + margem desejada.</p>
<p>Veja a diferenca de impacto entre categorias com comissao de 12% e 16%:</p>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Cenario</th><th>Comissao 12%</th><th>Comissao 16%</th></tr></thead>
    <tbody>
      <tr><td>Venda de R$ 300</td><td>- R$ 36,00</td><td>- R$ 48,00</td></tr>
      <tr><td>Venda de R$ 1.000</td><td>- R$ 120,00</td><td>- R$ 160,00</td></tr>
      <tr><td>100 vendas de R$ 300</td><td>- R$ 3.600,00</td><td>- R$ 4.800,00</td></tr>
    </tbody>
  </table>
</div>
<p>A diferenca de 4 pontos percentuais entre categorias representa R$1.200 a menos por mês em 100 vendas de R$300. Parece pouco, mas e a diferenca entre um negocio lucrativo e um no vermelho.</p>

<h2>Classico vs Premium: qual anuncio compensa</h2>
<p>O tipo de anuncio tambem afeta o custo total:</p>
<ul>
  <li><strong>Anuncio Classico:</strong> sem custo adicional por clique, mas com menor visibilidade e limite de vendas mensais.</li>
  <li><strong>Anuncio Premium:</strong> maior visibilidade, sem limite de vendas, mas com custo adicional por clique (geralmente 1% a 2% sobre a venda).</li>
</ul>
<p>Para produtos com alto volume de vendas, o anuncio Premium costuma compensar pelo volume. Para produtos de nicho ou ticket alto, o Classico pode ser suficiente.</p>

<div class="callout callout-warn">
  <p><strong>Atencao:</strong> O Mercado Livre atualiza as taxas periodicamente. Sempre confirme os valores atuais no painel do vendedor em: Minha conta > Tarifas e comissoes.</p>
</div>
"""
  },

  # ── 3. LUCRO REAL MERCADO LIVRE ───────────────────────────────────────────
  {
    "slug": "lucro-real-mercado-livre",
    "title": "Como calcular lucro real no Mercado Livre: o guia completo",
    "desc": "Aprenda a calcular o lucro real das suas vendas no ML descontando comissao, frete, imposto e custo do produto. Pare de confundir faturamento com lucro.",
    "tag": "Gestao Financeira",
    "h1": "Como calcular lucro real no Mercado Livre: pare de confundir faturamento com lucro",
    "lead": "Faturar R$50 mil por mes nao significa lucrar R$50 mil. Depois de comissao, frete, imposto e custo do produto, o que realmente sobra pode surpreender — para o bem ou para o mal.",
    "read_time": "7",
    "cta_title": "Descubra quanto realmente sobrou no seu ML este mes",
    "cta_desc": "Importe o relatorio do Mercado Livre e veja lucro liquido, margem por produto e DRE completo em segundos. Sem planilha, sem API.",
    "content": """
<h2>Por que faturamento alto nao garante lucro</h2>
<p>Esse e um dos erros mais comuns entre vendedores do Mercado Livre: olhar para o faturamento bruto e celebrar. Mas o dinheiro que aparece no seu extrato do ML ja passou por varios descontos que a maioria das pessoas nao calcula corretamente.</p>
<p>Um vendedor que fatura R$80.000 por mes pode estar lucrando R$12.000 — ou pode estar no prejuizo de R$3.000. A diferenca esta nos detalhes da operacao.</p>

<div class="callout callout-warn">
  <p><strong>Dado importante:</strong> Segundo relatos de vendedores experientes, e comum descobrir que produtos que "vendem bem" tem margem negativa quando todos os custos sao considerados corretamente.</p>
</div>

<h2>A formula do lucro real no Mercado Livre</h2>
<p>Para calcular o lucro real de uma venda, voce precisa subtrair do valor da venda todos os custos envolvidos:</p>

<div class="callout callout-green">
  <p><strong>Lucro liquido = Receita bruta - CMV - Comissao ML - Frete - Taxa de parcelamento - Imposto - Despesas operacionais</strong></p>
</div>

<p>Veja o que significa cada componente:</p>
<ul>
  <li><strong>Receita bruta:</strong> valor total pago pelo comprador (incluindo frete quando cobrado)</li>
  <li><strong>CMV (Custo da Mercadoria Vendida):</strong> valor de compra ou producao do produto</li>
  <li><strong>Comissao ML:</strong> percentual por categoria (10% a 16%)</li>
  <li><strong>Frete:</strong> custo do Mercado Envios descontado na venda</li>
  <li><strong>Taxa de parcelamento:</strong> custo do parcelamento repassado ao vendedor</li>
  <li><strong>Imposto:</strong> Simples Nacional, Lucro Presumido ou MEI — depende do seu regime</li>
  <li><strong>Despesas operacionais:</strong> embalagem, mao de obra, plataformas, etc.</li>
</ul>

<h2>Exemplo pratico: produto que parece lucrativo mas nao e</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Item</th><th>Valor</th></tr></thead>
    <tbody>
      <tr><td>Preco de venda</td><td><strong>R$ 150,00</strong></td></tr>
      <tr><td>Custo do produto (CMV)</td><td>- R$ 65,00</td></tr>
      <tr><td>Comissao ML 14%</td><td>- R$ 21,00</td></tr>
      <tr><td>Frete Mercado Envios</td><td>- R$ 18,00</td></tr>
      <tr><td>Parcelamento 6x (~6%)</td><td>- R$ 9,00</td></tr>
      <tr><td>Imposto Simples (~6%)</td><td>- R$ 9,00</td></tr>
      <tr><td>Embalagem</td><td>- R$ 3,00</td></tr>
      <tr><td><strong>Lucro liquido</strong></td><td><strong>R$ 25,00</strong></td></tr>
      <tr><td><strong>Margem real</strong></td><td><strong>16,7%</strong></td></tr>
    </tbody>
  </table>
</div>
<p>De R$150 faturados, sobraram R$25. Se o vendedor achar que esta faturando R$150 de lucro, vai tomar decisoes completamente erradas de escala e estoque.</p>

<h2>Os 3 custos que mais destroem a margem sem que o vendedor perceba</h2>
<h3>1. Frete gratis sem calcular o custo real</h3>
<p>Oferecer frete gratis aumenta a conversao, mas o custo e integralmente descontado do seu repasse. Produtos pesados ou enviados para regioes distantes podem ter custo de frete equivalente a 20-30% do valor do produto.</p>

<h3>2. Parcelamento em muitas vezes</h3>
<p>Clientes preferem parcelar, e produtos parcelados em 12x podem ter um desconto adicional de 12% a 13% sobre o valor da venda — em cima da comissao que ja foi descontada.</p>

<h3>3. Devolucoes e cancelamentos</h3>
<p>Cada devolucao representa o custo do produto + frete de retorno sem receita correspondente. Em categorias com alta taxa de devolucao, esse impacto pode ser significativo no DRE mensal.</p>

<h2>Como monitorar o lucro real no dia a dia</h2>
<p>Fazer essa conta manualmente para cada produto e inviavel quando voce tem dezenas de SKUs e centenas de vendas por mes. O caminho mais eficiente e:</p>
<ol>
  <li>Exportar o relatorio mensal do Mercado Livre (painel > Relatorios > Vendas)</li>
  <li>Importar em uma ferramenta que calcule automaticamente todos os custos</li>
  <li>Analisar o DRE mensal e a margem por produto</li>
  <li>Identificar produtos no prejuizo e agir antes que o dano se acumule</li>
</ol>

<div class="benefit-grid">
  <div class="benefit-card">
    <div class="b-icon">$</div>
    <h4>Lucro por produto</h4>
    <p>Veja quais produtos realmente contribuem para o resultado e quais estao drenando a margem.</p>
  </div>
  <div class="benefit-card">
    <div class="b-icon">%</div>
    <h4>Margem real</h4>
    <p>Margem calculada com todos os custos — nao so a comissao do ML.</p>
  </div>
  <div class="benefit-card">
    <div class="b-icon">DRE</div>
    <h4>DRE automatico</h4>
    <p>Demonstrativo completo gerado direto do relatorio oficial do ML.</p>
  </div>
</div>
"""
  },

  # ── 4. DRE PARA MEI ──────────────────────────────────────────────────────
  {
    "slug": "dre-para-mei",
    "title": "DRE para MEI que vende no Mercado Livre: como montar",
    "desc": "Aprenda a montar um DRE simples para MEI vendedor do Mercado Livre. Entenda receita, custos e lucro liquido no seu regime tributario.",
    "tag": "Gestao Financeira · MEI",
    "h1": "DRE para MEI no Mercado Livre: como montar seu Demonstrativo de Resultados",
    "lead": "O MEI e o regime mais simples do Brasil, mas isso nao significa que o controle financeiro pode ser improvosado. Um DRE basico ajuda o microempreendedor a saber se o negocio esta saudavel — e o ML tem todos os dados necessarios.",
    "read_time": "6",
    "cta_title": "Gere o DRE do seu negocio MEI automaticamente",
    "cta_desc": "Importe o relatorio do Mercado Livre e veja seu DRE completo gerado automaticamente, com receita, custos, impostos MEI e lucro liquido.",
    "content": """
<h2>Por que o MEI precisa de DRE</h2>
<p>O DAS do MEI e simples e fixo, mas isso nao significa que o negocio e automaticamente lucrativo. Muitos microempreendedores confundem a facilidade tributaria do MEI com ausencia de necessidade de controle financeiro.</p>
<p>O DRE (Demonstrativo do Resultado do Exercicio) e o documento que mostra, de forma organizada, se o negocio gerou lucro ou prejuizo em um periodo. Para quem vende no Mercado Livre, ele e essencial para entender para onde vai o dinheiro.</p>

<div class="callout">
  <p><strong>Lembre-se:</strong> O MEI tem faturamento maximo de R$81.000 por ano (R$6.750/mes). Se voce esta proximo desse limite, planeje a transicao para ME antes de ultrapassar — as multas e o reenquadramento retroativo podem ser pesados.</p>
</div>

<h2>Estrutura do DRE para MEI vendedor do ML</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Linha</th><th>O que representa</th><th>Exemplo (R$)</th></tr></thead>
    <tbody>
      <tr><td><strong>(+) Receita Bruta</strong></td><td>Total de vendas no ML no periodo</td><td>R$ 6.200,00</td></tr>
      <tr><td>(-) Devolucoes e cancelamentos</td><td>Vendas canceladas ou produtos devolvidos</td><td>- R$ 180,00</td></tr>
      <tr><td><strong>(=) Receita Liquida</strong></td><td>Receita bruta menos devolucoes</td><td>R$ 6.020,00</td></tr>
      <tr><td>(-) CMV</td><td>Custo de compra dos produtos vendidos</td><td>- R$ 2.800,00</td></tr>
      <tr><td><strong>(=) Lucro Bruto</strong></td><td>Receita liquida menos custo dos produtos</td><td>R$ 3.220,00</td></tr>
      <tr><td>(-) Comissao ML</td><td>Taxa cobrada pelo Mercado Livre</td><td>- R$ 868,00</td></tr>
      <tr><td>(-) Frete</td><td>Custo do Mercado Envios</td><td>- R$ 420,00</td></tr>
      <tr><td>(-) DAS MEI</td><td>Contribuicao mensal fixa (comercio: ~R$71,60 em 2026)</td><td>- R$ 71,60</td></tr>
      <tr><td>(-) Despesas operacionais</td><td>Embalagem, internet, ferramentas</td><td>- R$ 150,00</td></tr>
      <tr><td><strong>(=) Lucro Liquido</strong></td><td>O que realmente sobrou</td><td>R$ 1.710,40</td></tr>
    </tbody>
  </table>
</div>

<h2>O DAS do MEI: quanto paga e como entra no DRE</h2>
<p>O MEI paga um DAS (Documento de Arrecadacao do Simples) mensal com valor fixo, independente do faturamento. Os valores para 2026 sao aproximadamente:</p>
<ul>
  <li><strong>Comercio e industria:</strong> R$ 71,60/mes</li>
  <li><strong>Servicos:</strong> R$ 75,60/mes</li>
  <li><strong>Comercio + servicos:</strong> R$ 76,60/mes</li>
</ul>
<p>Esses valores entram no DRE como despesa fixa em "impostos e contribuicoes". A vantagem do MEI e que esse custo nao cresce com o faturamento — ate o teto de R$81.000/ano.</p>

<h2>Margem de lucro saudavel para MEI no ML</h2>
<p>Nao existe uma regra unica, mas vendedores MEI no Mercado Livre costumam trabalhar com margens entre 15% e 30% de lucro liquido sobre a receita. Abaixo de 10%, o negocio fica vulneravel a qualquer variacao de custo ou queda de vendas.</p>
<p>Para calcular sua margem:</p>

<div class="callout callout-green">
  <p><strong>Margem de lucro = (Lucro liquido / Receita bruta) x 100</strong><br/>
  Exemplo: R$1.710 / R$6.200 x 100 = <strong>27,6% de margem</strong></p>
</div>

<h2>Quando o MEI precisa migrar para ME</h2>
<p>Se o faturamento ja ultrapassou R$5.000/mes consistentemente, fique atento ao teto anual de R$81.000. Ultrapassar esse limite exige a migracao para Microempresa (ME) — e quanto antes voce planejar, menos surpresas tributarias voce vai ter.</p>

<div class="callout callout-warn">
  <p><strong>Atencao:</strong> Ultrapassar o limite do MEI sem migrar pode resultar em reenquadramento retroativo, com pagamento de impostos da diferenca com multa e juros. Acompanhe seu faturamento mensalmente.</p>
</div>

<h2>Como gerar o DRE do MEI a partir do relatorio do ML</h2>
<p>O Mercado Livre gera um relatorio mensal em formato .xlsx com todas as vendas, descontos, frete e taxas detalhadas. A partir desse relatorio, e possivel montar o DRE completo sem precisar de contabilidade cara ou planilha complexa.</p>
<p>O processo manual leva horas e e sujeito a erros. Automatizar essa leitura permite ter o DRE pronto em segundos, com os dados exatos do seu negocio.</p>
"""
  },

  # ── 5. DRE SIMPLES NACIONAL ───────────────────────────────────────────────
  {
    "slug": "dre-simples-nacional",
    "title": "DRE para Simples Nacional no Mercado Livre 2026",
    "desc": "Como montar o DRE para empresas do Simples Nacional que vendem no Mercado Livre. Entenda receita, impostos e lucro liquido no seu regime.",
    "tag": "Gestao Financeira · Simples Nacional",
    "h1": "DRE para Simples Nacional no Mercado Livre: o guia pratico 2026",
    "lead": "O Simples Nacional unifica varios impostos em uma guia, mas a aliquota varia com o faturamento acumulado. Para quem vende no ML, entender como o imposto entra no DRE e fundamental para nao se surpreender com a margem real.",
    "read_time": "7",
    "cta_title": "Gere o DRE do Simples Nacional automaticamente",
    "cta_desc": "Importe o relatorio do Mercado Livre e veja receita, custos, imposto Simples e lucro liquido num DRE completo gerado em segundos.",
    "content": """
<h2>Como funciona o Simples Nacional para quem vende no ML</h2>
<p>O Simples Nacional e o regime tributario mais utilizado por pequenas empresas no Brasil. Ele unifica o pagamento de IRPJ, CSLL, PIS, COFINS, ICMS e outros tributos em uma unica guia (DAS), com aliquota que varia de acordo com o faturamento dos ultimos 12 meses.</p>
<p>Para o comercio (quem revende produtos), as aliquotas do Simples ficam no Anexo I, que varia de <strong>4% a 19%</strong> dependendo da faixa de faturamento.</p>

<h2>Tabela do Simples Nacional — Anexo I (Comercio) 2026</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Faixa de faturamento anual</th><th>Aliquota nominal</th><th>Aliquota efetiva (aprox.)</th></tr></thead>
    <tbody>
      <tr><td>Ate R$ 180.000</td><td><strong>4%</strong></td><td>~4,0%</td></tr>
      <tr><td>R$ 180.001 a R$ 360.000</td><td><strong>7,3%</strong></td><td>~5,5% a 6,5%</td></tr>
      <tr><td>R$ 360.001 a R$ 720.000</td><td><strong>9,5%</strong></td><td>~7,0% a 8,5%</td></tr>
      <tr><td>R$ 720.001 a R$ 1,8 milhao</td><td><strong>10,7%</strong></td><td>~8,5% a 10,0%</td></tr>
      <tr><td>R$ 1,8 milhao a R$ 3,6 milhoes</td><td><strong>14,3%</strong></td><td>~11,0% a 13,5%</td></tr>
      <tr><td>R$ 3,6 milhoes a R$ 4,8 milhoes</td><td><strong>19%</strong></td><td>~16,0% a 19,0%</td></tr>
    </tbody>
  </table>
</div>

<div class="callout">
  <p><strong>Aliquota efetiva vs nominal:</strong> A aliquota que voce realmente paga e a efetiva, calculada com uma formula que inclui uma deducao. Sempre calcule a efetiva — ela e menor que a nominal nas faixas iniciais.</p>
</div>

<h2>Estrutura do DRE para empresa do Simples vendendo no ML</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Linha do DRE</th><th>Exemplo (R$)</th></tr></thead>
    <tbody>
      <tr><td><strong>(+) Receita Bruta</strong></td><td>R$ 28.000,00</td></tr>
      <tr><td>(-) Devolucoes e cancelamentos</td><td>- R$ 650,00</td></tr>
      <tr><td><strong>(=) Receita Liquida</strong></td><td>R$ 27.350,00</td></tr>
      <tr><td>(-) Impostos Simples (~6,5% efetivo)</td><td>- R$ 1.820,00</td></tr>
      <tr><td>(-) Comissao ML (~14%)</td><td>- R$ 3.829,00</td></tr>
      <tr><td>(-) Frete Mercado Envios</td><td>- R$ 1.960,00</td></tr>
      <tr><td>(-) CMV</td><td>- R$ 12.600,00</td></tr>
      <tr><td><strong>(=) Lucro Bruto</strong></td><td>R$ 7.141,00</td></tr>
      <tr><td>(-) Despesas operacionais (embalagem, pessoal, etc.)</td><td>- R$ 2.200,00</td></tr>
      <tr><td><strong>(=) Lucro Liquido</strong></td><td>R$ 4.941,00</td></tr>
      <tr><td><strong>Margem liquida</strong></td><td><strong>17,6%</strong></td></tr>
    </tbody>
  </table>
</div>

<h2>O imposto Simples entra na base de calculo sobre o que?</h2>
<p>O Simples Nacional e calculado sobre a <strong>receita bruta</strong>, nao sobre o lucro. Isso e importante: mesmo que voce tenha um mes com margem baixa, o imposto continua sendo cobrado sobre tudo que vendeu.</p>
<p>Na pratica, se voce teve um mes com muitas devolucoes ou vendas no prejuizo, o Simples continua sendo cobrado sobre o faturamento total — o que pode acentuar o impacto negativo.</p>

<h2>Fator R: quando compensa optar pelo Anexo III</h2>
<p>Empresas de servicos no Simples podem optar entre o Anexo III (menores aliquotas) e o Anexo V (maiores aliquotas) com base no <strong>Fator R</strong> — a relacao entre a folha de pagamento e o faturamento dos ultimos 12 meses.</p>
<p>Se a folha de pagamento for >= 28% do faturamento, a empresa se enquadra no Anexo III, com aliquotas menores. Esse calculo precisa ser feito mensalmente.</p>

<div class="callout callout-warn">
  <p><strong>Importante:</strong> Essa informacao e de carater educacional. Para decisoes tributarias especificas do seu negocio, consulte sempre um contador.</p>
</div>

<h2>Como o ML prejudica o DRE de quem nao acompanha os descontos</h2>
<p>O grande problema de quem vende no ML pelo Simples Nacional e que a receita bruta para calculo do imposto inclui o valor total da venda — mas o repasse ja vem com os descontos do ML. Voce paga imposto sobre R$28.000, mas recebeu efetivamente menos.</p>
<p>Isso exige que o DRE seja feito com base no relatorio oficial do ML, que mostra o valor bruto de cada venda e os descontos separados, para garantir que o imposto esta sendo calculado corretamente.</p>
"""
  },

  # ── 6. DRE LUCRO PRESUMIDO ────────────────────────────────────────────────
  {
    "slug": "dre-lucro-presumido",
    "title": "DRE para Lucro Presumido no Mercado Livre: guia 2026",
    "desc": "Como montar o DRE para empresas no Lucro Presumido que vendem no Mercado Livre. Entenda IRPJ, CSLL, PIS, COFINS e o impacto na margem.",
    "tag": "Gestao Financeira · Lucro Presumido",
    "h1": "DRE para Lucro Presumido no Mercado Livre: o que muda na sua margem",
    "lead": "Empresas no Lucro Presumido tem uma carga tributaria mais complexa que o Simples — e quem vende no Mercado Livre precisa entender como IRPJ, CSLL, PIS e COFINS impactam a margem real antes de tomar qualquer decisao de escala.",
    "read_time": "8",
    "cta_title": "Veja o DRE do Lucro Presumido com seus dados reais do ML",
    "cta_desc": "Importe o relatorio do ML e calcule automaticamente receita, custos, impostos e lucro liquido no regime Lucro Presumido.",
    "content": """
<h2>O que e o Lucro Presumido</h2>
<p>O Lucro Presumido e um regime tributario intermediario entre o Simples Nacional e o Lucro Real. Nele, a Receita Federal presume que uma parcela do faturamento e lucro — e cobra IRPJ e CSLL sobre essa presuncao, independentemente do lucro real da empresa.</p>
<p>Para o comercio (revenda de mercadorias), a base de presuncao e de <strong>8% do faturamento para IRPJ</strong> e <strong>12% para CSLL</strong>. Sobre essas bases, aplicam-se as aliquotas do imposto.</p>

<h2>Impostos do Lucro Presumido: quem paga o que</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Imposto</th><th>Base de calculo (comercio)</th><th>Aliquota</th><th>Efetivo sobre faturamento</th></tr></thead>
    <tbody>
      <tr><td>IRPJ</td><td>8% do faturamento</td><td>15%</td><td>1,20%</td></tr>
      <tr><td>IRPJ adicional (acima R$60k/tri)</td><td>Lucro presumido excedente</td><td>10%</td><td>variavel</td></tr>
      <tr><td>CSLL</td><td>12% do faturamento</td><td>9%</td><td>1,08%</td></tr>
      <tr><td>PIS</td><td>Faturamento</td><td>0,65%</td><td>0,65%</td></tr>
      <tr><td>COFINS</td><td>Faturamento</td><td>3,00%</td><td>3,00%</td></tr>
      <tr><td><strong>Total base (sem adicional)</strong></td><td>—</td><td>—</td><td><strong>~5,93%</strong></td></tr>
    </tbody>
  </table>
</div>

<div class="callout">
  <p><strong>Atencao ao ICMS:</strong> No Lucro Presumido, o ICMS e pago separadamente (nao esta incluso nas guias acima). A aliquota varia por estado e produto — entre 7% e 20% sobre o valor da mercadoria na entrada. Isso pode aumentar substancialmente a carga total.</p>
</div>

<h2>DRE completo para empresa no Lucro Presumido vendendo no ML</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Linha do DRE</th><th>Exemplo (R$)</th></tr></thead>
    <tbody>
      <tr><td><strong>(+) Receita Bruta</strong></td><td>R$ 80.000,00</td></tr>
      <tr><td>(-) Devolucoes</td><td>- R$ 1.800,00</td></tr>
      <tr><td><strong>(=) Receita Liquida</strong></td><td>R$ 78.200,00</td></tr>
      <tr><td>(-) PIS (0,65%)</td><td>- R$ 520,00</td></tr>
      <tr><td>(-) COFINS (3%)</td><td>- R$ 2.400,00</td></tr>
      <tr><td>(-) IRPJ + CSLL (~2,28%)</td><td>- R$ 1.824,00</td></tr>
      <tr><td>(-) Comissao ML (~13%)</td><td>- R$ 10.166,00</td></tr>
      <tr><td>(-) Frete Mercado Envios</td><td>- R$ 5.600,00</td></tr>
      <tr><td>(-) CMV</td><td>- R$ 34.000,00</td></tr>
      <tr><td><strong>(=) Lucro Bruto</strong></td><td>R$ 23.690,00</td></tr>
      <tr><td>(-) Despesas operacionais</td><td>- R$ 6.500,00</td></tr>
      <tr><td><strong>(=) Lucro Liquido</strong></td><td>R$ 17.190,00</td></tr>
      <tr><td><strong>Margem liquida</strong></td><td><strong>21,5%</strong></td></tr>
    </tbody>
  </table>
</div>

<h2>Lucro Presumido vs Simples Nacional: quando compensa migrar</h2>
<p>Empresas que faturam acima do teto do Simples (R$4,8 milhoes/ano) sao obrigadas a migrar. Mas algumas empresas optam pelo Lucro Presumido ainda dentro do limite — especialmente quando a carga efetiva do Simples nas faixas superiores supera os ~5,93% do Lucro Presumido.</p>
<p>Para quem vende muito com margem alta, o Lucro Presumido pode ser vantajoso. Para quem tem margem baixa (tipo revenda de eletronicos com margem de 5% a 10%), o Simples geralmente e mais eficiente.</p>

<div class="callout callout-warn">
  <p><strong>Recomendacao:</strong> A decisao entre regimes tributarios deve sempre ser feita com um contador. Os numeros acima sao ilustrativos e nao consideram todas as especificidades de cada negocio e estado.</p>
</div>

<h2>Por que o DRE e ainda mais critico no Lucro Presumido</h2>
<p>No Simples, o imposto e calculado automaticamente sobre o faturamento. No Lucro Presumido, ha apuracoes trimestrais que exigem controle rigoroso das receitas. Um DRE mensal bem estruturado permite:</p>
<ul>
  <li>Prever o valor do imposto trimestral com antecedencia</li>
  <li>Identificar se o lucro presumido esta bem dimensionado para a realidade do negocio</li>
  <li>Tomar decisoes de antecipacao ou diferimento de receitas dentro do trimestre</li>
</ul>
<p>Para quem vende no Mercado Livre, ter o DRE atualizado mensalmente a partir do relatorio oficial do ML e a base para qualquer decisao financeira saudavel.</p>
"""
  },

  # ── 7. PRECIFICACAO MERCADO LIVRE ─────────────────────────────────────────
  {
    "slug": "precificacao-mercado-livre",
    "title": "Como precificar produtos no Mercado Livre sem vender no prejuizo",
    "desc": "Aprenda a calcular o preco minimo de venda no Mercado Livre considerando CMV, comissao, frete, imposto e margem desejada. Formula completa.",
    "tag": "Precificacao",
    "h1": "Como precificar no Mercado Livre: formula completa para nao vender no prejuizo",
    "lead": "Precificar errado e o erro silencioso que destroi a margem de milhares de vendedores. Antes de cadastrar qualquer preco, voce precisa calcular o minimo que garante lucro — considerando todos os custos reais da operacao no ML.",
    "read_time": "7",
    "cta_title": "Use o precificador com dados reais do seu negocio",
    "cta_desc": "O Sobrou Quanto ML tem um precificador inteligente que considera comissao, frete, imposto e CMV para calcular o preco minimo de cada produto.",
    "content": """
<h2>Por que a precificacao no ML e diferente de outros canais</h2>
<p>Vender no Mercado Livre tem custos especificos que nao existem em outros canais: comissao por venda, custo de frete repassado, taxa de parcelamento e, eventualmente, custo de anuncio Premium. Qualquer formula de precificacao generica vai gerar resultados errados.</p>
<p>A boa noticia: uma vez que voce entende os componentes, a formula e simples e pode ser aplicada em qualquer produto.</p>

<h2>A formula de precificacao para o Mercado Livre</h2>
<div class="callout callout-green">
  <p><strong>Preco minimo = CMV / (1 - comissao% - frete% - imposto% - margem_desejada%)</strong></p>
</div>

<p>Onde:</p>
<ul>
  <li><strong>CMV:</strong> custo de aquisicao ou producao do produto</li>
  <li><strong>Comissao%:</strong> percentual do ML para a categoria (10% a 16%)</li>
  <li><strong>Frete%:</strong> estimativa do custo do frete como percentual do preco de venda</li>
  <li><strong>Imposto%:</strong> aliquota efetiva do seu regime tributario</li>
  <li><strong>Margem desejada%:</strong> o lucro que voce quer ter sobre o preco de venda</li>
</ul>

<h2>Exemplo pratico: produto com CMV de R$45</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Parametro</th><th>Valor</th></tr></thead>
    <tbody>
      <tr><td>CMV (custo do produto)</td><td>R$ 45,00</td></tr>
      <tr><td>Comissao ML (categoria: 14%)</td><td>14%</td></tr>
      <tr><td>Frete estimado sobre o preco</td><td>8%</td></tr>
      <tr><td>Imposto Simples Nacional</td><td>6%</td></tr>
      <tr><td>Margem desejada</td><td>20%</td></tr>
      <tr><td><strong>Preco minimo calculado</strong></td><td><strong>R$ 86,54</strong></td></tr>
    </tbody>
  </table>
</div>
<p>Calculando: R$45 / (1 - 0,14 - 0,08 - 0,06 - 0,20) = R$45 / 0,52 = <strong>R$86,54</strong></p>
<p>Se voce precificar abaixo de R$86,54, sua margem sera menor que 20%. Se precificar abaixo de R$69 (sem a margem de 20%), voce estara vendendo no prejuizo.</p>

<h2>O maior erro de precificacao no ML: nao incluir o frete</h2>
<p>Muitos vendedores calculam apenas CMV + comissao e esquecem que, ao oferecer frete gratis, o custo do envio e descontado do repasse. Esse erro e especialmente grave em produtos leves e baratos, onde o frete pode representar 15% a 25% do valor do produto.</p>

<div class="callout callout-warn">
  <p><strong>Exemplo real:</strong> Um produto vendido por R$30 com frete gratis pode ter um custo de envio de R$12 a R$18, dependendo da regiao. Isso transforma uma venda aparentemente lucravel em prejuizo puro.</p>
</div>

<h2>Como estimar o percentual de frete para a formula</h2>
<p>O custo do frete no ML varia por peso, dimensao e regiao de entrega. Para estimar o percentual a usar na formula:</p>
<ol>
  <li>Acesse o simulador de frete do Mercado Livre (Envios > Simular frete)</li>
  <li>Calcule o custo medio de envio para as principais regioes que voce atende</li>
  <li>Divida o frete medio pelo preco medio de venda</li>
  <li>Use esse percentual como referencia na formula</li>
</ol>
<p>Para produtos com preco acima de R$150, o frete raramente passa de 10% do valor. Para produtos abaixo de R$50, pode chegar a 30% ou mais.</p>

<h2>Precificacao por regime tributario</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Regime</th><th>Aliquota a usar na formula</th></tr></thead>
    <tbody>
      <tr><td>MEI</td><td>Imposto fixo — distribuir o DAS pelo faturamento mensal</td></tr>
      <tr><td>Simples Nacional (comercio, faixa 1)</td><td>~4% a 6,5% (aliquota efetiva)</td></tr>
      <tr><td>Simples Nacional (comercio, faixa 3+)</td><td>~7% a 10%</td></tr>
      <tr><td>Lucro Presumido (comercio)</td><td>~5,93% + ICMS do estado</td></tr>
    </tbody>
  </table>
</div>

<h2>Precificacao competitiva vs precificacao lucrativa</h2>
<p>No ML, ha uma pressao constante para baixar precos e ganhar o Buy Box. Mas precificar abaixo do minimo lucravel para ganhar visibilidade e uma armadilha — voce aumenta volume mas piora (ou elimina) a margem.</p>
<p>A estrategia correta e calcular o preco minimo primeiro, e so entao decidir se o mercado comporta esse preco. Se o concorrente vende abaixo do seu custo, ele provavelmente esta no prejuizo — e nao e um modelo para seguir.</p>

<div class="benefit-grid">
  <div class="benefit-card">
    <div class="b-icon">%</div>
    <h4>Precificador por produto</h4>
    <p>Calcule o preco minimo de cada produto com CMV, comissao, frete e imposto do seu regime.</p>
  </div>
  <div class="benefit-card">
    <div class="b-icon">$</div>
    <h4>Margem real por venda</h4>
    <p>Depois de vender, veja se a margem realizada bate com o que foi planejado na precificacao.</p>
  </div>
  <div class="benefit-card">
    <div class="b-icon">!</div>
    <h4>Alerta de prejuizo</h4>
    <p>Produtos vendidos abaixo do custo real sao identificados automaticamente no relatorio.</p>
  </div>
</div>
"""
  },

  # ── 8. QUANTO O ML COBRA ──────────────────────────────────────────────────
  {
    "slug": "quanto-mercado-livre-cobra",
    "title": "Quanto o Mercado Livre Cobra por Venda em 2026: a conta completa",
    "desc": "Descubra o total descontado pelo Mercado Livre em cada venda: comissao, frete, parcelamento e taxas adicionais. Calcule o impacto no seu negocio.",
    "tag": "Taxas e Custos",
    "h1": "Quanto o Mercado Livre cobra por venda em 2026: a conta que ninguem te mostra completa",
    "lead": "Voce sabe quanto o Mercado Livre desconta antes de te pagar? A conta vai muito alem da comissao que aparece nas configuracoes do anuncio — e entender cada componente e o que separa vendedores lucrativos dos que trabalham para o ML.",
    "read_time": "6",
    "cta_title": "Veja o total exato descontado em cada uma das suas vendas",
    "cta_desc": "Importe o relatorio oficial do ML e veja automaticamente quanto foi descontado em taxas, frete e impostos em cada venda do mes.",
    "content": """
<h2>O ML cobra mais do que voce imagina</h2>
<p>A maioria dos vendedores sabe que o ML cobra comissao. Mas poucos calculam o total de todos os descontos antes do repasse. A soma pode chegar facilmente a 25% a 40% do valor da venda — e e por isso que tantos vendedores faturam bem mas nao conseguem acumular dinheiro.</p>

<h2>Todos os descontos que o Mercado Livre faz</h2>

<h3>1. Comissao por venda (10% a 16%)</h3>
<p>O principal custo. Varia por categoria e tipo de anuncio. Incide sobre o valor total da venda, incluindo frete quando cobrado do comprador.</p>

<h3>2. Taxa de parcelamento</h3>
<p>Quando o comprador parcela, o custo financeiro e repassado ao vendedor. Em parcelamentos longos, pode adicionar 10% a 13% de desconto adicional sobre o valor da venda.</p>

<h3>3. Frete Mercado Envios (quando o vendedor paga)</h3>
<p>Com frete gratis para o comprador, o valor do envio e descontado do repasse. Depende do peso, dimensao e destino do produto.</p>

<h3>4. Custo de anuncio Premium (quando ativado)</h3>
<p>O anuncio Premium garante mais visibilidade mas cobra um percentual adicional por venda (geralmente 1% a 2%). O custo aparece no extrato de repasse.</p>

<h2>Exemplo: quanto o ML fica de uma venda de R$300</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Desconto</th><th>Valor</th><th>% sobre a venda</th></tr></thead>
    <tbody>
      <tr><td>Comissao ML (14%)</td><td>R$ 42,00</td><td>14,0%</td></tr>
      <tr><td>Frete gratis (estimado)</td><td>R$ 22,00</td><td>7,3%</td></tr>
      <tr><td>Parcelamento 6x (~6%)</td><td>R$ 18,00</td><td>6,0%</td></tr>
      <tr><td>Anuncio Premium (1,5%)</td><td>R$ 4,50</td><td>1,5%</td></tr>
      <tr><td><strong>Total descontado pelo ML</strong></td><td><strong>R$ 86,50</strong></td><td><strong>28,8%</strong></td></tr>
      <tr><td><strong>Repasse ao vendedor</strong></td><td><strong>R$ 213,50</strong></td><td><strong>71,2%</strong></td></tr>
    </tbody>
  </table>
</div>
<p>De R$300 de venda, o vendedor recebe R$213,50 — e ainda precisa pagar o custo do produto e o imposto.</p>

<div class="callout callout-warn">
  <p><strong>O que muita gente nao calcula:</strong> Os R$213,50 de repasse nao sao lucro. Depois de descontar o custo do produto (suponha R$130) e o imposto (~R$18), sobram apenas R$65,50 — 21,8% de margem. E se voce nao calcular, acha que lucrou R$300.</p>
</div>

<h2>Como o repasse e calculado e quando cai na conta</h2>
<p>O Mercado Livre libera o repasse seguindo um calendario baseado na reputacao do vendedor:</p>
<ul>
  <li><strong>Reputacao Verde:</strong> repasse em ate 7 dias uteis apos confirmacao de entrega</li>
  <li><strong>Reputacao Amarela ou Laranja:</strong> ate 14 dias uteis</li>
  <li><strong>Vendedores novos:</strong> ate 21 dias uteis no inicio</li>
</ul>
<p>O prazo de repasse afeta o fluxo de caixa — especialmente para quem precisa repor estoque antes de receber pelas vendas anteriores.</p>

<h2>Por que o extrato do ML e dificil de interpretar</h2>
<p>O extrato de pagamentos do Mercado Livre mostra cada transacao individualmente, com dezenas de linhas por venda (valor da venda, comissao, frete, parcelamento, antecipacao, etc.). Sem uma ferramenta de consolidacao, e praticamente impossivel saber o total de custos e o lucro real do mes.</p>
<p>O relatorio de vendas em formato .xlsx, disponivel no painel do ML, tem todas essas informacoes em formato estruturado — mas ainda precisa ser processado para gerar um DRE legivel.</p>
"""
  },

  # ── 9. CONCILIACAO MERCADO LIVRE ──────────────────────────────────────────
  {
    "slug": "conciliacao-mercado-livre",
    "title": "Conciliacao de Vendas Mercado Livre: o guia completo 2026",
    "desc": "Aprenda o que e conciliacao de vendas no ML, como fazer e por que e essencial para saber quanto realmente entrou no seu caixa.",
    "tag": "Controle Financeiro",
    "h1": "Conciliacao de Vendas no Mercado Livre: o que e e como fazer corretamente",
    "lead": "Conciliar vendas significa confirmar que cada venda registrada no ML foi efetivamente paga, com os valores corretos descontados. Sem conciliacao, voce nunca sabe com certeza quanto entrou no seu caixa.",
    "read_time": "6",
    "cta_title": "Faca a conciliacao automatica do seu relatorio ML",
    "cta_desc": "Importe o relatorio oficial do Mercado Livre e veja cada venda conciliada com receita, comissao, frete, imposto e lucro por produto em segundos.",
    "content": """
<h2>O que e conciliacao financeira</h2>
<p>Conciliacao financeira e o processo de comparar dois registros do mesmo fato economico e confirmar que eles batem. No caso do Mercado Livre, e confirmar que cada venda no extrato de vendas corresponde a um repasse no extrato bancario, com os valores corretos.</p>
<p>Para quem vende no ML, a conciliacao tambem inclui verificar se todos os descontos (comissao, frete, parcelamento) foram aplicados corretamente em cada venda.</p>

<h2>Por que a conciliacao e critica para vendedores ML</h2>
<p>Sem conciliacao, os seguintes problemas passam despercebidos:</p>
<ul>
  <li><strong>Cobranca incorreta de comissao</strong> — raramente, mas acontece erros de categoria</li>
  <li><strong>Frete cobrado mas nao entregue</strong> — devolucoes onde o frete nao foi estornado corretamente</li>
  <li><strong>Vendas canceladas nao estornadas</strong> — caso o valor nao volte para o saldo</li>
  <li><strong>Desvio entre faturamento e receita real</strong> — quando o negocio cresce e ninguem acompanha o repasse real</li>
</ul>

<h2>Os 3 documentos para fazer a conciliacao do ML</h2>
<h3>1. Relatorio de Vendas (.xlsx)</h3>
<p>Disponivel em: Vendas > Relatorios > Vendas. Contem todas as vendas do periodo com valor bruto, comissao, frete e dados do comprador. E a base principal para a conciliacao.</p>

<h3>2. Extrato de Pagamentos do ML</h3>
<p>Disponivel em: Minha conta > Dinheiro > Extrato. Mostra todos os repasses, taxas e movimentacoes financeiras na conta do ML.</p>

<h3>3. Extrato Bancario</h3>
<p>A confirmacao final — os valores repassados pelo ML devem aparecer como creditos na conta bancaria cadastrada.</p>

<div class="callout">
  <p><strong>Dica pratica:</strong> Comece sempre pelo relatorio de vendas. Ele e mais estruturado e facil de processar do que o extrato de pagamentos, que mistura varios tipos de transacao.</p>
</div>

<h2>Passo a passo da conciliacao manual</h2>
<ol>
  <li>Exporte o relatorio de vendas do periodo (mes ou semana)</li>
  <li>Some o valor total de vendas e o total de descontos do relatorio</li>
  <li>Compare com o total de repasses no extrato do ML para o mesmo periodo</li>
  <li>Identifique diferencas — pode ser timing de repasse ou erro real</li>
  <li>Compare os repasses do ML com os creditos no extrato bancario</li>
</ol>
<p>Fazer isso manualmente para centenas de vendas leva horas por mes — e e sujeito a erros de soma e classificacao.</p>

<h2>Conciliacao automatica vs manual: o impacto no tempo</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Processo</th><th>Conciliacao manual</th><th>Conciliacao automatica</th></tr></thead>
    <tbody>
      <tr><td>Exportar relatorio</td><td>5 min</td><td>5 min</td></tr>
      <tr><td>Processar e categorizar dados</td><td>2 a 4 horas</td><td>30 segundos</td></tr>
      <tr><td>Calcular totais e margem</td><td>1 a 2 horas</td><td>Automatico</td></tr>
      <tr><td>Gerar DRE</td><td>1 a 3 horas</td><td>Automatico</td></tr>
      <tr><td><strong>Total mensal</strong></td><td><strong>4 a 9 horas</strong></td><td><strong>menos de 10 min</strong></td></tr>
    </tbody>
  </table>
</div>

<h2>O relatorio ML sem API: como funciona na pratica</h2>
<p>Algumas ferramentas de conciliacao usam a API do Mercado Livre para buscar dados automaticamente. O problema e que a API tem limitacoes de historico, pode apresentar dados inconsistentes em periodos de alta demanda e exige permissoes que muitos vendedores nao querem conceder.</p>
<p>A alternativa mais confiavel e trabalhar diretamente com o arquivo .xlsx exportado do painel do ML — esse relatorio e o mesmo que o ML usa internamente, sem filtros ou limitacoes de API. Cada numero do relatorio e exatamente o que foi processado pelo sistema do ML.</p>
"""
  },

  # ── 10. FLUXO DE CAIXA ML ─────────────────────────────────────────────────
  {
    "slug": "fluxo-de-caixa-mercado-livre",
    "title": "Fluxo de Caixa para Vendedores do Mercado Livre: guia pratico",
    "desc": "Como montar e controlar o fluxo de caixa para quem vende no Mercado Livre. Entenda entradas, saidas e como evitar falta de dinheiro no mes.",
    "tag": "Gestao Financeira",
    "h1": "Fluxo de caixa para vendedores do Mercado Livre: como nao ficar sem dinheiro",
    "lead": "Vender muito nao garante ter dinheiro disponivel quando voce precisa. O fluxo de caixa do vendedor ML tem particularidades — como o prazo de repasse — que precisam ser gerenciadas com cuidado para evitar falta de capital de giro.",
    "read_time": "6",
    "cta_title": "Controle o fluxo de caixa do seu negocio ML automaticamente",
    "cta_desc": "Importe o relatorio do Mercado Livre e veja entradas, saidas e o saldo do mes no DRE completo gerado em segundos.",
    "content": """
<h2>Por que o fluxo de caixa e diferente no Mercado Livre</h2>
<p>Quem vende em loja fisica recebe na hora. Quem vende no ML tem um prazo de repasse entre a venda e o credito na conta — que pode variar de 7 a 21 dias uteis dependendo da reputacao do vendedor.</p>
<p>Isso cria um descasamento temporal: voce ja gastou para comprar o produto e despachar o pedido, mas o dinheiro so vai chegar semanas depois. Com volume alto, esse descasamento pode travar o capital de giro.</p>

<h2>Os dois fluxos que todo vendedor ML precisa controlar</h2>
<h3>Fluxo de entradas (recebimentos)</h3>
<ul>
  <li>Repasses do Mercado Livre (por periodo de liberacao)</li>
  <li>Antecipacoes solicitadas (quando disponivel na conta ML)</li>
  <li>Eventuais vendas em outros canais</li>
</ul>

<h3>Fluxo de saidas (pagamentos)</h3>
<ul>
  <li>Compra de estoque (principal saida)</li>
  <li>Embalagens e materiais de expedicao</li>
  <li>Frete quando pago separado do repasse</li>
  <li>Imposto (DAS, Simples, Lucro Presumido)</li>
  <li>Despesas fixas (internet, ferramentas, pessoal)</li>
</ul>

<div class="callout callout-warn">
  <p><strong>Armadilha comum:</strong> Aumentar o volume de vendas rapidamente sem planejar o capital de giro para repor estoque. Voce vende mais, precisa comprar mais produto, mas o dinheiro ainda nao chegou — e fica sem estoque antes do repasse cair.</p>
</div>

<h2>Como estruturar o fluxo de caixa do vendedor ML</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Semana</th><th>Entradas previstas</th><th>Saidas previstas</th><th>Saldo projetado</th></tr></thead>
    <tbody>
      <tr><td>Semana 1</td><td>Repasses de vendas da semana -2</td><td>Compra estoque</td><td>+/-</td></tr>
      <tr><td>Semana 2</td><td>Repasses de vendas da semana -1</td><td>Imposto + fixos</td><td>+/-</td></tr>
      <tr><td>Semana 3</td><td>Repasses de vendas desta semana</td><td>Compra estoque</td><td>+/-</td></tr>
      <tr><td>Semana 4</td><td>Repasses acumulados</td><td>Fechamento do mes</td><td>+/-</td></tr>
    </tbody>
  </table>
</div>
<p>O segredo e projetar as entradas com base no historico de repasse e as saidas com base nos compromissos ja assumidos.</p>

<h2>Reserva de caixa: quanto manter para nao travar</h2>
<p>Para vendedores do ML, recomenda-se manter uma reserva minima equivalente a <strong>3 a 4 semanas de custo de estoque</strong>. Isso garante que voce consegue repor estoque enquanto espera os repasses das vendas ja realizadas.</p>
<p>Vendedores sem essa reserva ficam dependentes de antecipacao (que tem custo) ou param de vender enquanto esperam o repasse — perdendo posicao no ranking e vendas.</p>

<h2>Sazonalidade e fluxo de caixa no ML</h2>
<p>Datas como Black Friday, Natal e Dia das Maes aumentam muito o volume de vendas — mas tambem aumentam proporcionalmente as saidas de estoque e o prazo necessario de capital de giro. Planejar essas datas com antecedencia e fundamental para nao ficar sem produto no pico de demanda.</p>

<h2>Como o DRE mensal ajuda no fluxo de caixa</h2>
<p>O DRE mensal mostra lucro, mas nao necessariamente caixa disponivel — porque o lucro pode ainda estar nos repasses pendentes do ML. Para o vendedor ML, acompanhar tanto o DRE quanto o calendario de repasses e o que permite tomar decisoes de investimento e reposicao com seguranca.</p>
"""
  },

  # ── 11. MARGEM DE LUCRO ML ────────────────────────────────────────────────
  {
    "slug": "margem-de-lucro-mercado-livre",
    "title": "Margem de Lucro no Mercado Livre: qual e a ideal e como calcular",
    "desc": "Entenda o que e margem de lucro no ML, como calcular a sua e qual percentual e considerado saudavel para vendedores da plataforma.",
    "tag": "Gestao Financeira",
    "h1": "Margem de lucro no Mercado Livre: como calcular e qual e o numero saudavel",
    "lead": "Margem de lucro e o percentual que sobra para o vendedor depois de todos os custos. No Mercado Livre, onde as taxas sao altas e os precos sao comprimidos pela concorrencia, saber qual e a sua margem real e o que separa um negocio sustentavel de um que vai falir sem avisar.",
    "read_time": "5",
    "cta_title": "Descubra sua margem real por produto agora",
    "cta_desc": "Importe o relatorio do ML e veja a margem liquida de cada produto vendido no mes — com todos os custos considerados, sem achismo.",
    "content": """
<h2>Margem bruta vs margem liquida: qual monitorar</h2>
<p>Existem dois tipos principais de margem que todo vendedor do ML precisa conhecer:</p>
<ul>
  <li><strong>Margem bruta:</strong> (Receita - CMV) / Receita. Mostra quanto sobra depois de pagar o produto, antes de pagar taxas e impostos.</li>
  <li><strong>Margem liquida:</strong> (Lucro liquido) / Receita. Mostra quanto sobra depois de todos os custos — e o numero que realmente importa.</li>
</ul>
<p>Muitos vendedores acompanham apenas a margem bruta e ficam surpresos quando o lucro liquido e muito menor do que esperavam.</p>

<h2>Como calcular margem de lucro no ML</h2>
<div class="callout callout-green">
  <p><strong>Margem liquida (%) = (Receita - CMV - Comissao - Frete - Imposto - Despesas) / Receita x 100</strong></p>
</div>

<h3>Exemplo para uma venda de R$200:</h3>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Componente</th><th>Valor</th></tr></thead>
    <tbody>
      <tr><td>Receita bruta</td><td>R$ 200,00</td></tr>
      <tr><td>CMV</td><td>- R$ 85,00</td></tr>
      <tr><td>Comissao ML (14%)</td><td>- R$ 28,00</td></tr>
      <tr><td>Frete</td><td>- R$ 16,00</td></tr>
      <tr><td>Imposto Simples (~6%)</td><td>- R$ 12,00</td></tr>
      <tr><td>Embalagem</td><td>- R$ 3,00</td></tr>
      <tr><td><strong>Lucro liquido</strong></td><td><strong>R$ 56,00</strong></td></tr>
      <tr><td><strong>Margem liquida</strong></td><td><strong>28%</strong></td></tr>
    </tbody>
  </table>
</div>

<h2>Qual margem e considerada saudavel no Mercado Livre</h2>
<div class="table-wrapper">
  <table>
    <thead><tr><th>Margem liquida</th><th>Avaliacao</th></tr></thead>
    <tbody>
      <tr><td>Abaixo de 5%</td><td>Perigosa — qualquer custo extra coloca no vermelho</td></tr>
      <tr><td>5% a 10%</td><td>Baixa — viavel apenas com alto volume</td></tr>
      <tr><td>10% a 20%</td><td>Razoavel — negocio funciona, mas sem folga</td></tr>
      <tr><td>20% a 35%</td><td>Saudavel — permite reinvestir e crescer</td></tr>
      <tr><td>Acima de 35%</td><td>Excelente — produto ou nicho privilegiado</td></tr>
    </tbody>
  </table>
</div>

<div class="callout">
  <p><strong>Referencia do mercado:</strong> Vendedores experientes do ML costumam trabalhar com margem liquida entre 15% e 25% como meta. Abaixo de 10%, o negocio fica vulneravel a qualquer aumento de custo ou queda de volume.</p>
</div>

<h2>Por que a margem varia tanto entre produtos do mesmo vendedor</h2>
<p>Mesmo vendendo na mesma categoria, a margem de cada produto pode ser muito diferente por causa de:</p>
<ul>
  <li><strong>Peso e dimensao:</strong> produtos maiores tem frete mais caro relativo ao preco</li>
  <li><strong>Taxa de devolucao:</strong> produtos com mais devolucao tem margem menor no acumulado</li>
  <li><strong>Frequencia de parcelamento:</strong> produtos comprados a vista tem margem maior que parcelados</li>
  <li><strong>CMV variavel:</strong> custo de compra que muda com cada lote de estoque</li>
</ul>
<p>Monitorar a margem produto a produto e o que permite identificar quais produtos escalar e quais descontinuar.</p>

<h2>O efeito invisivel das devolucoes na margem</h2>
<p>Cada devolucao representa: custo do produto sem receita correspondente + eventual custo de frete de retorno + tempo de processamento. Em produtos com taxa de devolucao de 5% a 10%, o impacto na margem pode ser de 2 a 5 pontos percentuais.</p>
<p>Por isso, acompanhar o percentual de devolucao por produto e parte essencial da gestao de margem no ML.</p>
"""
  },

]

# ── GERADOR ───────────────────────────────────────────────────────────────────

def load_template():
    with open(TEMPLATE, encoding="utf-8") as f:
        return f.read()

def generate_page(tpl, page):
    html = tpl
    html = html.replace("{{TITLE}}", page["title"])
    html = html.replace("{{DESC}}", page["desc"])
    html = html.replace("{{SLUG}}", page["slug"])
    html = html.replace("{{TAG}}", page["tag"])
    html = html.replace("{{H1}}", page["h1"])
    html = html.replace("{{LEAD}}", page["lead"])
    html = html.replace("{{DATE_ISO}}", TODAY_ISO)
    html = html.replace("{{DATE_BR}}", TODAY_BR)
    html = html.replace("{{READ_TIME}}", page["read_time"])
    html = html.replace("{{CTA_TITLE}}", page["cta_title"])
    html = html.replace("{{CTA_DESC}}", page["cta_desc"])
    html = html.replace("{{CONTENT}}", page["content"])
    return html

def generate_sitemap_entries():
    entries = []
    for page in PAGES:
        entries.append(f"""
  <url>
    <loc>{SITE_URL}/{page['slug']}/</loc>
    <lastmod>{TODAY_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")
    return "\n".join(entries)

def main():
    tpl = load_template()
    generated = []

    for page in PAGES:
        folder = os.path.join(OUTPUT_DIR, page["slug"])
        os.makedirs(folder, exist_ok=True)
        out_path = os.path.join(folder, "index.html")
        html = generate_page(tpl, page)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        generated.append(page["slug"])
        print(f"  [OK] /{page['slug']}/index.html")

    # Atualiza sitemap.xml adicionando as novas paginas
    sitemap_path = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(sitemap_path, encoding="utf-8") as f:
        current = f.read()

    new_entries = generate_sitemap_entries()
    # Insere antes do fechamento </urlset>
    updated = current.replace("</urlset>", new_entries + "\n\n</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"\n  [OK] sitemap.xml atualizado com {len(generated)} paginas")
    print(f"\nTotal: {len(generated)} paginas geradas em public/")
    print("\nURLs geradas:")
    for slug in generated:
        print(f"  {SITE_URL}/{slug}/")

if __name__ == "__main__":
    main()
