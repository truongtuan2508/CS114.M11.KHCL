x = int(input())
f1 = f2 = f= 1
if 1 <= x <= 30:
    for i in range(x-2):
        f = f1 + f2
        f1 = f2
        f2 = f
    print(f)
else:
    print("So", x ,"khong nam trong khoang [1,30].")