menu = """
[d]: Depositar
[s]: Sacar
[e]: Extrato
[q]: Sair

---> """

saldo=0
limite=500
extrato=''
num_saques=0
limite_saques=3

while True:
    opcao=input(menu).lower()
    if opcao=='d':
        print('Depósito')
        dep=float(input('Quanto gostaria de depositar? R$'))
        saldo+=dep
        extrato+=f'Depósito: R${dep:.2f}\n'

    elif opcao=='s':
        print('Saque')
        saq=float(input('Quanto gostaria de sacar? R$'))
        if saq>limite:
            print(f'\033[31mSEU LIMITE DE VALOR POR SAQUE É DE R$500,00\033[m')
        if saq<=saldo:
            saldo-=saq
            extrato+=f'Saque: {saq:.2f}\n'
            num_saques += 1
            if num_saques > limite_saques:
                print(f'\033[31mVOCÊ JÁ ATINGIU O LIMITE DE SAQUES DIÁRIOS\033[m')
        else:
            print(f'\033[31mVOCÊ NÃO TEM DINHEIRO SUFICIENTE\033[m')

    elif opcao=='e':
        print('Extrato')
        print('\033[33mNão foram realizadas movimentações\033[m' if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')

    elif opcao=='q':
        break
    else:
        print(f'\033[31mOPÇÃO INVÁLIDA!\033[m')