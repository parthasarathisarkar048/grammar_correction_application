from flask import Flask, render_template, request, send_file
import os
from grammar_model import correct_grammar

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
CORRECTED_FOLDER = "corrected"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CORRECTED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct_text():
    text = request.form.get('text')
    corrected = correct_grammar(text)
    return corrected

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        corrected_text = correct_grammar(text)

        corrected_path = os.path.join(CORRECTED_FOLDER, "corrected_" + file.filename)
        with open(corrected_path, 'w', encoding='utf-8') as f:
            f.write(corrected_text)

        return send_file(corrected_path, as_attachment=True)

    return "No file uploaded"

if __name__ == '__main__':
    app.run(debug=True)