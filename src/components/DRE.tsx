import React, { useState, useMemo, useEffect } from 'react';
import { supabase } from '../lib/supabase';
import { Plus, Trash2, Landmark, Wallet, Receipt, BarChart3, Info, Download, AlertTriangle } from 'lucide-react';

// ─── Tipos ───────────────────────────────────────────────────────────────────

type Regime = 'MEI' | 'SIMPLES' | 'PRESUMIDO';

interface Lancamento { id: string; nome: string; valor: number; categoria: string; }

// ─── Componente principal ─────────────────────────────────────────────────────

export const DRE = ({ data, userId }: { data: any; userId?: string }) => {
  const [regime, setRegime]           = useState<Regime>('SIMPLES');
  const [dasMei, setDasMei]           = useState<number>(75.90);   // MEI: valor fixo DAS
  const [aliqSimples, setAliqSimples] = useState<number>(0);       // Simples: alíquota efetiva %
  const [lancamentos, setLancamentos] = useState<Lancamento[]>([]);

  // Carregar lançamentos
  useEffect(() => {
    if (!userId) return;
    supabase.from('sobra_quanto_dre_lancamentos')
      .select('*').eq('user_id', userId)
      .then(({ data }) => {
        if (data) setLancamentos(data.map((l: any) => ({
          id: l.id, nome: l.nome, valor: Number(l.valor), categoria: l.categoria
        })));
      });
  }, [userId]);

  const salvarLancamento = async (item: Lancamento) => {
    if (!userId) return;
    await supabase.from('sobra_quanto_dre_lancamentos')
      .upsert({ id: item.id, user_id: userId, nome: item.nome, valor: item.valor, categoria: item.categoria });
  };
  const deletarLancamento = async (id: string) => {
    if (!userId) return;
    await supabase.from('sobra_quanto_dre_lancamentos').delete().eq('id', id);
  };

  // ─── Cálculo central ─────────────────────────────────────────────────────────
  const totals = useMemo(() => {
    const stats       = data?.stats || {};
    const receitaBruta    = Number(stats.receitaBruta    || 0);
    const totalCMV        = Number(stats.totalCMV        || 0);
    const comissaoML      = Number(stats.comissaoML      || 0);
    const freteVendedor   = Number(stats.freteVendedor   || 0);
    const perdaDevolucao  = Number(stats.perdaDevolucao  || 0);
    const perdaCancelamento = Number(stats.perdaCancelamento || 0);

    // ── Imposto por regime ──────────────────────────────────────────────────────
    let impostoTotal  = 0;
    let irpj          = 0;
    let csll          = 0;
    let basePresuncao = 0;
    let adicionalIRPJ = 0;

    if (regime === 'MEI') {
      // MEI: DAS fixo mensal — não incide sobre receita
      impostoTotal = dasMei;
    }

    // Base líquida: exclui devoluções e cancelamentos (dinheiro que não ficou com o vendedor)
    const baseReceita = receitaBruta - perdaDevolucao - perdaCancelamento;

    if (regime === 'SIMPLES') {
      impostoTotal = baseReceita * (aliqSimples / 100);
    }

    if (regime === 'PRESUMIDO') {
      basePresuncao = baseReceita * 0.08;
      irpj          = basePresuncao * 0.15;
      adicionalIRPJ = Math.max(0, (basePresuncao - 20000)) * 0.10;
      csll          = (baseReceita * 0.12) * 0.09;
      const pis     = baseReceita * 0.0065;
      const cofins  = baseReceita * 0.03;
      impostoTotal  = irpj + adicionalIRPJ + csll + pis + cofins;
    }

    // ── DRE ──────────────────────────────────────────────────────────────────────
    // Receita líquida = bruta − imposto − taxas ML − frete ML − devoluções − cancelamentos
    const receitaLiquida = receitaBruta - impostoTotal - comissaoML - freteVendedor
                         - perdaDevolucao - perdaCancelamento;

    const lucroBruto = receitaLiquida - totalCMV;

    // Despesas operacionais lançadas manualmente
    const getSum = (cat: string) =>
      lancamentos.filter(l => l.categoria === cat).reduce((a, c) => a + (Number(c.valor) || 0), 0);

    const totalAds       = getSum('ADS');
    const totalFull      = getSum('FULL');
    const totalFixas     = getSum('FIXA');
    const totalLogistica = getSum('LOGISTICA');
    const totalCaixa     = getSum('CAIXA');
    const totalDespesas  = totalAds + totalFull + totalFixas + totalLogistica;

    const lucroLiquido = lucroBruto - totalDespesas;
    const caixaFinal   = lucroLiquido - totalCaixa;
    const margemPerc   = receitaBruta > 0 ? (lucroLiquido / receitaBruta) * 100 : 0;

    // Alíquota efetiva real (para exibir no PDF e na tela)
    const aliquotaEfetiva = receitaBruta > 0 ? (impostoTotal / receitaBruta) * 100 : 0;

    return {
      receitaBruta, receitaLiquida,
      impostoTotal, irpj, adicionalIRPJ, csll, basePresuncao,
      comissaoML, freteVendedor,
      perdaDevolucao, perdaCancelamento,
      totalCMV, lucroBruto,
      totalAds, totalFull, totalFixas, totalLogistica, totalDespesas,
      lucroLiquido, totalCaixa, caixaFinal,
      margemPerc, aliquotaEfetiva,
    };
  }, [data, lancamentos, regime, dasMei, aliqSimples]);

  // ── Lançamentos ──────────────────────────────────────────────────────────────
  const addItem = (cat: string) => {
    const novo: Lancamento = { id: Date.now().toString(), nome: '', valor: 0, categoria: cat };
    setLancamentos(p => [...p, novo]);
    salvarLancamento(novo);
  };
  const updItem = (id: string, f: string, v: any) => {
    setLancamentos(p => {
      const next    = p.map(l => l.id === id ? { ...l, [f]: f === 'valor' ? parseFloat(v) || 0 : v } : l);
      const updated = next.find(l => l.id === id);
      if (updated) salvarLancamento(updated);
      return next;
    });
  };
  const delItem = (id: string) => {
    setLancamentos(p => p.filter(l => l.id !== id));
    deletarLancamento(id);
  };

  const fmt = (v: number) =>
    new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v);

  // ── Exportar PDF ─────────────────────────────────────────────────────────────
  const exportarPDF = () => {
    const mesLabel    = new Date().toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' });
    const regimeLabel = regime === 'MEI'
      ? `MEI — DAS mensal ${fmt(dasMei)}`
      : regime === 'SIMPLES'
        ? `Simples Nacional — ${aliqSimples}% sobre receita bruta`
        : `Lucro Presumido — IRPJ/CSLL/PIS/COFINS calculados automaticamente`;

    const despesasExtras = lancamentos
      .filter(l => !['CAIXA', 'ADS', 'FULL'].includes(l.categoria))
      .map(l => `<tr><td>(–) ${l.nome || 'Custo'}</td><td class="neg">${fmt(-l.valor)}</td></tr>`)
      .join('');

    const investimentos = lancamentos
      .filter(l => l.categoria === 'CAIXA')
      .map(l => `<tr><td>${l.nome || 'Investimento'}</td><td class="neg">${fmt(-l.valor)}</td></tr>`)
      .join('');

    const impostoDetalhe = regime === 'PRESUMIDO'
      ? `<tr><td style="padding-left:16px;color:#6b7280;font-size:10px">Base de presunção (8%)</td><td style="text-align:right;font-size:10px;color:#6b7280">${fmt(totals.basePresuncao)}</td></tr>
         <tr><td style="padding-left:16px;color:#6b7280;font-size:10px">IRPJ 15%</td><td style="text-align:right;font-size:10px;color:#6b7280">${fmt(totals.irpj)}</td></tr>
         ${totals.adicionalIRPJ > 0 ? `<tr><td style="padding-left:16px;color:#6b7280;font-size:10px">Adicional IRPJ 10%</td><td style="text-align:right;font-size:10px;color:#6b7280">${fmt(totals.adicionalIRPJ)}</td></tr>` : ''}
         <tr><td style="padding-left:16px;color:#6b7280;font-size:10px">CSLL 9%</td><td style="text-align:right;font-size:10px;color:#6b7280">${fmt(totals.csll)}</td></tr>
         <tr><td style="padding-left:16px;color:#6b7280;font-size:10px">PIS 0,65% + COFINS 3%</td><td style="text-align:right;font-size:10px;color:#6b7280">${fmt(totals.receitaBruta * 0.0365)}</td></tr>`
      : regime === 'MEI'
        ? `<tr><td style="padding-left:16px;color:#6b7280;font-size:10px">DAS fixo mensal</td><td style="text-align:right;font-size:10px;color:#6b7280">${fmt(dasMei)}</td></tr>`
        : '';

    const html = `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"/>
<title>DRE — Sobra Quanto ML</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:Arial,sans-serif;font-size:11px;color:#1a1a2e;background:#fff;padding:32px 40px;max-width:680px;margin:0 auto}
  .header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:28px;border-bottom:2px solid #2563EB;padding-bottom:16px}
  .logo{font-size:18px;font-weight:800;color:#2563EB}.logo span{color:#1a1a2e}
  .meta{text-align:right;color:#6b7280;font-size:10px;line-height:1.6}.meta strong{color:#1a1a2e;font-size:11px}
  .section{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#2563EB;margin:18px 0 6px;padding-left:8px;border-left:3px solid #2563EB}
  table{width:100%;border-collapse:collapse}
  tr{border-bottom:1px solid #f0f0f0}tr:last-child{border-bottom:none}
  td{padding:5px 8px}
  td:first-child{color:#374151;text-transform:uppercase;font-size:10px}
  td:last-child{text-align:right;font-weight:600;font-size:11px;color:#111827;font-family:'Courier New',monospace;white-space:nowrap}
  td.neg{color:#dc2626!important}td.green{color:#059669!important}
  tr.bold td{font-weight:700;font-size:12px;background:#f9fafb}tr.bold td:first-child{color:#111827}
  .divider{height:1px;background:#e5e7eb;margin:8px 0}
  .result{background:#eff6ff;border:1px solid #bfdbfe;border-radius:8px;padding:12px 16px;margin-top:12px}
  .result td:first-child{color:#1e40af;font-weight:700;font-size:12px}
  .result td:last-child{font-size:14px;font-weight:800}
  .margem{text-align:right;font-size:10px;font-weight:700;color:#2563EB;text-transform:uppercase;margin-top:4px}
  .caixa{border:1px solid #e5e7eb;border-radius:8px;padding:12px 16px;margin-top:12px;opacity:.8}
  .caixa-title{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:#9ca3af;margin-bottom:8px}
  .caixa-total{display:flex;justify-content:space-between;align-items:center;margin-top:10px;padding-top:10px;border-top:1px solid #e5e7eb}
  .caixa-total span:first-child{font-size:10px;font-weight:700;text-transform:uppercase;color:#2563EB}
  .caixa-total span:last-child{font-size:16px;font-weight:800;color:#111827;font-family:'Courier New',monospace}
  .footer{margin-top:32px;padding-top:12px;border-top:1px solid #e5e7eb;display:flex;justify-content:space-between;font-size:9px;color:#9ca3af}
  @media print{body{padding:20px 28px}@page{margin:0;size:A4}}
</style></head><body>
<div class="header">
  <div><div class="logo">Sobra <span>Quanto</span> ML</div><div style="font-size:10px;color:#6b7280;margin-top:3px">by ProspectIA</div></div>
  <div class="meta"><strong>Demonstrativo de Resultados</strong><br/>${mesLabel}<br/>${regimeLabel}</div>
</div>
<table>
  <tr class="bold"><td>(+) Receita Bruta de Vendas</td><td>${fmt(totals.receitaBruta)}</td></tr>
</table>
<div class="section">Deduções sobre a Receita</div>
<table>
  <tr><td>(–) Impostos e Tributos (${regime})</td><td class="neg">${fmt(-totals.impostoTotal)}</td></tr>
  ${impostoDetalhe}
  <tr><td>(–) Comissão Mercado Livre</td><td class="neg">${fmt(-totals.comissaoML)}</td></tr>
  <tr><td>(–) Tarifas de Envio (ML)</td><td class="neg">${fmt(-totals.freteVendedor)}</td></tr>
  ${totals.perdaDevolucao > 0 ? `<tr><td>(–) Perdas por Devoluções</td><td class="neg">${fmt(-totals.perdaDevolucao)}</td></tr>` : ''}
  ${totals.perdaCancelamento > 0 ? `<tr><td>(–) Perdas por Cancelamentos</td><td class="neg">${fmt(-totals.perdaCancelamento)}</td></tr>` : ''}
</table>
<div class="divider"></div>
<table>
  <tr class="bold"><td>(=) Receita Líquida</td><td>${fmt(totals.receitaLiquida)}</td></tr>
  <tr><td>(–) Custo das Mercadorias Vendidas (CMV)</td><td class="neg">${fmt(-totals.totalCMV)}</td></tr>
</table>
<div class="divider"></div>
<table>
  <tr class="bold"><td>(=) Lucro Bruto Operacional</td><td class="${totals.lucroBruto >= 0 ? 'green' : 'neg'}">${fmt(totals.lucroBruto)}</td></tr>
</table>
${(totals.totalAds + totals.totalFull + totals.totalFixas + totals.totalLogistica) > 0 ? `
<div class="section">Despesas Operacionais</div>
<table>
  ${totals.totalAds  > 0 ? `<tr><td>(–) Investimento em Ads</td><td class="neg">${fmt(-totals.totalAds)}</td></tr>` : ''}
  ${totals.totalFull > 0 ? `<tr><td>(–) Custo Full ML</td><td class="neg">${fmt(-totals.totalFull)}</td></tr>` : ''}
  ${despesasExtras}
</table>` : ''}
<div class="result">
  <table><tr><td>(=) Lucro Líquido Final</td><td class="${totals.lucroLiquido >= 0 ? 'green' : 'neg'}">${fmt(totals.lucroLiquido)}</td></tr></table>
  <div class="margem">Margem líquida: ${totals.margemPerc.toFixed(2)}% &nbsp;|&nbsp; Alíquota efetiva: ${totals.aliquotaEfetiva.toFixed(2)}%</div>
</div>
${(investimentos || totals.totalCaixa > 0) ? `
<div class="caixa">
  <div class="caixa-title">Fluxo de Caixa — Investimentos em Estoque</div>
  <table>${investimentos}</table>
  <div class="caixa-total"><span>Dinheiro Disponível</span><span>${fmt(totals.caixaFinal)}</span></div>
</div>` : ''}
<div class="footer">
  <span>Sobra Quanto ML — sobrouquantoml.prospectia.space</span>
  <span>Gerado em ${new Date().toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' })}</span>
</div>
<script>window.onload=()=>{window.print();window.onafterprint=()=>window.close()}</script>
</body></html>`;

    const janela = window.open('', '_blank', 'width=780,height=900');
    if (janela) { janela.document.write(html); janela.document.close(); }
  };

  // ── CSS ───────────────────────────────────────────────────────────────────────
  const CSS = `
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    .dre-wrap{max-width:1100px;margin:0 auto;font-family:'Inter',system-ui,sans-serif}
    .dre-regime{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);padding:14px 18px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px;margin-bottom:20px}
    .dre-regime-label{display:flex;align-items:center;gap:8px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--tx-3)}
    .dre-regime-r{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
    .dre-tabs{display:flex;background:var(--surface-2);border:1px solid var(--border);border-radius:8px;padding:3px;gap:2px}
    .dre-tab{padding:5px 14px;border-radius:6px;font-size:11px;font-weight:600;color:var(--tx-3);cursor:pointer;background:none;border:none;font-family:inherit;transition:all .14s}
    .dre-tab.on{background:var(--surface);color:var(--tx);box-shadow:0 1px 3px rgba(0,0,0,.08)}
    .dre-aliq{display:flex;align-items:center;gap:6px;background:var(--surface-2);border:1px solid var(--border);border-radius:8px;padding:5px 10px;font-size:12px}
    .dre-aliq span{color:var(--tx-3);font-weight:500}
    .dre-aliq input{background:transparent;border:none;outline:none;color:#2563EB;font-weight:700;width:52px;text-align:center;font-size:12px;font-family:inherit}
    .dre-aliq em{color:#2563EB;font-style:normal;font-weight:700}
    .dre-pdf-btn{display:flex;align-items:center;gap:6px;height:32px;padding:0 14px;background:var(--surface-2);color:var(--tx-2);border:1.5px solid var(--border);border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;font-family:inherit;transition:all .14s;white-space:nowrap}
    .dre-pdf-btn:hover{border-color:var(--green);color:var(--green)}
    .dre-grid{display:grid;grid-template-columns:1fr 400px;gap:20px;align-items:start}
    @media(max-width:900px){.dre-grid{grid-template-columns:1fr}}
    .dre-doc{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);padding:28px;font-size:12px}
    .dre-doc-head{display:flex;align-items:center;justify-content:space-between;gap:8px;font-size:13px;font-weight:700;color:var(--tx);margin-bottom:24px;padding-bottom:16px;border-bottom:1px solid var(--border)}
    .dre-aliq-efetiva{font-size:10px;font-weight:600;color:var(--tx-4);background:var(--surface-2);border:1px solid var(--border);border-radius:6px;padding:3px 8px;white-space:nowrap}
    .dre-line{display:flex;justify-content:space-between;padding:6px 8px;border-radius:6px;transition:background .1s;font-family:'SF Mono','Fira Code',monospace}
    .dre-line:hover{background:var(--surface-2)}
    .dre-line.bold{font-weight:700;font-size:13px}
    .dre-line.indent{padding-left:24px}
    .dre-line .lbl{text-transform:uppercase;letter-spacing:-.02em;color:var(--tx-3);flex:1;padding-right:16px}
    .dre-line.bold .lbl{color:var(--tx)}
    .dre-line.indent .lbl{color:var(--tx-4);font-size:11px}
    .dre-line .val{flex-shrink:0;font-weight:600;color:var(--tx-2)}
    .dre-line.neg .val{color:var(--red)}
    .dre-line.indent .val{color:var(--tx-4);font-size:11px}
    .dre-div{height:1px;background:var(--border);margin:12px 0}
    .dre-section-title{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:#2563EB;margin:20px 0 8px;padding-left:8px;border-left:3px solid #2563EB}
    .dre-result{background:var(--blue-50);border:1px solid var(--blue-100);border-radius:var(--r-lg);padding:16px;margin-top:16px}
    .dre-result .dre-line .lbl{color:var(--tx)}
    .dre-margem{display:flex;justify-content:flex-end;gap:12px;margin-top:6px}
    .dre-margem span{font-size:11px;color:#2563EB;font-weight:700;text-transform:uppercase;letter-spacing:.04em}
    .dre-caixa{margin-top:16px;padding:16px;border:1px solid var(--border);border-radius:var(--r-lg);opacity:.6}
    .dre-caixa-title{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--tx-4);margin-bottom:10px}
    .dre-caixa-total{display:flex;justify-content:space-between;align-items:center;margin-top:12px;padding-top:10px;border-top:1px solid var(--border)}
    .dre-caixa-total span:first-child{font-size:11px;font-weight:700;text-transform:uppercase;color:#2563EB}
    .dre-caixa-total span:last-child{font-size:18px;font-weight:800;color:var(--tx)}
    .dre-presumido-info{background:var(--blue-50);border:1px solid var(--blue-100);border-radius:var(--r-lg);padding:10px 14px;margin-bottom:20px;font-size:11px;color:var(--tx-3);line-height:1.6}
    .dre-presumido-info strong{color:var(--tx-2)}
    .ibox{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);overflow:hidden;margin-bottom:12px}
    .ibox-head{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;background:var(--surface-2);border-bottom:1px solid var(--border)}
    .ibox-title{display:flex;align-items:center;gap:7px;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--tx-2)}
    .ibox-add{width:26px;height:26px;border-radius:6px;background:#2563EB;color:#fff;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background .14s}
    .ibox-add:hover{background:#1D4ED8}
    .ibox-body{padding:14px 16px}
    .ibox-row{display:flex;gap:8px;align-items:center;margin-bottom:10px}
    .ibox-row:last-child{margin-bottom:0}
    .ibox-name{background:transparent;border:none;border-bottom:1.5px solid var(--border);outline:none;flex:1;font-size:12px;font-weight:500;color:var(--tx-2);font-family:inherit;padding:3px 0;transition:border-color .14s}
    .ibox-name:focus{border-color:#2563EB}
    .ibox-name::placeholder{color:var(--tx-4)}
    .ibox-val-wrap{position:relative}
    .ibox-val-wrap span{position:absolute;left:8px;top:50%;transform:translateY(-50%);font-size:10px;color:var(--tx-4);font-weight:600}
    .ibox-val{background:var(--surface-2);border:1.5px solid var(--border);border-radius:8px;padding:5px 8px 5px 24px;width:100px;text-align:right;font-size:12px;font-weight:600;color:#2563EB;outline:none;font-family:inherit;transition:border-color .14s}
    .ibox-val:focus{border-color:#2563EB}
    .ibox-del{background:none;border:none;cursor:pointer;color:var(--tx-4);transition:color .14s;padding:2px;display:flex}
    .ibox-del:hover{color:var(--red)}
    .ibox-empty{font-size:11px;color:var(--tx-4);text-align:center;padding:16px 0;font-style:italic}
    .dre-info{display:flex;gap:10px;align-items:flex-start;background:var(--blue-50);border:1px solid var(--blue-100);border-radius:var(--r-lg);padding:12px 14px}
    .dre-info p{font-size:11px;color:var(--tx-3);line-height:1.6}
    input::-webkit-outer-spin-button,input::-webkit-inner-spin-button{-webkit-appearance:none}
    input[type=number]{-moz-appearance:textfield}
  `;

  const semDados = !data?.stats?.receitaBruta;

  return (
    <div className="dre-wrap">
      <style>{CSS}</style>

      {/* BARRA DE REGIME */}
      <div className="dre-regime">
        <div className="dre-regime-label">
          <Landmark size={15} style={{color:'#2563EB'}}/> Regime Tributário
        </div>
        <div className="dre-regime-r">
          <div className="dre-tabs">
            {(['MEI','SIMPLES','PRESUMIDO'] as Regime[]).map(r => (
              <button key={r} className={`dre-tab ${regime===r?'on':''}`} onClick={() => setRegime(r)}>
                {r === 'PRESUMIDO' ? 'L. Presumido' : r}
              </button>
            ))}
          </div>

          {/* Campo de configuração por regime */}
          {regime === 'MEI' && (
            <div className="dre-aliq">
              <span>DAS mensal</span>
              <input type="number" step="0.01" value={dasMei}
                onChange={e => setDasMei(parseFloat(e.target.value) || 0)}/>
            </div>
          )}
          {regime === 'SIMPLES' && (
            <div className="dre-aliq">
              <span>Alíquota efetiva</span>
              <input type="number" step="0.01"
                value={aliqSimples === 0 ? '' : aliqSimples}
                onChange={e => setAliqSimples(parseFloat(e.target.value) || 0)}
                onFocus={e => e.target.select()}
                placeholder="0"/>
              <em>%</em>
            </div>
          )}
          {regime === 'PRESUMIDO' && (
            <div style={{fontSize:11,color:'var(--tx-3)',fontWeight:500}}>
              Calculado automaticamente
            </div>
          )}

          <button className="dre-pdf-btn" onClick={exportarPDF} disabled={semDados}>
            <Download size={13}/> Exportar PDF
          </button>
        </div>
      </div>

      {/* Aviso Lucro Presumido */}
      {regime === 'PRESUMIDO' && (
        <div className="dre-presumido-info">
          <strong>Lucro Presumido — Comércio/Indústria:</strong> IRPJ 15% s/ 8% da RB + Adicional 10% s/ base &gt; R$ 20k + CSLL 9% s/ 12% da RB + PIS 0,65% + COFINS 3%.
          Alíquota efetiva calculada: <strong>{totals.aliquotaEfetiva.toFixed(2)}%</strong> sobre receita bruta.
          Consulte seu contador para confirmar o enquadramento correto.
        </div>
      )}

      <div className="dre-grid">
        {/* DRE DOCUMENTO */}
        <div className="dre-doc">
          <div className="dre-doc-head">
            <div style={{display:'flex',alignItems:'center',gap:8}}>
              <Receipt size={16} style={{color:'#2563EB'}}/>
              Demonstrativo de Resultados
            </div>
            {!semDados && (
              <span className="dre-aliq-efetiva">
                Alíquota efetiva: {totals.aliquotaEfetiva.toFixed(2)}%
              </span>
            )}
          </div>

          {/* RECEITA BRUTA */}
          <DRELine label="(+) Receita Bruta de Vendas" value={totals.receitaBruta} bold fmt={fmt}/>

          {/* DEDUÇÕES */}
          <div className="dre-section-title">Deduções sobre a Receita</div>

          {/* Imposto por regime */}
          {regime === 'MEI' && (
            <DRELine label="(–) DAS — MEI (fixo mensal)" value={-totals.impostoTotal} neg fmt={fmt}/>
          )}
          {regime === 'SIMPLES' && (
            <DRELine label={`(–) DAS — Simples Nacional (${aliqSimples}%)`} value={-totals.impostoTotal} neg fmt={fmt}/>
          )}
          {regime === 'PRESUMIDO' && (
            <>
              <DRELine label="(–) Tributos — Lucro Presumido" value={-totals.impostoTotal} neg fmt={fmt}/>
              {/* Detalhamento */}
              <DRELine label={`Base de presunção 8% = ${fmt(totals.basePresuncao)}`} value={null} indent fmt={fmt} detalhe/>
              <DRELine label={`IRPJ 15% s/ base`} value={-totals.irpj} indent neg fmt={fmt}/>
              {totals.adicionalIRPJ > 0 && (
                <DRELine label="Adicional IRPJ 10%" value={-totals.adicionalIRPJ} indent neg fmt={fmt}/>
              )}
              <DRELine label="CSLL 9% s/ 12% da RB" value={-totals.csll} indent neg fmt={fmt}/>
              <DRELine label="PIS 0,65% + COFINS 3%" value={-(totals.receitaBruta * 0.0365)} indent neg fmt={fmt}/>
            </>
          )}

          <DRELine label="(–) Comissão Mercado Livre" value={-totals.comissaoML} neg fmt={fmt}/>
          <DRELine label="(–) Tarifas de Envio (ML)"  value={-totals.freteVendedor} neg fmt={fmt}/>

          {totals.perdaDevolucao > 0 && (
            <DRELine label="(–) Perdas por Devoluções" value={-totals.perdaDevolucao} neg fmt={fmt}/>
          )}
          {totals.perdaCancelamento > 0 && (
            <DRELine label="(–) Perdas por Cancelamentos" value={-totals.perdaCancelamento} neg fmt={fmt}/>
          )}

          <div className="dre-div"/>
          <DRELine label="(=) Receita Líquida" value={totals.receitaLiquida} bold fmt={fmt}/>
          <DRELine label="(–) Custo das Mercadorias Vendidas (CMV)" value={-totals.totalCMV} neg fmt={fmt}/>
          <div className="dre-div"/>
          <DRELine label="(=) Lucro Bruto Operacional" value={totals.lucroBruto} bold fmt={fmt} green={totals.lucroBruto >= 0}/>

          {/* DESPESAS OPERACIONAIS */}
          {totals.totalDespesas > 0 && (
            <>
              <div className="dre-section-title">Despesas Operacionais</div>
              {totals.totalAds  > 0 && <DRELine label="(–) Investimento em Ads"    value={-totals.totalAds}  neg fmt={fmt}/>}
              {totals.totalFull > 0 && <DRELine label="(–) Armazenagem Full ML"    value={-totals.totalFull} neg fmt={fmt}/>}
              {lancamentos.filter(l => !['CAIXA','ADS','FULL'].includes(l.categoria)).map(l => (
                <DRELine key={l.id} label={`(–) ${l.nome || 'Custo'}`} value={-l.valor} neg fmt={fmt}/>
              ))}
            </>
          )}

          {/* RESULTADO FINAL */}
          <div className="dre-result">
            <DRELine label="(=) Lucro Líquido Final" value={totals.lucroLiquido} bold fmt={fmt}
              green={totals.lucroLiquido >= 0} red={totals.lucroLiquido < 0}/>
            <div className="dre-margem">
              <span>Margem: {totals.margemPerc.toFixed(2)}%</span>
            </div>
          </div>

          {/* FLUXO DE CAIXA */}
          <div className="dre-caixa">
            <div className="dre-caixa-title">Fluxo de Caixa — Investimentos em Estoque</div>
            {lancamentos.filter(l => l.categoria==='CAIXA').map(l => (
              <DRELine key={l.id} label={l.nome || 'Investimento'} value={-l.valor} neg fmt={fmt}/>
            ))}
            {lancamentos.filter(l => l.categoria==='CAIXA').length === 0 && (
              <div style={{fontSize:11,color:'var(--tx-4)',fontStyle:'italic'}}>Nenhum lançamento</div>
            )}
            <div className="dre-caixa-total">
              <span>Dinheiro Disponível</span>
              <span>{fmt(totals.caixaFinal)}</span>
            </div>
          </div>
        </div>

        {/* LANÇAMENTOS MANUAIS */}
        <div>
          <IBox title="Ads & Marketing"       cat="ADS"       icon={<BarChart3 size={13}/>} items={lancamentos} onAdd={addItem} onUpd={updItem} onDel={delItem}/>
          <IBox title="Armazenagem Full ML"   cat="FULL"      icon={<BarChart3 size={13}/>} items={lancamentos} onAdd={addItem} onUpd={updItem} onDel={delItem}/>
          <IBox title="Fixas / Estrutura"     cat="FIXA"      icon={<BarChart3 size={13}/>} items={lancamentos} onAdd={addItem} onUpd={updItem} onDel={delItem}/>
          <IBox title="Logística / Embalagem" cat="LOGISTICA"  icon={<BarChart3 size={13}/>} items={lancamentos} onAdd={addItem} onUpd={updItem} onDel={delItem}/>
          <IBox title="Investimento Estoque"  cat="CAIXA"     icon={<Wallet    size={13}/>} items={lancamentos} onAdd={addItem} onUpd={updItem} onDel={delItem}/>

          <div className="dre-info">
            <Info size={14} style={{color:'#2563EB',flexShrink:0,marginTop:1}}/>
            <p>
              {regime === 'MEI' && <>MEI: imposto fixo (DAS mensal). Não incide % sobre receita.</>}
              {regime === 'SIMPLES' && <>Simples Nacional: informe a alíquota efetiva do seu anexo (I–V) conforme sua faixa de faturamento anual.</>}
              {regime === 'PRESUMIDO' && <>Lucro Presumido: tributos calculados automaticamente. Confirme com seu contador os percentuais aplicáveis ao seu CNAE.</>}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

// ── Sub-componentes ───────────────────────────────────────────────────────────

function DRELine({ label, value, bold, neg, green, red, fmt, indent, detalhe }: any) {
  if (detalhe) {
    return (
      <div className="dre-line indent">
        <span className="lbl">{label}</span>
      </div>
    );
  }
  const valColor = green ? 'var(--green)' : red ? 'var(--red)' : neg ? 'var(--red)' : 'var(--tx-2)';
  return (
    <div className={`dre-line ${bold ? 'bold' : ''} ${indent ? 'indent' : ''}`}>
      <span className="lbl">{label}</span>
      <span className="val" style={{color: valColor}}>{fmt(value)}</span>
    </div>
  );
}

function IBox({ title, cat, icon, items, onAdd, onUpd, onDel }: any) {
  const filtered = items.filter((i: any) => i.categoria === cat);
  return (
    <div className="ibox">
      <div className="ibox-head">
        <div className="ibox-title" style={{color:'#2563EB'}}>{icon}{title}</div>
        <button className="ibox-add" onClick={() => onAdd(cat)}><Plus size={14}/></button>
      </div>
      <div className="ibox-body">
        {filtered.map((item: any) => (
          <div key={item.id} className="ibox-row">
            <input className="ibox-name" type="text" placeholder="Nome do custo..."
              value={item.nome} onChange={e => onUpd(item.id,'nome',e.target.value.toUpperCase())}/>
            <div className="ibox-val-wrap">
              <span>R$</span>
              <input className="ibox-val" type="number" value={item.valor||''}
                onChange={e => onUpd(item.id,'valor',e.target.value)}/>
            </div>
            <button className="ibox-del" onClick={() => onDel(item.id)}><Trash2 size={13}/></button>
          </div>
        ))}
        {filtered.length === 0 && <div className="ibox-empty">Nenhum lançamento</div>}
      </div>
    </div>
  );
}