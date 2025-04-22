import cv2
import os

def capture_media(media_type='image', filename='capture'):
    output_path = f"uploads/{filename}.{'jpg' if media_type == 'image' else 'mp4'}"
    
    # Inicializar webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Não foi possível acessar a webcam")

    if media_type == 'image':
        # Capturar uma foto
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(output_path, frame)
        else:
            raise Exception("Falha ao capturar imagem")
    else:
        # Capturar vídeo (5 segundos)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))
        for _ in range(100):  # 100 frames (~5 segundos a 20 fps)
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                raise Exception("Falha ao capturar vídeo")
        out.release()

    cap.release()
    return output_path