#Conversor de temperatura

cel = float (input("Informe a temperatura em C:\n"))
far = ((1.8 * cel) + 32)

print("{}ºC correspondem a {:.1f}ºF.".format(cel, far))