import geometria as geo
opcao = int(input('Informe o número da figura que você que saber a área.\n1. Circulo\n2. Quadrado'))
if opcao == 1:
    raio = float(input('Informe o raio em cm: '))
    geo.area_circulo(raio)
elif opcao == 2:
    tam = float(input('Informe o tamanho do lado em cm: '))
    geo.area_quadrado(tam)
else:
    print('Opção invalida')
