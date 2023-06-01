from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return "",401

@app.route('/ping')
def ping():
    return 'Pong',200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)