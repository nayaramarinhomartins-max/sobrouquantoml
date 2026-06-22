import React from "react";
import { ProductData } from "../lib/engine";

interface ProductsTableProps {
  data: ProductData[];
}

const fmt = (v: number) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v);

export function ProductsTable({ data }: ProductsTableProps) {
  const CSS = `
    .pt-empty{padding:48px 24px;text-align:center;color:var(--tx-4);font-size:13px;font-style:italic}
    .pt-wrap{overflow-x:auto}
    .pt-table{width:100%;border-collapse:collapse;font-size:12px}
    .pt-table thead tr{background:var(--surface-2)}
    .pt-table th{padding:10px 14px;text-align:left;font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--tx-3);border-bottom:1px solid var(--border);white-space:nowrap}
    .pt-table th.r{text-align:right}
    .pt-table th.c{text-align:center}
    .pt-table td{padding:10px 14px;border-bottom:1px solid var(--border);color:var(--tx-2);vertical-align:middle}
    .pt-table tbody tr{transition:background .1s}
    .pt-table tbody tr:hover{background:var(--surface-2)}
    .pt-table tbody tr:last-child td{border-bottom:none}
    .pt-sku{font-size:12px;font-weight:700;color:var(--tx);margin-bottom:2px}
    .pt-name{font-size:11px;color:var(--tx-4);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:280px}
    .pt-mono{font-family:'SF Mono','Fira Code',monospace;font-size:12px}
    .pt-badge{display:inline-block;padding:2px 8px;border-radius:99px;font-size:9px;font-weight:700;letter-spacing:.04em;white-space:nowrap}
    .pt-badge.alta{background:var(--green-bg);color:var(--green);border:1px solid var(--green-border)}
    .pt-badge.estavel{background:var(--yellow-bg);color:var(--yellow);border:1px solid var(--yellow-border)}
    .pt-badge.critico{background:var(--red-bg);color:var(--red);border:1px solid var(--red)}
  `;

  if (!data || data.length === 0) {
    return (
      <>
        <style>{CSS}</style>
        <div className="pt-empty">Nenhum dado encontrado para os filtros selecionados.</div>
      </>
    );
  }

  return (
    <>
      <style>{CSS}</style>
      <div className="pt-wrap">
        <table className="pt-table">
          <thead>
            <tr>
              <th style={{ minWidth: 220 }}>SKU / Produto</th>
              <th className="c" style={{ minWidth: 60 }}>Qtd</th>
              <th style={{ minWidth: 130 }}>Receita Bruta</th>
              <th style={{ minWidth: 130 }}>Lucro Líquido</th>
              <th style={{ minWidth: 80 }}>Margem</th>
              <th className="r" style={{ minWidth: 130 }}>Status</th>
            </tr>
          </thead>
          <tbody>
            {data.map((p, i) => {
              const badgeClass = p.margin >= 15 ? 'alta' : p.margin >= 0 ? 'estavel' : 'critico';
              const badgeLabel = p.margin >= 15 ? 'ALTA PERFORMANCE' : p.margin >= 0 ? 'ESTÁVEL' : 'CRÍTICO';
              const profitColor = p.profit >= 0 ? 'var(--green)' : 'var(--red)';
              const marginColor = p.margin >= 15 ? 'var(--green)' : p.margin >= 0 ? 'var(--yellow)' : 'var(--red)';

              return (
                <tr key={`${p.mlb}-${i}`}>
                  <td>
                    <div className="pt-sku">{p.sku || p.mlb}</div>
                    <div className="pt-name" title={p.name}>{p.name}</div>
                  </td>
                  <td style={{ textAlign: 'center', color: 'var(--tx-3)' }} className="pt-mono">
                    {p.quantity}
                  </td>
                  <td className="pt-mono" style={{ color: 'var(--tx)', fontWeight: 600 }}>
                    {fmt(p.revenue)}
                  </td>
                  <td className="pt-mono" style={{ color: profitColor, fontWeight: 700 }}>
                    {fmt(p.profit)}
                  </td>
                  <td className="pt-mono" style={{ color: marginColor, fontWeight: 700 }}>
                    {p.margin.toFixed(2)}%
                  </td>
                  <td style={{ textAlign: 'right' }}>
                    <span className={`pt-badge ${badgeClass}`}>{badgeLabel}</span>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </>
  );
}