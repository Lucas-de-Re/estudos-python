import os
import json

def inicializar_json():
    if os.path.exists("controle_de_gastos.json"):
        with open("controle_de_gastos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []
controle_de_gastos = inicializar_json()

def save():
    with open("controle_de_gastos.json", "w", encoding="utf-8") as f:
        json.dump(controle_de_gastos, f, ensure_ascii=False, indent=2)
        