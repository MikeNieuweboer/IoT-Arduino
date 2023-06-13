#include <Arduino_LSM6DS3.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin() || !IMU.accelerationAvailable()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

void loop() {
  float x, y, z;
  String inp;
  while (!input_on());
  for (int i = 0; i < 30; i++) {
    long start_time = millis();
    if (input_on()) {
      i = 0;
      start_time = millis();
    }
    IMU.readAcceleration(x, y, z);
    Serial.print(x);
    Serial.print(' ');
    Serial.print(y);
    Serial.print(' ');
    Serial.println(z);
    delay(500 - millis() + start_time);
  }
  Serial.print('\n');
}

bool input_on() {
  if (Serial.available()) {
    String inp = Serial.readString();
    inp.trim();
    return inp == "On";
  }
  return false;
}
