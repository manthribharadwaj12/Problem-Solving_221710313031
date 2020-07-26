#https://www.codechef.com/problems/HS08TEST
n=input().split(' ');

k=float(n[1])
n1=int(n[0])
if(n1%5==0 and n1<=k-0.5):
    n1=float(n1)+0.5;
    k=k-n1;
    print("%.2f" % k)
else:
    print("%.2f" % k)