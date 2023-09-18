from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

nltk.download('punkt')

def read_text():
    with open('q2_sample_text.txt', encoding="utf-8") as f:
        txt = f.read()
    return txt

if __name__ == '__main__':
    text = read_text()
    print("text: ", text)
    print("work_tokenize: ", word_tokenize(text))
    print("sent_tokenize: ", sent_tokenize(text))