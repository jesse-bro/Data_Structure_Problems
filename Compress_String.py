### Method to perform basic string compression using the
### counts of repeated characters. String only contains
### uppercase and lowercase letters (a-z).

def stringCompress(string):
    compressed = ""
    count = 0

    for i, ch in enumerate(string[:-1]):

        if ch != string[i+1] or i+1 >= len(string):
            compressed += "" + ch + str(count)
            count = 0
        count+=1

    # Last letter
    compressed += "" + string[-1] + str(count)
    if len(compressed) < len(string) :
        return compressed
    else:
        return string

    
sentence = "aabbbbccceeeefffgggh"
test = "aaeeegggdgjkloi"
print(stringCompress(sentence))
print(stringCompress(test))
