#So co hau
n,m = map(int, input().split())
x = 1
result = 0
while x <= n:
  x = x*10
result = m // x
if (m % x) >= n:
  result = result + 1
print(result)