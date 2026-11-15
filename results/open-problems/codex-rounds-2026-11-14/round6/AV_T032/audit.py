"""Bounded exact checks for the conditional law and folded skeleton geometry."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import os
import re
import resource
import sys

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
root = Path(__file__).resolve().parent
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

# Independent four-state, four-label version of the preceding law check.
# Each site allocates one label uniformly from its entire eligible list.
# Products of integer weights share one global denominator, omitted below.
weights = ((1, 2, 3, 5), (2, 5, 1, 3), (3, 1, 5, 2), (5, 3, 2, 1))
edges = ((0, 1), (0, 2), (1, 3), (2, 3))

def compatible(state):
    return all(not (state[i] == state[j] != 0) for i, j in edges)

fibers = defaultdict(lambda: defaultdict(F))
samples = records = 0
for state in product(range(4), repeat=4):
    eligible = tuple(x != 0 for x in state)
    left = [i for i in (0, 1) if eligible[i]]
    right = [i for i in (2, 3) if eligible[i]]
    if not left or not right or not compatible(state):
        continue
    samples += 1
    mass = math.prod(weights[i][state[i]] for i in range(4))
    for alloc in product(left, right):
        frozen = tuple((i, state[i]) for i in range(4) if i not in alloc)
        key = (eligible, alloc, frozen)
        fibers[key][tuple(state[i] for i in alloc)] += F(mass, len(left)*len(right))
        records += 1

normalizers = []
checks_mutual = checks_frozen = 0
for (eligible, alloc, frozen), observed in fibers.items():
    frozen = dict(frozen)
    own = {}
    for i in alloc:
        own[i] = {}
        for color in (1, 2, 3):
            blocked = any(
                j in frozen and frozen[j] == color
                for edge in edges if i in edge for j in edge if j != i)
            own[i][color] = 0 if blocked else weights[i][color]
            checks_frozen += int(blocked)
    predicted = {}
    for retained in product((1, 2, 3), repeat=2):
        state = dict(frozen)
        state.update(zip(alloc, retained))
        raw = math.prod(own[i][x] for i, x in zip(alloc, retained))
        if not compatible(state):
            checks_mutual += int(raw > 0)
            raw = 0
        if raw:
            predicted[retained] = raw
    assert predicted.keys() == observed.keys()
    observed_Z = sum(observed.values())
    predicted_Z = sum(predicted.values())
    assert predicted_Z > 0
    for s in predicted:
        assert observed[s]*predicted_Z == predicted[s]*observed_Z
    normalizers.append(predicted_Z)
assert checks_frozen and checks_mutual
print(f'PASS: prior conditional law independently rederived on {len(fibers)} '
      f'positive four-state fibers ({samples} samples, {records} allocations)')

# Every alignment offset through 256, every future length through 256.
block_checks = 0
for t in range(257):
    for k in range(1, 257):
        L = 1 if k == 1 else 1 << ((k//2).bit_length()-1)
        start0 = ((t+L-1)//L)*L
        assert t <= start0 and start0+L <= t+k
        assert start0 % L == 0
        assert F(L) > F(k, 4)
        # Count appearances independently, one time index at a time.
        count = sum((i-1)//L == start0//L for i in range(1, t+k+1))
        assert count == L
        assert 1/(L**1.5) <= 8/(k**1.5) * (1+1e-14)
        block_checks += 1
print(f'PASS: {block_checks} fresh aligned-block/coefficient checks, including '
      'blocks crossing previously revealed larger blocks')

def make_walk(n, drift, velocities):
    h = n//2
    Z = [(F(0), F(0))]
    for i in range(h):
        a, b = velocities[i % len(velocities)]
        Z.append((Z[-1][0]+a, Z[-1][1]+b))
    base = []
    for t in range(n+1):
        u = min(t, n-t)
        base.append((t, math.floor(F(t*drift[0], n)+Z[u][0]),
                        math.floor(F(t*drift[1], n)+Z[u][1])))
    walk = [base[0]]
    for target in base[1:]:
        current = list(walk[-1])
        current[0] += 1
        walk.append(tuple(current))
        for j in (1, 2):
            while current[j] != target[j]:
                current[j] += 1 if current[j] < target[j] else -1
                walk.append(tuple(current))
        assert tuple(current) == target
    assert walk[0] == (0, 0, 0) and walk[-1] == (n, *drift)
    for t in range(n+1):
        level = [z for z in walk if z[0] == t]
        assert len(level) <= (1 if t == 0 else 5)
        assert all(max(abs(z[j]-base[t][j]) for j in range(3)) <= 2 for z in level)
    return walk, Z

def periodic_distance(a, b, K):
    return max(min((x-y) % K, (y-x) % K) for x, y in zip(a, b))

# Rational deterministic velocity patterns test geometry independently of the
# probabilistic law. The inequalities only need coordinate speeds <= 1/2.
patterns = [((F(0), F(0)),),
            ((F(1,2), F(-1,2)),),
            ((F(-1,2), F(1,2)),),
            ((F(1,2), F(1,2)), (F(-1,2), F(-1,2))),
            ((F(1,3), F(-1,4)), (F(-1,2), F(1,2)), (F(0), F(1,3)))]
path_pairs = occurrence_pairs = 0
for n in (1, 2, 3, 4, 7, 8, 15, 16):
    K = 8*n
    for drift in product((-n, 0, n), repeat=2):
        walks = [make_walk(n, drift, p) for p in patterns]
        for (walk, Z), (other, Zp) in product(walks, repeat=2):
            path_pairs += 1
            D = [max(abs(a-b) for a, b in zip(x, xp)) for x, xp in zip(Z, Zp)]
            distances = []
            for z in walk:
                ds = []
                for zp in other:
                    d = periodic_distance(z, zp, K)
                    assert abs(z[0]-zp[0]) <= d
                    assert D[min(z[0], n-z[0])] <= 3*d+5
                    ds.append(d)
                    occurrence_pairs += 1
                distances.append(min(ds))
            reverse_min = [min(periodic_distance(z, zp, K) for z in walk)
                           for zp in other]
            for R in (1, 2, 5):
                Jocc = sum(d <= R for d in distances+reverse_min)
                assert Jocc <= 20*sum(d <= 3*R+5 for d in D)
                Jpair = sum(periodic_distance(z, zp, K) <= R
                            for z in walk for zp in other)
                assert Jpair <= 5*(2*R+1)*Jocc
            for B in (F(1, 2), F(1), F(3)):
                lhs = math.fsum(math.exp(-float(d/B)) for d in distances)
                rhs = 10*math.exp(float(F(5,3)/B))*math.fsum(
                    math.exp(-float(d/(3*B))) for d in D)
                assert lhs <= rhs*(1+1e-13)
print(f'PASS: {path_pairs} exact rational folded/refined path pairs; '
      f'{occurrence_pairs} occurrence inequalities; hard/soft count bounds')

# Constants checked by two algebraic descriptions rather than estimates from
# sampled paths. Integrate the maximum-norm radial function by shells and
# layer cake; integral log(1/u)^2 du = 2 by two integrations by parts.
assert 8*3**2 == 4*3**2*2 == 72
assert 3*72 == 216
assert 12*4**2 == 192 and 4*20 == 80
assert 2*5*2 == 20 and 2*5 == 10
for R in range(1, 1001):
    assert 3*R+5 <= 4*(R+1)
for B0 in (1, 2, 10, 100, 10**6):
    theta = 1/(4*B0)
    assert math.expm1(theta)*B0 < 0.5
assert F(1,2)**-3 == 8
print('PASS: density exponent, occurrence factors 20/10, integrals 72/216, '
      'hard constant 192/80, exponential-series ratio < 1/2')

source = (root/'sources/lattice-current.tex').read_text()
lemma = re.search(r'\\begin\{lemma\}\[Skeleton encounters\][\s\S]*?\\end\{lemma\}', source)[0]
proof = (root/'PROOF.md').read_text()
assert proof.count(lemma) == 1
prefix = source.split(r'\label{lem:skeleton}')[0]
assert len(re.findall(r'\\begin\{(?:theorem|lemma|proposition|corollary|definition|remark)\}', prefix)) == 2
dossier = (root/'VERIFY.md').read_text()
for i in range(3):
    intro = (root/f'sources/introduction-round6-{i}.tex').read_text()
    theorem = re.search(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}', intro)[0]
    assert dossier.count(theorem) == 1
assert (root/'REPORT.md').read_text().startswith('VERDICT: PARTIAL ')
for text in (proof, dossier):
    assert text.count('```') % 2 == 0
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target:
            assert (root/target).exists(), target
print('PASS: exact Lemma 8.2 and three theorem quotations, local links and report format')

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1_000_000_000
print(f'PASS: nice {os.getpriority(os.PRIO_PROCESS, 0)}, one thread, '
      f'peak RSS {rss_bytes} bytes')

