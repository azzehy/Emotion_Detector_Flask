''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_analysis()
        function. The output returned shows the emotion and its confidence 
        score and the dominant emotion between all of them for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is \
        'anger': {anger}, \
        'disgust': {disgust}, \
        'fear': {fear}, \
        'joy': {joy} and \
        'sadness': {sadness}.\
        The dominant emotion is {dominant_emotion}."


@app.route("/")
def index():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
