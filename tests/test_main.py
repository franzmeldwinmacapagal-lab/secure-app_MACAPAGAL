"""
Unit tests for the secure Flask microservice.
"""
import pytest
import json
from app.main import app, validate_email, sanitize_input
@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
class TestValidateEmail:
    """Tests for email validation function."""
    
    def test_valid_email(self):
        assert validate_email("user@example.com") is True
        assert validate_email("test.user@domain.org") is True
        assert validate_email("user+tag@example.co.uk") is True
    
    def test_invalid_email(self):
        assert validate_email("invalid") is False
        assert validate_email("@example.com") is False
        assert validate_email("user@") is False
        assert validate_email("") is False
        assert validate_email(None) is False
    
    def test_email_type_validation(self):
        assert validate_email(123) is False
        assert validate_email([]) is False
class TestSanitizeInput:
    """Tests for input sanitization function."""
    
    def test_clean_input(self):
        assert sanitize_input("John Doe") == "John Doe"
        assert sanitize_input("Alice") == "Alice"
    
    def test_removes_dangerous_chars(self):
        assert sanitize_input("<script>alert('xss')</script>") == "scriptalert(xss)script"
        assert sanitize_input("'; DROP TABLE users;--") == " DROP TABLE users--"
    
    def test_non_string_input(self):
        assert sanitize_input(None) == ""
        assert sanitize_input(123) == ""
class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def test_health_returns_200(self, client):
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
class TestCreateUserEndpoint:
    """Tests for user creation endpoint."""
    
    def test_create_user_success(self, client):
        response = client.post('/api/user',
            data=json.dumps({"email": "test@example.com", "name": "Test User"}),
            content_type='application/json')
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['user']['email'] == "test@example.com"
    
    def test_create_user_invalid_email(self, client):
        response = client.post('/api/user',
            data=json.dumps({"email": "invalid", "name": "Test User"}),
            content_type='application/json')
        assert response.status_code == 400
    
    def test_create_user_no_data(self, client):
        response = client.post('/api/user',
            data=None,
            content_type='application/json')
        assert response.status_code == 400
class TestGetUserEndpoint:
    """Tests for user retrieval endpoint."""
    
    def test_get_user_success(self, client):
        response = client.get('/api/user/1')
        assert response.status_code == 200
    
    def test_get_user_invalid_id(self, client):
        response = client.get('/api/user/0')
        assert response.status_code == 400
