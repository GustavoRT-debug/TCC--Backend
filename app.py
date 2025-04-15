import cv2
from detector import FacialExpressionDetector

def main():
    detector = FacialExpressionDetector()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro: Não foi possível abrir a webcam.")
        return
    # Reduzir resolução para melhorar performance
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro: Não foi possível capturar o frame.")
            break
        emotion, classification, bit = detector.process_frame(frame)
        text = f"Emoção: {emotion} ({classification}, {bit})"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        detector.save_data(emotion, classification, bit)
        cv2.imshow("Detecção de Emoções", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()