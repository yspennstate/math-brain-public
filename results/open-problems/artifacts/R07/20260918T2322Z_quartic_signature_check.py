from fractions import Fraction
from itertools import product
from collections import Counter

# Exact self-check for the dyadic Takagi template
# F(t)=sum_{m>=0} 2^{-m/2} dist(2^m t, Z).
# At dyadic level N, Delta_k F = 2^{-N} sum_{m<N} 2^{m/2} r_m(k).
# Walsh averaging kills every monomial in which some Rademacher index
# occurs an odd number of times.  The surviving weights are integral
# powers of 2, so all checks below use Fraction/integer arithmetic only.

def direct_qv(N):
    total = 0
    for i, j in product(range(N), repeat=2):
        if i == j:
            total += 1 << i
    return Fraction(total, 1 << N)


def direct_quarticity(N):
    total = 0
    for inds in product(range(N), repeat=4):
        counts = Counter(inds)
        if all(v % 2 == 0 for v in counts.values()):
            s = sum(inds)
            assert s % 2 == 0
            total += 1 << (s // 2)
    return Fraction(total, 1 << (2 * N))


for N in range(1, 13):
    qv = direct_qv(N)
    rq = direct_quarticity(N)
    qv_closed = Fraction((1 << N) - 1, 1 << N)
    rq_closed = Fraction(7, 3) - Fraction(6, 1 << N) + Fraction(11, 3 * (1 << (2 * N)))
    assert qv == qv_closed
    assert rq == rq_closed
    print(f"N={N:2d} qv={qv} quarticity={rq}")

print("LIMITS: qv -> 1 ; quarticity -> 7/3")
print("BROWNIAN QUARTICITY BENCHMARK: 3")
print("EXACT_GAP: 3 - 7/3 = 2/3")
print("PASS")
