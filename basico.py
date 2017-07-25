### Bem vindo
print("Hello World")

### Carregar bibliotecas

# Mas antes, uma mensagem:

import this

# Agora, uma biblioteca com apelido

import matplotlib.pyplot as plt

### Uma funcao que calcula o dobro

def double(x):
    return x*2

### Uma funcao  que devolve para 1

def apply_to_one(f):
    return f(1)

### Exemplo de uma funcao como argumento

my_double = double
x = apply_to_one(my_double)

print(x)

### Funcao sem nome

y = apply_to_one(lambda x:x+4)

print("y =",y)

### Nao importa as aspas da string

a = "ana"
c = 'ciconelle'

print(a,c)

### Barra invertida para caracteres especiais

tab_string = '\t'
len(tab_string)
print(a,tab_string,c)

### Se quiser o caracter, use string bruta(r"")

not_tab_string = r"\t"
print(not_tab_string)

### Coisas que dao erro, da para informar usando except:

try:
    print(0/0)
except ZeroDivisionError:
    print("Nao dividir por 0")

### Existe listas:

lista = [1,2,3]

lista_estranha = ["texto", 0.1, True]
