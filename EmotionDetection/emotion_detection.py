import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = {"raw_document":{"text": text_to_analyze}}
    response = requests.post(url, json = my_obj, headers=headers)
    formatted_response = json.loads(response.text)
    if response.status_code == 200 :
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        result = {'anger': anger_score, 'disgust': disgust_score, 'fear' : fear_score, 'joy' : joy_score,
        'sadness' : sadness_score }
        test_key = 'anger'
        for key in result.keys():
            if result[test_key] < result[key]:
                test_key = key
        dominant_emotion = test_key
        result["dominant_emotion"] = dominant_emotion
    elif response.status_code == 400 :
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
        result = {'anger': anger_score, 'disgust': disgust_score, 'fear' : fear_score, 'joy' : joy_score,
        'sadness' : sadness_score, 'dominant_emotion' : dominant_emotion}
    
    return result