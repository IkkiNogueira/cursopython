from random import random, randrange

########## LISTAS ###############

# Como uma lista é identificada? Através de colchetes []
lista_estranha = ['duas palavras', 42, True, ['Batman', 'Robin'], -0.84,  'hipótese']

resp1 = 42 in lista_estranha
resp2 = 'duas palavras' in lista_estranha
resp3 = 'domino' in lista_estranha
resp4 = 'Batman' in lista_estranha[3]
resp5 = 'Coringa' in lista_estranha[3]
del lista_estranha[2]

print(len(lista_estranha))
print(resp1)
print(resp2)
print(resp3)
print(resp4)
print(resp5)

lista_estranha.append('e')
print("Append 'e' na lista_estranha: ", lista_estranha)

lista_estranha.insert(2,'d')
print("Insert 'd' na lista estranha: ", lista_estranha)

lista2 = ['estendendo', 'lista', 'estranha']
lista_estranha.extend(lista2)
print("Extend 'lista2' na lista estranha: ", lista_estranha)

listaDesordenada = [4, 8, 5, 10]
print(listaDesordenada)
listaDesordenada.sort()
print(listaDesordenada)

print(list(range(1,200)))

telefone = {
    "ana": 123456, 
    "yudi": 7890123, 
    "julia": 14657889
    }

print(telefone)

lista3 = ["brigadeiro", "leite condensado, achocolatado"]
lista4 = ["omelete", "ovos, azeite, condimentos a gosto"]
lista5 = ["ovo frito", "ovo, oleo, condimentos a gosto"]

listaReceitas = [lista3, lista4, lista5]

print(listaReceitas)

receitas = dict(listaReceitas)

print(receitas)


capitais = {
    "SP": "Sao Paulo", 
    "AC": "Rio Branco", 
    "TO": "Palmas",
    "RJ": "Rio de janeiro", 
    "SE": "Aracaju",
    "MG": "Belo Horizonte"
    }

print("Exemplo DICT: ", capitais["MG"])

numeros = {
    "primos":[2,3,5], 
    "pares":[0,2,4], 
    "impares":[1,3,5]
    }

print(numeros["impares"])

pessoa = {
    "nome": "Daiane",
    "idade": 28,
    "familia": {
        "mae": "Margarete",
        "pai": "Carlos"
    }
}

print(pessoa["idade"])
pessoa["idade"] = 28.6
print(pessoa["idade"])

meses = {
    1:"janeiro",
    2:"fevereiro",
    3:"março"
    }

print(meses)
meses[4] = "abril"
print(meses)

del(meses[4])
print(meses)

print(meses.items())
print(meses.values())
print(meses.keys())

chaves = list(meses.keys())
print(chaves)

resp6 = "fevereiro" in meses
resp7 = 2 in meses
if resp6:
    print("Está")
else:
    if resp7:
        print("Ele olha a chave, não o valor")
    else:
        print("Não está")

meses.clear()
print(meses)

####### Condições ########
n = 0
value = randrange(10)
print(value)
for _ in range(value):
    n += 1
    print("Numero: ", n)


getitens = {
    "valor1": "teste1",
    "valor2": "teste2",
    "valor3": "teste3"
}
    
for chave,valor in getitens.items():
    print(chave, "->", valor)

a = 10
b = 0
while b < a:
    b += 1
    print("ainda não acabou", b)


while True:
    stringDigitada = input("Digite uma palavra: ")
    if stringDigitada.lower() == "sair":
        print("Saindo")
        break
    if len(stringDigitada) < 2:
        print("String muito pequena")
        continue
