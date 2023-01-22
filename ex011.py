#Pintando parede

altura = float (input ("Digite a altura da parede em m: \n"))
largura = float (input ("Digite a largura da parede em m: \n"))

parede = (altura * largura)

print ("Sua parede tem área de {}m2 e você precisará de {}l de tinta".format (parede, parede/2))


