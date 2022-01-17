import pyrebase
import serial
from time import sleep


def get_status():
    firebase_config = {
        # Replace with firebase api
    }

    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()

    # There may be other ways to access data from firebase other than this:
    status = db.child().get().val().get("LED").get("LED")

    return status


def comArduino(arduino, status):
    if status == "ON":
        status = "1"
        arduino.write(bytes(status, 'utf-8'))
        sleep(.05)
    else:
        status = "0"
        arduino.write(bytes(status, 'utf-8'))
        sleep(.05)


def main():
    arduino = serial.Serial(port="COM3", baudrate=115200, timeout=.1)
    print("Running...")
    while True:
        status = get_status()
        comArduino(arduino, status)


if __name__ == '__main__':
    main()

__author__ = "rafawastaken"
