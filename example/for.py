
myList = [i for i in range(10) if i%2==0]
print(myList)

word_list=["apple","banaba","carrot"]
myList = [i[0].upper() for i in word_list]
print(myList)

myList = [i.upper() for i in word_list]
print(myList)


# 딕셔너리 자주사용
myDict ={ i:str(i) for i in range(10)}
print(myDict)

myDict2={v:k for k,v in myDict.items()}
print(myDict2)