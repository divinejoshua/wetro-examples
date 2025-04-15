from wetro import Wetrocloud
import os

# Initialize Wetrocloud client
client = Wetrocloud(api_key=os.getenv("WETROCLOUD_API_KEY"))

# Generate text with a specific model
response = client.generate_text(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, 
        {"role": "user", "content": "Write a short poem about technology."}
    ],
    model="gpt-4.1-nano"
)
# Process streaming response
for chunk in response.response:
    print(chunk, end="")
