from audio import Audio
from content import Content

def text_to_video(self,text):
    audio=Audio()
    content=Content()

    audio.text_to_speech('Hi i am Dev Team Leader.')
    content.Image_generator("sky is blue")

    with open('text_image.png','r') as file:
        content.video_generator()