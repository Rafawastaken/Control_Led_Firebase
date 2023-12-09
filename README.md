# Firebase-Controlled Output Device

This project enables the remote control of an output device, such as an LED or relay, utilizing Firebase for internet-based control.

## How It Works

The system comprises a straightforward web application with two buttons that update the LED value in the Firebase database. Additionally, there's a Python script running in an infinite loop to monitor the LED state and transmit it to the controller.

## Usage

1. Create a Firebase account at [firebase.google.com](https://firebase.google.com).
2. Establish a RealTime Database within Firebase.
3. Download or clone this repository.
4. Install the required dependencies using the command: `python3 -m pip install -r requirements.txt`
5. Update the placeholders in `website/app.js` and `server-side-control/run.py` with your Firebase API data.
6. Adjust the port in `server-side-control/run.py` to match your device's port.

## Potential Improvements

While the project is functional, there are opportunities for enhancement, including:

1. Implementing communication with the controller only when the Firebase LED status changes, instead of every check.
2. Introducing a database field for feedback, updating it only after the Arduino INPUT changes. The button would toggle only when the feedback matches the current status.

**Project by: @rafawastaken**
