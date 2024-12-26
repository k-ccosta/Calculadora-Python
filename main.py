import os

def exibir_cabecalho():
    print("-" * 15)
    print("Calculadora Py")
    print("-" * 15)
    print()

def listar_operacoes():
    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão", "Exponenciação"]
    for indice, operacao in enumerate(operacoes):
        print(f"[{indice}] - {operacao}")

def obter_opcao_valida():
    while True:
        try:
            opcao = int(input("\nEscolha uma opção: "))
            if opcao not in range(5): 
                print("\nOPÇÃO INVÁLIDA. Escolha entre 0 e 4.")
            else:
                return opcao
        except ValueError:
            print("\nOPÇÃO INVÁLIDA. Por favor, insira um número inteiro.")

def obter_numeros():
    while True:
        try:
            numero1 = float(input("\nDigite o primeiro número: "))
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

    while True:
        try:
            numero2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido.")
        
    return numero1, numero2

def executar_operacao(opcao, numero1, numero2):
    if opcao == 0:
        print(f"\n{numero1} + {numero2} = {numero1 + numero2}")
    elif opcao == 1:
        print(f"\n{numero1} - {numero2} = {numero1 - numero2}")
    elif opcao == 2:
        print(f"\n{numero1} * {numero2} = {numero1 * numero2}")
    elif opcao == 3:
        if numero2 != 0:
            print(f"\n{numero1} / {numero2} = {numero1 / numero2}")
        else:
            print("\nErro: Divisão por zero não é permitida.")        
    elif opcao == 4:
        print(f"\n{numero1} ** {numero2} = {numero1 ** numero2}")

def continuar_ou_encerrar():
    while True:
        resposta = input("\nDeseja realizar outra operação?\n[S]/[N]: ").upper().strip()
            
        if resposta not in ["S", "N"]:
            print("Erro: Por favor, insira 'S' para Sim ou 'N' para Não.")
        else:
            break

    if resposta == "S":
        os.system("cls" if os.name == "nt" else "clear")
        iniciar_calculadora()
    else: 
        os.system("clear")
        print("Encerrando calculadora. Até logo!") 

def iniciar_calculadora():
    exibir_cabecalho()
    listar_operacoes()
    opcao = obter_opcao_valida()
    numero1, numero2 = obter_numeros()
    executar_operacao(opcao, numero1, numero2)
    continuar_ou_encerrar()

iniciar_calculadora()