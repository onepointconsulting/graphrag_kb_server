# GraphRag Knowledge Base Engine

Project with indexing and search functions to create the knowledge graph and the embeddings that can be used for GraphRAG.
It also provides a simple API to expose GraphRAG as an API.

# Install

```bash
# conda remove -n graphrag_kb_server --all
conda create -n graphrag_kb_server python=3.12
conda activate graphrag_kb_server
pip install poetry
poetry install
```

# Configuration

The application is configured used environment variables which you can set in a `.env` file.

And example with all variables can be found here:

[.env_local](.env_local)

The most important variables are:

```
# The Open API key
OPENAI_API_KEY

# The directory with the text files with the knowledge base.
DOCS_DIR

# The directory where the whole GraphRAG files are stored after generation
GRAPHRAG_ROOT_DIR

# The director where the vectors are stored
STORAGE_BASE_DIR
```

# Indexing

```bash
python ./graphrag_kb_server/main/index.py
```

# Searching 

```bash
python .\graphrag_kb_server\main\search.py "Why are questions so important?"
python .\graphrag_kb_server\main\search.py "Why are the main topics related to a healthy enterprise data environment?"
```

# Build context

```bash
python .\graphrag_kb_server\main\build_context.py "Why are questions so important?" 
```

# Running the server

```bash
poetry run python .\graphrag_kb_server\main\server.py
```

Check the content of the server on for example:

http://127.0.0.1:9999/about

## Example requests

http://127.0.0.1:9999/about

http://127.0.0.1:9999/context?use_context_records=true&question=What%20are%20the%20most%20important%20principles%20of%20data%20governance?

http://127.0.0.1:9999/query?format=html&question=What%20are%20the%20most%20important%20principles%20of%20data%20governance?

http://127.0.0.1:9999/context?question=What%20are%20the%20most%20important%20principles%20of%20data%20governance?

## Swagger UI

Please open to see the exposed API and its parameters:

http://127.0.0.1:9999/docs
