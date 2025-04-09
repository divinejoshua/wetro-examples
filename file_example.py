from wetro import Wetrocloud
import os

# Initialize RAG client
client = Wetrocloud(
    api_key=os.getenv("WETROCLOUD_API_KEY"),
)

collection_id = "my_unique_collection_id_file"

# Create a collection
client.collection.create_collection(collection_id=collection_id)

# Insert a resource
client.collection.insert_resource(
    collection_id=collection_id,
    resource="./data/sample.pdf",
    type="file"
)

# Query the collection with llama 4 model
query_response = client.collection.query_collection(
    collection_id=collection_id,
    request_query= "What are the key points in this file?",
    # model="meta-llama/llama-4-scout-17b-16e-instruct",
    stream=True
)

# Print the query response
# print("Query response: %s", query_response)

# Process streaming response
for chunk in query_response:
    print(chunk.response, end="")

