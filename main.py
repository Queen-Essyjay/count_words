# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment]
    with open(filename) as f:
        contents = f.readlines()
        return contents


def count_words(word):
    text = read_file_content("./story.txt")
    # [assignment]
    
    word_list = word.split(" ")
    word_list = [word for word in word_list if word.isalnum()]

    word_dictionary = {}
    for word in word_list:
        word = word.lower()
        if word in word_dictionary:
        
            prev_count = word_dictionary[word]
            word_dictionary[word] = prev_count + 1
        
        else:
            word_dictionary[word] = 1
        
    
    return word_dictionary

count_words("The cake is done. It is a big cake !")
