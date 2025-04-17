import requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    formatted_response = json.loads(response.text)

    emotion = formatted_response["emotionPredictions"][0]["emotion"]

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