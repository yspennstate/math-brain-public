# Independent partial review of A006 (sunflower spectrum and elementary chains) and A007 (root normalizer delta).
import sys, math, random
from fractions import Fraction
sys.path.insert(0, sys.argv[2])
from check_single_gate_lib import fwht_int
out = []
def say(s):
    print(s); out.append(s)
say("A006 sunflower f_m = x0 AND OR(x1..xm), true=-1: exact FWHT spectrum vs claimed closed form")
for m in range(1, 11):
    n = m + 1
    tt = []
    for x in range(1 << n):
        t = (x & 1) and (x >> 1) != 0
        tt.append(-1 if t else 1)
    co = fwht_int(tt); N = 1 << n
    P = [Fraction(c * c, N * N) for c in co]
    ok = P[0] == Fraction(1, 4 ** m) and P[1] == (1 - Fraction(1, 2 ** m)) ** 2
    for A in range(2, 1 << n):
        if (A >> 1) == 0: continue
        if P[A] != Fraction(1, 4 ** m): ok = False
    I = sum(P[A] * bin(A).count('1') for A in range(1 << n))
    say(f" m={m}: spectrum claim {ok}; I = 1+(m-1)2^-m: {I == 1 + Fraction(m - 1, 2 ** m)}")
g = lambda m: Fraction(1, 2 ** m) * (m * m + Fraction(11, 5) * m + Fraction(4, 5))
Q = lambda m: m * m + 9 * m + 5
mx = max(g(m) for m in range(1, 400)); arg = max(range(1, 400), key=g)
say(f"A006 chain (i): max_m 2^-m[m^2+11m/5+4/5] over 1..399 = {mx} at m={arg}; <= 23/10: {mx <= Fraction(23, 10)}; ratio step g(m+1)<=g(m) iff m^2+m/5-12/5>=0, true for m>=2")
say(f"A006 chain (ii): Q(m)=m^2+9m+5 <= (15/2)2^m for m=1..399: {all(Q(m) <= Fraction(15, 2) * 2 ** m for m in range(1, 400))}; equality at m=1: {Q(1) == Fraction(15, 2) * 2}; induction step Q(m+1)<=2Q(m) iff m^2+7m-5>=0, true m>=1")
Ds = [(1 + Fraction(1, 4 * m)) ** m - 1 for m in range(1, 60)]
say(f"A006 D_m=(1+1/(4m))^m-1: D_1={Ds[0]}, nondecreasing over 1..59: {all(Ds[i] <= Ds[i+1] for i in range(len(Ds)-1))}, all in [1/4,1/3): {all(Fraction(1,4) <= d < Fraction(1,3) for d in Ds)}; limit e^(1/4)-1={math.exp(0.25)-1:.6f}")
rng = random.Random(7); worst_lo = 1e9; worst_hi = -1e9
for _ in range(20000):
    N = rng.randint(1, 30)
    x = [rng.random() ** rng.choice([1, 3, 8]) * rng.choice([1, 0.1, 0.01]) for _ in range(N)]
    x = [max(t, 1e-9) for t in x]
    a = sum(x); D = math.prod(1 + t for t in x) - 1
    delta = math.log2(D) - math.log2(a)
    worst_lo = min(worst_lo, delta); worst_hi = max(worst_hi, delta - a * math.log2(math.e))
say(f"A007 root normalizer: 0 <= delta = log D - log a <= a log e on 20000 random tables: min delta={worst_lo:.3e}, max(delta - a log e)={worst_hi:.3e}; analytic: D>=a (expand product), D<=e^a-1<=a e^a")
open(sys.argv[1], 'w', encoding='utf-8').write("\n".join(out) + "\n")
