def menu():
    menu = '''\n
    ================ FLUXO ================
    [0] Criar Usuário
    [1] Criar Conta Nova
    [2] Depositar
    [3] Sacar
    [4] Exibir Extrato
    [5] Sair
    ======================================
    O que você deseja? '''
    return input((menu))

print(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito realizado de: R$ {valor:.2f}\n'
        print(extrato)

    else:
        print('Operação falhou! O valor informado é inválido.')
        
    print('==========================================')
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print('Opa! Operação falhou! \nVocê não tem saldo suficiente.')

    elif valor > limite:
        print('Opa! Operação falhou! \nO valor do saque excede o limite.')

    elif numero_saques >= LIMITE_SAQUES:
        print('Opa! Operação falhou! \nNúmero máximo de saques excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque realizado de: R$ {valor:.2f}\n'
        numero_saques += 1
        print(extrato)

    else:
        print('Opa! Operação falhou! \nO valor informado é inválido.')
    
    print('==========================================')
   
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')

        print('==========================================')
    
def criar_usuario(usuarios):
    cpf = int(input('Digite seu CPF (apenas números): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nJá existe usuário com esse CPF!')
        return

    nome = input('Digite seu nome completo: ')
    data_de_nascimento = input('Digite sua data de nascimento (dd/mm/aaaa): ')
    endereco = input('Digite seu endereço (logradouro, nro - bairro, cidade/sigla do estado): ')
    
    usuarios.append({'nome': nome, 'data_de_nascimento': data_de_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário cadastrado!')
    print('==========================================')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(NUMERO_DA_AGENCIA, numero_conta, usuarios):
    cpf = int(input('Digite seu CPF: '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        print('====================================================')

        return {'NUMERO_DA_AGENCIA': NUMERO_DA_AGENCIA, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\nUsuário não encontrado.')
    print('====================================================')

def main():
    LIMITE_SAQUES = 3
    NUMERO_DA_AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    
    while True:
        opcao_escolhida = menu()

        if opcao_escolhida == '0':
            print('\n================ Cadastro ================')
            
            criar_usuario(usuarios)
        
        elif opcao_escolhida == '1':
            print('\n================ Criando conta nova ================')
            
            numero_conta = len(contas) + 1
            conta = criar_conta(NUMERO_DA_AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao_escolhida == '2':
            print('\n================ DEPÓSITO ================')

            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao_escolhida == '3':
            print('\n================ SAQUE ================')

            valor = float(input('Informe o valor do saque: '))
        
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao_escolhida == '4':
            print('\n================ EXTRATO ================')
            
            exibir_extrato(saldo, extrato=extrato)
    
        elif opcao_escolhida == '5':
            print('Obrigado por ser nosso cliente! \nVolte sempre =)')
            break

main()

# Colocar a explicação do código