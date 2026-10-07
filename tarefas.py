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