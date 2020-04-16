#write a program to prit 1 to 30 rpime numbers
for i in range(2,30):
    flag=True
    for n in range(2,i):
        if i%n==0:
            flag=False
            break
    if flag==True:
        print(i,"is prime")
   
