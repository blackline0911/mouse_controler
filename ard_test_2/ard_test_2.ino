int ledPin = 9;
int analogPin = A3;
int val = 0;
String str;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin,OUTPUT);//red
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
//    val = analogRead(analogPin);
    str = ( Serial.readStringUntil('\n') );
    val = str.toInt();
    Serial.println(val);
    analogWrite(ledPin, val);
    delay(500);
    }
  
}
