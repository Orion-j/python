# reading file and counting words occurring most.

words = {}
the_file = input("txt file: ")
complete_file = open(the_file)
# print(complete_file)
for words_count in complete_file:
    some_word = words_count.split()  # words from file into a list.
    for one_word in some_word:
        if one_word not in words:
            words[one_word] = 1
        words[one_word] = words[one_word] + 1
print("counting the words\n")
# print(words)
