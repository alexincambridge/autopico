import time
from machine import Pin, PWM

# Definir clase Servo directamente
class Servo:
    def __init__(self, pin_id):
        self.pwm = PWM(Pin(pin_id))
        self.pwm.freq(50)  # Frecuencia típica para servos (50 Hz)
        self.angle = 0     # Guarda el ángulo actual simulado

    def write(self, angle):
        min_us = 500
        max_us = 2500
        pulse_width = min_us + (angle / 180) * (max_us - min_us)
        duty = int(pulse_width * 65535 / 20000)  # Convertir a duty de 16 bits
        self.pwm.duty_u16(duty)
        self.angle = angle  # Guarda el ángulo para simular "read"

    def read(self):
        return self.angle  # Devuelve el último ángulo registrado

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
    servo.write(target_position)  # Asegurar que llega a la posición exacta

# Ejecutar secuencia de reinicio
print("Ejecutando 'Reinicio': Presionando Power y Vol Down por 10 segundos...")
move_servo_slowly(power, 40)
time.sleep(0.5)
move_servo_slowly(vol_down, 0)
time.sleep(0.5)
move_servo_slowly(power, 0)
move_servo_slowly(vol_down, 0)
print("Reinicio completo.")
