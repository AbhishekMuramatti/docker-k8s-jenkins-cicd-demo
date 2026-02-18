from flask import Flask
import socket

app = Flask(__name__)

VERSION = "v2.0"

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <h2>CI/CD Kubernetes Demo</h2>
    <p>Version: {VERSION}</p>
    <p>Hostname: {hostname}</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
