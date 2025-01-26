import os
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer

MODEL_PATH = "C:/Users/domin/PycharmProjects/AppliedRobotics/vosk-model-small-en-us-0.15/vosk-model-small-en-us-0.15"

if not os.path.exists(MODEL_PATH):
    print("Please download the Vosk model and specify the correct path.")
    exit(1)

def recognize_speech_offline():
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, 16000)
    audio_queue = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(f"Audio error: {status}", flush=True)
        audio_queue.put(bytes(indata))

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening... Speak into the microphone.")
        while True:
            data = audio_queue.get()
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print("Recognized:", result)

                # Check "hit" or "stand"
                if "hit" in result.lower():
                    print("You said: HIT")
                    return "hit"
                elif "stand" in result.lower():
                    print("You said: STAND")
                    return "stand"
                elif "it" in result.lower():
                    print("You said: IT")
                    return "hit"

if __name__ == "__main__":
    try:
        result = recognize_speech_offline()
        print(f"Detected command: {result}")
    except KeyboardInterrupt:
        print("\nSpeech recognition stopped.")
