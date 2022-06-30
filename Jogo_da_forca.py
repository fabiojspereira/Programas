from time import sleep

print("*" * 41)
print("{:^51}".format("BEM VINDO AO JOGO DA FORCA v1.0"))
print("*" * 41)
print()

palavra_secreta = "paralelepipedo"
palavra_temporaria = list()
for letra in palavra_secreta:
	palavra_temporaria.append("?")

qtd_chances = 5
letras_erradas = []

print("{:<18}{:<2}{}".format("PALAVRA SECRETA", ":", palavra_temporaria))
print("{:<18}{:<2}{}".format("Letras erradas", ":", letras_erradas))
print("{:<18}{:<2}{}".format("Chances", ":", qtd_chances))

continua = True
while continua == True:
	letra = str(input("\nDigite uma letra : ").strip().lower())

	if letra not in "abcdefghijklmnopqrstuvwxyz":
		print("Digite apenas uma letra por tentativa...")
		continue

	if letra == "":
		print("Digite apenas uma letra por tentativa...")
		continue

	else:
		print(f"Você escolheu a letra '{letra}'. Verificando se você acertou ou errou...")
		sleep(0.5)

		if letra in letras_erradas or letra in palavra_temporaria:
			print(f"A letra {letra} já foi escolhida anteriormente... Escolha outra letra.")
			continue

		if letra in palavra_secreta:
			print(f"Acertou ! A letra '{letra}' está na palavra secreta.")
			for valor in range(0, len(palavra_secreta)):
				if letra == palavra_secreta[valor]:
					palavra_temporaria[valor] = letra

			print("{:<18}{:<2}{}".format("PALAVRA SECRETA", ":", palavra_temporaria))
			print("{:<18}{:<2}{}".format("Letras erradas", ":", letras_erradas))
			print("{:<18}{:<2}{}".format("Chances restantes", ":", qtd_chances))

			palavra_verificada = "".join(palavra_temporaria)
			if palavra_verificada == palavra_secreta:
				print(f"Parabéns ! Você acertou todas as letras da palavra {palavra_secreta.title()}.")
				break

		else:
			qtd_chances -= 1
			letras_erradas.append(letra)
			print(f"Errou ! A letra '{letra}' não está na palavra secreta...")
			print("{:<18}{:<2}{}".format("PALAVRA SECRETA", ":", palavra_temporaria))
			print("{:<18}{:<2}{}".format("Letras erradas", ":", letras_erradas))
			print("{:<18}{:<2}{}".format("Chances restantes", ":", qtd_chances))

			if qtd_chances == 0:
				continua = False
				print("\nSuas chances acabaram ! O jogo chegou ao fim.")
				print(f"A palavra secreta era : {palavra_secreta.title()}")
