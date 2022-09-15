from flask import Flask, render_template, jsonify
from urls import index_urls, genre_urls, release_urls, review_urls, ml_urls
import data

app = Flask(__name__)

@app.route('/genre_data')
def chart_data():
   return jsonify(data.data)

@app.route('/data/<val>')
def data_retrieval(val):
    return data.plot_genre_by_year(val)

index_js = "<script src='/static/js/main.js'></script><script>index();</script>"
@app.route("/")
def index():
    return render_template("index.html", data=data, js=index_js)

genre_js = "<script src='/static/js/main.js'></script><script>genre();</script>"
@app.route("/genre")
def genre():
    return render_template("index.html", data=data, genre=data.plot_genre_by_year, js=genre_js)

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