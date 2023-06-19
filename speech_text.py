import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


def convert_wav_to_text(wav_file):
    audio = AudioSegment.from_wav(wav_file)

    audio_data = audio.raw_data
    sample_rate = audio.frame_rate
    sample_width = audio.sample_width

    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(audio_data, sample_rate, sample_width)
    text = recognizer.recognize_google(audio_data)

    return text
