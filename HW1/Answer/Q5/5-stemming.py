from nltk import TreebankWordTokenizer, WordNetLemmatizer
from nltk.stem import LancasterStemmer, PorterStemmer


def read_text(path):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    return txt


if __name__ == '__main__':
    english_sample = read_text("AlbertEinstein.txt")
    indices = [2, 10, 18, 19, 21, 22, 42]

    porter_stemmer = PorterStemmer()
    lanc_stemmer = LancasterStemmer()

    treebank_tokenizer = TreebankWordTokenizer()
    tokens = treebank_tokenizer.tokenize(english_sample)

    for idx in indices:
        word = tokens[idx]
        print(f"word: {word}, porter: {porter_stemmer.stem(word)}, lank: {lanc_stemmer.stem(word)}")

    print("-----------------")
    words = ["waves", "fishing", "rocks", "was", "corpora", "better", "ate", "broken"]
    lemmatizer = WordNetLemmatizer()
    for w in words:
        print(f"word: {w}, lemmatized (default): {lemmatizer.lemmatize(w)}")
    print("-----------------")

    poss = ["n", "v", "n", "v", "n", "a", "v", "v"]
    for i in range(len(words)):
        print(f"word: {words[i]}, lemmatized (with pos): {lemmatizer.lemmatize(words[i], poss[i])}")
