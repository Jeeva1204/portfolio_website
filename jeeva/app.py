from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # Here you can add code to:
        # 1. Save the message to a database
        # 2. Send an email notification
        # 3. Integrate with a CRM system
        
        return jsonify({
            'status': 'success',
            'message': 'Thank you for your message! I will get back to you soon.'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'An error occurred while processing your message.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 