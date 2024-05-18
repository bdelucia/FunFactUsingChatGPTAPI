import os
from openai import OpenAI
from flask import Flask
from views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# chatGPT api implementation
client = OpenAI()

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

print(chat_gpt("Give me a fun fact"))

