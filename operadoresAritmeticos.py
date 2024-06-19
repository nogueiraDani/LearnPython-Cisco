##
#1. Uma expressão é uma combinação de valores (ou variáveis, operadores, chamadas para funções - você aprenderá sobre eles em breve) que resulta em um determinado valor, por exemplo, 1 + 2.

#2. Operadores são símbolos especiais ou palavras-chave que são capazes de operar nos valores e realizar operações (matemáticas), por exemplo, o operador * multiplica dois valores: x * y.

#3. Operadores aritméticos em Python: + (adição), - (subtração), * (multiplicação), / (divisão clássica ‒ sempre retorna um ponto flutuante), % (módulo ‒ divide o operando esquerdo pelo operando direito e retorna o restante da operação, por exemplo , 5 % 2 = 1), ** (exponenciação ‒ operando esquerdo elevado à potência do operando direito, por exemplo, 2 ** 3 = 2 * 2 * 2 = 8), // (floor/divisão inteira ‒ retorna um número resultante da divisão, mas arredondado para o número inteiro mais próximo, por exemplo, 3 // 2.0 = 1.0)

#4. Um operador unário é um operador com apenas um operando, por exemplo, -1 ou +3.

#5. Um operador binário é um operador com dois operandos, por exemplo, 4 + 5 ou 12 % 5.

#6. Alguns operadores agem antes de outros - a hierarquia de prioridades:

    #o operador ** (exponenciação) tem a prioridade mais alta;
    #então o unário + e - (Nota: um operador unário à direita do operador de exponenciação se liga mais fortemente, por exemplo, 4 ** -1 é igual a 0.25)
    #então: *, /, e %,
    #e, por fim, a prioridade mais baixa: binário + e -.
#7. Subexpressões entre parênteses são sempre calculadas primeiro, por exemplo, 15 - 1 * (5 * (1 + 2)) = 0.

#8. O operador de exponenciação usa a associação do lado direito, por exemplo, 2 ** 2 ** 3 = 256.


print(2 + 2) # soma
print(2 - 2.0) # subtração
print(2 * 2) # multiplicação
print(2 / 2.0) # divisão
print(2 ** 3) # exponenciação
print(6 // 4.0) # divisão arredondada
print(15 % 2) # restante da divisao por num inteiro

