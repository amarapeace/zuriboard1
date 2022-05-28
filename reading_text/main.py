# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file=open(filename, 'r')
    content=file.read()
    file.close()
    print(content)
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words=text.split()
    print(words)

    dic={}
    for word in words:
        if word in dic.keys():
            dic[word] +=1
        else:
            dic[word] =1
    print(dic)

    
count_words()

    #return {"as": 10, "would": 20}