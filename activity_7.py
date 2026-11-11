from gpiozero import LED, Button
from signal import pause

led_list = [LED(17), LED(27), LED(22)]
button = Button(26, bounce_time=0.05)
led_index = 0

def reset_leds():
    for led in led_list:
        led.off()

def switch_led():
    global led_index
    reset_leds()
    led_list[led_index].on()
    led_index += 1
    if led_index >= len(led_list):
        led_index = 0

reset_leds()
button.when_pressed = switch_led
pause()