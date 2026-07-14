import os
import json


controle_de_gastos = []

def inicializar_json():
    if os.path.exists("controle_dos_gastos.json"):
        with open("controle_dos_gastos.json", "r", encoding="utf-8") as f:
            controle_de_gastos = json.load(f)

def save():
    with open("controle_de_gastos.json", "w", encoding="utf-8") as f:
        json.dump(controle_de_gastos, f, ensure_ascii=False, indent=2)
        