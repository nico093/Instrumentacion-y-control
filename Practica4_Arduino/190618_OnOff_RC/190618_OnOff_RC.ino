
int sensorPin = A0;    // select the input pin for the potentiometer
int outPin = 3;      // select the pin for the LED
int sensorValue = 10;  // variable to store the value coming from the sensor
int i = 1;
double Read = 0.0;
double Limit = 3.0;
double LimitDown = Limit;
double LimitUp = Limit;
bool kill = false;

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(outPin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(outPin, HIGH);
}

void loop() {
// si el bool kill es true, apaga la salida del arduino para que el capacitor se descargue
if(kill){
  digitalWrite(outPin, LOW);
}

if(not kill){
  Read = analogRead(sensorPin);
  Serial.println(Read);
  
  if(Read<(LimitDown*(1023.0/5.0))) {
  digitalWrite(outPin, HIGH);  
  }
  
  if(Read>=(LimitUp*(1023.0/5.0))) {
  digitalWrite(outPin, LOW);  
  }
  delay(1000);

}
}
