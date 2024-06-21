a = 3
def prime(a):
    ctr=0
    for i in range(a,0,-1):
            if a%i ==0:
                ctr = ctr+1
    if ctr > 2:
        print("the number is not prime")
    else:
        print("the number is  prime")
n= int(input("Enter a number "))
prime(n)

