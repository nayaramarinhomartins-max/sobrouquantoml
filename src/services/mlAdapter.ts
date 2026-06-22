// src/services/mlAdapter.ts

export const normalizeMLData = (dadosBrutos: any[]) => {
  if (!dadosBrutos || !Array.isArray(dadosBrutos)) return [];

  return dadosBrutos.map((row) => {
    const parseNumber = (val: any) => {
      if (val === undefined || val === null || val === "") return 0;
      if (typeof val === 'number') return val;
      const clean = String(val).replace('R$', '').replace(/\./g, '').replace(',', '.').trim();
      return parseFloat(clean) || 0;
    };

    const parseBool = (val: any) => {
      const v = String(val).toLowerCase();
      return v === 'sim' || v === 'si'; // 'si' caso venha de conta em espanhol
    };

    return {
      // --- BLOCO VENDAS (A a S) ---
      idVenda:            row["NUMERO DA VENDA"],               // A
      dataVenda:          row["DATA DA VENDA"],                 // B
      deposito:           row["DEPOSITO"],                      // C (Importante: Matriz vs Full)
      statusVenda:        row["ESTADO"],                        // D
      statusDetalhe:      row["DESCRIÇÃO DO STATUS"],           // E
      isKit:              parseBool(row["PERTENCE A UM KIT"]),   // G
      unidades:           parseNumber(row["UNIDADES"]),         // H
      receitaProduto:     parseNumber(row["RECEITA POR PRODUTO"]), // I
      comissaoML:         parseNumber(row["TARIFA DE VENDAS E IMPOSTO"]), // M
      custoFrete:         parseNumber(row["TARIFA DE ENVIO"]),   // N
      freteDeclarado:     parseNumber(row["CUSTO DE ENVIO COM BASE NAS MEDIDAS E PESO DECLARADO"]), // O
      freteDivergente:    parseNumber(row["CUSTO POR DIFERENÇAS NAS MEDIDAS E NO PESO DO PACOTE"]), // P (ALERTA!)
      totalVenda:         parseNumber(row["TOTAL DA VENDA"]),    // R
      mesFaturamento:     row["MES DE FATURAMENTO DA TARIFA"],  // S

      // --- BLOCO PUBLICIDADE (T) ---
      isAds:              parseBool(row["VENDA POR PUBLICIDADE"]), // T

      // --- BLOCO ANÚNCIOS (U a Z) ---
      sku:                row["SKU DO PRODUTO"],                // U
      mlb:                row["# DE ANUNCIO"],                  // V
      tituloAnuncio:      row["TITULO DO ANUNCIO"],             // W
      variacao:           row["VARIAÇÃO"],                      // X
      tipoAnuncio:        row["TIPO DE ANUNCIO"],               // Z (Premium/Clássico)

      // --- BLOCO FATURAMENTO (AA a AF) ---
      notaFiscal:         row["NF EMITIDA"],                    // AA
      documentoCliente:   row["DOCUMENTO DO CLIENTE"],          // AC
      tipoContribuinte:   row["TIPO DE CONTRIBUINTE"],          // AE (PJ vs PF)

      // --- BLOCO COMPRADORES / CRM (AG a AN) ---
      nomeComprador:      row["NOME DO COMPRADOR"],             // AG
      isBusiness:         parseBool(row["É NEGOCIO?"]),         // AH
      cpfComprador:       row["CPF SO COMPRADOR"] || row["CPF DO COMPRADOR"], // AI (CHAVE CRM)
      cidade:             row["CIDADE"],                        // AK
      estadoUF:           row["ESTADO (COMPRADOR)"] || row["AL"], // AL
      cep:                row["CEP"],                           // AM

      // --- BLOCO ENVIOS / RASTREIO (AO a AT) ---
      formaEntrega:       row["FORMA DE ENTREGA"],              // AO
      dataEntrega:        row["DATA DE ENTREGA"],               // AQ
      codigoRastreio:     row["NUMERO DO RASTREIO"],            // AS
      urlRastreio:        row["URL DO ACOMPANHAMENTO"],         // AT

      // --- BLOCO DEVOLUÇÕES (AU a BG) ---
      dinheiroLiberado:   parseBool(row["DINHEIRO LIBERADO"]),  // BD
      resultadoDevolucao: row["RESULTADO"],                     // BE (Reestoque?)
      motivoResultado:    row["MOTIVO DO RESULTADO"],           // BG

      // --- BLOCO RECLAMAÇÕES (BH a BK) ---
      reclamacoesAbertas: parseNumber(row["RECLAMAÇÕES ABERTAS"]), // BI
      reclamacoesFechadas: parseNumber(row["RECLAMAÇÕES ENCERRADA"]), // BJ
      isMediacao:         parseBool(row["EM MEDIAÇÃO"]),        // BK (ALERTA REPUTAÇÃO)

      // CAMPO CALCULADO: Margem de Contribuição Inicial
      // (Total que sobrou após comissão e frete)
      margemContribuicao: parseNumber(row["TOTAL DA VENDA"]) - parseNumber(row["TARIFA DE ENVIO"])
    };
  });
};