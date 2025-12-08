""" This module does the emotion analysis through Watson AI"""
import requests, json

def emotion_detector(text_to_analyse):
    """This function connects to the waston AI and does the sentiment analysis"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotions': None
        }

    emotions_detected = json.loads(response.text)

    # Extract the emmotion from the dictionary
    anger_score = emotions_detected['emotionPredictions'][0]['emotion']['anger']
    disgust_score = emotions_detected['emotionPredictions'][0]['emotion']['disgust']
    fear_score = emotions_detected['emotionPredictions'][0]['emotion']['fear']
    joy_score = emotions_detected['emotionPredictions'][0]['emotion']['joy']
    sadness_score = emotions_detected['emotionPredictions'][0]['emotion']['sadness']

    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }

    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotions'] = dominant_emotion

    return emotions


"""
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I am really mad about this")
"""