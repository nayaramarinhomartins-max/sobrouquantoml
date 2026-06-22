import React, { useState, useEffect, useMemo } from 'react';
import { supabase } from '../lib/supabase';
import {
  TrendingUp, TrendingDown, Minus, BarChart2,
  Calendar, ArrowUpRight, Loader, PackageOpen
} from 'lucide-react';

// ─── Tipos ───────────────────────────────────────────────────────────────────

interface MesRow {
  id: string;
  referencia: string;
  label: string;
  receita_bruta: number;
  total_cmv: number;
  lucro_liquido: number;
  margem_percentual: number;
  total_vendas: number;
  perda_devolucao: number;
  perda_cancelamento: number;
}

interface ProdutoRow {
  mlb: string; sku: string; nome: string;
  preco: number; quantidade: number; receita: number;
  custo: number; lucro: number; margem: number;
}

type DadosCarregados = {
  label: string;
  stats: {
    receitaBruta: number; totalCMV: number; totalImposto: number;
    comissaoML: number; freteVendedor: number; mercadoAds: number;
    totalReembolsos: number; lucroLiquido: number;
    perdaDevolucao: number; perdaCancelamento: number;
  };
  vendasSaudaveis: Array<{
    mlb: string; sku: string; name: string; price: number;
    quantity: number; revenue: number; tax: number; fees: number;
    refund: number; cost: number; profit: number; margin: number;
  }>;
  dadosParaAdvisor: any[];
  prejuizos: any[];
};

interface Props {
  userId: string;
  onCarregarMes: (dados: DadosCarregados) => void;
}

// ─── Helpers ─────────────────────────────────────────────────────────────────

type MetricaKey = 'receita_bruta' | 'lucro_liquido' | 'margem_percentual' | 'total_cmv';

const METRICAS: { key: MetricaKey; label: string; cor: string; corFill: string; isPct?: boolean }[] = [
  { key: 'receita_bruta',     label: 'Receita Bruta', cor: '#3B82F6', corFill: 'rgba(59,130,246,.08)' },
  { key: 'lucro_liquido',     label: 'Lucro Líquido', cor: '#10B981', corFill: 'rgba(16,185,129,.08)' },
  { key: 'margem_percentual', label: 'Margem %',      cor: '#F59E0B', corFill: 'rgba(245,158,11,.08)', isPct: true },
  { key: 'total_cmv',         label: 'CMV',           cor: '#EF4444', corFill: 'rgba(239,68,68,.08)' },
];

const fmt    = (v: number) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v);
const fmtK   = (v: number) => {
  if (Math.abs(v) >= 1_000_000) return `R$ ${(v / 1_000_000).toFixed(1)}M`;
  if (Math.abs(v) >= 10_000)    return `R$ ${(v / 1_000).toFixed(1)}k`;
  return fmt(v);
};
const fmtPct = (v: number) => `${v.toFixed(1)}%`;

// ─── CSS ─────────────────────────────────────────────────────────────────────

const CSS = `
  .hist-wrap{max-width:1100px;margin:0 auto;font-family:'Inter',system-ui,sans-serif}
  .hist-kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
  @media(max-width:760px){.hist-kpis{grid-template-columns:repeat(2,1fr)}}
  .kpi-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);padding:16px;cursor:pointer;transition:border-color .15s;position:relative;overflow:hidden}
  .kpi-card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:var(--cor);transform:scaleX(0);transition:transform .2s}
  .kpi-card.ativa{border-color:var(--cor)}.kpi-card.ativa::after{transform:scaleX(1)}
  .kpi-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--tx-3);margin-bottom:8px;display:flex;align-items:center;gap:6px}
  .kpi-dot{width:7px;height:7px;border-radius:50%;background:var(--cor);flex-shrink:0}
  .kpi-value{font-size:20px;font-weight:800;color:var(--tx);line-height:1;margin-bottom:6px;letter-spacing:-.5px}
  .kpi-delta{display:flex;align-items:center;gap:4px;font-size:11px;font-weight:600}
  .kpi-delta.up{color:#10B981}.kpi-delta.down{color:#EF4444}.kpi-delta.flat{color:var(--tx-4)}
  .hist-chart-wrap{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);padding:20px 16px 16px;margin-bottom:20px;position:relative}
  .hist-chart-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px}
  .hist-chart-title{font-size:13px;font-weight:700;color:var(--tx);display:flex;align-items:center;gap:8px}
  .hist-range{font-size:11px;color:var(--tx-4);display:flex;align-items:center;gap:4px}
  .hist-tooltip{background:var(--surface);border:1px solid var(--border-2);border-radius:var(--r-lg);padding:10px 14px;pointer-events:none;box-shadow:0 4px 20px rgba(0,0,0,.15);min-width:160px;position:absolute;top:36px;z-index:10}
  .hist-tooltip-title{font-weight:700;color:var(--tx);margin-bottom:8px;font-size:12px;text-transform:capitalize}
  .hist-tooltip-row{display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:4px;font-size:11px}
  .hist-tooltip-row:last-child{margin-bottom:0}
  .hist-tooltip-lbl{display:flex;align-items:center;gap:5px;color:var(--tx-3)}
  .hist-tooltip-val{font-weight:600;color:var(--tx)}
  .hist-table-wrap{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);overflow:hidden}
  .hist-table-head{display:flex;align-items:center;padding:14px 18px;border-bottom:1px solid var(--border);background:var(--surface-2)}
  .hist-table-title{font-size:12px;font-weight:700;color:var(--tx-2);display:flex;align-items:center;gap:8px}
  table.htbl{width:100%;border-collapse:collapse;font-size:12px}
  table.htbl th{padding:10px 16px;text-align:left;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--tx-4);border-bottom:1px solid var(--border);background:var(--surface-2);white-space:nowrap}
  table.htbl th:not(:first-child){text-align:right}
  table.htbl td{padding:12px 16px;border-bottom:1px solid var(--border);color:var(--tx-2)}
  table.htbl td:not(:first-child){text-align:right;font-variant-numeric:tabular-nums}
  table.htbl tr:last-child td{border-bottom:none}
  table.htbl tbody tr:hover td{background:var(--surface-2)}
  .htbl-mes{font-weight:600;color:var(--tx);text-transform:capitalize}
  .htbl-badge{font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;background:#2563EB;color:#fff;padding:2px 6px;border-radius:4px;margin-left:8px;vertical-align:middle}
  .htbl-btn{display:inline-flex;align-items:center;gap:4px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:#2563EB;background:none;border:none;cursor:pointer;padding:4px 8px;border-radius:6px;transition:background .14s;font-family:inherit}
  .htbl-btn:hover{background:var(--blue-50)}.htbl-btn:disabled{opacity:.5;cursor:not-allowed}
  .hist-empty{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px 20px;color:var(--tx-4);gap:12px;text-align:center}
  .hist-empty-title{font-size:14px;font-weight:700;color:var(--tx-3)}
  .hist-empty-sub{font-size:12px;max-width:280px;line-height:1.6}
  .hist-mini-empty{font-size:12px;color:var(--tx-4);text-align:center;padding:20px 0}
  @keyframes spin-h{to{transform:rotate(360deg)}}
`;

// ─── Componente ──────────────────────────────────────────────────────────────

export function Historico({ userId, onCarregarMes }: Props) {
  const [meses, setMeses]           = useState<MesRow[]>([]);
  const [loading, setLoading]       = useState(true);
  const [loadingMes, setLoadingMes] = useState<string | null>(null);
  const [ativas, setAtivas]         = useState<Set<MetricaKey>>(
    new Set(['receita_bruta', 'lucro_liquido', 'margem_percentual', 'total_cmv'])
  );
  const [hovIdx, setHovIdx]         = useState<number | null>(null);

  useEffect(() => {
    if (!userId) return;
    setLoading(true);
    supabase
      .from('sobra_quanto_meses')
      .select('*')
      .eq('user_id', userId)
      .order('referencia', { ascending: true })
      .limit(12)
      .then(({ data }) => {
        if (data) setMeses(data as MesRow[]);
        setLoading(false);
      });
  }, [userId]);

  // Busca produtos do mês no Supabase e chama o callback com dados completos
  const handleCarregarMes = async (mes: MesRow) => {
    setLoadingMes(mes.id);
    try {
      const { data: produtos } = await supabase
        .from('sobra_quanto_produtos')
        .select('*')
        .eq('mes_id', mes.id)
        .eq('user_id', userId);

      const vendasSaudaveis = (produtos || []).map((p: ProdutoRow) => ({
        mlb: p.mlb, sku: p.sku, name: p.nome,
        price: p.preco, quantity: p.quantidade,
        revenue: p.receita, tax: 0, fees: 0, refund: 0,
        cost: p.custo, profit: p.lucro, margin: p.margem,
      }));

      onCarregarMes({
        label: mes.label,
        stats: {
          receitaBruta:      mes.receita_bruta,
          totalCMV:          mes.total_cmv,
          totalImposto:      0,
          comissaoML:        0,
          freteVendedor:     0,
          mercadoAds:        0,
          totalReembolsos:   mes.perda_devolucao + mes.perda_cancelamento,
          lucroLiquido:      mes.lucro_liquido,
          perdaDevolucao:    mes.perda_devolucao,
          perdaCancelamento: mes.perda_cancelamento,
        },
        vendasSaudaveis,
        dadosParaAdvisor: [],
        prejuizos: [],
      });
    } finally {
      setLoadingMes(null);
    }
  };

  // ─── Gráfico ─────────────────────────────────────────────────────────────

  const W = 680, H = 240;
  const PAD = { top: 20, right: 24, bottom: 36, left: 56 };
  const gW = W - PAD.left - PAD.right;
  const gH = H - PAD.top - PAD.bottom;

  const { escalaY, xStep, pontos, ticksY } = useMemo(() => {
    if (meses.length < 2) return { escalaY: () => 0, xStep: 0, pontos: {}, ticksY: [] };

    const valoresNum = meses.flatMap(m =>
      Array.from(ativas)
        .filter(k => !METRICAS.find(x => x.key === k)?.isPct)
        .map(k => m[k] as number)
    );
    const raw_min = Math.min(...valoresNum, 0);
    const raw_max = Math.max(...valoresNum, 1);
    const pad     = (raw_max - raw_min) * 0.15 || 100;
    const yMin    = raw_min - pad;
    const yMax    = raw_max + pad;

    const escalaY = (v: number) =>
      PAD.top + gH - Math.max(0, Math.min(1, (v - yMin) / (yMax - yMin))) * gH;

    const xStep = gW / Math.max(meses.length - 1, 1);

    const pontos: Record<string, { x: number; y: number }[]> = {};
    for (const m of METRICAS) {
      if (!ativas.has(m.key)) continue;
      pontos[m.key] = meses.map((mes, i) => {
        const v = mes[m.key] as number;
        if (m.isPct) {
          const y = PAD.top + gH - Math.max(0, Math.min(1, v / 50)) * gH;
          return { x: PAD.left + i * xStep, y };
        }
        return { x: PAD.left + i * xStep, y: escalaY(v) };
      });
    }

    const range = yMax - yMin;
    const step  = Math.pow(10, Math.floor(Math.log10(range / 4))) || 1;
    const ticks: number[] = [];
    const start = Math.ceil(yMin / step) * step;
    for (let v = start; v <= yMax; v += step) ticks.push(v);

    return { escalaY, xStep, pontos, ticksY: ticks.slice(0, 6) };
  }, [meses, ativas]);

  const linha = (pts: { x: number; y: number }[]) =>
    pts.reduce((acc, p, i) => {
      if (i === 0) return `M ${p.x} ${p.y}`;
      const prev = pts[i - 1];
      const cpx  = (prev.x + p.x) / 2;
      return `${acc} C ${cpx} ${prev.y} ${cpx} ${p.y} ${p.x} ${p.y}`;
    }, '');

  const area = (pts: { x: number; y: number }[]) =>
    `${linha(pts)} L ${pts[pts.length - 1].x} ${PAD.top + gH} L ${pts[0].x} ${PAD.top + gH} Z`;

  // Deltas vs mês anterior
  const ultimo    = meses[meses.length - 1];
  const penultimo = meses[meses.length - 2];
  const delta = (key: MetricaKey): number | null => {
    if (!ultimo || !penultimo) return null;
    const a = penultimo[key] as number;
    const b = ultimo[key]    as number;
    return a === 0 ? null : ((b - a) / Math.abs(a)) * 100;
  };

  const toggleMetrica = (k: MetricaKey) =>
    setAtivas(prev => {
      const next = new Set(prev);
      if (next.has(k)) { if (next.size > 1) next.delete(k); }
      else next.add(k);
      return next;
    });

  // ─── Render ──────────────────────────────────────────────────────────────

  if (loading) {
    return (
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '80px 0', gap: 10 }}>
        <style>{CSS}</style>
        <Loader size={18} style={{ color: '#2563EB', animation: 'spin-h .6s linear infinite' }} />
        <span style={{ fontSize: 13, color: 'var(--tx-3)' }}>Carregando histórico...</span>
      </div>
    );
  }

  if (meses.length === 0) {
    return (
      <div className="hist-wrap">
        <style>{CSS}</style>
        <div className="hist-empty">
          <PackageOpen size={32} style={{ color: 'var(--tx-4)' }} />
          <div className="hist-empty-title">Nenhum histórico ainda</div>
          <div className="hist-empty-sub">
            Importe o Relatório ML e processe pelo menos um mês para ver a evolução aqui.
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="hist-wrap">
      <style>{CSS}</style>

      {/* KPI Cards — clicáveis para ligar/desligar linha no gráfico */}
      <div className="hist-kpis">
        {METRICAS.map(m => {
          const v     = ultimo ? (ultimo[m.key] as number) : 0;
          const d     = delta(m.key);
          const ativo = ativas.has(m.key);
          return (
            <div key={m.key}
              className={`kpi-card ${ativo ? 'ativa' : ''}`}
              style={{ '--cor': m.cor } as React.CSSProperties}
              onClick={() => toggleMetrica(m.key)}
            >
              <div className="kpi-label">
                <span className="kpi-dot" />{m.label}
              </div>
              <div className="kpi-value">
                {m.isPct ? fmtPct(v) : fmtK(v)}
              </div>
              {d !== null
                ? <div className={`kpi-delta ${d > 0.5 ? 'up' : d < -0.5 ? 'down' : 'flat'}`}>
                    {d > 0.5 ? <TrendingUp size={11} /> : d < -0.5 ? <TrendingDown size={11} /> : <Minus size={11} />}
                    {d > 0 ? '+' : ''}{d.toFixed(1)}% vs mês anterior
                  </div>
                : <div className="kpi-delta flat"><Minus size={11} /> primeiro mês</div>
              }
            </div>
          );
        })}
      </div>

      {/* Gráfico de linha */}
      <div className="hist-chart-wrap">
        <div className="hist-chart-header">
          <div className="hist-chart-title">
            <BarChart2 size={15} style={{ color: '#2563EB' }} />
            Evolução mensal — {meses.length} meses
          </div>
          {meses.length >= 2 && (
            <div className="hist-range">
              <Calendar size={11} />
              {meses[0].label} → {ultimo.label}
            </div>
          )}
        </div>

        {meses.length < 2
          ? <div className="hist-mini-empty">Importe pelo menos 2 meses para visualizar a evolução.</div>
          : (
            <div style={{ position: 'relative' }}>
              <svg width="100%" viewBox={`0 0 ${W} ${H}`}
                style={{ overflow: 'visible', cursor: 'crosshair', display: 'block' }}
                onMouseLeave={() => setHovIdx(null)}
                onMouseMove={e => {
                  const rect = (e.currentTarget as SVGSVGElement).getBoundingClientRect();
                  const px   = (e.clientX - rect.left) / rect.width * W;
                  setHovIdx(Math.max(0, Math.min(meses.length - 1, Math.round((px - PAD.left) / xStep))));
                }}
              >
                {ticksY.map((v, i) => {
                  const y = escalaY(v);
                  return (
                    <g key={i}>
                      <line x1={PAD.left} y1={y} x2={PAD.left + gW} y2={y}
                        stroke="var(--border)" strokeWidth={0.5} />
                      <text x={PAD.left - 6} y={y} textAnchor="end" dominantBaseline="central"
                        fontSize={9} fill="var(--tx-4)" fontFamily="Inter, system-ui, sans-serif">
                        {fmtK(v).replace('R$ ', '')}
                      </text>
                    </g>
                  );
                })}

                {meses.map((m, i) => (
                  <text key={i} x={PAD.left + i * xStep} y={PAD.top + gH + 18}
                    textAnchor="middle" fontSize={9}
                    fill={hovIdx === i ? 'var(--tx-2)' : 'var(--tx-4)'}
                    fontWeight={hovIdx === i ? 600 : 400}
                    fontFamily="Inter, system-ui, sans-serif">
                    {m.label.slice(0, 3)}/{m.referencia.slice(2, 4)}
                  </text>
                ))}

                {METRICAS.filter(m => ativas.has(m.key)).map(m => {
                  const pts = pontos[m.key];
                  if (!pts || pts.length < 2) return null;
                  return (
                    <g key={m.key}>
                      <path d={area(pts)} fill={m.corFill} stroke="none" />
                      <path d={linha(pts)} fill="none" stroke={m.cor} strokeWidth={2}
                        strokeLinejoin="round" strokeLinecap="round" />
                      {pts.map((p, i) => (
                        <circle key={i} cx={p.x} cy={p.y}
                          r={hovIdx === i ? 5 : 3}
                          fill={m.cor} stroke="var(--surface)" strokeWidth={2}
                          style={{ transition: 'r .1s' }} />
                      ))}
                    </g>
                  );
                })}

                {hovIdx !== null && (
                  <line x1={PAD.left + hovIdx * xStep} y1={PAD.top}
                    x2={PAD.left + hovIdx * xStep} y2={PAD.top + gH}
                    stroke="var(--border-2)" strokeWidth={1} strokeDasharray="3 3" />
                )}
              </svg>

              {hovIdx !== null && meses[hovIdx] && (() => {
                const m    = meses[hovIdx];
                const xPct = ((PAD.left + hovIdx * xStep) / W) * 100;
                return (
                  <div className="hist-tooltip"
                    style={xPct <= 60 ? { left: `${xPct + 2}%` } : { right: `${100 - xPct + 2}%` }}>
                    <div className="hist-tooltip-title">{m.label}</div>
                    {METRICAS.filter(mt => ativas.has(mt.key)).map(mt => (
                      <div key={mt.key} className="hist-tooltip-row">
                        <span className="hist-tooltip-lbl">
                          <span style={{ width: 6, height: 6, borderRadius: '50%', background: mt.cor, display: 'inline-block' }} />
                          {mt.label}
                        </span>
                        <span className="hist-tooltip-val">
                          {mt.isPct ? fmtPct(m[mt.key] as number) : fmt(m[mt.key] as number)}
                        </span>
                      </div>
                    ))}
                  </div>
                );
              })()}
            </div>
          )
        }
      </div>

      {/* Tabela histórico */}
      <div className="hist-table-wrap">
        <div className="hist-table-head">
          <div className="hist-table-title">
            <Calendar size={14} style={{ color: '#2563EB' }} />
            Todos os meses
          </div>
        </div>
        <div style={{ overflowX: 'auto' }}>
          <table className="htbl">
            <thead>
              <tr>
                <th>Mês</th><th>Receita</th><th>CMV</th>
                <th>Lucro</th><th>Margem</th><th>Vendas</th><th></th>
              </tr>
            </thead>
            <tbody>
              {[...meses].reverse().map((m, i) => {
                const isLast = i === 0;
                return (
                  <tr key={m.id} style={isLast ? { background: 'var(--blue-50)' } : {}}>
                    <td>
                      <span className="htbl-mes">{m.label}</span>
                      {isLast && <span className="htbl-badge">Atual</span>}
                    </td>
                    <td>{fmt(m.receita_bruta)}</td>
                    <td style={{ color: 'var(--red)' }}>{fmt(m.total_cmv)}</td>
                    <td style={{ color: m.lucro_liquido >= 0 ? '#10B981' : 'var(--red)', fontWeight: 600 }}>
                      {fmt(m.lucro_liquido)}
                    </td>
                    <td style={{ color: m.margem_percentual >= 10 ? '#10B981' : m.margem_percentual >= 0 ? '#F59E0B' : 'var(--red)' }}>
                      {fmtPct(m.margem_percentual)}
                    </td>
                    <td>{m.total_vendas}</td>
                    <td>
                      <button className="htbl-btn" disabled={loadingMes === m.id}
                        onClick={() => handleCarregarMes(m)}>
                        {loadingMes === m.id
                          ? <Loader size={11} style={{ animation: 'spin-h .6s linear infinite' }} />
                          : <ArrowUpRight size={11} />}
                        {loadingMes === m.id ? 'Carregando...' : 'Carregar'}
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}