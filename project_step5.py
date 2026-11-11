from flask import Flask
import os

LOG_FILE_NAME = "/home/pi/photos_final_project/photo_logs.txt"
previous_line_counter = 0

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/check-photos")
def check_photos():
    global previous_line_counter
    line_counter = 0
    if os.path.exists(LOG_FILE_NAME):
        last_photo_file_name = ""
        with open(LOG_FILE_NAME, "r") as f:
            for line in f:
                line_counter += 1
                last_photo_file_name = line.rstrip()
        difference = line_counter - previous_line_counter
        previous_line_counter = line_counter
        message = str(difference) + " new photos since you last checked"
        message += "Last photo: " + last_photo_file_name
        return message
    else:
        return "No photo available"
    

app.run(host="0.0.0.0")