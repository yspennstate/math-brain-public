"""Quick scan: is H (the homogenised Phi') negative anywhere on the cone for n = 11..14? Families with few values."""
import sys, random
from fractions import Fraction
from cone_recheck import H_num
rnd = random.Random(7)
for n in range(11, 15):
    worst = None
    # family (p, 1 x m, -q x r) and (p x s, t x m, -q x r), integer entries, sum zero, ordered, x1 + xn >= 0
    for s in (1, 2):
        for r in (1, 2, 3):
            m = n - s - r
            if m < 1: continue
            for p in range(1, 60):
                for q in range(1, p + 1):
                    num = r * q - s * p
                    # middle value t = num / m, need q >= -t ... ordered: p >= t >= -q
                    t = Fraction(num, m)
                    if not (p >= t >= -q): continue
                    x = [Fraction(p)] * s + [t] * m + [Fraction(-q)] * r
                    T = sum(v * v for v in x)
                    h = H_num(n, x) / T ** 4
                    if worst is None or h < worst[0]:
                        worst = (h, s, r, p, q, t)
    print(n, "min H/T^4 over the family:", float(worst[0]), worst[1:], flush=True)
