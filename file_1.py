list=[1,2,2,3,10,10,3,4,5,6,6,7]
for x in range(len(list)):
    if((list.count(x))>1):
        print(x,'is duplicate')
o/p
2 is duplicate
3 is duplicate
6 is duplicate
10 is duplicate
