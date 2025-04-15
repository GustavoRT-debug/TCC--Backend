import cv2
from deepface import DeepFace

class FacialExpressionDetector:
    def __init__(self):
        # Mapeamento de emoções para positiva (0) ou negativa (1)
        self.emotion_classification = {
            "happy": "positiva",    # 0
            "surprise": "positiva", # 0
            "sad": "negativa",      # 1
            "angry": "negativa",    # 1
            "fear": "negativa",     # 1
            "disgust": "negativa",  # 1
            "neutral": "positiva"   # 0 (ajustável, pode ser ignorado)
        }
        self.classification_to_bit = {
            "positiva": "0",
            "negativa": "1"
        }
        self.supported_emotions = ["happy", "sad", "neutral", "angry", "surprise", "fear", "disgust"]

    def detect_emotion(self, frame):
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
            return emotion if emotion in self.supported_emotions else "neutral"
        except:
            return "neutral"

    def classify_emotion(self, emotion):
        return self.emotion_classification.get(emotion, "positiva")

    def encode_emotion(self, classification):
        return self.classification_to_bit.get(classification, "0")

    def process_frame(self, frame):
        emotion = self.detect_emotion(frame)
        classification = self.classify_emotion(emotion)
        bit = self.encode_emotion(classification)
        return emotion, classification, bit

    def save_data(self, emotion, classification, bit, output_file="output.txt"):
        with open(output_file, "a") as f:
            f.write(f"{emotion}|{classification}|{bit}\n")