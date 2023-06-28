numeros = ["VAZIO", "VAZIO", "VAZIO"]

# VARIÁVEIS DE INICIALIZAÇÃO DO FOR
INICIAL = 0
FINAL = 3

continua_001 = True
while continua_001 == True:

    # VERIFICAÇÃO DA LISTA COMPLETA
    if numeros[0] != "VAZIO" and numeros[1] != "VAZIO" and numeros[2] != "VAZIO":
        continua_001 = False
        break

    for contador in range(INICIAL, FINAL):
        print(f"\ncontador atual : {contador+1}")
        n = str(input(f"Digite um número para ser inserido no {contador+1}º espaço : "))

        # VERIFICAÇÃO SE É UM NUMÉRICO DIGITADO
        if n.isnumeric():
            # CASO O ÍNDICE ESTEJA VAZIO, PODERA SER PREENCHIDO. CASO CONTRÁRIO SERÁ NOTIFICADO
            if numeros[contador] == "VAZIO":
                numeros[contador] = n
                print(f"Lista atualizada : {numeros}")
                continua_001 = True
            else:
                print(f"Este espaço já foi preenchido com o valor {numeros[contador]} e não pode ser modificado. ")

        else:
            print("ERROR ! Tente novamente !")
            print(f"Lista atualizada : {numeros}")
            INICIAL = contador
            continua_001 = True
            break

print(f"\nA lista foi preenchida corretamente  {numeros}")
