# Check of A021 v1 section 2: sign of R(q) := -2(1-q)^2 log2(1-q) - (2cq - 3cq^2), c = log2(e).
# A021 states R(q) = -4c sum_{j>=3} q^j/[j(j-1)(j-2)] and -2cq^3/[3(1-q)] <= R(q) <= 0.
from mpmath import mp, mpf, log, nsum, inf
mp.dps = 50
c = 1/log(2)
rows = []
for q in [mpf(1)/2, mpf(1)/4, mpf(1)/16, mpf(1)/256]:
    R = -2*(1-q)**2*log(1-q)/log(2) - (2*c*q - 3*c*q**2)
    S = nsum(lambda j: q**j/(j*(j-1)*(j-2)), [3, inf])
    rows.append((float(q), float(R), float(4*c*S), float(2*c*q**3/(3*(1-q)))))
for u in [mpf(1)/4, mpf(1)/8, mpf(1)/64]:
    Rf = lambda x: -2*(1-x)**2*log(1-x)/log(2) - (2*c*x - 3*c*x**2)
    G = Rf(u) - Rf(2*u)/2
    rows.append(('G_s at u', float(u), float(G)))
for r in rows: print(r)
