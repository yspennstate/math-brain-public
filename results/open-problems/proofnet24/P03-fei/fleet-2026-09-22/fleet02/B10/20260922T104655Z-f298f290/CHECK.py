from fractions import Fraction
from itertools import product
import math


def coeffs(k, d):
    pts = list(product([1, -1], repeat=k))
    a = (1,) * k
    b = tuple(-1 if i < d else 1 for i in range(k))
    vals = {}
    for x in pts:
        v = x[0]
        if x == a or x == b:
            v = -v
        vals[x] = v
    out = {}
    for mask in range(1 << k):
        s = Fraction(0, 1)
        for x in pts:
            chi = 1
            for i in range(k):
                if (mask >> i) & 1:
                    chi *= x[i]
            s += vals[x] * chi
        out[mask] = s / Fraction(1 << k)
    return out


worst = None
cases = 0
for k in range(3, 8):
    q = Fraction(4, 1 << k)
    for d in range(1, k + 1):
        c = coeffs(k, d)
        Dmask = (1 << d) - 1
        assert c[0] == 0
        assert c[1] == 1 - q
        nz = 0
        for mask, v in c.items():
            if mask == 1:
                continue
            odd = ((mask & Dmask).bit_count() % 2) == 1
            assert v == (-q if odd else 0)
            if v:
                nz += 1
        assert nz == (1 << (k - 1)) - 1
        I = sum(Fraction(mask.bit_count()) * v * v for mask, v in c.items())
        expected = 1 + (k - 1) * q if d == 1 else 1 + (k - 2) * q
        assert I == expected
        H = -sum(float(v * v) * math.log2(float(v * v)) for v in c.values() if v)
        ratio = H / float(I - 1)
        if worst is None or ratio > worst[-1]:
            worst = (k, d, float(I - 1), H, ratio)
        cases += 1

print("cases", cases)
print("worst_k_d_delta_H_ratio", *worst)
print("analytic_constant", 4 + 1 / math.log(2))
print("PASS")
