from flask import Flask, render_template_string

app = Flask(__name__)

apps = [
    {
        "name": "Minecraft Premium",
        "image": "https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png",
        "link": "PASTE_GOOGLE_DRIVE_LINK_HERE"
    },
    {
        "name": "Spotify Premium",
        "image": "https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_Green.png",
        "link": "PASTE_GOOGLE_DRIVE_LINK_HERE"
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>APK HUB</title>

<style>

body{
    background:#0f0f0f;
    color:white;
    font-family:Arial;
    padding:20px;
}

h1{
    text-align:center;
    color:#00ff99;
}

.container{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
}

.card{
    background:#1b1b1b;
    border-radius:20px;
    padding:15px;
    text-align:center;
    box-shadow:0 0 10px rgba(0,0,0,0.5);
}

.card img{
    width:100%;
    border-radius:15px;
    height:200px;
    object-fit:cover;
}

button{
    background:#00ff99;
    border:none;
    padding:12px 20px;
    border-radius:12px;
    font-weight:bold;
    cursor:pointer;
    margin-top:10px;
}

button:hover{
    opacity:0.8;
}

</style>

</head>

<body>

<h1>🔥 APK HUB 🔥</h1>

<div class="container">

{% for app in apps %}

<div class="card">
    <img src="{{ app.image }}">
    <h2>{{ app.name }}</h2>

    <a href="{{ app.link }}">
        <button>Download APK</button>
    </a>
</div>

{% endfor %}

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, apps=apps)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
