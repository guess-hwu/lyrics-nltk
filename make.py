import nltk
import xlwt
from xlwt import Workbook

nounList = ['NN', 'NNS', 'NNP', 'NNPS']
verbList = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
modList = ['RB', 'RBR', 'RBS', 'JJ', 'JJR', 'JJS']

numNouns = 0
numVerbs = 0
numMods = 0
others = 0

print("Enter mode (0 for write to file, 1 for one emotion printed to screen): ")
mode = int(input())

if (mode):
    print("Enter emotion (happy, sad, or informative): ")
    emotion = input()
    filename = emotion + ".txt"

    f = open(filename,'r')
    raw = f.read()
    tokens = nltk.word_tokenize(raw)
    # print(tokens)

    # text = nltk.Text(tokens)
    # print(text)

    tagged = nltk.pos_tag(tokens)

    # print(tagged)

    for i in range(0, len(tagged)):
        label = str(tagged[i][1])
        if (label in nounList):
            numNouns += 1
        elif (label in verbList):
            numVerbs += 1
        elif (label in modList):
            numMods += 1
        else:
            others += 1
    total = numNouns + numVerbs + numMods

    print("Number of nouns: " + str(numNouns))
    print("Number of verbs: " + str(numVerbs))
    print("Number of modifiers: " + str(numMods))
    print("Percentage of nouns: " + str(numNouns/total))
    print("Percentage of verbs: " + str(numVerbs/total))
    print("Percentage of modifiers: " + str(numMods/total))
    # print("Number of others: " + str(others))

else:
    print("Enter what you would like to call the .xls file: ")
    title = input()

    statsWB = Workbook() #creates a new Workbook
    sheet1 = statsWB.add_sheet('Sheet 1') #creates sheet1 sheet

    # (row, column)
    sheet1.write(0, 1, "% Nouns")
    sheet1.write(0, 2, "% Verbs")
    sheet1.write(0, 3, "% Modifiers (Adj & Adv)")

    emotions = ["happy", "sad", "informative"]
    row = 1
    for emot in emotions:
        filename = emot + ".txt"

        f = open(filename,'r')
        raw = f.read()
        tokens = nltk.word_tokenize(raw)
        # print(tokens)

        # text = nltk.Text(tokens)
        # print(text)

        tagged = nltk.pos_tag(tokens)
        # print(tagged)

        for i in range(0, len(tagged)):
            label = str(tagged[i][1])
            if (label in nounList):
                numNouns += 1
            elif (label in verbList):
                numVerbs += 1
            elif (label in modList):
                numMods += 1
            else:
                others += 1
        total = numNouns + numVerbs + numMods

        # write to Excel
        sheet1.write(row, 0, emot)
        sheet1.write(row, 1, str(numNouns/total))
        sheet1.write(row, 2, str(numVerbs/total))
        sheet1.write(row, 3, str(numMods/total))
        row += 1
        print(row)

    statsWB.save(title + '.xls')
