from flask import Flask
app = Flask(__name__)

API_KEY = "sk_test_1234567890thisshouldnotbeleaked"

@app.route('/')
def home():
    return "Hello from Dockerized Flask App!"

if __name__ == '__main__':a
    app.run(host='0.0.0.0', port=5000)
