from flask import Flask

app = Flask(__name__)

@app.route('/health1')
def health():
    return "",401

@app.route('/ping1')
def ping():
    return 'Pong1',200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)