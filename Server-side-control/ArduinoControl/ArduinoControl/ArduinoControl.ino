int x;

void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(5, OUTPUT);
}

void loop()
{
  while (!Serial.available())
    ;
  x = Serial.readString().toInt();

  if (x == 1)
  {
    digitalWrite(5, HIGH);
  }

  if (x == 0)
  {
    digitalWrite(5, LOW);
  }
}
