from fractions import Fraction
import random, math, itertools


def ek(lam, k):
    total = 0.0
    for comb in itertools.combinations(lam, k):
        p = 1.0
        for x in comb:
            p *= x
        total += p
    return total


assert Fraction(1, 9) - Fraction(1, 4617) == Fraction(512, 4617)
assert (Fraction(1, 9) - Fraction(1, 4617))/2 == Fraction(256, 4617)
assert 3240 * 4617**2 == 69066072360

rng = random.Random(20260923)
tests = 0
for _ in range(5000):
    n = rng.randint(5, 10)
    s = sorted([10**rng.uniform(-3, 3) for __ in range(n)], reverse=True)
    lam = [x*x for x in s]
    T2 = sum(lam[2:])
    T4 = sum(lam[4:])
    E3 = ek(lam, 3)
    E5 = ek(lam, 5)
    if T2 <= 0 or E3 <= 0:
        continue
    pmax = min(9*T2, (162*E3)**(1/3))
    P = 0.9*pmax
    assert T2 >= P/9 - 1e-12*max(1, T2)
    assert E3 >= (P**3/162)*(1-1e-12)
    if T4 >= P/4617:
        lb = P**5/(3240*4617**2)
        assert E5 + 1e-10*max(1, E5) >= lb
    else:
        assert s[2]**2 + 1e-12*max(1, s[2]**2) >= 256*P/4617
        assert s[4] <= math.sqrt(T4) + 1e-15
    tests += 1

h = (2*math.sqrt(2)-1)/1572864
beta = math.sqrt(63)/16
Pmin = beta*h*h
gmin = math.sqrt(Pmin/9234)
tau0 = h*h/128

print("fraction_identity_1", Fraction(1, 9) - Fraction(1, 4617))
print("fraction_identity_2", (Fraction(1, 9) - Fraction(1, 4617))/2)
print("D5_denominator", 3240*4617**2)
print("C_D5", 5*math.sqrt(2*math.e)*(3240*4617**2)**0.1)
print("C_volume", 23*math.sqrt(4617)/16)
print("h", h)
print("beta", beta)
print("Pmin", Pmin)
print("gmin", gmin)
print("tau0", tau0)
print("gmin/(4*tau0)", gmin/(4*tau0))
print("edge_pair_abs_bound", 3*400**(1/3)*(32/9)**(1/6)*2**(5/6)*(Pmin/9234)**(-5/12))
print("spectral_random_tests", tests)
print("STATUS=PASS")
