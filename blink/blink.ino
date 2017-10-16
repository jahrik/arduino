/*
First program
*/
int ledPin = 13;

void setup() {
  // initialize pins as outputs
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // turn led on, sleep, off
  digitalWrite(ledPin, HIGH);
  delay(3000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
