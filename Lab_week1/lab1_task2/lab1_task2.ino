// -------------------------------------------
//  Poject: Lab1_task2
//  Group: G
//  Students: Rob Bieman, Mike Nieuweboer
//  Date: 8 juni 2023
//  ------------------------------------------

#include <RTCZero.h>

RTCZero rtc;
String answers[] = {"LED on", "LED off", "LED blink"};
enum states {ON, OFF, BLINK};

states state;

void setup() {
  state = OFF;

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  // initialize serial port and wait for port to open:
  Serial.begin(9600);

  // wait for serial port to connect. Needed for native USB port only
  while (!Serial); 
  
  // init digital IO pins
  digitalWrite(LED_BUILTIN, LOW); 

  rtc.begin(); // initialize RTC 24H format

  rtc.attachInterrupt(blink);
}

// Loop to receive and execute commands for builtin led.
void loop() {
  if (Serial.available()) {
    String str = Serial.readString();
    str.trim();
    if (str == "On") {
      digitalWrite(LED_BUILTIN, HIGH);
      rtc.disableAlarm();
      state = ON;
      Serial.println(answers[state]);
    } else if (str == "Off") {
      digitalWrite(LED_BUILTIN, LOW);
      rtc.disableAlarm();
      state = OFF;
      Serial.println(answers[state]);
    } else if (str == "Blink") {
      blink();
      state = BLINK;
      Serial.println(answers[state]);
    } else if (str == "status") {
      Serial.println(answers[state]);
    } else {
      Serial.println("Unknown command");
    }
  }
}

// Resets the alarm and inverts the current led status.
void blink() {
  rtc.setAlarmSeconds(rtc.getSeconds());
  rtc.enableAlarm(rtc.MATCH_SS);
  digitalWrite(LED_BUILTIN, digitalRead(LED_BUILTIN) == HIGH ? LOW : HIGH);
}
