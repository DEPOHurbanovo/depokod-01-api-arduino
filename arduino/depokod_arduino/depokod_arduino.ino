/*
  Depokod arduino example
  blink led twice after receiver something from serial 
*/

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  if(Serial.available() > 0) {
    int character = Serial.read();
    
    digitalWrite(LED_BUILTIN, HIGH);
    delay(200);
    digitalWrite(LED_BUILTIN, LOW);
    delay(200);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(200); 
    digitalWrite(LED_BUILTIN, LOW);
  }
}
