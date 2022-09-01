# Dataflix :movie_camera:

In this project we will be analyzing a MovieLens movie ratings database provided by [GroupLens Research](https://grouplens.org/datasets/movielens/).

<img src="https://bigpicturefilmclub.com/wp-content/uploads/2020/05/hinh-mo-bai_chong-dich-corona_elle-man_0320.jpg" width="95%">

## Preparing the Data

The following methods and dependencies were used:

* Python / Flask
* Pandas
* Jupyter Notebook
* Matplotlib
* SKLearn (KMeans, StandardScaler, PCA, TSNE)
* HTML / CSS / Bootstrap to present the results

https://drive.google.com/drive/folders/1XDCefA1BaBP1fFcp_JU2vIuuGGqWGIFf?usp=sharing

## Cleaning the Data
* Cleaned the data prior to analysis. Only wanted relevant tags and removed from the 'relevance' Column anything that was less than 85:
``` python
relevant_genomes = reduced_genome_scores_df.loc[reduced_genome_scores_df['relevance'] > .85]
```
``` python
new_df = reduced_ratings_df.merge(relevant_genomes, how="inner")
new_df.head()
```
<img src="https://github.com/blancacarretero/movie-recommendation-engine/blob/main/images/title_with_year.png?raw=true" width="60%">

* Used extract and split functions to separate release year from the title column:
``` python
movies_df['release_year'] = movies_df['year'].str.split('(').str[-1]
movies_df = movies_df.drop(columns = ['year'])
```
<img src="https://github.com/blancacarretero/movie-recommendation-engine/blob/main/images/title_year_separated.png?raw=true" width="60%">

* To use supervised machine learning, we categorized movies into two categories - liked or disliked movies. If the rating score was less than 3, it was a disliked movie (0). If it was more 3, it was a liked movie (1):
``` python
new_df["rating"] = np.where(new_df["rating"] >= 3, 1, 0)
```

## Dataflix Website 
Built website using HTML to portray all analysis, plots, and machine learning:

<img src="https://github.com/blancacarretero/movie-recommendation-engine/blob/main/images/releaseyear.png?raw=true" width="60%">

* There is a big jump in the number of movies released, which could be due to the impact of rapidly improving digital technology in the world and the overall rise in the film industry.

<img src="https://github.com/blancacarretero/movie-recommendation-engine/blob/main/images/reviewyear.png?raw=true" width="60%">

* We wanted to look into cult classics (that were released around the mid-nineties (when reviews start)) to see how they were received when they were first released compared to reviews posted more recently. Cult classics often have poor initial reception or limited early commercial success

<img src="https://github.com/blancacarretero/movie-recommendation-engine/blob/main/images/ml.png?raw=true" width="60%">

## Movie Analysis
<img src="https://github.com/blancacarretero/movie-recommendation-engine/blob/main/images/all_genre.png?raw=true" width="60%">

* The trend for all genres is that the average rating has slowly gone down since 1960.

<img src="https://github.com/blancacarretero/movie-recommendation-engine/blob/main/images/plots/action-combined.png?raw=true" width="60%">

* The big increase in movies released throughout the years could affect the average rating of movies that has been slowly decreasing.

## Conclusion
* Predictive Model
   * Intent was to be able to push out movie recommendations based on previous ratings for various movies and genres they fell under
* Reviews have not only become increasingly popular but also more essential since they started in the mid-nineties
  * Older movies with poor initial reception often see their ratings continue to increase over time; trend of ratings increasing over the years
  * Recent movies have less variation in ratings
* As more movies were released over the years, action movies were the primary genre that moved in the same direction 
* By continuing to evaluate the most recent ratings, we are confident our future model will be able to accurately project the popularity of new movies for an user

## Limitations
* The dataset we chose did not have a lot of demographic information.
  * Location, Age, Gender (User ID)
* Missing information such as Actor/Director details that would help further predictive model
* Reviews only went back to 1995; 
* Massive dataset before condensing to reduced dataset to actualize data easier; ability for higher processing power would’ve led to increased accuracy

## Further Considerations
* Release Year vs. Review Year
  * Time varying between release/review year effects accuracy of review
* Rating per User ID varies by different criteria each individual may use to evaluate movie
* Movies may fall under multiple genres which can skew data in either direction
* Review popular tags with corresponding ratings to consider other user feedback
* Per the time frame evaluated, other factors may have influenced rating:
  * Movie Experience
  * Graphics/Picture
* With time permitted, we would like to continue our model to factor in previous movies/ratings that would allow user to input personal ratings that would help predict if they would enjoy an upcoming movie release


