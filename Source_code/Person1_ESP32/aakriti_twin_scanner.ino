#include <ESP32Servo.h>

#define TRIG 5
#define ECHO 18

Servo myServo;
int scan_id = 0;

long getDistance() {
  long total = 0;
  int count = 0;

  for (int i = 0; i < 3; i++) {
    digitalWrite(TRIG, LOW);
    delayMicroseconds(2);

    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);

    digitalWrite(TRIG, LOW);

    long duration = pulseIn(ECHO, HIGH, 30000);
    long distance = duration * 0.034 / 2;

    if (distance > 5 && distance < 300) {
      total += distance;
      count++;
    }

    delay(10);
  }

  if (count == 0) return -1;
  return total / count;
}

void setup() {
  Serial.begin(115200);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  myServo.setPeriodHertz(50);
  myServo.attach(19);
}

void loop() {
  scan_id++;

  // Forward scan
  for (int angle = 0; angle <= 180; angle += 15) {
    myServo.write(angle);
    delay(400);

    long distance = getDistance();

    Serial.print("{");
    Serial.print("\"scan_id\": "); Serial.print(scan_id);
    Serial.print(", \"timestamp\": "); Serial.print(millis());
    Serial.print(", \"angle_deg\": "); Serial.print(angle);
    Serial.print(", \"distance_cm\": "); Serial.print(distance);
    Serial.println("}");
  }

  // Reverse scan
  for (int angle = 180; angle >= 0; angle -= 15) {
    myServo.write(angle);
    delay(400);

    long distance = getDistance();

    Serial.print("{");
    Serial.print("\"scan_id\": "); Serial.print(scan_id);
    Serial.print(", \"timestamp\": "); Serial.print(millis());
    Serial.print(", \"angle_deg\": "); Serial.print(angle);
    Serial.print(", \"distance_cm\": "); Serial.print(distance);
    Serial.println("}");
  }
}
