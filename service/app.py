from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return 'Service is healthy'

@app.route('/ping')
def ping():
    return 'Pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)