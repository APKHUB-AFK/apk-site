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
<html>

<head>

<title>APK HUB</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

body{
    margin:0;
    padding:0;
    background:#0d0d0d;
    color:white;
    font-family:Arial,sans-serif;
}

.header{
    text-align:center;
    padding:30px 20px;
}

.header h1{
    color:#00ff99;
    font-size:40px;
    margin-bottom:10px;
}

.header p{
    color:gray;
}

.container{
    display:flex;
    justify-content:center;
    padding:20px;
}

.card{
    background:#1a1a1a;
    width:300px;
    border-radius:25px;
    overflow:hidden;
    box-shadow:0 0 25px rgba(0,255,153,0.2);
    transition:0.3s;
}

.card:hover{
    transform:scale(1.03);
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
    margin-top:0;
}

.size{
    color:#00ff99;
    margin-bottom:20px;
}

.download-btn{
    display:inline-block;
    background:#00ff99;
    color:black;
    text-decoration:none;
    padding:14px 25px;
    border-radius:15px;
    font-weight:bold;
    transition:0.3s;
}

.download-btn:hover{
    opacity:0.8;
}

.footer{
    text-align:center;
    color:gray;
    padding:30px;
    font-size:14px;
}

</style>

</head>

<body>

<div class="header">
    <h1>🔥 APK HUB 🔥</h1>
    <p>Hosted with pure chaos engineering 💀</p>
</div>

<div class="container">

{% for app in apps %}

<div class="card">

<img src="{{ app.image }}">

<div class="info">

<h2>{{ app.name }}</h2>

<p class="size">{{ app.size }}</p>

<a class="download-btn" href="{{ app.link }}">
Download APK
</a>

</div>

</div>

{% endfor %}

</div>

<div class="footer">
Made with Flask + Render + Google Drive 😭🔥
</div>

</body>
</html>

"""

@app.route("/")
def home():
    return render_template_string(HTML, apps=apps)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
