import time
from servo import Servo

# Configurar servos
power = Servo(pin_id=0)
vol_down = Servo(pin_id=2)

def move_servo_slowly(servo, target_position, delay=0.05, step=1):
    current_position = servo.read()
    while abs(current_position - target_position) > step:
        if current_position < target_position:
            current_position += step
        else:
            current_position -= step
        servo.write(current_position)
        time.sleep(delay)
    servo.write(target_position)

print("Ejecutando 'Reinicio': Presionando Power y Vol Down por 10 segundos...")
move_servo_slowly(power, 40)
time.sleep(0.5)
move_servo_slowly(vol_down, 0)
time.sleep(0.5)
move_servo_slowly(power, 0)
move_servo_slowly(vol_down, 0)
print("Reinicio completo.")
