from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
date = datetime.today().strftime('%B %d, %Y')
#print(posts)
#print(date)

@app.route("/")
def get_home():
    return render_template('index.html', posts=posts, date=date)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/<int:id>")
def create_post(id):
    for post in posts:
        if post['id'] == id:
            return render_template("post.html", post=post, date=date)
        
@app.route("/form-entry", methods=["POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        return render_template("form-entry.html", name=name, email=email, phone=phone, 
                               message=message)
