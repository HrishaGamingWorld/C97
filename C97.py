h = input("Enter the string:")
c=0
w=1
for i in h:
    c = c+1
    if i==' ':
        w=w+1
print("Number of words.",w)
print("Number of characters.",c)