def saque(*, saldo, saq, limite, limite_saques, num_saques, opcao, extrato):
    if opcao == 's':
        print('Saque')
        saq = float(input('Quanto gostaria de sacar? R$'))
        if saq > limite:
            print('\033[31mSEU LIMITE DE VALOR POR SAQUE É DE R$500,00\033[m')
        elif saq > saldo:
            print('\033[31mVOCÊ NÃO TEM DINHEIRO SUFICIENTE\033[m')
        elif num_saques >= limite_saques:
            print('\033[31mVOCÊ JÁ ATINGIU O LIMITE DE SAQUES DIÁRIOS\033[m')
        else:
            saldo -= saq
            extrato += f'Saque: R$ {saq:.2f}\n'
            return saldo, extrato, True #contabiliza no num_saques
    return saldo, extrato, False #nao contabiliza no num_saques

def deposito(saldo,extrato):
    print('Depósito')
    dep=float(input('Quanto gostaria de depositar? R$'))
    saldo+=dep
    extrato+=f'Depósito: R${dep:.2f}\n'
    return saldo,extrato

def extr(saldo,*,extrato):
    print('Extrato')
    print('\033[33mNão foram realizadas movimentações\033[m' if not extrato else extrato)
    print(f'Saldo: R${saldo:.2f}')
    return saldo,extrato

def criar_usuario(usuarios):
    nm = input('Insira o nome: ')
    data_nasc = input('Insira sua data de nascimento (DD/MM/AAAA): ')
    if data_nasc.count('/') != 2:
        print('\033[31mINSIRA UM FORMATO DE DATA VÁLIDO (DD/MM/AAAA)\033[m')
        return
    cpf = input('Insira o CPF (apenas números): ')
    cpf_existe = any(usuario[2] == cpf for usuario in usuarios)
    if cpf_existe:
        print('\033[31mCPF JÁ CADASTRADO NO SISTEMA!\033[m')
        return
    endereco = input('Insira seu endereço: ')
    novo_usuario = [nm, data_nasc, cpf, endereco]
    usuarios.append(novo_usuario)
    print('\033[32mUSUÁRIO CADASTRADO COM SUCESSO!\033[m')

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario[2] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, user):
    cpf = input('Insira o CPF do titular da conta: ') 
    usuario = filtrar_usuario(cpf, user)
    if usuario:
        print('Conta criada com sucesso!')
        return agencia, num_conta, usuario
    print('\033[31mNão foi possível encontrar o usuário')
    return None

contas=[]

menu = """
[d]: Depositar
[s]: Sacar
[e]: Extrato
[q]: Sair
[c]: Criar usuário
[t]: Criar conta

---> """

saldo=0
limite=500
extrato=''
num_saques=0
limite_saques=3
usuarios = []
numero_conta=1

while True:
    opcao=input(menu).lower()
    if opcao=='d':
        saldo,extrato=deposito(saldo,extrato)
       
    elif opcao=='s':
        saldo,extrato,num_saques=saque(
            saldo=saldo,
            saq=0,
            limite=limite,
            limite_saques=limite_saques,
            num_saques=num_saques,
            opcao=opcao,
            extrato=extrato
        )
    elif opcao=='e':
       saldo,extrato=extr(saldo,extrato=extrato)
    elif opcao == 'c':
        criar_usuario(usuarios)
    elif opcao == 't':
        resultado = criar_conta(agencia='0001', num_conta=numero_conta, user=usuarios)
        if resultado:
            agencia, numero, usuario = resultado
            contas.append({'agencia': agencia, 'numero': numero, 'user': usuario})
            numero_conta += 1  # incrementa o número da próxima conta
    elif opcao=='q':
        break
    else:
        print(f'\033[31mOPÇÃO INVÁLIDA!\033[m')
