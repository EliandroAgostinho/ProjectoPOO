import cv2
from Model.Face_Recognition_Handler import treinar_reconhecedor, reconhecer_rosto
from Model.Emotion_Analysis import analisar_emocao

class Controller:
    def __init__(self):
        self.modelo_lbph = None

    def treinar_modelo(self, imagens_treino, etiquetas):
        """
        Treina o LBPH usando as imagens fornecidas e etiquetas.
        """
        self.modelo_lbph = treinar_reconhecedor(imagens_treino, etiquetas)

    def reconhecer(self, imagem_teste):
        """
        Reconhece a cara na imagem de teste.
        """
        if not self.modelo_lbph:
            raise ValueError("O modelo não foi treinado ainda.")
        etiqueta, confianca = reconhecer_rosto(self.modelo_lbph, imagem_teste)
        if confianca > 100:  # Ajuste o limite de confiança conforme necessário
            raise ValueError("Rosto não reconhecido com confiança suficiente.")
        return etiqueta, confianca

    def analisar_emocao(self, caminho_imagem_teste):
        """
        Analisa a emoção na imagem de teste.
        """
        return analisar_emocao(caminho_imagem_teste)