import cv2
from detector import FacialExpressionDetector

def main():
    # Inicializa o detector
    detector = FacialExpressionDetector()

    # Inicializa a webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro: Não foi possível abrir a webcam.")
        return

    while True:
        # Captura o frame
        ret, frame = cap.read()
        if not ret:
            print("Erro: Não foi possível capturar o frame.")
            break

        # Processa o frame
        landmarks, emotion, bits = detector.process_frame(frame)

        # Desenha os resultados
        if landmarks is not None:
            # Desenha os pontos faciais
            for x, y in landmarks:
                cv2.circle(frame, (int(x), int(y)), 1, (0, 255, 0), -1)
            
            # Exibe a emoção e bits
            text = f"Emoção: {emotion} ({bits})"
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Salva os dados
            detector.save_data(landmarks, bits)

        else:
            # Mensagem se nenhuma face for detectada
            cv2.putText(frame, "Nenhuma face detectada", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Exibe o frame
        cv2.imshow("Detecção de Expressões Faciais", frame)

        # Para a captura ao pressionar 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Libera os recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()