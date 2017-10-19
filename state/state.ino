// Reads the state of a button and displays it on the screen
int buttonPin = 8;

void setup() {
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  Serial.println(digitalRead(buttonPin));
  delay(1000);
}
