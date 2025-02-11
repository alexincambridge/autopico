import serial
import time

# Configurar el puerto serie (ajusta el puerto según tu sistema)
# pico_port = "/dev/ttyUSB0"  # En Windows puede ser COM3, COM4, etc.
pico_port = "/dev/tty.usbmodem146401"  # En Windows puede ser COM3, COM4, etc.
baud_rate = 115200

# Conectarse a la Pico
ser = serial.Serial(pico_port, baud_rate, timeout=1)
time.sleep(2)  # Esperar para que la Pico inicie correctamente

# Lista de scripts a ejecutar
scripts = ["reboot.py", "pyserial.py", "factory_reset.py"]

for script in scripts :
    print(f"Ejecutando {script} en la Raspberry Pi Pico...")

    with open(script, "r") as file :
        script_content = file.read()

    ser.write(script_content.encode())  # Enviar el script a la Pico
    ser.write(b'\r\n')  # Simular presionar Enter

    time.sleep(2)  # Dar tiempo para ejecutar
    response = ser.read_all().decode()
    print(response)

ser.close()
