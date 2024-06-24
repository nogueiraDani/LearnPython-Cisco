numbers = [1,2,3,4,5] # criando lista com valores
my_list = [] # criando lista vazia

numbers[0] = 11
numbers[4] = 55

print(numbers)
print(len(numbers))

del numbers[2]

print(len(numbers))

#indice negativo , para pegar ultimo [-1] e penultimo [-2]

print(numbers[-1])

numbers.append(6) # adiciona sempre no final
numbers.insert(-0, 0) # adiciona conforme localização (-0 para ser o primeiro) e 0 para o valor adiciondo
print(numbers)

for i in range(5):
   my_list.append (i + 1)

print (my_list)

for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)

total = 0

#for i in range(len(my_list)):

#  total += my_list[i]

for i in my_list: #forma abreviada do for acima
    total += i

print(total)

numbers.sort()
print(numbers)

numbers.reverse()

print(numbers)


## nome da lista define o local do armazenamento e nao o valor da variavel

list_1 = [1]
#list_2 = list_1
list_2 = list_1[:] # usando : vc copia o conteudo e nao o nome da lista
list_1 [0] = 2
print(list_2)

my_list2 = [10, 8, 6, 4, 2]
new_list = my_list2 [1: 3]
print(new_list)

del new_list[1:]
print(new_list)

#verificar se há na lista

print(55 in numbers)
print(32 in numbers)
print(25 not in numbers)

## listas complexas

squares = [x ** 2 for x in range(10)] # cria a lista já quando executa o for
print(squares)

twos = [2 ** i for i in range(8)]
print(twos)
 
odds = [x for x in squares if x % 2 != 0 ]
print(odds)


## matrizes bidimensionais

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura média ao meio-dia:", average)

highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("A maior temperatura foi:", highest)

hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "dias estavam quentes.")

## exemplo hotel 3 torres, 15 andares, 20 quartos por andar

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
rooms[0][4][1] = False
 
vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
        
# Uma tabela de quatro colunas/quatro linhas ‒ uma matriz bidimensional (4x4)
 
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]
 
print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'
 

 

 

 

 


 

 


