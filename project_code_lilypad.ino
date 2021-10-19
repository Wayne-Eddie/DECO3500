#include <Adafruit_CircuitPlayground.h>
uint8_t pixe_0 = 0;
uint8_t pixe_1 = 0;
uint8_t pixe_2 = 0;
uint8_t pixe_3 = 0;
const int  buttonPin = 4;  
int buttonPushCounter = 0; 
int buttonState = 0;         
int lastButtonState = 0;  

void setup() {
  Serial.begin(9600);
  CircuitPlayground.begin();
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState != lastButtonState) { 
    buttonPushCounter++;
    CircuitPlayground.clearPixels();
    }
    
    switch(buttonPushCounter) {
    case 1:
      CircuitPlayground.setPixelColor(pixe_0++, 0xFF0000);
      if (pixe_0 == 11) {
      CircuitPlayground.clearPixels();
      pixe_0 = 0;
      }
      delay(1000);
    break;
  
    case 2:
      CircuitPlayground.setPixelColor(pixe_1++, 0x0000FF);
      if (pixe_1 == 11) {
      CircuitPlayground.clearPixels();
      pixe_1 = 0;
      }
      delay(800);
    break;

    case 3:
      CircuitPlayground.setPixelColor(pixe_2++, 0x08000);
      if (pixe_2 == 11) {
      pixe_2 = 0;
      CircuitPlayground.clearPixels();
      }
    delay(600);
    break;

    case 4:
      CircuitPlayground.setPixelColor(pixe_3++, CircuitPlayground.colorWheel(25 * pixe_3));
      if (pixe_3 == 11) {
        pixe_3 = 0;
        CircuitPlayground.clearPixels();
        }
      delay(300);
      break;
    }
}
