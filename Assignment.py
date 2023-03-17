q = 80
r = 60
s = 50
number = int(input("Enter Number:"))
if number>=q:
    print("Grade A")
elif number>=r<q:
    print("Grade B")
elif number>=s<r:
    print("Grade C")
else:
    print("Ungraded")

