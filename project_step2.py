from gpiozero import MotionSensor, LED
from picamzero import Camera
from signal import pause
import time
import os

def take_photo(camera, folder_path):
    file_name = folder_path + "/img_" + str(time.time()) + ".jpg"
    camera.take_photo(file_name)
    return file_name

# Global variables
time_motion_started = time.time()
last_time_photo_taken = 0
MOVEMENT_DETECTED_THRESHOLD = 5.0
MIN_DURATION_BETWEEN_PHOTOS = 30.0
CAMERA_FOLDER_PATH = "/home/pi/photos_final_project"

# Setup Camera
camera = Camera()
camera.still_size = (1536, 864)
camera.flip_camera(vflip=True, hflip=True)
time.sleep(2)
if not os.path.exists(CAMERA_FOLDER_PATH):
    os.mkdir(CAMERA_FOLDER_PATH)
print("Camera setup OK")

# Setup GPIOs
pir = MotionSensor(4)
led = LED(17)
print("GPIOs setup OK")

def motion_detected():
    # print("Starting timer")
    global time_motion_started
    time_motion_started = time.time()
    led.on()
    
def motion_finished():
    global last_time_photo_taken
    led.off()
    motion_duration = time.time() - time_motion_started
    # print(motion_duration)
    if motion_duration > MOVEMENT_DETECTED_THRESHOLD:
        if time.time() - last_time_photo_taken > MIN_DURATION_BETWEEN_PHOTOS:
            last_time_photo_taken = time.time()
            print("Taking a photo and sending it by email")
            photo_file_name = take_photo(camera, CAMERA_FOLDER_PATH)
            

pir.when_motion = motion_detected
pir.when_no_motion = motion_finished
pause()