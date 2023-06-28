import time

start_time = time.time()

universo = list()

quantidade_repeat = int(input("Digite a quantidade de repetições : "))

# PARTE DO PROGRAMA QUE GERA O UNIVERSO COM 1000 NÚMEROS DE 1 A 9.
seletor_001 = 0
for contador_001 in range(1, 10001):  # Valor que define o tamanho do universo.
	seletor_001 = seletor_001 + 1
	if 1 <= seletor_001 <= 9:
		universo.append(seletor_001)
	elif seletor_001 >= 10:
		seletor_001 = 1
		universo.append(seletor_001)

# PARTE DO PROGRAMA QUE ORGANIZA A QUANTIDADE DE ITENS DO UNIVERSO NA TELA.
numero_linha = 0
if len(universo) <= 9:
	numero_linha = 1
else:
	numero_linha = len(universo) // 9
	if (len(universo) % 9) > 0:
		numero_linha = numero_linha + 1
numero_coluna = 0
if len(universo) <= 9:
	numero_coluna = len(universo)
else:
	numero_coluna = 9

# PARTE DO PROGRAMA QUE GERA A GRADE DE VALORES DO UNIVERSO.
controlador_001 = 0     # Responsável por imprimir os valores da lista universo.
controlador_002 = 4     # Responsável por selecionar os valores selecionados.
check_numero_final = 0  # Contador que soma a quantidade de saltos.

for linha in range(1, numero_linha + 1):
	if check_numero_final == quantidade_repeat:
		break

	else:
		print("\n{:<10}{:<3}{:^3}".format("\033[1;35mLoop \033[m", linha, "\033[1;32m : \033[m"), end="")  # Para um melhor entendimento da resolução.
		for coluna in range(1, numero_coluna + 1):
			if controlador_001 <= len(universo):  # Verifica se ainda existem valores a serem exibidos.
				if check_numero_final == quantidade_repeat:
					break

				else:
					if universo[controlador_001] == universo[controlador_002]:
						if check_numero_final+1 == quantidade_repeat:
							print("{}{}{}".format("\033[7;30;42m", universo[controlador_001], "\033[m "), end="")

						else:
							print("{}{}{}".format("\033[34;40m", universo[controlador_001], "\033[m "), end="")

						controlador_002 = universo[controlador_002]
						controlador_002 = controlador_002 + 3
						check_numero_final = check_numero_final + 1

					else:
						print(universo[controlador_001], end=" ")  # Responsável por imprimir os valores da lista universo.
						if check_numero_final == quantidade_repeat:
							break
					controlador_001 = controlador_001 + 1

		if check_numero_final == quantidade_repeat:
			print("\033[7;30;42m RESULTADO \033[m")

print("\n")
print("{:<32}{:^5}{:<2}".format("\033[1;33mRepetições solicitadas", ":\033[m",quantidade_repeat))
print("{:<32}{:^5}{}{:<1}{}".format("\033[1;33mÚltimo número descoberto", ":\033[m", "\033[7;30;42m", universo[controlador_002-4], "\033[m"))
print("{:<32}{:^5}{:<2}".format("\033[1;33mUniverso pré carregado", ":\033[m", len(universo)))

end_time = time.time()
execution_time = end_time - start_time

print("Tempo de execução: {:.2f} segundos".format(execution_time))
