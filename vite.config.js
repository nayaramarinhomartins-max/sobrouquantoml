import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'
import fs from 'fs'
import path from 'path'

export default defineConfig({
  plugins: [
    react(),
    {
      name: 'serve-html-pages',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          // /login.html → src/pages/login.html
          if (req.url === '/login.html' || req.url === '/login') {
            const file = path.resolve(__dirname, 'src/pages/login.html')
            if (fs.existsSync(file)) {
              res.setHeader('Content-Type', 'text/html')
              res.end(fs.readFileSync(file, 'utf-8'))
              return
            }
          }
          // sitemap.xml → serve com content-type correto
          if (req.url === '/sitemap.xml') {
            const file = path.resolve(__dirname, 'sitemap.xml')
            if (fs.existsSync(file)) {
              res.setHeader('Content-Type', 'application/xml')
              res.end(fs.readFileSync(file, 'utf-8'))
              return
            }
          }
          // robots.txt
          if (req.url === '/robots.txt') {
            const file = path.resolve(__dirname, 'robots.txt')
            if (fs.existsSync(file)) {
              res.setHeader('Content-Type', 'text/plain')
              res.end(fs.readFileSync(file, 'utf-8'))
              return
            }
          }
          next()
        })
      }
    }
  ],

  build: {
    rollupOptions: {
      input: {
        main:    resolve(__dirname, 'index.html'),
        landing: resolve(__dirname, 'landing.html'),
        login:   resolve(__dirname, 'src/pages/login.html'),
      },
    },
  },

  server: {
    open: '/landing.html',
  },
})