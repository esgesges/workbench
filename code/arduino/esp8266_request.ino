#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "s24";  // Replace with your WiFi SSID
const char* password = "12356789";  // Replace with your WiFi password
const char* serverUrl = "https://google.com";  // Replace with your server URL

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    
    Serial.print("Connecting to WiFi...");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nConnected to WiFi!");
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {  // Ensure WiFi is connected
        HTTPClient http;
        http.begin(serverUrl);  // Specify the server URL
        int httpResponseCode = http.GET();  // Send the GET request

        if (httpResponseCode > 0) {  // Check for a valid response
            String response = http.getString();
            Serial.println("Response: " + response);
        } else {
            Serial.print("Error on sending request: ");
            Serial.println(httpResponseCode);
        }
        
        http.end();  // Close connection
    } else {
        Serial.println("WiFi Disconnected!");
    }

    delay(10000);  // Wait 10 seconds before next request
}
