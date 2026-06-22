/**
 * BIBLIOTECA MESTRA DE PUBLICIDADE (ADS) - ROBOT PLACE
 * Localização: src/core/ml-ads-library.ts
 * Finalidade: Mapeamento integral do Relatório de Anúncios Patrocinados.
 */

export const MLAdsLibrary = {
  // CONFIGURAÇÃO DE NAVEGAÇÃO DO EXCEL
  excelConfig: {
    targetSheetName: "Relatório Anúncios Patrocinados", // ABA OBRIGATÓRIA
    headerRow: 1, // Linha onde se encontram os cabeçalhos
  },

  // MAPEAMENTO COMPLETO DE COLUNAS (A até T) - SEM FILTROS
  columns: {
    // [A-B] TEMPO
    timeframe: {
      start: "Desde",
      end: "Até"
    },
    // [C-F] IDENTIFICAÇÃO E STATUS
    identification: {
      campaign: "Campanha",
      adTitle: "Título do anúncio patrocinado",
      adCode: "Código do anúncio", // MLB de cruzamento
      status: "Status"
    },
    // [G-K] DADOS CONCRETOS DE PERFORMANCE (CIÊNCIA)
    performance: {
      impressions: "Impressões",
      clicks: "Cliques",
      cpc: "CPC (Custo por clique)",
      ctr: "CTR (Click Through Rate)",
      cvr: "CVR (Conversion rate)"
    },
    // [L-O] MÉTRICAS FINANCEIRAS DE EFICIÊNCIA
    efficiency: {
      revenueLocal: "Receita(Moeda local)",
      investmentLocal: "Investimento(Moeda local)",
      acos: "ACOS(Investimento / Receitas)",
      roas: "ROAS(Receitas / Investimento)"
    },
    // [P-T] DETALHAMENTO DE VENDAS (DIRETAS E INDIRETAS)
    salesDetail: {
      directSales: "Vendas diretas",
      indirectSales: "Vendas indiretas",
      totalAdsSales: "Vendas por publicidade (Diretas + Indiretas)",
      directRevenue: "Receita por vendas diretas (Moeda Local)",
      indirectRevenue: "Receita por vendas indiretas"
    }
  },

  // DICIONÁRIO DE STATUS (Monitoramento total do estado da campanha)
  statusDictionary: [
    "Ativa",
    "Pausada",
    "Finalizada",
    "Sem orçamento",
    "Pendente de revisão",
    "Interrompida"
  ],

  // REGRAS DE INTEGRAÇÃO COM O RELATÓRIO DE VENDAS
  integrationRules: {
    syncKey: "Código do anúncio", // Deve bater com "N.º de anúncio" ou "MLB"
    attributionModel: "Direta + Indireta", // Considera o impacto total do Ads
    impactAnalysis: [
      "Vendas diretas", 
      "Vendas indiretas", 
      "Receita por vendas indiretas"
    ]
  }
};