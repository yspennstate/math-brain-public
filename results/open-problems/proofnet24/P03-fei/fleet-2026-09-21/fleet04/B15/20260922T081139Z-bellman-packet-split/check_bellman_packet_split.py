#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
from math import comb, log2

C = 6.521851214
LAM = 0.75
NEG = {0,1,2,3,4,5,6,8}

def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

vals = [-1 if x in NEG else 1 for x in range(16)]
raw = fwht_int(vals)
expected = [0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0]
assert raw == expected
w = [Fraction(r*r, 256) for r in raw]
assert sum(w) == 1
assert w[0] == 0
I = sum(Fraction(s.bit_count())*w[s] for s in range(16))
assert I == Fraction(3,2)
infl = [sum(w[s] for s in range(16) if (s>>i)&1) for i in range(4)]
assert infl == [Fraction(1,4), Fraction(1,4), Fraction(1,4), Fraction(3,4)]

# Signed packet valuations: both raw-magnitude packets have odd packet sums everywhere.
for mag in (4,12):
    supp = [s for s,r in enumerate(raw) if abs(r)==mag]
    for x in range(16):
        total = 0
        for s in supp:
            chi = -1 if ((s & x).bit_count() & 1) else 1
            total += (1 if raw[s] > 0 else -1) * chi
        assert total & 1

level_mass = defaultdict(Fraction)
class_mass = defaultdict(Fraction)
multiplicity = defaultdict(int)
for s,r in enumerate(raw):
    k = s.bit_count()
    m = abs(r)
    multiplicity[(k,m)] += 1
    if r:
        level_mass[k] += w[s]
        class_mass[(k,m)] += w[s]

assert level_mass == {1: Fraction(3,4), 3: Fraction(1,4)}
Kmag = 0.0
for k, pk in level_mass.items():
    for (kk,m), cnt in multiplicity.items():
        if kk != k:
            continue
        p = float(class_mass[(k,m)] / pk) if class_mass[(k,m)] else 0.0
        q = cnt / comb(4,k)
        if p:
            Kmag += float(pk) * p * log2(p/q)
Kmag_exact = 3.0/8.0 * log2(3.0)
assert abs(Kmag-Kmag_exact) < 1e-14

x = 2.0**(-C)
t = x**(1.0-LAM)
A_lam = (1.0+t)**4 - 1.0
m = 1.5*C
B = LAM*m - log2(A_lam/x)
lower_combo = B + Kmag
assert lower_combo > 17.0/80.0

H = sum(float(z)*log2(1.0/float(z)) for z in w if z)
R_direct = C*(float(I)-1.0) - H

Q_level = {k: comb(4,k)*(t**k)/A_lam for k in range(1,5)}
Kprice = 0.0
for k, pkq in level_mass.items():
    p = float(pkq)
    q = Q_level[k]
    Kprice += p*log2(p/q)
R_split = B + Kprice + Kmag
assert abs(R_direct-R_split) < 2e-13

A0 = (1.0+x)**4 - 1.0
KL = 0.0
for s,z in enumerate(w):
    if not z:
        continue
    k=s.bit_count()
    nu = x**k/A0
    KL += float(z)*log2(float(z)/nu)
R_gibbs = KL - log2(A0/x)
assert abs(R_direct-R_gibbs) < 2e-13

print("PASS")
print("walsh_raw", raw)
print("influences", [str(z) for z in infl], "I", str(I))
print("valuation_depths", {"raw4":0, "raw12":0})
print("K_mag_given_price_bits", f"{Kmag:.15f}")
print("bellman_lambda", LAM, "B_lambda_bits", f"{B:.15f}")
print("B_plus_Kmag_bits", f"{lower_combo:.15f}", "rigorous_floor", "17/80")
print("price_profile_KL_bits", f"{Kprice:.15f}")
print("R_direct_bits", f"{R_direct:.15f}")
print("R_split_bits", f"{R_split:.15f}")
print("R_gibbs_bits", f"{R_gibbs:.15f}")
