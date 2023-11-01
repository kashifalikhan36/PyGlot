from audio import Audio
from content import Content
from unsplash import Unsplash_images

def text_to_video(text,Unsplash_API):
    audio=Audio()
    content=Content()
    unsplash=Unsplash_images(Unsplash_API)

    #We are making Images
    k=""
    j=0
    for i in range(0,len(text)):
        if i%77==0:
            para_for_image=text[j:i]
            unsplash.get_image(para_for_image)
            j=i

    audio.text_to_speech(text)
    content.Image_generator(text)
    content.video_generator()