"""Detecting emotions of a given text."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emot_detector():
    """Function to detect emotions of a given text."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid input! Try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f" The dominant emotion is {dominant_emotion}")

@app.route("/")
def render_index_page():
    """To render index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
