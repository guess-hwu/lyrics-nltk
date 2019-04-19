import nltk

nounList = ['NN', 'NNS', 'NNP', 'NNPS']
verbList = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
modList = ['RB', 'RBR', 'RBS', 'JJ', 'JJR', 'JJS']

numNouns = 0
numVerbs = 0
numMods = 0
others = 0

print("Enter emotion (happy, sad, or informative): ")
filename = input()
filename = filename + ".txt"

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
