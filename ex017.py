from math import hypot

x = float(input("Insira o valor do cateto oposto: \n"))
y = float(input("Insura o valor do cateto adjacente: \n"))

hip = math.hypot(x,y)

print ("Valor da hipotenusa é {:.3}".format(hip))