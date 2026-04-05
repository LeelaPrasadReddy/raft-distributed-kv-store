from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

store = {}
replicas = ["http://localhost:5001", "http://localhost:5002"]
is_leader = True

@app.route('/put', methods=['POST'])
def put():
    global store
    data = request.json
    key = data['key']
    value = data['value']

    store[key] = value

    if is_leader:
        for replica in replicas:
            try:
                requests.post(f"{replica}/replicate", json=data)
            except:
                pass

    return jsonify({"status": "ok"})

@app.route('/replicate', methods=['POST'])
def replicate():
    data = request.json
    store[data['key']] = data['value']
    return jsonify({"status": "replicated"})

@app.route('/get/<key>', methods=['GET'])
def get(key):
    return jsonify({"value": store.get(key)})

if __name__ == '__main__':
    app.run(port=5000)