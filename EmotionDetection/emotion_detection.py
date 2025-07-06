import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=input_json, headers=header)

    #Converting the response into a dictionary using json lib
    formatted_response = json.loads(response.text)

    #extracting the emotions with thier scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    #finding the dominant emotions in the dictionairy
    dominant_emotion = max(emotions, key=emotions.get)

    #to match the required output
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
