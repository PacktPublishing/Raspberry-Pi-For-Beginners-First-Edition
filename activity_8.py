from gpiozero import LED, MotionSensor
from signal import pause
# import time

led = LED(17)
pir = MotionSensor(4)

pir.when_motion = led.on
pir.when_no_motion = led.off
pause()

# while True:
#     time.sleep(0.01)
#     if pir.motion_detected:
#         led.on()
#     else:
#         led.off()