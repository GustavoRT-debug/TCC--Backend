from deepface import DeepFace
import cv2
import os

def analyze_emotions(media_path):
    # Se for vídeo, extrair o primeiro frame
    if media_path.endswith('.mp4'):
        cap = cv2.VideoCapture(media_path)
        ret, frame = cap.read()
        if not ret:
            cap.release()
            raise Exception("Falha ao extrair frame do vídeo")
        frame_path = media_path.replace('.mp4', '_frame.jpg')
        cv2.imwrite(frame_path, frame)
        cap.release()
        media_path = frame_path

    # Analisar emoções
    try:
        result = DeepFace.analyze(img_path=media_path, actions=['emotion'], enforce_detection=True)
        emotions = result[0]['emotion']
        return {
            'happy': emotions['happy'],
            'sad': emotions['sad'],
            'angry': emotions['angry'],
            'surprise': emotions['surprise'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'neutral': emotions['neutral']
        }
    except Exception as e:
        return {'error': f'Erro na análise: {str(e)}'}
    finally:
        # Remover frame temporário, se criado
        if media_path.endswith('_frame.jpg') and os.path.exists(media_path):
            os.remove(media_path)