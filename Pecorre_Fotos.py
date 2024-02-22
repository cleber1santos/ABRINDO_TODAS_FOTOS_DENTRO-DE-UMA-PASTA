import os
import cv2

# Defina o caminho para a pasta que contém as imagens
pasta_imagens = 'license-plate-recognition/imgs'

# Lista todos os arquivos na pasta
arquivos = os.listdir(pasta_imagens)

# Filtra apenas arquivos com extensões de imagem comuns
extensoes_validas = ['.jpg', '.jpeg', '.png']
arquivos_imagem = [arq for arq in arquivos if any(arq.lower().endswith(ext) for ext in extensoes_validas)]


for arquivo in arquivos_imagem:
    caminho_completo = os.path.join(pasta_imagens, arquivo)
    img = cv2.imread(caminho_completo)
    if img is not None:
        cv2.imshow('Imagem', img)  # Exibe a imagem
        cv2.waitKey(200)  # Espera por 200ms antes de continuar
    else:
        print(f"Não foi possível carregar a imagem: {caminho_completo}")

cv2.destroyAllWindows()
