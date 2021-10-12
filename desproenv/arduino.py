import pyfirmata
import time

comPort = 'COM9'
board = pyfirmata.Arduino(comPort)

#deklarasi pin servo
#d = digital, 9 = pin 9, s = servo
servo = board.get_pin('d:9:s')
buzzer = board.get_pin(('d:5:o'))

class ValueOfLight:
    # deklarasi variable servo angle
    servo_angle: int = 0
    def ledLight(val):

        if val == 1:
            # membuat mode sweep
            buzzer.write(0)
            for angle in range(180):
                servo_angle = angle

                # gerakkan servo sesuai dengan sudut
                servo.write(servo_angle)

                # memberi delay
                time.sleep(0.05)
        elif val == 2:
            # deklarasi variable servo angle
            buzzer.write(1)
            servo.write(0)
        elif val == 3:
            # deklarasi variable servo angle
            buzzer.write(0)
            servo.write(0)

        elif val == 4:
            # deklarasi variable servo angle
            servo.write(0)
            buzzer.write(0)

        elif val == 5:
            # deklarasi variable servo angle
            servo.write(0)
            buzzer.write(0)

        else:
            # deklarasi variable servo angle
            servo.write(0)
            buzzer.write(0)
