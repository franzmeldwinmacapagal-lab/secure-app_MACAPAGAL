"""
Secure Flask microservice demonstrating DevSecOps best practices.
"""
from flask import Flask, jsonify, request
import re
app = Flask(__name__)
def validate_email(email: str) -> bool:
    """Validate email format using a secure regex pattern."""
    if not email or not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
def sanitize_input(data: str) -> str:
    """Sanitize user input to prevent injection attacks."""
    if not isinstance(data, str):
        return ""
    # Remove potentially dangerous characters
    return re.sub(r'[<>&\'";\\/]', '', data)
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for container orchestration."""
    return jsonify({"status": "healthy", "service": "secure-app"}), 200
@app.route('/api/user', methods=['POST'])
def create_user():
    """Create a new user with validated and sanitized input."""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    email = data.get('email', '')
    name = data.get('name', '')
    
    if not validate_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    
    sanitized_name = sanitize_input(name)
    if not sanitized_name:
        return jsonify({"error": "Invalid name provided"}), 400
    
    return jsonify({
        "message": "User created successfully",
        "user": {
            "email": email,
            "name": sanitized_name
        }
    }), 201
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    """Retrieve user by ID with proper type validation."""
    if user_id <= 0:
        return jsonify({"error": "Invalid user ID"}), 400
    
    # Simulated user lookup
    return jsonify({
        "id": user_id,
        "email": "user@example.com",
        "name": "Demo User"
    }), 200
if __name__ == '__main__':
    # Never run with debug=True in production
    app.run(host='0.0.0.0', port=8080, debug=False)
