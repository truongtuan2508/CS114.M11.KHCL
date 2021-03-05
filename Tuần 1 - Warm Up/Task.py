n = int(input())
k = int(input())
p = int(input())
q = int(input())

ith = (p-1) * 2 + (q-1)

before = ith - k
after = ith + k

if before >= 0:
    print(before//2+1, before%2+1)
elif after <= n-1:
    print(after//2+1, after%2+1)
else:
    print(-1)
