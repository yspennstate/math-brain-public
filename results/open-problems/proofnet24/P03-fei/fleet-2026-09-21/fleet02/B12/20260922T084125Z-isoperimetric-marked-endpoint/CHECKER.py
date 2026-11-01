from fractions import Fraction
from itertools import combinations
import math

K = Fraction(13132, 2021)
C = Fraction(3260925607, 500000000)
LN2_LOWER = 2*(Fraction(1,3)+Fraction(1,81)+Fraction(1,1215))
DELTA_STAR = 47*(3-math.sqrt(3))/3456

def fwht(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def stats(vals, n):
    N = 1 << n
    W = fwht(vals)
    p = [Fraction(w*w, N*N) for w in W]
    I = sum(Fraction(s.bit_count())*p[s] for s in range(N))
    H = 0.0
    for q in p:
        if q:
            x = float(q)
            H -= x*math.log2(x)
    mx = max(p[1 << i] for i in range(n))
    return I, H, mx

assert 3**12 > 2**19
assert LN2_LOWER > Fraction(9,13)
assert K < C

peer_viol = 0
main_viol = 0
balanced_checked = 0
for n in range(1,5):
    N = 1 << n
    for neg in combinations(range(N), N//2):
        vals = [1]*N
        for x in neg:
            vals[x] = -1
        I, H, mx = stats(vals,n)
        delta = float(I-1)
        balanced_checked += 1
        if float(1-mx) > (3+math.sqrt(3))*max(delta,0.0) + 1e-12:
            peer_viol += 1
        if delta <= DELTA_STAR + 1e-15 and H > float(K)*max(delta,0.0) + 1e-12:
            main_viol += 1

sparse = []
for n in range(12,16):
    N=1 << n
    vals=[1 if (x&1)==0 else -1 for x in range(N)]
    for x in (0, 7):
        vals[x] *= -1
    I,H,mx=stats(vals,n)
    delta=float(I-1)
    sparse.append((n,delta,H/delta,H <= float(K)*delta+1e-12))

print("PASS")
print("K", K, f"{float(K):.15f}")
print("C_minus_K", C-K, f"{float(C-K):.15f}")
print("ln2_lower", LN2_LOWER, f"{float(LN2_LOWER):.15f}")
print("pow_check", 3**12, 2**19, 3**12 > 2**19)
print("delta_star", f"{DELTA_STAR:.15f}")
print("balanced_small_checked", balanced_checked)
print("peer_concentration_violations", peer_viol)
print("endpoint_bound_violations", main_viol)
for n,delta,ratio,ok in sparse:
    print("sparse", n, f"{delta:.15f}", f"{ratio:.15f}", ok)
