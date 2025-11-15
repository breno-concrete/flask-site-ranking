# ⚔️ LIGA - Embaixadores do Rei
## Igreja Batista Betsaida - Sistema de Ranking

---

## 🎨 Design & Branding Finalizado

### Cores Oficiais
- 🟡 **Amarelo/Ouro:** `#FFD700` - Destaque e Acento
- 🔵 **Azul Real:** `#1e40af` - Primária (Headers, Textos)
- ⚪ **Branco:** `#ffffff` - Backgrounds de Cards

### Tipografia
- **Font:** Segoe UI, Roboto, Oxygen, Ubuntu
- **Títulos:** 700-900 weight, Azul Primário
- **Corpo:** 400-500 weight, Cinza Escuro

### Componentes Visuais
✅ Headers com Gradiente Azul  
✅ Cards Brancos com Bordas Azuis  
✅ Botões com Gradientes  
✅ Tabelas Responsivas  
✅ Info Boxes com Cores Temáticas  
✅ Animações Suaves (0.3s)  
✅ Shadows Profissionais  

---

## 📁 Estrutura de Arquivos Otimizada

```
liga_ranking/
├── 📄 app.py                 ← Aplicação Flask (Backend)
├── 📄 requirements.txt       ← Dependências
├── 📄 README.md              ← Documentação
├── 📄 CORES.md               ← Paleta de Cores
│
├── 📁 models/
│   └── 📄 ranking.py         ← Lógica de Ranking
│
├── 📁 data/
│   └── 📄 usuarios.json      ← Banco de Dados (JSON)
│
├── 📁 static/
│   └── 📄 style.css          ← CSS Centralizado (ÚNICO ARQUIVO)
│
└── 📁 templates/
    ├── 📄 homepage.html      ← Ranking Público
    ├── 📄 login.html         ← Login Admin
    ├── 📄 admin.html         ← Dashboard CRUD
    └── 📄 semana.html        ← Pontuação Semanal
```

---

## 🚀 Features Implementadas

### 👥 Para Usuários (Público)
- ✅ Visualizar Ranking Geral
- ✅ Ver Posições em Tempo Real
- ✅ Certificados com Emojis (🥇🥈🥉)
- ✅ Classes dos Embaixadores

### 🔐 Para Admin (Protegido)
- ✅ Autenticação por Token
- ✅ CRUD Completo em Página Única
- ✅ Adicionar Embaixadores
- ✅ Editar Pontos e Classe
- ✅ Deletar Embaixadores
- ✅ Adicionar Pontuação Semanal (Soma Automática)
- ✅ Preview em Tempo Real

---

## 💾 CSS Reorganizado

### ✨ Antes
- Estilos **INLINE** em cada HTML
- Código **DUPLICADO** e desorganizado
- Difícil **MANUTENÇÃO**

### ✨ Depois
- ✅ **1 ARQUIVO CSS** centralizado
- ✅ **Variáveis CSS** (Custom Properties)
- ✅ **Organização por Seções**
- ✅ **Responsivo** (Mobile, Tablet, Desktop)
- ✅ **Animações** e Transições
- ✅ **DRY** (Don't Repeat Yourself)

---

## 📊 Estrutura CSS

```css
/* 1. Variáveis e Reset */
:root { ... }

/* 2. Layout Geral */
.container, .header, .section

/* 3. Navegação */
.nav-buttons, .nav-link, .logout-btn

/* 4. Formulários */
.form-row, .form-group, input, select

/* 5. Botões */
button, .btn, .btn-warning, .btn-danger

/* 6. Tabelas */
table, thead, tbody, tr, td

/* 7. Ranking */
.ranking-table, .classe, .podium-*

/* 8. Info Boxes */
.info-box, .success-box, .warning-box

/* 9. Login */
.login-container, .erro, .voltar

/* 10. Responsive */
@media (max-width: 768px)
@media (max-width: 480px)

/* 11. Animações */
@keyframes slideIn, pulse

/* 12. Utilitários */
.text-center, .mb-20, .shadow, .hidden
```

---

## 🎯 Como Usar

### Iniciar o Servidor
```bash
python3 app.py
```

### Acessar
- **Público:** http://localhost:5000/
- **Admin:** http://localhost:5000/login
- **Token:** `admin123`

---

## 🔧 Personalizar Cores

### Mudar Cores Primárias
Edite `/static/style.css` linhas 7-14:

```css
:root {
    --primary-yellow: #FFD700;    /* Amarelo */
    --primary-blue: #1e40af;      /* Azul */
    --white: #ffffff;              /* Branco */
    /* ... mais cores ... */
}
```

### Mudar Nomes em HTML
- `homepage.html` - Altere "LIGA" e textos
- `admin.html` - Customize títulos
- `semana.html` - Personalize labels

---

## ✅ Testes Realizados

- ✅ Syntax Python (app.py, ranking.py)
- ✅ JSON válido (usuarios.json)
- ✅ CSS sem erros
- ✅ Templates sem erros críticos
- ✅ Responsividade (768px, 480px)
- ✅ Cores aplicadas corretamente
- ✅ Todos os componentes funcionando

---

## 📈 Próximos Passos Opcionais

1. **Banco de Dados Real** (SQLite/PostgreSQL)
2. **Autenticação Melhorada** (Hash de senhas)
3. **Histórico de Pontuações** por semana
4. **Relatórios** em PDF
5. **Mobile App** (React Native/Flutter)
6. **Deploy** (Heroku/AWS)

---

## 📞 Suporte

Qualquer dúvida sobre:
- **CSS:** Veja `/static/style.css`
- **Cores:** Veja `/CORES.md`
- **Documentação:** Veja `/README.md`

---

**Desenvolvido para LIGA - Embaixadores do Rei**  
**Igreja Batista Betsaida**  
🙏