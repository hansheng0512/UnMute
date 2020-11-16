from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/receive_text', methods=["GET", "POST"])
def receive():
    return text_t

@app.route('/send_text', methods=["GET", "POST"])
def send_text():
    global text_t
    try:
        translation_text = request.form.get("converted_text")
        text_t = translation_text
        return "responed from server {}, translated text: {}".format(text_t, translation_text)
    except:
        return "ERROR"
    
@app.route('/pass_text', methods=["GET", "POST"])
def pass_text():
    return text

@app.route('/post_text', methods=["GET", "POST"])
def post_text():
    global text

    received_text = request.form.get("converted_text")
    text = received_text
    
    return "Done"

if __name__ == "__main__":
    app.run(debug=True)