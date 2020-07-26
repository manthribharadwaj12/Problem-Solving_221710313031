#include<stdio.h>
#include<math.h>
int main()
{ int i,j,n,b,s=0,a;
 scanf("%d",&n);
 for(i=0;pow(2,i)<=n;i++)
 {a=pow(2,i);
 for(j=0;j<=n;j++)
 {  
 b=pow(2,(a+2*j));
  s=s+b;}}
 printf("%d",s%10);
 return 0; 
}
