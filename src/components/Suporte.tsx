import React, { useState, useEffect } from 'react';
import { supabase } from '../lib/supabase';
import { MessageCircle, Send, CheckCircle2, Clock, AlertCircle, Plus, ChevronDown, ChevronUp } from 'lucide-react';

const ADMIN_EMAIL = 'nayaramarinhomartins@gmail.com'; // ← TROQUE pelo seu e-mail

interface Ticket {
  id: string;
  assunto: string;
  mensagem: string;
  status: 'aberto' | 'respondido' | 'fechado';
  created_at: string;
  resposta?: string;
  respondido_em?: string;
}

export function Suporte({ userId, userEmail }: { userId: string; userEmail: string }) {
  const [tickets, setTickets]       = useState<Ticket[]>([]);
  const [loading, setLoading]       = useState(true);
  const [enviando, setEnviando]     = useState(false);
  const [expandido, setExpandido]   = useState<string | null>(null);
  const [assunto, setAssunto]       = useState('');
  const [mensagem, setMensagem]     = useState('');
  const [sucesso, setSucesso]       = useState(false);
  const [erro, setErro]             = useState('');
  const isAdmin                     = userEmail === ADMIN_EMAIL;

  const carregarTickets = async () => {
    setLoading(true);
    const query = isAdmin
      ? supabase.from('sobra_quanto_suporte').select('*').order('created_at', { ascending: false })
      : supabase.from('sobra_quanto_suporte').select('*').eq('user_id', userId).order('created_at', { ascending: false });
    const { data } = await query;
    setTickets(data || []);
    setLoading(false);
  };

  useEffect(() => { carregarTickets(); }, [userId]);

  const enviarTicket = async () => {
    if (!assunto.trim() || !mensagem.trim()) { setErro('Preencha o assunto e a mensagem.'); return; }
    setEnviando(true); setErro('');
    const { error } = await supabase.from('sobra_quanto_suporte').insert({
      user_id: userId,
      user_email: userEmail,
      assunto: assunto.trim(),
      mensagem: mensagem.trim(),
      status: 'aberto',
    });
    setEnviando(false);
    if (error) { setErro('Erro ao enviar. Tente novamente.'); return; }
    setAssunto(''); setMensagem(''); setSucesso(true);
    setTimeout(() => setSucesso(false), 4000);
    carregarTickets();
  };

  const responderTicket = async (id: string, resposta: string) => {
    await supabase.from('sobra_quanto_suporte').update({
      resposta,
      status: 'respondido',
      respondido_em: new Date().toISOString(),
    }).eq('id', id);
    carregarTickets();
  };

  const fecharTicket = async (id: string) => {
    await supabase.from('sobra_quanto_suporte').update({ status: 'fechado' }).eq('id', id);
    carregarTickets();
  };

  const statusIcon = (s: string) => {
    if (s === 'aberto')      return <Clock size={13} style={{ color: 'var(--yellow)' }} />;
    if (s === 'respondido')  return <CheckCircle2 size={13} style={{ color: 'var(--green)' }} />;
    return <AlertCircle size={13} style={{ color: 'var(--tx-4)' }} />;
  };

  const statusLabel = (s: string) => ({
    aberto: 'Aguardando resposta', respondido: 'Respondido', fechado: 'Fechado'
  }[s] || s);

  const CSS = `
    .sup-wrap{max-width:720px;margin:0 auto}
    .sup-header{display:flex;align-items:center;gap:10px;margin-bottom:24px}
    .sup-title{font-size:17px;font-weight:700;color:var(--tx)}
    .sup-admin-badge{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;padding:3px 10px;border-radius:99px;background:rgba(37,99,235,.15);color:var(--blue-500);border:1px solid rgba(37,99,235,.25)}
    .sup-form{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);padding:20px;margin-bottom:20px}
    .sup-form-title{font-size:13px;font-weight:700;color:var(--tx);margin-bottom:14px;display:flex;align-items:center;gap:7px}
    .sup-field{margin-bottom:12px}
    .sup-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:var(--tx-3);margin-bottom:5px;display:block}
    .sup-input{width:100%;padding:9px 12px;background:var(--surface-2);border:1.5px solid var(--border);border-radius:var(--r);color:var(--tx);font-size:13px;font-family:inherit;outline:none;transition:border-color var(--t)}
    .sup-input:focus{border-color:var(--blue-500)}
    .sup-input::placeholder{color:var(--tx-4)}
    textarea.sup-input{resize:vertical;min-height:90px}
    .sup-send{display:flex;align-items:center;gap:6px;padding:9px 18px;background:var(--blue-600);color:#fff;border:none;border-radius:var(--r-lg);font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;transition:background var(--t)}
    .sup-send:hover{background:var(--blue-700)}
    .sup-send:disabled{opacity:.5;cursor:not-allowed}
    .sup-success{display:flex;align-items:center;gap:8px;background:var(--green-bg);border:1px solid var(--green-border);border-radius:var(--r);padding:10px 14px;font-size:13px;color:var(--green);font-weight:600;margin-top:10px}
    .sup-error{font-size:12px;color:var(--red);margin-top:6px}
    .sup-list-title{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--tx-3);margin-bottom:10px}
    .sup-ticket{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-lg);margin-bottom:8px;overflow:hidden;transition:border-color var(--t)}
    .sup-ticket.open-t{border-color:var(--yellow-border)}
    .sup-ticket.respondido-t{border-color:var(--green-border)}
    .sup-ticket-head{display:flex;align-items:center;gap:10px;padding:12px 14px;cursor:pointer;background:var(--surface)}
    .sup-ticket-head:hover{background:var(--surface-2)}
    .sup-ticket-assunto{font-size:13px;font-weight:600;color:var(--tx);flex:1}
    .sup-ticket-meta{font-size:11px;color:var(--tx-4);white-space:nowrap}
    .sup-ticket-status{display:flex;align-items:center;gap:4px;font-size:11px;font-weight:600;white-space:nowrap}
    .sup-ticket-body{padding:0 14px;max-height:0;overflow:hidden;transition:max-height .3s ease,padding .3s}
    .sup-ticket-body.exp{max-height:600px;padding:0 14px 14px}
    .sup-ticket-msg{font-size:13px;color:var(--tx-2);line-height:1.7;background:var(--surface-2);border-radius:var(--r);padding:10px 12px;margin-bottom:10px}
    .sup-ticket-label{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--tx-4);margin-bottom:4px}
    .sup-ticket-email{font-size:11px;color:var(--tx-4);margin-bottom:8px}
    .sup-resp-area{background:var(--green-bg);border:1px solid var(--green-border);border-radius:var(--r);padding:10px 12px;font-size:13px;color:var(--tx-2);line-height:1.7}
    .sup-resp-input{width:100%;padding:9px 12px;background:var(--surface-2);border:1.5px solid var(--border);border-radius:var(--r);color:var(--tx);font-size:13px;font-family:inherit;outline:none;resize:vertical;min-height:70px;transition:border-color var(--t)}
    .sup-resp-input:focus{border-color:var(--green)}
    .sup-resp-actions{display:flex;gap:8px;margin-top:8px}
    .sup-btn-resp{display:flex;align-items:center;gap:5px;padding:7px 14px;background:var(--green);color:#fff;border:none;border-radius:var(--r);font-size:12px;font-weight:700;cursor:pointer;font-family:inherit}
    .sup-btn-close{padding:7px 14px;background:var(--surface-3);color:var(--tx-3);border:1px solid var(--border);border-radius:var(--r);font-size:12px;font-weight:600;cursor:pointer;font-family:inherit}
    .sup-empty{text-align:center;padding:40px;color:var(--tx-4);font-size:13px}
  `;

  const [respostaTexto, setRespostaTexto] = useState<Record<string, string>>({});

  return (
    <div className="sup-wrap">
      <style>{CSS}</style>

      <div className="sup-header">
        <MessageCircle size={18} style={{ color: 'var(--blue-600)', flexShrink: 0 }} />
        <span className="sup-title">{isAdmin ? 'Suporte — Painel Admin' : 'Suporte'}</span>
        {isAdmin && <span className="sup-admin-badge">Admin</span>}
      </div>

      {/* Formulário de novo ticket — só para não-admin */}
      {!isAdmin && (
        <div className="sup-form">
          <div className="sup-form-title">
            <Plus size={15} style={{ color: 'var(--blue-500)' }} />
            Abrir chamado
          </div>
          <div className="sup-field">
            <label className="sup-label">Assunto</label>
            <input className="sup-input" placeholder="Ex: Dúvida sobre importação do relatório"
              value={assunto} onChange={e => setAssunto(e.target.value)} />
          </div>
          <div className="sup-field">
            <label className="sup-label">Mensagem</label>
            <textarea className="sup-input" placeholder="Descreva sua dúvida ou problema com detalhes..."
              value={mensagem} onChange={e => setMensagem(e.target.value)} />
          </div>
          {erro && <div className="sup-error">{erro}</div>}
          {sucesso && (
            <div className="sup-success">
              <CheckCircle2 size={15} /> Chamado enviado! Responderemos em breve.
            </div>
          )}
          <button className="sup-send" onClick={enviarTicket} disabled={enviando} style={{ marginTop: 12 }}>
            <Send size={13} /> {enviando ? 'Enviando...' : 'Enviar chamado'}
          </button>
        </div>
      )}

      {/* Lista de tickets */}
      <div className="sup-list-title">
        {isAdmin ? `Todos os chamados (${tickets.length})` : `Meus chamados (${tickets.length})`}
      </div>

      {loading ? (
        <div className="sup-empty">Carregando...</div>
      ) : tickets.length === 0 ? (
        <div className="sup-empty">
          {isAdmin ? 'Nenhum chamado aberto.' : 'Você ainda não abriu nenhum chamado.'}
        </div>
      ) : tickets.map(t => (
        <div key={t.id} className={`sup-ticket ${t.status}-t`}>
          <div className="sup-ticket-head" onClick={() => setExpandido(expandido === t.id ? null : t.id)}>
            {statusIcon(t.status)}
            <span className="sup-ticket-assunto">{t.assunto}</span>
            <span className="sup-ticket-meta">{new Date(t.created_at).toLocaleDateString('pt-BR')}</span>
            <span className="sup-ticket-status" style={{
              color: t.status === 'aberto' ? 'var(--yellow)' : t.status === 'respondido' ? 'var(--green)' : 'var(--tx-4)'
            }}>{statusLabel(t.status)}</span>
            {expandido === t.id ? <ChevronUp size={14} style={{ color: 'var(--tx-4)', flexShrink: 0 }} /> : <ChevronDown size={14} style={{ color: 'var(--tx-4)', flexShrink: 0 }} />}
          </div>
          <div className={`sup-ticket-body ${expandido === t.id ? 'exp' : ''}`}>
            {isAdmin && <div className="sup-ticket-email">De: {(t as any).user_email}</div>}
            <div className="sup-ticket-label">Mensagem</div>
            <div className="sup-ticket-msg">{t.mensagem}</div>

            {t.resposta ? (
              <>
                <div className="sup-ticket-label" style={{ color: 'var(--green)' }}>Resposta</div>
                <div className="sup-resp-area">{t.resposta}</div>
              </>
            ) : isAdmin && t.status !== 'fechado' ? (
              <>
                <div className="sup-ticket-label">Responder</div>
                <textarea className="sup-resp-input" placeholder="Digite sua resposta..."
                  value={respostaTexto[t.id] || ''}
                  onChange={e => setRespostaTexto(p => ({ ...p, [t.id]: e.target.value }))} />
                <div className="sup-resp-actions">
                  <button className="sup-btn-resp" onClick={() => responderTicket(t.id, respostaTexto[t.id] || '')}>
                    <Send size={12} /> Enviar resposta
                  </button>
                  <button className="sup-btn-close" onClick={() => fecharTicket(t.id)}>Fechar sem responder</button>
                </div>
              </>
            ) : null}

            {isAdmin && t.status !== 'fechado' && t.resposta && (
              <button className="sup-btn-close" style={{ marginTop: 8 }} onClick={() => fecharTicket(t.id)}>Fechar chamado</button>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}
