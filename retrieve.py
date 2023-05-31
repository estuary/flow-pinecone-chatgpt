import os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or "OPENAI_API_KEY"
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") or "PINECONE_API_KEY"
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT") or "PINECONE_ENVIRONMENT"

model_name = "text-embedding-ada-002"
text_field = "input"

index_name = "flow-index"  # Replace with your index name
namespace = "flow-docs"  # Replace with your namespace name

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
embed = OpenAIEmbeddings(model=model_name, openai_api_key=OPENAI_API_KEY)
vectorstore = Pinecone(
    pinecone.Index(index_name), embed.embed_query, text_field, namespace
)
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0.0
)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# Enter your query here.
query = "What modes does Flow support for shuffling documents as part of a derivation?"
answer = qa.run(query)

print("Question: ", query)
print("----")
print("Answer: ", answer)
