#include <SoftwareSerial.h>
#include "VoiceRecognitionV3.h"

// RX and TX pins for the Voice Recognition Module
SoftwareSerial mySerial(2, 3);

// Initialize the Voice Recognition module
VR myVR(mySerial);

uint8_t records[7]; // save record
uint8_t buf[64];

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  
  if (myVR.begin()) {
    Serial.println("VR Module ready.");
  } else {
    Serial.println("VR Module not detected.");
    while(1);
  }
  
  // Add voice commands previously trained on the module

  // Example record IDs you’ve trained:
  // 0: Take off
  // 1: Land
  // 2: Move forward
  // 3: Move backward
  // 4: Turn left
  // 5: Turn right
  // 6: Hover

}

void loop() {
  int ret = myVR.recognize(buf, 50);
  
  if (ret > 0) {
    uint8_t command = buf[1];
    Serial.print("Command: ");
    Serial.println(command);
    
    switch (command) {
      case 0: takeOff(); break;
      case 1: land(); break;
      case 2: moveForward(); break;
      case 3: moveBackward(); break;
      case 4: turnLeft(); break;
      case 5: turnRight(); break;
      case 6: hover(); break;
      default: Serial.println("Unknown command"); break;
    }
  }
}

void takeOff() {
  Serial.println("Taking off...");
  // Add drone motor control for takeoff
}

void land() {
  Serial.println("Landing...");
  // Add motor control to safely land
}

void moveForward() {
  Serial.println("Moving forward...");
  // Add motor control for forward movement
}

void moveBackward() {
  Serial.println("Moving backward...");
  // Add motor control for backward
}

void turnLeft() {
  Serial.println("Turning left...");
  // Add motor control to rotate left
}

void turnRight() {
  Serial.println("Turning right...");
  // Add motor control to rotate right
}

void hover() {
  Serial.println("Hovering...");
  // Add stabilization motor control
}
