from models.carro import Carro

def menu():
    print("\n=== SISTEMA DE CADASTRO DE CARROS ===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("0 - Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR CARRO ---")
        print("\nEscolha a marca:")
        print("1 - Ford")
        print("2 - Chevrolet")
        print("3 - Volkswagen")

        op_marca = input("Opção: ")

        if op_marca == "1":
            marca = "Ford"
        elif op_marca == "2":
            marca = "Chevrolet"
        elif op_marca == "3":
            marca = "Volkswagen"
        else:
            print("Opção inválida!")
        
        print("\nEscolha o modelo:")

        if marca == "Ford":
            print("1 - Fiesta")
            print("2 - Focus")
            print("3 - Mustang")
            op_modelo = input("Opção: ")
            if op_modelo == "1":
                modelo = "Fiesta"
            elif op_modelo == "2":
                modelo = "Focus"
            elif op_modelo == "3":
                modelo = "Mustang"
            else:
                print("Opção inválida!")
        elif marca == "Chevrolet":
            print("1 - Onix")
            print("2 - Cruze")
            print("3 - Camaro")
            op_modelo = input("Opção: ")
            if op_modelo == "1":
                modelo = "Onix"
            elif op_modelo == "2":
                modelo = "Cruze"
            elif op_modelo == "3":
                modelo = "Camaro"
            else:
                print("Opção inválida!")
        elif marca == "Volkswagen":
            print("1 - Gol")
            print("2 - Polo")
            print("3 - Golf")
            op_modelo = input("Opção: ")
            if op_modelo == "1":
                modelo = "Gol"
            elif op_modelo == "2":
                modelo = "Polo"
            elif op_modelo == "3":
                modelo = "Golf"
            else:
                print("Opção inválida!")
        
        ano = input("Digite o ano do carro:  (Apenas números) ")

        while ano.isdigit() == False:
            print("Ano inválido! Digite apenas números.")
            ano = input("Digite o ano do carro: ")

        carro = Carro(marca, modelo, ano)
        carro.salvar_carro()

    elif opcao == "2":
        print("\n--- LISTA DE CARROS ---")

        lista = Carro("", "", "").carregar_todos()

        if not lista:
            print("Nenhum carro cadastrado ainda.")
        else:
            for c in lista:
                print(f"{c['marca']} - {c['modelo']} - {c['ano']}")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

