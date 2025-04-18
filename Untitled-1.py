#a= int(input("Digite um valor:"))
#pos= a+1
#ant= a-1
#print("O numero escolhido foi:", a, "O posterior dele é:", pos, "e o anterior é:",#ant)

#num = int(input("Digite um número:"))
#dobro= num*2
#print("O dobro de {} é {}".format(num, dobro))

#nota1 = float(input("Digite sua primeira nota:"))
#nota2 = float(input("Digite sua segunda nota:"))
#media = (nota1 + nota2)/2
#print(media)

metragem= float(input("Digita a medida em metros: "))
cent = metragem*100
mili = metragem*1000
print("A conversão em centimetros é {} e em milímetros é:{}".format(cent, mili))

tab= int(input("Escolha o número pra exibir sua tabuada: "))
n1=1
for i in range(1,11):
    n1= n1+1
    mut1 = tab*n1
    print(i, "x", n1, "=", mut1)

