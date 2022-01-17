import pyrebase
import serial
from time import sleep


def get_status():
    firebase_config = {
        "apiKey": "AIzaSyBIIYAufROoblUDgPahtLoWfvDNlrLAWw0",
        "authDomain": "led-control-fc3ce.firebaseapp.com",
        "databaseURL": "https://led-control-fc3ce-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "led-control-fc3ce",
        "storageBucket": "led-control-fc3ce.appspot.com",
        "messagingSenderId": "167274057880",
        "appId": "1:167274057880:web:88c680ffd66c4b2dfac0ed",
        "measurementId": "G-0JTZ7G1T52"
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
