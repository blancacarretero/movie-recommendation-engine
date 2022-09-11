from flask import Flask, render_template, jsonify
from urls import index_urls, genre_urls, release_urls, review_urls, ml_urls
import data

app = Flask(__name__)

def data_creation(data, percent, class_labels, group=None):
   for index, item in enumerate(percent):
       data_instance = {}
       data_instance['category'] = class_labels[index]
       data_instance['value'] = item
       data_instance['group'] = group
       data.append(data_instance)

@app.route('/genre_data')
def chart_data():
   return jsonify(data.data)

@app.route("/")
def index():
    return render_template("index.html", data=data)

@app.route("/genre")
def genre():
    return render_template("genre.html", data=data)

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