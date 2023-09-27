from gtts import gTTS
from pydub import AudioSegment

class Audio():
    def __init__(self):
        pass

    def text_to_speech(self, text):
        output_file=".\\temp\\input.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(output_file)
        print(f"Text converted to speech and saved as {output_file}")