# Control an Output Device with Firebase

These project consists in controling an output device (led, relay, etc...) using firebase so it can be controled over the internet.

## How does it work

Firstly we have a simple webapp  with 2 buttons which update the value of the LED in the database.
Then we have a python script in a infinite loop to check for the state of LED, and to send it to the controller.

## How to use

1. Need to have a firebase account - firebase.google.com
2. Create an RealTime Database
3. Download or Clone this repo.
4. Need to install the requirements.txt - python3 -m pip install -r requirements.txt
5. Change placeholders in website/app.js and server-side-control/run.py for your api data
6. Change the port to the port of your device in server-side-control/run.py


### How it can be improved

Even though functional it's not the most efficent project, it has some features that can be upgraded, to name a few:
1. Instead of always comunicating with the controller at every check, only comunicate when the firebase LED status change.
2. Create a filed in the database with the feedback - These field would be updated after the arduino INPUT actually updates. The button would only toggle after the Feedback matches the current status.


Project by: @rafawastaken
