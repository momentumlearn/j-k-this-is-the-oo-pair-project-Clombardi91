fileObject = open("words.txt", "r")
lines = fileObject.readlines()
words = [line[:-1] for line in lines]
print(words)