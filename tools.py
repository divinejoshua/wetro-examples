from wetro import Wetrocloud
import os

# Initialize Wetrocloud client
client = Wetrocloud(api_key=os.getenv("WETROCLOUD_API_KEY"))

# Extract structured data from a website
extract_response = client.extract(
   website="https://yeungmancooking.com/collections/ymc-merch",
   json_schema=[{ "name": "Name of Item", "price": "Price of Item", "image": "Image of Item" }]
)
print(extract_response)