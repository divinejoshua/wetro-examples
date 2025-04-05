from wetro import Wetrocloud
from decouple import config

client = Wetrocloud(api_key=config("WETROCLOUD_API_KEY"))

# Access modules
rag = client.rag

# Set or create a collection
rag.collection.get_or_create_collection_id("my_unique_x_yt")

# Insert a youtube resource
insert_response = rag.collection.insert(
    resource="https://www.youtube.com/watch?v=66ApiDp-nV8", 
    type="youtube",)

# Query the collection
query_response = rag.collection.query(
    request_query="What are the key points in this video?",
    stream=True,
)

# Process streaming response
for chunk in query_response:
    print(chunk.response, end="")

