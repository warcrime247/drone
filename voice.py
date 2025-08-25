import speech_recognition as sr
import time

#Simplified drone control class for demonstration
class Drone:
    def takeoff(self):
        print("Drone is taking off!")
        # Add actual takeoff code here
        
    def land(self):
        print("Drone is landing!")
        
    def move_forward(self):
        print("Drone moving forward")
        
    def move_backward(self):
        print("Drone moving backward")
        
    def turn_left(self):
        print("Drone turning left")
        
    def turn_right(self):
        print("Drone turning right")
        
    def hover(self):
        print("Drone hovering")

recognizer = sr.Recognizer()
drone = Drone()

def listen_command():
    with sr.Microphone() as source:
        print("Say a command for the drone:")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results from the service.")
        return None

def execute_command(command):
    if not command:
        return
    
    if 'take off' in command or 'takeoff' in command:
        drone.takeoff()
    elif 'land' in command:
        drone.land()
    elif 'forward' in command:
        drone.move_forward()
    elif 'backward' in command:
        drone.move_backward()
    elif 'left' in command:
        drone.turn_left()
    elif 'right' in command:
        drone.turn_right()
    elif 'hover' in command or 'stop' in command:
        drone.hover()
    else:
        print("Command not recognized. Try again!")

def main():
    print("Voice-controlled drone system started. Say 'take off', 'land', or directions.")
    try:
        while True:
            command = listen_command()
            execute_command(command)
            time.sleep(1)  # Pause between commands
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!")

if __name__ == "__main__":
    main()
