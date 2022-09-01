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
Cleaned the data prior to analysis. Only wanted relevant tags and removed from the 'relevance' Column anything that was less than 85.
``` python
relevant_genomes = reduced_genome_scores_df.loc[reduced_genome_scores_df['relevance'] > .85]
```

