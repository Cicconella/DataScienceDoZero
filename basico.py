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

# Existe listas, elas podem conter coisas diferentes:

lista = [1,2,3]
lista_estranha = ["texto", 0.1, True]
print(lista_estranha)

# Voce pode mexer nela, mas comeca na posicao 0:

lista = [1,2,3]
print(lista)

lista[0] = "zero"
print(lista)
print(lista[:2])
print(lista[-1])

# Checar se tem algo na lista:

print(1 in lista)
print("zero" in lista)

# Aumentar a lista

lista2 = lista + lista_estranha
print(lista2)

lista2.append("passaros")
print(lista2)

# Tamanho da lista

print(len(lista))

# Definindo coisas ao mesmo tempo
lista, lista2 = [[1,2], [3,4]]

print(lista,lista2)

# Tuplas (Iguas as listas, mas nao podem ser mudadas), uteis para retornar funcoes

a = (1,2,3)

try:
    a[1]=3
except TypeError:
    print("Tuple nao muda")

# Dicionario

dic_vazio = {}
print(dic_vazio)

dic_novo = {"Dia": 16, "Mes": 2}
print(dic_novo)

dia = dic_novo["Dia"]
print(dia)

#E se nao tiver

try:
    ano = dic_novo["Ano"]
except KeyError:
    print("Nao tem")


# Contar palavras no texto

documento = ("azul", "amarelo", "verde", "azul")

numero_palavras = {}

for palavra in documento:
    if palavra in numero_palavras:
        numero_palavras[palavra] += 1
    else:
        numero_palavras[palavra] = 1

print(numero_palavras)

# Ou faz assim

numero_palavras = {}

for palavra in documento:
    numero_anterior = numero_palavras.get(palavra,0)
    numero_palavras[palavra] = numero_anterior + 1

print(numero_palavras)

# Existe o defaultdict

from collections import defaultdict

numero_palavras = defaultdict(int)
for palavra in documento:
    numero_palavras[palavra] += 1

print(numero_palavras)

# Existe o counter

from collections import Counter

c = Counter([0,1,2,1,0])
print(c)