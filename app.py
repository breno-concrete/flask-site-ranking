from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os
from functools import wraps
from models.ranking import calc_ranking

app = Flask(__name__)
app.secret_key = "sua_chave_secreta_aqui" 

# Token de admin 
ADMIN_TOKEN = "admin123"
DATA_FILE = "data/usuarios.json"

# Decorador para verificar autenticação
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token') or session.get('token')
        if not token or token != ADMIN_TOKEN:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# Carregar dados do JSON
def carregar_dados():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Salvar dados no JSON
def salvar_dados(dados):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# Rotas
@app.route("/")
def home():
    ranking = calc_ranking(DATA_FILE)
    return render_template("homepage.html", ranking=ranking)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        token = request.form.get('token')
        if token == ADMIN_TOKEN:
            session['token'] = token
            return redirect(url_for('admin'))
        else:
            return render_template("login.html", erro="Token inválido")
    return render_template("login.html")

@app.route("/admin")
@token_required
def admin():
    dados = carregar_dados()
    ranking = calc_ranking(DATA_FILE)
    return render_template("admin.html", usuarios=dados['usuarios'], ranking=ranking)

@app.route("/admin/add", methods=["POST"])
@token_required
def admin_add():
    dados = carregar_dados()
    novo_id = max([u['id'] for u in dados['usuarios']], default=0) + 1
    novo_usuario = {
        'id': novo_id,
        'nome': request.form.get('nome'),
        'nascimento': request.form.get('nascimento'),
        'pontuacao': int(request.form.get('pontuacao', 0)),
        'classe': request.form.get('classe', 'Escudeiro')
    }
    dados['usuarios'].append(novo_usuario)
    salvar_dados(dados)
    return redirect(url_for('admin'))

@app.route("/admin/edit/<int:user_id>", methods=["POST"])
@token_required
def admin_edit(user_id):
    dados = carregar_dados()
    usuario = next((u for u in dados['usuarios'] if u['id'] == user_id), None)
    if usuario:
        usuario['nome'] = request.form.get('nome', usuario['nome'])
        usuario['pontuacao'] = int(request.form.get('pontuacao', usuario['pontuacao']))
        usuario['classe'] = request.form.get('classe', usuario['classe'])
        usuario['nascimento'] = request.form.get('nascimento', usuario['nascimento'])
        salvar_dados(dados)
    return redirect(url_for('admin'))

@app.route("/admin/delete/<int:user_id>", methods=["POST"])
@token_required
def admin_delete(user_id):
    dados = carregar_dados()
    dados['usuarios'] = [u for u in dados['usuarios'] if u['id'] != user_id]
    salvar_dados(dados)
    return redirect(url_for('admin'))

@app.route("/admin/semana")
@token_required
def admin_semana():
    dados = carregar_dados()
    ranking = calc_ranking(DATA_FILE)
    return render_template("semana.html", usuarios=dados['usuarios'], ranking=ranking)

@app.route("/admin/semana/adicionar", methods=["POST"])
@token_required
def admin_semana_adicionar():
    dados = carregar_dados()
    
    # Processar cada usuário 
    for usuario in dados['usuarios']:
        pontos_semana = request.form.get(f'pontos_{usuario["id"]}')
        if pontos_semana and pontos_semana.strip():
            try:
                pontos = int(pontos_semana)
                usuario['pontuacao'] += pontos
            except ValueError:
                pass
    
    salvar_dados(dados)
    return redirect(url_for('admin_semana'))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True) 