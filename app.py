from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Simple mock check
    if username == "admin" and password == "password123":
        logging.info(f"SUCCESS login for user: {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        logging.warning(f"FAILED login attempt for user: {username}")
        return jsonify({"message": "Login failed"}), 401

if __name__ == "__main__":
    app.run()
