# O dicionário é outra estrutura de dados Python. 
# Não é um tipo de sequência (mas pode ser facilmente adaptado ao processamento de sequência) e é mutável.

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

 
for key in dictionary.keys():
    print(key, "->", dictionary[key])

 
for english, french in dictionary.items():
    print(english, "->", french)
    

dictionary['gato'] = 'minou'
print(dictionary)

for french in dictionary.values():
    print(french)
    
dictionary['swan'] = 'cygne'
print(dictionary)

dictionary.update({"pato": "canard"})
print(dictionary)

del dictionary['cachorro']
print(dictionary)

dictionary.popitem()
print(dictionary)
