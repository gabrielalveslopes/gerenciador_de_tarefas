def menu():
    print("\n=== DEV TASK CLI ===")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")


while True:
    menu()

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("Criar tarefa")

    elif opcao == "2":
        print("Listar tarefas")

    elif opcao == "3":
        print("Concluir tarefa")

    elif opcao == "4":
        print("Remover tarefa")

    elif opcao == "5":
        print("Até mais!")
        break

    else:
        print("Opção inválida.")