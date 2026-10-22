from fastapi.testclient import TestClient

from app import app

client = TestClient(app, raise_server_exceptions=False)

def test_hello_returns_success():
    response = client.get("/hello")
    """ The hello endpoint should respond successfully. """
    # Verify the HTTP status code.
    assert response.status_code == 200
    # Verify the expected response body.
    assert response.json() == {
        "message" : "Hello, observability!"
    }

def test_error_returns_500():
    """ The intentional error endpoint should return HTTP 500. """
    response = client.get("/error")
    # Verify the application returns an internal server error
    assert response.status_code == 500