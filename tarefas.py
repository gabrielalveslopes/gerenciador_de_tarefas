from unicodedata import category
import json
from pathlib import Path

ARQUIVO = Path(__file__).with_name("tarefas.json")
tarefas = []


tarefas = []


def criar_tarefa():
    titulo = input("Título da tarefa: ")
    categoria = input("Categoria: ")

    if tarefas:
        novo_id = max(item["id"] for item in tarefas) + 1
    else:
        novo_id = 1

    tarefa = {
    "id": novo_id,
    "titulo": titulo,
    "categoria": categoria,
    "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas()

    print(f'Tarefa {titulo} criada com sucesso!')


def listar_tarefas():

    for item in tarefas:
        if item["concluida"]:
            status = "[✓]"
        else:
            status = "[ ]"
        print(f'{status} {item["id"]} - {item["titulo"]} ({item["categoria"]})')


def concluir_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja concluir: "))

    for item in tarefas:
        if item["id"] == id_tarefa:
            item["concluida"] = True
            salvar_tarefas()
            print("Tarefa concluída com sucesso!")
            return

    print("Tarefa não encontrada!")

def remover_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja remover: "))

    for item in tarefas:
        if item["id"] == id_tarefa:
            tarefas.remove(item)
            salvar_tarefas()
            print("Tarefa removida com sucesso!")
            return

    print("Tarefa não encontrada!")


def salvar_tarefas():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def carregar_tarefas():
    global tarefas

    if ARQUIVO.exists():
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)
