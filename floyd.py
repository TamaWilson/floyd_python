INF = float("inf")

#Matriz de distancias entre cada Nó. INF = Nós não possuem ligação.
grafo =  [  [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0,   1],
            [INF, INF, INF, 0]
        ]

def floyd(grafo):
    ponderados = grafo
    
    len_matrix = len(grafo)
    
    #Aplicação do algoritmo de Floyd
    for k in range(len_matrix):
        for i in range(len_matrix):
            for j in range(len_matrix):
                ponderados[i][j] = min(ponderados[i][j], ponderados[i][k] + ponderados[k][j])                

    for itens in ponderados: #Printa a matriz final organizando a leitura
        print("")
        for item in itens:
            print("%s\t" % item, end="")
