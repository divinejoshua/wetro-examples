from wetro import Wetrocloud
from decouple import config

client = Wetrocloud(api_key=config("WETROCLOUD_API_KEY"))
tools_client = client.tools

# Extract structured data from a website
extract_response = tools_client.extract(
    website="https://thegenzhr.substack.com/p/thriving-in-the-workplace-as-an-introvert",
    json_schema={"name_of_sponsor": "<name>", "about_sponsor": "<string>"}
)
print(extract_response)
print(type(extract_response.response))