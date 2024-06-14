#Write a python program that calculates the factorial of a given number. 
num=int(input("Enter a number whose factorial you want?....."))
fac=1
for i in range(1,num+1):
    fac=i*fac
print("Factorial of given number=",fac)

