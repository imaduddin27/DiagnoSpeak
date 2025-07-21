import os
from gtts import gTTS
from elevenlabs import save
from elevenlabs import ElevenLabs
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv()

def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text, 
        lang=language, 
        slow=False)
    audioobj.save(output_filepath)
input_text = "Hello, how can I assist you today?"
#text_to_speech_with_gtts(input_text, "gtts_test.mp3")


def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    api_key = os.getenv("ELEVEN_API_KEY")
    client=  ElevenLabs(api_key=api_key)
    audio= client.text_to_speech.convert(
        text=input_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        output_format="mp3_22050_32",
        model_id="eleven_turbo_v2"
    )
    save(audio, output_filepath)
#text_to_speech_with_elevenlabs(input_text, "elevenlabs_test.mp3")


import subprocess
import platform


def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text, 
        lang=language, 
        slow=False)
    audioobj.save(output_filepath)
    os_name = platform.system()
    filepath = output_filepath
    try:
            if os_name == "Windows":  # Windows
                if filepath.lower().endswith(".mp3"):
                    wav_path = filepath.replace(".mp3", ".wav")
                    convert_mp3_to_wav(filepath, wav_path)
                    filepath = wav_path
                subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{filepath}").PlaySync();'])

            elif os_name == "Darwin":  # macOS
                subprocess.run(['afplay', output_filepath])
            
            elif os_name == "Linux":  # Linux
                try:
                    subprocess.run(['ffplay', '-nodisp', '-autoexit', filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except FileNotFoundError:
                    if filepath.lower().endswith(".mp3"):
                        wav_path = filepath.replace(".mp3", ".wav")
                        convert_mp3_to_wav(filepath, wav_path)
                        filepath = wav_path
                    subprocess.run(['aplay', filepath])
            else:
                raise OSError("Unsupported operating system")
    except Exception as e:
            print(f"An error occurred while trying to play the audio: {e}")
input_text = "Testing, this new version with autoplay."
#text_to_speech_with_gtts(input_text, "gtts_autoplay_test.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    api_key = os.getenv("ELEVEN_API_KEY")
    client=  ElevenLabs(api_key=api_key)
    audio= client.text_to_speech.convert(
        text=input_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        output_format="mp3_22050_32",
        model_id="eleven_turbo_v2"
    )
    save(audio, output_filepath)
    os_name = platform.system()
    filepath = output_filepath
    try:
        if os_name == "Windows":  # Windows
            if filepath.lower().endswith(".mp3"):
                wav_path = filepath.replace(".mp3", ".wav")
                convert_mp3_to_wav(filepath, wav_path)
                filepath = wav_path
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{filepath}").PlaySync();'])

        elif os_name == "Darwin":  # macOS
                subprocess.run(['afplay', output_filepath])
            
        elif os_name == "Linux":  # Linux
            try:
                subprocess.run(['ffplay', '-nodisp', '-autoexit', filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except FileNotFoundError:
                if filepath.lower().endswith(".mp3"):
                    wav_path = filepath.replace(".mp3", ".wav")
                    convert_mp3_to_wav(filepath, wav_path)
                    filepath = wav_path
                subprocess.run(['aplay', filepath])
            else:
                raise OSError("Unsupported operating system")
    except Exception as e:
            print(f"An error occurred while trying to play the audio: {e}")
    

#text_to_speech_with_elevenlabs(input_text, "elevenlabs_autoplay_test.mp3")