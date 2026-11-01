from fractions import Fraction
from math import log2

def h2(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*log2(x) - (1.0-x)*log2(1.0-x)

def c_root(n):
    delta = 2.0**(2-n)
    lo = (n-2)/(n-1)
    hi = 1.0
    def F(c):
        return (1-c*(1-delta))*(1-c*delta)**(n-1) - (1-c)
    assert F(lo) <= 1e-15
    assert F(hi) >= 0.0
    for _ in range(240):
        mid = (lo+hi)/2
        if F(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def row(n):
    delta = Fraction(4, 2**n)
    M = 2**(n-1)-1
    big = (1-delta)**2
    small = delta**2
    assert big + M*small == 1
    I = big + small*(n*2**(n-2)-1)
    assert I - 1 == (n-2)*delta
    r1 = big + (2**(n-2)-1)*small
    ri = 2**(n-2)*small
    assert r1 == 1-delta
    assert ri == delta

    d = float(delta)
    t = float(M*small)
    H = h2(t) + t*log2(M)
    c = c_root(n)
    Hmax = (h2(c*(1-d)) + (n-1)*h2(c*d) - h2(c))/c
    gap = float(I-1)
    assert H <= 7.0*gap + 1e-12
    assert Hmax + 1e-12 >= (n-1)*gap
    K = Hmax-H
    assert K + 1e-12 >= (n-8)*gap
    return n, d, c, H/gap, Hmax/gap, K/gap

print("ANTIPODAL_TWO_FLIP_DICTATOR_CREDIT_BARRIER")
for n in (8,9,12,15,20,30):
    n,d,c,hr,hmr,kr = row(n)
    print(f"n={n} delta={d:.12g} c={c:.12g} "
          f"H/(I-1)={hr:.12g} Hmax/(I-1)={hmr:.12g} "
          f"K/(I-1)={kr:.12g} analytic_K_lower={n-8}")
print("STATUS=PASS")
