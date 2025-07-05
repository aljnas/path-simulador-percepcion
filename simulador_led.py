import json
from neopixel import *
import time

# Configuración de la tira LED
LED_COUNT = 30
LED_PIN = 18
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN)
strip.begin()

# Cargar configuración desde archivo JSON
with open('config.json', 'r') as f:
    data = json.load(f)

# Extraer color
color_hex = data['luz']['color'].lstrip('#')
r, g, b = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))

# Simular efecto básico
while True:
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(g, r, b))
    strip.show()
    time.sleep(0.1 if data['luz']['modo'] == 'oscilante' else 0.3)
