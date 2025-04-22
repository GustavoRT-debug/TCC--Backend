import schedule
import time
from capture import capture_media
from emotion_analysis import analyze_emotions
import os

def job():
    try:
        filename = f"capture_{int(time.time())}"
        media_path = capture_media('image', filename)
        emotions = analyze_emotions(media_path)
        print(f"Emoções detectadas: {emotions}")
        # Salvar no banco de dados, se necessário
    except Exception as e:
        print(f"Erro: {str(e)}")

# Agendar captura a cada 10 segundos
schedule.every(10).seconds.do(job)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)