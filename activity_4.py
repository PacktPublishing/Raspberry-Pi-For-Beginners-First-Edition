from gpiozero import LED
import time

led = LED(17)

user_choice = int(input("Enter 0 to turn off the LED, 1 to turn it on: "))

if user_choice == 0:
    led.off()
elif user_choice == 1:
    led.on()
else:
    print("Invalid choice, must be 0 or 1")
    exit()

time.sleep(2)
print("End")
