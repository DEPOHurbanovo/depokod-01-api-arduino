from flask import Flask
import serial

app = Flask(__name__)

@app.route("/arduino/send/<message>")
def hello(message):
    arduino = serial.Serial("/dev/ttyACM0")
    to_write = message.encode("ascii")
    arduino.write(to_write)
    return "ok"

if __name__ == "__main__":
    app.run()