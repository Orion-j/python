# put a .txt file in the dir.
fileName = input('file name: ')
# open and read file user inputs
myFile = open(fileName)

# fetch word(s) in file and store in dict.
counts = {}
for line in myFile:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# count words which appears most.
bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(f'the word "{bigWord}" appeared {bigCount} times.')