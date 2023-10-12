# -*- coding: utf-8 -*-
"""
Text Data Visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Collection, Callable, Tuple

__all__ = ['rank_features_by_label', 'rank_features_for_all_labels', 'plot_top_features']

def rank_features_by_label(X: np.ndarray, features: Collection[str], label_idx: Collection[bool] = None,
                    min_value: float = 0.1, aggregation_function: Callable = np.mean) -> pd.DataFrame:
    """
    Rank features of each label by their encoded values (e.g., CountVectorizer, TfidfVectorizer, etc.)
    aggregated with `aggregation_function`.

    :param X np.ndarray: Document-value matrix.
    :param features Collection[str]: Feature names.
    :param label_idx Collection[int]: Position of rows with specified label.
    :param min_value float: Minimum value to take into account for each feature.
    :param aggregation_function Callable: Function to aggregate features such as `np.mean` or `np.sum`.
    :return: A DataFrame with 'feature', 'score' and 'ngram'.
    """
    # Filter features based on the label index and apply the min_value threshold
    filtered_features = X[label_idx] if label_idx is not None else X
    filtered_features[filtered_features < min_value] = 0
    
    # Calculate the aggregated scores for each feature
    aggregated_scores = aggregation_function(filtered_features, axis=0)
    
    # Create a DataFrame with feature names, scores, and ngram counts
    df = pd.DataFrame({
        'feature': features,
        'score': aggregated_scores,
        'ngram': [len(set(feat.split(' '))) for feat in features]
    })
    return df

def rank_features_for_all_labels(X: np.ndarray, y: np.ndarray, features: Collection[str], min_value: float = 0.1,
                  aggregation_function: Callable = np.mean) -> Collection[pd.DataFrame]:
    """
    Rank features for all labels by their encoded values (e.g., CountVectorizer, TfidfVectorizer, etc.)
    aggregated with `aggregation_function`.

    :param X np.ndarray: Document-value matrix.
    :param y np.ndarray: Labels.
    :param features Collection[str]: Feature names.
    :param min_value float: Minimum value to take into account for each feature.
    :param aggregation_function Callable: Function to aggregate features such as `np.mean` or `np.sum`.
    :return: A list of DataFrames with 'rank' (rank within label), 'feature', 'score', 'ngram' and 'label'.
    """
    unique_labels = np.unique(y)
    dfs = []
    for label in unique_labels:
        label_idx = (y == label)
        df = rank_features_by_label(X, features, label_idx, min_value, aggregation_function).reset_index()
        df['label'] = label
        df.columns = ['rank', 'feature', 'score', 'ngram', 'label']
        dfs.append(df)
    return dfs

def plot_top_features(dataframes: Collection[pd.DataFrame], top_n: int = 25, ngram_range: Tuple[int,int]=(1,2)) -> None:
    """
    Plot top features from a collection of dataframes.

    :param dataframes Collection[pd.DataFrame]: A list of dataframes.
    :param top_n int: Number of top features to show.
    :param ngram_range Tuple[int,int]: Range of ngrams for features to show.
    :return: None
    """
    fig = plt.figure(figsize=(12, 9), facecolor="w")
    x = np.arange(top_n)
    for i, df in enumerate(dataframes):
        # Filter data by ngram range and select the top_n features
        filtered_df = df[(df.ngram >= ngram_range[0]) & (df.ngram <= ngram_range[1])][:top_n]
        ax = fig.add_subplot(1, len(dataframes), i + 1)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_frame_on(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        ax.set_xlabel("Score", labelpad=16, fontsize=14)
        ax.set_title(f"Label = {str(df.label[0])}", fontsize=16)
        ax.ticklabel_format(axis='x', style='sci', scilimits=(-2, 2))
        ax.barh(x, filtered_df.score, align='center', color='#3F5D7D')
        ax.set_yticks(x)
        ax.set_ylim([-1, x[-1] + 1])
        ax.invert_yaxis()
        yticks = ax.set_yticklabels(filtered_df.feature)
        plt.subplots_adjust(bottom=0.09, right=0.97, left=0.15, top=0.95, wspace=0.52)
    plt.show()
