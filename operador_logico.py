counter > 0 and value == 100 #and
counter > 0 or value == 10 #or


#A negação de uma conjunção é a disjunção das negações.

#A negação de uma disjunção é a conjunção das negações.

# Exemplo 1:
print(var > 0)
print(not (var <= 0))
 
 
# Exemplo 2:
print(var != 0)
print(not (var == 0))

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

#No entanto, existem quatro operadores que permitem manipular bits únicos de dados. Eles são chamados de operadores bit a bit.

#Eles abrangem todas as operações que mencionamos anteriormente no contexto lógico e um operador adicional. Este é o operador xor (as em exclusivo ou) e é indicado como ^ (circunflexo).

# & (e comercial) - conjunção bit a bit;
# | (barra) - disjunção bit a bit;
# ~ (til) - negação bit a bit;
# ^ (circunflexo) ‒ bit a bit exclusivo ou (xor)

## deslocamento binario para esq ou dir
var = 17
var_right = var >> 1
var_left = var << 2
print (var, var_left, var_right)