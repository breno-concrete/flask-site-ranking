# Liga Ranking - Sistema de Gerenciamento de Pontuações

Um site completo para gerenciar rankings com autenticação por token e adição de pontuações semanais.

## 🚀 Funcionalidades

### Para Usuários (Público)
- 👀 Visualizar ranking completo e atualizado
- 🥇 Ver posições, pontuações e classes

### Para Admin (Protegido por Token)
- 👤 **Gerenciar Usuários**: Adicionar, editar e deletar
- 📊 **Pontuação Semanal**: Adicionar pontos para múltiplos usuários com soma automática
- ✏️ **Edição Direta**: Modificar pontos, classe e dados
- 📈 **Preview em Tempo Real**: Ver mudanças antes de salvar

## 📋 Instalação

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o aplicativo
```bash
python3 app.py
```

O servidor rodará em `http://localhost:5000`

## 🔐 Autenticação

**Token de Admin Padrão**: `admin123`

⚠️ **Mude o token em `app.py`** para algo mais seguro antes de colocar em produção:
```python
ADMIN_TOKEN = "seu_token_seguro_aqui"
```

## 📍 Rotas Disponíveis

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Homepage com ranking público |
| `/login` | GET, POST | Página de login para admin |
| `/admin` | GET | Dashboard de gerenciamento de usuários |
| `/admin/add` | POST | Adicionar novo usuário |
| `/admin/edit/<id>` | POST | Editar usuário |
| `/admin/delete/<id>` | POST | Deletar usuário |
| `/admin/semana` | GET | Página de pontuação semanal |
| `/admin/semana/adicionar` | POST | Submeter pontuação semanal |
| `/logout` | GET | Sair da sessão |

## 💡 Como Usar a Pontuação Semanal

1. Acesse o **Dashboard Admin** (`/admin`)
2. Clique em **"📊 Pontuação Semanal"**
3. Digite os pontos conquistados por cada usuário naquela semana
4. Veja a **Nova Pontuação** atualizar em tempo real
5. Clique em **"✅ Salvar Pontuação Semanal"**
6. Os pontos serão automaticamente somados à pontuação existente

## 📁 Estrutura do Projeto

```
liga_ranking/
├── app.py                 # Aplicação principal Flask
├── data/
│   └── usuarios.json      # Banco de dados (JSON)
├── models/
│   └── ranking.py         # Lógica de cálculo de ranking
├── static/
│   └── style.css          # Estilos CSS
├── templates/
│   ├── homepage.html      # Página pública de ranking
│   ├── login.html         # Página de login
│   ├── admin.html         # Dashboard admin
│   └── semana.html        # Página de pontuação semanal
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

## 📊 Formato do JSON de Usuários

```json
{
  "usuarios": [
    {
      "id": 1,
      "nome": "Nome do Usuário",
      "nascimento": "DD/MM/YYYY",
      "pontuacao": 100,
      "classe": "Escudeiro"
    }
  ]
}
```

### Classes Disponíveis
- Escudeiro (padrão)
- Cavaleiro
- Nobre
- Lenda

## 🔧 Modificações Recomendadas

### 1. Mudar Token de Admin
Em `app.py`, linha 12:
```python
ADMIN_TOKEN = "seu_novo_token_seguro"
```

### 2. Mudar Chave Secreta
Em `app.py`, linha 9:
```python
app.secret_key = "sua_chave_secreta_muito_segura_aqui"
```

### 3. Adicionar Novas Classes
Em `semana.html` e `admin.html`, procure pelo `<select>` e adicione:
```html
<option value="Nova Classe">Nova Classe</option>
```

## 🎨 Customização

### Cores
Os estilos estão em `static/style.css` e em cada template. Procure por:
- `#667eea` - Cor primária
- `#333` - Cor secundária
- `#ff4444` - Cor de perigo

### Emojis
Todos os títulos usam emojis para melhor UX. Altere conforme desejar.

## ⚠️ Notas de Segurança

- **Nunca** use `debug=True` em produção
- Altere o `ADMIN_TOKEN` e `app.secret_key` antes de publicar
- Faça backup regular do arquivo `data/usuarios.json`
- Considere usar um banco de dados real (SQLite, PostgreSQL) em produção

## 📝 Licença

Projeto desenvolvido para fins educacionais.

## 🤝 Contribuições

Sinta-se à vontade para melhorar e adaptar este projeto!