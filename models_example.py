from wetro import Wetrocloud
import os

# Initialize RAG client
client = Wetrocloud(
    api_key=os.getenv("WETROCLOUD_API_KEY"),
)

# Create a collection
client.collection.create_collection(collection_id="my_unique_collection_id_yt")

# Insert a resource
client.collection.insert_resource(
    collection_id="my_unique_collection_id_yt",
    resource="https://www.youtube.com/watch?v=VIkphkYlkaQ",
    type="youtube"
)

# Query the collection with llama 4 model
query_response = client.collection.query_collection(
    collection_id="my_unique_collection_id_yt",
    request_query= "What are the key points of the video?",
    stream=True
)


# Print the query response
# print("Query response: %s", query_response)

# Process streaming response
for chunk in query_response:
    print(chunk.response, end="")

