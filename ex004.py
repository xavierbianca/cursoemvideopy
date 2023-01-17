#Tipo primitivo da variavel

n = input ("Digite algo \n")
print("Tipo primitivo: {}.".format(type(n)))

print("É numérico? {}".format(n.isnumeric()))
print("É alfanumérico? {}.".format(n.isalpha()))
print("É um decimal? {}.".format(n.isdecimal()))
print("Está em caixa baixa? {}.".format(n.islower()))
print("É apenas espaço em branco? {}.".format(n.isspace()))
print("Está em caixa alta? {}.".format(n.isupper()))
