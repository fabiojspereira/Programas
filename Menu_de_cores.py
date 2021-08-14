print("\033[0;30;46m{:>80}\033[m".format("Programação Python "))
print("\033[0;40m{:>80}\033[m".format("Fábio JS Pereira "))
print("\033[37m{:>80}\033[m".format("Programa 001 : Menus de Cores "))

print("\nSerá exibido o conjunto de estilos e cores básicos do Python.")
print("\nVamos começar pelo estilo do texto. Escolha uma opção :")
print("1 - Para estilo : Sem formatação\n"
      "2 - Para estilo : \033[1mNegrito\033[m\n"
      "3 - Para estilo : \033[4mSublinhado\033[m\n"
      "4 - Para estilo : \033[7mInvertido\033[m")
op1 = int(input(": "))
estilo = ["sem formatação", "Negrito", "Sublinhado", "Invertido"]

print("\nAgora vamos escolher a cor do texto. Escolha uma opção :")
m = len("Agora vamos escolher a cor do texto. Escolha uma opção :")
print("=" * m)

print("\n1 - Para {:<8}{:>2}{:>19}".format("Branco", ":", "\033[7;40m        \033[m"))
print("2 - Para {:<8}{:>2}{:>22}".format("Vermelho", ":", "\033[0;00;41m        \033[m"))
print("3 - Para {:<8}{:>2}{:>22}".format("Verde", ":", "\033[0;00;42m        \033[m"))
print("4 - Para {:<8}{:>2}{:>22}".format("Amarelo", ":", "\033[0;00;43m        \033[m"))
print("5 - Para {:<8}{:>2}{:>22}".format("Azul", ":", "\033[0;00;44m        \033[m"))
print("6 - Para {:<8}{:>2}{:>22}".format("Lilás", ":", "\033[0;00;45m        \033[m"))
print("7 - Para {:<8}{:>2}{:>22}".format("Ciano", ":", "\033[0;00;46m        \033[m"))
print("8 - Para {:<8}{:>2}{:>22}".format("Cinza", ":", "\033[0;00;47m        \033[m"))
print("9 - Para {:<8}{:>2}{:>19}".format("Preto", ":", "\033[0;40m        \033[m"))
op2 = int(input(": "))
cor_txt = ["Branco", "Vermelho", "Verde", "Amarelo", "Azul", "Lilás", "Ciano", "Cinza", "Preto"]

print("\nAgora vamos escolher a cor de fundo. Escolha uma opção :")
m = len("Agora vamos escolher a cor de fundo. Escolha uma opção :")
print("=" * (m))

print("\n1 - Para {:<8}{:>2}{:>19}".format("Branco", ":", "\033[7;40m        \033[m"))
print("2 - Para {:<8}{:>2}{:>22}".format("Vermelho", ":", "\033[0;00;41m        \033[m"))
print("3 - Para {:<8}{:>2}{:>22}".format("Verde", ":", "\033[0;00;42m        \033[m"))
print("4 - Para {:<8}{:>2}{:>22}".format("Amarelo", ":", "\033[0;00;43m        \033[m"))
print("5 - Para {:<8}{:>2}{:>22}".format("Azul", ":", "\033[0;00;44m        \033[m"))
print("6 - Para {:<8}{:>2}{:>22}".format("Lilás", ":", "\033[0;00;45m        \033[m"))
print("7 - Para {:<8}{:>2}{:>22}".format("Ciano", ":", "\033[0;00;46m        \033[m"))
print("8 - Para {:<8}{:>2}{:>22}".format("Cinza", ":", "\033[0;00;47m        \033[m"))
print("9 - Para {:<8}{:>2}{:>19}".format("Preto", ":", "\033[0;40m        \033[m"))
op3 = int(input(": "))
cor_bkg = ["Branco", "Vermelho", "Verde", "Amarelo", "Azul", "Lilás", "Ciano", "Cinza", "Preto"]

# print(estilo[op1-1])
# print(type(op1))

if op1 == 1:
    print("\nEstilo : \033[m{}\033[m".format(estilo[int(op1) - 1]))
elif op1 == 2:
    print("\nEstilo : \033[1m{}\033[m".format(estilo[int(op1) - 1]))
elif op1 == 3:
    print("\nEstilo : \033[4m{}\033[m".format(estilo[int(op1) - 1]))
elif op1 == 4:
    print("\nEstilo : \033[7m{}\033[m".format(estilo[int(op1) - 1]))

if op2 == 1:
    print("Cor do texto : \033[0;30m{}\033[m".format(cor_txt[int(op2) - 1]))
elif op2 == 2:
    print("Cor do texto : \033[0;31m{}\033[m".format(cor_txt[int(op2) - 1]))
elif op2 == 3:
    print("Cor do texto : \033[0;32m{}\033[m".format(cor_txt[int(op2) - 1]))
elif op2 == 4:
    print("Cor do texto : \033[0;33m{}\033[m".format(cor_txt[int(op2) - 1]))
elif op2 == 5:
    print("Cor do texto : \033[0;34m{}\033[m".format(cor_txt[int(op2) - 1]))
elif op2 == 6:
    print("Cor do texto : \033[0;35m{}\033[m".format(cor_txt[int(op2) - 1]))
elif op2 == 7:
    print("Cor do texto : \033[0;36m{}\033[m".format(cor_txt[int(op2) - 1]))
elif op2 == 8:
    print("Cor do texto : \033[0;37m{}\033[m".format(cor_txt[int(op2) - 1]))
elif op2 == 9:
    print("Cor do texto : \033[40m{}\033[m".format(cor_txt[int(op2) - 1]))

if op3 == 1:
    print("Cor do background : \033[7;40m{}\033[m".format(cor_bkg[int(op3) - 1]))
elif op3 == 2:
    print("Cor do background : \033[41m{}\033[m".format(cor_bkg[int(op3) - 1]))
elif op3 == 3:
    print("Cor do background : \033[42m{}\033[m".format(cor_bkg[int(op3) - 1]))
elif op3 == 4:
    print("Cor do background : \033[43m{}\033[m".format(cor_bkg[int(op3) - 1]))
elif op3 == 5:
    print("Cor do background : \033[44m{}\033[m".format(cor_bkg[int(op3) - 1]))
elif op3 == 6:
    print("Cor do background : \033[45m{}\033[m".format(cor_bkg[int(op3) - 1]))
elif op3 == 7:
    print("Cor do background : \033[46m{}\033[m".format(cor_bkg[int(op3) - 1]))
elif op3 == 8:
    print("Cor do background : \033[47m{}\033[m".format(cor_bkg[int(op3) - 1]))
elif op3 == 9:
    print("Cor do background : \033[40m{}\033[m".format(cor_bkg[int(op3) - 1]))

#print("\nCerto ! Você escolheu o estilo {}, a cor do texto {} e a cor de fundo {}.".format(estilo[op1-1], cor_txt[op2-1],cor_bkg[op3-1]))



"""
if op1 == ("1") or op1 == ("2") or op1 == ("3") or op1 == ("4"):
        print("OK, dentro do interválo")
else:
        print("Você não digitou uma opção válida !")
"""
