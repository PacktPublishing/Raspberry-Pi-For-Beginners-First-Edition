from flask import Flask
from gpiozero import Button, LED

button = Button(26, bounce_time=0.05)
led_list = [LED(17), LED(27), LED(22)]
for led in led_list:
    led.off()
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask"

@app.route("/push-button")
def check_push_button_state():
    if button.is_pressed:
        return "Button is pressed"
    return "Button is not pressed"

@app.route("/led/<int:led_number>/state/<int:state>")
def switch_led(led_number, state):
    if led_number < 0 or led_number >= len(led_list):
        return "Wrong LED number: " + str(led_number)
    if state != 0 and state != 1:
        return "State must be 0 or 1"
    if state == 0:
        led_list[led_number].off()
    else:
        led_list[led_number].on()
    return "OK"
    
app.run(host="0.0.0.0")
