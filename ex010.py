#Conversor de real em dolar

real = float (input ("Quanto de dinheiro você tem? \nR$ "))
dolar = float (input ("Informe a cotação do dolar no dia: \nUS$ "))

convert = (real/dolar)

print ("A conversão de R$ {} em dolar é US$ {:.2f}".format(real, convert))