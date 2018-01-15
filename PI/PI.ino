#include <RotaryEncoder.h>

RotaryEncoder encoder_e(A0, A1);
RotaryEncoder encoder_d(A2, A3);
int pos_nova = 0;
int k = 0;
bool up = 1;
String s;
int sum = 0;
void setup() {
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (k == 100) up = 0;
  if (k == 1) up = 1;
  //static int pos = 0;
  encoder_e.tick();
  int pos_e = encoder_e.getPosition();
  encoder_d.tick();
  int pos_d = encoder_d.getPosition();
  /*
    if (pos != pos_nova) {
    Serial.print(pos_nova);
    Serial.println();
    pos = pos_nova;
    }
  */
  int a = analogRead(A13);
  int b = analogRead(A12);
  int c = analogRead(A11);
  int d = analogRead(A10);
  int e = analogRead(A9);
  int f = analogRead(A8);
  int g = analogRead(A7);
  int h = analogRead(A6);
  int i = analogRead(A5);
  int j = analogRead(A4);

  sum = 0;
  s = String("F"+String(a)+"_"+"G"+String(b)+"_"+"T"+String(c)+"_"+
              "D"+String(d)+"_"+"R"+String(e)+"_"+"P"+String(f)+"_"+
              "f"+String(g)+"_"+"g"+String(h)+"_"+"t"+String(i)+"_"+
              "d"+String(j)+"_"+"r"+String(pos_e)+"_"+"p"+String(pos_d)+"*");
  for (int j = 0; j < s.length() - 1; j++) sum += int(s.charAt(j));
  s = String(s + String(sum));
  if (Serial.available() > 0) {
    Serial.println(s);
    Serial.read();
  }
  delay(10);
  if (up) k++;
  else k--;
}
