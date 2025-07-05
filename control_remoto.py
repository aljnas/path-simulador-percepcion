from flask import Flask, request, jsonify, render_template_string
import json
import subprocess

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head><title>Control Remoto PATH</title></head>
<body style="font-family: sans-serif; padding: 20px;">
  <h2>🌐 Activar Escena PATH</h2>
  <form method="POST">
    <label for="escena">Selecciona una escena:</label>
    <select name="escena">
      <option value="playa">Playa</option>
      <option value="helicoptero">Helicóptero</option>
      <option value="ritual">Ritual</option>
    </select>
    <button type="submit">Activar</button>
  </form>
  {% if mensaje %}
  <p><strong>{{ mensaje }}</strong></p>
  {% endif %}
</body>
</html>
'''

CONFIGURACIONES = {
    "playa": {
        "escena": "playa",
        "luz": { "color": "#FFD580", "modo": "oscilante", "intensidad": 0.8 },
        "sonido": "olas_suaves.mp3",
        "olor": "brisa_marina",
        "textura": "toalla_arenosa"
    },
    "helicoptero": {
        "escena": "helicoptero",
        "luz": { "color": "#A0A0FF", "modo": "parpadeo", "intensidad": 0.5 },
        "sonido": "helicoptero_loop.mp3",
        "olor": "aceite_mecanico",
        "textura": "asiento_rigido"
    },
    "ritual": {
        "escena": "ritual",
        "luz": { "color": "#FFAA99", "modo": "foco", "intensidad": 0.4 },
        "sonido": "musica_suave.mp3",
        "olor": "lavanda",
        "textura": "objeto_sagrado"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        escena = request.form["escena"]
        config = CONFIGURACIONES.get(escena)
        if config:
            with open("pi/config.json", "w") as f:
                json.dump(config, f, indent=2)
            try:
                subprocess.Popen(["python3", "pi/simulador_led.py"])
                mensaje = f"Escena '{escena}' activada."
            except Exception as e:
                mensaje = f"Error al ejecutar el script: {e}"
    return render_template_string(HTML_FORM, mensaje=mensaje)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
