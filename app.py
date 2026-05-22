from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🔥 APK SITE LIVE (hosted on a poor innocent phone 💀)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
