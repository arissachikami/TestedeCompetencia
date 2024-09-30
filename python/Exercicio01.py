Numero = int(input('Insira número de peças: '))
        
Numero1 = list(map(int,input('Insira a numeração das peças que você tem:').split()))

busca = 0
for i in range(1, Numero + 1):
    busca ^= i

for Numero in Numero1:
    busca ^= Numero

print(busca)
