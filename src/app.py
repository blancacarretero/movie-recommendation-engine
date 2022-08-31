from flask import Flask, render_template

index_urls = {
    'all_movies':'/static/Resources/all-movies.png',
    'by_genre':'/static/Resources/avg_rating_by_genre.png',
    'movies_per_genre':'/static/Resources/num_movies_per_genre.png'
}

genre_urls = {
    'action':'/static/Resources/genre/average_rating_action.png',
    'avg_action':'/static/Resources/genre/avg_rating_by_year_action.png',
    'avg_crime':'/static/Resources/genre/avg_rating_by_year_crime.png',
    'avg_drama':'/static/Resources/genre/avg_rating_by_year_drama.png',
    'avg_war':'/static/Resources/genre/avg_rating_by_year_war.png',
}

release_urls = {
    'all':'/static/Resources/by_release_year/all-movies.png',
    'action':'/static/Resources/by_release_year/action-combined.png',
    'all_genre':'/static/Resources/by_release_year/all_genre.png',
}

review_urls = {
    'cult':'/static/Resources/by_review_year/cult-classics.png',
    'disney':'/static/Resources/by_review_year/disney-classics.png',
    'disney2':'/static/Resources/by_review_year/disney-classics2.png',
    'thriller_mystery':'/static/Resources/by_review_year/Thriller-Mystery.png',
    'animation_adventure':'/static/Resources/by_review_year/Animation-Adventure.png',
    'war_action':'/static/Resources/by_review_year/War-Action.png'
}

ml_urls = {
    'logreg':'/static/Resources/ml/logreg.png',
    'ttt':'/static/Resources/ml/train-test-split.png',
    'cluster1':'/static/Resources/ml/drama-vs-romance-1.png',
    'elbow':'/static/Resources/ml/elbow.png',
    'kmeans3':'/static/Resources/ml/kmeans-3.png',
    'kmeans4':'/static/Resources/ml/kmeans-4.png',
    'kmeans7':'/static/Resources/ml/kmeans-7.png',
    'tsne':'/static/Resources/ml/drama-vs-romance-tsne.png',
}

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