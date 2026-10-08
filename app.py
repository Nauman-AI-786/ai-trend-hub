import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tools.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model (Table structure)
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(200), nullable=False)

# Database tables create karna aur initial data dalna
with app.app_context():
    db.create_all()
    if Tool.query.count() == 0:
        initial_tools = [
            Tool(name="ChatGPT", category="Text & Coding", desc="Dunya ka sab se mashhoor AI assistant jo har sawal ka jawab deta hai.", url="https://chatgpt.com"),
            Tool(name="Midjourney", category="Image Generation", desc="Behtareen realistic tasveerein banane ke liye AI tool.", url="https://midjourney.com"),
            Tool(name="Notion AI", category="Productivity", desc="Notes aur writing ko automate karne ke liye workspace.", url="https://www.notion.so")
        ]
        db.session.add_all(initial_tools)
        db.session.commit()

@app.route("/")
def home():
    tools = Tool.query.all()
    return render_template("index.html", tools=tools)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=["GET", "POST"])
def add_tool():
    if request.method == "POST":
        name = request.form.get("name")
        category = request.form.get("category")
        desc = request.form.get("desc")
        url = request.form.get("url")
        
        if name and category and desc and url:
            new_tool = Tool(name=name, category=category, desc=desc, url=url)
            db.session.add(new_tool)
            db.session.commit()
        return redirect(url_for("home"))
        
    return render_template("add.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)