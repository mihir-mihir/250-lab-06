import grovepi
import grove_rgb_lcd as lcd
import time

potentiometer = 0
ultrasonic_ranger = 7


grovepi.pinMode(potentiometer, "INPUT")

MAX_CM = 500

# clear the display
lcd.setText("")
lcd.setRGB(0, 0, 0)

while True:
    try:
        # read value from potentiometer
        rotary_value = grovepi.analogRead(potentiometer)

        # putting the round() in here helped to stabilize the threshold value (it would go back and forth between consecutive values more without roun())
        thresh_cm = (int)(round((float)(rotary_value) / 1023 * MAX_CM)) 
        thresh_str = '{:3d}'.format(thresh_cm) + 'cm '

        dist_cm = (int)(grovepi.ultrasonicRead(ultrasonic_ranger))
        dist_str = '{:3d}'.format(dist_cm) + 'cm '

        if (dist_cm > thresh_cm):
            lcd.setText_norefresh(thresh_str + '        \n' + dist_str)
            lcd.setRGB(0, 255, 0)
        else:
            lcd.setText_norefresh(thresh_str + 'OBJ PRES\n' + dist_str)
            lcd.setRGB(255, 0, 0)

    except Exception as e:
        print("Error:{}".format(e))

    time.sleep(0.1)  # don't overload the i2c bus
