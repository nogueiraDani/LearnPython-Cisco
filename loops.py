l = 0
while l < 10:
    print(l)
    l += 1

for i in range(10):
   print("O valor de i é atualmente", i)

for j in range(2, 8, 3): # o 3º numero é o incremento
  print("O valor de i é atualmente", j)
  
for k in range(1, 1):
    print("O valor de i é atualmente", k)
    
    power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2
  
#break
largest_number = -99999999
counter = 0

while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > maior_numero:
        maior_numero = number

if counter != 0:
    print("TO maior número é", maior_numero)
else:
    print("Você não inseriu nenhum número.")
    

#continue
largest_number = -99999999
counter = 0

number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

if counter:
    print("O maior número é",  largest_number)
else:
    print("Você nnão tem inseriu qualquer número.")
    
#while com else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
    

#for com else
for i in range(5):
 print(i)
else:
 print("else:", i)
