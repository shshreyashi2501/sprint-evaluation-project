from flask import Flask

app = Flask(__name__)

# ❌ intentionally vulnerable secret (for SAST demo)
#API_KEY = "hardcoded-secret-123"

@app.route("/")
def home():
    return "DevSecOps CI/CD Pipeline Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)