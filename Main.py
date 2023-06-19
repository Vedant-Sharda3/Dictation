from speech_text import convert_wav_to_text
from Audio_Recorder import record_audio

duration = 6  # Duration in seconds
filename = "recorded_audio.wav"
record_audio(duration, filename)
print(f"Audio recorded for {duration} seconds and saved as {filename}")

wav_file_path = "recorded_audio.wav"
result = convert_wav_to_text(wav_file_path)
print(result)