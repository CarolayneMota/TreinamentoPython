import geometria as geo
opcao = int(input('Informe o número da figura que você que saber a área.\n1. Circulo\n2. Quadrado\nR: '))
if opcao == 1:
    raio = float(input('Informe o raio em cm: '))
    area = geo.area_circulo(raio)
    print(f'A área do círculo de raio {raio} é {area}cm')
elif opcao == 2:
    tam = float(input('Informe o tamanho do lado em cm: '))
    area = geo.area_quadrado(tam)
    print(f'A área do quadrado de lado {tam}cm é {area}cm ')
else:
    print('Opção invalida')
