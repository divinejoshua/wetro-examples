from wetro import Wetrocloud
import os

# Initialize Wetrocloud client
client = Wetrocloud(api_key=os.getenv("WETROCLOUD_API_KEY"))

# Extract markdown data from a website
markdown_response = client.markdown_converter(
   link="https://medium.com/@AlexanderObregon/a-brief-history-of-artificial-intelligence-1656693721f9#:~:text=In%20this%20article%2C%20we%20explore,learning%20are%20breaking%20new%20ground.",
   resource_type="web",
)
print(markdown_response)

#Youtube transcript
markdown_response = client.transcript(
   link="https://www.youtube.com/watch?v=7kbQnLN2y_I&t=1164s",
   resource_type="youtube",
)
print(markdown_response)

