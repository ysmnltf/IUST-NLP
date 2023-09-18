import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
import nltk
import csv
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
all_tokens = []
hashtags = []
hashtag_regex = re.compile(r"[\s\W]#(\w+)")

def preprocess(text: str, print_steps=False):
    # 1 - remove redundant spaces
    prepro_text = re.sub(r"\s+", " ", text)
    if print_steps:
        print("remove redundant spaces: ", prepro_text)
    hashtags.extend(re.findall(hashtag_regex,prepro_text))
    # 2 - lowercase
    prepro_text = prepro_text.lower()
    if print_steps:
        print("lowercase: ", prepro_text)
    # 3 - remove handles
    prepro_text = re.sub(r"@\S+ ", "", prepro_text)
    if print_steps:
        print("remove handles: ", prepro_text)
    # 4 - remove numbers, special characters and punctuation
    prepro_text = re.sub(r"[^A-Za-z\s]+", " ", prepro_text)
    if print_steps:
        print("remove special characters and punc: ", prepro_text)
    # 5 - tokenize with nltk recommended tokenizer
    tokens = word_tokenize(prepro_text)
    if print_steps:
        print("tokens: ", tokens)
    # 6 - remove stop words
    filtered_tokens = [token for token in tokens if not token in stop_words]
    if print_steps:
        print("removed stopwords: ", filtered_tokens)
    # 7 - remove short tokens
    filtered_tokens = [token for token in filtered_tokens if len(token) > 3]
    if print_steps:
        print("remove tokens shorter than 3: ", filtered_tokens)
    # 8 - stem with porter stemmer
    porter_stemmer = PorterStemmer()
    stemmed_tokens = [porter_stemmer.stem(token) for token in filtered_tokens]
    if print_steps:
        print("stemmed tokens: ", stemmed_tokens)
    all_tokens.extend(stemmed_tokens)
    full_tweet = " ".join(stemmed_tokens)
    return full_tweet


if __name__ == '__main__':
    tweets = []
    with open("tweets.csv", encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if (len(row) > 0):
                tweets.append(row[0])
            else:
                tweets.append("")
    print("tweet: ", tweets[0])
    preprocess(tweets[0], print_steps=True)
    print("-------------------------------")
    print("tweet: ", tweets[1])
    preprocess(tweets[1], print_steps=True)
    print("-------------------------------")
    print("tweet: ", tweets[2])
    preprocess(tweets[2], print_steps=True)
    preprocessed_tweets = [preprocess(tweet) for tweet in tweets]
    counted_tokens = Counter(all_tokens)
    print("50 most common words: ", counted_tokens.most_common(50))
    trends = Counter(hashtags).most_common(10)
    print("10 trends: ", trends)
    wordcloud = WordCloud(collocations=True, background_color="white")
    wordcloud.generate_from_frequencies(dict(counted_tokens), 50)
    wordcloud.to_file("./wordcloud.png")


    data = dict(trends)
    courses = list(data.keys())
    values = list(data.values())
    plt.rcParams.update({'font.size': 14})

    fig = plt.figure(figsize=(30, 5))

    # creating the bar plot
    bar = plt.bar(courses, values, color='maroon',
            width=0.4)

    plt.title("Trends")
    # plt.show()
    plt.savefig('./trends-barchart.png')




