#Programa para Saque Bancário e Consulta de Saldo em Python

### Neste programa, o usuário seleciona as opções 1 para Saque ou 2 para Consulta de Saldo.

### Caso seja selecione a opção 1, Informa o valor que quer sacar, e como resposta terá saque realizado ou saldo insuficiente.

### Caso seja opção 2, é informado o saldo em conta.

### Caso o usuário insira valor diferente de 1 ou 2, o programa informa que a opção está inválida,
### e o mesmo pode selecionar novas opções, 1 para retornar ao menu anterior e 2 para sair, este último encerra o programa.


saldo = 250

while True:
    opcao = int(input("Informe uma opção: \n[1] - Sacar \n[2] - Extrato\n ->:"))

    if opcao == 1:
        valor = float(input("Informe a quantia para o saque: "))
        if valor <= saldo:
            print("Saque realizado!\nTenha um bom dia!\n")
            
        else:
            print("Saldo insuficiente!\n")
        

    elif opcao == 2:
        print(f"Seu saldo bancário é de: {saldo} reais\n")

    else: 
        print("Opção inválida, tente novamente!\n")
        
        opcao2 = int(input("Gostaria de voltar ao menu anterior?\n Digite [1] para SIM e [2] para NAO: "))
        if opcao2 == 1:
            print(opcao)
        elif opcao2 == 2:
            print("Consulta encerrada!\nTenha um bom dia!\n") 
            break
        





