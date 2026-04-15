import json
from datetime import datetime

tarefas = []
proximo_id = 1

def salvar_dado():
    """Salva o estado atual das tarefas no arquivo JSON."""
    global proximo_id, tarefas
    with open('tarefas.json', 'w') as f:
        dados_para_salvar = {
            'proximo_id': proximo_id, 
            'tarefas': tarefas
        }
        json.dump(dados_para_salvar, f, indent=4)

def carregar_dados():
    """Lê os dados do arquivo JSON ao iniciar o app."""
    global proximo_id, tarefas
    try:
        with open('tarefas.json', 'r') as f:
            dado = json.load(f)
            tarefas = dado['tarefas']
            proximo_id = dado['proximo_id']
    except (FileNotFoundError, KeyError, json.JSONDecodeError):
        pass

def adicionar_tarefa(texto):
    global proximo_id
    tarefas.append({
        'id': proximo_id,
        'texto': texto,
        'feito': False,
        'data_criacao': datetime.now().strftime("%d/%m %H:%M")
    })
    proximo_id += 1

def completar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['feito'] = True
            break