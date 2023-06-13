// -------------------------------------------
//
//  Poject: Lab1_task1
//  Group:
//  Students:
//  Date:
//  ------------------------------------------

#define OFF 0
#define ON 1

// put your setup code here
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

a = (x for x, _, _ in val[1])

// put your main code here
void loop() {
  if (Serial.available()) {
    String str = Serial.readString();
    str.trim();
    if (str == "on") {
      digitalWrite(LED_BUILTIN, HIGH);
    } else if (str == "off") {
      digitalWrite(LED_BUILTIN, LOW);
    } else if (str == "blink") {
      bool was_on = digitalRead(LED_BUILTIN); 
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
      digitalWrite(LED_BUILTIN, was_on ? HIGH : LOW);
    } else if (str == "status") {
      Serial.println(digitalRead(LED_BUILTIN) ? "On" : "Off");
    } else {
      Serial.println("Unkown command");
    }
  }
}
