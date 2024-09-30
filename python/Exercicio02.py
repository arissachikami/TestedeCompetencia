while True:
    try:
        numero = int(input('Número de botas individuais: '))
        sapato = []
        pares = 0

        for i in range (0,numero):
            numeraçao = input('Insira tamanho e lado da bota:')
            tamanho, lado = numeraçao.split()
            sapato.append((tamanho,lado))
            
        for i in range (0,numero):
            tamanhoA,ladoA = sapato[i]
            for j in range (i +1,numero):
                tamanhoB,ladoB = sapato[j]
                if tamanhoA == tamanhoB and ladoA != ladoB:
                    pares= pares + 1
                
        print(f'A quantidade de pares é: {pares}')
        
    except EOFError:
        break
    
