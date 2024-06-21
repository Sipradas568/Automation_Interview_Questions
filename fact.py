a = 2
def fact(a):
    x=1
    for i in range(a,0,-1):
        x=x*i
    print("factorial of {} is: " .format(a), x)

n = int(input("enter the number"))
fact(n)
