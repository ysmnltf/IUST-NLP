import re
regex = re.compile(r"((Doctor|Dr\.) (([A-Z][a-z-\.]+) ?)+)|(([A-Z][a-z\.]+,?( )?)+M\.D\.)")
def read_names():
    names = []
    with open('doctors_names.txt') as f:
        lines = f.readlines()
        for line in lines:
            names.append(line.strip())
    return names

def match_regex(text):
    match = regex.fullmatch(text)
    if match is None:
        return "False"
    return "True"


if __name__ == '__main__':
    names = read_names()
    for name in names:
        print(name, ": ", match_regex(name))