int analogPin = A4; // potentiometer wiper (middle terminal) connected to analog pin 3
                    // outside leads to ground and +5V
int val = 0;  // variable to store the value read
int a = 0;

void setup() {
  Serial.begin(9600);           //  setup serial
  pinMode(7, INPUT);
}

void loop() {
  //val = analogRead(analogPin);  // read the input pin
  //Serial.println(val);          // debug value
  a = digitalRead(7);
  Serial.print(a);
}
