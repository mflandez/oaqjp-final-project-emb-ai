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
    #label = "UNKNOWN"
    #score = "UNKNOWN"
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
    # Returning a dictionary containing sentiment analysis results
    return formatted_response

'''
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
    # If the response status code is 500, set label and score to None
    elif response.status_code == 404:

'''
