from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>APK HUB</title>
    </head>

    <body style="background:black;color:lime;text-align:center;padding-top:100px;font-family:Arial;">

        <h1>🔥 APK HUB 🔥</h1>

        <a href="https://drive.google.com/uc?export=download&id=1uN5VEs9SV_oHuVXt5r6hi-12DKibvsvr">

            <button style="padding:20px;font-size:20px;">
            Download F-Droid
            </button>

        </a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
