
#include <dht.h>
#include <Bridge.h>
#include <Process.h>

dht DHT;

#define DHT11_PIN 6



void setup() {
 
  Bridge.begin();
  

}

void loop() {

   int chk = DHT.read11(DHT11_PIN);
   char _buffer[10];
   char _buffer1[10];
   float n = DHT.humidity;
   float n1 = DHT.temperature;
  
   Process p;
   p.runShellCommand("sqlite3 -line /mnt/sda1/test.db 'CREATE TABLE IF NOT EXISTS Temp ( a DATETIME DEFAULT (CURRENT_DATE), b DATETIME DEFAULT (CURRENT_TIME), c INT, d INT);'");
   String string1 = "sqlite3 -line /mnt/sda1/test.db ";
   String string2 = "'INSERT INTO Temp ( c, d) VALUES (  ";
   //String string3 = "";
   //String string4 = "CURRENT_TIME";
   //String string5 = "";
   //String string6 = ", ";
   String string7 = dtostrf(n, 2, 2, _buffer);
   String string8 = ", ";
   String string9 = dtostrf(n1, 2, 2, _buffer1);
   String string10 = ");'";

   p.runShellCommand(string1+string2+string7+string8+string9+string10);
   
   delay(600000);
  
}

