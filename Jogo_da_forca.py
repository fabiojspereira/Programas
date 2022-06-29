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
	if letra.isdigit():
		print("Digite apenas uma letra por vez ...")
		continue

	if letra == "":
		print("Digite apenas uma letra por vez ...")
		continue

	if len(letra) > 1:
		print("Digite apenas uma letra por vez ...")
		continue
	else:
		print(f"Você escolheu a letra '{letra}'. Vamos verificar se você acertou ou errou...")
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
				print("\Suas chances acabaram ! O jogo chegou ao fim.")
				print(f"A palavra secreta era {palavra_secreta.title()}")

"""
from time import sleep

print("*" * 41)
print("{:^51}".format("\033[1;33mBEM VINDO AO JOGO DA FORCA v1.0\033[m"))
print("*" * 41)
print()

palavra_secreta = "paralelepipedo"
palavra_temporaria = list()
for letra in palavra_secreta:
	palavra_temporaria.append("?")

qtd_chances = 5
letras_erradas = []

print("{:<18}{:<2}{}".format("\033[1;34mPALAVRA SECRETA   \033[m", ":", palavra_temporaria))
print("{:<28}{:<2}{}".format("\033[1;31mLetras erradas \033[m", ":", letras_erradas))
print("{:<28}{:<2}{}".format("\033[1;32mChances \033[m", ":", qtd_chances))

continua = True
while continua == True:
	letra = str(input("\nDigite uma letra : ").strip().lower())
	if letra.isdigit():
		print("Digite apenas uma letra por vez ...")
		continue

	if letra == "":
		print("Digite apenas uma letra por vez ...")
		continue

	if len(letra) > 1:
		print("Digite apenas uma letra por vez ...")
		continue
	else:
		print(f"Você escolheu a letra '\033[1;33m{letra.upper()}\033[m'. Vamos verificar se você acertou ou errou...")
		sleep(0.5)

		if letra in letras_erradas or letra in palavra_temporaria:
			print(f"A letra \033[1;32m{letra.upper()}\033[m já foi escolhida anteriormente... Escolha outra letra.")
			continue

		if letra in palavra_secreta:
			print(f"Acertou ! A letra '\033[1;33m{letra.upper()}\033[m' está na palavra secreta.")
			for valor in range(0, len(palavra_secreta)):
				if letra == palavra_secreta[valor]:
					palavra_temporaria[valor] = letra

			print("{:<18}{:<2}{}".format("\033[1;34mPALAVRA SECRETA   \033[m", ":", palavra_temporaria))
			print("{:<28}{:<2}{}".format("\033[1;32mLetras erradas \033[m", ":", letras_erradas))
			print("{:<28}{:<2}{}".format("\033[1;32mChances restantes \033[m", ":", qtd_chances))

			palavra_verificada = "".join(palavra_temporaria)
			if palavra_verificada == palavra_secreta:
				print(f"Parabéns ! Você acertou todas as letras da palavra {palavra_secreta}.")
				break

		else:
			qtd_chances -= 1
			letras_erradas.append(letra)
			print(f"Errou ! A letra '\033[1;31m{letra.upper()}\033[m' não está na palavra secreta...")
			print("{:<18}{:<2}{}".format("\033[1;34mPALAVRA SECRETA   \033[m", ":", palavra_temporaria))
			print("{:<28}{:<2}{}".format("\033[1;32mLetras erradas \033[m", ":", letras_erradas))
			print("{:<28}{:<2}{}".format("\033[1;32mChances restantes \033[m", ":", qtd_chances))

			if qtd_chances == 0:
				continua = False
				print("\n\033[1;31mSuas chances acabaram ! O jogo chegou ao fim.\033[m")
				print(f"A palavra secreta era \033[1;33m{palavra_secreta.upper()}\033[m.")


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
print("{:<28}{:<2}{}".format("Letras erradas", ":", letras_erradas))
print("{:<28}{:<2}{}".format("Chances", ":", qtd_chances))

continua = True
while continua == True:
	letra = str(input("\nDigite uma letra : ").strip().lower())
	if letra.isdigit():
		print("Digite apenas uma letra por vez ...")
		continue

	if letra == "":
		print("Digite apenas uma letra por vez ...")
		continue

	if len(letra) > 1:
		print("Digite apenas uma letra por vez ...")
		continue
	else:
		print(f"Você escolheu a letra '{letra.upper()}'. Vamos verificar se você acertou ou errou...")
		sleep(0.5)

		if letra in letras_erradas or letra in palavra_temporaria:
			print(f"A letra {letra.upper()} já foi escolhida anteriormente... Escolha outra letra.")
			continue

		if letra in palavra_secreta:
			print(f"Acertou ! A letra '{letra.upper()}' está na palavra secreta.")
			for valor in range(0, len(palavra_secreta)):
				if letra == palavra_secreta[valor]:
					palavra_temporaria[valor] = letra

			print("{:<18}{:<2}{}".format("PALAVRA SECRETA", ":", palavra_temporaria))
			print("{:<28}{:<2}{}".format("Letras erradas", ":", letras_erradas))
			print("{:<28}{:<2}{}".format("Chances restantes", ":", qtd_chances))

			palavra_verificada = "".join(palavra_temporaria)
			if palavra_verificada == palavra_secreta:
				print(f"Parabéns ! Você acertou todas as letras da palavra {palavra_secreta}.")
				break

		else:
			qtd_chances -= 1
			letras_erradas.append(letra)
			print(f"Errou ! A letra '{letra.upper()}' não está na palavra secreta...")
			print("{:<18}{:<2}{}".format("PALAVRA SECRETA", ":", palavra_temporaria))
			print("{:<28}{:<2}{}".format("Letras erradas", ":", letras_erradas))
			print("{:<28}{:<2}{}".format("Chances restantes", ":", qtd_chances))

			if qtd_chances == 0:
				continua = False
				print("\Suas chances acabaram ! O jogo chegou ao fim.")
				print(f"A palavra secreta era {palavra_secreta.upper()}")
				
"""
