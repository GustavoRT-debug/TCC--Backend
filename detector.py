import cv2
import mediapipe as mp
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

class FacialExpressionDetector:
    def __init__(self):
        # Inicializa o MediaPipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.5)

        # Modelo de classificação (SVM com dados fictícios para exemplo)
        self.emotion_classifier = SVC(kernel='linear', probability=True)
        self.scaler = StandardScaler()

        # Mapeamento de emoções para bits
        self.emotion_to_bits = {
            "feliz": "00",
            "triste": "01",
            "neutro": "10",
            "raiva": "11"
        }

        # Treina o modelo com dados fictícios (substitua por FER2013 para resultados reais)
        self.train_model()

    def train_model(self):
        # Dados fictícios (100 amostras, 468 pontos * 2)
        X_train = np.random.rand(100, 936)
        y_train = np.random.choice(["feliz", "triste", "neutro", "raiva"], 100)
        X_train = self.scaler.fit_transform(X_train)
        self.emotion_classifier.fit(X_train, y_train)

    def preprocess_frame(self, frame):
        # Converte o frame para RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return rgb, frame.shape

    def detect_landmarks(self, rgb_frame, frame_shape):
        # Detecta pontos faciais
        results = self.face_mesh.process(rgb_frame)
        if not results.multi_face_landmarks:
            return None
        landmarks = np.array([(lm.x * frame_shape[1], lm.y * frame_shape[0])
                             for lm in results.multi_face_landmarks[0].landmark])
        return landmarks

    def normalize_landmarks(self, landmarks):
        # Normaliza os pontos
        landmarks_flat = landmarks.flatten()
        return self.scaler.transform([landmarks_flat])[0]

    def predict_emotion(self, landmarks):
        # Prediz a emoção
        normalized_landmarks = self.normalize_landmarks(landmarks)
        emotion = self.emotion_classifier.predict([normalized_landmarks])[0]
        return emotion

    def encode_emotion(self, emotion):
        # Codifica em bits
        return self.emotion_to_bits.get(emotion, "10")  # Neutro como padrão

    def process_frame(self, frame):
        # Pipeline para um frame
        rgb, frame_shape = self.preprocess_frame(frame)
        landmarks = self.detect_landmarks(rgb, frame_shape)
        if landmarks is None:
            return None, None, None
        emotion = self.predict_emotion(landmarks)
        bits = self.encode_emotion(emotion)
        return landmarks, emotion, bits

    def save_data(self, landmarks, bits, output_file="output.txt"):
        # Salva os dados
        with open(output_file, "a") as f:
            landmarks_str = ",".join([f"{x:.2f},{y:.2f}" for x, y in landmarks])
            f.write(f"{landmarks_str}|{bits}\n")