'''Write a program to count the number of
lines, words, and characters in a text file.'''

def count(files): #function to count
    try:
        with open(files,'r') as f: #opining file in read mode
            word_count = 0
            char_count = 0
            lines_count = 0

            for line in f:
                lines_count +=1
                char_count += len(line)
                words = line.split()
                word_count += len(words)

            print("Output: \n")
            print("The number of lines in the following files are",lines_count)
            print("The number of words in the following files are",word_count)
            print("The number of characters in the following files are",char_count)

    except FileNotFoundError: #for error while finding file
        print("File not Found!")

files = "program1.txt"
count(files)#call func.