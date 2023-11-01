import requests
import os
from PIl import Image

class Unsplash_images:
    def __init__(self,API_KEY):
        self.api_key = API_KEY

    def get_image(self,paragraph):
        search_query = paragraph
            # API endpoint URL
        url = f"https://api.unsplash.com/photos/random?query={search_query}&client_id={self.api_key}"
            # Make the API request
        response = requests.get(url)

            # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            image_url = data["urls"]["regular"]

                # Download the image
            response = requests.get(image_url)
            if response.status_code == 200:
                    # Save the image
                with open(f"./temp/{search_query}.jpg", "wb") as f:
                    f.write(response.content)
                print(f"Image saved as {search_query}.jpg")
            else:
                print("Failed to download image.")
        else:
            print("Failed to fetch data from the Unsplash API.")


            # Directory where your image files are located
        image_dir = './temp'

            # Get a list of image files in the directory
        image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg', '.gif'))]

            # Ensure the directory where you want to save the images exists
        output_dir = './temp'
        os.makedirs(output_dir, exist_ok=True)

            # Iterate through the image files and save them with numbered filenames
        for i, image_file in enumerate(image_files, start=1):
                # Open the image file
            with Image.open(os.path.join(image_dir, image_file)) as img:
                    # Create a numbered filename
                output_filename = f"{i:03d}.jpg"  # Change the extension to match your image format
                    # Save the image with the numbered filename in the output directory
                img.save(os.path.join(output_dir, output_filename))