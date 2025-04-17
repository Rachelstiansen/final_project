import requests
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers    
    formatted_response = json.loads(response.text)

    emotion = formatted_response["emotionPredictions"][0]["emotion"]

    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None}

    anger_score = emotion['anger']
    disgust_score = emotion["disgust"]
    fear_score = emotion["fear"]
    joy_score = emotion["joy"]
    sadness_score = emotion["sadness"]

    max_emotion = max(emotion.items(), key=lambda x: x[1])
    dominant_emotion = max_emotion[0]

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
            'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}

"""
import json
from emotion_detection import emotion_detector
response = emotion_detector("I am so happy I am doing this.")

"""