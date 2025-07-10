s = int(input("Enter a the starting number: "))
e = int(input("Enter the ending number: "))
j = 0
for i in range(s, e+1):
    j = i**2
    if j % 2 == 0:
        print("The square of the number",i,"is",j,"which is an EVEN number")
    elif j % 2 != 0:
        print("The square of the number",i,"is",j,"which is an ODD number")