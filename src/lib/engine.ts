import * as XLSX from 'xlsx';

export interface ProductData {
  mlb: string; sku: string; name: string; price: number;
  quantity: number; revenue: number; tax: number; fees: number;
  refund: number; cost: number; profit: number; margin: number;
}

export interface FinancialSummary {
  vendasSaudaveis: ProductData[];
  prejuizos: ProductData[];
  dadosParaAdvisor: any[];
  stats: {
    receitaBruta: number; totalCMV: number; totalImposto: number;
    impostoSomenteSaudaveis: number;
    comissaoML: number; freteVendedor: number; mercadoAds: number;
    totalReembolsos: number; lucroLiquido: number;
    perdaDevolucao: number; perdaCancelamento: number;
  };
}

// ─────────────────────────────────────────────────────────────────
// Índices padrão (relatório sem coluna "Depósito" — vendedor regular)
// Vendedores Full têm "Depósito" como col C, deslocando tudo em +1.
// buildColMap() detecta isso dinamicamente pelo cabeçalho.
// ─────────────────────────────────────────────────────────────────
const ML_COL_DEFAULT = {
  dataVenda:   1,
  estadoVenda: 2,
  unidades:    6,
  receita:     7,
  taxaVenda:  10,
  taxaEnvio:  12,
  reembolso:  15,
  publi:      18,
  sku:        19,
  mlb:        20,
  titulo:     22,
  preco:      24,
} as const;

type ColMap = typeof ML_COL_DEFAULT;

const STATUS_SAUDAVEL = [
  // Entregue / concluído
  'entregue', 'conclu', 'chegou', 'chega', 'chegar',
  // Em trânsito / envio pendente
  'caminho', 'enviar', 'enviado', 'preparando', 'trânsito', 'transit',
  // Aguardando / pronto
  'pronta', 'aprovado', 'etiqueta', 'aguardando', 'retirada',
  // ML confirmou entrega ou encerrou reclamação a favor do vendedor
  'liberamos o dinheiro', 'encerramos', 'entendemos que voc',
  'não poderá reiniciar', 'leve o pacote', 'comprador escolheu',
];
const STATUS_DEVOLUCAO = [
  'devolvid', 'devolu', 'devolvido',
  // Mediação onde comprador recebe
  'te demos o dinheiro',
  // Reclamação com reembolso ao comprador
  'reembolso para o comprador',
  // Valor parcial liberado (produto foi devolvido)
  'liberamos parte do valor',
  // ML analisando devolução
  'analisando o que aconteceu',
];
const STATUS_CANCELAMENTO = ['cancelad', 'cancelou', 'não envie'];

// Remove acentos e normaliza para comparação de cabeçalhos
export const normalizeStr = (s: any): string =>
  String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').trim();

// Linha de cabeçalho começa com "N.º de Venda" ou variante
export const isHeaderRow = (row: any[]): boolean => {
  if (!row || row.length < 3) return false;
  const first = normalizeStr(row[0]);
  return (
    first.includes('venda') ||
    first.startsWith('n.') ||
    first.includes('numero') ||
    first.includes('nº')
  );
};

// Detecta índices das colunas pelo nome do cabeçalho.
// Isso torna o parser robusto a versões do relatório com/sem "Depósito".
export const buildColMap = (headers: any[]): ColMap => {
  const idx: Partial<Record<keyof ColMap, number>> = {};

  headers.forEach((h, i) => {
    const n = normalizeStr(h);

    if (n.includes('data') && n.includes('venda')) idx.dataVenda = i;

    // Estado da venda — primeira ocorrência (col UF do comprador vem depois)
    if (!('estadoVenda' in idx) && (n === 'estado' || n === 'situacao' || n === 'status')) {
      idx.estadoVenda = i;
    }
    if (!('unidades' in idx) && n === 'unidades') idx.unidades = i;
    if (n.includes('receita') && n.includes('produto')) idx.receita = i;
    if (n.includes('tarifa') && (n.includes('venda') || n.includes('imposto'))) idx.taxaVenda = i;
    if (n.includes('tarifa') && n.includes('envio') && !n.includes('custo')) idx.taxaEnvio = i;
    if (n.includes('cancelamento') || (n.includes('reembolso') && !n.includes('custo'))) {
      idx.reembolso = i;
    }
    if (n.includes('publicidade')) idx.publi = i;
    if (n === 'sku' || (n.startsWith('sku') && n.includes('produto'))) idx.sku = i;
    // MLB: coluna "# de anúncio" — exclui variações que contenham preço, valor, unitário ou venda
    if (
      !('mlb' in idx) &&
      (n.startsWith('#') || n === 'anuncio' || n === '# de anuncio') &&
      !n.includes('titulo') && !n.includes('tipo') && !n.includes('canal') &&
      !n.includes('preco') && !n.includes('valor') && !n.includes('unitario') && !n.includes('venda')
    ) {
      idx.mlb = i;
    }
    if (n.includes('titulo') && n.includes('anuncio')) idx.titulo = i;
    if ((n.includes('preco') || n.includes('valor')) &&
        (n.includes('unitario') || n.includes('anuncio') || n.includes('venda'))) {
      idx.preco = i;
    }
  });

  return {
    dataVenda:   idx.dataVenda   ?? ML_COL_DEFAULT.dataVenda,
    estadoVenda: idx.estadoVenda ?? ML_COL_DEFAULT.estadoVenda,
    unidades:    idx.unidades    ?? ML_COL_DEFAULT.unidades,
    receita:     idx.receita     ?? ML_COL_DEFAULT.receita,
    taxaVenda:   idx.taxaVenda   ?? ML_COL_DEFAULT.taxaVenda,
    taxaEnvio:   idx.taxaEnvio   ?? ML_COL_DEFAULT.taxaEnvio,
    reembolso:   idx.reembolso   ?? ML_COL_DEFAULT.reembolso,
    publi:       idx.publi       ?? ML_COL_DEFAULT.publi,
    sku:         idx.sku         ?? ML_COL_DEFAULT.sku,
    mlb:         idx.mlb         ?? ML_COL_DEFAULT.mlb,
    titulo:      idx.titulo      ?? ML_COL_DEFAULT.titulo,
    preco:       idx.preco       ?? ML_COL_DEFAULT.preco,
  };
};

// Extrai referência de mês "YYYY-MM" de um valor de data do relatório ML.
// Suporta ISO ("2026-01-15"), BR ("15/01/2026") e serial Excel.
export const extractMonthRef = (val: any): string => {
  if (!val) return '';
  if (typeof val === 'number' && val > 40000) {
    const d = new Date(Math.round((val - 25569) * 86400 * 1000));
    return `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, '0')}`;
  }
  const s = String(val).trim();
  const iso = s.match(/^(\d{4})-(\d{2})/);
  if (iso) return `${iso[1]}-${iso[2]}`;
  const br = s.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})/);
  if (br) return `${br[3]}-${br[2].padStart(2, '0')}`;
  return '';
};

// Divide as linhas do relatório ML por mês.
// Cada grupo inclui a linha de cabeçalho para que processData funcione normalmente.
export const splitDataByMonth = (mlData: any[]): Map<string, any[]> => {
  const firstHeaderIdx = mlData.findIndex(isHeaderRow);
  if (firstHeaderIdx < 0) return new Map([['', mlData]]);

  const headerRow = mlData[firstHeaderIdx];
  const cols      = buildColMap(headerRow);
  const dataRows  = mlData.filter(row => row && row.length > 0 && !isHeaderRow(row));

  const map = new Map<string, any[]>();
  dataRows.forEach(row => {
    const ref = extractMonthRef(row[cols.dataVenda]) || 'sem-data';
    if (!map.has(ref)) map.set(ref, [headerRow]);
    map.get(ref)!.push(row);
  });

  if (map.size === 0) return new Map([['', mlData]]);
  return new Map([...map.entries()].sort(([a], [b]) => a.localeCompare(b)));
};

// ─── Detecta em qual linha está o cabeçalho ───────────────────────
const detectHeaderRow = (sheet: XLSX.WorkSheet): number => {
  const range = XLSX.utils.decode_range(sheet['!ref'] || 'A1');
  for (let R = range.s.r; R <= Math.min(range.s.r + 20, range.e.r); R++) {
    for (let C = range.s.c; C <= range.e.c; C++) {
      const cell = sheet[XLSX.utils.encode_cell({ r: R, c: C })];
      if (cell && typeof cell.v === 'string') {
        const val = cell.v.toLowerCase().trim();
        if (val.includes('n.º de venda') || val.includes('numero de venda') || val.includes('nº de venda')) {
          return R;
        }
      }
    }
  }
  for (let R = range.s.r; R <= Math.min(range.s.r + 20, range.e.r); R++) {
    let filled = 0;
    for (let C = range.s.c; C <= range.e.c; C++) {
      const cell = sheet[XLSX.utils.encode_cell({ r: R, c: C })];
      if (cell && cell.v !== null && cell.v !== '') filled++;
    }
    if (filled >= 5) return R;
  }
  return 0;
};

// ─── parseExcelFile ───────────────────────────────────────────────
// Para relatório ML (sheetName='Vendas'): retorna raw completo, com
// a linha de cabeçalho em [0]. processData detecta e usa o cabeçalho
// para mapear colunas dinamicamente.
// Para planilha de custos (skipRows=0): retorna array de objetos normalmente.
export const parseExcelFile = async (
  file: File,
  skipRows?: number,
  sheetName?: string
): Promise<any[]> => {
  const data = await file.arrayBuffer();
  const workbook = XLSX.read(data);
  const sheet = sheetName
    ? workbook.Sheets[workbook.SheetNames.find(n => n.includes(sheetName)) || workbook.SheetNames[0]]
    : workbook.Sheets[workbook.SheetNames[0]];

  const headerRow = skipRows !== undefined ? skipRows : detectHeaderRow(sheet);

  if (skipRows === 0) {
    // Retorna arrays brutos — nenhuma linha é consumida como cabeçalho.
    // processData detecta MLB/custo pelo conteúdo de cada célula.
    return XLSX.utils.sheet_to_json<any[]>(sheet, { header: 1, range: headerRow, defval: '' });
  }

  // Retorna raw incluindo cabeçalho em [0] para detecção dinâmica de colunas
  const raw = XLSX.utils.sheet_to_json<any[]>(sheet, { header: 1, range: headerRow, defval: '' });
  return raw;
};

const toNum = (v: any): number => parseFloat(String(v || '0').replace(',', '.')) || 0;
const toStr = (v: any): string => String(v || '').trim();

// ─── processData ──────────────────────────────────────────────────
export const processData = (mlData: any[], costData: any[], taxRate: number): FinancialSummary => {
  // Constrói dois mapas de custo: por MLB e por SKU.
  // Para duplicatas (mesmo MLB/SKU com custos diferentes), usa a média.
  const costByMlb = new Map<string, { sum: number; n: number }>();
  const costBySku = new Map<string, { sum: number; n: number }>();

  costData.forEach(item => {
    // Aceita tanto arrays brutos (sem cabeçalho) quanto objetos (com cabeçalho).
    // Identifica MLB/SKU e custo pelo conteúdo — robusto a qualquer estrutura.
    const values: any[] = Array.isArray(item) ? item : Object.values(item);

    let key   = '';
    let custo = 0;

    for (const val of values) {
      const s = toStr(val).trim();
      const n = toNum(val);
      if (!s || s.toUpperCase() === 'MLB' || s.toUpperCase() === 'SKU') continue;
      if (s.toUpperCase().startsWith('MLB') && s.length > 3) {
        key = s;
      } else if (!key && n === 0 && s.length > 1 && isNaN(Number(s))) {
        key = s; // SKU (texto não-numérico)
      } else if (n > 0 && custo === 0) {
        custo = n;
      }
    }

    if (!key || custo <= 0) return;

    const isMlb = key.toUpperCase().startsWith('MLB');
    const map   = isMlb ? costByMlb : costBySku;
    const prev  = map.get(key) || { sum: 0, n: 0 };
    map.set(key, { sum: prev.sum + custo, n: prev.n + 1 });
  });

  // Resolve média para duplicatas
  const resolveCost = (map: Map<string, { sum: number; n: number }>) =>
    new Map([...map.entries()].map(([k, v]) => [k, v.sum / v.n]));

  const costMap    = resolveCost(costByMlb);
  const costMapSku = resolveCost(costBySku);

  // Lookup inteligente: tenta MLB → SKU → sem custo
  const getCusto = (mlb: string, sku: string): number =>
    costMap.get(mlb) ?? costMapSku.get(sku) ?? costMap.get(sku) ?? costMapSku.get(mlb) ?? 0;

  // Detecta cabeçalho e constrói mapa de colunas dinâmico.
  // Isso garante compatibilidade com relatórios Full (coluna "Depósito") e
  // quaisquer versões futuras do relatório ML.
  const firstHeaderIdx = mlData.findIndex(isHeaderRow);
  const cols: ColMap = firstHeaderIdx >= 0
    ? buildColMap(mlData[firstHeaderIdx])
    : { ...ML_COL_DEFAULT };


  // Filtra linhas de cabeçalho (pode haver uma por arquivo ao mesclar vários meses)
  const rows = mlData.filter(row => row && row.length > 0 && !isHeaderRow(row));

  const summary: FinancialSummary = {
    vendasSaudaveis: [], prejuizos: [], dadosParaAdvisor: mlData,
    stats: {
      receitaBruta: 0, totalCMV: 0, totalImposto: 0, impostoSomenteSaudaveis: 0,
      comissaoML: 0, freteVendedor: 0, mercadoAds: 0, totalReembolsos: 0,
      lucroLiquido: 0, perdaDevolucao: 0, perdaCancelamento: 0
    }
  };

  const agrupado = new Map<string, ProductData>();

  rows.forEach((row: any[]) => {
    if (!row || row.length === 0) return;

    const estadoVenda = toStr(row[cols.estadoVenda]).toLowerCase();
    const mlb         = toStr(row[cols.mlb]);
    const titulo      = toStr(row[cols.titulo]);
    const sku         = toStr(row[cols.sku]);

    const preco     = toNum(row[cols.preco]);
    const receita   = toNum(row[cols.receita]);
    const taxaVenda = Math.abs(toNum(row[cols.taxaVenda]));
    const taxaEnvio = Math.abs(toNum(row[cols.taxaEnvio]));
    const reembolso = Math.abs(toNum(row[cols.reembolso]));

    // Unidades: usa coluna dedicada; fallback = receita ÷ preço
    const qtdCol = parseInt(toStr(row[cols.unidades])) || 0;
    const qtd    = qtdCol > 0 ? qtdCol : (preco > 0 ? Math.round(receita / preco) : 0);

    // Linhas de cobrança de publicidade (sem produto)
    if (titulo.toLowerCase().includes('publicidade') && preco <= 0) {
      summary.stats.mercadoAds += (taxaVenda + taxaEnvio);
      return;
    }

    if (!mlb || preco <= 0) return;

    const custoUnit  = getCusto(mlb, sku);
    const custoTotal = custoUnit * qtd;
    const imposto    = receita * (taxRate / 100);

    const ehDevolucao    = STATUS_DEVOLUCAO.some(s => estadoVenda.includes(s));
    const ehCancelamento = STATUS_CANCELAMENTO.some(s => estadoVenda.includes(s));
    const ehSaudavel     = !ehDevolucao && !ehCancelamento && STATUS_SAUDAVEL.some(s => estadoVenda.includes(s));

    summary.stats.receitaBruta += receita;

    if (ehSaudavel) {
      const chave = `${mlb}_${preco}`;
      if (!agrupado.has(chave)) {
        agrupado.set(chave, {
          mlb, sku, name: titulo || 'Sem Título',
          price: preco, quantity: 0, revenue: 0, tax: 0,
          fees: 0, refund: 0, cost: 0, profit: 0, margin: 0
        });
      }
      const p = agrupado.get(chave)!;
      p.quantity += qtd;
      p.revenue  += receita;
      p.tax      += imposto;
      p.fees     += (taxaVenda + taxaEnvio);
      p.refund   += reembolso;
      p.cost     += custoTotal;

      summary.stats.totalCMV      += custoTotal;
      summary.stats.totalImposto  += imposto;
      summary.stats.comissaoML    += taxaVenda;
      summary.stats.freteVendedor += taxaEnvio;

    } else if (ehDevolucao) {
      summary.stats.comissaoML        += taxaVenda;
      summary.stats.freteVendedor     += taxaEnvio;
      summary.stats.perdaDevolucao    += reembolso;
      summary.stats.totalReembolsos   += reembolso;

    } else if (ehCancelamento) {
      summary.stats.comissaoML        += taxaVenda;
      summary.stats.freteVendedor     += taxaEnvio;
      summary.stats.perdaCancelamento += reembolso;
      summary.stats.totalReembolsos   += reembolso;
    }
  });

  summary.vendasSaudaveis = Array.from(agrupado.values()).map(p => {
    const lucroLimpo = p.revenue - p.tax - p.fees - p.refund - p.cost;
    return {
      ...p,
      profit: lucroLimpo,
      margin: p.revenue > 0 ? Number(((lucroLimpo / p.revenue) * 100).toFixed(2)) : 0
    };
  });

  // Guarda imposto só das saudáveis para mostrar comparativo no UI
  summary.stats.impostoSomenteSaudaveis = summary.stats.totalImposto;

  // Base correta: receita bruta menos reembolsos de devoluções e cancelamentos
  if (taxRate > 0) {
    const baseImposto = summary.stats.receitaBruta - summary.stats.perdaDevolucao - summary.stats.perdaCancelamento;
    summary.stats.totalImposto = baseImposto * (taxRate / 100);
  }

  summary.stats.lucroLiquido =
    summary.stats.receitaBruta      -
    summary.stats.totalCMV          -
    summary.stats.totalImposto      -
    summary.stats.comissaoML        -
    summary.stats.freteVendedor     -
    summary.stats.mercadoAds        -
    summary.stats.perdaDevolucao    -
    summary.stats.perdaCancelamento;

  return summary;
};
