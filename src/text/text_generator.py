
import os
from google import genai

def main():
    api_key = "" #os.getenv('GEMINI_API_KEY')
    if api_key == False:
        print("API_KEY not found.")
        return

    while True: 
        question = input("user> ")
        client = genai.Client(api_key=api_key)  # read API key from GOOGLE_API_KEY
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=question
        )
        print("gemini> " + response.text)

if __name__ == "__main__":
    main()