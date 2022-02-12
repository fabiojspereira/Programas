universo = list()
resposta = list()

# PARTE DO PROGRAMA QUE GERA O UNIVERSO COM 1000 NÚMEROS DE 1 A 9.
seletor_001 = 0
for contador_001 in range(1, 1001):
	seletor_001 = seletor_001 + 1
	if 1 <= seletor_001 <= 9:
		universo.append(seletor_001)
	elif seletor_001 >= 10 :
		seletor_001 = 1
		universo.append(seletor_001)

# PARTE DO PROGRAMA QUE ORGANIZA A QUANTIDADE DE ITENS DO UNIVERSO NA TELA.
numero_linha = 0
if len(universo) <= 30:
	numero_linha = 1
else :
	numero_linha = len(universo) // 30
	if ( len(universo) % 30 ) > 0:
		numero_linha = numero_linha + 1
numero_coluna = 0
if len(universo) <= 30:
	numero_coluna = len(universo)
else:
	numero_coluna = 30

# PARTE DO PROGRAMA QUE FAZ A EXIBIÇÃO DE INFORMAÇÕENS BÁSICAS.
print(f"\nUniverso : {len(universo)} itens")
print(f"Número de linhas : {numero_linha}")
print(f"Número de colunas : {numero_coluna}\n")

# PARTE DO PROGRAMA QUE GERA A GRADE DE VALORES DO UNIVERSO.
controlador = 0
for linha in range (1, numero_linha+1):
	for coluna in range (1, numero_coluna+1):
		if controlador < len(universo) :
			print(universo[controlador],end=" ")
			controlador = controlador + 1
		else:
			print("\033[1;31mSem mais itens !\033[m")
			break
	print()

# PARTE DO PROGRAMA QUE GERA A TABELA FINAL DE VALORES DO UNIVERSO.
seletor_002 = 0
for contador_002 in range(1, 1001):
	seletor_002 = universo[seletor_002]
	print("Passo --->",contador_002,end="")
	print("\tNúmero :\033[1;34m",seletor_002,"\033[m")
	resposta.append(seletor_002)
	seletor_002 = seletor_002 + 3
