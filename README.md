# Judge QnA Handler

A Python package for handling question-answering functionality with your RAG (Retrieval-Augmented Generation) capabilities.

## Installation

Install the package using pip:

```bash
pip install git+https://github.com/Umer-Ishtiaq-Q/rag_ans_retreival.git
```

## Quick Start

Here's a simple example of how to use the package:

```python
from judge_qna_handler.handler import JudgeQnaHandler
from flask import Flask

# Initialize FastAPI app
app = Flask()

# Initialize the handler
handler = JudgeQnaHandler()

# Define your query response function
def get_query_response(query: str) -> str:
    # Add your query processing logic here
    # This function should return the answer as a string
    return "Your processed answer here"

# Create the endpoint
handler.create_rag_response_endpoint(
    app=app,
    get_query_response=get_query_response
)
```

## Usage

1. First, import the necessary components:
   ```python
   from judge_qna_handler.handler import JudgeQnaHandler
   ```

2. Initialize the handler instance:
   ```python
   handler = JudgeQnaHandler()
   ```

3. Define your query response function:
   ```python
   def get_query_response(query: str) -> str:
       # Your implementation here
       return answer
   ```

4. Create the endpoint using the handler:
   ```python
   handler.create_rag_response_endpoint(
       app=app,
       get_query_response=get_query_response
   )
   ```

## API Reference

### JudgeQnaHandler

#### `create_rag_response_endpoint(app, get_query_response)`

Creates an endpoint for handling RAG-based question-answering.

Parameters:
- `app`: Flask application instance
- `get_query_response`: Function that processes the query and returns an answer

The function should have the following signature:
```python
def get_query_response(query: str) -> str
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]