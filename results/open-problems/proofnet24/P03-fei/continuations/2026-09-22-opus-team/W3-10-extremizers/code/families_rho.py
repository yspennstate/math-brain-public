"""rho_0 and composition-primality on structured families (search for prime functions with large rho_0)."""
import sys, itertools
import numpy as np
sys.path.insert(0, '.')
from core import polite, stats, is_prime, tt_from_pred, find_blocks, decompose
from structure import max_coin_set
polite()
out = open('../logs/families_rho.log', 'w')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()

def dnf(n, terms):
    return tt_from_pred(n, lambda b: any(all(b[i] for i in T) for T in terms))

def report(name, t, check_prime=True):
    s = stats(t)
    pr = is_prime(t) if check_prime else None
    log('%-44s n=%2d  rho0=%.5f  H/I=%.5f  mean=%+.4f  maxInf=%.4f  prime=%s' % (name, s['n'], s['rho0'], s['ratio'], s['mean'], s['Inf'].max(), pr))
    return s

# width-2 tribes (composite) as reference
for sN in (4, 5, 6, 7):
    n = 2 * sN
    report('tribes w2 s%d (reference, composite)' % sN, dnf(n, [(2*i, 2*i+1) for i in range(sN)]))
# cycle 2-DNF and path 2-DNF
for n in range(6, 17, 2):
    report('cycle 2-DNF C_%d' % n, dnf(n, [(i, (i+1) % n) for i in range(n)]))
for n in (8, 12, 16):
    report('path 2-DNF P_%d' % n, dnf(n, [(i, i+1) for i in range(n-1)]))
# cycle of triangles-ish: 3-DNF on sliding windows
for n in (9, 12, 15):
    report('cycle 3-DNF windows n=%d' % n, dnf(n, [(i, (i+1) % n, (i+2) % n) for i in range(n)]))
# disjoint-pair tribes with each variable in two terms: 2-DNF of a 2-regular graph = union of cycles
for L in (3, 4, 5):
    k = 12 // L
    terms = []
    for c in range(k):
        base = c * L
        terms += [(base + i, base + (i + 1) % L) for i in range(L)]
    report('union of %d disjoint C_%d (composite OR)' % (k, L), dnf(12, terms))
# graph properties on K_5 (10 edge variables)
E5 = list(itertools.combinations(range(5), 2))
tri = [tuple(E5.index(e) for e in itertools.combinations(T, 2)) for T in itertools.combinations(range(5), 3)]
report('K5 has a triangle (10 vars)', dnf(10, tri))
# star of degree >= 3 at some vertex in K5 (monotone)
stars = []
for v in range(5):
    inc = [E5.index(tuple(sorted((v, u)))) for u in range(5) if u != v]
    for T in itertools.combinations(inc, 3):
        stars.append(T)
report('K5 has a vertex of degree>=3', dnf(10, stars))
# 4-cycles / matchings in K_{3,4}? use 'contains a matching of size 2' on K_{2,4} (8 vars)
# Fano plane lines DNF (7 vars)
fano = [(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
report('Fano lines 3-DNF (7 vars)', dnf(7, fano))
# one-point flips of tribes (prime? close to composite)
for sN in (5, 6, 7):
    n = 2 * sN
    t = dnf(n, [(2*i, 2*i+1) for i in range(sN)])
    for x in (0, (1 << n) - 1, int('01' * sN, 2)):
        t2 = t.copy(); t2[x] = -t2[x]
        report('tribes w2 s%d with point %s flipped' % (sN, format(x, 'b')[:6] + '..'), t2)
