from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    data = request.get_json()
    data = data["result"]["action"]
    print("Request_action: ", data)

    return "yo!"

if __name__ == "__main__":
    app.run()