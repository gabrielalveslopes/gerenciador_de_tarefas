from tarefas import criar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa, carregar_tarefas

def menu():
    print("\n=== DEV TASK CLI ===")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")


carregar_tarefas()


while True:
    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        criar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        concluir_tarefa()

    elif opcao == "4":
        remover_tarefa()

    elif opcao == "5":
        print("Até mais!")
        break

    else:
        print("Opção inválida.")