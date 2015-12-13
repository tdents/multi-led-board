#define ch1 5
#define ch2 6
#define ch3 7
#define ch4 8
#define ch5 9
#define ch6 10


long previousMillis = 0;         // hold last millis value
long interval = 200;           // time intervel to provide delay for led function
int ledState = LOW;
int channels[] = {0, ch1, ch2, ch3, ch4, ch5, ch6 };
int states[] = { 0, 0, 0, 0, 0, 0, 0};

void setup() {
 Serial.begin(9600);
 pinMode(ch1, OUTPUT); 
 pinMode(ch2, OUTPUT);
 pinMode(ch3, OUTPUT); 
 pinMode(ch4, OUTPUT);
 pinMode(ch5, OUTPUT); 
 pinMode(ch6, OUTPUT);
 digitalWrite(ch1, LOW);
 digitalWrite(ch2, LOW);
 digitalWrite(ch3, LOW);
 digitalWrite(ch4, LOW);
 digitalWrite(ch5, LOW);
 digitalWrite(ch6, LOW);

}

void loop() {
unsigned long currentMillis = millis(); // saving current millis() value to a variable
if(currentMillis - previousMillis > interval) {
    previousMillis = currentMillis;
    //channel 1
    if (states[1] == 1) { 
      if (digitalRead(ch1) == HIGH) {
        digitalWrite(ch1, LOW);
      }
      else digitalWrite(ch1, HIGH);
    }
    //channel 2
    if (states[2] == 1) { 
      if (digitalRead(ch2) == HIGH) {
        digitalWrite(ch2, LOW);
      }
      else digitalWrite(ch2, HIGH);
    }
    //channel 3
    if (states[3] == 1) { 
      if (digitalRead(ch3) == HIGH) {
        digitalWrite(ch3, LOW);
      }
      else digitalWrite(ch3, HIGH);
    }
    //channel 4
    if (states[4] == 1) { 
      if (digitalRead(ch4) == HIGH) {
        digitalWrite(ch4, LOW);
      }
      else digitalWrite(ch4, HIGH);
    }
    //channel 5    
    if (states[5] == 1) { 
      if (digitalRead(ch5) == HIGH) {
        digitalWrite(ch5, LOW);
      }
      else digitalWrite(ch5, HIGH);
    }
    //channel 6
    if (states[6] == 1) { 
      if (digitalRead(ch6) == HIGH) {
        digitalWrite(ch6, LOW);
      }
      else digitalWrite(ch6, HIGH);
    }
    
}

while (Serial.available() > 0) {

  int channel = Serial.parseInt(); 
  int state = Serial.parseInt(); 

  if (Serial.read() == '\n') {
  channel = constrain(channel, 1, 6);
  state = constrain(state, 0, 1);
  digitalWrite(channels[channel], state);
  // print the three numbers in one string as hexadecimal:
  states[channel] = state;
  digitalWrite(ch1, LOW);
  digitalWrite(ch2, LOW);
  digitalWrite(ch3, LOW);
  digitalWrite(ch4, LOW);
  digitalWrite(ch5, LOW);
  digitalWrite(ch6, LOW);

  Serial.print("Channel ");
  Serial.print(channel);
  Serial.print(", state:");
  Serial.println(state);
  }
 }
}
