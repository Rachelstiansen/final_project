import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    print(response.text)

    anger_score = formatted_response["documentSentiment"]["anger"]
    disgust_score = formatted_response["documentSentiment"]["disgust"]
    fear_score = formatted_response["documentSentiment"]["fear"]
    joy_score = formatted_response["documentSentiment"]["joy"]
    sadness_score = formatted_response["documentSentiment"]["sadness"]

    emotion = formatted_response['emotionPredictions'][0]['emotion']
    max_emotion = max(emotion.items(), key=lambda x: x[1])
    dominant_emotion = max_emotion[0]

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
            'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}



"""
import json
from emotion_detection import emotion_detector
response = emotion_detector("I love this new technology")
"""