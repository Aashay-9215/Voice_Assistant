import google.generativeai as genai
import os
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def gemini_reply(command):
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "You are a virtual assistant named John like Alexa. Answer any queries I ask in 100-150 words. Reply in a paragraph not in a list ever"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )
    response = chat.send_message(command)
    return(response.text)