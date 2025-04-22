from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['tcc_backend']
collection = db['emotions']

def save_emotions(media_path, emotions):
    document = {
        'timestamp': datetime.now(),
        'media_path': media_path,
        'emotions': emotions
    }
    collection.insert_one(document)

def get_emotion_peaks(emotion_type):
    pipeline = [
        {'$sort': {f'emotions.{emotion_type}': -1}},
        {'$limit': 1}
    ]
    return list(collection.aggregate(pipeline))