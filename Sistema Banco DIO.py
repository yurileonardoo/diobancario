saldo = 0
valor_deposito = 0
valorlimite_saque = 500
extrato = ""
numero_saques = 0
numlimite_saque = 3

while True:
    print('\n==== Bem vindo ao Banco Fsn! ====\n==== Selecione uma operação pelo número: ====\n')
    opcao = int(input('1 - Depósito\n2 - Saque\n3 - Extrato\n0 - Sair\n'))
    
    if opcao == 1:
        valor_deposito = float(input('Digite o valor que será depositado: '))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R${valor_deposito:.2f} realizado.\n"
        
        else:
            print('Operação não sucedida. O valor informado é inválido.')    
    
    elif opcao == 2:
        if numero_saques == numlimite_saque:
            print('Limite de saques diários realizados.')
            continue        
        valor_saque = float(input('Digite o valor que será sacado: '))
        if valor_saque < 0:
            print('Operação não sucedida. O valor informado é inválido.')
                    
        if valor_saque <= saldo:
            if valor_saque > 500:
                print('Operação não sucedida. O valor máximo de um saque é de R$500,00')
            else:
                saldo-=valor_saque
                extrato += f"Saque de R${valor_saque:.2f} realizado.\n"
                numero_saques += 1
        
        else:
            print('Você não possui saldo suficiente para o saque.')
    
    elif opcao == 3:
        print("\n============= EXTRATO =============")  
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSALDO: R${saldo:.2f}")
        print("=====================================")
    
    elif opcao == 0:
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
