#!/usr/bin/env python3
"""Bounded checks for the feasibility-loss proof; not a test of a CLT."""
import json
import math
import os
import resource
import time
from collections import Counter, defaultdict
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
getcontext().prec = 90


def dec(x):
    x = F(x)
    return D(x.numerator)/D(x.denominator)


def graph_info(n, g):
    edges = list(combinations(range(n), 2))
    adj = [0]*n
    for e, (u, v) in enumerate(edges):
        if (g >> e) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    todo = (1 << n)-1
    components = []
    while todo:
        frontier = todo & -todo
        comp = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length()-1
            comp |= bit
            todo &= ~bit
            frontier |= adj[v] & todo & ~comp
        components.append(comp)
    trees = []
    stars = 0
    for comp in components:
        vs = [v for v in range(n) if (comp >> v) & 1]
        if len(vs) == 4 and sum(adj[v].bit_count() for v in vs) == 6:
            trees.append(comp)
            stars += max(adj[v].bit_count() for v in vs) == 3
    # Subset enumeration is independent of any tree classification.
    best = 0
    for s in range(1 << n):
        if s.bit_count() <= best:
            continue
        if all(not (adj[v] & s) for v in range(n) if (s >> v) & 1):
            best = s.bit_count()
    erased = sum(trees)
    rest = sum(1 << e for e, (u, v) in enumerate(edges)
               if ((g >> e) & 1) and not ((erased >> u) & 1 or (erased >> v) & 1))
    return best, tuple(sorted(trees)), rest, stars


def prufer_tree(code):
    degrees = [1]*4
    for x in code:
        degrees[x] += 1
    result = set()
    for x in code:
        v = next(v for v in range(4) if degrees[v] == 1)
        result.add(tuple(sorted((v, x))))
        degrees[v] -= 1
        degrees[x] -= 1
    leaves = [v for v in range(4) if degrees[v] == 1]
    result.add(tuple(leaves))
    return frozenset(result)


edges4 = list(combinations(range(4), 2))
tree_masks = []
tree_alphas = {}
for g in range(64):
    alpha, trees, _, stars = graph_info(4, g)
    if trees:
        tree_masks.append(g)
        tree_alphas[g] = alpha
assert len(tree_masks) == 16
assert Counter(tree_alphas.values()) == {2: 12, 3: 4}
from_prufer = {prufer_tree(code) for code in product(range(4), repeat=2)}
from_edges = {frozenset(e for j, e in enumerate(edges4) if (g >> j) & 1)
              for g in tree_masks}
assert from_prufer == from_edges

graph_checks = fibre_checks = moment_checks = 0
for n in range(1, 7):
    pairs = math.comb(n, 2)
    hist = defaultdict(lambda: [0, 0, 0])
    fibres = defaultdict(Counter)
    for g in range(1 << pairs):
        alpha, trees, rest, stars = graph_info(n, g)
        t = len(trees)
        row = hist[g.bit_count()]
        row[0] += 1
        row[1] += t
        row[2] += t*t
        if t:
            fibres[(trees, rest)][(stars, alpha-2*t-stars)] += 1
        graph_checks += 1
    for (trees, rest), outcomes in fibres.items():
        t = len(trees)
        z_values = {z for b, z in outcomes}
        assert len(z_values) == 1
        z = next(iter(z_values))
        assert outcomes == Counter({(b, z): math.comb(t, b)*4**b*12**(t-b)
                                    for b in range(t+1)})
        fibre_checks += 1
    for bias in (F(1, 2*n), F(2, 7), F(3, 4)):
        totals = [sum((F(values[j])*bias**e*(1-bias)**(pairs-e)
                       for e, values in hist.items()), F(0)) for j in range(3)]
        assert totals[0] == 1
        if n >= 4:
            single = 16*bias**3*(1-bias)**(4*n-13)
            mean = math.comb(n, 4)*single
            factorial2 = (math.comb(n, 4)*math.comb(n-4, 4)*single**2
                          *(1-bias)**(-16)) if n >= 8 else F(0)
        else:
            mean = factorial2 = F(0)
        assert totals[1] == mean
        assert totals[2] == mean+factorial2
        variance = totals[2]-mean**2
        assert variance >= 0
        assert variance <= mean+mean**2*((1-bias)**(-16)-1)
        moment_checks += 1

# Two independent ways to count joint events on two disjoint four-sets.
joint_component_checks = 0
for n, bias in product((8, 9, 12, 100), (F(1, 2), F(2, 7), F(1, 100))):
    single = 16*bias**3*(1-bias)**(4*n-13)
    # 6 present edges; 6 internal absent edges, 16 joining pairs,
    # and 8(n-8) pairs to the remaining vertices must be absent.
    direct = 256*bias**6*(1-bias)**(6+16+8*(n-8))
    assert direct == single**2*(1-bias)**(-16)
    joint_component_checks += 1

forest_checks = 0
for t in (1, 2, 3):
    histogram = Counter()
    for forest in product(tree_masks, repeat=t):
        histogram[sum(tree_alphas[g] for g in forest)-2*t] += 1
        forest_checks += 1
    assert histogram == Counter({b: math.comb(t, b)*4**b*12**(t-b)
                                 for b in range(t+1)})


def binomial_integer_weights(t):
    # P(B=j)=C(t,j)3^(t-j)/4^t, with exact recurrence.
    w = 3**t
    for j in range(t+1):
        yield j, w
        if j < t:
            numerator = w*(t-j)
            divisor = 3*(j+1)
            assert numerator % divisor == 0
            w = numerator//divisor


chebyshev_checks = 0
for t in range(1, 121):
    cdf = 0
    for h, w in binomial_integer_weights(t):
        cdf += w
        if 6*cdf >= 4**t:
            # h>=t/4-2sqrt(t), written without floating point.
            assert 4*h >= t or (t-4*h)**2 <= 64*t
            chebyshev_checks += 1

tail_checks = likelihood_checks = constant_checks = 0
smallest_log_margin = D('Infinity')
for root in (32, 48, 64, 96, 128):
    t = root*root
    weights = list(binomial_integer_weights(t))
    prefix = []
    total = 0
    for j, w in weights:
        total += w
        prefix.append(total)
    assert total == 4**t
    for r in sorted({0, root//2, root, 2*root, 4*root, t//32, t//16}):
        delta = F(r+4*root, t)
        if delta > F(1, 8):
            continue
        q = F(1, 4)
        qp = q-delta
        assert F(1, 8) <= qp < q
        h = t//4-2*root
        cutoff = h-r
        assert cutoff >= 0
        log_actual = D(prefix[cutoff]).ln()-D(4**t).ln()
        log_bound = D(F(3, 4).numerator).ln()-D(F(3, 4).denominator).ln()-320-dec(F(20*r*r, t))
        assert log_actual >= log_bound
        smallest_log_margin = min(smallest_log_margin, log_actual-log_bound)
        tail_checks += 1
        kl = dec(qp)*(dec(qp)/dec(q)).ln() + dec(1-qp)*(dec(1-qp)/dec(1-q)).ln()
        theta = (dec(q*(1-qp)/(qp*(1-q)))).ln()
        assert kl <= 6*dec(delta**2)+D('1e-80')
        assert theta <= 16*dec(delta)+D('1e-80')
        mean = t*qp
        low = math.floor(mean-root)+1
        high = math.ceil(mean+root)-1
        assert high <= h-r
        for b in (low, high):
            direct = D(b)*(dec(q/qp)).ln()+D(t-b)*(dec((1-q)/(1-qp))).ln()
            centred = -t*kl+(D(b)-dec(mean))*theta
            assert abs(direct-centred) < D('1e-75')
            assert direct >= log_bound-(D(3)/4).ln()
            likelihood_checks += 1
        u = F(r, root)
        left = 6*(u+4)**2+16*(u+4)
        assert left <= 10*(u+4)**2 <= 20*u*u+320
        constant_checks += 1

# Independently bracket beta and hence the target and the CLT variance.
def exponential_interval(x, terms=80):
    total = term = F(1)
    for j in range(1, terms+1):
        term = term*x/j
        total += term
    return total, total+F(2, math.factorial(terms+1))


lo, hi = F(0), F(1)
for _ in range(100):
    mid = (lo+hi)/2
    el, eu = exponential_interval(mid)
    if mid*eu < F(1, 2):
        lo = mid
    elif mid*el > F(1, 2):
        hi = mid
    else:
        raise AssertionError('Insufficient exponential precision')
a_lo, a_hi = 2*lo+lo*lo, 2*hi+hi*hi
var_lo, var_hi = a_lo-6*hi*hi, a_hi-6*lo*lo
assert 0 < a_lo < a_hi < 1
assert 0 < var_lo < var_hi
# Second variance expression, evaluated at an independently iterated Decimal root.
beta = D('0.35')
for _ in range(20):
    beta -= (beta*beta.exp()-D('0.5'))/(beta.exp()*(1+beta))
a_direct = 2*beta+beta*beta
variance_direct = a_direct-6*beta*beta
variance_alternative = (-2*beta).exp()*(beta.exp()*(1-beta/2)-1)
assert dec(lo) <= beta <= dec(hi)
assert dec(var_lo) <= variance_direct <= dec(var_hi)
assert abs(variance_direct-variance_alternative) < D('1e-85')
target_checks = 0
for n in (2, 3, 100, 10**6, 10**12):
    k = max(1, math.floor(n*a_lo))
    assert dec(k) <= n*a_direct
    assert dec(k) >= n*a_direct-2
    target_checks += 1

gamma = D(2).ln()-D('0.5')
assert gamma >= D(1)/6
assert 1-64*gamma/D(2).ln() < 0
assert (D(3)/4/D(12)) == D(1)/16

report = {
    'status': 'PASS',
    'labelled_four_vertex_trees': len(tree_masks),
    'independence_number_counts': dict(Counter(tree_alphas.values())),
    'prufer_tree_set_agrees': True,
    'exhaustive_graph_checks': graph_checks,
    'conditional_shape_fibres_checked': fibre_checks,
    'exact_component_moment_checks': moment_checks,
    'exact_disjoint_component_checks': joint_component_checks,
    'forest_shape_checks': forest_checks,
    'exact_threshold_checks': chebyshev_checks,
    'exact_binomial_tails_checked': tail_checks,
    'likelihood_identity_checks': likelihood_checks,
    'rational_constant_checks': constant_checks,
    'minimum_log_tail_margin': str(smallest_log_margin),
    'beta_at_d_one_half': str(beta),
    'limiting_independence_density': str(a_direct),
    'variance_coefficient': str(variance_direct),
    'target_rounding_checks': target_checks,
    'component_cutoff_exponent': str(1-64*gamma/D(2).ln()),
    'largest_exhaustive_graph_n': 6,
    'largest_binomial_t': 16384,
    'omp_num_threads': os.environ['OMP_NUM_THREADS'],
    'nice': os.getpriority(os.PRIO_PROCESS, 0),
    'elapsed_seconds': round(time.monotonic()-started, 4),
    'max_rss_bytes_macos': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    'limitations': 'Finite checks support the elementary application; they do not verify Pittel\'s CLT or the imported concentration theorem, and do not solve T284.'
}
assert report['max_rss_bytes_macos'] < 1024**3
Path('loss_verification.json').write_text(json.dumps(report, indent=2)+'\n')
for key, value in report.items():
    print(f'{key}: {value}')
