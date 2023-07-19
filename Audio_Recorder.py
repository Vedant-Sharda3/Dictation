import sounddevice as sd
import soundfile as sf

"""This file records audio for the specified duration and saves it as a wav file
Returns 0 if successful else -1"""
def record_audio(duration, filename):
    try:
        sample_rate = 44100
        channels = 1
        frames = int(duration * sample_rate)

        recording = sd.rec(frames, samplerate=sample_rate, channels=channels)
        sd.wait()

        # We save the recorded audio to a WAV file
        sf.write(filename, recording, sample_rate)

        return 0
    except sd.PortAudioError as e:
        print("PortAudioError:", e)
        return -1
    except Exception as e:
        print("Error:", e)
        return -1
