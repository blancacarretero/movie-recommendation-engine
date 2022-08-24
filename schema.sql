CREATE TABLE movies (
  movieId int PRIMARY KEY,
  title VARCHAR,
  genres VARCHAR
);

CREATE TABLE ratings (
    userId int,
    movieId int,
    rating float,
    timestamp int
);

CREATE TABLE genome_scores (
    movieId int,
    tagId int,
    relevance float
);

CREATE TABLE genome_tags (
    tagId int,
    tag VARCHAR
);

CREATE TABLE links (
    movieId int,
    imdbId int,
    tmdbId int
);

CREATE TABLE tags (
    userId int,
    movieId int,
    tag VARCHAR,
    timestamp int
);