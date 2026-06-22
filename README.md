# SobrouQuantoML

Plataforma web para vendedores do Mercado Livre calcularem lucro real, precificarem produtos e acompanharem performance — desenvolvida com React, TypeScript, Vite e Supabase.

## Sobre o projeto

Ferramenta SaaS que resolve um problema prático de quem vende no Mercado Livre: saber exatamente quanto sobra depois de taxas, frete, impostos e custos operacionais.

## Módulos

- **Dashboard de Anúncios** — visão geral de performance dos anúncios
- **DRE** — Demonstrativo de Resultado simplificado por produto
- **Precificação** — calculadora de preço com margem real
- **Histórico** — acompanhamento de vendas e resultados
- **Advisor** — recomendações baseadas nos dados do vendedor
- **Onboarding** — configuração inicial guiada
- **FAQ e Suporte**

## Stack

- React + TypeScript
- Vite
- Supabase (autenticação e banco de dados)
- Integração com API do Mercado Livre

## Como rodar

```bash
npm install
cp .env.example .env
# preencha as variáveis no .env
npm run dev
```

## Variáveis de ambiente

```
VITE_SUPABASE_URL=sua_url_do_supabase
VITE_SUPABASE_ANON_KEY=sua_chave_anonima_do_supabase
```

## Desenvolvido por

[Nayara Martins](https://linkedin.com/in/nayaramartinsdev) — Desenvolvedora de Sistemas para Empresas
