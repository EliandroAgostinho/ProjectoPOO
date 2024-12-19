import cv2
import face_recognition
import numpy as np
import os 
import pickle
import uuid
import shutil
from pathlib import Path

import cv2
import face_recognition
import numpy as np
import os
import uuid
import shutil
from pathlib import Path

# Gerar um identificador único (UUID) para esse dataset
dataset_id = str(uuid.uuid4())  # UUID exclusivo para o dataset
print(f"ID exclusivo para o dataset: {dataset_id}")

# Caminho da pasta onde o projeto será armazenado
base_path = r"C:\Users\breno\OneDrive\Desktop\projeto de reconhecimento facial poo"
dataset_path = os.path.join(base_path, "imagens", dataset_id)

# Criação da pasta para o dataset único
Path(dataset_path).mkdir(parents=True, exist_ok=True)  # Cria a pasta com o UUID único

# Função para carregar os dados das imagens
def carregar_dados(dataset_path):
    imagens = []  # Aqui vamos armazenar as imagens de faces
    labels = []   # Aqui vamos armazenar os labels (IDs dos membros)
    
    # Caminho da pasta onde estão os dados (dataset)
    for pessoa_id in os.listdir(dataset_path):
        pessoa_path = os.path.join(dataset_path, pessoa_id)
        
        if os.path.isdir(pessoa_path):  # Se for uma pasta de um membro
            for imagem_name in os.listdir(pessoa_path):
                imagem_path = os.path.join(pessoa_path, imagem_name)
                # Carregar a imagem em RGB (mais adequado para face_recognition)
                img = cv2.imread(imagem_path)
                
                # Detectar as faces usando face_recognition
                face_locations = face_recognition.face_locations(img)
                
                for face_location in face_locations:
                    # Extraímos a face da imagem
                    top, right, bottom, left = face_location
                    face_img = img[top:bottom, left:right]
                    
                    # Redimensionar ou ajustar se necessário (opcional)
                    face_img = cv2.resize(face_img, (200, 200))  # Ajuste o tamanho da face se necessário
                    
                    imagens.append(face_img)
                    labels.append(int(pessoa_id))  # Usando o nome da pasta como ID do membro

    return imagens, labels

# Carregando as imagens e labels
imagens, labels = carregar_dados(dataset_path)

# Verificando quantas imagens e labels foram carregadas
print(f"Total de imagens carregadas: {len(imagens)}")
print(f"Total de labels carregados: {len(labels)}")

# Opcional: Para evitar conflitos em ambientes colaborativos, você pode mover o dataset para uma pasta separada
# Isso garante que o dataset gerado será armazenado de forma única para cada usuário.
# Aqui estou movendo para uma pasta chamada 'datasets_exclusivos'.
final_path = os.path.join(base_path, 'datasets_exclusivos', dataset_id)
shutil.move(dataset_path, final_path)
print(f"Dataset foi movido para: {final_path}")




