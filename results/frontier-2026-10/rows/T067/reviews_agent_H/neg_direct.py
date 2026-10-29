# Direct evaluation: shifted K (g24 - 1/10) goes negative on the domain; the true K stays >= 0 at the same points.
import random, sys
from fractions import Fraction as Fr
import cert_b1e as C
rng = random.Random(18)
best = None
for t in range(int(sys.argv[1]) if len(sys.argv) > 1 else 4000):
    a, _, _ = C.point([rng.random() ** 3 for _ in range(4)], rng.randint(0, 1))
    b, _, _ = C.point([rng.random() ** 3 for _ in range(4)], rng.randint(0, 1))
    m = float(C.M_END) if t % 2 else 0.0
    ks = float(C.K_direct(a, b, m, Fr(-1, 10)))
    if best is None or ks < best[0]:
        best = (ks, float(C.K_direct(a, b, m)), a, b, m)
print('min shifted K %.6g ; true K at that point %.6g ; m %s' % (best[0], best[1], best[4]))
print('a', [round(x, 4) for x in best[2]], 'b', [round(x, 4) for x in best[3]])
# exact recheck at the minimiser, rationalised
a = [Fr(x).limit_denominator(10**6) for x in best[2]]; b = [Fr(x).limit_denominator(10**6) for x in best[3]]
m = Fr(best[4]).limit_denominator(10**16) if best[4] else Fr(0)
print('exact shifted', float(C.K_direct(a, b, C.M_END if best[4] else Fr(0), Fr(-1, 10))), 'exact true', float(C.K_direct(a, b, C.M_END if best[4] else Fr(0))))
