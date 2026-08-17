char=input()
a=int(input())
b=int(input())
if char=='+':
    print("%d + %d = %d"%(a,b,a+b))
elif char=='-':
    print("%d - %d = %d"%(a,b,a-b))
elif char=='*' :
    print("%d * %d = %d"%(a,b,a*b))
elif char=='/':
    print("%d / %d = %.3f"%(a,b,a/b))
elif char=='%':
    print(f"{a} % {b} = {a%b}")
elif char=='//':
    print(f"{a} // {b} = {a//b}")
elif char=='**':
    print(f"{a} ** {b} = {a**b}")
else:
    print("Error")
        