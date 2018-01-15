#include <RotaryEncoder.h>

RotaryEncoder encoder_e(A0, A5);
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
  float pos_e = encoder_e.getPosition();
  encoder_d.tick();
  int pos_d = encoder_d.getPosition();
  /*
    if (pos != pos_nova) {
    Serial.print(pos_nova);
    Serial.println();
    pos = pos_nova;
    }
//  */
//
//  int a = analogRead(A2) / 10;
//  int b = analogRead(A3) %100;
  int c = analogRead(A4);
  int d = analogRead(A1);
  int e = analogRead(A6);
  int f = analogRead(A8);
  int g = analogRead(A10);
  int h = analogRead(A6);
  int i = analogRead(A7);
  int j = analogRead(A9);
  int k = analogRead(A11);
  int l = analogRead(A12);
 // int m = analogRead(A13);

  sum = 0;
  s = String("F"+String(c)+"_"+"G"+String(e)+"_"+"T"+String(d)+"_"+
              "D"+String(g)+"_"+"R"+String(int(pos_e))+"_"+"P"+String(f)+"_"+
              "f"+String(h)+"_"+"g"+String(i)+"_"+"t"+String(j)+"_"+
              "d"+String(k)+"_"+"r"+String(pos_d)+"_"+"p"+String(l)+"*");
  for(int j=0;j<s.length()-1;j++) sum+=int(s.charAt(j));
  s = String(s + String(sum));
  if (Serial.available() > 0) {
    Serial.print(s);
    Serial.read();
  }
  delay(10);
  if (up) k++;
  else k--;
}
