import numpy


def entradaDados(nomeArquivo):                                                                      # Nome da Função. Recebe o nome do arquivo.
    caminho = r"C:/Users/Pronu/PycharmProjects/pythonProject/instancias/" + nomeArquivo + '.txt'    # Caminho do arquivo .txt
    array = numpy.loadtxt(caminho)                                                                  # Carregando dados do arquivo e colocando numa matriz tipo numpy
    return nomeArquivo, array.shape                                                                 # retornando nome do arquivo e a dimensão da matriz
