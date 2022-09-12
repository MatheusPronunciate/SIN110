'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

import numpy as np

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''


def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0:                                                      # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


def tipoGrafo(matriz):
    #inicializa valores para identificar o tipo do grafo
    laco = False
    arestaMultipla = False
    direcionado = False
    
    # Descobrir a dimensão da matriz
    qtdVertices = np.shape(matriz)[0]                                           
    for vi in range(0, qtdVertices):                                            # Para vi
        if matriz[vi][vi] >= 1:                                                 # verifica se possui laço, caso sim, define como True
            laco = True                                                         
        if matriz[vi][vi] > 1:                                                  # verifica se possui arestas multiplas, caso sim, define como True
            arestaMultipla = True                                               
        for vj in range(vi + 1, qtdVertices):                                   # Para vj
            escolha = matriz[vi][vj]
            while escolha > 0:                                                 # Adiciona a quantidade de arestas paralelas ou peso da aresta
                if (matriz[vi][vj]) != (matriz[vj][vi]):                        # verifica se é um grafo direcionado (DÍGRAFO)
                    direcionado = True
                if escolha > 1:                                                # verifica se possui arestas multiplas
                    arestaMultipla = True
                escolha -= 1
    if not laco and not arestaMultipla:                                         # se possui laco e não tem arestas multiplas: GRAFO SIMPLES
        return 0                                                                # simples
    if direcionado:                                                             # se e um grafo direcionado: DIGRAFO
        return 1                                                                # dígrafo
    if not laco and arestaMultipla:                                             # se nao possui laco e possui arestas multiplas: MULTIGRAFO
        return 2                                                                # multigrafo
    if laco and arestaMultipla:                                                 # se possui laco e não possui arestas multiplas : PSEUDOGRAFO
        return 3                                                                # pseudografo


def calcDensidade(matriz):
    densidade = 0
    qtdVertices = np.shape(matriz)[0]                                           # descobre quantidade de vertices
    qtdArestas = 0
    x = tipoGrafo(matriz)
    simples = x == 0
    digrafo = x == 1

    # calcula quantidade de arestas
    for vi in range(0, qtdVertices):                                            # Para cada vértice vi
        for vj in range(vi + 1, qtdVertices):                                   # Para cada vértice vj
            escolha = matriz[vi][vj]
            while escolha > 0:
                qtdArestas += 1
                escolha -= 1

    if simples:                                                                 # calcula densidade para um grafo simples
        densidade = (2 * qtdArestas) / (qtdVertices * (qtdVertices - 1))
    if digrafo:                                                                 # calcula a densidade para um grafo digrafo
        densidade = qtdArestas / (qtdVertices * (qtdVertices - 1))

    densidadeArred = "{:.3f}".format(densidade)
    return float(densidadeArred)


def insereAresta(matriz, vi, vj):
    matriz[vi][vj] += 1                                                         # soma um na posição(aresta) desejada
    return matriz

def insereVertice(matriz, vi):
    vi = []                                                                     # define vi como um vetor vazio
    size = np.shape(matriz)                                                     # decobre a densidade da matriz
    x = size[0]
    # adiciona valores ao vetor
    while x > 0:
        vi.append(3)
        x -= 1
    npVetor = np.vetor(vi)                                                      # transforma um vetor em um vetor numpy
    matriz = np.insert(matriz, matriz.shape[0], [npVetor], axis=0)              # metodo para inserir no vetor numpy
    vi.append(0)
    colunaAdicionada = np.Vetor(vi)
    # adiciona coluna a matriz numpy
    matriz = np.column_stack((matriz, colunaAdicionada))
    return matriz


def removeVertice(matriz, vi):
    vetor = np.vetor(matriz)                                                    # define como vetor do tipo numpy
    vetor = np.delete(vetor, vi, axis=0)                                        # metodo para remover linha do vetor numpy
    resultado = np.delete(vetor, vi, 1)                                         # deleta coluna do vertice inserida pelo usuário
    return resultado

def removeAresta(matriz, vi, vj):
    if matriz[vi][vj] > 0:                                                     # Se matriz (aresta) maior que 0, subtrai um na aresta desejada
        matriz[vi][vj] -= 1
    return