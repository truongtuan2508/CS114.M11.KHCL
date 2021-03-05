from decimal import *
PSI = float(input())
Kg_Cm2 = (PSI*0.453592) / (2.54 * 2.54)
getcontext().prec = 6
print(Decimal(Kg_Cm2).normalize())