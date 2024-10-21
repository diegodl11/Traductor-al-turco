import os
import tkinter as tk
from dotenv import load_dotenv
import speech_recognition as sr
from gtts import gTTS

import google.generativeai as genai

load_dotenv()

token = os.getenv("BARD_API_KEY")

genai.configure(api_key=token)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]



def reconocer_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
    
    try:
        texto = recognizer.recognize_google(audio, language="en-EN")
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error en la solicitud:", e)

def usar_texto():
    texto_reconocido = reconocer_audio()
    
    # Traducir el texto
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

    #con el flujo en modo false, se espera hasta que se genere la respuesta
    response = model.generate_content("Translate to turkish: "+texto_reconocido, stream=False)

    try:
        result = response.text
        # Actualiza el cuadro de texto con el texto reconocido
        texto_recibido.delete(1.0, tk.END)
        texto_recibido.insert(tk.END, texto_reconocido +" ("+result+" )")
    except Exception as e:
        print(f'{type(e).__name__}: {e}')

    #elaborar una respuesta
    
    response2 = model.generate_content("Te van a decir algo en inglés (variable TEXTO) y tú tienes que responder de manera más o menos ingeniosa. Incluye una pregunta. Añade la traducción al español. La respuesta tiene esta estructura: párrafo en turco y otro párrafo con su traducción en inglés (importante: no añadir especificaciones de qué párrafo esta en turco y cuál en inglés). TEXTO = " + texto_reconocido, stream=False)
    
    try:
        result = response2.text
        texto_respuesta.delete(1.0, tk.END)
        texto_respuesta.insert(tk.END, result)
    except Exception as e:
        print(f'{type(e).__name__}: {e}')

    # Separar el texto en párrafos
    parrafos = response2.text.split('\n')

    # Obtener el primer párrafo (si hay párrafos disponibles)
    primer_parrafo = parrafos[0] if parrafos else None

    speech = gTTS(text = primer_parrafo, lang = "tr", slow=False)
    speech.save("text.mp3")
    os.system("start text.mp3")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Reconocimiento de voz")

# Crear cuadros de texto

#ventana de respuesta
texto_respuesta = tk.Text(ventana, height=10, width=100)
texto_respuesta.pack(pady=10)

texto_recibido = tk.Text(ventana, height=10, width=100)
texto_recibido.pack(pady=10)

# Crear botón para acceder al micrófono
boton_mic = tk.Button(ventana, text="Acceder al micrófono", command=usar_texto)
boton_mic.pack(pady=10)

# Ejecutar la interfaz
ventana.mainloop()