
from google import genai

client = genai.Client(api_key="")  # read API key from GOOGLE_API_KEY
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Quantas cidades existem na baixada santista, litoral do estado de são paulo?"
)

print(response.text)