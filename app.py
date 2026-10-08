import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initial AI Tools List
ai_tools = [
    {"name": "ChatGPT", "category": "Text & Coding", "desc": "Dunya ka sab se mashhoor AI assistant jo har sawal ka jawab deta hai."},
    {"name": "Midjourney", "category": "Image Generation", "desc": "Behtareen realistic tasveerein banane ke liye AI tool."},
    {"name": "Notion AI", "category": "Productivity", "desc": "Notes aur writing ko automate karne ke liye workspace."}
]

@app.route("/")
def home():
    return render_template("index.html", tools=ai_tools)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=["GET", "POST"])
def add_tool():
    if request.method == "POST":
        name = request.form.get("name")
        category = request.form.get("category")
        desc = request.form.get("desc")
        
        if name and category and desc:
            ai_tools.append({"name": name, "category": category, "desc": desc})
        return redirect(url_for("home"))
        
    return render_template("add.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)