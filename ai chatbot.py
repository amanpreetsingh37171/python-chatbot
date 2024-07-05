import google.generativeai as genai
import os


text = "who is the founder of the sikhism?"

genai.configure(api_key="AIzaSyCA3cNfkCeDRGOj9iM-ptgRGgybkIofRrY")

generation_config = {"temperature":0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

response = model.generate_content(text)

ans = response.text
print(ans)