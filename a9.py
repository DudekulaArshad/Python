n=int(input())
m=int(input())
for i in range(n,m):
    if n<=m:
        if i%m==0:
            print(i)
            n=n+1