"""
This module analyzes text sentiment

"""
import json
import requests

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotiont of the given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary containing the emotion.
    """

    # URL of the emotion analysis service
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        #return formatted_response
        anger_score     = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score   = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score      = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score       = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score   = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        emotion_scores  = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }



'''
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
    # If the response status code is 500, set label and score to None
    elif response.status_code == 404:

'''
