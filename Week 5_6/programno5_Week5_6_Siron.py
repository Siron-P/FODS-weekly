'''Develop a program that counts the occurrence of each word in a file.'''

text = open("program5.txt","r")
d=dict()

for line in text:
    line = line.strip() #removing the spaces and newline characters
    words = line.split(" ") #splitting the lines into words

    for word in words:
            if word in d:
                  d[word] = d[word] + 1

            else:
                  d[word] = 1

for key in list(d.keys()):
      print(key, ": ", d[key])