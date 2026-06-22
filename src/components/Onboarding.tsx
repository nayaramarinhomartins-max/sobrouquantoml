import React, { useState } from 'react';
import { Upload, DollarSign, BarChart2, CheckCircle2, ArrowRight, X } from 'lucide-react';

interface Props { onConcluir: () => void; }

const PASSOS = [
  {
    icon: <Upload size={28} />,
    cor: 'var(--blue-600)',
    titulo: 'Exporte o relatório do Mercado Livre',
    desc: 'Acesse mercadolivre.com.br → Vendas → Relatórios. Selecione o período desejado e exporte o arquivo .xlsx. Leva menos de 1 minuto.',
    dica: 'Dica: o arquivo se chama algo como "Vendas_Jan_2026.xlsx". Funciona com qualquer período.',
  },
  {
    icon: <DollarSign size={28} />,
    cor: 'var(--green)',
    titulo: 'Monte sua Planilha de Custos',
    desc: 'Crie uma planilha .xlsx com duas colunas. Na primeira linha coloque o cabeçalho: MLB na coluna A e Custo Unitário na coluna B. Nas linhas seguintes, preencha o código do anúncio (ex: MLB123456) e o valor que você pagou pelo produto (ex: 45.90). Atenção: sem essa linha de cabeçalho o sistema não processa os custos corretamente.',
    dica: 'Dica: você pode exportar a lista de MLBs direto do relatório do ML, colar na coluna A e preencher só os custos na coluna B.',
  },
  {
    icon: <Upload size={28} />,
    cor: '#7C3AED',
    titulo: 'Faça o upload dos dois arquivos',
    desc: 'Na barra lateral esquerda, clique em "Relatório ML" e selecione o arquivo do Mercado Livre. Depois clique em "Meus Custos" e selecione sua planilha de custos. O sistema processa tudo automaticamente.',
    dica: 'Dica: se quiser analisar mais de um mês, basta adicionar mais relatórios ML na fila.',
  },
  {
    icon: <BarChart2 size={28} />,
    cor: 'var(--yellow)',
    titulo: 'Configure a alíquota de imposto',
    desc: 'No topo da tela de Conciliação, informe sua alíquota de imposto (% sobre receita). Se for MEI, use 0 aqui e configure no DRE. Se for Simples Nacional, informe sua alíquota efetiva.',
    dica: 'Dica: não sabe a alíquota? Consulte seu contador ou verifique seu DAS no portal do Simples.',
  },
  {
    icon: <CheckCircle2 size={28} />,
    cor: 'var(--green)',
    titulo: 'Pronto! Seus números estão aqui.',
    desc: 'Explore as 5 abas do sistema: Conciliação (lucro por produto), Precificador (preço ideal), Advisor AI (análise inteligente), DRE Mensal (demonstrativo completo) e Histórico (evolução mês a mês).',
    dica: 'Dica: ative o Advisor AI para ver quais produtos estão consumindo sua margem sem você saber.',
  },
];

export function Onboarding({ onConcluir }: Props) {
  const [passo, setPasso] = useState(0);
  const atual = PASSOS[passo];
  const ultimo = passo === PASSOS.length - 1;

  const CSS = `
    .ob-overlay{position:fixed;inset:0;background:rgba(0,0,0,.65);z-index:9000;display:flex;align-items:center;justify-content:center;padding:20px;animation:fi .2s ease}
    .ob-card{background:var(--surface);border:1px solid var(--border);border-radius:20px;width:100%;max-width:480px;overflow:hidden;box-shadow:0 32px 80px rgba(0,0,0,.3)}
    .ob-top{height:4px;background:var(--border)}
    .ob-progress{height:4px;background:var(--blue-600);transition:width .4s ease}
    .ob-body{padding:32px 28px 24px}
    .ob-icon{width:60px;height:60px;border-radius:16px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;background:var(--surface-2);border:1px solid var(--border)}
    .ob-step-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--tx-4);margin-bottom:6px}
    .ob-titulo{font-size:18px;font-weight:800;color:var(--tx);letter-spacing:-.4px;line-height:1.3;margin-bottom:12px}
    .ob-desc{font-size:14px;color:var(--tx-2);line-height:1.75;margin-bottom:14px}
    .ob-dica{background:var(--surface-2);border:1px solid var(--border);border-left:3px solid var(--blue-500);border-radius:0 var(--r) var(--r) 0;padding:10px 14px;font-size:12px;color:var(--tx-3);line-height:1.6;margin-bottom:24px}
    .ob-dots{display:flex;gap:6px;margin-bottom:20px}
    .ob-dot{width:24px;height:4px;border-radius:2px;background:var(--border);transition:background .3s,width .3s}
    .ob-dot.ativo{background:var(--blue-600);width:32px}
    .ob-dot.feito{background:var(--green)}
    .ob-footer{display:flex;align-items:center;justify-content:space-between;gap:12px}
    .ob-skip{background:none;border:none;font-size:13px;color:var(--tx-4);cursor:pointer;font-family:inherit;transition:color var(--t)}
    .ob-skip:hover{color:var(--tx-3)}
    .ob-next{display:flex;align-items:center;gap:7px;padding:10px 22px;background:var(--blue-600);color:#fff;border:none;border-radius:var(--r-lg);font-size:14px;font-weight:700;cursor:pointer;font-family:inherit;transition:background var(--t)}
    .ob-next:hover{background:var(--blue-700)}
    .ob-next.green{background:var(--green)}
    .ob-next.green:hover{background:#059669}
    .ob-close{position:absolute;top:14px;right:14px;background:none;border:none;cursor:pointer;color:var(--tx-4);display:flex;padding:4px}
    .ob-close:hover{color:var(--tx)}
  `;

  return (
    <div className="ob-overlay">
      <style>{CSS}</style>
      <div className="ob-card" style={{ position: 'relative' }}>
        <button className="ob-close" onClick={onConcluir}><X size={16} /></button>
        <div className="ob-top">
          <div className="ob-progress" style={{ width: `${((passo + 1) / PASSOS.length) * 100}%` }} />
        </div>
        <div className="ob-body">
          <div className="ob-icon" style={{ borderColor: atual.cor }}>
            <span style={{ color: atual.cor }}>{atual.icon}</span>
          </div>
          <div className="ob-step-label">Passo {passo + 1} de {PASSOS.length}</div>
          <div className="ob-titulo">{atual.titulo}</div>
          <div className="ob-desc">{atual.desc}</div>
          <div className="ob-dica">{atual.dica}</div>
          <div className="ob-dots">
            {PASSOS.map((_, i) => (
              <div key={i} className={`ob-dot ${i === passo ? 'ativo' : i < passo ? 'feito' : ''}`} />
            ))}
          </div>
          <div className="ob-footer">
            <button className="ob-skip" onClick={onConcluir}>Pular tutorial</button>
            <button
              className={`ob-next ${ultimo ? 'green' : ''}`}
              onClick={() => ultimo ? onConcluir() : setPasso(p => p + 1)}
            >
              {ultimo ? <><CheckCircle2 size={15} /> Começar agora</> : <>Próximo <ArrowRight size={15} /></>}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
