from PIL import Image, ImageDraw, ImageFont
import subprocess

class Content():
    def __init__(self):
        pass

    def Image_generator(self,text):
        # Create a blank image
        image = Image.new('RGB', (400, 200), color='white')

        # Add a background image
        background_image = Image.open('background.jpg')
        image.paste(background_image, (0, 0))

        # Add text
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', 20)
        draw.text((10, 10), text, fill='black', font=font)

        # Save the image
        image.save('./temp/text_image.png')

    def video_generator(self):
        # Paths to input image and audio files
        image_path = "./temp/text_image.png"
        audio_path = "./temp/input.mp3"

        # Output video file path
        output_path = "./output/output_video.mp4"

        ffmpeg_command = [
            "C:\\bin\\ffmpeg.exe",  # Replace with the actual path to the FFmpeg executable
            "-loop", "1",
            "-i", image_path,
            "-i", audio_path,
            "-c:v", "libx264",
            "-c:a", "aac",
            "-strict", "experimental",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-t", str('3'),  # Replace with the duration of your audio
            output_path
        ]

        # Run the FFmpeg command
        subprocess.run(ffmpeg_command)