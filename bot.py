import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up the model
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('input', '')

    # Start a conversation
    chat = model.start_chat(history=[])
    
    # Generate a response
    response = chat.send_message(user_input)
    
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
