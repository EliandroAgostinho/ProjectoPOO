import os
import cv2
import numpy as np
from deepface import DeepFace

class FaceRecognition:
    def __init__(self, images_path):
        self.images_path = images_path
        self.known_faces = []
        self.known_names = []
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()  # Alteração para a versão mais recente do OpenCV

    def load_known_faces(self):
        """Carrega as imagens e codifica os rostos conhecidos."""
        images = [f for f in os.listdir(self.images_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

        if len(images) < 2:
            raise ValueError("É necessário ter pelo menos duas imagens para treinar o modelo.")

        training_images = []
        labels = []
        label_map = {}
        label_counter = 0

        for image_name in images:
            image_path = os.path.join(self.images_path, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if image is None:
                print(f"Erro ao carregar a imagem: {image_name}")
                continue

            label = os.path.splitext(image_name)[0]
            if label not in label_map:
                label_map[label] = label_counter
                label_counter += 1

            labels.append(label_map[label])
            training_images.append(image)
        
        if len(training_images) == 0:
            raise ValueError("Nenhuma imagem válida foi carregada. Verifique o diretório.")

        self.recognizer.train(training_images, np.array(labels))
        print("Modelo treinado com sucesso!")

    def recognize_faces(self, frame):
        """Reconhece rostos em um frame de vídeo e calcula a confiança."""
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            face = gray_frame[y:y+h, x:x+w]
            label, confidence = self.recognizer.predict(face)
            name = f"Label: {label} - Confiança: {confidence:.2f}"

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        return frame

class EmotionDetection:
    def detect_emotion(self, image_path):
        """Detecta a emoção dominante em uma imagem."""
        try:
            # Verifica se a imagem pode ser carregada
            img = cv2.imread(image_path)
            if img is None:
                print(f"Erro: Imagem não encontrada ou não pode ser carregada: {image_path}")
                return "Erro", 0

            # Passando enforce_detection=False para permitir detecção de emoções sem rosto detectado
            result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)

            # Verifica se o resultado é uma lista e acessa o primeiro item corretamente
            if isinstance(result, list):
                dominant_emotion = result[0]['dominant_emotion']
                confidence = result[0]['emotion'][dominant_emotion]
                return dominant_emotion, confidence
            else:
                print("Erro: O resultado não está no formato esperado.")
                return "Erro", 0
        except Exception as e:
            print(f"Erro ao detectar emoção: {e}")
            return "Erro", 0

class ImageProcessing:
    def pixelize_image(self, image, pixel_size=10):
        """Pixeliza uma imagem."""
        height, width = image.shape[:2]
        small_image = cv2.resize(image, (pixel_size, pixel_size), interpolation=cv2.INTER_LINEAR)
        pixelated_image = cv2.resize(small_image, (width, height), interpolation=cv2.INTER_NEAREST)
        return pixelated_image

class FacialRecognitionApp:
    def __init__(self, images_path):
        self.face_recognition = FaceRecognition(images_path)
        self.emotion_detection = EmotionDetection()
        self.image_processing = ImageProcessing()
        self.face_recognition.load_known_faces()

    def run(self):
        """Executa o sistema de reconhecimento facial e detecção de emoções."""
        capture = cv2.VideoCapture(0)

        while True:
            ret, frame = capture.read()
            if not ret:
                break

            # Reconhecimento facial
            frame = self.face_recognition.recognize_faces(frame)

            # Verifica se um rosto foi detectado
            if np.count_nonzero(frame) > 0:  
                try:
                    cv2.imwrite("temp_frame.jpg", frame)
                    emotion, confidence = self.emotion_detection.detect_emotion("temp_frame.jpg")
                    cv2.putText(frame, f"Emoção: {emotion} ({confidence:.2f})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                except Exception as e:
                    print(f"Erro ao detectar emoção: {e}")
            else:
                print("Nenhum rosto detectado no frame.")

            # Exibe o frame resultante
            cv2.imshow('Reconhecimento Facial', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Caminho absoluto da pasta de imagens para treinamento
    images_path = "projeto de reconhecimento facial poo/imagens/membro1"

    try:
        app = FacialRecognitionApp(images_path)
        app.run()
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

