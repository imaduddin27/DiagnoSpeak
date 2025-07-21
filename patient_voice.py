import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """ Function to record the audio from the microphone and save it as MP3 file.
    
    Args:
        file_path (str): The path to save the recorded file.
        timeout (int): Maximum time to wait for the user to start speaking(in seconds).
        phrase_time_limit (int): Maximum time for the phrase to be recorded(in seconds).
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting the ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert audio to MP3 format
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while recording audio: {e}")
        raise
audio_file_path= "patient_voice.mp3"
#record_audio(file_path=audio_file_path)

model="whisper-large-v3-turbo"
def transcribe_with_groq(model, audio_filepath):
    client = Groq()
    audio_file = open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
        model=model,
        file=audio_file, 
        language="en")
    return transcription.text