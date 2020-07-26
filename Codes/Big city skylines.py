#https://static.googleusercontent.com/media/services.google.com/en//blog_resources/Google_CodeJam_Practice.pdf
n=int(input())
a=list(map(int,input().split()))
a1=[a[i] for i in range(0,len(a)) if i%2==0]
a2=[a[i] for i in range(0,len(a)) if i%2!=0]
print(sum(a1)*min(a2))