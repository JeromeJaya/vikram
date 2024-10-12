import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up the model
model = genai.GenerativeModel('gemini-pro')

def chat_with_gemini():
    print("Welcome to the Gemini Chatbot! Type 'quit' to exit.")
    
    # Start a conversation
    chat = model.start_chat(history=[])
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Generate a response
        response = chat.send_message(user_input)
        print("Gemini:", response.text)

if _name_ == "_main_":
    chat_with_gemini()
