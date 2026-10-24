from fractions import Fraction
from mpmath import mp, log, mpf
mp.dps = 30
L3 = log(3)
def sigma_from_c(c): return 1 - log(mpf(c))/L3
D = {1: Fraction(5,2), 2: Fraction(393,64), 3: Fraction(15796051,1048576)}
U4 = Fraction(20871140813662641,562949953421312)   # heuristic policy at depth 4 (upper bound on D_4)
print("greedy (5/6)^k:      sigma >=", sigma_from_c(mpf(5)/2))
for k,d in D.items():
    print(f"D_{k}^(1/{k}) = {mpf(d.numerator)/d.denominator**1 if False else (mpf(d.numerator)/mpf(d.denominator))**(mpf(1)/k)}   sigma >= {sigma_from_c((mpf(d.numerator)/mpf(d.denominator))**(mpf(1)/k))}")
c4 = (mpf(U4.numerator)/mpf(U4.denominator))**(mpf(1)/4)
print("U_4^(1/4) =", c4, "  sigma >=", sigma_from_c(c4))
print("influence bound: sigma <= log(4/3)/log 3 =", log(mpf(4)/3)/L3)
print("old ledger bound 1-log2/log3 =", 1-log(2)/L3)
print("ratios D2/D1, D3/D2, U4/D3:", float(D[2]/D[1]), float(D[3]/D[2]), float(U4/D[3]))
# guess: if c ~ 2.452
print("if c=2.452: sigma ~", sigma_from_c(mpf('2.452')))
