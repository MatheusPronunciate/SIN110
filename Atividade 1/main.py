import entradaDados as ent
import saidaDados as sai

if __name__=='__main__':
  nomeArquivo=input("Insira o nome do arquivo que deseja: ")
  resultado = ent.entradaDados(nomeArquivo) # Passa o nome da intância como argumento
  sai.saidaDados(resultado)