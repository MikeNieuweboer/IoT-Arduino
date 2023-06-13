// -------------------------------------------
//  Poject: Lab1_task1
//  Group: G
//  Students: Rob Bieman, Mike Nieuweboer
//  Date: 8 juni 2023
//  ------------------------------------------

String answers[] = {"LED off", "LED on"};
enum states {OFF = LOW, ON = HIGH};

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  // initialize serial port and wait for port to open:
  Serial.begin(9600);

  // wait for serial port to connect. Needed for native USB port only
  while (!Serial) {} 
  
  // init digital IO pins
  digitalWrite(LED_BUILTIN, LOW); 
}

// Loop to receive and execute commands for builtin led.
void loop() {
  while (!Serial.available()) {}
  String str = Serial.readString();
  str.trim();
  if (str == "On") {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println(answers[ON]);
  } else if (str == "Off") {
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println(answers[OFF]);
  } else if (str == "status") {
    Serial.println(digitalRead(LED_BUILTIN) == HIGH ? answers[ON] : answers[OFF]);
  } else {
    Serial.println("Unknown command");
  }
}
