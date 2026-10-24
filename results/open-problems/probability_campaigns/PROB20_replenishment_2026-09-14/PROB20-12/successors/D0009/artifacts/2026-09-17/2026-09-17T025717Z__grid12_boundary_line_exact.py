#!/usr/bin/env python3
from fractions import Fraction as Q
from itertools import combinations_with_replacement

D = 12
S = Q(1,1)

# Each interval is represented by integer endpoints (l,r) meaning [l/D,r/D].
intervals = [(l,r) for l in range(D) for r in range(l+1,D+1)]

def valid_atom(t):
    # center sum = S iff sum(l+r)/(2D)=S
    if sum(l+r for l,r in t) != 2*D*S:
        return False
    w = sorted(r-l for l,r in t)
    # one-uniform line coupling criterion: largest width = sum of other two
    return w[2] == w[0] + w[1]

atoms = [t for t in combinations_with_replacement(intervals,3) if valid_atom(t)]
assert len(atoms) == 511

def density_on_cell(t,k):
    # Exchangeabilized branch marginal density on cell k/D < x < (k+1)/D.
    mid = Q(2*k+1,2*D)
    ans = Q(0)
    for l,r in t:
        if Q(l,D) < mid < Q(r,D):
            ans += Q(D,3*(r-l))
    return ans

A = [[density_on_cell(t,k) for t in atoms] for k in range(D)]

# Sparse exact certificates discovered numerically, then solved and verified over Q.
# Key j means a=j/12, boundary center m=2/3, target sum 1.
CERT = {
  1: [
    (0,Q(5,22)),(3,Q(2,11)),(39,Q(2,11)),(52,Q(1,11)),(55,Q(1,22)),
    (61,Q(3,22)),(62,Q(2,33)),(85,Q(7,132)),(88,Q(1,44))
  ],
  2: [
    (1,Q(1347,163354)),(15,Q(4041,163354)),(66,Q(35520,81677)),
    (71,Q(20615,81677)),(119,Q(7800,81677)),(146,Q(7320,81677)),
    (161,Q(3424,81677)),(175,Q(1712,81677)),(426,Q(2592,81677))
  ],
  3: [
    (1,Q(125,15534)),(15,Q(125,5178)),(71,Q(560,7767)),(125,Q(5755,7767)),
    (403,Q(500,7767)),(500,Q(39,863)),(506,Q(39,863))
  ],
  4: [(0,Q(1,4)),(407,Q(3,4))],
  5: [(66,Q(1,3)),(71,Q(1,6)),(499,Q(1,2))],
  6: [
    (3,Q(2,51)),(126,Q(35,68)),(146,Q(1,102)),(175,Q(5,204)),
    (284,Q(43,136)),(405,Q(1,34)),(430,Q(9,136))
  ],
  7: [
    (1,Q(51247,682230)),(15,Q(14319,227410)),(71,Q(668507,5116725)),
    (127,Q(18464,1023345)),(163,Q(78772,1023345)),(236,Q(1045688,5116725)),
    (296,Q(298768,1023345)),(426,Q(9756,113705)),(474,Q(18464,341115))
  ],
}

def target_density(j,k):
    a = Q(j,D)
    low = (Q(1,3)+a)/a
    high = (Q(2,3)-a)/(1-a)
    return low if k < j else high

for j, cert in CERT.items():
    assert all(w > 0 for _,w in cert)
    assert sum(w for _,w in cert) == 1
    got = []
    for k in range(D):
        got.append(sum(w*A[k][idx] for idx,w in cert))
    want = [target_density(j,k) for k in range(D)]
    assert got == want, (j,got,want)

    # Exact mean and mass from cellwise target density.
    mass = sum(got) / D
    mean = sum(got[k]*Q(2*k+1,2*D*D) for k in range(D))
    assert mass == 1
    assert mean == Q(1,3)

    # Every support atom itself has the exact line-coupling identities.
    for idx,w in cert:
        t = atoms[idx]
        widths = sorted(Q(r-l,D) for l,r in t)
        centers = [Q(l+r,2*D) for l,r in t]
        assert widths[2] == widths[0] + widths[1]
        assert sum(centers) == 1

# B12 conservation law for every atom: the exchangeabilized marginal has mass 1
# and mean 1/3. Check directly from exact cell densities (endpoints are null).
for t in atoms:
    d = [density_on_cell(t,k) for k in range(D)]
    assert sum(d)/D == 1
    assert sum(d[k]*Q(2*k+1,2*D*D) for k in range(D)) == Q(1,3)

# Grid-parity warning: for an integer-grid boundary-line atom,
# sum(l_i+r_i) is even because after orienting w3=w1+w2 it equals
# 2*(l1+l2+l3+w1+w2). Verify across the enumerated library.
assert all(sum(l+r for l,r in t) % 2 == 0 for t in atoms)

print("GRID_DENOMINATOR", D)
print("UNORDERED_S3_ORBIT_REPRESENTATIVES", len(atoms))
for j in sorted(CERT):
    print("BOUNDARY_BREAKPOINT", f"{j}/{D}",
          "SUPPORT", len(CERT[j]),
          "WEIGHT_SUM", sum(w for _,w in CERT[j]),
          "EXACT_MARGINAL_PASS")
print("B12_MASS_MEAN_CONSERVATION PASS")
print("GRID_PARITY_INVARIANT PASS")
print("ALL EXACT CHECKS PASSED")
