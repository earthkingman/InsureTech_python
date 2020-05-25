
myLambda = lambda x: x+1
print(myLambda(10))


# 파리미터가 두개 일 때
myLambda=lambda  x,y: x+y
print(myLambda(10,11))

# if else
myLambda = lambda x,y: x+y if x==y else x-y
print(myLambda(10,11))

# lisst comprehension에 적용하기
myLambda=lambda  x:x%4
myList = [i for i in range(1,11) if myLambda(i)]
print(myList)