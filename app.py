from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current date and time: {current_date}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
