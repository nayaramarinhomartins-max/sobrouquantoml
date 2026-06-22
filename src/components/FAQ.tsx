import React, { useState } from 'react';
import { ChevronDown, HelpCircle } from 'lucide-react';

const PERGUNTAS = [
  {
    q: 'O Sobrou Quanto ML usa API do Mercado Livre?',
    a: 'Não. Essa é exatamente a nossa vantagem. Lemos direto do relatório .xlsx que você exporta do painel do ML. Isso significa dados 100% reais, sem defasagem de API, sem falha de integração e sem risco de o ML bloquear o acesso.'
  },
  {
    q: 'Preciso compartilhar minha senha do Mercado Livre?',
    a: 'Nunca. Você apenas exporta o relatório de vendas no formato Excel (.xlsx) diretamente do painel do ML e faz o upload aqui. Nenhuma credencial sua é necessária.'
  },
  {
    q: 'Como funciona o cálculo do lucro líquido?',
    a: 'O sistema lê cada linha do relatório e calcula: Receita Bruta − CMV (seu custo de produto) − Comissão ML − Frete cobrado pelo ML − Imposto (pela alíquota que você informa) − Devoluções e Cancelamentos = Lucro Líquido real.'
  },
  {
    q: 'O que é a Planilha de Custos e como monto ela?',
    a: 'É uma planilha com duas colunas. Na primeira linha, coloque o cabeçalho: MLB na coluna A e Custo Unitário na coluna B. Nas linhas seguintes, preencha o código do anúncio (ex: MLB123456) e o valor que você pagou pelo produto. Atenção: sem a linha de cabeçalho o sistema pula o primeiro produto da lista. Uma terceira coluna com o nome do produto é opcional e não interfere no cálculo.'
  },
  {
    q: 'Posso importar mais de um mês no mesmo upload?',
    a: 'Sim! Você pode adicionar múltiplos relatórios mensais na fila de importação. O sistema mescla todos os dados e calcula o período completo de uma vez.'
  },
  {
    q: 'O DRE contempla qual regime tributário?',
    a: 'Os três principais: MEI (DAS fixo mensal), Simples Nacional (alíquota efetiva sobre receita) e Lucro Presumido (IRPJ + adicional + CSLL + PIS + COFINS calculados automaticamente). Você escolhe o regime na aba DRE.'
  },
  {
    q: 'O Precificador usa dados reais das taxas do ML?',
    a: 'Sim. As tabelas de comissão e frete do ML ficam salvas no banco de dados e são atualizadas periodicamente. O sistema busca a faixa correta de preço e peso para calcular o custo real de cada venda antes de você precificar.'
  },
  {
    q: 'Meus dados ficam salvos entre sessões?',
    a: 'Sim. Cada mês processado fica salvo no histórico. Você pode acessar qualquer mês anterior, ver os dados de conciliação, DRE e produtos sem precisar reimportar nada.'
  },
  {
    q: 'O Advisor AI analisa o quê exatamente?',
    a: 'Ele lê os dados brutos do relatório ML e identifica: produtos vendendo no prejuízo, devoluções por SKU com prejuízo real calculado, clientes recorrentes (retenção B2C/B2B), melhor dia da semana para vender, frete divergente por peso declarado errado, e cancelamentos em trânsito.'
  },
  {
    q: 'Posso cancelar quando quiser?',
    a: 'Sim. Sem fidelidade, sem multa. O cancelamento é feito pelo suporte e a conta fica ativa até o fim do período pago.'
  },
];

export function FAQ() {
  const [aberto, setAberto] = useState<number | null>(null);

  const CSS = `
    .faq-wrap{max-width:720px;margin:0 auto}
    .faq-header{display:flex;align-items:center;gap:10px;margin-bottom:24px}
    .faq-title{font-size:17px;font-weight:700;color:var(--tx)}
    .faq-item{border:1px solid var(--border);border-radius:var(--r-lg);margin-bottom:8px;overflow:hidden;transition:border-color var(--t)}
    .faq-item.open{border-color:var(--blue-500)}
    .faq-btn{width:100%;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 16px;background:var(--surface);border:none;cursor:pointer;text-align:left;font-family:inherit;transition:background var(--t)}
    .faq-btn:hover{background:var(--surface-2)}
    .faq-q{font-size:13px;font-weight:600;color:var(--tx-2);line-height:1.5}
    .faq-item.open .faq-q{color:var(--tx)}
    .faq-chevron{flex-shrink:0;color:var(--tx-4);transition:transform .25s}
    .faq-item.open .faq-chevron{transform:rotate(180deg);color:var(--blue-500)}
    .faq-body{padding:0 16px;max-height:0;overflow:hidden;transition:max-height .3s ease,padding .3s ease}
    .faq-item.open .faq-body{max-height:300px;padding:0 16px 14px}
    .faq-a{font-size:13px;color:var(--tx-3);line-height:1.7;border-top:1px solid var(--border);padding-top:12px}
    .faq-empty{text-align:center;padding:40px;color:var(--tx-4);font-size:13px}
  `;

  return (
    <div className="faq-wrap">
      <style>{CSS}</style>
      <div className="faq-header">
        <HelpCircle size={18} style={{ color: 'var(--blue-600)', flexShrink: 0 }} />
        <span className="faq-title">Perguntas frequentes</span>
      </div>
      {PERGUNTAS.map((item, i) => (
        <div key={i} className={`faq-item ${aberto === i ? 'open' : ''}`}>
          <button className="faq-btn" onClick={() => setAberto(aberto === i ? null : i)}>
            <span className="faq-q">{item.q}</span>
            <ChevronDown size={16} className="faq-chevron" />
          </button>
          <div className="faq-body">
            <p className="faq-a">{item.a}</p>
          </div>
        </div>
      ))}
    </div>
  );
}
