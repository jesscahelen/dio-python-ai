def menu():
    menu = '''
    [1] depositar
    [2] sacar
    [3] extrato
    [4] criar usuário
    [5] criar conta corrente
    [0] sair

    -> '''
    return input(menu)

def deposito(saldo, extrato_impressao, /):
    quantidade = float(input('Digite a quantidade a ser depositada: '))
    if (quantidade > 0):
        saldo += quantidade
        extrato_impressao += f'Depósito R$ {quantidade:.2f}\nSaldo: R$ {saldo:.2f}\n==============================\n'
        print('Valor R$ %.2f depositado com sucesso.' %quantidade)
    else:
        print('Operação negada. Quantidade de depósito inválida.')
    return saldo, extrato_impressao

def saque(saldo, numero_saques, limite_saques, limite, extrato_impressao):
    quantidade = float(input('Digite a quantidade a ser depositada: '))

    saldo_insuficiente = quantidade > saldo
    sem_limite_de_saques = numero_saques >= limite_saques
    limite_de_saque_ultrapassado = quantidade > limite
    numero_negativo = quantidade <= 0

    if saldo_insuficiente:
        print('Operação negada. Saldo insuficiente.')
    elif sem_limite_de_saques:
        print('Operação negada. Limite de saques atingido.')
    elif limite_de_saque_ultrapassado:
        print('Operação negada. Valor maior do que limite permitido para saque.')
    elif numero_negativo:
        print('Operação negada. Quantidade de saque inválida.')
    else:
        saldo -= quantidade
        numero_saques += 1
        extrato_impressao += f'Saque R$ {quantidade:.2f}\nSaldo: R$ {saldo:.2f} \n==============================\n'
        print('Valor R$ %.2f sacado com sucesso.' %quantidade)
    return saldo, extrato_impressao, numero_saques

def extrato(extrato_impressao, saldo, /):
    if (extrato_impressao == ''):
        print('Saldo: R$ %.2f' %saldo)
    else:
        print(extrato_impressao)
        return extrato_impressao

def usuario_existe(usuarios, cpf, /):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False

def criar_usuario(usuarios):
    cpf = input('Digite o cpf do usuário: ')
    cpf = cpf.replace('.', '').replace('-', '')
    if not usuario_existe(usuarios, cpf):
        nome = input('Digite o nome do usuário: ')
        data_nascimento = input('Digite a data de nascimento. formato dd/MM/yyyy: ')
        endereco = input('Digite o endereço: ')
        usuario = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
        usuarios.append(usuario)
        return usuarios
    else:
        print(f'Usuário com CPF %s já existe' %cpf)
        return usuarios

def criar_conta_corrente(usuarios, numero_conta, contas_correntes, /):
    cpf = cpf = input('Digite o cpf do usuário: ')
    cpf = cpf.replace('.', '').replace('-', '')
    if usuario_existe(usuarios, cpf):
        numero_conta =+ 1
        conta_corrente = {'agencia': '0001', 'numero_conta': numero_conta, 'usuario': cpf}
        contas_correntes.append(conta_corrente)
        return contas_correntes, numero_conta
    else:
        print(f'Usuário com CPF %s não existe' %cpf)
        return contas_correntes, numero_conta

def main():
    saldo = 0.0
    limite = 500
    extrato_impressao = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas_correntes = []
    numero_conta = 0

    while True:
        opcao = menu()

        if opcao == '1':
            saldo, extrato_impressao = deposito(saldo, extrato_impressao)
        elif opcao == '2':
            saldo, extrato_impressao, numero_saques = saque(saldo=saldo, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, limite=limite, extrato_impressao=extrato_impressao)
        elif opcao == '3':
            extrato_impressao = extrato(extrato_impressao, saldo)
        elif opcao == '4':
            usuarios = criar_usuario(usuarios)
        elif opcao == '5':
            contas_correntes, numero_conta = criar_conta_corrente(usuarios, numero_conta, contas_correntes)
        elif opcao == '0':
            break
        else:
            print('Opção inválida, selecione a opção desejada.')

main()
