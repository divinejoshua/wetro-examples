from wetrocloud import WetroCloud
from decouple import config

client = WetroCloud(api_key=config("WETROCLOUD_API_KEY"))

# Access modules
rag = client.rag
tools = client.tools
# Initialize RAG client

# Set or create a collection
rag.collection.get_or_create_collection_id("my_unique")

# Insert a web resource
insert_response = rag.collection.insert("https://medium.com/@wetrocloud/why-legal-tech-needs-wetrocloud-ai-rag-and-the-future-of-legal-practice-66fb38c4df09", "web")
print("Insert response: %s", insert_response)

json_schema = {"topics": "<string>", "summary": "<string>"}

# Query the collection
query_response = rag.collection.query(
    request_query="What are the key points of the article?", 
    json_schema=json_schema,
    json_schema_rules="topics:required,summary:required",
)

print("Query response: %s", query_response)
# # Process streaming response
# for chunk in query_response:
#     print(chunk.response, end="")

