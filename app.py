from flask import Flask, request
from rasa.core.agent import Agent
import asyncio
import os

app = Flask(__name__)
model = Agent("training_data.yml").load("models/"+os.listdir("models")[-1])
loop = asyncio.new_event_loop()
 
@app.route('/get', methods=['GET'])
def get():
    try:
        result = loop.run_until_complete(model.parse_message_using_nlu_interpreter(request.args.get("query")))
        loop.stop()
        return result
    except Exception as e:
        return str(e)

@app.route('/health', methods=['GET'])
def health():
    return "All good G!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)