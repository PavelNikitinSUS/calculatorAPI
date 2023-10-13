from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/dif', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 - num2
    return jsonify({'result': result})

@app.route('/mul', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2
    return jsonify({'result': result})

@app.route('/div', methods=['POST'])
def divide():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 / num2
    if num2 == 0:
        return jsonify({'error': 'Нельзя делить на ноль'})
    else:
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050)