#https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003381cb
import math
t=int(input())
for i in range(1,t+1):
    n=int(input())
    list1=list(map(int,input().split()))
    sublist = [math.sqrt(sum(list1[k:j]))-math.floor(math.sqrt(sum(list1[k:j])))==0 for k in range(len(list1) + 1) for j in range(k + 1, len(list1) + 1)]
    print("Case #"+str(i)+": "+str(sublist.count(1)))