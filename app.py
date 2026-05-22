from flask import Flask, request, render_template_string, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML = """
<h1>🔥 APK HUB</h1>

<h2>Upload APK</h2>

<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <button type="submit">Upload</button>
</form>

<h2>Available APKs</h2>

<ul>
{% for file in files %}
<li>
    {{ file }}
    <a href="/download/{{ file }}">
        <button>Download</button>
    </a>
</li>
{% endfor %}
</ul>
"""

@app.route("/")
def home():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML, files=files)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return "APK uploaded 😄 <br><a href='/'>Go Back</a>"

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
