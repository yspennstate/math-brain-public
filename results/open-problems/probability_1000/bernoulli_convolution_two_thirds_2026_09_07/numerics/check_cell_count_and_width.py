"""Foundation check for the width/cost criterion: the cell count and the total width.

Cells are the pieces of xi in [1,2) on which every A_m = round((3/2)^m xi), m < K, is constant.
Claimed: #cells = 3.03 (3/2)^K, sum of cell d-interval widths = (3/2)^K exactly, mean width 1/3.
The width claim should be near-trivial - as xi crosses [1,2) the quantity (3/2)^K xi sweeps a total
length (3/2)^K - but the CELL COUNT is the load-bearing one, because #cells ~ (3/2)^K is what makes the
leaf-string entropy rate log(3/2) rather than the orbit-digit rate log 3. Enumerate by exact rational
breakpoints: a new cell starts wherever (3/2)^m xi crosses a half-integer, for some m < K.
"""
from fractions import Fraction as F

print(f"{'K':>3} {'#cells':>8} {'(3/2)^K':>10} {'#cells/(3/2)^K':>16} {'sum width':>12} {'/(3/2)^K':>10}")
for K in range(2, 17):
    cuts = {F(1), F(2)}
    for m in range(K):
        p = F(3,2)**m                      # (3/2)^m xi = half-integer  =>  xi = (j+1/2)/p
        lo, hi = p*1, p*2
        j = int(lo - 1)
        while True:
            x = (F(j) + F(1,2)) / p
            if x >= 2: break
            if 1 < x < 2: cuts.add(x)
            j += 1
    xs = sorted(cuts)
    n = len(xs) - 1
    tot = F(0)
    for a, b in zip(xs, xs[1:]):
        mid = (a + b) / 2
        NK = F(3,2)**K * mid
        # the cell's image length under xi -> (3/2)^K xi
        tot += (b - a) * F(3,2)**K
    g = F(3,2)**K
    print(f"{K:>3} {n:>8} {float(g):>10.2f} {n/float(g):>16.4f} {float(tot):>12.4f} {float(tot/g):>10.6f}")
print()
print("mean width = (sum width)/#cells should approach 1/3 = 0.3333")
