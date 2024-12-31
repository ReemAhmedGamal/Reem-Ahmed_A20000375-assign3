# -*- coding: utf-8 -*-
"""Reem_Ahmed _A20000375_Assign3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RYwy539wZdmwQrHH_lnz5dyIil1bRLOY
"""

import pandas as pd
import matplotlib.pyplot as plt


file_path = '/content/5000_movies.csv'
df = pd.read_csv(file_path)

df.head(), df.info()

import numpy as np


df['adjusted_rating'] = (df['vote_average'] - df['vote_average'].min()) / \
                        (df['vote_average'].max() - df['vote_average'].min()) * 4 + 1

Thu = df['vote_count'].sum()

Tni = df['id'].nunique()


ratings_per_product = df[['title', 'vote_count']].sort_values(by='vote_count', ascending=False)

plt.figure(figsize=(10, 6))
plt.hist(df['adjusted_rating'], bins=np.arange(1, 6, 0.5), edgecolor='black', color='skyblue')
plt.title('Distribution of Ratings (Adjusted)', fontsize=14)
plt.xlabel('Rating (1-5 scale)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


actual_ratings = df['vote_count'].sum()
sparsity = 1 - (actual_ratings / possible_ratings)


rating_bias = df['adjusted_rating'].mean()


lowest_rated_items = df.nsmallest(2, 'adjusted_rating')[['title', 'adjusted_rating']]

Thu, Tni, sparsity, rating_bias, lowest_rated_items

ratings_matrix = df.pivot(index='id', columns='title', values='vote_average')

target_items = ['Black Water Transit', "Should've Been Romeo"]
ratings_matrix_target = ratings_matrix[target_items]

avg_ratings_target = ratings_matrix_target.mean()

ratings_matrix_target_filled = ratings_matrix_target.fillna(avg_ratings_target)

avg_ratings_all = ratings_matrix.mean(axis=0)

ratings_diff = ratings_matrix.sub(avg_ratings_all, axis=1)

covariance_matrix = ratings_diff.cov()

top_5_peers = {item: covariance_matrix[item].nlargest(6).iloc[1:6] for item in target_items}
top_10_peers = {item: covariance_matrix[item].nlargest(11).iloc[1:11] for item in target_items}

avg_ratings_target, ratings_matrix_target_filled.head(), avg_ratings_all.head(), top_5_peers, top_10_peers

ratings_diff = ratings_matrix.sub(ratings_matrix.mean(axis=0), axis=1)


covariance_matrix = ratings_diff.cov()


ratings_diff.head(), covariance_matrix.head()

ratings_matrix.shape,

if not isinstance(covariance_matrix, np.ndarray):
    print("covariance_matrix value:", covariance_matrix)

mean_filled_data = ratings_matrix.fillna(ratings_matrix.mean(axis=0))


print(mean_filled_data.head())

cov_matrix = np.cov(mean_filled_data.T)


print("Covariance Matrix:\n", cov_matrix)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)


print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

orthogonal_check = np.allclose(np.dot(eigenvectors.T, eigenvectors), np.eye(len(eigenvectors)))
print("Are eigenvectors orthogonal?", orthogonal_check)


if not orthogonal_check:
    def gram_schmidt(vectors):
        ortho_vectors = []
        for v in vectors.T:
            for u in ortho_vectors:
                v -= np.dot(v, u) * u
            ortho_vectors.append(v / np.linalg.norm(v))
        return np.array(ortho_vectors).T

    eigenvectors = gram_schmidt(eigenvectors)
    print("Orthogonalized Eigenvectors:\n", eigenvectors)