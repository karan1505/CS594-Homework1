# Packages needed:
# Flask
# azure-cognitiveservices-vision-computervision
# python-dotenv

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

endpoint = os.getenv("AZURE_VISION_ENDPOINT")
key = os.getenv("AZURE_VISION_KEY")

credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(endpoint, credentials)

def generate_caption_and_tags(image_path_or_url):
    try:
        # If the input is a URL, use the API's URL method
        if image_path_or_url.startswith("http://") or image_path_or_url.startswith("https://"):
            description_result = client.describe_image(image_path_or_url, max_descriptions=1, language="en")
            tags_result = client.tag_image(image_path_or_url)
        else:
            with open(image_path_or_url, "rb") as image_file:
                description_result = client.describe_image_in_stream(image_file, max_descriptions=1, language="en")
                image_file.seek(0)  # Reset the file pointer for the next request
                tags_result = client.tag_image_in_stream(image_file)
        
        # Extract caption
        caption = "No caption generated"
        if description_result.captions:
            caption = description_result.captions[0].text
        
        # Extract tags
        tags = [tag.name for tag in tags_result.tags[:2]]  # Get up to 2 tags

        return caption, tags
    except Exception as e:
        return f"Error processing caption and tags: {str(e)}", []

