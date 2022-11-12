li = []
n = int(input("Enter the size of list"))
for i in range(0,n):
    e = int(input("Enter the element of list"))
    li.append(e)

print("Positive numbers in",li,"are:")

for i in li:
    if i >= 0:
        print(i,end = " ")
           
