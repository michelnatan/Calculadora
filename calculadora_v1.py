
import os

# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************\n")

continuar = 's'

while(continuar == 's' or continuar == 'S'):
    print("Selecione o número da operação desejada:\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n")

    menu = int(input("Digite sua opção (1/2/3/4):"))

    if menu > 4 or menu < 1:
        print("\nOpção Inválida!")
        ##exit()
        continuar = input("Desejar fazer outro calculo (S=SIM / N=NÃO) ?")
        os.system("cls") 
        continue

    try:
        num1 = int(input("\nDigite o primeiro número:"))
    except ValueError:
        print("\n## Operação não permitida ##\n")
        continue
    try:
        num2 = int(input("Digite o segundo número:"))
    except ValueError:
        print("\n## Operação não permitida ##=\n")
        continue
    
    print("")   

    ##Definindo case para o menu utilizando um dicionario(opção selecionada(valor da variavel menu) + nome da variavel)
    def soma():
        print("## Modo soma ##")
        print(num1,"+", num2, "=", num1+num2)
    def subtracao():
        print("## Modo subtracao ##")
        print(num1,"-", num2, "=", num1-num2)
    def multiplicacao():
        print("## Modo multiplicação ##")
        print(num1,"*", num2, "=", num1*num2)
    def divisao():
        print("## Modo divisão ##")
        try:
            print(num1,"/", num2, "=", num1/num2)
        except ZeroDivisionError:
            print (num1,"/", num2, "= " '0')
            
    menus = { 1:soma, 2:subtracao, 3:multiplicacao, 4:divisao}
    menus.get(menu)()
    
    input("\nPress Enter to continue...")
    os.system("cls")
    
    continuar = input("Desejar fazer outro calculo (S=SIM / N=NÃO) ?")
    os.system("cls")
    