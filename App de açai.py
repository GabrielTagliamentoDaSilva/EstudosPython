def acai():
      continuar = True
      valorTotal = 0
      while continuar ==True:
            produto =input("Escolha Cupuaçu(CPU) ou Açai(AC) digite a sigla do produto\n"
                           "---Tamanho---Sabor---  Preço   ---\n"
                           "---   P   --- CPU  ---  R$10  ---\n"
                           "---   M   --- CPU  ---  R$15  ---\n"
                           "---   G   --- CPU  ---  R$19  ---\n"
                           "---   P   --- AC   ---  R$12 ---\n"
                           "---   M   --- AC   ---  R$17 ---\n"
                           "---   G   --- AC   ---  R$21 ---\n"
                           ">>>").upper()
            tamanho = input("Escolha o tamanho do produto(P/M/G)\n"
                            ">>>").upper()

            if produto =="CPU" and  tamanho =="P":
                  valorTotal+=10
                  print("\nVocê escolheu cupuaçu tamanho pequeno no valor de 10 o valor a se pagar é R${:.2f}".format(valorTotal))
                  confirmar = input("Deseja continuar S/N:").upper()
                  if confirmar =="N":
                        print("Finalizando")
                        break
                  else:
                        continue
            elif produto =="CPU" and tamanho =="M":
                  valorTotal+=15
                  print("\nVocê escolheu cupuaçu tamanho médio no valor de 15 o valor a se pagar é R${:.2f}".format(valorTotal))
                  confirmar = input("Deseja continuar S/N:").upper()
                  if confirmar == "N":
                        print("Finalizando")
                        break
                  else:
                        continue

            elif produto == "CPU" and tamanho == "G":
                  valorTotal += 19
                  print("\nVocê escolheu cupuaçu tamanho grande no valor de 19 o valor a se pagar é R${:.2f}".format(
                        valorTotal))
                  confirmar = input("Deseja continuar S/N:").upper()
                  if confirmar == "N":
                        print("Finalizando")
                        break
                  else:
                        continue
            elif produto == "AC" and tamanho == "P":
                  valorTotal += 12
                  print("\nVocê escolheu açai tamanho pequeno no valor de 12 o valor a se pagar é R${:.2f}".format(
                        valorTotal))
                  confirmar = input("Deseja continuar S/N:").upper()
                  if confirmar == "N":
                        print("Finalizando")
                        break
                  else:
                        continue
            elif produto == "AC" and tamanho == "M":
                  valorTotal += 17
                  print("\nVocê escolheu açai tamanho médio no valor de 17 o valor a se pagar é R${:.2f}".format(
                        valorTotal))
                  confirmar = input("Deseja continuar S/N:").upper()
                  if confirmar == "N":
                        print("Finalizando")
                        break
                  else:
                        continue
            elif produto == "AC" and tamanho == "G":
                  valorTotal += 21
                  print("\nVocê escolheu açai tamanho grande no valor de 21 o valor a se pagar é R${:.2f}".format(
                        valorTotal))
            confirmar = input("Deseja continuar S/N:").upper()
            if confirmar == "N":
                  print("Finalizando")
                  break
      print("\nO valor final a se pagar é R${:.2f}".format(valorTotal))

acai()