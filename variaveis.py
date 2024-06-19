# O PEP 8 - Guia de Estilo para Código Python recomenda a seguinte convenção de nomenclatura para variáveis e funções em Python:

#os nomes de variáveis devem estar em letras minúsculas, com palavras separadas por sublinhados para melhorar a legibilidade (por exemplo, var, my_variable)
#nomes de funções seguem a mesma convenção que nomes de variáveis (por exemplo, fun, my_function)
#também é possível usar casos mistos (por exemplo, myVariable), mas apenas em contextos onde esse já é o estilo predominante, para manter a compatibilidade com a convenção adotada.

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=",")


total_apples = john + mary + adam

print("total de maças: ", total_apples)


kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "milhas é", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros é", round(kilometers_to_miles, 2), "milhas")

x = -1
x = float(x)
y = 3 * (x ** 3) - 2 * (x ** 2) + (3 * x) - 1

print("Y = ", y)