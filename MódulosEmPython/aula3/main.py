
import os


caminho_procura = 'C:/Users/MathS/OneDrive/Imagens/Amigos/Camp'
termo_procura = '09'

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    print(arquivos)
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta +=1
                caminho_completo = os.path.join(raiz,arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo: ', arquivo, tamanho)
                print('Caminho do arquivo: ', arquivo)
                print('Nome do arquivo: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)

            except PermissionError as e:
                print('Sem permissão!')
            except FileNotFoundError as e:
                print('Arquivo não encontrado!')
            except Exception as e:
                print('Erro desconhecido: ', e)

print()
print(f'{conta} arquivo (s) encotrado (s) ')