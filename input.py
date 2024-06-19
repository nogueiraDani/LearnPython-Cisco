# print("Conta-me qualquer coisa...")
# anything = input()
anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "... Realmente?")

# float() / int()

leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)

fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")

# Replicação

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

x= float(input("Digite x: "))
y = 1. / (x + (1. / (x + 1. / (x + 1. / x ))))

print("y = ", y)