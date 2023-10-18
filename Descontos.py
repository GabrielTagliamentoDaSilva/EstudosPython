#Criando um valor que da desconto com base na quantidade de items adquiridos então quanto maior é o valor final do produto maior é o desconto
def desconto():
    #Váriavel continuar recebendo o valor True para conseguir desativar o loop
    continuar = True
    #Laço de repetição para pedir os inputs aos usúarios
    while continuar:
        #printando na tela uma mensagem de boas-vindas
        print("====Bem vindo ao  app de descontos====")
        #Solicitando inputs ao usuário
        valor = int(input("Digite o valor do produto:"))
        quantidade = int(input("Digite  a quantidade do produto:"))
        valorTotal = valor*quantidade
        #Usando condicionais para fazer a checagem dos valores e seus descontos a serem aplicados
        if valorTotal <=1000:
            print("O desconto adquirido é de 0% e o valor total a se pagar foi R${:.2f}".format(valorTotal))
            continuar = input("Para continuar digite sim").upper()

        elif valorTotal >= 1000 and valorTotal <3000:
            valorFinal = valorTotal - (0.3 * 100)
            print("O valor do produto ficou R${:.2f} e o valor com desconto 3% foi R${:.2f}".format(valorTotal,valorFinal))
            continuar = input("Para continuar digite sim").upper()

        elif valorTotal >= 3000 and valorTotal <=5000:
            valorFinal = valorTotal - (0.5*100)
            print("O valor do produto ficou R${:.2f} e o valor com desconto 5% foi R${:.2f}".format(valorTotal, valorFinal))
            continuar = input("Para continuar digite sim").upper()


        elif valorTotal > 5000:
            valorFinal = valorTotal - (0.8 * 100)
            print("O valor do produto ficou R${:.2f} e o valor com desconto 8% foi R${:.2f}".format(valorTotal,valorFinal))
            continuar = input("Para continuar digite sim").upper()

        if continuar =="SIM":
            print("continuando programa")
        else:
            print("\nMuito obrigado por utilizar nosso programa")
            break
desconto()