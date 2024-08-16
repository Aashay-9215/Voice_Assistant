from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(
    api_key = OPENAI_API_KEY
)

def ai_reply(command):
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named John."},
            {"role": "user", "content": command}
        ]
    )
    return(completion.choices[0].message.content)
