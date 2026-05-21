from flask import Flask, request, render_template, jsonify
import os, base64
from datetime import datetime

app = Flask(__name__)
os.makedirs("images", exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json["image"]
    img = data.split(",")[1]

    name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    path = os.path.join("images", name)

    with open(path, "wb") as f:
        f.write(base64.b64decode(img))

    return jsonify({"status": "ok", "file": name})

if __name__ == "__main__":
    app.run(debug=True)