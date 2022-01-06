string1=input("enter a string")
charactercount=0
wordcount=1
for i in string1:
    charactercount=charactercount+1
    if(i==' '):
        wordcount=wordcount+1
print("number of words in the string")
print(wordcount)
print("number of characters in the string")
print(charactercount)
