# flow-pinecone-chatgpt
Example scripts for querying ChatGPT using retrieval augmentation with a Pinecone database populated by a Flow materialization.

To use these scripts, set the following environment variables to enable authenticating with your Pinecone database and OpenAI:

- `OPENAI_API_KEY`
- `PINECONE_API_KEY`
- `PINECONE_ENVIRONMENT`

The scripts can be edited directly to set your Pinecone index name, namespace, and the query you want to run.

You can run them with `poetry` like so:
```
poetry run python retrieve.py
```