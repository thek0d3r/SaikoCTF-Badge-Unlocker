import os
import serial
import time


if os.geteuid() != 0:
    print("Please run this script as root")
    exit()

print("Welcome to the SaikoCTF Badge (unintended) solver")
print("Are you sure you want to solve the badge? (y/n)\nPlease note that doing this is irreversible and will forever solve your badge\n")
ak = str(input("> "))

if ak.lower() not in ['y', 'yes']:
    print("Exiting...")
    exit()

print("Solving the badge...")
print("Opening the tty connection...")
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
print("Connection opened!")
time.sleep(2)

print("Sending Ctrl+C to open the Python interpreter...")

ser.write(b'\x03')
ser.flush()

time.sleep(1)

# Open the file in write mode
with open("badge.py", "w") as output_file:
    try:
        # Read some lines to reach the interpreter prompt
        for _ in range(6):
            line = ser.readline().decode('utf-8')
            print(line, end='')  # Optional: print to console
            output_file.write(line.replace('\r\n', '\n'))  # Write to file with standardized line endings

        print("Python interpreter ready!")

        print("Sending command to print main.py...")
        python_command = b'(type("", (), {"read_main": lambda self: open("main.py").read()})()).read_main()\r'
        time.sleep(1)

        ser.reset_input_buffer()
        ser.reset_output_buffer()

        ser.write(python_command)
        ser.flush()

        # Read and write the response (contents of main.py) to the file
        while True:
            try:
                line = ser.readline()
                if line:
                    decoded_line = line.decode('utf-8')
                    print(decoded_line, end='')  # Optional: print to console
                    output_file.write(decoded_line.replace('\\r\\n', '\n').replace("\'", "'"))  # Write to file with standardized line endings
            except KeyboardInterrupt:
                break    
            
        print("You can go look around and get the flags. I will save you some time:")
        print("1. thesaikobadge")
        print("2. s14k0")
        print("3. 5aiko4wakend")
        
    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        ser.close()
