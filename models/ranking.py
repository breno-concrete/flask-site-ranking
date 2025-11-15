import json
from datetime import datetime

def calc_ranking(dados_json="data/usuarios.json"):
    with open(dados_json, "r", encoding="utf-8") as f:
        dados = json.load(f)

    usuarios = dados["usuarios"]

    ordenado = sorted(usuarios, key=lambda x: x["pontuacao"], reverse=True) 

    ranking = []

    for posicao, u in enumerate(ordenado, start=1):
        ranking.append({
            "posicao": posicao,
            "id": u["id"],
            "nome": u["nome"],
            "pontuacao": u["pontuacao"],
            "classe": u["classe"],
            "nascimento": u["nascimento"]
        })
    return ranking

