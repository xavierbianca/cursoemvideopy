import math

angulo = float (input("Digite o angulo em graus \n"))

sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print ("Seno: {:.2f} // Cosseno: {:.2f} // Tangente: {:.2f}".format(sen,cos,tan))