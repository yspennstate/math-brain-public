"""Independent finite checks; these do not prove stochastic limit statements."""
from fractions import Fraction as F
from pathlib import Path

recurrences = endpoints = lower_bounds = 0
for q in range(2, 13):
    for L in range(2, 46):
        def f(r):
            return (F(1, q**r) - F(1, q**L)) / (1 - F(1, q**L))
        assert f(0) == 1 and f(L) == 0
        endpoints += 2
        for r in range(1, L):
            assert f(r) == (f(r-1) + q*f(r+1))/(q+1)
            assert 0 < f(r) < 1
            recurrences += 1
    # Exact exit probability: at v, symmetry of incoming branches gives
    # h(v)=q/(q+1); at depth d below v, first hit v has probability q^-d.
    for d in range(50):
        exact = 1 - F(1, (q+1)*q**d)
        claimed = 1 - F(1, q**(d+1))
        assert exact >= claimed
        lower_bounds += 1

# Check the truncation inequality on all assignments Y<=Z for a finite grid.
# Pointwise: Y <= K*1_{Y>0} + Z*1_{Z>K}.
truncations = 0
for K in [F(1,2), F(1), F(3), F(10)]:
    for zi in range(81):
        z = F(zi,4)
        for yi in range(zi+1):
            y = F(yi,4)
            assert y <= K*(y>0) + z*(z>K)
            truncations += 1

out = (f'PASS: {recurrences} exact radial recurrence/interior checks; '
       f'{endpoints} endpoint checks; {lower_bounds} cylinder lower bounds; '
       f'{truncations} pointwise truncation checks.\n'
       'No simulation or finite computation certifies the infinite-time proof.\n')
Path(__file__).with_name('exact_checks.txt').write_text(out, encoding='utf-8')
print(out)
