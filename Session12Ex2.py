#print out only the words that appear more than 2 times in a file

fg = open('Text.txt')
twice = []
words = []
signs = [',','.','!','?',':',';','-','+']
for line in fg:
    for sign in signs:
        line.replace(sign,"")

    line_words = line.split( )
    for word in line_words:
        if word in words:
            if not word in twice:
                twice.append(word)
        else:
            words.append(word)
    print(twice)
    fg.close