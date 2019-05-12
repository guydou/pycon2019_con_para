from flask import Flask
app = Flask(__name__)
import time

@app.route("/")
def sleep_well():
    sleep_duration = 2
    time.sleep(sleep_duration)
    return "Hello World!"


