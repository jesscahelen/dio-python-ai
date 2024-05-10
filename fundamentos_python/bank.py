menu = """

[1] depositar
[2] sacar
[3] extrato
[0] sair

-> """

saldo = 0.0
limite = 500
extrato_impressao = ""
numero_saques = 0
LIMITE_SAQUES = 3
    

while True:
    opcao = input(menu)

    if opcao == "1":
        quantidade = float(input("Digite a quantidade a ser depositada: "))
        if (quantidade > 0):
            saldo += quantidade
            extrato_impressao += f"Depósito R$ {quantidade:.2f}\nSaldo: R$ {saldo:.2f}\n==============================\n"
            print("Valor R$ %.2f depositado com sucesso." %quantidade)
        else:
            print("Operação negada. Valores devem ser positivos.")
    elif opcao == "2":  
        quantidade = float(input("Digite a quantidade a ser depositada: "))
        if (numero_saques <= LIMITE_SAQUES and quantidade <= limite):
            if (quantidade > 0) and (quantidade <= saldo):
                saldo -= quantidade
                numero_saques += 1
                extrato_impressao += f"Saque R$ {quantidade:.2f}\nSaldo: R$ {saldo:.2f} \n==============================\n"
                print("Valor R$ %.2f sacado com sucesso." %quantidade)
            else:
                print("Operação negada. Quantidade incompatível com o saldo.")
        else:
            print("Operação negada. Limite de saques foi atingido.")
    elif opcao == "3":
        if (extrato_impressao == ""):
            print("Saldo: R$ %.2f" %saldo)
        else:
            print(extrato_impressao)
    elif opcao == "0":
        break
    else:
        print("Opção inválida, selecione a opção desejada.")
