from wetro import Wetrocloud
import os

# Initialize Wetrocloud client
client = Wetrocloud(api_key=os.getenv("WETROCLOUD_API_KEY"))

# Extract structured data from a website
extract_response = client.extract(
   website="https://www.forbes.com/real-time-billionaires/#7583ee253d78",
   json_schema=[{"name": "name of rich man", "networth": "amount worth"}]
)
print(extract_response)