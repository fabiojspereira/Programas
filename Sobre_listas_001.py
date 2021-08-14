# https://www.w3schools.com/python/python_lists.asp
# Criação das listas :
mercado = ["leite","pão","café"]
casa = ["sala","quarto","cozinha","banheiro","varanda"]
objetos = ["lapis","caneta","caneca","livro","copo","régua","borracha"]

# Exibição das listas :
print("\nVou imprimir a lista do \033[1;32mmercado\033[m{:>3} {}".format(" :",mercado))
print("Vou imprimir a lista da \033[1;33mcasa\033[m{:>6}".format(" :"),casa)
print("Vou imprimir a lista dos \033[1;34mobjetos\033[m{:>2}".format(" :"),(objetos))

# Comprimento das listas : Mostra a quantidade de itens dentro de cada lista :
print("\nQuantidade de itens dentro das listas : ")
print("Lista 1 : \033[1;32mMERCADO\033[m :",(len(mercado)),"itens.")
print("Lista 2 : \033[1;33mCASA\033[m    : {} itens.".format(len(casa)))
print("Lista 3 : \033[1;34mOBJETOS\033[m : {} itens.".format(len(objetos)))

# Acessando itens das listas :
print("\nItem com índice \033[1;31m[0]\033[m na lista do \033[1;32mmercado\033[m{:>15} {}.".format(" :",mercado[0]))
print("Item com índice \033[1;31m[1]\033[m na lista da \033[1;33mcasa\033[m{:>18} {}.".format(" :",casa[1]))
print("Item com índice \033[1;34m[0],[1] e [5]\033[m na lista da \033[1;33mobjetos\033[m{:>5} {},{} e {}.".format(" :",objetos[0],objetos[1],objetos[5]))

# Modificando itens dentro de uma lista :
print("\nEscolha uma lista para podermos trocar um item por outro.")
print("\033[1;32mLista 1\033[m", end =" ou ")
print("\033[1;33mLista 2\033[m", end =" ou ")
print("\033[1;34mLista 3\033[m", end ="")
esc_1 = str(input("\nLista : ")).strip().lower()

c_l1 = len(mercado)
c_l2 = len(casa)
c_l3 = len(objetos)

if esc_1 == "lista 1" or esc_1 == "lista1" or esc_1 == "1": # ESCOLHA LISTA 1
	print("\nLista \033[1;32m{}\033[m selecionado.".format("MERCADO"))
	print("Agora escolha um item para ser substituído :")
	#print("\033[1;32mLista 1\033[m : ",(mercado))
	for item in range (0, len(mercado),1):
		print("Item [{}] da lista : {}".format(item,mercado[item]))
	esc_1_2 = int(input("Item : "))
	if esc_1_2 > ( c_l1-1 ):
		print("\nItem não cadastraado !")
	else:
		print("\nItem \033[1;37m{}\033[m selecionado.".format(mercado[esc_1_2]))
		mercado[esc_1_2] = str(input("Digite o item que substituirá o \033[1;37m{}.\033[m\nItem : ".format(mercado[esc_1_2])))
		print("\nVou imprimir a lista do \033[1;32mmMERCADO\033[m atualizada : ")
		for item in range (0, c_l1):
			print("Item [{}] da lista : {}".format(item, mercado[item]))

elif esc_1 == "lista 2" or esc_1 == "lista2" or esc_1 == "2": # ESCOLHA LISTA 2
	print("\nLista \033[1;33m{}\033[m selecionado.".format("CASA"))
	print("Agora escolha um item para ser substituído :")
	for item in range (0, len(casa),1):
		print("Item [{}] da lista : {}".format(item,casa[item]))
	esc_1_2 = int(input("Item : "))
	if esc_1_2 > ( c_l2-1 ):
		print("\nItem não cadastraado !")
	else:
		print("\nItem \033[1;37m{}\033[m selecionado.".format(casa[esc_1_2]))
		casa[esc_1_2] = str(input("Digite o item que substituirá o \033[1;37m{}.\033[m\nItem : ".format(casa[esc_1_2])))
		print("\nVou imprimir a lista do \033[1;33mCASA\033[m atualizada : ")
		for item in range (0, c_l2):
			print("Item [{}] da lista : {}".format(item, casa[item]))

elif esc_1 == "lista 3" or esc_1 == "lista3" or esc_1 == "3": # ESCOLHA LISTA 3
	print("\nLista \033[1;34m{}\033[m selecionado.".format("OBJETOS"))
	print("Agora escolha um item para ser substituído :")
	for item in range (0, len(objetos),1):
		print("Item [{}] da lista : {}".format(item,objetos[item]))
	esc_1_2 = int(input("Item : "))
	if esc_1_2 > ( c_l3-1 ):
		print("\nItem não cadastraado !")
	else:
		print("\nItem \033[1;37m{}\033[m selecionado.".format(objetos[esc_1_2]))
		objetos[esc_1_2] = str(input("Digite o item que substituirá o \033[1;37m{}.\033[m\nItem : ".format(objetos[esc_1_2])))
		print("\nVou imprimir a lista do \033[1;34mOBJETOS\033[m atualizada : ")
		for item in range (0, c_l3):
			print("Item [{}] da lista : {}".format(item, objetos[item]))


else:
	print("Lista inválida !")

print("\nFIM")


