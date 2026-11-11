import os
from picamzero import Camera
import time

folder_name = "/home/pi/camera/activity_10"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

camera = Camera()
camera.still_size = (1536, 864)
camera.flip_camera(hflip=True, vflip=True)
time.sleep(2)
print("Camera has been initialized")

counter = 0
try:
    while True:
        file_name = folder_name + "/image" + str(counter) + ".jpg"
        camera.take_photo(file_name)
        print("New photo has been taken")
        counter += 1
        time.sleep(5)
except KeyboardInterrupt:
    print("End")
    
#camera.capture_sequence("/home/pi/camera/activity_10/image.jpg", num_images=10, interval=5)
