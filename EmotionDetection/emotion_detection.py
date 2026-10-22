import requests
import json


def emotion_detector(text_to_analyze):
    # URL of the Watson NLP emotion detection model
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # text imput taken as a dictionary
    myobj = {"raw_document": {"text": text_to_analyze}}

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # POST request sent 
    response = requests.post(url, json=myobj, headers=header)

    # For blank entry the server returns 400, so return None for every key
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Converted the response text into a dictionary
    formatted_response = json.loads(response.text)

    # Extracted the required emotions and their scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the dominant emotion (the one with the highest score)
    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }
    dominant_emotion = max(scores, key=scores.get)

    # 4. Return the required output format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }