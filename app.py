from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>APK HUB</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:#0d0d0d;
    color:white;
    font-family:Arial,sans-serif;
}

.header{
    text-align:center;
    padding:40px 20px;
}

.header h1{
    font-size:45px;
    color:#00ff99;
    margin-bottom:10px;
}

.header p{
    color:gray;
    font-size:14px;
}

.container{
    display:flex;
    justify-content:center;
    align-items:center;
    padding:20px;
}

.card{
    width:320px;
    background:#1a1a1a;
    border-radius:25px;
    overflow:hidden;
    box-shadow:0 0 20px rgba(0,255,153,0.15);
    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
}

.card img{
    width:100%;
    height:220px;
    object-fit:cover;
}

.info{
    padding:20px;
    text-align:center;
}

.info h2{
    margin-bottom:10px;
}

.size{
    color:#00ff99;
    margin-bottom:20px;
}

.btn{
    display:inline-block;
    text-decoration:none;
    background:#00ff99;
    color:black;
    padding:14px 24px;
    border-radius:14px;
    font-weight:bold;
    transition:0.3s;
}

.btn:hover{
    opacity:0.8;
}

.footer{
    text-align:center;
    padding:30px;
    color:gray;
    font-size:14px;
}

</style>

</head>

<body>

<div class="header">
    <h1>🔥 APK HUB 🔥</h1>
    <p>Hosted from a phone with dangerous confidence 💀</p>
</div>

<div class="container">

<div class="card">

<img src="https://f-droid.org/repo/icons-640/org.fdroid.fdroid.png">

<div class="info">

<h2>F-Droid</h2>

<p class="size">11 MB</p>

<a class="btn"
href="https://drive.usercontent.google.com/download?id=1uN5VEs9SV_oHuVXt5r6hi-12DKibvsvr&export=download&confirm=t">

Download APK

</a>

</div>

</div>

</div>

<div class="footer">
Direct APK download working 😭🔥
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
