/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Blink
*/

  int LED = 6;
  int i = 0;
  int step = +1;
  int PD = A0;
  int val = 0;
  
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  //  i = 80;
  i = i + step*2;
  analogWrite(LED, i);
  val = analogRead(PD);
  
//  Serial.println(i);
  Serial.println(val);


// Si llega a una punta del scaneo, el step se invierte para que el scan vaya para el otro lado
  if (i >= 255){
    analogWrite(LED, 255);
    step = -1;
  }
  
// Lo mismo pero con el otro extremo
  else if (i <= 0){
    
    step = 1;
  }
  delay(100);

}
