import cv2
from deepface import DeepFace

# Carregar o classificador Haar Cascade para detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Verificar se o classificador foi carregado corretamente
if face_cascade.empty():
    raise IOError("Erro ao carregar o arquivo haarcascade_frontalface_default.xml")

# Iniciar a captura de vídeo da webcam
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Verificar se a webcam foi aberta corretamente
if not video.isOpened():
    raise IOError("Não foi possível abrir a webcam")

# Dicionário para traduzir emoções para português
emotions_dict = {
    'happy': 'Feliz',
    'sad': 'Triste',
    'angry': 'Bravo',
    'surprise': 'Surpreso',
    'disgust': 'Nojo',
    'fear': 'Medo',
    'neutral': 'Neutro'
}

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        print("Erro ao capturar frame")
        break

    # Converter para escala de cinza para detecção facial
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Processar cada rosto detectado
    for (x, y, w, h) in faces:
        # Desenhar retângulo ao redor do rosto
        cv2.rectangle(frame, (x, y), (x + w, y + h), (89, 2, 236), 2)

        # Extrair a região do rosto
        face_roi = frame[y:y + h, x:x + w]

        try:
            # Analisar a emoção usando DeepFace
            analyze = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)
            emotion = analyze[0]['dominant_emotion']

            # Traduzir a emoção para português
            emotion_pt = emotions_dict.get(emotion, emotion)

            # Exibir a emoção na tela
            cv2.putText(frame, emotion_pt, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (224, 77, 176), 2)

        except Exception:
            # Em caso de erro na análise, mostrar mensagem na tela
            cv2.putText(frame, "Erro na detecção", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Se nenhum rosto for detectado, mostrar mensagem na tela
    if len(faces) == 0:
        cv2.putText(frame, "Nenhum rosto detectado", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Exibir o frame resultante
    cv2.imshow('Detecção de Emoções', frame)

    # Sair do loop ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar as janelas
video.release()
cv2.destroyAllWindows()