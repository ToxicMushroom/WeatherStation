int analog = 3;
float a = 1.60;

void setup() {
  pinMode(analog, INPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(analog);
  float voltage = sensorValue * (5.0 / 1023.0);
  float speed = a * voltage;
  Serial.println(voltage);
}