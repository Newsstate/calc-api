from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# ✅ Only allow requests from your domain
CORS(app, origins=["https://www.asthaguru.com"])

@app.route('/')
def home():
    return '✅ Calculator API is live. Send POST to /calculate with JSON: {"a": 5, "b": 3, "operation": "add"}'

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    operation = data.get('operation')

    if a is None or b is None or operation is None:
        return jsonify({'error': 'Missing a, b, or operation'}), 400

    try:
        a = float(a)
        b = float(b)

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return jsonify({'error': 'Cannot divide by zero'}), 400
            result = a / b
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid number input'}), 400
