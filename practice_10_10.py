def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.count('the')
        print("Tht file " + filename + " has " + str(words) +
            " words of 'the'.")
        words_lower = contents.lower().count('the')
        print("The file " + filename + " has " + str(words_lower) +
            " words of 'the' and 'The'.")

filenames = ['The American Missionary.txt', 'dogs.txt', 'cats.txt',
    'alice.txt']
for filename in filenames:
    count_words(filename)
