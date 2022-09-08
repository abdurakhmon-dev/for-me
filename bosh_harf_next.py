def changefirstletter(words,letters):
    new_word = []
    for v in range(len(words)):
        new_word.append(letters[v]+words[v][1:]) 

    return " ".join(new_word)



def shiftsentence(sentence):
    words = sentence.split(" ")
    letters = [v[0] for v in words]
    letters.insert(0,letters[len(letters)-1])
    letters.pop(len(letters)-1)
    return changefirstletter(words,letters)


print(shiftsentence("Salom hammaga yaxshimisizlar"))