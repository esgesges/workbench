import serial

def read_from_serial(port, baudrate=9600, timeout=1):
    try:
        # Open the serial port
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"Connected to {port} at {baudrate} baudrate")

        while True:
            if ser.in_waiting > 0:
                # Read incoming data from the serial port
                data = ser.readline().decode('utf-8').rstrip()
                print(f"Received: {data}")

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("Interrupted by user, closing connection.")
    finally:
        if ser.is_open:
            ser.close()
            print("Serial port closed.")

# Usage: Replace 'COM3' with your actual serial port name
read_from_serial('COM3', baudrate=9600)
