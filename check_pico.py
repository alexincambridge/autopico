import os
import sys
import serial.tools.list_ports
import subprocess

def check_pico():
    """
    Verifica si la Raspberry Pi Pico está conectada al sistema.
    """
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "Pico" in port.description or "RP2" in port.description:
            print(f"✅ Raspberry Pi Pico detectada en {port.device}")
            return True
    print("❌ Raspberry Pi Pico NO detectada.")
    return False

def install_requirements():
    """
    Instala los paquetes de requirements.txt si no están ya instalados.
    """
    if not os.path.exists("requirements.txt"):
        print("⚠️ No se encontró el archivo requirements.txt.")
        return

    print("📦 Instalando paquetes desde requirements.txt...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Instalación de dependencias completada.")
    except subprocess.CalledProcessError:
        print("❌ Error al instalar los paquetes.")

if __name__ == "__main__":
    if not check_pico():
        install_requirements()
