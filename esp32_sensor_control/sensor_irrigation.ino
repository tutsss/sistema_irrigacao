#include <DHT.h>

#define DHTPIN 21
#define DHTTYPE DHT22
#define LDR_PIN 34
#define PHOSPHORUS_PIN 12
#define POTASSIUM_PIN 14
#define RELAY_PIN 26

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(LDR_PIN, INPUT);
  pinMode(PHOSPHORUS_PIN, INPUT_PULLUP);
  pinMode(POTASSIUM_PIN, INPUT_PULLUP);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
}

void loop() {
  float humidity = dht.readHumidity();
  int ldrValue = analogRead(LDR_PIN);
  bool phosphorus = !digitalRead(PHOSPHORUS_PIN);
  bool potassium = !digitalRead(POTASSIUM_PIN);

  if (isnan(humidity)) {
    Serial.println("Falha na leitura do sensor DHT22!");
    return;
  }

  Serial.print("Umidade: ");
  Serial.print(humidity);
  Serial.print("% | pH (simulado pelo LDR): ");
  Serial.print(ldrValue);
  Serial.print(" | Fósforo: ");
  Serial.print(phosphorus ? "Presente" : "Ausente");
  Serial.print(" | Potássio: ");
  Serial.println(potassium ? "Presente" : "Ausente");

  if (humidity < 50.0 && phosphorus && potassium && ldrValue > 500) {
    digitalWrite(RELAY_PIN, HIGH);
    Serial.println("Irrigação Ativada");
  } else {
    digitalWrite(RELAY_PIN, LOW);
    Serial.println("Irrigação Desativada");
  }

  delay(2000);
}
