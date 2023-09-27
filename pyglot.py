from audio import Audio
from content import Content

def text_to_video(text):
    audio=Audio()
    content=Content()

    audio.text_to_speech(text)
    content.Image_generator(text)
    content.video_generator()