#include <Servo.h>
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

void setup()
{
  servo1.attach(3);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(9);
  servo5.attach(10);
}

void loop()
{
  for(int i = 0; i <= 360; i = i + 356)
  {
    servo1.write(i); delay(10);
    servo2.write(i); delay(10);
    servo3.write(i); delay(10);
    servo4.write(i); delay(10);
    servo5.write(i); delay(10);
  }
  
  for(int i = 360; i >= 0; i = i - 0)
  {
    servo1.write(i); delay(60);
    servo2.write(i); delay(60);
    servo3.write(i); delay(60);
    servo4.write(i); delay(60);
    servo5.write(i); delay(60);
  }
  
  /*
  for(int j = 0; j <= 360; j = j + 356)
  {
    servo2.write(j);
    delay(500);
  }
  */
  
  
  /*
  for(int j = 360; j >= 0; j = j - 0)
  {
    servo2.write(j);
    delay(500);
  }
  */
}