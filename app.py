from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# ✅ This enables CORS on all routes, for specific domain
CORS(app, supports_credentials=True, origins=["https://www.asthaguru.com"])

@app.route('/')
def home():
    return '✅ Calculator API is live. POST to /calculate with JSON'

@app.route('/calculate', methods=['POST', 'OPTIONS'])
def calculate():
    if request.method == 'OPTIONS':
        # CORS preflight request
        return '', 204

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
