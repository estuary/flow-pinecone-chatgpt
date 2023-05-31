import os
import openai
import pinecone

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "OPENAI_API_KEY"
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") or "PINECONE_API_KEY"
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT") or "PINECONE_ENVIRONMENT"

model_name = "text-embedding-ada-002"

index_name = "flow-index"  # Replace with your index name
namespace = "flow-docs"  # Replace with your namespace

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
pinecone.whoami()
index = pinecone.Index(index_name)
openai.Engine.list()

# Enter your query here.
query = "What modes does Estuary Flow support for shuffling documents as part of a derivation?"

query_embedding = openai.Embedding.create(input=[query], engine=model_name)
embedding_value = query_embedding["data"][0]["embedding"]

res = index.query(embedding_value, top_k=3, include_metadata=True, namespace=namespace)
for match in res["matches"]:
    print(match["metadata"]["input"])
    print("----")
