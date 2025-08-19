from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", blog_post = blog)

@app.route('/blog/<int:id>')
def get_blog(id):
    blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    filtered = blog[id-1]
    return render_template("post.html", blog_post=filtered)

if __name__ == "__main__":
    app.run(debug=True)

blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

