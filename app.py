from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style='color:lime;text-align:center;margin-top:100px;'>
    APK HUB WORKING 😭🔥
    </h1>
    """

app.run(host="0.0.0.0", port=10000)
