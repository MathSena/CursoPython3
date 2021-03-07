import os
import shutil

caminho_original = 'C:/Users/MathS/Downloads/notas'
caminho_novo = 'C:/Users/MathS/OneDrive/Área de Trabalho/Imposto de Renda 2021'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'{caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_flile_path = os.path.join(caminho_original, file)
        print(new_flile_path)

        shutil.move(old_file_path, new_flile_path) #Movendo arquivos)
        print(f'Arquivo {file} movido com sucesso')