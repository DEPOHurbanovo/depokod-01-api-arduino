from flask import Flask

from serial import Serial as serial
from serial.tools import list_ports as ports

# awesome magic hack (filter arduino outta all available ports)
arduino_port = ports.grep("VID:PID=2341:0043").next()

# initialize communication with arduino
arduino = serial(arduino_port.device)

# initialize http server
app = Flask(__name__)

@app.route("/arduino/send/<message>")
def hello(message):
	# send message
    arduino.write(message.encode("ascii"))

    return "successful"

if __name__ == "__main__":
    app.run()