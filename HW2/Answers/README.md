# Sentiment Analysis of IMDB Movie Reviews

## Dataset

IMDB dataset is imported from keras.datasets.

## Preprocessing

The dataset is preprocessed through these steps:

1. Punctuations are removed.
2. Text is tokenized using nltk's 'word_tokenize' method.
3. Tokens are stemmed with 'SnowballStemmer'.
4. English stopwords are removed.

## Models

A unigram, a bigram and a trigram classifers are trained on the data.

## Evaluation

Each model is evaluted with recall, precision, f1score and accuracy.
|model|recall|precision|f1score|accuracy|
|-----|------|---------|-------|--------|
|unigram | 0.81504 | 0.851555 | 0.832897 | 0.83648 |
|bigram | 0.8516 | 0.866363 | 0.858918 | 0.86012 |
|trigram | 0.79064 | 0.812479 | 0.801411 | 0.80408 |
