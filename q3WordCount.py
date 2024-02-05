def wordCount(t):
    dictionary = {}
    file = open(t, "r")
    
    for lineNum, line in enumerate(file, start=1):
        words = line.replace(',','').replace('.','').strip().split()
        # set will get unique words in the text
        for word in set(words):
            if word not in dictionary:
                dictionary[word] = [lineNum]
            elif lineNum not in dictionary[word]:
                dictionary[word].append(lineNum)

    return dictionary

# Print the result
for word, lineNum in wordCount("./q3Text.txt").items():
    print(f"{word}: {lineNum}")