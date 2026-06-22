import { useEffect } from 'react';

export function Login({ onLogin }: { onLogin: () => void }) {
  useEffect(() => {
    // Em dev (Vite) o login.html fica em /src/pages/login.html
    // Em prod (build) fica em /login.html (pela config do rollup)
    const isProd = import.meta.env.PROD;
    window.location.href = isProd ? '/login.html' : '/src/pages/login.html';
  }, []);
  return null;
}