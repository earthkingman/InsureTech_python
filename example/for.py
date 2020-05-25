
myList = [i for i in range(10) if i%2==0]
print(myList)

word_list=["apple","banaba","carrot"]
myList = [i[0].upper() for i in word_list]
print(myList)

myList = [i.upper() for i in word_list]
print(myList)