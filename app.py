from flask import Flask, render_template, request
import json, random
from pathlib import Path
app = Flask(__name__)
PHRASES = json.loads(Path(__file__).with_name("phrases.json").read_text(encoding="utf-8"))
@app.route("/", methods=["GET", "POST"])
def index():
    categories = list(PHRASES.keys())
    category = request.form.get("category", categories[0])
    if category not in PHRASES: category = categories[0]
    phrase = "Choisis une catégorie et clique sur Générer 🔥"
    if request.method == "POST": phrase = random.choice(PHRASES[category])
    return render_template("index.html", categories=PHRASES, category=category, phrase=phrase)
if __name__ == "__main__": app.run(debug=True)
PHRASES = json.loads(
    Path(__file__).with_name("phrases.json").read_text(encoding="utf-8")
)
