import keyboard
import rotatescreen
import time
screen = rotatescreen.get_primary_display()
i=1
while True:
    time.sleep(1)
    if keyboard.is_pressed('q'):
        screen.rotate_to(0)
        break
    screen.rotate_to(i*90%360)
    i+=1
