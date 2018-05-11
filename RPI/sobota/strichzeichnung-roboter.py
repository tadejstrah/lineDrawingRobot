from flask import Flask
from flask import request
from stepper_control import speed
app = Flask(__name__)

@app.route('/a', methods=['POST'])
def home():
    data = request.get_json()
    data = data["result"]["action"]
    print("Request_action: ", data)
    if(data=='levo'):
        speed(0,500,1,1,4)
    elif(data=='desno'):
        speed(500,0,0,0,4)
    elif(data=='naprej'):
        speed(500,500,0,1,5)
    elif(data=='nazaj'):
        speed(500,500,1,0,5)
    return "yo!"

if __name__ == "__main__":
    app.run()
