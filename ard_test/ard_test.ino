String str;

void setup() {
  // put your setup code here, to run once:
  pinMode(2,OUTPUT);//red
  pinMode(4,OUTPUT);//green
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
      str = Serial.readStringUntil('\n');
      Serial.println(str);
      if (str=="Red"){
        Serial.println("Red turn on");
        digitalWrite(2,1);
        delay(1000);
        digitalWrite(2,0);
        }
      if (str=="Green"){
        Serial.println("Green turn on");
        digitalWrite(4,1);
        delay(1000);
        digitalWrite(4,0);
        }
    }
  Serial.write(44);
  delay(500);
}
