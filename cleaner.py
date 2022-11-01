import pandas as pd

dataset_users = pd.read_csv('./datasets/users.csv', encoding='unicode_escape')
clean_users = dataset_users.dropna()
ratings = pd.read_csv('./datasets/ratings.csv', encoding='unicode_escape')
ratings_clean = ratings.dropna()

clean_users.to_csv('./datasets/clean_users.csv')
clean_ratings = ratings.to_csv('./datasets/clean_ratings.csv')