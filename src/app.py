from flask import Flask, render_template
from urls import index_urls, genre_urls, release_urls, review_urls, ml_urls

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", index_urls=index_urls)

@app.route("/genre")
def genre():
    return render_template("genre.html", genre_urls=genre_urls)

@app.route("/release_year")
def release_year():
    return render_template("release_year.html", release_urls=release_urls)

@app.route("/review_year")
def review_year():
    return render_template("review_year.html", review_urls=review_urls)

@app.route("/machine_learning")
def machine_learning():
    return render_template("machine_learning.html", ml_urls=ml_urls)

if __name__ == "__main__":
    app.run(debug=True)