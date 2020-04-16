'''
#Wap to print the pyramid like this

A
B B
C C C
D D D D
E E E E E

'''
n=int(input("Enter number of rows:"))
for i in range(n):
    print((chr(65+i)+' ')*(i+1))
