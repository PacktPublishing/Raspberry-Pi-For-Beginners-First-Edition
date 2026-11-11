from gpiozero import MotionSensor, LED
from signal import pause
import time

# Global variables
time_motion_started = time.time()
last_time_photo_taken = 0
MOVEMENT_DETECTED_THRESHOLD = 5.0
MIN_DURATION_BETWEEN_PHOTOS = 30.0

# Setup GPIO
pir = MotionSensor(4)
led = LED(17)
print("GPIOs setup OK")

def motion_detected():
    print("Starting timer")
    global time_motion_started
    time_motion_started = time.time()
    led.on()
    
def motion_finished():
    global last_time_photo_taken
    led.off()
    motion_duration = time.time() - time_motion_started
    print(motion_duration)
    if motion_duration > MOVEMENT_DETECTED_THRESHOLD:
        if time.time() - last_time_photo_taken > MIN_DURATION_BETWEEN_PHOTOS:
            last_time_photo_taken = time.time()
            print("Taking a photo and sending it by email")
    

pir.when_motion = motion_detected
pir.when_no_motion = motion_finished
pause()