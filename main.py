# Lets us access book names from the terminal
import sys


# Function takes any number of arguments and puts them in to a list
# so this means it will work with a list of the word lists
def organiseWords(wordLists):
    # file that the output will be written to
    outputFile = open("output/output.txt", "w")


    # length of the shortest book
    for i in range(len(min(wordLists, key=len))):
        # length of the number of books given
        for j in range(len(wordLists)):
            # j is accessing the books, i is accessing the words
            # these are written to the output file with a new line
            # for each word ("\n" denotes a new line)
            outputFile.write(wordLists[j][i] + "\n")
        # take a new line between sets of words (set of 1st words, 2nd words etc)
        outputFile.write("\n")

    # Close and save the output file
    outputFile.close()

# This function puts the text files in to a form the program can work with
# Words in the book are put in to a list called wordList

def makeList(fileName):

    # open the file called whatever the variable 'fileName' contains in
    # read-only mode
    f = open(fileName, "r")
    allWords = f.read()
    # The .split() method gives a list of all the words in the file
    # it understands a words as being separated by spaces
    wordList = allWords.split()
    return wordList





# main body of code
if __name__ == "__main__":
    wordLists = []
    # make word lists for all of the file names you typed in to
    # the terminal
    for i in range(1,len(sys.argv)):
        wordLists.append(makeList(sys.argv[i]))

    organiseWords(wordLists)
