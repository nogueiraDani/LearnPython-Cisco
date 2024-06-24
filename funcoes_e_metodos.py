def message():
    print("Digite um número: ")
 
#message()
#a = int(input())

def message(number):
    print("Digite um número:", number)
 
number = 1234
#message(1)
#print(number)

def message(what, number):
    print("Entrar", what, "número", number)
 
message("telefone", 11)
message("preço", 5)
message("número", "número")

def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
    
adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)

# adding(3, a = 1, b = 2) # erro, 2x passado o argumento a
 
#funções parametrizadas
def introduction(first_name, last_name="Smith"):
     print("Olá meu nome é", first_name, last_name)
 
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")
 
def introduction(first_name="John", last_name="Smith"):
    print("Olá meu nome é", first_name, last_name)
 
introduction()
introduction(last_name="Hopkins")

#lista como paramentro
def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s

print(list_sum([5, 4, 3]))


# escopo
def my_function():
 print("Eu conheço aquela variável?", var)


var = 1
my_function()
print(var)

def my_function():
    var = 2
    print("Eu conheço aquela variável?", var)
 
 
var = 1
my_function()
print(var)

#escopo global
def my_function():
 global var
 var = 22
 print("Eu conheço aquela variável?", var)


var = 11
my_function()
print(var)


#interagindo com variaveis
def my_function(n):
 print("Eu obtive", n)
 n += 1
 print("Eu tenho", n)


var = 1
my_function(var)
print(var)

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
 

 


 

 






 

 

 

 

 

 

 

 


 


 


 

 




 

 

 

 

 
