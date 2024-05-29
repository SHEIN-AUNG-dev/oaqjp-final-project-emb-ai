"""
this program detects user's emotion based on their inputs
"""
#import flask
from flask import Flask, request, render_template
#import emotiondetction
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
#get emotion response from the url
@app.route("/emotionDetector")
def sent_emotion ():
    """
    This function is analyzed using emotion_detector moudle
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None :
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger' : {response['anger']}\
    ,'disgust' : {response['anger']},'fear' : {response['anger']}, 'joy' : {response['anger']} \
    and 'sadness' : {response['anger']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """
    To render static web page to interact
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
