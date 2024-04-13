menu = """ 
    Escolha a Operação desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
    
=> """

extrato = ""
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input(f"Quantos reais deseja depositar? "))
       
        if valor > 0 :
            saldo  += valor
            extrato += f"Depósito: R${valor:.2f}\n"
       
        else:
            print(f"Depósito não realizado! Valor inválido!")
    
    elif opcao == "s":
        valor = float(input("Qual valor deseja sacar? "))
       
        if (valor <= saldo) and (numero_saques < LIMITE_SAQUES) and (valor <= 500)  :
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print(f"Escolha novamente a operação que deseja realizar: ")
       
        elif (valor > saldo):
            print(f"Saldo insuficiente!")
                    
        elif (valor <= saldo) and (numero_saques > LIMITE_SAQUES):
            print(f"Limite diário de saques excedido!")
            
        elif (valor <= saldo) and (numero_saques <= LIMITE_SAQUES) and (valor > 500): 
            print(f"Valor solicitado superior ao limite por saque!")
            
    elif opcao == "e":
        print("\n------------Extrato--------------")
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print(" ---------------------------------")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
