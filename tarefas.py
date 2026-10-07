from unicodedata import category


tarefas = []


def criar_tarefa():
    titulo = input("Título da tarefa: ")
    categoria = input("Categoria: ")

    tarefa = {
    "id": len(tarefas) + 1,
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

        
