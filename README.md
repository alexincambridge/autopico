# Cómo ejecutar scripts automaticos via CLI en Raspberry Pi Pico
usa mpremote, puedes ejecutar los scripts directamente desde tu computadora:

Cómo usar mpremote en cada sistema operativo

🔹 En Linux/macOS
Puedes conectarte a Raspberry Pi Pico con:

mpremote connect list
macOS
/dev/cu.usbmodem146401 554d45060c8ab2da 2e8a:0005 MicroPython Board in FS mode
linux
Si ves un puerto como /dev/ttyUSB0 o /dev/ttyACM0, conéctate con:
mpremote connect /dev/ttyUSB0

🔹 En Windows

Para ver los puertos disponibles, usa:

mpremote connect list
Si aparece algo como COM3, conéctate con:
mpremote connect COM3

mpremote run reboot.py
mpremote run boot_loader.py
mpremote run factory_reset.py

si prefieres copiarlos Pico y ejecutarlos desde allí:

mpremote cp reinicio.py :main.py
mpremote reboot

Cada vez que copies un script como main.py, se ejecutará automáticamente al reiniciar la Pico.
