export const MLSalesLibrary = {
  // 1. MAPEAMENTO DINÂMICO DE COLUNAS (Onde a Engine deve olhar)
  columns: {
    identification: ["n.º de venda", "data da venda", "# de anúncio", "sku", "título do anúncio"],
    status: ["estado", "descrição do status"],
    financial: {
      revenue: ["receita por produtos", "receita por acréscimo no preço"],
      fees: ["tarifa de venda e impostos", "taxa de parcelamento"],
      shipping: ["receita por envio", "tarifas de envio", "custo de envio declarado"],
      penalties: ["custo por diferenças nas medidas e no peso do pacote"],
      adjustments: ["cancelamentos e reembolsos", "total"]
    },
    logistics: ["forma de entrega", "depósito", "pacote de diversos produtos", "pertence a um kit"],
    returns: ["revisado pelo mercado livre", "dinheiro liberado", "resultado", "destino", "motivo do resultado"],
    customer: ["comprador", "negócio", "cpf", "cidade", "estado", "país"],
    fiscal: ["nf-e em anexo"]
  },

  // 2. DICIONÁRIO COMPLETO DE STATUS (Sem excluir nada)
  statusDictionary: {
    VALID_REVENUE: [
      "entregue", "venda entregue", "venda concretizada", "a caminho", 
      "processando no centro de distribuição", "etiqueta pronta para imprimir", 
      "etiqueta impressa", "para enviar no dia", "vamos enviar o pacote no dia",
      "envio atrasado", "no ponto de retirada", "chegou em", "o pacote chegou",
      "te demos o dinheiro desta venda", "creditamos o valor na sua conta",
      "logo poderá imprimir a etiqueta", "chega entre os dias", "chega hoje",
      "o comprador escolheu um envio padrão", "entendemos que você recebeu conforme o esperado"
    ],
    ZERO_REVENUE: [
      "cancelada pelo comprador", "cancelada pelo mercado livre", 
      "venda cancelada. não envie.", "pacote cancelado pelo mercado livre", 
      "cancelada", "reembolsamos o dinheiro", "não podia esperar", 
      "arrependeu da compra", "não há estoque"
    ],
    LOGISTICS_REVERSA: [
      "devolução em preparação", "devolução em preparação sem custo de envio",
      "devolução a caminho", "devolvido no dia", "devolução finalizada", 
      "devolução reagendada", "devolução com data atualizada", 
      "devolução com revisão inicial", "devolução para revisar",
      "retornará para você", "produto retornou", "entrega recusada", 
      "endereço incorreto", "não foi possível entregá-lo", 
      "vamos te devolver um pacote", "em devolução"
    ],
    AUDIT_REQUIRED: [
      "reclamação aberta", "reclamação encerrada", "mediação com devolução habilitada",
      "mediação finalizada", "reclamação esperando resposta", 
      "venda com solicitação de alteração"
    ]
  },

  // 3. MATRIZ DE DETALHES DE DEVOLUÇÃO (BG, BE, BD)
  returnAuditory: {
    condition: ["apto para venda", "não apto para venda"],
    destination: ["vendedor", "mercado livre"],
    reasons: [
      "está em boas condições", "não corresponde ao produto enviado", 
      "a caixa original está danificada", "apresenta irregularidades", 
      "tem características diferentes daquele que foi enviado"
    ],
    payout: ["do comprador", "do vendedor"]
  },

  // 4. FISCAL E ADVERTISING
  fiscalStatus: ["não emitida", "autorizado", "inutilizada", "cancelada"],
  advertising: {
    header: "venda por publicidade",
    values: ["sim", "não"]
  }
};