import React, { useState, useEffect } from 'react';
import { BarChart2, Link, Settings, Users, TrendingUp, Copy, Check, Plus, X } from 'lucide-react';

const LS_KEY = 'sqads_';
const sg = (key: string) => { try { return JSON.parse(localStorage.getItem(LS_KEY + key) || 'null'); } catch { return null; } };
const ss = (key: string, val: any) => localStorage.setItem(LS_KEY + key, JSON.stringify(val));

interface Metricas { total: number | null; trial: number | null; pagantes: number | null; }
interface ChartPoint { label: string; val: number; }
interface Usuario { nome: string; email: string; data: string; plano: string; origem: string; }

export function AdsDashboard() {
  const [metricas, setMetricas]   = useState<Metricas>(sg('metricas') || { total: null, trial: null, pagantes: null });
  const [pixel, setPixel]         = useState<string>(localStorage.getItem(LS_KEY + 'pixel') || '');
  const [pixelInput, setPixelInput] = useState<string>(localStorage.getItem(LS_KEY + 'pixel') || '');
  const [urlBase, setUrlBase]     = useState<string>(localStorage.getItem(LS_KEY + 'urlbase') || '');
  const [chartData, setChartData] = useState<ChartPoint[]>(sg('chartdata') || []);
  const [users, setUsers]         = useState<Usuario[]>(sg('users') || []);
  const [modal, setModal]         = useState<string | null>(null);
  const [copied, setCopied]       = useState<string | null>(null);

  // Form states
  const [mEdit, setMEdit]         = useState<Metricas>({ total: null, trial: null, pagantes: null });
  const [chartRaw, setChartRaw]   = useState<string>('');
  const [uForm, setUForm]         = useState({ nome: '', email: '', data: '', plano: 'trial', origem: '' });
  const [utmSrc, setUtmSrc]       = useState(''); const [utmMed, setUtmMed] = useState('');
  const [utmCam, setUtmCam]       = useState(''); const [utmCon, setUtmCon] = useState('');

  useEffect(() => {
    if (chartData.length) setChartRaw(chartData.map(d => `${d.label}: ${d.val}`).join('\n'));
  }, []);

  const conv = (metricas.trial != null && metricas.pagantes != null && (metricas.trial + metricas.pagantes) > 0)
    ? ((metricas.pagantes / (metricas.trial + metricas.pagantes)) * 100).toFixed(1) + '%'
    : '—';

  const utmUrl = (() => {
    if (!urlBase || !utmSrc) return '';
    let u = urlBase + '?utm_source=' + encodeURIComponent(utmSrc);
    if (utmMed) u += '&utm_medium=' + encodeURIComponent(utmMed);
    if (utmCam) u += '&utm_campaign=' + encodeURIComponent(utmCam);
    if (utmCon) u += '&utm_content=' + encodeURIComponent(utmCon);
    return u;
  })();

  const pixelCode = pixel ? `<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;
s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}
(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','${pixel}');fbq('track','PageView');
<\/script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=${pixel}&ev=PageView&noscript=1"/></noscript>
<!-- End Meta Pixel Code -->` : '';

  const copy = (text: string, id: string) => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(id);
      setTimeout(() => setCopied(null), 2000);
    });
  };

  const salvarMetricas = () => {
    setMetricas(mEdit);
    ss('metricas', mEdit);
    setModal(null);
  };

  const aplicarPixel = () => {
    setPixel(pixelInput);
    localStorage.setItem(LS_KEY + 'pixel', pixelInput);
  };

  const salvarUrlBase = (v: string) => {
    setUrlBase(v);
    localStorage.setItem(LS_KEY + 'urlbase', v);
  };

  const salvarGrafico = () => {
    const data = chartRaw.trim().split('\n').filter(Boolean).map(l => {
      const [lbl, val] = l.split(':');
      return { label: (lbl || '').trim(), val: parseInt((val || '0').trim()) || 0 };
    }).filter(d => d.label);
    setChartData(data);
    ss('chartdata', data);
    setModal(null);
  };

  const adicionarUsuario = () => {
    if (!uForm.nome || !uForm.email) return;
    const novo = [...users, { ...uForm, data: uForm.data || new Date().toLocaleDateString('pt-BR') }];
    setUsers(novo);
    ss('users', novo);
    setUForm({ nome: '', email: '', data: '', plano: 'trial', origem: '' });
    setModal(null);
  };

  const checklist = [
    { label: 'URL da landing configurada',    desc: 'Para gerar links de campanha',           done: !!urlBase },
    { label: 'Pixel do Facebook configurado', desc: 'Para rastrear conversões',               done: !!pixel,  warn: !pixel },
    { label: 'Política de Privacidade',       desc: 'Exigida pelo Facebook para aprovar ads', done: false,    warn: true },
    { label: 'Link UTM criado',               desc: 'Para rastrear origem dos cadastros',     done: !!utmUrl },
    { label: 'Conta no Meta Ads Manager',     desc: 'Para criar e veicular anúncios',         done: false },
  ];

  const maxBar = Math.max(...chartData.map(d => d.val), 1);

  const CSS = `
    .ads-wrap{max-width:1100px;margin:0 auto}
    .ads-section{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--tx-3);margin:24px 0 12px;display:flex;align-items:center;gap:8px}
    .ads-section::after{content:'';flex:1;height:1px;background:var(--border)}
    .ads-metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:4px}
    .ads-mc{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px;position:relative;overflow:hidden;cursor:pointer;transition:box-shadow .2s}
    .ads-mc:hover{box-shadow:0 4px 16px rgba(0,0,0,.1)}
    .ads-mc::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;border-radius:12px 12px 0 0}
    .ads-mc.b::before{background:var(--blue-500)} .ads-mc.g::before{background:var(--green)} .ads-mc.y::before{background:var(--yellow)} .ads-mc.p::before{background:#7C3AED}
    .ads-mc-lbl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--tx-3);margin-bottom:8px}
    .ads-mc-val{font-size:26px;font-weight:900;letter-spacing:-1px;color:var(--tx);line-height:1}
    .ads-mc-val.g{color:var(--green)} .ads-mc-val.y{color:var(--yellow)}
    .ads-mc-sub{font-size:11px;color:var(--tx-4);margin-top:5px}
    .ads-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:12px}
    .ads-card-title{font-size:13px;font-weight:700;color:var(--tx);margin-bottom:14px;display:flex;align-items:center;gap:7px}
    .ads-grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
    .ads-field{margin-bottom:10px}
    .ads-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:var(--tx-3);margin-bottom:4px;display:block}
    .ads-input{width:100%;padding:9px 12px;border:1.5px solid var(--border);border-radius:8px;font-family:inherit;font-size:13px;color:var(--tx);background:var(--surface-2);outline:none;transition:border-color var(--t)}
    .ads-input:focus{border-color:var(--blue-500);background:var(--surface)}
    .ads-input::placeholder{color:var(--tx-4)}
    .ads-row{display:flex;gap:8px;align-items:flex-end}
    .ads-btn{padding:9px 16px;background:var(--blue-600);color:#fff;border:none;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer;font-family:inherit;transition:background var(--t);white-space:nowrap;display:flex;align-items:center;gap:5px}
    .ads-btn:hover{background:var(--blue-700)}
    .ads-btn-s{padding:9px 14px;background:var(--surface-2);color:var(--tx-2);border:1.5px solid var(--border);border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;font-family:inherit;transition:all var(--t);white-space:nowrap;display:flex;align-items:center;gap:5px}
    .ads-btn-s:hover{border-color:var(--blue-500);color:var(--blue-500)}
    .ads-btn-s.ok{border-color:var(--green);color:var(--green)}
    .ads-pixel-ok{background:var(--green-bg);border:1px solid var(--green-border);border-radius:8px;padding:10px 14px;font-size:12px;color:var(--green);font-weight:600;margin-bottom:10px;display:flex;align-items:center;gap:7px}
    .ads-pixel-warn{background:var(--yellow-bg);border:1px solid var(--yellow-border);border-radius:8px;padding:10px 14px;font-size:12px;color:var(--yellow);font-weight:600;margin-bottom:10px;display:flex;align-items:center;gap:7px}
    .ads-code{width:100%;padding:9px 12px;background:var(--surface-2);border:1.5px solid var(--border);border-radius:8px;font-size:11px;font-family:monospace;color:var(--tx);resize:none;outline:none}
    .ads-link-row{display:flex;gap:7px;align-items:center;margin-bottom:7px}
    .ads-link-tag{font-size:10px;font-weight:700;padding:3px 9px;border-radius:99px;flex-shrink:0}
    .ads-link-tag.l{background:var(--blue-50);color:var(--blue-600)} .ads-link-tag.t{background:var(--green-bg);color:var(--green)}
    .ads-link-val{flex:1;padding:8px 11px;background:var(--surface-2);border:1.5px solid var(--border);border-radius:8px;font-size:12px;color:var(--tx);font-family:inherit;outline:none}
    .ads-utm-result{background:var(--surface-2);border:1.5px solid var(--border);border-radius:8px;padding:10px 12px;font-size:12px;color:var(--tx);word-break:break-all;line-height:1.6;min-height:40px}
    .ads-chart{display:flex;align-items:flex-end;gap:7px;height:140px;padding-bottom:20px;margin-top:8px}
    .ads-bar-g{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px}
    .ads-bar{width:100%;border-radius:4px 4px 0 0;background:linear-gradient(180deg,var(--blue-500),#60A5FA);position:relative}
    .ads-bar-lbl{font-size:9px;color:var(--tx-4);font-weight:600;position:absolute;bottom:-17px;left:0;right:0;text-align:center}
    .ads-bar-v{font-size:10px;font-weight:700;color:var(--tx);margin-bottom:2px}
    .ads-check{display:flex;flex-direction:column;gap:7px}
    .ads-check-item{display:flex;align-items:flex-start;gap:9px;padding:9px 11px;border-radius:8px;border:1px solid var(--border);background:var(--surface-2)}
    .ads-check-item.done{background:var(--green-bg);border-color:var(--green-border)}
    .ads-check-item.warn{background:var(--yellow-bg);border-color:var(--yellow-border)}
    .ads-check-dot{width:16px;height:16px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:9px;font-weight:800;margin-top:1px}
    .ads-check-dot.done{background:var(--green);color:#fff} .ads-check-dot.warn{background:var(--yellow);color:#fff} .ads-check-dot.pend{background:var(--border-2);color:var(--tx-4)}
    .ads-check-text h4{font-size:12px;font-weight:600;color:var(--tx);margin-bottom:1px}
    .ads-check-text p{font-size:11px;color:var(--tx-3);line-height:1.4}
    .ads-users-tbl{width:100%;border-collapse:collapse;font-size:12px}
    .ads-users-tbl th{padding:8px 10px;text-align:left;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--tx-3);border-bottom:1px solid var(--border)}
    .ads-users-tbl td{padding:9px 10px;border-bottom:1px solid var(--border);color:var(--tx)}
    .ads-users-tbl tr:last-child td{border-bottom:none}
    .ads-plan{font-size:10px;font-weight:700;padding:2px 8px;border-radius:99px;text-transform:uppercase}
    .ads-plan.trial{background:var(--surface-3);color:var(--tx-3)} .ads-plan.mensal{background:var(--blue-50);color:var(--blue-700)} .ads-plan.anual{background:var(--yellow-bg);color:#92400E}
    .ads-modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.55);backdrop-filter:blur(4px);z-index:9999;display:flex;align-items:center;justify-content:center;padding:20px}
    .ads-modal{background:var(--surface);border-radius:16px;width:100%;max-width:460px;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.3)}
    .ads-modal-h{padding:20px 22px 0;display:flex;align-items:center;justify-content:space-between}
    .ads-modal-title{font-size:15px;font-weight:800;color:var(--tx)}
    .ads-modal-close{background:none;border:none;cursor:pointer;color:var(--tx-3);padding:2px 6px;font-size:18px;line-height:1}
    .ads-modal-body{padding:18px 22px}
    .ads-modal-foot{padding:0 22px 20px;display:flex;gap:8px;justify-content:flex-end}
    .hint{font-size:11px;color:var(--tx-4);line-height:1.6;margin-top:6px}
  `;

  return (
    <div className="ads-wrap">
      <style>{CSS}</style>

      {/* MÉTRICAS */}
      <div className="ads-section">Métricas de usuários</div>
      <div className="ads-metrics">
        {[
          { cls:'b', lbl:'Total cadastros', val: metricas.total ?? '—', sub:'todos os usuários' },
          { cls:'y', lbl:'Em trial',        val: metricas.trial ?? '—', sub:'7 dias grátis', vcls:'y' },
          { cls:'g', lbl:'Pagantes',        val: metricas.pagantes ?? '—', sub:'plano ativo', vcls:'g' },
          { cls:'p', lbl:'Conversão trial→pago', val: conv, sub:'calculado automaticamente' },
        ].map((m, i) => (
          <div key={i} className={`ads-mc ${m.cls}`} onClick={() => { setMEdit(metricas); setModal('metricas'); }}>
            <div className="ads-mc-lbl">{m.lbl}</div>
            <div className={`ads-mc-val ${m.vcls || ''}`}>{m.val as any}</div>
            <div className="ads-mc-sub">{m.sub}</div>
          </div>
        ))}
      </div>

      <div className="ads-grid2" style={{ marginTop: 12 }}>
        {/* PIXEL */}
        <div className="ads-card">
          <div className="ads-card-title"><Settings size={14} style={{ color: 'var(--blue-500)' }}/>Pixel do Facebook</div>
          {pixel
            ? <div className="ads-pixel-ok"><Check size={13}/>Pixel configurado: <strong>{pixel}</strong></div>
            : <div className="ads-pixel-warn">⚠ Pixel não configurado ainda</div>
          }
          <div className="ads-row">
            <div className="ads-field" style={{ flex:1, marginBottom:0 }}>
              <label className="ads-label">ID do Pixel</label>
              <input className="ads-input" value={pixelInput} onChange={e => setPixelInput(e.target.value)} placeholder="Ex: 1234567890123"/>
            </div>
            <button className="ads-btn" style={{ marginBottom:0 }} onClick={aplicarPixel}>Aplicar</button>
          </div>
          <p className="hint">Onde achar: <strong>Meta Business → Gerenciador de Eventos → seu Pixel</strong></p>
          {pixel && (
            <div style={{ marginTop: 12 }}>
              <label className="ads-label">Código para colar no &lt;head&gt; da landing</label>
              <textarea className="ads-code" rows={5} value={pixelCode} readOnly/>
              <button className="ads-btn-s" style={{ marginTop:6, width:'100%', justifyContent:'center' }}
                onClick={() => copy(pixelCode, 'pixel')} >
                {copied === 'pixel' ? <><Check size={12}/>Copiado!</> : <><Copy size={12}/>Copiar código</>}
              </button>
            </div>
          )}
        </div>

        {/* LINKS */}
        <div className="ads-card">
          <div className="ads-card-title"><Link size={14} style={{ color: 'var(--blue-500)' }}/>Links de campanha</div>
          <div className="ads-field">
            <label className="ads-label">URL base do site</label>
            <input className="ads-input" value={urlBase} onChange={e => salvarUrlBase(e.target.value)} placeholder="https://seudominio.com.br"/>
          </div>
          <div className="ads-link-row">
            <span className="ads-link-tag l">Landing</span>
            <input className="ads-link-val" value={urlBase} readOnly placeholder="Configure a URL acima"/>
            <button className="ads-btn-s" onClick={() => copy(urlBase, 'land')}>
              {copied === 'land' ? <Check size={12}/> : <Copy size={12}/>}
            </button>
          </div>
          <div className="ads-link-row">
            <span className="ads-link-tag t">Trial</span>
            <input className="ads-link-val" value={urlBase ? urlBase + '#trial' : ''} readOnly placeholder="Configure a URL acima"/>
            <button className="ads-btn-s" onClick={() => copy(urlBase + '#trial', 'trial')}>
              {copied === 'trial' ? <Check size={12}/> : <Copy size={12}/>}
            </button>
          </div>
          <div style={{ marginTop: 12 }}>
            <label className="ads-label" style={{ marginBottom:8 }}>Construtor de UTM</label>
            <div className="ads-grid2" style={{ gap:7, marginBottom:8 }}>
              <div><label className="ads-label">Fonte</label><input className="ads-input" value={utmSrc} onChange={e=>setUtmSrc(e.target.value)} placeholder="facebook"/></div>
              <div><label className="ads-label">Mídia</label><input className="ads-input" value={utmMed} onChange={e=>setUtmMed(e.target.value)} placeholder="cpc"/></div>
              <div><label className="ads-label">Campanha</label><input className="ads-input" value={utmCam} onChange={e=>setUtmCam(e.target.value)} placeholder="lancamento"/></div>
              <div><label className="ads-label">Conteúdo</label><input className="ads-input" value={utmCon} onChange={e=>setUtmCon(e.target.value)} placeholder="criativo-1"/></div>
            </div>
            <div className="ads-utm-result">{utmUrl || <span style={{ color:'var(--tx-4)' }}>Preencha fonte e URL para gerar o link</span>}</div>
            {utmUrl && <button className="ads-btn-s" style={{ marginTop:6, width:'100%', justifyContent:'center' }} onClick={() => copy(utmUrl, 'utm')}>
              {copied === 'utm' ? <><Check size={12}/>Copiado!</> : <><Copy size={12}/>Copiar link UTM</>}
            </button>}
          </div>
        </div>
      </div>

      <div className="ads-grid2">
        {/* GRÁFICO */}
        <div className="ads-card">
          <div className="ads-card-title">
            <TrendingUp size={14} style={{ color: 'var(--blue-500)' }}/>Crescimento de cadastros
            <button className="ads-btn-s" style={{ marginLeft:'auto', fontSize:11, padding:'4px 10px' }} onClick={() => setModal('chart')}>Editar dados</button>
          </div>
          {chartData.length === 0
            ? <div style={{ display:'flex', flexDirection:'column', alignItems:'center', justifyContent:'center', height:120, gap:8, color:'var(--tx-4)', fontSize:13 }}>
                <BarChart2 size={28} style={{ opacity:.3 }}/> Clique em "Editar dados" para começar
              </div>
            : <div className="ads-chart">
                {chartData.map((d, i) => (
                  <div key={i} className="ads-bar-g">
                    <div className="ads-bar-v">{d.val}</div>
                    <div className="ads-bar" style={{ height: `${Math.max((d.val/maxBar)*100, 5)}%` }}>
                      <span className="ads-bar-lbl">{d.label}</span>
                    </div>
                  </div>
                ))}
              </div>
          }
        </div>

        {/* CHECKLIST */}
        <div className="ads-card">
          <div className="ads-card-title">✓ Checklist pré-campanha</div>
          <div className="ads-check">
            {checklist.map((it, i) => (
              <div key={i} className={`ads-check-item ${it.done ? 'done' : it.warn ? 'warn' : ''}`}>
                <div className={`ads-check-dot ${it.done ? 'done' : it.warn ? 'warn' : 'pend'}`}>{it.done ? '✓' : it.warn ? '!' : '·'}</div>
                <div className="ads-check-text"><h4>{it.label}</h4><p>{it.desc}</p></div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* USUÁRIOS */}
      <div className="ads-section">Últimos cadastros</div>
      <div className="ads-card">
        <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center', marginBottom:14 }}>
          <span style={{ fontSize:12, color:'var(--tx-3)' }}>Registro manual enquanto não há integração automática</span>
          <button className="ads-btn" style={{ fontSize:12, padding:'7px 13px' }} onClick={() => setModal('user')}>
            <Plus size={13}/>Adicionar
          </button>
        </div>
        <table className="ads-users-tbl">
          <thead><tr><th>Nome</th><th>E-mail</th><th>Data</th><th>Plano</th><th>Origem</th></tr></thead>
          <tbody>
            {users.length === 0
              ? <tr><td colSpan={5} style={{ textAlign:'center', color:'var(--tx-4)', padding:24 }}>Nenhum usuário registrado ainda.</td></tr>
              : [...users].reverse().map((u, i) => (
                  <tr key={i}>
                    <td><strong>{u.nome}</strong></td>
                    <td style={{ color:'var(--tx-3)' }}>{u.email}</td>
                    <td style={{ color:'var(--tx-3)' }}>{u.data}</td>
                    <td><span className={`ads-plan ${u.plano}`}>{u.plano}</span></td>
                    <td style={{ color:'var(--tx-3)' }}>{u.origem || '—'}</td>
                  </tr>
                ))
            }
          </tbody>
        </table>
      </div>

      {/* MODAIS */}
      {modal && (
        <div className="ads-modal-overlay" onClick={e => { if (e.target === e.currentTarget) setModal(null); }}>
          <div className="ads-modal">
            <div className="ads-modal-h">
              <span className="ads-modal-title">
                {modal === 'metricas' ? 'Editar métricas' : modal === 'chart' ? 'Dados do gráfico' : 'Adicionar usuário'}
              </span>
              <button className="ads-modal-close" onClick={() => setModal(null)}>×</button>
            </div>

            {modal === 'metricas' && (
              <>
                <div className="ads-modal-body" style={{ display:'flex', flexDirection:'column', gap:12 }}>
                  {[{id:'total',lbl:'Total de cadastros'},{id:'trial',lbl:'Em trial'},{id:'pagantes',lbl:'Pagantes'}].map(f => (
                    <div key={f.id}>
                      <label className="ads-label">{f.lbl}</label>
                      <input className="ads-input" type="number" value={(mEdit as any)[f.id] ?? ''}
                        onChange={e => setMEdit(p => ({ ...p, [f.id]: parseInt(e.target.value) || 0 }))}/>
                    </div>
                  ))}
                </div>
                <div className="ads-modal-foot">
                  <button className="ads-btn-s" onClick={() => setModal(null)}>Cancelar</button>
                  <button className="ads-btn" onClick={salvarMetricas}>Salvar</button>
                </div>
              </>
            )}

            {modal === 'chart' && (
              <>
                <div className="ads-modal-body">
                  <p className="hint" style={{ marginBottom:10 }}>Um dado por linha no formato <strong>Mês: Número</strong><br/>Ex: Jan: 5 / Fev: 12 / Mar: 20</p>
                  <textarea className="ads-input" rows={9} value={chartRaw} onChange={e => setChartRaw(e.target.value)}/>
                </div>
                <div className="ads-modal-foot">
                  <button className="ads-btn-s" onClick={() => setModal(null)}>Cancelar</button>
                  <button className="ads-btn" onClick={salvarGrafico}>Atualizar</button>
                </div>
              </>
            )}

            {modal === 'user' && (
              <>
                <div className="ads-modal-body" style={{ display:'flex', flexDirection:'column', gap:10 }}>
                  {[{id:'nome',lbl:'Nome',ph:'Nome do usuário',type:'text'},{id:'email',lbl:'E-mail',ph:'email@exemplo.com',type:'email'}].map(f => (
                    <div key={f.id}>
                      <label className="ads-label">{f.lbl}</label>
                      <input className="ads-input" type={f.type} placeholder={f.ph}
                        value={(uForm as any)[f.id]} onChange={e => setUForm(p => ({ ...p, [f.id]: e.target.value }))}/>
                    </div>
                  ))}
                  <div><label className="ads-label">Data</label><input className="ads-input" type="date" value={uForm.data} onChange={e => setUForm(p => ({ ...p, data: e.target.value }))}/></div>
                  <div>
                    <label className="ads-label">Plano</label>
                    <select className="ads-input" value={uForm.plano} onChange={e => setUForm(p => ({ ...p, plano: e.target.value }))}>
                      <option value="trial">Trial</option><option value="mensal">Mensal</option><option value="anual">Anual</option>
                    </select>
                  </div>
                  <div><label className="ads-label">Origem</label><input className="ads-input" placeholder="Ex: Facebook Ads, Orgânico" value={uForm.origem} onChange={e => setUForm(p => ({ ...p, origem: e.target.value }))}/></div>
                </div>
                <div className="ads-modal-foot">
                  <button className="ads-btn-s" onClick={() => setModal(null)}>Cancelar</button>
                  <button className="ads-btn" onClick={adicionarUsuario}>Adicionar</button>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
