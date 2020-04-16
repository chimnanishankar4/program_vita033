#Write a program to calculate the percentage of five subject
cpro=float(input("Enter mark of c programming:"))
java=float(input("Enter mark of java:"))
rprog=float(input("Enter mark of rprog:"))
dbms=float(input("Enter mark of dbms:"))
python=float(input("Enter mark of python:"))
tot=cpro+java+rprog+dbms+python
per=(tot/500)*100
print("marks percentage::",per)
