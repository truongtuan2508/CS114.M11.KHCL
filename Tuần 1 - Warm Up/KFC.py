from decimal import *
F = float(input())
C = (F - 32.0)/1.8
K = C + 273.15
getcontext().prec = 6
print(Decimal(C).normalize(), Decimal(K).normalize())