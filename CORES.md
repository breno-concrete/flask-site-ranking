# 🎨 Paleta de Cores - LIGA

## Cores Oficiais

### Amarelo (Ouro)
- **Primário:** `#FFD700` (Gold)
- **Acento:** `#fbbf24` (Amber)
- Uso: Destaque, botões, bordas

### Azul (Real)
- **Primário:** `#1e40af` (Blue-900)
- **Secundário:** `#3b82f6` (Blue-500)
- **Escuro:** `#0f172a` (Slate-950)
- Uso: Headers, backgrounds, texto

### Branco
- **Branco:** `#ffffff`
- **Claro:** `#f8fafc` (Slate-50)
- **Cinza:** `#e2e8f0` (Slate-200)
- Uso: Backgrounds, cards, texto

## Gradientes Principais

### Header
```css
background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
```

### Buttons
```css
background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
```

### Button Warning (Dourado)
```css
background: linear-gradient(135deg, #fbbf24 0%, #fbbf24 100%);
```

## Variáveis CSS

```css
:root {
    --primary-yellow: #FFD700;
    --primary-blue: #1e40af;
    --light-blue: #3b82f6;
    --dark-blue: #0f172a;
    --white: #ffffff;
    --light-gray: #f8fafc;
    --gray: #e2e8f0;
    --dark-gray: #64748b;
    --accent-gold: #fbbf24;
}
```

## Aplicação

### Backgrounds
- Hero/Header: Azul Gradiente
- Página: Azul Escuro Gradiente
- Cards: Branco

### Textos
- Títulos: Azul Primário (#1e40af)
- Corpo: Cinza Escuro (#64748b)
- Links: Azul Primário

### Destaque
- Amarelo/Ouro (#FFD700)
- Usado em bordas, badges, botões especiais

## Temas Especiais

### Info Box
```css
background: rgba(59, 130, 246, 0.1);
border-left: 5px solid #1e40af;
```

### Success Box
```css
background: rgba(34, 197, 94, 0.1);
border-left: 5px solid #22c55e;
```

### Warning Box
```css
background: rgba(251, 191, 36, 0.1);
border-left: 5px solid #FFD700;
```

## Sombras

```css
box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
```

## Transições

```css
transition: all 0.3s ease;
```