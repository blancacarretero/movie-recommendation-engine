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
<img src="   " width="60%">

* Used extract and split function sto separate release year from the title column:
``` python
movies_df['release_year'] = movies_df['year'].str.split('(').str[-1]
movies_df = movies_df.drop(columns = ['year'])
```
<img src="   " width="60%">

* To use supervised machine learning, we categorized movies into two categories - liked or disliked movies. If the rating score was less than 3, it was a disliked movie (0). If it was more 3, it was a liked movie (1):
``` python
new_df["rating"] = np.where(new_df["rating"] >= 3, 1, 0)
```

## Dataflix Website 
<img src="   " width="60%">
<img src="   " width="60%">
<img src="   " width="60%">

* Movie Analysis
<img src="   " width="60%">
<img src="   " width="60%">

