import time
from machine import Pin, PWM

# Definir la clase Servo directamente
class Servo:
    def __init__(self, pin_id):
        self.pwm = PWM(Pin(pin_id))
        self.pwm.freq(50)  # 50 Hz es la frecuencia estándar para servos
        self.angle = 0     # Guarda el último ángulo

    def write(self, angle):
        min_us = 500
        max_us = 2500
        pulse_width = min_us + (angle / 180) * (max_us - min_us)
        duty = int(pulse_width * 65535 / 20000)  # Convertir a duty de 16 bits
        self.pwm.duty_u16(duty)
        self.angle = angle  # Almacenar el ángulo actual

    def read(self):
        return self.angle  # Devolver el último ángulo escrito (simulado)

# Configurar servos
power = Servo(pin_id=0)
vol_up = Servo(pin_id=1)

def move_servo_slowly(servo, target_position, delay=0.05, step=1):
    current_position = servo.read()
    while abs(current_position - target_position) > step:
        if current_position < target_position:
            current_position += step
        else:
            current_position -= step
        servo.write(current_position)
        time.sleep(delay)
    servo.write(target_position)  # Ajustar a posición exacta al final

# Ejecutar secuencia de Boot Loader
print("Ejecutando 'Boot Loader': Presionando Power y Vol Up por 10 segundos...")
move_servo_slowly(power, 20)
move_servo_slowly(vol_up, 20)
time.sleep(0.5)
move_servo_slowly(power, 0)
move_servo_slowly(vol_up, 0)
print("Boot Loader completo.")
