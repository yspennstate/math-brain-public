from decimal import Decimal, getcontext
from itertools import combinations
import numpy as np

getcontext().prec = 50

T0 = Decimal(8192) / Decimal(31)
d = Decimal("0.10429071727552326290")
r1 = Decimal(2).sqrt() * d
c2 = (T0 - d*d) / Decimal(2)
eps = Decimal(2) ** Decimal(-16)
delta = c2 * eps**4 / Decimal(3)
C_E3 = Decimal("8.4530212255281768747049")
density = C_E3 * delta ** (Decimal(-1) / Decimal(6))
pstar = Decimal("1.19876993884320")
z2 = pstar*pstar
z2del = z2/Decimal(3)

print("T0 =", T0)
print("d* =", d)
print("sqrt(2)d* =", r1)
print("c2 =", c2)
print("delta_E3 =", delta)
print("density_E3 =", density)
print("pstar^2 =", z2)
print("pstar^2/3 =", z2del)

assert density < Decimal(7312)
assert d > Decimal(1)/Decimal(64)
assert z2del > Decimal("0.479")
assert c2 > Decimal(132)

rng = np.random.default_rng(20260924)
max_sum_beta = 0.0
max_delete_error = 0.0
max_heavy = 0
trials = 1000
for _ in range(trials):
    rows = 5
    npairs = 6
    cols = 2*npairs
    M = rng.normal(size=(rows, cols))
    weights = {}
    Z = 0.0
    for a,b in combinations(range(cols),2):
        w=0.0
        for i,j in combinations(range(rows),2):
            det = M[i,a]*M[j,b]-M[i,b]*M[j,a]
            w += det*det
        weights[(a,b)] = w
        Z += w
    betas=[]
    for k in range(npairs):
        block={2*k,2*k+1}
        lost=sum(w for J,w in weights.items() if block.intersection(J))
        beta=lost/Z
        betas.append(beta)
        keep=[j for j in range(cols) if j not in block]
        Zd=sum(weights[tuple(sorted((a,b)))] for a,b in combinations(keep,2))
        max_delete_error=max(max_delete_error, abs(Zd-Z*(1-beta))/max(1.0,Z))
    max_sum_beta=max(max_sum_beta,sum(betas))
    max_heavy=max(max_heavy,sum(b>2/3 for b in betas))
assert max_sum_beta <= 2.0 + 1e-12
assert max_heavy <= 2
assert max_delete_error < 1e-12
print("pair_block_trials =", trials)
print("max_sum_beta =", format(max_sum_beta, ".15g"))
print("max_heavy_count =", max_heavy)
print("max_relative_delete_identity_error =", format(max_delete_error, ".3e"))
print("STATUS=PASS")
