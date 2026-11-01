"""Diagnostic only for QFORM-NO-UNIFORM-OUTPUT-MODULUS-v1.
The proof is analytic; this script only checks the exact finite-band length formula.
"""
import math

DELTA = math.pi / 3

def measure_G(s):
    total = 0.0
    count = 0
    kmin = math.floor((s - DELTA)/(2*math.pi)) - 2
    kmax = math.ceil((100*s + DELTA)/(2*math.pi)) + 2
    for k in range(kmin, kmax + 1):
        lo = (2*math.pi*k - DELTA)/s
        hi = (2*math.pi*k + DELTA)/s
        if hi <= 0:
            continue
        a = max(1.0, math.sqrt(max(lo, 0.0)))
        b = min(10.0, math.sqrt(max(hi, 0.0)))
        if b > a:
            total += b-a
            count += 1
    return total, count

for s in (50, 100, 200, 1000):
    m, n = measure_G(s)
    print(f"s={s:4d} |G_s|={m:.15f} components={n}")

print("phase lower bound Re g_s(s) >=", math.cos(DELTA))
print("three-copy Fourier lower bound >=", math.cos(DELTA)**3)
print("L1 translation lower bound >=", 2*math.cos(DELTA)**3)
print("Linf translation lower bound (support length <=298) >=", (2*math.cos(DELTA)**3)/298)
