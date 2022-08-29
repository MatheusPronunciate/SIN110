

def saidaDados(resultado):
    file = open(r"C:/Users/Pronu/PycharmProjects/pythonProject/resultado/resultado.txt", "a+")      # Caminho para criação do arquivo, a+ = append
    stringConcatenada = f'{resultado[0]} {resultado[1][0]} {resultado[1][1]}'                       # Concatenando as informações da matriz no formato: nome_instância qtd_linhas qtd_colunas.
    file.writelines(stringConcatenada+'\n')                                                         #escrevendo no arquivo as informações: nome e quantidade de linhas/colunas
    print('Operação concluida!')
    file.close()                                                                                    #fecha arquivo após escrita