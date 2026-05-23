from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>

<head>

<title>APK HUB</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

body{
    background:#0d0d0d;
    color:white;
    font-family:Arial;
    text-align:center;
    padding:40px;
}

h1{
    color:#00ff99;
    font-size:45px;
}

.card{
    background:#1a1a1a;
    padding:20px;
    border-radius:20px;
    max-width:320px;
    margin:auto;
    margin-top:40px;
    box-shadow:0 0 20px rgba(0,255,153,0.2);
}

img{
    width:100%;
    border-radius:15px;
}

.btn{
    display:inline-block;
    margin-top:20px;
    background:#00ff99;
    color:black;
    padding:14px 25px;
    border-radius:12px;
    text-decoration:none;
    font-weight:bold;
}

</style>

</head>

<body>

<h1>🔥 APK HUB 🔥</h1>

<div class="card">

<img src="https://f-droid.org/repo/icons-640/org.fdroid.fdroid.png">

<h2>F-Droid APK</h2>

<p>11 MB</p>

<a class="btn"
href="https://drive.google.com/uc?export=download&id=1uN5VEs9SV_oHuVXt5r6hi-12DKibvsvr"
download>

Download APK

</a>

</div>

<p style="margin-top:40px;color:gray;">
Direct APK download 😭🔥
</p>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
