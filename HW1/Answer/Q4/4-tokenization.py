from nltk.tokenize import TreebankWordTokenizer, RegexpTokenizer,\
    WhitespaceTokenizer, WordPunctTokenizer
import nltk


def read_text(path):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    return txt


if __name__ == '__main__':
    # الف
    english_sample = read_text("AlbertEinstein.txt")
    english_short = read_text("ShortSampleEnglish.txt")
    persian_sample = read_text("Shahnameh.txt")
    persian_short = read_text("ShortSamplePersian.txt")

    # پ
    print("---TreeBankTokenizer------------------------")
    treebank_tokenizer = TreebankWordTokenizer()
    tree_bank_english_sample_res = treebank_tokenizer.tokenize(english_sample)
    print(
        f"English sample:\nTokens num: {len(tree_bank_english_sample_res)}, Types num: {len(set(tree_bank_english_sample_res))}")
    tree_bank_persian_sample_res = treebank_tokenizer.tokenize(persian_sample)
    print(
        f"Persian sample:\nTokens num: {len(tree_bank_persian_sample_res)}, Types num: {len(set(tree_bank_persian_sample_res))}")
    tree_bank_english_short_res = treebank_tokenizer.tokenize(english_short)
    print(
        f"English short:\nTokens num: {len(tree_bank_english_short_res)}, Types num: {len(set(tree_bank_english_short_res))}")
    tree_bank_persian_short_res = treebank_tokenizer.tokenize(persian_short)
    print(
        f"Persian short:\nTokens num: {len(tree_bank_persian_short_res)}, Types num: {len(set(tree_bank_persian_short_res))}")

    # ت
    print("---RegexpTokenizer------------------------")
    word_re_tokenizer = RegexpTokenizer('\s+', gaps=True)
    num_re_tokenizer = RegexpTokenizer('\d+')
    num_re_english_sample_res = num_re_tokenizer.tokenize(english_sample)
    print(f"English sample numbers:\n{', '.join(num_re_english_sample_res)}")
    word_re_english_short_res = word_re_tokenizer.tokenize(english_short)
    print(f"English short words:\n{', '.join(word_re_english_short_res)}")
    word_re_persian_short_res = word_re_tokenizer.tokenize(persian_short)
    print(f"Persian short words:\n{', '.join(word_re_persian_short_res)}")

    # ث
    print("---WhitespaceTokenizer------------------------")
    whitespace_tokenizer = WhitespaceTokenizer()
    whitespace_regex_tokenizer = RegexpTokenizer('\s+', gaps=True)
    whitespace_english_short_res = whitespace_tokenizer.tokenize(english_short)
    whitespace_re_english_short_res = whitespace_regex_tokenizer.tokenize(english_short)
    print(f"English short words with whitespace tokenizer:\n{', '.join(whitespace_english_short_res)}")
    print(f"English short words with whitespace regex tokenizer:\n{', '.join(whitespace_re_english_short_res)}")

    # ج
    print("---WordPunctTokenizer------------------------")
    wordpunct_tokenizer = WordPunctTokenizer()
    wordpunct_english_short_res = wordpunct_tokenizer.tokenize(english_short)
    print(f"English short words:\n{', '.join(wordpunct_english_short_res)}")
