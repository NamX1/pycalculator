import flask
from flask import render_template, request, jsonify
import re

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'})
            
        expression = data.get('expression', '')
        
        # Basic security: only allow numbers, operators, and parentheses
        if not re.match(r'^[0-9+\-*/().\s]+$', expression):
            return jsonify({'error': 'Invalid characters in expression'})
        
        # Evaluate the expression safely
        result = eval(expression)
        return jsonify({'result': result})
        
    except ZeroDivisionError:
        return jsonify({'error': 'Cannot divide by zero'})
    except Exception as e:
        return jsonify({'error': 'Invalid expression'})

if __name__ == '__main__':
    app.run(debug=True)