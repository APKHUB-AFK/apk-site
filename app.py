from flask import Flask, render_template_string

app = Flask(__name__)

apps = [
    {
        "name": "F-Droid",
        "image": "https://f-droid.org/repo/icons-640/org.fdroid.fdroid.png",
        "link": "https://drive.google.com/uc?export=download&id=1uN5VEs9SV_oHuVXt5r6hi-12DKibvsvr",
        "size": "11 MB"
    }
]

HTML = """

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
    font-family:Arial,sans-serif;
    color:white;
}

.header{
    text-align:center;
    padding:40px 20px;
}

.header h1{
    font-size:42px;
    color:#00ff99;
    margin-bottom:10px;
}

.header p{
    color:gray;
    font-size:15px;
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

{% for app in apps %}

<div class="card">

<img src="{{ app.image }}">

<div class="info">

<h2>{{ app.name }}</h2>

<p class="size">{{ app.size }}</p>

<a class="btn" href="{{ app.link }}">
Download APK
</a>

</div>

</div>

{% endfor %}

</div>

<div class="footer">
Made using Flask + Render + Google Drive 😭🔥
</div>

</body>
</html>

"""

@app.route("/")
def home():
    return render_template_string(HTML, apps=apps)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
