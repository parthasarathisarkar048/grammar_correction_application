# Grammar Error Correction Application (Flask + Python)
## Project Overview

The Grammar Error Correction Application is a web-based system that detects and corrects grammatical errors in English text. The application allows users to enter text manually or upload a text file for batch grammar correction. The system uses Python, Flask, and a grammar correction library to process text and return corrected output.

## Features
* Grammar correction for sentences
* Real-time correction from text input
* File upload and batch correction
* Download corrected file
* Web-based interface
* Flask backend processing
* Corpus-based probability support
* Evaluation using JFLEG dataset (for performance testing)

## Technologies Used
* Python
* Flask
* HTML
* JavaScript
* LanguageTool (Grammar correction)
* NLTK
* JFLEG Dataset
* Machine Learning Evaluation Metrics
## Project Structure
```
grammar-correction-app/

├── app.py
├── grammar_model.py
├── evaluator.py
├── corpus.txt
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── script.js
├── uploads/
├── corrected/
├── jfleg/
   └──correct.txt
   └──corrected_by_model.txt
   └──original.txt
```

## Installation Instructions
* Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate
* Install Dependencies
pip install -r requirements.txt
* Install Java (Required for LanguageTool)

Install Java JDK and check:

java -version
* Download LanguageTool Data
python -m language_tool_python.download

## Running the Application
python app.py

Open browser:

http://127.0.0.1:5000
## How to Use
1. Enter text in the text area and click Correct Grammar
2. The corrected text will be displayed below
3. Upload a text file to correct grammar in the entire file
4. Download the corrected file

## Example Input
```
i are a student.
she go to school yesterday.
he have a car.
they is playing.
```
## Example Output
```
I am a student.
She went to school yesterday.
He has a car.
They are playing.
```

## Evaluation Metrics

### The system can be evaluated using:
* Accuracy
* Precision
* Recall
* F1 Score
* BLEU Score
* GLEU Score
* Word Error Rate (WER)

Evaluation is performed using the JFLEG Grammar Correction Dataset.

## Future Improvements
1. Add deep learning grammar correction model
2. Improve corpus probability model
3. Add multiple language support
4. Deploy application online
5. Add user login system

### Author

Partha Sarathi Sarkar
