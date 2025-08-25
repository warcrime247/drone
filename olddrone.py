import speech_recognition as sr
from djitellopy import Tello
import time

# Initialize Tello Drone
tello = Tello()
tello.connect()
print(f"Battery Life: {tello.get_battery()}%")

# Initialize speech recognizer
recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command received: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand audio, try again.")
    except sr.RequestError:
        print("Error with the speech recognition service.")
    return ""

def execute_command(command):
    if 'take off' in command or 'takeoff' in command:
        print("Taking off...")
        tello.takeoff()

    elif 'land' in command:
        print("Landing...")
        tello.land()

    elif 'forward' in command:
        print("Moving forward...")
        tello.move_forward(50)

    elif 'backward' in command:
        print("Moving backward...")
        tello.move_back(50)

    elif 'left' in command:
        print("Turning left...")
        tello.rotate_counter_clockwise(45)

    elif 'right' in command:
        print("Turning right...")
        tello.rotate_clockwise(45)

    elif 'up' in command:
        print("Moving up...")
        tello.move_up(30)

    elif 'down' in command:
        print("Moving down...")
        tello.move_down(30)

    elif 'flip' in command:
        print("Performing a flip!")
        tello.flip('f')  # front flip

    elif 'stop' in command or 'hover' in command:
        print("Stopping movement / hovering.")
        tello.send_control_command('stop')

    else:
        print("Unknown command, please try again.")

def main():
    print("Voice-controlled drone ready. Say commands like 'take off', 'land', 'forward', etc.")
    try:
        while True:
            command = listen_command()
            if command:
                execute_command(command)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nLanding drone and exiting program.")
        tello.land()
        tello.end()

if __name__ == "__main__":
    main()
