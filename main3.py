from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    curr_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
    return curr_time

if __name__ == '__main__':
    app.run()