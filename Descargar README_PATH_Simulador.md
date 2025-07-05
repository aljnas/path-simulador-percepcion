# 🌈 PATH Simulador de Percepción

Este proyecto permite simular estados emocionales o sensoriales usando una Raspberry Pi y una tira LED. Utiliza una interfaz web para seleccionar escenas (como una playa, un helicóptero o un ritual), y traduce esas elecciones en señales físicas: luz, sonido, olor, textura.

---

## 🧠 ¿Para qué sirve?

Transforma cualquier espacio en una **escena simbólica emocional** usando:
- Luz (tira LED)
- Sonido (mp3, ruido blanco)
- Olores (manuales o automatizados)
- Texturas físicas (objetos en tu entorno)

Ideal para: 
- Meditación guiada
- Terapia sensorial
- Rituales familiares o personales
- Educación emocional con niños

---

## ⚙️ Requisitos

- Raspberry Pi con Python 3
- Tira LED WS2812 (o compatible)
- Librerías: `rpi_ws281x`, `neopixel`
- Navegador web local (para usar la interfaz)

---

## 📁 Estructura del Proyecto

```
PATH_Simulador_Percepcion/
│
├── web/
│   └── index.html         # Interfaz web con selector de escenas
│
├── pi/
│   ├── config.json        # Escena seleccionada (generado por la web)
│   └── simulador_led.py   # Script que enciende la tira LED
```

---

## 🧪 Instrucciones Paso a Paso

### 1. Crear repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Haz clic en "New repository"
3. Nómbralo: `path-simulador-percepcion`
4. No marques ninguna opción extra (ni README, ni .gitignore)
5. Crea el repositorio

---

### 2. Subir los archivos

1. Descarga el ZIP desde este repositorio
2. Extrae todo en tu computadora
3. Arrastra y suelta los archivos a GitHub o usa Git:

```bash
git clone https://github.com/tu_usuario/path-simulador-percepcion.git
cd path-simulador-percepcion
cp -r /carpeta/del/proyecto/* .
git add .
git commit -m "Primer commit: simulador perceptual PATH"
git push
```

---

### 3. Usar en Raspberry Pi

#### a. Instalar dependencias

```bash
sudo pip install rpi_ws281x adafruit-circuitpython-neopixel
```

#### b. Ejecutar el simulador

```bash
cd pi
sudo python3 simulador_led.py
```

---

### 4. Usar la interfaz web

1. Abre el archivo `web/index.html` en cualquier navegador
2. Elige una escena (ej: "Playa")
3. Copia el JSON generado en el panel inferior
4. Guarda ese JSON como `pi/config.json` en tu Raspberry
5. Vuelve a ejecutar el script para aplicar la escena

---

## ✨ Escenas Incluidas

- `playa`: luz cálida oscilante, sonido de olas, aroma marino
- `helicoptero`: luz azul parpadeante, sonido de hélices
- `ritual`: luz tenue, música suave, símbolo emocional

---

## 📡 Extensiones futuras

- Automatizar olores con relés GPIO
- Activación por voz o botón físico
- Almacén sensorial físico (PATH Box)
- Registro de emociones antes/después de la escena

---

## 🤍 Creado con propósito por Alejandro + IA (ChatGPT)

> “La percepción es una simulación con parámetros. Si eliges bien, puedes transformar tu realidad desde la luz.”
