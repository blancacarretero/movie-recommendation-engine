import numpy as np
import pandas as pd

csv1 = "static/data/movies.csv"
csv2 = "static/data/ratings.csv"

movies = pd.read_csv(csv1)
ratings = pd.read_csv(csv2)

movies['year'] = movies.title.str.extract('.*\((.*)\).*',expand = False)
movies = movies.dropna()

movies = movies[movies.year.str.contains('1983\)')==False]
movies = movies[movies.year.str.contains('Das Millionenspiel')==False]
movies = movies[movies.year.str.contains('Your Past Is Showing')==False]
movies = movies[movies.year.str.contains('Close Relations')==False]
movies = movies[movies.year.str.contains('2006–2007')==False]

movies.year = pd.to_numeric(movies.year)

movie_ratings = movies.merge(ratings, how="inner")

# release year column
movie_ratings['year'] = movie_ratings.title.str.extract('\((.*)\)')[0]
movie_ratings['release_year'] = movie_ratings['year'].str.split('(').str[-1]
movie_ratings = movie_ratings.drop(columns = ['year'])

# Genre Ratings function
def genre_ratings(genre):
    df = movie_ratings[movie_ratings['genres'].str.contains(genre, regex=False)]
    return df

# Rating by Year Function
def ratings_by_year(genre, year):
    df = movie_ratings[movie_ratings['genres'].str.contains(genre, regex=False)]
    year_df = df.loc[df['release_year'] == year]
    avg_rating = year_df.groupby('release_year')['rating'].mean()
    return avg_rating[0]

genres = ['Comedy','Adventure','Animation','Children','Fantasy','Romance','Drama',
          'Documentary','Action','Horror','Mystery','Sci-Fi','Western','Crime','Thriller',
          'Film-Noir','Musical','War']

# genre averages
genre_averages_dict = {
    'Genre': [],
    'avgRate': []
}

for genre in genres:
    avg_rating = genre_ratings(genre)['rating'].mean()
    genre_averages_dict['Genre'].append(genre)
    genre_averages_dict['avgRate'].append(round(avg_rating,2))

# ratings
ratings_dict = {
    'Year': [],
    'avgRate': []
}

years = ['1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006',
         '2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']

for year in years:
    avg = ratings_by_year('Action',year)
    ratings_dict['avgRate'].append(avg)
    ratings_dict['Year'].append(year)

data = {
    'genreAvg':genre_averages_dict,
    'ratings':ratings_dict
}