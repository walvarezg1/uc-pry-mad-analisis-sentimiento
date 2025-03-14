import pandas as pd

import speech_recognition as sr
from pydub import AudioSegment

import shutil
import tempfile
import yt_dlp
import time

def load_excel(path):
    try:
        df = pd.read_excel(path)
        return df
    except Exception as e:
        print(f"Error: {e}")

def export_excel(df, path):
    try:
        df.to_excel(path, index=False)
    except Exception as e:
        print(f"Error: {e}")

def clean_text(text: str):
    text = text.replace('\t','').replace('\n','')
    text = text.replace('á','a').replace('Á','A')
    text = text.replace('é','e').replace('É','E')
    text = text.replace('í','i').replace('Í','I')
    text = text.replace('ó','o').replace('Ó','O')
    text = text.replace('ú','u').replace('Ú','U')
    return text

def extraer_texto_de_audio(audio_path):
  '''
    Extraer el texto del audio

    Parámetros:
    audio_path: Ruta del archivo de audio

    Retorna:
    data: Diccionario con los datos del audio
  '''
  try:
    reconocedor = sr.Recognizer() # Libreria speech recognition
    audio = AudioSegment.from_wav(audio_path) # Libreria Pydup
    text = ''
    for i in range(0, len(audio), 60000): # Empezando en el ms 0 hasta el ms final del audio dando saltos de a 60 segundos
      fragmento = audio[i:i+60000]
      fragmento.export('temp.wav', format='wav')

      with sr.AudioFile('temp.wav') as fuente:
        audio_data = reconocedor.record(fuente)
        text_chunk = reconocedor.recognize_google(audio_data, language='es-ES')
        text += text_chunk + ' '

    text = clean_text(text)

    #print(f'Archivo {audio_path} procesado!!')
    return text
  except Exception as e:
    return print(f'Archivo {audio_path} con error: ', e)
  
def descargar_audio(url, COOKIES_FILE_PATH):
  # Crear una copia temporal del archivo de cookies
  temp_cookies = tempfile.NamedTemporaryFile(delete=False)
  shutil.copy(COOKIES_FILE_PATH, temp_cookies.name)

  ydl_opts = {
    "quiet": True,
    'geo_bypass': True,
    'format': 'bestaudio/best',
    'outtmpl': 'audio',
    'cookiefile': temp_cookies.name,
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'wav',
      'preferredquality': '192',
    }]
  }
  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
    #print('Descarga completada')
  except Exception as e:
    print(f'Ocurrió un error: {e}')

def get_lyrics(url):
  time.sleep(2)
  descargar_audio(url)
  audio_path = 'audio.wav'
  text = extraer_texto_de_audio(audio_path)
  return text