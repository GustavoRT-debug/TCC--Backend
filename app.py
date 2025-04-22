from flask import Flask, request, jsonify
from capture import capture_media
from emotion_analysis import analyze_emotions
from pymongo import MongoClient
from datetime import datetime
import os
import schedule
import time
import threading

app = Flask(__name__)

# Configurar MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['tcc_backend']
collection = db['emotions']

# Função para salvar emoções no banco
def save_emotions(media_path, emotions):
    document = {
        'timestamp': datetime.now(),
        'media_path': media_path,
        'emotions': emotions
    }
    collection.insert_one(document)

# Função para encontrar pico de uma emoção
def get_emotion_peaks(emotion_type):
    pipeline = [
        {'$sort': {f'emotions.{emotion_type}': -1}},
        {'$limit': 1}
    ]
    return list(collection.aggregate(pipeline))

# Endpoint para capturar e analisar
@app.route('/capture-and-analyze', methods=['POST'])
def capture_and_analyze():
    try:
        data = request.json
        media_type = data.get('media_type', 'image')
        filename = f"capture_{int(os.times()[4])}"
        media_path = capture_media(media_type, filename)
        emotions = analyze_emotions(media_path)
        save_emotions(media_path, emotions)
        return jsonify({'media_path': media_path, 'emotions': emotions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint para upload de mídia (caso a captura seja no cliente)
@app.route('/analyze-upload', methods=['POST'])
def analyze_upload():
    if 'media' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    file = request.files['media']
    media_path = f"uploads/{file.filename}"
    file.save(media_path)
    try:
        emotions = analyze_emotions(media_path)
        save_emotions(media_path, emotions)
        return jsonify({'emotions': emotions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if os.path.exists(media_path):
            os.remove(media_path)

# Endpoint para consultar pico de emoção
@app.route('/peak-emotion/<emotion_type>', methods=['GET'])
def peak_emotion(emotion_type):
    try:
        peak = get_emotion_peaks(emotion_type)
        return jsonify(peak[0] if peak else {'error': 'Nenhum dado encontrado'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Função de agendamento para capturas automáticas
def scheduled_capture():
    try:
        filename = f"capture_{int(time.time())}"
        media_path = capture_media('image', filename)
        emotions = analyze_emotions(media_path)
        save_emotions(media_path, emotions)
        print(f"Emoções detectadas: {emotions}")
    except Exception as e:
        print(f"Erro na captura agendada: {str(e)}")

# Configurar agendamento (a cada 10 segundos)
schedule.every(10).seconds.do(scheduled_capture)

# Função para rodar o agendador em uma thread separada
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Iniciar o agendador em uma thread
def start_scheduler():
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    start_scheduler()
    app.run(debug=True, port=5000)