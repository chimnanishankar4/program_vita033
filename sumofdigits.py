#Write a program to calculate sum of digits
tot=0
n=int(input("Enter a number:"))
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("Sum of the digits",tot)
