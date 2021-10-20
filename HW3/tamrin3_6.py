n = int(input("enter the number of list items :"))
a = []
for i in range(n) :
    a.append(int(input(f"enter item {i+1} of list : ")))

b = sorted(a)
f = True
for i in range(len(b)):
    if b[i] == a[i]:
        pass
    else:
        f = False
        break

if f:
    print("\n list is sort")
else:
    print("\n list is not sort")