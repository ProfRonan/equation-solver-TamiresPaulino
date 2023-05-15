recebe_num = int(input('Qual o grau da função: '))

if recebe_num < 1 or recebe_num > 2:

    print('Grau inválido')

if recebe_num == 1:

    print('A equação é do primeiro grau.')
    a = int(input('Digite um valor para "a": '))

    if a == 0:
        print('Valor de a inválido')
    elif a != 0:

        b = int(input('Digite um valor para "b": '))
        resul = -(b/a)
        print(f'{resul:.2f}')

if recebe_num == 2:
    print('A equação é do segundo grau.')
    a = int(input('Digite um valor para "a": '))

    if a == 0: 
        print('Valor de a inválido')
    elif a != 0:

        b = int(input('Digite um valor para "b": '))
        c = int(input('Digite um valor para "c": '))
        delta=((b**2) - 4*(a)*(c))
        
        if delta < 0:
            print('A equação não possui raízes reais')
           
        elif delta == 0:
            print('A equação possui uma raiz real')
            raiz= -(b)/(2*a)

            print(f'{raiz:.2f}')
        elif delta > 0: 
            print('A equação possui duas raízes reais')

            raiz_um = ((-b) + (delta**0.5))/(2*a)
            raiz_dois = ((-b) - (delta**0.5))/(2*a)
            print(f'{raiz_dois:.2f}')
            print(f'{raiz_um:.2f}')
         