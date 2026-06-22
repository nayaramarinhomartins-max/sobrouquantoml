import React, { useState, useRef, useEffect } from "react";
import {
  Calculator, Brain, FileText, Upload, LogOut,
  Sun, Moon, RotateCcw, XCircle, Package, Percent,
  ChevronRight, BarChart2, Search, Filter, CheckCircle2,
  DollarSign, ShoppingBag, Loader, TrendingUp, Plus, Trash2,
  AlertCircle, HelpCircle, MessageCircle, BookOpen
} from "lucide-react";
import { ProductsTable } from "./components/ProductsTable";
import { Advisor }        from "./components/Advisor";
import { DRE }            from "./components/DRE";
import { Precificacao }   from "./components/Precificacao";
import { Historico }      from "./components/Historico";
import { FAQ }            from "./components/FAQ";
import { Suporte }        from "./components/Suporte";
import { Onboarding }     from "./components/Onboarding";
import { AdsDashboard }   from "./components/AdsDashboard";
import { Login }          from "./pages/Login";
import { parseExcelFile, processData, splitDataByMonth, FinancialSummary } from "./lib/engine";
import { supabase } from "./lib/supabase";

const ADMIN_EMAIL = 'nayaramarinhomartins@gmail.com';

type Tab = 'concile' | 'precificacao' | 'advisor' | 'dre' | 'historico' | 'faq' | 'suporte' | 'ads';

interface MLFile { name: string; data: any[]; }
interface MonthResult { ref: string; label: string; summary: FinancialSummary; }

const ONBOARDING_KEY = 'sq_onboarding_done';

export default function App() {
  const [user, setUser]               = useState<any>(null);
  const [userProfile, setUserProfile] = useState<any>(null);
  const [checkingAuth, setCheckingAuth] = useState(true);
  const [theme, setTheme]             = useState<'light'|'dark'>('dark');
  const [activeTab, setActiveTab]     = useState<Tab>('concile');
  const [results, setResults]         = useState<FinancialSummary|null>(null);
  const [allMonths, setAllMonths]     = useState<MonthResult[]>([]);
  const [selectedMonthRef, setSelectedMonthRef] = useState<string>('');
  const [mlFiles, setMlFiles]         = useState<MLFile[]>([]);
  const [costData, setCostData]       = useState<any[]>([]);
  const [taxRate, setTaxRate]         = useState(0);
  const [filterMode, setFilterMode]   = useState<'all'|'loss'|'top'|'alta'>('all');
  const [searchTerm, setSearchTerm]   = useState("");
  const [showFilters, setShowFilters] = useState(false);
  const [costFileName, setCostFileName] = useState("");
  const [saving, setSaving]           = useState(false);
  const [processing, setProcessing]   = useState(false);
  const [mesHistoricoLabel, setMesHistoricoLabel] = useState<string | null>(null);
  const [alertaFechado, setAlertaFechado] = useState(false);
  const [showImpostoInfo, setShowImpostoInfo] = useState(false);
  const [showKpiInfo, setShowKpiInfo] = useState<string | null>(null);
  const [showOnboarding, setShowOnboarding] = useState(false);
  const [showPasswordReset, setShowPasswordReset] = useState(false);
  const [newPassword, setNewPassword]       = useState('');
  const [newPasswordConfirm, setNewPasswordConfirm] = useState('');
  const [passwordResetMsg, setPasswordResetMsg] = useState('');
  const [passwordResetLoading, setPasswordResetLoading] = useState(false);

  const mlRef   = useRef<HTMLInputElement>(null);
  const costRef = useRef<HTMLInputElement>(null);

  const aguardandoCustos = mlFiles.length > 0 && costData.length === 0;

  useEffect(() => { document.documentElement.setAttribute('data-theme', theme); }, [theme]);

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      setUser(session?.user ?? null);
      if (session?.user) {
        loadProfile(session.user.id);
        // Mostra onboarding apenas na primeira vez
        if (!localStorage.getItem(ONBOARDING_KEY)) {
          setShowOnboarding(true);
        }
      }
      setCheckingAuth(false);
    });
    const { data: { subscription } } = supabase.auth.onAuthStateChange((event, session) => {
      setUser(session?.user ?? null);
      if (session?.user) loadProfile(session.user.id);
      if (event === 'PASSWORD_RECOVERY') setShowPasswordReset(true);
    });
    return () => subscription.unsubscribe();
  }, []);

  const loadProfile = async (uid: string) => {
    try {
      const { data } = await supabase
        .from('sobra_quanto_users').select('*').eq('id', uid).single();
      if (data) setUserProfile(data);
    } catch {
      // usuario sem perfil ainda — app roda com defaults (plano trial)
    }
  };

  const handleLogout = async () => {
    if (confirm('Sair e limpar dados da sessão?')) {
      await supabase.auth.signOut();
      setUser(null); setUserProfile(null); setResults(null);
      setMlFiles([]); setCostData([]); setCostFileName('');
      setMesHistoricoLabel(null);
    }
  };

  const handlePasswordReset = async () => {
    setPasswordResetMsg('');
    if (newPassword.length < 6) { setPasswordResetMsg('A senha precisa ter pelo menos 6 caracteres.'); return; }
    if (newPassword !== newPasswordConfirm) { setPasswordResetMsg('As senhas não coincidem.'); return; }
    setPasswordResetLoading(true);
    try {
      const { error } = await supabase.auth.updateUser({ password: newPassword });
      if (error) { setPasswordResetMsg(error.message || 'Erro ao redefinir. Tente novamente.'); return; }
      setShowPasswordReset(false);
      setNewPassword(''); setNewPasswordConfirm('');
    } catch {
      setPasswordResetMsg('Erro de conexão. Tente novamente.');
    } finally {
      setPasswordResetLoading(false);
    }
  };

  const concluirOnboarding = () => {
    localStorage.setItem(ONBOARDING_KEY, '1');
    setShowOnboarding(false);
  };

  const refToLabel = (ref: string): string => {
    if (!ref || ref === 'sem-data') return 'Período';
    const [year, month] = ref.split('-');
    return new Date(parseInt(year), parseInt(month) - 1, 1)
      .toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' });
  };

  const salvarMesData = async (summary: FinancialSummary, ref: string, label: string) => {
    if (!user) return;
    const s = summary.stats;
    const { data: mes, error } = await supabase
      .from('sobra_quanto_meses')
      .upsert({
        user_id: user.id, referencia: ref, label,
        receita_bruta: s.receitaBruta, total_cmv: s.totalCMV,
        total_imposto: s.totalImposto, comissao_ml: s.comissaoML,
        frete_vendedor: s.freteVendedor, lucro_liquido: s.lucroLiquido,
        margem_percentual: s.receitaBruta > 0 ? (s.lucroLiquido/s.receitaBruta)*100 : 0,
        total_vendas: summary.vendasSaudaveis.reduce((acc, p) => acc + p.quantity, 0),
        perda_devolucao: s.perdaDevolucao, perda_cancelamento: s.perdaCancelamento,
        atualizado_em: new Date().toISOString()
      }, { onConflict: 'user_id,referencia' })
      .select().single();
    if (error || !mes) return;
    await supabase.from('sobra_quanto_produtos').delete().eq('mes_id', mes.id);
    const prods = summary.vendasSaudaveis.map(p => ({
      user_id: user.id, mes_id: mes.id,
      mlb: p.mlb, sku: p.sku, nome: p.name,
      preco: p.price, quantidade: p.quantity,
      receita: p.revenue, custo: p.cost,
      lucro: p.profit, margem: p.margin
    }));
    if (prods.length) await supabase.from('sobra_quanto_produtos').insert(prods);
  };

  const run = async (files = mlFiles, cost = costData, tax = taxRate) => {
    if (files.length === 0 || cost.length === 0) return;
    setProcessing(true);
    setSaving(true);
    try {
      const mlMesclado = files.flatMap(f => f.data);
      const byMonth    = splitDataByMonth(mlMesclado);

      if (byMonth.size <= 1) {
        // Um único mês ou sem info de data — comportamento original
        const summary = processData(mlMesclado, cost, tax);
        const agora   = new Date();
        const ref     = `${agora.getFullYear()}-${String(agora.getMonth()+1).padStart(2,'0')}`;
        const label   = agora.toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' });
        setResults(summary);
        setAllMonths([]);
        setSelectedMonthRef('');
        setMesHistoricoLabel(null);
        setAlertaFechado(false);
        await salvarMesData(summary, ref, label);
      } else {
        // Múltiplos meses — processa e salva cada um separadamente
        const monthResults: MonthResult[] = [];
        for (const [ref, rows] of byMonth.entries()) {
          const label   = refToLabel(ref);
          const summary = processData(rows, cost, tax);
          monthResults.push({ ref, label, summary });
          await salvarMesData(summary, ref, label);
        }
        const latest = monthResults[monthResults.length - 1];
        setAllMonths(monthResults);
        setSelectedMonthRef(latest.ref);
        setResults(latest.summary);
        setMesHistoricoLabel(null);
        setAlertaFechado(false);
      }
    } catch (e) {
      console.error('Erro ao processar:', e);
    } finally {
      setProcessing(false);
      setSaving(false);
    }
  };

  const adicionarArquivoML = async (file: File) => {
    const data     = await parseExcelFile(file, undefined, 'Vendas');
    const novaFila = [...mlFiles, { name: file.name, data }];
    setMlFiles(novaFila);
    if (costData.length > 0) run(novaFila, costData, taxRate);
  };

  const removerArquivoML = (index: number) => {
    const novaFila = mlFiles.filter((_, i) => i !== index);
    setMlFiles(novaFila);
    if (novaFila.length > 0 && costData.length > 0) run(novaFila, costData, taxRate);
    else setResults(null);
  };

  const handleCarregarMesHistorico = (dados: any) => {
    const summary: FinancialSummary = {
      vendasSaudaveis:  dados.vendasSaudaveis,
      prejuizos:        dados.prejuizos,
      dadosParaAdvisor: dados.dadosParaAdvisor,
      stats:            dados.stats,
    };
    setResults(summary);
    setAllMonths([]);
    setSelectedMonthRef('');
    setMesHistoricoLabel(dados.label);
    setActiveTab('concile');
  };

  if (checkingAuth) {
    return (
      <div style={{ minHeight:'100vh', background:'#080E1C', display:'flex', alignItems:'center', justifyContent:'center' }}>
        <Loader size={24} style={{ color:'#2563EB', animation:'spin .6s linear infinite' }}/>
        <style>{`@keyframes spin{to{transform:rotate(360deg)}}`}</style>
      </div>
    );
  }

  if (!user) return <Login onLogin={() => {}} />;

  const s = results?.stats || {
    receitaBruta:0, totalCMV:0, totalImposto:0, impostoSomenteSaudaveis:0, comissaoML:0,
    freteVendedor:0, lucroLiquido:0, perdaDevolucao:0, perdaCancelamento:0
  };

  const fmt = (v: number) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v);

  const produtosPrejuizo = (results?.vendasSaudaveis || [])
    .filter(p => p.profit < 0)
    .sort((a, b) => a.profit - b.profit)
    .slice(0, 5);
  const totalPrejuizo = produtosPrejuizo.reduce((acc, p) => acc + p.profit, 0);

  const filtered = (() => {
    const base = (results?.vendasSaudaveis || []).filter(p => {
      return p.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
             p.sku?.toLowerCase().includes(searchTerm.toLowerCase()) ||
             p.mlb?.toLowerCase().includes(searchTerm.toLowerCase());
    });
    if (filterMode === 'loss') return base.filter(p => p.profit < 0);
    if (filterMode === 'alta') return base.filter(p => p.margin >= 15);
    if (filterMode === 'top') {
      if (base.length === 0) return [];
      const sorted    = [...base].sort((a, b) => b.revenue - a.revenue);
      const corte     = Math.max(1, Math.ceil(sorted.length * 0.25));
      const threshold = sorted[corte - 1].revenue;
      return sorted.filter(p => p.revenue >= threshold);
    }
    return base;
  })();

  const isAdmin = user.email === ADMIN_EMAIL;

  const tabs: { id: Tab; label: string; icon: React.ReactNode; divider?: boolean }[] = [
    { id: 'concile',      label: 'Conciliação',  icon: <BarChart2  size={15}/> },
    { id: 'precificacao', label: 'Precificador', icon: <Calculator size={15}/> },
    { id: 'advisor',      label: 'Advisor AI',   icon: <Brain      size={15}/> },
    { id: 'dre',          label: 'DRE Mensal',   icon: <FileText   size={15}/> },
    { id: 'historico',    label: 'Histórico',    icon: <TrendingUp size={15}/> },
    { id: 'faq',          label: 'Ajuda / FAQ',  icon: <HelpCircle size={15}/>, divider: true },
    { id: 'suporte',      label: 'Suporte',      icon: <MessageCircle size={15}/> },
    ...(isAdmin ? [{ id: 'ads' as Tab, label: 'Ads Dashboard', icon: <DollarSign size={15}/>, divider: true }] : []),
  ];

  const nomeUsuario = userProfile?.nome || user.email?.split('@')[0] || 'Vendedor';
  const plano       = userProfile?.plano || 'trial';

  const tabTitle: Record<Tab, string> = {
    concile:      mesHistoricoLabel ? `Conciliação — ${mesHistoricoLabel}` : 'Conciliação',
    precificacao: 'Precificador',
    advisor:      'Advisor AI',
    dre:          'DRE Mensal',
    historico:    'Histórico',
    faq:          'Ajuda & FAQ',
    suporte:      'Suporte',
    ads:          'Ads Dashboard',
  };

  const CSS = `
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
    :root{
      --blue-50:#EFF6FF;--blue-100:#DBEAFE;--blue-500:#3B82F6;--blue-600:#2563EB;--blue-700:#1D4ED8;--blue-800:#1E40AF;
      --green:#10B981;--green-bg:#D1FAE5;--green-border:#6EE7B7;
      --yellow:#F59E0B;--yellow-bg:#FEF3C7;--yellow-border:#FCD34D;
      --red:#EF4444;--red-bg:#FEE2E2;
      --orange:#F97316;--orange-bg:#FFEDD5;
      --sidebar-w:224px;--topbar-h:64px;
      --r:6px;--r-lg:10px;--r-xl:14px;
      --shadow-lg:0 10px 32px rgba(0,0,0,.12);--t:140ms ease;
    }
    [data-theme="light"]{
      --bg:#F4F6FB;--surface:#FFF;--surface-2:#F0F3FA;--surface-3:#E8EEFA;
      --border:#E2E7F3;--border-2:#CDD5ED;
      --tx:#0D1526;--tx-2:#2D3A55;--tx-3:#5A6A8A;--tx-4:#8FA0BF;
      --sb-bg:#FFF;--sb-border:#E8EDF7;--sb-hover:#F4F6FB;
      --sb-active-bg:#EEF2FF;--sb-active-tx:#1D4ED8;--sb-active-ic:#2563EB;
      --sb-tx:#3D4D6A;--sb-label:#9AAAC5;--tb-bg:#FFF;
    }
    [data-theme="dark"]{
      --bg:#080E1C;--surface:#0F1829;--surface-2:#162035;--surface-3:#1C2941;
      --border:#1F2E47;--border-2:#28395A;
      --tx:#E8EEFF;--tx-2:#B0BEDD;--tx-3:#6A82A8;--tx-4:#3D5070;
      --sb-bg:#0C1523;--sb-border:#182438;--sb-hover:#162035;
      --sb-active-bg:rgba(37,99,235,.15);--sb-active-tx:#60A5FA;--sb-active-ic:#60A5FA;
      --sb-tx:#8FA8CC;--sb-label:#3D5070;--tb-bg:#0C1523;
      --blue-50:rgba(30,58,138,.18);--blue-100:rgba(30,58,138,.30);
      --green-bg:#022C22;--yellow-bg:#271700;--red-bg:#200909;
      --green-border:#065F46;--yellow-border:#92400E;--red:#F87171;--orange-bg:#1F0C02;
    }
    html,body,#root{height:100%;font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--tx)}
    .app{display:flex;height:100vh;overflow:hidden}
    @keyframes spin{to{transform:rotate(360deg)}}
    @keyframes fi{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
    @keyframes pulse-border{0%,100%{border-color:var(--yellow-border)}50%{border-color:var(--yellow)}}

    .sb{width:var(--sidebar-w);flex-shrink:0;background:var(--sb-bg);border-right:1px solid var(--sb-border);display:flex;flex-direction:column;height:100vh;overflow:hidden}
    .sb-logo{padding:16px 14px 14px;border-bottom:1px solid var(--sb-border);display:flex;align-items:center;gap:10px;flex-shrink:0}
    .sb-logo-ic{width:34px;height:34px;border-radius:8px;flex-shrink:0;background:linear-gradient(135deg,#2563EB,#1D4ED8);display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(37,99,235,.35)}
    .sb-name{font-size:15px;font-weight:800;letter-spacing:-.4px;color:var(--tx);line-height:1.2}
    .sb-name em{font-style:normal;color:var(--blue-600)}
    .sb-by{font-size:10px;color:var(--tx-4);font-weight:500;margin-top:1px}
    .sb-nav{flex:1;overflow-y:auto;padding:6px 8px}
    .sb-lbl{font-size:10px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--sb-label);padding:6px 8px 5px}
    .sb-divider{height:1px;background:var(--sb-border);margin:8px 8px 4px}
    .sb-item{display:flex;align-items:center;gap:9px;height:36px;padding:0 9px;border-radius:6px;cursor:pointer;color:var(--sb-tx);font-size:13px;font-weight:500;width:100%;text-align:left;background:none;border:none;transition:background var(--t),color var(--t);white-space:nowrap;font-family:inherit}
    .sb-item .ic{width:15px;height:15px;flex-shrink:0;color:var(--tx-4)}
    .sb-item:hover{background:var(--sb-hover);color:var(--tx)}
    .sb-item.active{background:var(--sb-active-bg);color:var(--sb-active-tx);font-weight:600}
    .sb-item.active .ic{color:var(--sb-active-ic)}
    .sb-up-area{padding:4px 8px 4px}
    .sb-up-btn{display:flex;align-items:center;gap:8px;width:100%;padding:8px 10px;border-radius:8px;border:1.5px dashed var(--border-2);background:var(--surface-2);color:var(--tx-3);font-size:12px;font-weight:500;cursor:pointer;transition:all var(--t);margin-bottom:6px;text-align:left;font-family:inherit}
    .sb-up-btn:hover{border-color:var(--blue-500);color:var(--blue-600);background:var(--blue-50)}
    .sb-up-btn.done{border-color:var(--green-border);color:var(--green);background:var(--green-bg);border-style:solid}
    .sb-up-btn.waiting{border-color:var(--yellow-border);color:var(--yellow);background:var(--yellow-bg);border-style:solid;animation:pulse-border 1.8s ease-in-out infinite}
    .sb-up-btn .ic{width:14px;height:14px;flex-shrink:0}
    .ml-queue{display:flex;flex-direction:column;gap:4px;margin-bottom:6px}
    .ml-queue-item{display:flex;align-items:center;gap:6px;background:var(--green-bg);border:1px solid var(--green-border);border-radius:7px;padding:5px 8px}
    .ml-queue-name{flex:1;font-size:10px;font-weight:600;color:var(--green);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
    .ml-queue-del{background:none;border:none;cursor:pointer;color:var(--green);opacity:.6;padding:0;display:flex;transition:opacity .14s;flex-shrink:0}
    .ml-queue-del:hover{opacity:1}
    .ml-add-btn{display:flex;align-items:center;gap:7px;width:100%;padding:7px 10px;border-radius:8px;border:1.5px dashed var(--border-2);background:transparent;color:var(--tx-4);font-size:11px;font-weight:500;cursor:pointer;transition:all var(--t);font-family:inherit}
    .ml-add-btn:hover{border-color:var(--blue-500);color:var(--blue-600)}
    .ml-count-badge{font-size:10px;font-weight:700;background:var(--blue-600);color:#fff;border-radius:99px;padding:1px 6px;margin-left:auto}
    .sb-footer{padding:10px 8px 14px;border-top:1px solid var(--sb-border);flex-shrink:0}
    .sb-user{display:flex;align-items:center;gap:9px;padding:7px 8px;border-radius:7px;cursor:pointer;transition:background var(--t)}
    .sb-user:hover{background:var(--sb-hover)}
    .sb-av{width:30px;height:30px;border-radius:7px;flex-shrink:0;background:linear-gradient(135deg,var(--blue-600),var(--blue-800));color:#fff;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700}
    .plan-chip{display:inline-flex;align-items:center;font-size:10px;font-weight:700;padding:1px 7px;border-radius:99px;letter-spacing:.03em;text-transform:uppercase}
    .plan-trial{background:var(--surface-3);color:var(--tx-3)}
    .plan-mensal{background:var(--blue-100);color:var(--blue-700)}
    .plan-anual{background:#FEF3C7;color:#92400E}
    .sb-ob-btn{display:flex;align-items:center;gap:6px;width:100%;padding:6px 9px;border-radius:6px;background:none;border:none;cursor:pointer;font-size:11px;color:var(--tx-4);font-family:inherit;transition:all var(--t);margin-top:2px}
    .sb-ob-btn:hover{background:var(--sb-hover);color:var(--blue-500)}

    .main{flex:1;display:flex;flex-direction:column;min-width:0;overflow:hidden}
    .topbar{height:var(--topbar-h);background:var(--tb-bg);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 24px;flex-shrink:0;gap:12px}
    .tb-l{display:flex;align-items:center;gap:8px;min-width:0}
    .tb-title{font-size:15px;font-weight:700;color:var(--tx);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:400px}
    .tb-sep{color:var(--tx-4)}
    .tb-sub{font-size:13px;color:var(--tx-3);white-space:nowrap}
    .tb-hist-chip{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;background:var(--blue-50);color:var(--blue-600);border:1px solid var(--blue-100);padding:2px 8px;border-radius:99px;white-space:nowrap}
    .tb-warn-chip{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;background:var(--yellow-bg);color:var(--yellow);border:1px solid var(--yellow-border);padding:2px 8px;border-radius:99px;white-space:nowrap;display:flex;align-items:center;gap:4px}
    .tb-r{display:flex;align-items:center;gap:8px}
    .aliq{display:flex;align-items:center;gap:6px;background:var(--surface-2);border:1px solid var(--border);border-radius:8px;padding:5px 10px;font-size:12px}
    .aliq span{color:var(--tx-3);font-weight:500}
    .aliq input{background:transparent;border:none;outline:none;color:var(--blue-600);font-weight:700;width:32px;text-align:center;font-size:12px;font-family:inherit}
    .aliq em{color:var(--blue-600);font-style:normal;font-weight:700}
    .icbtn{width:32px;height:32px;border-radius:6px;display:flex;align-items:center;justify-content:center;color:var(--tx-3);transition:all var(--t);border:none;background:none;cursor:pointer}
    .icbtn:hover{background:var(--surface-2);color:var(--tx)}
    .saving-pill{display:flex;align-items:center;gap:5px;font-size:11px;color:var(--tx-4);font-weight:500}

    .content{flex:1;overflow-y:auto;padding:24px}
    .month-selector{display:flex;gap:6px;margin-bottom:16px;flex-wrap:wrap}
    .month-tab{padding:6px 16px;border-radius:20px;font-size:12px;font-weight:600;background:var(--surface);border:1.5px solid var(--border);color:var(--tx-3);cursor:pointer;font-family:inherit;transition:all .15s}
    .month-tab.active{background:var(--blue-600);border-color:var(--blue-600);color:#fff}
    .month-tab:hover:not(.active){border-color:var(--blue-500);color:var(--tx)}
    .alerta-prejuizo{background:var(--red-bg);border:1px solid var(--red);border-radius:var(--r-xl);padding:14px 18px;margin-bottom:18px;display:flex;align-items:flex-start;gap:14px;animation:fi .4s ease}
    .alerta-prejuizo-ic{width:36px;height:36px;border-radius:8px;background:var(--red);display:flex;align-items:center;justify-content:center;flex-shrink:0}
    .alerta-prejuizo-body{flex:1;min-width:0}
    .alerta-prejuizo-title{font-size:13px;font-weight:700;color:var(--red);margin-bottom:4px;display:flex;align-items:center;gap:8px}
    .alerta-prejuizo-sub{font-size:11px;color:var(--tx-3);margin-bottom:10px}
    .alerta-prejuizo-lista{display:flex;flex-wrap:wrap;gap:6px}
    .alerta-prejuizo-tag{display:flex;align-items:center;gap:5px;background:var(--surface);border:1px solid var(--red);border-radius:6px;padding:4px 10px;font-size:11px;font-weight:600;color:var(--red);white-space:nowrap}
    .alerta-fechar{background:none;border:none;cursor:pointer;color:var(--red);opacity:.6;padding:2px;display:flex;transition:opacity .14s;flex-shrink:0;margin-top:2px}
    .alerta-fechar:hover{opacity:1}
    .sg{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:18px}
    .sc{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);padding:16px 18px;position:relative;overflow:hidden}
    .sc::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;border-radius:var(--r-xl) var(--r-xl) 0 0}
    .sc.cb::after{background:var(--blue-500)}.sc.cg::after{background:var(--green)}.sc.cr::after{background:var(--red)}.sc.co::after{background:var(--orange)}
    .slbl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--tx-3);margin-bottom:8px}
    .sval{font-size:22px;font-weight:800;color:var(--tx);line-height:1;letter-spacing:-.5px}
    .sval.g{color:var(--green)}.sval.r{color:var(--red)}.sval.o{color:var(--orange)}
    .ssub{font-size:11px;color:var(--tx-4);margin-top:5px;display:flex;align-items:center;gap:4px}
    .ss{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px;overflow:visible}
    .ssm{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl);padding:14px 16px;display:flex;justify-content:space-between;align-items:center;overflow:visible}
    .ssm-l p:first-child{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--tx-3);margin-bottom:4px}
    .ssm-l p:last-child{font-size:16px;font-weight:700;color:var(--tx)}
    .ssm-ic{width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
    .tb2{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl) var(--r-xl) 0 0;padding:12px 16px;display:flex;align-items:center;gap:10px}
    .srch{position:relative;flex:1;max-width:280px}
    .srch svg{position:absolute;left:9px;top:50%;transform:translateY(-50%);width:13px;height:13px;color:var(--tx-4);pointer-events:none}
    .srch input{width:100%;height:32px;padding:0 10px 0 30px;border:1.5px solid var(--border);border-radius:var(--r);background:var(--surface-2);color:var(--tx);font-size:12px;outline:none;font-family:inherit;transition:border-color var(--t)}
    .srch input:focus{border-color:var(--blue-500)}
    .srch input::placeholder{color:var(--tx-4)}
    .fbtn{height:32px;padding:0 12px;border:1.5px solid var(--border);border-radius:var(--r);background:var(--surface-2);color:var(--tx-2);font-size:12px;font-weight:500;cursor:pointer;display:flex;align-items:center;gap:6px;font-family:inherit;transition:all var(--t);position:relative}
    .fbtn:hover{border-color:var(--blue-500);color:var(--blue-600)}
    .fdrop{position:absolute;top:calc(100% + 4px);right:0;background:var(--surface);border:1px solid var(--border);border-radius:var(--r-lg);box-shadow:var(--shadow-lg);overflow:hidden;z-index:50;min-width:180px}
    .fopt{display:block;width:100%;padding:9px 14px;text-align:left;font-size:12px;font-weight:500;color:var(--tx-2);background:none;border:none;cursor:pointer;font-family:inherit;transition:background var(--t)}
    .fopt:hover{background:var(--surface-2)}
    .fopt.on{color:var(--blue-600);font-weight:600;background:var(--blue-50)}
    .tblwrap{background:var(--surface);border:1px solid var(--border);border-top:none;border-radius:0 0 var(--r-xl) var(--r-xl);overflow:hidden}
    .empty{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:80px 24px;text-align:center;background:var(--surface);border:1px solid var(--border);border-radius:var(--r-xl)}
    .empty-ic{width:56px;height:56px;border-radius:16px;background:var(--blue-50);display:flex;align-items:center;justify-content:center;margin-bottom:16px}
    .empty-ic.warn{background:var(--yellow-bg)}
    .empty h3{font-size:15px;font-weight:700;color:var(--tx);margin-bottom:6px}
    .empty p{font-size:13px;color:var(--tx-3);max-width:320px;line-height:1.6}
    .empty-acts{display:flex;gap:8px;margin-top:20px;flex-wrap:wrap;justify-content:center}
    .btn-p{display:flex;align-items:center;gap:6px;padding:8px 16px;border-radius:var(--r-lg);background:var(--blue-600);color:#fff;border:none;cursor:pointer;font-size:13px;font-weight:600;font-family:inherit;transition:background var(--t)}
    .btn-p:hover{background:var(--blue-700)}
    .btn-p.warn{background:var(--yellow)}
    .btn-p.warn:hover{background:#D97706}
    .btn-s{display:flex;align-items:center;gap:6px;padding:8px 16px;border-radius:var(--r-lg);background:var(--surface-2);color:var(--tx-2);border:1.5px solid var(--border);cursor:pointer;font-size:13px;font-weight:600;font-family:inherit;transition:all var(--t)}
    .btn-s:hover{border-color:var(--blue-500);color:var(--blue-600)}
    .imp-info-btn{display:inline-flex;align-items:center;justify-content:center;width:15px;height:15px;border-radius:50%;background:var(--yellow);color:#000;font-size:9px;font-weight:800;cursor:pointer;flex-shrink:0;line-height:1;user-select:none}
    .imp-info-btn:hover{opacity:.8}
    .kpi-info-btn{display:inline-flex;align-items:center;justify-content:center;width:14px;height:14px;border-radius:50%;background:rgba(255,255,255,.25);color:#fff;font-size:9px;font-weight:800;cursor:pointer;flex-shrink:0;line-height:1;user-select:none;border:1px solid rgba(255,255,255,.4)}
    .kpi-info-btn:hover{background:rgba(255,255,255,.4)}
    .kpi-tooltip{position:absolute;top:calc(100% + 6px);left:0;width:280px;background:var(--surface);border:1px solid var(--border-2);border-radius:var(--r-lg);box-shadow:0 8px 24px rgba(0,0,0,.25);padding:14px 16px;z-index:9999;font-size:12px}
    .imp-tooltip{position:absolute;top:calc(100% + 6px);right:0;width:320px;background:var(--surface);border:1px solid var(--border-2);border-radius:var(--r-lg);box-shadow:0 8px 24px rgba(0,0,0,.25);padding:14px 16px;z-index:9999;font-size:12px;max-height:80vh;overflow-y:auto}
    .imp-tooltip-title{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--tx-3);margin-bottom:10px}
    .imp-tooltip-row{display:flex;justify-content:space-between;align-items:center;padding:4px 0;color:var(--tx-2);border-bottom:1px solid var(--border)}
    .imp-tooltip-row.imp-minus{color:var(--red)}
    .imp-tooltip-row.imp-base{font-weight:700;color:var(--tx);border-bottom:2px solid var(--border-2)}
    .imp-tooltip-row.imp-result{font-weight:700;color:var(--yellow);border-bottom:none;padding-top:8px}
    .imp-tooltip-divider{height:1px;background:var(--border-2);margin:10px 0}
    .imp-tooltip-obs{font-size:11px;color:var(--tx-3);line-height:1.6}
    .imp-tooltip-close{margin-top:10px;width:100%;padding:6px;border:1px solid var(--border);border-radius:6px;background:var(--surface-2);color:var(--tx-3);font-size:11px;cursor:pointer;font-family:inherit}
    .imp-tooltip-close:hover{background:var(--surface-3)}
    ::-webkit-scrollbar{width:4px;height:4px}
    ::-webkit-scrollbar-track{background:transparent}
    ::-webkit-scrollbar-thumb{background:var(--border-2);border-radius:99px}
    input::-webkit-outer-spin-button,input::-webkit-inner-spin-button{-webkit-appearance:none}
    input[type=number]{-moz-appearance:textfield}
  `;

  return (
    <div className="app">
      <style>{CSS}</style>

      {showOnboarding && <Onboarding onConcluir={concluirOnboarding} />}

      {showPasswordReset && (
        <div style={{ position:'fixed', inset:0, zIndex:9999, background:'rgba(8,14,28,.8)', backdropFilter:'blur(6px)', display:'flex', alignItems:'center', justifyContent:'center', padding:20 }}>
          <div style={{ background:'var(--surface)', border:'1px solid var(--border)', borderRadius:16, width:'100%', maxWidth:380, overflow:'hidden' }}>
            <div style={{ height:4, background:'linear-gradient(90deg,#2563EB,#10B981)' }}/>
            <div style={{ padding:'28px 28px 24px' }}>
              <div style={{ fontSize:18, fontWeight:800, color:'var(--tx)', marginBottom:6 }}>Redefinir senha</div>
              <div style={{ fontSize:13, color:'var(--tx-3)', marginBottom:24 }}>Digite e confirme sua nova senha.</div>
              <div style={{ marginBottom:14 }}>
                <div style={{ fontSize:11, fontWeight:700, textTransform:'uppercase', letterSpacing:'.05em', color:'var(--tx-3)', marginBottom:6 }}>Nova senha</div>
                <input
                  type="password" value={newPassword} onChange={e => setNewPassword(e.target.value)}
                  placeholder="Mínimo 6 caracteres"
                  style={{ width:'100%', height:42, padding:'0 12px', border:'1.5px solid var(--border)', borderRadius:8, background:'var(--surface-2)', color:'var(--tx)', fontSize:14, outline:'none', fontFamily:'inherit' }}
                  onKeyDown={e => e.key === 'Enter' && handlePasswordReset()}
                />
              </div>
              <div style={{ marginBottom:18 }}>
                <div style={{ fontSize:11, fontWeight:700, textTransform:'uppercase', letterSpacing:'.05em', color:'var(--tx-3)', marginBottom:6 }}>Confirmar senha</div>
                <input
                  type="password" value={newPasswordConfirm} onChange={e => setNewPasswordConfirm(e.target.value)}
                  placeholder="Repita a senha"
                  style={{ width:'100%', height:42, padding:'0 12px', border:'1.5px solid var(--border)', borderRadius:8, background:'var(--surface-2)', color:'var(--tx)', fontSize:14, outline:'none', fontFamily:'inherit' }}
                  onKeyDown={e => e.key === 'Enter' && handlePasswordReset()}
                />
              </div>
              {passwordResetMsg && (
                <div style={{ fontSize:13, color:'var(--red)', background:'var(--red-bg)', border:'1px solid var(--red)', borderRadius:8, padding:'9px 12px', marginBottom:14 }}>{passwordResetMsg}</div>
              )}
              <button
                onClick={handlePasswordReset} disabled={passwordResetLoading}
                style={{ width:'100%', height:42, background:'linear-gradient(135deg,#2563EB,#1D4ED8)', color:'#fff', border:'none', borderRadius:9, fontSize:14, fontWeight:700, cursor:'pointer', fontFamily:'inherit', opacity: passwordResetLoading ? .6 : 1 }}
              >
                {passwordResetLoading ? 'Salvando...' : 'Salvar nova senha'}
              </button>
            </div>
          </div>
        </div>
      )}

      <input type="file" ref={mlRef} style={{ display: 'none' }} accept=".xlsx,.xls"
        onChange={async e => {
          const f = e.target.files?.[0];
          if (f) await adicionarArquivoML(f);
          if (mlRef.current) mlRef.current.value = '';
        }}
      />
      <input type="file" ref={costRef} style={{ display: 'none' }} accept=".xlsx,.xls"
        onChange={async e => {
          const f = e.target.files?.[0];
          if (f) {
            const r = await parseExcelFile(f, 0);
            setCostData(r); setCostFileName(f.name);
            run(mlFiles, r, taxRate);
          }
        }}
      />

      {/* SIDEBAR */}
      <aside className="sb">
        <div className="sb-logo">
          <div className="sb-logo-ic"><DollarSign size={16} color="white"/></div>
          <div>
            <div className="sb-name">Sobrou <em>Quanto</em> ML</div>
            <div className="sb-by">by ProspectIA</div>
          </div>
        </div>

        <nav className="sb-nav">
          <div className="sb-lbl">Menu</div>
          {tabs.map(t => (
            <React.Fragment key={t.id}>
              {t.divider && <div className="sb-divider" />}
              <button
                className={`sb-item ${activeTab === t.id ? 'active' : ''}`}
                onClick={() => setActiveTab(t.id)}
              >
                <span className="ic">{t.icon}</span>{t.label}
              </button>
            </React.Fragment>
          ))}

          <button className="sb-ob-btn" onClick={() => setShowOnboarding(true)}>
            <BookOpen size={12} /> Ver tutorial
          </button>

          <div className="sb-lbl" style={{ marginTop: 4 }}>Importar Dados</div>
          <div className="sb-up-area">
            {mlFiles.length > 0 && (
              <div className="ml-queue">
                {mlFiles.map((f, i) => (
                  <div key={i} className="ml-queue-item">
                    <CheckCircle2 size={11} style={{ color: 'var(--green)', flexShrink: 0 }}/>
                    <span className="ml-queue-name">{f.name}</span>
                    <button className="ml-queue-del" onClick={() => removerArquivoML(i)}>
                      <Trash2 size={11}/>
                    </button>
                  </div>
                ))}
              </div>
            )}
            <button className="ml-add-btn" onClick={() => mlRef.current?.click()}>
              {processing
                ? <Loader size={13} style={{ animation: 'spin .6s linear infinite', flexShrink: 0 }}/>
                : <Plus size={13} style={{ flexShrink: 0 }}/>
              }
              {mlFiles.length === 0 ? 'Relatório ML' : 'Adicionar outro mês'}
              {mlFiles.length > 0 && <span className="ml-count-badge">{mlFiles.length}</span>}
            </button>
            <button
              className={`sb-up-btn ${costFileName ? 'done' : aguardandoCustos ? 'waiting' : ''}`}
              style={{ marginTop: 4 }}
              onClick={() => costRef.current?.click()}
            >
              {costFileName
                ? <><CheckCircle2 size={14} className="ic"/><span style={{ fontSize:11, overflow:'hidden', textOverflow:'ellipsis', whiteSpace:'nowrap', maxWidth:130 }}>{costFileName}</span></>
                : aguardandoCustos
                  ? <><AlertCircle size={14} className="ic"/>Meus Custos ← agora!</>
                  : <><Upload size={14} className="ic"/>Meus Custos</>
              }
            </button>
          </div>
        </nav>

        <div className="sb-footer">
          <div className="sb-user" onClick={handleLogout}>
            <div className="sb-av">{nomeUsuario.slice(0,2).toUpperCase()}</div>
            <div style={{ flex:1, minWidth:0 }}>
              <div style={{ fontSize:12, fontWeight:600, color:'var(--tx)', overflow:'hidden', textOverflow:'ellipsis', whiteSpace:'nowrap' }}>{nomeUsuario}</div>
              <span className={`plan-chip ${plano==='mensal'?'plan-mensal':plano==='anual'?'plan-anual':'plan-trial'}`}>{plano}</span>
            </div>
            <LogOut size={13} style={{ color:'var(--tx-4)', flexShrink:0 }}/>
          </div>
        </div>
      </aside>

      {/* MAIN */}
      <div className="main">
        <header className="topbar">
          <div className="tb-l">
            <span className="tb-title">{tabTitle[activeTab]}</span>
            {mesHistoricoLabel && activeTab === 'concile' && <span className="tb-hist-chip">histórico</span>}
            {aguardandoCustos && activeTab === 'concile' && (
              <span className="tb-warn-chip"><AlertCircle size={10}/>aguardando custos</span>
            )}
            {results && activeTab === 'concile' && !mesHistoricoLabel && allMonths.length > 1 && (
              <><span className="tb-sep">·</span><span className="tb-sub">{allMonths.length} meses detectados</span></>
            )}
            {results && activeTab === 'concile' && !mesHistoricoLabel && allMonths.length === 0 && mlFiles.length > 1 && (
              <><span className="tb-sep">·</span><span className="tb-sub">{mlFiles.length} arquivos mesclados</span></>
            )}
            {results && activeTab === 'concile' && <><span className="tb-sep">·</span><span className="tb-sub">{results.vendasSaudaveis?.length || 0} produtos</span></>}
          </div>
          <div className="tb-r">
            {(saving || processing) && (
              <div className="saving-pill">
                <Loader size={12} style={{ animation: 'spin .6s linear infinite' }}/>
                {processing ? 'Processando...' : 'Salvando...'}
              </div>
            )}
            {activeTab === 'concile' && (
              <div className="aliq">
                <span>Alíquota</span>
                <input type="number" value={taxRate === 0 ? '' : taxRate}
                  placeholder="0"
                  onChange={e => {
                    const v = parseFloat(e.target.value) || 0;
                    setTaxRate(v);
                    if (mlFiles.length > 0 && costData.length > 0) run(mlFiles, costData, v);
                  }}
                />
                <em>%</em>
              </div>
            )}
            <button className="icbtn" onClick={() => setTheme(t => t === 'dark' ? 'light' : 'dark')}>
              {theme === 'dark' ? <Sun size={16}/> : <Moon size={16}/>}
            </button>
          </div>
        </header>

        <main className="content" onClick={() => { setShowKpiInfo(null); setShowImpostoInfo(false); }}>
          {activeTab === 'precificacao' && <Precificacao userId={user.id}/>}
          {activeTab === 'advisor'      && <Advisor data={results?.dadosParaAdvisor || []}/>}
          {activeTab === 'dre'          && <DRE data={results} userId={user.id}/>}
          {activeTab === 'historico'    && <Historico userId={user.id} onCarregarMes={handleCarregarMesHistorico}/>}
          {activeTab === 'faq'          && <FAQ />}
          {activeTab === 'suporte'      && <Suporte userId={user.id} userEmail={user.email || ''} />}
          {activeTab === 'ads'          && isAdmin && <AdsDashboard />}

          {activeTab === 'concile' && (
            aguardandoCustos ? (
              <div className="empty">
                <div className="empty-ic warn"><AlertCircle size={24} style={{ color: 'var(--yellow)' }}/></div>
                <h3>Falta a Planilha de Custos</h3>
                <p>O Relatório ML foi carregado. Importe agora a sua planilha de custos para calcular o CMV e processar a conciliação.</p>
                <div className="empty-acts">
                  <button className="btn-p warn" onClick={() => costRef.current?.click()}>
                    <Upload size={14}/> Importar Meus Custos
                  </button>
                </div>
              </div>
            ) : results ? (
              <div style={{ animation: 'fi .4s ease' }}>
                {allMonths.length > 1 && (
                  <div className="month-selector">
                    {allMonths.map(m => (
                      <button
                        key={m.ref}
                        className={`month-tab ${selectedMonthRef === m.ref ? 'active' : ''}`}
                        onClick={() => {
                          setSelectedMonthRef(m.ref);
                          setResults(m.summary);
                          setAlertaFechado(false);
                        }}
                      >
                        {m.label}
                      </button>
                    ))}
                  </div>
                )}
                {produtosPrejuizo.length > 0 && !alertaFechado && (
                  <div className="alerta-prejuizo">
                    <div className="alerta-prejuizo-ic"><AlertCircle size={18} color="#fff"/></div>
                    <div className="alerta-prejuizo-body">
                      <div className="alerta-prejuizo-title">
                        {produtosPrejuizo.length} produto{produtosPrejuizo.length > 1 ? 's' : ''} vendendo no prejuízo
                        <span style={{ fontSize: 11, fontWeight: 400, color: 'var(--tx-3)' }}>— total: {fmt(totalPrejuizo)}</span>
                      </div>
                      <div className="alerta-prejuizo-sub">Esses produtos estão gerando perda a cada venda. Revise o custo, preço ou pause o anúncio.</div>
                      <div className="alerta-prejuizo-lista">
                        {produtosPrejuizo.map((p, i) => (
                          <div key={i} className="alerta-prejuizo-tag">{p.sku || p.mlb}<span>{fmt(p.profit)}</span></div>
                        ))}
                      </div>
                    </div>
                    <button className="alerta-fechar" onClick={() => setAlertaFechado(true)}><XCircle size={16}/></button>
                  </div>
                )}
                <div className="sg">
                  {/* Faturamento Bruto */}
                  <div className="sc cb" style={{ position:'relative', overflow: showKpiInfo === 'fat' ? 'visible' : 'hidden' }}>
                    <div className="slbl" style={{ display:'flex', alignItems:'center', gap:5 }}>
                      Faturamento Bruto
                      <span className="kpi-info-btn" style={{ background:'var(--blue-500)', color:'#fff', border:'none' }} onClick={e => { e.stopPropagation(); setShowKpiInfo(v => v === 'fat' ? null : 'fat'); }}>?</span>
                    </div>
                    <div className="sval">{fmt(s.receitaBruta)}</div>
                    <div className="ssub"><ShoppingBag size={11}/> Vendas concluídas</div>
                    {showKpiInfo === 'fat' && (
                      <div className="kpi-tooltip" onClick={e => e.stopPropagation()}>
                        <div className="imp-tooltip-title">O que é o Faturamento Bruto</div>
                        <div className="imp-tooltip-obs">
                          Soma de toda receita gerada — inclui vendas entregues, devoluções e cancelamentos.<br/><br/>
                          <strong>Atenção:</strong> este valor inclui vendas que depois foram devolvidas ou canceladas. O dinheiro dessas operações aparece como desconto em Devoluções e Cancelamentos.
                        </div>
                        <button className="imp-tooltip-close" onClick={e => { e.stopPropagation(); setShowKpiInfo(null); }}>Fechar</button>
                      </div>
                    )}
                  </div>

                  {/* Lucro Líquido */}
                  <div className="sc cg" style={{ position:'relative', overflow: showKpiInfo === 'lucro' ? 'visible' : 'hidden' }}>
                    <div className="slbl" style={{ display:'flex', alignItems:'center', gap:5 }}>
                      Lucro Líquido
                      <span className="kpi-info-btn" style={{ background:'var(--green)', color:'#fff', border:'none' }} onClick={e => { e.stopPropagation(); setShowKpiInfo(v => v === 'lucro' ? null : 'lucro'); }}>?</span>
                    </div>
                    <div className={`sval ${s.lucroLiquido >= 0 ? 'g' : 'r'}`}>{fmt(s.lucroLiquido)}</div>
                    <div className="ssub">{s.receitaBruta > 0 ? `${((s.lucroLiquido/s.receitaBruta)*100).toFixed(1)}% de margem` : '—'}</div>
                    {showKpiInfo === 'lucro' && (
                      <div className="kpi-tooltip" onClick={e => e.stopPropagation()}>
                        <div className="imp-tooltip-title">Como o Lucro Líquido é calculado</div>
                        {[
                          { l: 'Faturamento bruto', v: s.receitaBruta, op: '' },
                          { l: '- Custo dos produtos (CMV)', v: s.totalCMV, op: '-', cor: 'var(--orange)' },
                          { l: '- Impostos', v: s.totalImposto, op: '-', cor: 'var(--yellow)' },
                          { l: '- Taxas & comissão ML', v: s.comissaoML, op: '-', cor: 'var(--red)' },
                          { l: '- Frete vendedor', v: s.freteVendedor, op: '-', cor: 'var(--red)' },
                          { l: '- Publicidade (Ads)', v: (s as any).mercadoAds || 0, op: '-', cor: 'var(--red)' },
                          { l: '- Perdas devoluções', v: s.perdaDevolucao, op: '-', cor: 'var(--red)' },
                          { l: '- Perdas cancelamentos', v: s.perdaCancelamento, op: '-', cor: 'var(--red)' },
                        ].map((item, i) => (
                          <div key={i} className="imp-tooltip-row" style={i === 0 ? {} : { color: item.cor || 'var(--tx-2)' }}>
                            <span>{item.l}</span>
                            <span>{item.op}{fmt(item.v)}</span>
                          </div>
                        ))}
                        <div className="imp-tooltip-row imp-base">
                          <span>= Lucro Líquido</span>
                          <span style={{ color: s.lucroLiquido >= 0 ? 'var(--green)' : 'var(--red)' }}>{fmt(s.lucroLiquido)}</span>
                        </div>
                        {taxRate === 0 && (
                          <div className="imp-tooltip-obs" style={{ color:'var(--yellow)', marginTop:8 }}>
                            Alíquota em 0% — o imposto não está sendo descontado.
                          </div>
                        )}
                        {s.totalCMV === 0 && (
                          <div className="imp-tooltip-obs" style={{ color:'var(--yellow)', marginTop:4 }}>
                            CMV = R$ 0,00 — importe a planilha de custos para o lucro ser preciso.
                          </div>
                        )}
                        <button className="imp-tooltip-close" onClick={e => { e.stopPropagation(); setShowKpiInfo(null); }}>Fechar</button>
                      </div>
                    )}
                  </div>

                  {/* Devoluções */}
                  <div className="sc cr" style={{ position:'relative', overflow: showKpiInfo === 'dev' ? 'visible' : 'hidden' }}>
                    <div className="slbl" style={{ display:'flex', alignItems:'center', gap:5 }}>
                      Devoluções
                      <span className="kpi-info-btn" style={{ background:'var(--red)', color:'#fff', border:'none' }} onClick={e => { e.stopPropagation(); setShowKpiInfo(v => v === 'dev' ? null : 'dev'); }}>?</span>
                    </div>
                    <div className="sval r">{fmt(s.perdaDevolucao)}</div>
                    <div className="ssub"><RotateCcw size={11}/> Custo logístico</div>
                    {showKpiInfo === 'dev' && (
                      <div className="kpi-tooltip" onClick={e => e.stopPropagation()}>
                        <div className="imp-tooltip-title">O que são as Devoluções</div>
                        <div className="imp-tooltip-obs">
                          Valor total <strong>reembolsado ao comprador</strong> em devoluções — não é a receita original da venda.<br/><br/>
                          Exemplo: produto vendido por R$200, comprador devolveu e recebeu R$200 de volta. Este card mostra R$200.<br/><br/>
                          O custo do frete dessas devoluções está separado no Advisor AI.
                        </div>
                        <button className="imp-tooltip-close" onClick={e => { e.stopPropagation(); setShowKpiInfo(null); }}>Fechar</button>
                      </div>
                    )}
                  </div>

                  {/* Cancelamentos */}
                  <div className="sc co" style={{ position:'relative', overflow: showKpiInfo === 'can' ? 'visible' : 'hidden' }}>
                    <div className="slbl" style={{ display:'flex', alignItems:'center', gap:5 }}>
                      Cancelamentos
                      <span className="kpi-info-btn" style={{ background:'var(--orange)', color:'#fff', border:'none' }} onClick={e => { e.stopPropagation(); setShowKpiInfo(v => v === 'can' ? null : 'can'); }}>?</span>
                    </div>
                    <div className="sval o">{fmt(s.perdaCancelamento)}</div>
                    <div className="ssub"><XCircle size={11}/> Vendas perdidas</div>
                    {showKpiInfo === 'can' && (
                      <div className="kpi-tooltip" onClick={e => e.stopPropagation()}>
                        <div className="imp-tooltip-title">O que são os Cancelamentos</div>
                        <div className="imp-tooltip-obs">
                          Valor total <strong>reembolsado</strong> em vendas canceladas antes ou durante a entrega.<br/><br/>
                          Cancelamentos após envio são mais graves — o produto pode ter saído e não voltado. Veja os detalhes no Advisor AI.
                        </div>
                        <button className="imp-tooltip-close" onClick={e => { e.stopPropagation(); setShowKpiInfo(null); }}>Fechar</button>
                      </div>
                    )}
                  </div>
                </div>
                <div className="ss">
                  <div className="ssm" style={{ position:'relative', overflow: showKpiInfo === 'cmv' ? 'visible' : 'hidden' }}>
                    <div className="ssm-l" style={{ flex:1, minWidth:0 }}>
                      <p style={{ display:'flex', alignItems:'center', gap:5 }}>
                        Custo do Produto (CMV)
                        <span className="kpi-info-btn" style={{ background:'var(--orange)', color:'#fff', border:'none' }} onClick={e => { e.stopPropagation(); setShowKpiInfo(v => v === 'cmv' ? null : 'cmv'); }}>?</span>
                      </p>
                      <p style={{ color:'var(--orange)' }}>{fmt(s.totalCMV)}</p>
                    </div>
                    <div className="ssm-ic" style={{ background:'var(--orange-bg)' }}><Package size={16} style={{ color:'var(--orange)' }}/></div>
                    {showKpiInfo === 'cmv' && (
                      <div className="kpi-tooltip" onClick={e => e.stopPropagation()}>
                        <div className="imp-tooltip-title">Como o CMV é calculado</div>
                        <div className="imp-tooltip-obs">
                          <strong>CMV = custo unitário × quantidade vendida</strong>, somado apenas para vendas onde o dinheiro ficou com o vendedor.<br/><br/>
                          <strong>✓ Entra no CMV:</strong><br/>
                          · Entregue / Chegou / Venda entregue<br/>
                          · A caminho / Chega entre...<br/>
                          · Etiqueta impressa / Para enviar<br/>
                          · Aguardando estoque (Full)<br/>
                          · Reclamação encerrada a favor do vendedor<br/>
                          · Mediação onde o dinheiro ficou com você<br/><br/>
                          <strong>✗ Não entra no CMV:</strong><br/>
                          · Devoluções — produto voltou<br/>
                          · Cancelamentos — venda não concluída<br/>
                          · Mediação onde ML devolveu ao comprador<br/>
                          · Reclamação com reembolso ao comprador<br/><br/>
                          O custo vem da planilha importada, identificado pelo MLB ou SKU. Produtos sem custo cadastrado contribuem R$ 0,00.
                        </div>
                        <button className="imp-tooltip-close" onClick={e => { e.stopPropagation(); setShowKpiInfo(null); }}>Fechar</button>
                      </div>
                    )}
                  </div>
                  <div className="ssm">
                    <div className="ssm-l"><p>Taxas & Frete ML</p><p>{fmt(s.comissaoML + s.freteVendedor)}</p></div>
                    <div className="ssm-ic" style={{ background:'var(--blue-50)' }}><Percent size={16} style={{ color:'var(--blue-600)' }}/></div>
                  </div>
                  <div className="ssm" style={{ position:'relative' }}>
                    <div className="ssm-l" style={{ flex:1, minWidth:0 }}>
                      <p style={{ display:'flex', alignItems:'center', gap:5 }}>
                        Impostos Calculados
                        <span className="imp-info-btn" onClick={e => { e.stopPropagation(); setShowImpostoInfo(v => !v); }} title="Ver detalhes do cálculo">?</span>
                      </p>
                      <p style={{ color:'var(--yellow)' }}>{fmt(s.totalImposto)}</p>
                    </div>
                    <div className="ssm-ic" style={{ background:'var(--yellow-bg)' }}><FileText size={16} style={{ color:'var(--yellow)' }}/></div>
                    {showImpostoInfo && (
                      <div className="imp-tooltip" onClick={e => e.stopPropagation()}>
                        <div className="imp-tooltip-title">Imposto ({taxRate > 0 ? `${taxRate}%` : 'alíquota não definida'})</div>

                        {taxRate === 0 ? (
                          <div className="imp-tooltip-obs" style={{ color:'var(--yellow)' }}>
                            Digite sua alíquota no campo "Alíquota %" no topo da tela.
                          </div>
                        ) : (() => {
                          const imp1 = s.totalImposto;
                          const imp2 = (s.receitaBruta - s.perdaCancelamento) * (taxRate / 100);
                          const imp3 = s.impostoSomenteSaudaveis || 0;
                          const bloco = (label: string, rows: {l:string; v:number; minus?:boolean}[], result: number, cor: string) => (
                            <div style={{ marginBottom:10 }}>
                              <div style={{ fontSize:10, fontWeight:700, textTransform:'uppercase', letterSpacing:'.04em', color: cor, marginBottom:5 }}>{label}</div>
                              {rows.map((r, i) => (
                                <div key={i} className={`imp-tooltip-row${r.minus ? ' imp-minus' : ''}`}>
                                  <span>{r.minus ? '- ' : ''}{r.l}</span>
                                  <span>{fmt(r.v)}</span>
                                </div>
                              ))}
                              <div className="imp-tooltip-row imp-result" style={{ color: cor }}>
                                <span>× {taxRate}% = Imposto</span>
                                <span>{fmt(result)}</span>
                              </div>
                            </div>
                          );
                          return (
                            <>
                              {bloco('Receita bruta − devoluções − cancelamentos', [
                                { l:'Receita bruta', v: s.receitaBruta },
                                { l:'Reembolsos devoluções', v: s.perdaDevolucao, minus:true },
                                { l:'Reembolsos cancelamentos', v: s.perdaCancelamento, minus:true },
                                { l:'= Base', v: s.receitaBruta - s.perdaDevolucao - s.perdaCancelamento },
                              ], imp1, 'var(--green)')}

                              <div className="imp-tooltip-divider"/>

                              {bloco('Receita bruta − cancelamentos', [
                                { l:'Receita bruta', v: s.receitaBruta },
                                { l:'Reembolsos cancelamentos', v: s.perdaCancelamento, minus:true },
                                { l:'= Base', v: s.receitaBruta - s.perdaCancelamento },
                              ], imp2, 'var(--orange)')}

                              <div className="imp-tooltip-divider"/>

                              <div style={{ display:'flex', justifyContent:'space-between', alignItems:'center', padding:'4px 0' }}>
                                <span style={{ fontSize:11, color:'var(--tx-3)' }}>Somente vendas concluídas</span>
                                <strong style={{ color:'var(--tx-3)' }}>{fmt(imp3)}</strong>
                              </div>
                            </>
                          );
                        })()}

                        <button className="imp-tooltip-close" onClick={() => setShowImpostoInfo(false)}>Fechar</button>
                      </div>
                    )}
                  </div>
                </div>
                <div className="tb2">
                  <div className="srch">
                    <Search/>
                    <input type="text" placeholder="Buscar MLB, SKU ou produto..."
                      value={searchTerm} onChange={e => setSearchTerm(e.target.value)}/>
                  </div>
                  <div style={{ position: 'relative' }}>
                    <button className="fbtn" onClick={() => setShowFilters(v => !v)}>
                      <Filter size={13}/>
                      {filterMode === 'all' ? 'Todos' : filterMode === 'loss' ? 'Prejuízos' : filterMode === 'alta' ? 'Alta perf.' : 'Top'}
                      <ChevronRight size={12} style={{ transform: showFilters ? 'rotate(90deg)' : 'none', transition: 'transform .15s' }}/>
                    </button>
                    {showFilters && (
                      <div className="fdrop">
                        {[{id:'all',l:'Todos os produtos'},{id:'alta',l:'Alta performance'},{id:'loss',l:'Apenas prejuízos'},{id:'top',l:'Top faturamento'}].map(o => (
                          <button key={o.id} className={`fopt ${filterMode === o.id ? 'on' : ''}`}
                            onClick={() => { setFilterMode(o.id as any); setShowFilters(false); }}>{o.l}</button>
                        ))}
                      </div>
                    )}
                  </div>
                  <span style={{ marginLeft:'auto', fontSize:11, color:'var(--tx-4)', fontWeight:500 }}>
                    {filtered.length} produto{filtered.length !== 1 ? 's' : ''}
                  </span>
                </div>
                <div className="tblwrap"><ProductsTable data={filtered}/></div>
              </div>
            ) : (
              <div className="empty">
                <div className="empty-ic"><BarChart2 size={24} style={{ color:'var(--blue-600)' }}/></div>
                <h3>Aguardando importação</h3>
                <p>Importe o Relatório ML e a Planilha de Custos na barra lateral para iniciar a conciliação financeira.</p>
                <div className="empty-acts">
                  <button className="btn-p" onClick={() => mlRef.current?.click()}><Upload size={14}/> Relatório ML</button>
                  <button className="btn-s" onClick={() => costRef.current?.click()}><Upload size={14}/> Meus Custos</button>
                </div>
              </div>
            )
          )}
        </main>
      </div>
    </div>
  );
}