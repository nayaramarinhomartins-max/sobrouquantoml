import React, { useMemo, useState } from 'react';
import {
  Users, Zap, AlertTriangle, RefreshCcw, XCircle,
  Calendar, Award, TrendingUp, ShoppingBag, MapPin,
  PackageX, Scale, Target, BarChart2, DollarSign, Percent
} from 'lucide-react';
import { MLSalesLibrary } from '../core/ml-sales-library';
import { normalizeStr, isHeaderRow } from '../lib/engine';

// ─────────────────────────────────────────────────────────────────
// ÍNDICES DO RELATÓRIO ML (array de arrays — mesma lógica do engine)
// ─────────────────────────────────────────────────────────────────
const COL = {
  estadoVenda:   2,   // Status resumido da venda (único por linha)
  descricao:     3,   // Descrição detalhada do status
  dataVenda:     1,   // Data da venda
  unidades:      6,
  receita:       7,   // Receita bruta por produto (BRL) ← usar para faturamento
  taxaVenda:    10,   // Comissão ML (BRL)
  taxaEnvio:    12,   // Frete cobrado pelo ML (BRL)
  erroFrete:    14,   // Custo por divergência de peso/medida (BRL)
  reembolso:    15,   // Cancelamentos e reembolsos (BRL)
  total:        16,   // Valor líquido depositado pelo ML (≠ lucro, ≠ receita bruta)
  publi:        18,   // "Sim" = venda por publicidade
  sku:          19,
  mlb:          20,
  titulo:       22,
  preco:        24,
  tipoAnuncio:  25,   // "Clássico" / "Premium"
  cpf:          33,   // CPF (11 dígitos) ou CNPJ (14 dígitos)
  cidade:       35,
  uf:           36,   // UF do comprador (coluna "Estado" do comprador)
  comprador:    32,   // Nome do comprador
  dataRetorno:  40,   // Data a caminho — logística reversa (quando saiu de volta)
  rastreio:     43,   // Código de rastreio da devolução
  revisadoML:   52,   // Revisado pelo Mercado Livre (Sim/Não)
  dinheiroLib:  54,   // Dinheiro liberado ao vendedor
  resultado:    55,   // Resultado da revisão (apto/não apto para venda)
  destino:      56,   // Destino do produto (vendedor/ML)
  motivoResult: 57,   // Motivo do resultado
} as const;

// ─────────────────────────────────────────────────────────────────
// DETECÇÃO DINÂMICA DE COLUNAS — lê o cabeçalho do relatório ML
// e retorna índices corretos para Full e não-Full sellers
// ─────────────────────────────────────────────────────────────────
type AdvisorCols = typeof COL;

function detectAdvisorCols(rawData: any[]): AdvisorCols {
  const hIdx = rawData.findIndex(isHeaderRow);
  if (hIdx < 0) return COL;

  const h = rawData[hIdx];
  const map: Partial<AdvisorCols> = {};

  h.forEach((cell: any, i: number) => {
    const n = normalizeStr(cell);
    if (!n) return;

    // publicidade / ads
    if (n.includes('publicidade') && n.includes('venda')) map.publi = i;
    // SKU
    if (n === 'sku' || (n.startsWith('sku') && n.includes('produto'))) map.sku = i;
    // MLB (# de anúncio)
    if ((n.startsWith('#') || (n.includes('anuncio') && !n.includes('titulo') && !n.includes('tipo') && !n.includes('canal')))) map.mlb = i;
    // título do anúncio
    if (n.includes('titulo') && n.includes('anuncio')) map.titulo = i;
    // preço unitário
    if ((n.includes('preco') || n.includes('valor')) && (n.includes('unitario') || n.includes('anuncio') || n.includes('venda'))) map.preco = i;
    // tipo de anúncio (Clássico/Premium)
    if (n.includes('tipo') && n.includes('anuncio')) map.tipoAnuncio = i;
    // CPF/CNPJ
    if ((n === 'cpf' || n.includes('cpf')) && i > 25) map.cpf = i;
    // cidade do comprador
    if (n === 'cidade' && i > 25) map.cidade = i;
    // UF/estado do comprador (não o estado da venda que fica no início)
    if (n === 'estado' && i > 25) map.uf = i;
    // comprador
    if (n === 'comprador' && i > 25) map.comprador = i;
    // data de retorno (logística reversa)
    if (n.includes('data') && n.includes('caminho') && i > 25) map.dataRetorno = i;
    // rastreamento
    if (n.includes('rastreamento') && i > 25) map.rastreio = i;
    // revisado ML
    if (n.includes('revisado') && n.includes('mercado')) map.revisadoML = i;
    // dinheiro liberado
    if (n.includes('dinheiro') && n.includes('liberado')) map.dinheiroLib = i;
    // resultado
    if (n === 'resultado' && i > 40) map.resultado = i;
    // destino
    if (n === 'destino' && i > 40) map.destino = i;
    // motivo do resultado
    if (n.includes('motivo') && n.includes('resultado')) map.motivoResult = i;
    // cancelamentos/reembolsos
    if (n.includes('cancelamento') || (n.includes('reembolso') && !n.includes('custo'))) map.reembolso = i;
    // receita por produtos
    if (n.includes('receita') && n.includes('produto')) map.receita = i;
    // tarifa de venda
    if ((n.includes('tarifa') || n.includes('imposto')) && n.includes('venda')) map.taxaVenda = i;
    // tarifas de envio
    if (n.includes('tarifa') && n.includes('envio')) map.taxaEnvio = i;
    // custo por diferenças de peso
    if (n.includes('diferenca') && (n.includes('medida') || n.includes('peso'))) map.erroFrete = i;
    // data da venda
    if (n.includes('data') && n.includes('venda')) map.dataVenda = i;
    // estado da venda (status) — coluna curta no início
    if ((n === 'estado' || n === 'situacao' || n === 'status') && i < 10) map.estadoVenda = i;
    // descrição do status
    if ((n.includes('descricao') || n.includes('descr')) && n.includes('status') && i < 10) map.descricao = i;
    // unidades
    if (n === 'unidades' && i < 12) map.unidades = i;
  });

  return { ...COL, ...map };
}

// ─────────────────────────────────────────────────────────────────
// STATUS — usando a ml-sales-library como fonte da verdade
// ─────────────────────────────────────────────────────────────────
const STATUS_DEVOLUCAO  = [
  ...MLSalesLibrary.statusDictionary.LOGISTICS_REVERSA.map(s => s.toLowerCase()),
  // Variações reais do relatório ML não cobertas pela library
  'devolvida pelo comprador',
  'devolvida pelo vendedor',
  'devolvida',
];
const STATUS_CANCELAMENTO = MLSalesLibrary.statusDictionary.ZERO_REVENUE.map(s => s.toLowerCase());
const STATUS_AUDITORIA  = MLSalesLibrary.statusDictionary.AUDIT_REQUIRED.map(s => s.toLowerCase());

const isDevolucao    = (estado: string) => STATUS_DEVOLUCAO.some(s => estado.includes(s));
const isCancelamento = (estado: string) => STATUS_CANCELAMENTO.some(s => estado.includes(s));
const isAuditoria    = (estado: string) => STATUS_AUDITORIA.some(s => estado.includes(s));

// ─── helpers ──────────────────────────────────────────────────────
const toNum = (v: any) => parseFloat(String(v || '0').replace(',', '.')) || 0;
const toStr = (v: any) => String(v || '').trim();
const fmt   = (v: number) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v);
const fmtPct = (v: number) => `${v.toFixed(1)}%`;

// ─── tipos internos ───────────────────────────────────────────────
interface AnuncioStats { vendas: number; receitaBruta: number; comissao: number; frete: number; }
interface SkuDev       { sku: string; titulo: string; total: number; }
interface CpfInfo      { compras: number; receitaTotal: number; isCnpj: boolean; }

// Detalhe individual de cada devolução (bloco expandido)
interface DevolucaoDetalhe {
  idVenda:      string;
  sku:          string;
  mlb:          string;
  titulo:       string;
  comprador:    string;
  cidade:       string;
  uf:           string;
  rastreio:     string;
  dataVenda:    string;
  dataRetorno:  string;
  diasCiclo:    number | null;
  receita:      number;
  reembolso:    number;  // pago ao comprador
  frete:        number;  // custo do frete no período
  prejuizo:     number;  // receita − reembolso + frete = o que o vendedor perdeu
  revisadoML:   string;
  resultado:    string;
  destino:      string;
  motivo:       string;
}

// ─────────────────────────────────────────────────────────────────
// COMPONENTE
// ─────────────────────────────────────────────────────────────────
export function Advisor({ data }: { data: any[] }) {

  const analysis = useMemo(() => {
    if (!data || !Array.isArray(data) || data.length === 0) return null;

    // Detecta colunas dinamicamente (suporta Full e não-Full sellers)
    const COLS = detectAdvisorCols(data);
    // Filtra linhas de cabeçalho — agora que data = mlData bruto
    const dataRows = data.filter(row => row && row.length > 5 && !isHeaderRow(row));

    const stats = {
      totalLinhas: 0,

      // Fidelidade — separada B2C (CPF) e B2B (CNPJ)
      clientes: new Map<string, CpfInfo>(),

      // Anúncios — usando receita bruta (col 7), não total (col 16)
      anuncios: {
        premium:  { vendas: 0, receitaBruta: 0, comissao: 0, frete: 0 } as AnuncioStats,
        classico: { vendas: 0, receitaBruta: 0, comissao: 0, frete: 0 } as AnuncioStats,
      },

      // Frete divergente — acumula valor total, não só contagem
      freteDivergente: {
        porSku:    new Map<string, { titulo: string; valor: number; ocorrencias: number }>(),
        totalPerdido: 0,
      },

      // Devoluções — usando status da ml-sales-library
      devolucoes: {
        total: 0,
        fretePerdido: 0,
        prejuizoTotal: 0,
        porSku: new Map<string, { titulo: string; total: number; receitaPerdida: number; prejuizo: number }>(),
        detalhes: [] as DevolucaoDetalhe[],
      },

      // Cancelamentos — corrigido: detecta "cancelada ANTES de enviar" vs "cancelada em trânsito"
      cancelamentos: {
        total: 0,
        emTransito: 0,   // Cancelados após envio (risco de perda de mercadoria)
        receitaPerdida: 0,
      },

      // Reclamações / Auditoria — usando ml-sales-library completa
      reclamacoes: {
        total: 0,
        porMlb: new Map<string, { titulo: string; total: number }>(),
      },

      // Ads — usando receita bruta (col 7) para valor correto
      ads: {
        qtd: 0,
        receitaBruta: 0,
        comissaoTotal: 0,
        freteTotal: 0,
        porMlb: new Map<string, { titulo: string; receita: number; comissao: number }>(),
      },

      // Geo
      cidades: new Map<string, number>(),
      ufs:     new Map<string, number>(),

      // Dias da semana (0=Dom … 6=Sáb)
      diasSemana: [0, 0, 0, 0, 0, 0, 0] as number[],
    };

    dataRows.forEach((row: any[]) => {
      if (!row || row.length < 10) return;
      stats.totalLinhas++;

      const estadoRaw   = toStr(row[COLS.estadoVenda]).toLowerCase();
      const descricao   = toStr(row[COLS.descricao]).toLowerCase();
      const receita     = toNum(row[COLS.receita]);
      const taxaVenda   = Math.abs(toNum(row[COLS.taxaVenda]));
      const taxaEnvio   = Math.abs(toNum(row[COLS.taxaEnvio]));
      const erroFrete   = Math.abs(toNum(row[COLS.erroFrete]));
      const sku         = toStr(row[COLS.sku]) || 'Sem SKU';
      const mlb         = toStr(row[COLS.mlb]) || 'S/ MLB';
      const titulo      = toStr(row[COLS.titulo]);
      const cpfRaw      = toStr(row[COLS.cpf]).replace(/\D/g, '');
      const cidade      = toStr(row[COLS.cidade]);
      const uf          = toStr(row[COLS.uf]);
      const tipoAnuncio = toStr(row[COLS.tipoAnuncio]).toLowerCase();
      const isAds       = toStr(row[COLS.publi]).toLowerCase() === 'sim';
      const dataVenda   = toStr(row[COLS.dataVenda]);

      // ── 1. Fidelidade (B2C + B2B)
      if (cpfRaw.length >= 11) {
        const isCnpj = cpfRaw.length === 14;
        const info   = stats.clientes.get(cpfRaw) || { compras: 0, receitaTotal: 0, isCnpj };
        info.compras++;
        info.receitaTotal += receita;
        stats.clientes.set(cpfRaw, info);
      }

      // ── 2. Performance de Anúncio (receita bruta, não total)
      const anuncio = tipoAnuncio.includes('premium') ? stats.anuncios.premium : stats.anuncios.classico;
      anuncio.vendas++;
      anuncio.receitaBruta += receita;
      anuncio.comissao     += taxaVenda;
      anuncio.frete        += taxaEnvio;

      // ── 3. Frete divergente (valor total acumulado)
      if (erroFrete > 0) {
        const entry = stats.freteDivergente.porSku.get(sku) || { titulo, valor: 0, ocorrencias: 0 };
        entry.valor       += erroFrete;
        entry.ocorrencias++;
        stats.freteDivergente.porSku.set(sku, entry);
        stats.freteDivergente.totalPerdido += erroFrete;
      }

      // ── 4. Devoluções (usando ml-sales-library completa)
      if (isDevolucao(estadoRaw) || isDevolucao(descricao)) {
        const reembolso    = Math.abs(toNum(row[COLS.reembolso]));
        const prejuizo     = receita - reembolso + taxaEnvio; // quanto o vendedor perdeu

        stats.devolucoes.total++;
        stats.devolucoes.fretePerdido  += taxaEnvio;
        stats.devolucoes.prejuizoTotal += prejuizo;

        // porSku — ranking resumido
        const entrySku = stats.devolucoes.porSku.get(sku) || { titulo, total: 0, receitaPerdida: 0, prejuizo: 0 };
        entrySku.total++;
        entrySku.receitaPerdida += receita;
        entrySku.prejuizo       += prejuizo;
        stats.devolucoes.porSku.set(sku, entrySku);

        // Detalhe individual — para a tabela expandida
        const dataRetornoStr = toStr(row[COLS.dataRetorno]);
        let diasCiclo: number | null = null;
        try {
          const MESES_PT2 = ['janeiro','fevereiro','março','abril','maio','junho',
                             'julho','agosto','setembro','outubro','novembro','dezembro'];
          const parseD = (s: string) => {
            const m2 = s.match(/(\d{1,2})\s+de\s+([^\s]+)\s+de\s+(\d{4})/i);
            if (!m2) return null;
            const mi = MESES_PT2.indexOf(m2[2].toLowerCase());
            return mi !== -1 ? new Date(Number(m2[3]), mi, Number(m2[1])) : null;
          };
          const dv = parseD(dataVenda);
          const dr = parseD(dataRetornoStr);
          if (dv && dr && !isNaN(dv.getTime()) && !isNaN(dr.getTime())) {
            const diff = Math.round((dr.getTime() - dv.getTime()) / 86_400_000);
            if (diff > 0) diasCiclo = diff; // 0 = dado sintético/igual, ignora
          }
        } catch (_) {}

        stats.devolucoes.detalhes.push({
          idVenda:     toStr(row[0]),
          sku,
          mlb,
          titulo,
          comprador:   toStr(row[COLS.comprador]),
          cidade,
          uf,
          rastreio:    toStr(row[COLS.rastreio]),
          dataVenda,
          dataRetorno: dataRetornoStr,
          diasCiclo,
          receita,
          reembolso,
          frete:       taxaEnvio,
          prejuizo,
          revisadoML:  toStr(row[COLS.revisadoML]),
          resultado:   toStr(row[COLS.resultado]),
          destino:     toStr(row[COLS.destino]),
          motivo:      toStr(row[COLS.motivoResult]),
        });
      }

      // ── 5. Cancelamentos — CORRIGIDO
      // "em trânsito" = descricao menciona envio/caminho mas estado é cancelado
      if (isCancelamento(estadoRaw) || isCancelamento(descricao)) {
        stats.cancelamentos.total++;
        stats.cancelamentos.receitaPerdida += receita;
        const descLower = descricao + ' ' + estadoRaw;
        const foiEnviado =
          descLower.includes('caminho') ||
          descLower.includes('trânsito') ||
          descLower.includes('transit') ||
          descLower.includes('enviado') ||
          descLower.includes('saiu para');
        if (foiEnviado) stats.cancelamentos.emTransito++;
      }

      // ── 6. Reclamações / Auditoria (ml-sales-library completa)
      if (isAuditoria(estadoRaw) || isAuditoria(descricao)) {
        stats.reclamacoes.total++;
        const entry = stats.reclamacoes.porMlb.get(mlb) || { titulo, total: 0 };
        entry.total++;
        stats.reclamacoes.porMlb.set(mlb, entry);
      }

      // ── 7. Ads (receita bruta, + ACoS por MLB)
      if (isAds) {
        stats.ads.qtd++;
        stats.ads.receitaBruta  += receita;
        stats.ads.comissaoTotal += taxaVenda;
        stats.ads.freteTotal    += taxaEnvio;
        const entry = stats.ads.porMlb.get(mlb) || { titulo, receita: 0, comissao: 0 };
        entry.receita  += receita;
        entry.comissao += taxaVenda;
        stats.ads.porMlb.set(mlb, entry);
      }

      // ── 8. Geo
      if (cidade && cidade.toLowerCase() !== 'null' && cidade.length > 2) {
        stats.cidades.set(cidade, (stats.cidades.get(cidade) || 0) + 1);
      }
      // UF pode vir como sigla ("SP") ou nome por extenso ("São Paulo")
      if (uf && uf.toLowerCase() !== 'null' && uf.length > 1) {
        stats.ufs.set(uf, (stats.ufs.get(uf) || 0) + 1);
      }

      // ── 9. Dias da semana
      // Formatos suportados:
      //   "9 de fevereiro de 2026 00:00 hs."  ← padrão do relatório ML
      //   "DD/MM/YYYY"
      //   "YYYY-MM-DD"
      if (dataVenda) {
        try {
          const MESES_PT = ['janeiro','fevereiro','março','abril','maio','junho',
                            'julho','agosto','setembro','outubro','novembro','dezembro'];
          let d: Date | null = null;

          // [^\s]+ em vez de \w+ porque \w em JS não captura ç, ã, etc.
          // "março" com cedilha seria truncado para "mar" com \w+
          const mPt = dataVenda.match(/(\d{1,2})\s+de\s+([^\s]+)\s+de\s+(\d{4})/i);
          if (mPt) {
            const mesIdx = MESES_PT.indexOf(mPt[2].toLowerCase());
            if (mesIdx !== -1) d = new Date(Number(mPt[3]), mesIdx, Number(mPt[1]));
          } else if (dataVenda.includes('/')) {
            const [dd, mm, yyyy] = dataVenda.split('/');
            d = new Date(Number(yyyy), Number(mm) - 1, Number(dd));
          } else {
            d = new Date(dataVenda);
          }
          // d.getDay(): 0=Dom, 1=Seg … 6=Sáb — alinhado com o array diasSemana
          if (d && !isNaN(d.getTime())) stats.diasSemana[d.getDay()]++;
        } catch (_) { /* ignora datas inválidas */ }
      }
    });

    return stats;
  }, [data]);

  // ─── derivados ────────────────────────────────────────────────────
  const derived = useMemo(() => {
    if (!analysis) return null;

    // Fidelidade
    const clientesB2C = [...analysis.clientes.values()].filter(c => !c.isCnpj);
    const clientesB2B = [...analysis.clientes.values()].filter(c => c.isCnpj);
    const recorrentesB2C  = clientesB2C.filter(c => c.compras > 1).length;
    const recorrentesB2B  = clientesB2B.filter(c => c.compras > 1).length;
    const taxaRetencaoB2C = clientesB2C.length > 0 ? (recorrentesB2C / clientesB2C.length) * 100 : 0;
    const ltvMedioB2C     = clientesB2C.length > 0
      ? clientesB2C.reduce((s, c) => s + c.receitaTotal, 0) / clientesB2C.length : 0;
    const ticketMedioB2B  = clientesB2B.length > 0
      ? clientesB2B.reduce((s, c) => s + c.receitaTotal / c.compras, 0) / clientesB2B.length : 0;

    // Anúncios — margem de contribuição = receita - comissao - frete (sem CMV)
    const margemPremium  = analysis.anuncios.premium.receitaBruta > 0
      ? ((analysis.anuncios.premium.receitaBruta - analysis.anuncios.premium.comissao - analysis.anuncios.premium.frete)
         / analysis.anuncios.premium.receitaBruta) * 100 : 0;
    const margemClassico = analysis.anuncios.classico.receitaBruta > 0
      ? ((analysis.anuncios.classico.receitaBruta - analysis.anuncios.classico.comissao - analysis.anuncios.classico.frete)
         / analysis.anuncios.classico.receitaBruta) * 100 : 0;
    const ticketMedioPremium  = analysis.anuncios.premium.vendas > 0
      ? analysis.anuncios.premium.receitaBruta / analysis.anuncios.premium.vendas : 0;
    const ticketMedioClassico = analysis.anuncios.classico.vendas > 0
      ? analysis.anuncios.classico.receitaBruta / analysis.anuncios.classico.vendas : 0;

    // Devoluções — ranking por prejuízo real, não só contagem
    const taxaDevPorSku = [...analysis.devolucoes.porSku.entries()]
      .sort((a, b) => b[1].prejuizo - a[1].prejuizo)
      .slice(0, 5)
      .map(([sku, info]) => ({ sku, ...info }));

    // Detalhes individuais ordenados por prejuízo desc
    const devolucaoDetalhes = [...analysis.devolucoes.detalhes]
      .sort((a, b) => b.prejuizo - a.prejuizo);

    // Frete divergente — ranking por valor
    const topFreteDivergente = [...analysis.freteDivergente.porSku.entries()]
      .sort((a, b) => b[1].valor - a[1].valor)
      .slice(0, 5);

    // Reclamações ranking
    const rankingReclamacoes = [...analysis.reclamacoes.porMlb.entries()]
      .sort((a, b) => b[1].total - a[1].total)
      .slice(0, 5);

    // Top cidades e UFs
    const topCidades = [...analysis.cidades.entries()].sort((a, b) => b[1] - a[1]).slice(0, 7);
    const topUFs     = [...analysis.ufs.entries()].sort((a, b) => b[1] - a[1]).slice(0, 7);

    // ACoS (somente taxaVenda/receitaBruta — sem investimento do relatório de Ads)
    const acosAds = analysis.ads.receitaBruta > 0
      ? (analysis.ads.comissaoTotal / analysis.ads.receitaBruta) * 100 : 0;

    // Melhor dia da semana
    const diasNomes = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'];
    const melhorDiaIdx = analysis.diasSemana.indexOf(Math.max(...analysis.diasSemana));

    return {
      clientesB2C, clientesB2B, recorrentesB2C, recorrentesB2B,
      taxaRetencaoB2C, ltvMedioB2C, ticketMedioB2B,
      margemPremium, margemClassico, ticketMedioPremium, ticketMedioClassico,
      taxaDevPorSku, devolucaoDetalhes, topFreteDivergente, rankingReclamacoes,
      topCidades, topUFs, acosAds,
      melhorDia: diasNomes[melhorDiaIdx],
      melhorDiaVendas: analysis.diasSemana[melhorDiaIdx],
      diasSemana: diasNomes.map((nome, i) => ({ nome, vendas: analysis.diasSemana[i] })),
    };
  }, [analysis]);

  // ─── Empty state ──────────────────────────────────────────────────
  if (!analysis || !derived) {
    return (
      <div style={{
        display: 'flex', flexDirection: 'column', alignItems: 'center',
        justifyContent: 'center', padding: '80px 24px', textAlign: 'center',
        background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: 14
      }}>
        <div style={{
          width: 56, height: 56, borderRadius: 16,
          background: 'var(--blue-50)', display: 'flex',
          alignItems: 'center', justifyContent: 'center', marginBottom: 16
        }}>
          <TrendingUp size={24} style={{ color: 'var(--blue-600)' }} />
        </div>
        <h3 style={{ fontSize: 15, fontWeight: 700, color: 'var(--tx)', marginBottom: 6 }}>
          Aguardando dados
        </h3>
        <p style={{ fontSize: 13, color: 'var(--tx-3)', maxWidth: 320, lineHeight: 1.6 }}>
          Importe o Relatório ML para ver a análise estratégica completa.
        </p>
      </div>
    );
  }

  // ─── CSS ───────────────────────────────────────────────────────────
  const CSS = `
    .adv-wrap{display:flex;flex-direction:column;gap:14px}
    .adv-grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    .adv-grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
    .adv-grid2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
    .adv-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:18px 20px;position:relative;overflow:hidden}
    .adv-card::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;border-radius:14px 14px 0 0}
    .adv-card.blue::after{background:var(--blue-500)}.adv-card.green::after{background:var(--green)}
    .adv-card.red::after{background:var(--red)}.adv-card.orange::after{background:var(--orange)}
    .adv-card.yellow::after{background:#F59E0B}.adv-card.indigo::after{background:#6366F1}
    .adv-card.teal::after{background:#14B8A6}.adv-card.rose::after{background:#F43F5E}
    .adv-lbl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--tx-3);margin-bottom:8px}
    .adv-val{font-size:22px;font-weight:800;color:var(--tx);line-height:1;letter-spacing:-.5px}
    .adv-val.g{color:var(--green)}.adv-val.r{color:var(--red)}.adv-val.o{color:var(--orange)}
    .adv-val.b{color:var(--blue-500)}.adv-val.y{color:#F59E0B}.adv-val.i{color:#6366F1}.adv-val.t{color:#14B8A6}
    .adv-sub{font-size:11px;color:var(--tx-4);margin-top:5px;display:flex;align-items:center;gap:4px}
    .adv-ic{position:absolute;top:16px;right:16px}
    .adv-inner{background:var(--surface-2);border:1px solid var(--border);border-radius:10px;padding:10px 12px}
    .adv-row{display:flex;justify-content:space-between;align-items:center;font-size:11px;padding:5px 0;border-bottom:1px solid var(--border)}
    .adv-row:last-child{border-bottom:none}
    .adv-badge-red{font-size:10px;font-weight:700;padding:2px 8px;border-radius:99px;background:rgba(239,68,68,.12);color:var(--red)}
    .adv-badge-blue{font-size:10px;font-weight:700;padding:2px 8px;border-radius:99px;background:rgba(59,130,246,.12);color:var(--blue-500)}
    .adv-badge-green{font-size:10px;font-weight:700;padding:2px 8px;border-radius:99px;background:rgba(34,197,94,.12);color:var(--green)}
    .adv-badge-orange{font-size:10px;font-weight:700;padding:2px 8px;border-radius:99px;background:rgba(249,115,22,.12);color:var(--orange)}
    .adv-section-title{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--tx-4);padding:4px 0 2px;border-bottom:1px solid var(--border);margin-bottom:2px}
    .bar-wrap{display:flex;flex-direction:column;gap:5px;margin-top:8px}
    .bar-row{display:grid;grid-template-columns:32px 1fr 36px;align-items:center;gap:8px;font-size:11px}
    .bar-bg{height:6px;background:var(--border);border-radius:99px;overflow:hidden}
    .bar-fill{height:100%;border-radius:99px;transition:width .4s ease}
    .adv-accordion-btn{width:100%;display:flex;justify-content:space-between;align-items:center;padding:10px 14px;background:var(--surface-2);border:1px solid var(--border);border-radius:10px;cursor:pointer;font-size:11px;font-weight:700;color:var(--tx-2);transition:background .15s}
    .adv-accordion-btn:hover{background:var(--border)}
    .adv-accordion-btn svg{transition:transform .25s}
    .adv-accordion-btn.open svg{transform:rotate(180deg)}
    .adv-dev-table{width:100%;border-collapse:collapse;font-size:11px;margin-top:10px}
    .adv-dev-table th{text-align:left;font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--tx-4);padding:6px 10px;border-bottom:2px solid var(--border);white-space:nowrap}
    .adv-dev-table td{padding:9px 10px;border-bottom:1px solid var(--border);color:var(--tx-2);vertical-align:middle}
    .adv-dev-table tr:last-child td{border-bottom:none}
    .adv-dev-table tr:hover td{background:var(--surface-2)}
    .adv-pill{display:inline-block;font-size:9px;font-weight:700;padding:2px 7px;border-radius:99px;white-space:nowrap}
    .adv-pill.prej-alto{background:rgba(239,68,68,.12);color:var(--red)}
    .adv-pill.prej-medio{background:rgba(249,115,22,.12);color:var(--orange)}
    .adv-pill.prej-baixo{background:rgba(234,179,8,.12);color:#CA8A04}
    .adv-pill.aguard{background:rgba(100,116,139,.12);color:var(--tx-3)}
    .adv-pill.revisado{background:rgba(34,197,94,.12);color:var(--green)}
    @media(max-width:900px){.adv-grid3,.adv-grid4,.adv-grid2{grid-template-columns:1fr}}
  `;

  const [devAberto, setDevAberto] = useState(false);
  const maxDia = Math.max(...analysis.diasSemana);

  return (
    <div className="adv-wrap">
      <style>{CSS}</style>

      {/* ── BLOCO 1: KPIs principais ── */}
      <div className="adv-section-title">Clientes &amp; Retenção</div>
      <div className="adv-grid4">

        {/* Taxa de Retenção B2C — CORRIGIDO: não mais "LTV" */}
        <div className="adv-card blue">
          <div className="adv-ic"><Users size={18} style={{ color: 'var(--blue-500)' }} /></div>
          <div className="adv-lbl">Retenção B2C</div>
          <div className={`adv-val ${derived.taxaRetencaoB2C > 20 ? 'g' : 'b'}`}>
            {fmtPct(derived.taxaRetencaoB2C)}
          </div>
          <div className="adv-sub">
            <ShoppingBag size={11} />
            {derived.recorrentesB2C} recorrentes de {derived.clientesB2C.length} únicos
          </div>
        </div>

        {/* LTV Médio B2C — NOVO: cálculo real de valor por cliente */}
        <div className="adv-card teal">
          <div className="adv-ic"><DollarSign size={18} style={{ color: '#14B8A6' }} /></div>
          <div className="adv-lbl">LTV Médio B2C</div>
          <div className="adv-val t">{fmt(derived.ltvMedioB2C)}</div>
          <div className="adv-sub">
            <TrendingUp size={11} /> receita média por cliente pessoa física
          </div>
        </div>

        {/* Clientes B2B — NOVO */}
        <div className="adv-card indigo">
          <div className="adv-ic"><Award size={18} style={{ color: '#6366F1' }} /></div>
          <div className="adv-lbl">Clientes B2B (CNPJ)</div>
          <div className="adv-val i">{derived.clientesB2B.length}</div>
          <div className="adv-sub">
            <DollarSign size={11} /> ticket médio {fmt(derived.ticketMedioB2B)}
          </div>
        </div>

        {/* Melhor dia da semana — NOVO */}
        <div className="adv-card green">
          <div className="adv-ic"><Calendar size={18} style={{ color: 'var(--green)' }} /></div>
          <div className="adv-lbl">Melhor Dia de Vendas</div>
          <div className="adv-val g">{derived.melhorDia}</div>
          <div className="adv-sub">
            <BarChart2 size={11} /> {derived.melhorDiaVendas} pedidos nesse dia
          </div>
        </div>
      </div>

      {/* ── BLOCO 2: Anúncios — CORRIGIDO: margem de contribuição, não "lucro" ── */}
      <div className="adv-section-title">Performance de Anúncios</div>
      <div className="adv-grid3">

        <div className="adv-card indigo" style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <div className="adv-lbl" style={{ marginBottom: 0 }}>Premium vs Clássico</div>

          <div className="adv-inner">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end' }}>
              <div>
                <div style={{ fontSize: 22, fontWeight: 800, color: 'var(--tx)' }}>
                  {analysis.anuncios.premium.vendas}
                </div>
                <div style={{ fontSize: 9, fontWeight: 700, textTransform: 'uppercase', color: '#6366F1' }}>
                  Vendas Premium
                </div>
              </div>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontSize: 10, color: 'var(--tx-3)' }}>Margem contrib. ML</div>
                <div style={{ fontSize: 15, fontWeight: 800, color: derived.margemPremium > 0 ? 'var(--green)' : 'var(--red)' }}>
                  {fmtPct(derived.margemPremium)}
                </div>
                <div style={{ fontSize: 10, color: 'var(--tx-4)' }}>
                  ticket {fmt(derived.ticketMedioPremium)}
                </div>
              </div>
            </div>
          </div>

          <div className="adv-inner">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end' }}>
              <div>
                <div style={{ fontSize: 22, fontWeight: 800, color: 'var(--tx)' }}>
                  {analysis.anuncios.classico.vendas}
                </div>
                <div style={{ fontSize: 9, fontWeight: 700, textTransform: 'uppercase', color: 'var(--tx-3)' }}>
                  Vendas Clássico
                </div>
              </div>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontSize: 10, color: 'var(--tx-3)' }}>Margem contrib. ML</div>
                <div style={{ fontSize: 15, fontWeight: 800, color: derived.margemClassico > 0 ? 'var(--green)' : 'var(--red)' }}>
                  {fmtPct(derived.margemClassico)}
                </div>
                <div style={{ fontSize: 10, color: 'var(--tx-4)' }}>
                  ticket {fmt(derived.ticketMedioClassico)}
                </div>
              </div>
            </div>
          </div>

          <div style={{ fontSize: 10, color: 'var(--tx-4)', lineHeight: 1.5, marginTop: 2 }}>
            ⚠ Margem de contribuição = receita bruta − comissão ML − frete. Não inclui CMV.
          </div>
        </div>

        {/* Ads — CORRIGIDO: receita bruta, + ACoS */}
        <div className="adv-card yellow" style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <div className="adv-lbl" style={{ marginBottom: 0 }}>Mercado Ads</div>
          <div className="adv-inner">
            <div className="adv-row">
              <span style={{ color: 'var(--tx-3)' }}>Vendas via Ads</span>
              <span style={{ fontWeight: 700, color: 'var(--tx)' }}>{analysis.ads.qtd}</span>
            </div>
            <div className="adv-row">
              <span style={{ color: 'var(--tx-3)' }}>Receita bruta Ads</span>
              <span style={{ fontWeight: 700, color: 'var(--tx)' }}>{fmt(analysis.ads.receitaBruta)}</span>
            </div>
            <div className="adv-row">
              <span style={{ color: 'var(--tx-3)' }}>Comissão ML em Ads</span>
              <span style={{ fontWeight: 700, color: 'var(--red)' }}>{fmt(analysis.ads.comissaoTotal)}</span>
            </div>
            <div className="adv-row">
              <span style={{ color: 'var(--tx-3)' }}>ACoS (comissão/receita)</span>
              <span className={`adv-badge-${derived.acosAds < 15 ? 'green' : derived.acosAds < 25 ? 'orange' : 'red'}`}>
                {fmtPct(derived.acosAds)}
              </span>
            </div>
          </div>
          <div style={{ fontSize: 10, color: 'var(--tx-4)', lineHeight: 1.5 }}>
            ACoS ideal &lt; 15%. Importe o relatório de Ads para ACoS por SKU.
          </div>
        </div>

        {/* Ranking de Reclamações — CORRIGIDO: usando ml-sales-library completa */}
        <div className="adv-card red" style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <div className="adv-lbl" style={{ marginBottom: 0 }}>Ranking de Reclamações</div>
          {derived.rankingReclamacoes.length === 0 ? (
            <div style={{ fontSize: 12, color: 'var(--tx-4)', marginTop: 8 }}>
              Nenhuma reclamação registrada ✅
            </div>
          ) : derived.rankingReclamacoes.map(([mlb, info], i) => (
            <div key={i} className="adv-inner" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ minWidth: 0, flex: 1, paddingRight: 8 }}>
                <div style={{ fontSize: 11, fontWeight: 700, color: 'var(--tx)' }}>{mlb}</div>
                <div style={{ fontSize: 10, color: 'var(--tx-4)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                  {info.titulo}
                </div>
              </div>
              <span className="adv-badge-red">{info.total}</span>
            </div>
          ))}
          <div style={{ fontSize: 11, fontWeight: 700, color: 'var(--tx-3)', marginTop: 4 }}>
            Total: <span style={{ color: 'var(--red)' }}>{analysis.reclamacoes.total}</span> ocorrências
          </div>
        </div>
      </div>

      {/* ── BLOCO 3: Perdas operacionais ── */}
      <div className="adv-section-title">Perdas Operacionais</div>
      <div className="adv-grid4">

        {/* Devoluções */}
        <div className="adv-card orange">
          <div className="adv-ic"><RefreshCcw size={16} style={{ color: 'var(--orange)' }} /></div>
          <div className="adv-lbl">Devoluções</div>
          <div className="adv-val o">{analysis.devolucoes.total}</div>
          <div className="adv-sub">
            <PackageX size={11} /> frete perdido: {fmt(analysis.devolucoes.fretePerdido)}
          </div>
        </div>

        {/* Cancelamentos — CORRIGIDO: emTransito via descrição */}
        <div className="adv-card red">
          <div className="adv-ic"><XCircle size={16} style={{ color: 'var(--red)' }} /></div>
          <div className="adv-lbl">Cancelamentos</div>
          <div className="adv-val r">{analysis.cancelamentos.total}</div>
          <div className="adv-sub">
            <AlertTriangle size={11} />
            {analysis.cancelamentos.emTransito > 0
              ? `${analysis.cancelamentos.emTransito} já enviados ⚠`
              : 'nenhum em trânsito'}
          </div>
        </div>

        {/* Frete divergente — CORRIGIDO: mostra valor total, não só contagem */}
        <div className="adv-card yellow">
          <div className="adv-ic"><Scale size={16} style={{ color: '#F59E0B' }} /></div>
          <div className="adv-lbl">Frete Divergente</div>
          <div className="adv-val y">{fmt(analysis.freteDivergente.totalPerdido)}</div>
          <div className="adv-sub">
            <AlertTriangle size={11} />
            {analysis.freteDivergente.porSku.size} SKUs com peso errado
          </div>
        </div>

        {/* Receita perdida em cancelamentos */}
        <div className="adv-card rose">
          <div className="adv-ic"><TrendingUp size={16} style={{ color: '#F43F5E' }} /></div>
          <div className="adv-lbl">Receita Cancelada</div>
          <div className="adv-val r">{fmt(analysis.cancelamentos.receitaPerdida)}</div>
          <div className="adv-sub">
            <XCircle size={11} /> receita bruta não concretizada
          </div>
        </div>
      </div>

      {/* ── BLOCO 4: Devoluções expandidas + frete divergente ── */}
      <div className="adv-grid2">

        {/* Devoluções expandidas — accordion com tabela linha a linha */}
        <div className="adv-card orange" style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div className="adv-lbl" style={{ marginBottom: 0 }}>Devoluções por SKU</div>
            <span style={{ fontSize: 10, color: 'var(--tx-4)' }}>
              prejuízo total: <strong style={{ color: 'var(--red)' }}>{fmt(analysis.devolucoes.prejuizoTotal)}</strong>
            </span>
          </div>

          {/* Resumo por SKU */}
          {derived.taxaDevPorSku.length === 0 ? (
            <div style={{ fontSize: 12, color: 'var(--tx-4)' }}>Nenhuma devolução ✅</div>
          ) : derived.taxaDevPorSku.map((item, i) => (
            <div key={i} className="adv-inner" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ minWidth: 0, flex: 1, paddingRight: 8 }}>
                <div style={{ fontSize: 11, fontWeight: 700, color: 'var(--tx)' }}>{item.sku}</div>
                <div style={{ fontSize: 10, color: 'var(--tx-4)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                  {item.titulo}
                </div>
                <div style={{ fontSize: 10, color: 'var(--tx-3)', marginTop: 2 }}>
                  prejuízo: <strong style={{ color: 'var(--red)' }}>{fmt(item.prejuizo)}</strong>
                  {' · '}receita perdida: {fmt(item.receitaPerdida)}
                </div>
              </div>
              <span className="adv-badge-orange">{item.total}×</span>
            </div>
          ))}

          {/* Botão accordion */}
          {derived.devolucaoDetalhes.length > 0 && (
            <button
              className={`adv-accordion-btn${devAberto ? ' open' : ''}`}
              onClick={() => setDevAberto(v => !v)}
            >
              <span>Ver detalhes linha a linha ({derived.devolucaoDetalhes.length})</span>
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M3 5l4 4 4-4" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </button>
          )}

          {/* Tabela expandida */}
          {devAberto && derived.devolucaoDetalhes.length > 0 && (
            <div style={{ overflowX: 'auto', marginTop: 4 }}>
              <table className="adv-dev-table">
                <thead>
                  <tr>
                    <th>SKU</th>
                    <th>Produto</th>
                    <th>Comprador</th>
                    <th>Cidade / UF</th>
                    <th>Data venda</th>
                    <th>Ciclo</th>
                    <th>Receita</th>
                    <th>Reembolso</th>
                    <th>Frete</th>
                    <th>Prejuízo</th>
                    <th>Status revisão</th>
                    <th>Rastreio</th>
                  </tr>
                </thead>
                <tbody>
                  {derived.devolucaoDetalhes.map((d, i) => {
                    // Classificação do prejuízo
                    const pillClass = d.prejuizo > 200 ? 'prej-alto' : d.prejuizo > 80 ? 'prej-medio' : 'prej-baixo';
                    // Status da revisão ML
                    const revisaoLabel = d.revisadoML && d.revisadoML.trim()
                      ? d.revisadoML
                      : d.resultado && d.resultado.trim()
                        ? d.resultado
                        : 'Aguardando';
                    const revisaoPill  = revisaoLabel === 'Aguardando' ? 'aguard' : 'revisado';
                    // Formatação da data (só DD/MM)
                    const fmtData = (s: string) => {
                      const m2 = s.match(/(\d{1,2})\s+de\s+([^\s]+)\s+de\s+(\d{4})/i);
                      const MESES_ABREV = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'];
                      const MESES_FULL  = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
                      if (m2) {
                        const mi = MESES_FULL.indexOf(m2[2].toLowerCase());
                        return `${m2[1].padStart(2,'0')}/${mi >= 0 ? MESES_ABREV[mi] : m2[2].slice(0,3)}`;
                      }
                      return s.slice(0,5);
                    };
                    return (
                      <tr key={i}>
                        <td><strong style={{ color: 'var(--tx)' }}>{d.sku}</strong></td>
                        <td style={{ maxWidth: 160, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}
                            title={d.titulo}>{d.titulo}</td>
                        <td style={{ whiteSpace: 'nowrap' }}>{d.comprador || '—'}</td>
                        <td style={{ whiteSpace: 'nowrap' }}>{d.cidade && d.uf ? `${d.cidade} / ${d.uf}` : '—'}</td>
                        <td style={{ whiteSpace: 'nowrap', fontFamily: 'var(--font-mono)', fontSize: 10 }}>
                          {fmtData(d.dataVenda)}
                        </td>
                        <td style={{ textAlign: 'center', fontFamily: 'var(--font-mono)', fontSize: 10 }}>
                          {d.diasCiclo !== null ? `${d.diasCiclo}d` : '—'}
                        </td>
                        <td style={{ fontFamily: 'var(--font-mono)', fontSize: 10, whiteSpace: 'nowrap' }}>
                          {fmt(d.receita)}
                        </td>
                        <td style={{ fontFamily: 'var(--font-mono)', fontSize: 10, whiteSpace: 'nowrap', color: 'var(--orange)' }}>
                          -{fmt(d.reembolso)}
                        </td>
                        <td style={{ fontFamily: 'var(--font-mono)', fontSize: 10, whiteSpace: 'nowrap', color: 'var(--orange)' }}>
                          -{fmt(d.frete)}
                        </td>
                        <td>
                          <span className={`adv-pill ${pillClass}`}>{fmt(d.prejuizo)}</span>
                        </td>
                        <td>
                          <span className={`adv-pill ${revisaoPill}`}>{revisaoLabel}</span>
                          {d.motivo && <div style={{ fontSize: 9, color: 'var(--tx-4)', marginTop: 2 }}>{d.motivo}</div>}
                        </td>
                        <td style={{ fontFamily: 'var(--font-mono)', fontSize: 9, color: 'var(--tx-4)' }}>
                          {d.rastreio || '—'}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}
        </div>

        {/* Frete divergente por SKU */}
        <div className="adv-card yellow" style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          <div className="adv-lbl" style={{ marginBottom: 0 }}>SKUs com maior erro de peso</div>
          {derived.topFreteDivergente.length === 0 ? (
            <div style={{ fontSize: 12, color: 'var(--tx-4)' }}>Nenhuma divergência ✅</div>
          ) : derived.topFreteDivergente.map(([sku, info], i) => (
            <div key={i} className="adv-inner" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ minWidth: 0, flex: 1, paddingRight: 8 }}>
                <div style={{ fontSize: 11, fontWeight: 700, color: 'var(--tx)' }}>{sku}</div>
                <div style={{ fontSize: 10, color: 'var(--tx-4)' }}>
                  {info.ocorrencias}× cobrado — total: {fmt(info.valor)}
                </div>
              </div>
              <span className="adv-badge-orange">{fmt(info.valor)}</span>
            </div>
          ))}
        </div>
      </div>

      {/* ── BLOCO 5: Geo + Dias da semana ── */}
      <div className="adv-section-title">Distribuição Geográfica &amp; Temporal</div>
      <div className="adv-grid3">

        {/* Top Cidades */}
        <div className="adv-card blue" style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <div className="adv-lbl" style={{ marginBottom: 4 }}>Top Cidades</div>
          {derived.topCidades.length === 0 ? (
            <div style={{ fontSize: 12, color: 'var(--tx-4)' }}>Sem dados de cidade</div>
          ) : derived.topCidades.map(([cid, qtd], i) => (
            <div key={i} className="adv-row">
              <span style={{ color: 'var(--tx-3)' }}><MapPin size={10} style={{ display: 'inline', marginRight: 4 }} />{cid}</span>
              <span style={{ fontWeight: 700, color: 'var(--tx)' }}>{qtd}</span>
            </div>
          ))}
        </div>

        {/* Top UFs — NOVO */}
        <div className="adv-card teal" style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <div className="adv-lbl" style={{ marginBottom: 4 }}>Top Estados (UF)</div>
          {derived.topUFs.length === 0 ? (
            <div style={{ fontSize: 12, color: 'var(--tx-4)' }}>Sem dados de UF</div>
          ) : derived.topUFs.map(([uf, qtd], i) => (
            <div key={i} className="adv-row">
              <span style={{ color: 'var(--tx-3)', fontWeight: 700, fontSize: 12 }}>{uf}</span>
              <span style={{ fontWeight: 700, color: 'var(--tx)' }}>{qtd} vendas</span>
            </div>
          ))}
        </div>

        {/* Dias da semana — NOVO */}
        <div className="adv-card green">
          <div className="adv-lbl" style={{ marginBottom: 6 }}>Vendas por Dia da Semana</div>
          <div className="bar-wrap">
            {derived.diasSemana.map(({ nome, vendas }, i) => (
              <div key={i} className="bar-row">
                <span style={{ color: 'var(--tx-3)', fontWeight: 600, textAlign: 'right' }}>{nome}</span>
                <div className="bar-bg">
                  <div
                    className="bar-fill"
                    style={{
                      width: maxDia > 0 ? `${(vendas / maxDia) * 100}%` : '0%',
                      background: vendas === maxDia ? 'var(--green)' : 'var(--blue-500)',
                      opacity: vendas === maxDia ? 1 : 0.5
                    }}
                  />
                </div>
                <span style={{ color: 'var(--tx-3)', textAlign: 'right', fontSize: 10 }}>{vendas}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* ── BLOCO 6: Resumo estratégico + calendário ── */}
      <div className="adv-grid2">
        <div className="adv-card">
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 14 }}>
            <Award size={16} style={{ color: 'var(--blue-500)' }} />
            <div className="adv-lbl" style={{ marginBottom: 0 }}>Resumo Estratégico</div>
          </div>
          <p style={{ fontSize: 13, color: 'var(--tx-2)', lineHeight: 1.8 }}>
            {derived.rankingReclamacoes.length > 0
              ? <>O anúncio <strong style={{ color: 'var(--tx)' }}>{derived.rankingReclamacoes[0][0]}</strong> concentra mais reclamações — priorize revisão do produto/descrição. </>
              : 'Nenhuma reclamação no período — ótima saúde de reputação. '}

            {derived.taxaDevPorSku.length > 0
              ? <>O SKU <strong style={{ color: 'var(--tx)' }}>{derived.taxaDevPorSku[0].sku}</strong> lidera devoluções. </>
              : ''}

            Anúncios <strong style={{ color: 'var(--blue-500)' }}>
              {derived.margemPremium >= derived.margemClassico ? 'Premium' : 'Clássico'}
            </strong> têm maior margem de contribuição ML ({fmtPct(Math.max(derived.margemPremium, derived.margemClassico))}).

            <br /><br />

            Taxa de retenção B2C de <strong style={{ color: derived.taxaRetencaoB2C > 20 ? 'var(--green)' : 'var(--orange)' }}>
              {fmtPct(derived.taxaRetencaoB2C)}
            </strong> com LTV médio de <strong style={{ color: 'var(--tx)' }}>{fmt(derived.ltvMedioB2C)}</strong> por cliente.{' '}
            {derived.clientesB2B.length > 0 && (
              <>Você tem <strong>{derived.clientesB2B.length}</strong> clientes B2B com ticket médio de {fmt(derived.ticketMedioB2B)} — explore esse segmento.</>
            )}
          </p>
        </div>

        <div className="adv-card">
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 14 }}>
            <Calendar size={16} style={{ color: 'var(--blue-500)' }} />
            <div className="adv-lbl" style={{ marginBottom: 0 }}>Próximas Datas do Varejo</div>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {[
              { date: '15 Mar', event: 'Dia do Consumidor' },
              { date: '18 Abr', event: 'Páscoa' },
              { date: '12 Mai', event: 'Dia das Mães' },
              { date: '12 Jun', event: 'Dia dos Namorados' },
              { date: '15 Ago', event: 'Dia dos Pais' },
              { date: '15 Nov', event: 'Black Friday' },
              { date: '25 Dez', event: 'Natal' },
            ].map(({ date, event }) => (
              <div key={date} style={{
                display: 'flex', alignItems: 'center', gap: 12,
                background: 'var(--surface-2)', border: '1px solid var(--border)',
                borderRadius: 8, padding: '8px 12px'
              }}>
                <span style={{ fontSize: 10, fontWeight: 800, color: 'var(--blue-500)', width: 40 }}>{date}</span>
                <span style={{ fontSize: 11, fontWeight: 600, color: 'var(--tx-2)', textTransform: 'uppercase' }}>{event}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}