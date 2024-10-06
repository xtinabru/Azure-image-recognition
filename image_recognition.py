import requests
from dotenv import load_dotenv
import os


load_dotenv()

subscription_key = os.getenv("SUBSCRIPTION_KEY")
endpoint = os.getenv("ENDPOINT")

analyze_url = endpoint + "vision/v3.2/analyze"

params = {
    "visualFeatures": "Categories,Description",
}

image_path = "C:/Users/Cristofer/Pictures/night.jpeg"
with open(image_path, "rb") as image:
    response = requests.post(
        analyze_url,
        headers={
            "Ocp-Apim-Subscription-Key": subscription_key,
            "Content-Type": "application/octet-stream",
        },
        params=params,
        data=image,
    )

    print(response.text)
    response.raise_for_status()
    analysis = response.json()

print("Available keys:")
for key in analysis:
    print(f"- {key}")

if "description" in analysis:
    print("What we can see in the picture:")
    for caption in analysis["description"]["captions"]:
        print(f"- {caption['text']} (confidence: {caption['confidence']:.2f})")
else:
    print("I have no idea")
