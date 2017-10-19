//www.elegoo.com
//2016.12.9

#include <SimpleDHT.h>

// for DHT11, 
//      VCC: 5V or 3V
//      GND: GND
//      DATA: 2
int pinDHT11 = 2;
SimpleDHT11 dht11;

void setup() {
  Serial.begin(9600);
}

void loop() {
  byte temperature = 0;
  byte humidity = 0;
  byte data[40] = {0};
  if (dht11.read(pinDHT11, &temperature, &humidity, data)) {
    return;
  }
  Serial.print("{\"temp\":\""); Serial.print((int)temperature);
  Serial.print("\",\"humid\":\""); Serial.print((int)humidity);
  Serial.println("\"}");
  delay(1000);
}
