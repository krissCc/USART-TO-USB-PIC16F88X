import serial

# Nombre del puerto COM (ajustar según tu configuración)
port_name = 'COM1'  # Cambiar COM1 al puerto que necesites

# Velocidad de baudios (ajustar según tu configuración)
baud_rate = 9600

try:
    # Abrir el puerto COM
    ser = serial.Serial(port_name, baud_rate)

    # Datos hexadecimales de 8 bits a enviar
    data_hex = b'\xAA\xBB\xCC\xDD'  # Ejemplo de datos hexadecimales de 8 bits

    # Escribir datos hexadecimales en el puerto COM
    ser.write(data_hex)

    print("Datos hexadecimales de 8 bits enviados correctamente.")

    # Cerrar el puerto COM
    ser.close()

except serial.SerialException as e:
    print("Error: No se pudo abrir el puerto COM. Asegúrate de que esté disponible y no esté siendo utilizado por otro programa.")
    print(e)
