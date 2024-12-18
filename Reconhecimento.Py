
import cv2
import numpy as np
from deepface import Deepface

def treinar_reconhecedor(imagens_treino, etiquetas): # Treina o modelo LBPH com as imagens fornecids.
    reconhecedor = cv2.face.LBPHFaceRecognizer_create()
    reconhecedor.train(imagens_treino, np.array(etiquetas))
    return reconhecedor

def reconhecer_rosto(reconhecedor, imagem_teste): # Reconhece o rosto e devolve a etiqueta prevista e o grau de confiança
 
    cinzento = cv2.cvtColor(imagem_teste, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza
    etiqueta, confianca = reconhecedor.predicao(cinzento)  # Predição
    return etiqueta, confianca


# 4: Reconhecimento de Emoções com Grau de Confiança 

def analisar_emocao(caminho_imagem): # Analisa a emoção na imagem e devolve a emoção apresentada.

    resultado = DeepFace.analyze(img_path=caminho_imagem, resultado=['emotion'], forcar_detecao=False)
    emocao = resultado[0]['dominant_emotion']
    confianca = resultado[0]['emotion'][emocao]
    return emocao, confianca


# Execução Principal 

if __name__ == "__main__":

    imagens_treino = [cv2.imread("rosto1.jpg", cv2.IMREAD_GRAYSCALE), 
                      cv2.imread("rosto2.jpg", cv2.IMREAD_GRAYSCALE)]
    
    etiquetas = [101, 102]  # Etiquetas associadas às imagens de treino

    # Treinar o modelo
    modelo_lbph = treinar_reconhecedor(imagens_treino, etiquetas)

    # Imagem de teste
    imagem_teste = cv2.imread("rosto_teste.jpg")
    etiqueta_prevista, grau_confianca = reconhecer_rosto(modelo_lbph, imagem_teste)
    print(f"Reconhecimento Facial -> Etiqueta Prevista: {etiqueta_prevista}, Confiança: {grau_confianca:.2f}")

    #  Análise de Emoções 
    caminho_imagem_teste = "rosto_teste.jpg"
    emocao, confianca_emocao = analisar_emocao(caminho_imagem_teste)
    print(f"Reconhecimento de Emoções -> Emoção: {emocao}, Confiança: {confianca_emocao:.2f}%")


  ''' if __name__ == "__main__":
     # Exemplo de uso para reconhecimento facial
    reconhecedor = ReconhecimentoFacial()
    reconhecedor.treinar(imagens_treino, etiquetas)
    etiqueta, confianca = reconhecedor.prever(imagem_teste)
    print(f"Etiqueta: {etiqueta}, Confiança: {confianca}")

    # Exemplo de uso para analisar emoções
    emocao, grau_confianca = AnaliseEmocional.analisar("rosto_teste.jpg")
    print(f"Emoção: {emocao}, Confiança: {grau_confianca}"   '''