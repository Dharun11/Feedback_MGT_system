from flask import render_template, Flask, request, redirect, url_for, flash
import sqlite3
from src.db import Databaseconnect
from src.sentiment import SentimentAnalysis

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages

db = Databaseconnect()
analysis = SentimentAnalysis()

@app.route('/', methods=["GET"])
def index():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    result = cursor.fetchall()
    conn.close()
    return render_template('index.html', feedbacks=result)  # Fixed template variable

@app.route('/clean_record',methods=["GET"])
def clean_records():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM feedback")
    res=cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template('index.html',feedbacks=res)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']
    sentiment = analysis.analyse_sentiment(feedback)
    
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (name, email, feedback, sentiment) VALUES (?, ?, ?, ?)',
                   (name, email, feedback, sentiment))
    conn.commit()
    conn.close()
    
    flash('Feedback submitted successfully!', 'success')
    return render_template('home.html', sentiment=sentiment)  # Fixed template variable

if __name__ == '__main__':
    app.run(debug=True)