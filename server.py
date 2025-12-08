"""This is the server script"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def run_sentiment_analysis():
    """ This function runs the emotion detection function"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the scores and the dominant emotion
    anger_score = response.get('anger')
    disgust_score = response.get('disgust')
    fear_score = response.get('fear')
    joy_score = response.get('joy')
    sadness_score = response.get('sadness')
    dominant_emotion = response.get('dominant_emotions')

    if dominant_emotion is None:
        return "invalid text!, Please try again!"

    # Format the output string
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return output_string

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
