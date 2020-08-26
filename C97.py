intro=input("enter your introduction")
characterCount=0
wordCount=1
for i in intro:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1

print(characterCount)
print("wordCount=",wordCount)

friend=["riya","rida","rima","ripa"]
for i in friend:
    print(i)


# whileloop
count=0
while(count<=0):
    print(count)
    count=count-1
