from wetro import Wetrocloud
from decouple import config

client = Wetrocloud(api_key=config("WETROCLOUD_API_KEY"))


# Set or create a collection
collection_id = "my_unique_x_file_paul_g"
client.collection.get_or_create_collection_id(collection_id)


# Insert a youtube resource
insert_response = client.collection.insert_resource(
    collection_id=collection_id,
    resource="./paul_g/data.txt", 
    type="file")

# Query the collection
query_response = client.collection.query_collection(
    collection_id=collection_id,
    request_query="What did the author do growing up?",
    stream=True,
)

# Process streaming response
for chunk in query_response:
    print(chunk.response, end="")

