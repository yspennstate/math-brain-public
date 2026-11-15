"""Exact, small checks accompanying PROOF.md. Standard library; one process."""
from collections import deque, defaultdict
from fractions import Fraction as F
from itertools import product
from math import prod
import os
import resource
import sys
import time

start = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

# Independent check of the earlier coefficient and decomposition, using
# successive one-coordinate integration rather than the earlier atom code.
p = (F(1, 3), F(2, 5), F(3, 7))
small = list(product((0, 1), repeat=3))
small_w = {a: prod(p[i] if a[i] else 1-p[i] for i in range(3)) for a in small}

def integrate(f, i):
    out = {}
    for a in small:
        a0, a1 = list(a), list(a)
        a0[i], a1[i] = 0, 1
        out[a] = (1-p[i])*f[tuple(a0)]+p[i]*f[tuple(a1)]
    return out

def tensor_projection(f, mask):
    out = f.copy()
    for i in range(3):
        averaged = integrate(out, i)
        out = {a: out[a]-averaged[a] for a in small} if mask >> i & 1 else averaged
    return out

for atom in small:
    f = {a: F(a == atom) for a in small}
    parts = [tensor_projection(f, mask) for mask in range(8)]
    assert all(sum(g[a] for g in parts) == f[a] for a in small)
    for mask in range(1, 8):
        assert sum(small_w[a]*parts[mask][a] for a in small) == 0
        assert sum(small_w[a]*abs(parts[mask][a]) for a in small) <= 2**mask.bit_count()*small_w[atom]
print('Earlier lemma: tensor decomposition, means and L1 norms on all 8 biased atom functions PASS')

earlier_coefficient = 2*73*73*163
assert earlier_coefficient == 1737254
assert 25+81 == 106
assert 2+earlier_coefficient*2**106 == 140942788854329116202736232342545760258
print('Earlier C_2 coefficient and integer value independently reproduced PASS')

for h in (2, 3, 5):
    r, ell = 8*h+20, 2*(8*h+20)+4*h+22
    boundary = {(x, y) for x in range(-r, r+1) for y in (-r, r)}
    boundary |= {(x, y) for x in (-r, r) for y in range(-r, r+1)}
    distances, queue = {(r, 0): 0}, deque([(r, 0)])
    while queue:
        u = queue.popleft()
        for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = u[0]+d[0], u[1]+d[1]
            if v in boundary and v not in distances:
                distances[v] = distances[u]+1
                queue.append(v)
    assert len(distances) == 8*r
    maxima = []
    for axis in (0, 1):
        maximum = 0
        for k in product(range(-r, r+1), repeat=2):
            entry = (-r, -k[1]) if axis == 0 else (-k[0], -r)
            first_length = ell+k[axis]-r
            assert first_length >= 0
            length = first_length+distances[entry]+4*h+10
            maximum = max(maximum, length)
            assert length+1 <= ell+4*r+4*h+11
        maxima.append(maximum)
    assert r > 3*h
    print(f'H={h}: all {(2*r+1)**2} centers, two baseline directions: maxima {maxima}; J={ell+4*r+4*h+11}; separation PASS')

assert 2*36+4*2+22 == 102
assert 102+4*36+4*2+11 == 265
assert 73**2*(102+265) == 1955743
print('New H=2 constants: L=102, J=265, C_common=5329*(102+265*K)*2^106 PASS')

# Three worlds share some exterior coordinates, but each world's own
# exterior is a product with the same marginal law, independent of a.
probabilities = p+(F(4, 9),)*5
states = list(product((0, 1), repeat=8))
weights = {a: prod(probabilities[i] if a[i] else 1-probabilities[i] for i in range(8)) for a in states}
assert sum(weights.values()) == 1
worlds = ((3, 4, 5), (3, 6, 7), (6, 4, 7))
q = {a: F(a[0]+2*a[1]-3*a[2]+5*a[0]*a[1]-7*a[0]*a[2]+11*a[0]*a[1]*a[2]) for a in states}

def conditional(f, indices):
    masses, totals = defaultdict(F), defaultdict(F)
    for a in states:
        key = tuple(a[i] for i in indices)
        masses[key] += weights[a]
        totals[key] += weights[a]*f[a]
    return {a: totals[tuple(a[i] for i in indices)]/masses[tuple(a[i] for i in indices)] for a in states}

incoming = {mask: conditional(q, [i for i in range(3) if mask >> i & 1]) for mask in range(8)}
all_projections = []
for exterior in worlds:
    cond = {}
    for mask in range(8):
        indices = [index for i in range(3) if mask >> i & 1 for index in (i, exterior[i])]
        cond[mask] = conditional(q, indices)
        assert cond[mask] == incoming[mask]
    projections = {}
    for mask in range(1, 8):
        projections[mask] = {a: sum(((-1)**(mask.bit_count()-sub.bit_count())*cond[sub][a] for sub in range(8) if sub & mask == sub), F(0)) for a in states}
        assert sum(weights[a]*projections[mask][a] for a in states) == 0
    all_projections.append(projections)
assert all(x == all_projections[0] for x in all_projections)
print('3 coupled worlds: all 24 conditional expectations and 21 nonempty projections are identical incoming functions PASS')

means = []
for exterior in worlds:
    def calibrated_anchor(a):
        x = a[0] ^ a[1]
        return (2*x-1)*(a[exterior[0]]+2*a[exterior[1]]+4*a[exterior[2]])+x*a[2]
    means.append(sum(weights[a]*calibrated_anchor(a) for a in states))
assert means[0] == means[1] == means[2]
print(f'Random-anchor same-map mean in each world = {means[0]} PASS')

# Deliberately break the own-input restriction: a projected exterior
# coordinate differs between worlds 0 and 2. This must fail to be common.
bad0 = {a: F(a[worlds[0][0]])-F(4, 9) for a in states}
bad2 = {a: F(a[worlds[2][0]])-F(4, 9) for a in states}
bad_distance = sum(weights[a]*abs(bad0[a]-bad2[a]) for a in states)
assert bad_distance == F(40, 81) > 0
print(f'Negative control: exterior-dependent projection differs by L1={bad_distance}, as required')

# Independent supports imply factorization for arbitrary incoming functions.
f = {a: F(a[0]+2*a[1]*a[2]) for a in small}
g = {a: F(5*a[0]-3*a[1]+a[0]*a[2]) for a in small}
ef = sum(small_w[a]*f[a] for a in small)
eg = sum(small_w[a]*g[a] for a in small)
efg = sum(small_w[a]*small_w[b]*f[a]*g[b] for a in small for b in small)
assert efg == ef*eg
print('Disjoint incoming blocks: exact mixed-moment factorization PASS')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024**2 if sys.platform == 'darwin' else 1024)
assert rss < 768
print(f'Elapsed {time.monotonic()-start:.3f} seconds; peak RSS {rss:.2f} MiB; inherited nice {os.getpriority(os.PRIO_PROCESS, 0)}')
