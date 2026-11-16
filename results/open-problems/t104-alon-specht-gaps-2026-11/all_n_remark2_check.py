"""From which n do the constants of Step 3 close?  (an agent, 11 Nov 2026, after the Codex referee)

Printed constants: Y2 <= 0.002, T <= 2.002, first term below 1/100 of the main term, second below 37.9 (n-2).
Repaired constants: Y2 <= 0.005, T <= 2.005, first term below 1/50 of the main term.
Exact rationals.  D = (n-1)^2 (n^2-6n+6)/(n+1) is the main coefficient per unit eps (T >= 1).
"""
from fractions import Fraction as F


def closes(n, y, share):
    e1 = F(21, 10) / (n * (n - 1))
    e2 = F(2) / ((n - 2) * (n + 1))
    D = F((n - 1) ** 2 * (n * n - 6 * n + 6), n + 1)
    ymax = (n - 2) * e1 * e1
    c1 = ymax <= y
    first = (4 + y) * (n - 4) * (n - 2) * e1 <= share * D
    second = 2 * (n - 3) * (3 * (n - 2) + y) ** 2 * e1 <= F(379, 10) * (n - 2)
    third = (1 - share) * D >= F(379, 10) * (n - 2)
    step2 = e2 <= e1 and (n - 2) * e1 * e1 - n * (n - 1) * e1 + 2 <= 0
    return c1, first, second, third, step2


for name, y, share in (("printed (0.002, 1/100)", F(2, 1000), F(1, 100)), ("repaired (0.005, 1/50)", F(5, 1000), F(1, 50))):
    ok = [n for n in range(5, 3001) if all(closes(n, y, share))]
    bad = [n for n in range(5, 3001) if not all(closes(n, y, share))]
    print(name, ": closes for n in", (min(ok), max(ok)), "fails for n =", bad)
    for n in (9, 10, 11, 12, 13):
        print("   n=%d  Y2max<=y %s  first %s  second %s  third %s  step2 %s" % ((n,) + closes(n, y, share)))
# the referee's vector at n = 10
x = [F(1)] + [F(7, 300)] * 4 + [F(-7, 300)] * 4 + [F(-1)]
print("n = 10 vector: sum", sum(x), " eps = e1:", x[1] == F(21, 10) / 90, " Y2 =", sum(v * v for v in x[1:-1]), " > 1/500:", sum(v * v for v in x[1:-1]) > F(1, 500))
