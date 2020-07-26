#https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6
t=int(input())
for i in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for j in range(1,n-1):
        if (a[j-1]<a[j] and a[j+1]<a[j]):
            c+=1
    print("Case #"+str(i)+": "+str(c))