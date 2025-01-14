from flask import Flask, request

def get_query_response(question: str) -> str:
    return "Answer: " + question

# Example usage
# app = Flask(__name__)

# Define a function for the new endpoint
def rag_endpoint_function() -> dict:
    """
    Handles HTTP requests to the RAG endpoint and returns a response.

    Expects a JSON payload containing a 'question' field.
    Returns a dictionary with the 'answer' to the question.
    """
    # Retrieve JSON payload from the request
    data = request.get_json()

    # Extract the 'question' from the payload, defaulting to an empty string if not present
    question = data.get('question', "")

    # If no question is provided, return an error message
    if not question:
        return "No question provided."

    # Obtain the answer by calling get_query_response with the provided question
    answer = get_query_response(question)

    # Return the answer within a dictionary
    return {
        "answer": answer
    }

def create_testing_rag_endpoint(app, route = '/test-rag-endpoint' , endpoint_function = rag_endpoint_function, methods=["GET"]):
    """
    Adds a new endpoint to the Flask app programmatically.

    Parameters
    Required:
    - app: Flask app object
    Optional:
    - route: The URL route (string)
    - endpoint_function: The function to be called when the route is accessed
    - methods: List of HTTP methods (default is ["GET"])
    """
    app.add_url_rule(route, view_func=endpoint_function, methods=methods)



# Dynamically add a new endpoint
# create_testing_rag_endpoint(app)

