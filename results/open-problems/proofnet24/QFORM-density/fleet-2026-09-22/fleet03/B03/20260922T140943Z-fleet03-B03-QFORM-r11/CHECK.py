"""Numerical sanity check for the r=4 collision constants in REPORT.md.
Not a proof: the analytic inequalities are proved in REPORT.md.
"""
import mpmath as mp
import math

mp.mp.dps = 50
for m in range(2, 9):
    I = (2**m/mp.pi) * mp.quad(lambda x: mp.besselk(0, x)**m, [0, 1, mp.inf])
    lower = (1/mp.pi)*(2/mp.e)**m*math.factorial(m)
    upper = 2**(m+1)*math.factorial(m)
    assert lower <= I <= upper
    print(m, mp.nstr(I, 18), mp.nstr(lower, 18), mp.nstr(upper, 18))
print("PASS")
