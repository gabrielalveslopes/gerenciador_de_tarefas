from unicodedata import category


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
            print("Tarefa concluída com sucesso!")
            return

    print("Tarefa não encontrada!")

def remover_tarefa():
    id_tarefa = int(input("Digite o ID da tarefa que deseja remover: "))

    for item in tarefas:
        if item["id"] == id_tarefa:
            tarefas.remove(item)
            print("Tarefa removida com sucesso!")
            return

    print("Tarefa não encontrada!")
