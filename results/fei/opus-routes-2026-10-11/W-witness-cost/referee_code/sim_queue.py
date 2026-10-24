"""Monte Carlo simulation of the paper's queue law Q_{1,lambda} (current-threshold-paper.tex lines 844-860) on a small
union with OVERLAPPING gates, to check W-L2 (Lemma 3.2): (i) the probability of the event E_l = {roots = {l}, s = |A|,
B = A, c = 0} equals rho_l 2^-Lambda /(s(s+1)) prod theta / Z / 2; (ii) the empirical Q(A) is >= the witness-sum
lower bound for every A.  Runs longer than a step cap are counted as failures (this only lowers the empirical Q).
"""
import math, random, itertools
from rc_common import elem_sym, theta

rng = random.Random(11)
lam = 1.0
# three gates on coordinates 0..4; each gate = list of inner functions, each inner function = ordered list (rank order)
gates = [
    {'inner': [[0, 1], [2]], 'pi': 0.3},
    {'inner': [[1, 3]], 'pi': 0.2},
    {'inner': [[2, 4, 3]], 'pi': 0.125},
]
for g in gates:
    g['R'] = sorted(set(v for inn in g['inner'] for v in inn))
d = {}
for li, g in enumerate(gates):
    for v in g['R']:
        d.setdefault(v, []).append(li)


def theta_g(g, s, v):
    return max(theta(s, inn.index(v) + 1) for inn in g['inner'] if v in inn)


def Zg(g, s):
    return elem_sym([theta_g(g, s, v) for v in g['R']], s)


Lam = sum(math.log2(1 + lam * g['pi']) for g in gates)


def draw_s():
    u = rng.random(); s = 1
    acc = 0.5
    while u > acc:
        s += 1; acc += 1 / (s * (s + 1))
    return s


def draw_c():
    u = rng.random(); c = 0
    acc = 0.5
    while u > acc:
        c += 1; acc += 1 / ((c + 1) * (c + 2))
    return c


_subcache = {}


def draw_subset(g, s):
    # P(B) = prod theta / Z over s-subsets of R (cached per gate and s)
    key = (id(g), s)
    if key not in _subcache:
        subs = list(itertools.combinations(g['R'], s))
        w = [math.prod(theta_g(g, s, v) for v in B) for B in subs]
        tot = sum(w)
        cum = list(itertools.accumulate(x / tot for x in w))
        _subcache[key] = (subs, cum)
    subs, cum = _subcache[key]
    u = rng.random()
    for B, c in zip(subs, cum):
        if u <= c:
            return B
    return subs[-1]


def run(cap=60):
    queue = [li for li, g in enumerate(gates) if rng.random() < lam * g['pi'] / (1 + lam * g['pi'])]
    roots = tuple(queue)
    out = set(); steps = 0; first = None
    while queue:
        steps += 1
        if steps > cap:
            return None, None
        li = queue.pop(0)
        g = gates[li]
        s = draw_s()
        if s > len(g['R']):
            return None, None
        B = draw_subset(g, s)
        c = draw_c()
        if first is None:
            first = (s, tuple(sorted(B)), c)
        out |= set(B)
        multiset = sorted(rng.choice(B) for _ in range(c))   # uniform multiset? see note below
        for v in multiset:
            queue.append(rng.choice(d[v]))
    return frozenset(out), (roots, first)


# NOTE on the multiset draw: the paper draws a UNIFORM multiset of c elements (each of the binom(s+c-1,c) multisets equally
# likely); i.i.d. draws are not uniform on multisets for c >= 2. Lemma 3.2 only uses c = 0, whose probability (1/2) and
# multiset (empty) are the same under both conventions, so the check of (i)/(ii) is unaffected. (Uniform multisets are
# used below anyway via stars and bars, to stay faithful.)
_mscache = {}


def uniform_multiset(B, c):
    s = len(B)
    if c > 12:
        return None   # absurdly long branch: treated as a failed run below (only lowers the empirical Q)
    if (s, c) not in _mscache:
        _mscache[(s, c)] = list(itertools.combinations_with_replacement(range(s), c))
    return [B[i] for i in rng.choice(_mscache[(s, c)])]


def run_faithful(cap=60):
    queue = [li for li, g in enumerate(gates) if rng.random() < lam * g['pi'] / (1 + lam * g['pi'])]
    roots = tuple(queue)
    out = set(); steps = 0; first = None
    while queue:
        steps += 1
        if steps > cap:
            return None, None
        li = queue.pop(0)
        g = gates[li]
        s = draw_s()
        if s > len(g['R']):
            return None, None
        B = draw_subset(g, s)
        c = draw_c()
        if first is None:
            first = (s, tuple(sorted(B)), c)
        out |= set(B)
        ms = uniform_multiset(list(B), c)
        if ms is None:
            return None, None
        for v in ms:
            queue.append(rng.choice(d[v]))
    return frozenset(out), (roots, first)


TR = 120000
counts = {}; ev = {}
for _ in range(TR):
    A, info = run_faithful()
    if A is None or not A:
        continue
    counts[A] = counts.get(A, 0) + 1
    roots, first = info
    if len(roots) == 1 and first[2] == 0 and frozenset(first[1]) == A:
        ev[(roots[0], A)] = ev.get((roots[0], A), 0) + 1
worst_ev = 0.0; worst_lb = 0.0; nA = 0
for A, cnt in counts.items():
    s = len(A)
    lb = 0.0
    for li, g in enumerate(gates):
        if A <= set(g['R']):
            p = lam * g['pi'] * 2 ** (-Lam) / (s * (s + 1)) * math.prod(theta_g(g, s, v) for v in A) / Zg(g, s) / 2
            lb += p
            emp = ev.get((li, A), 0) / TR
            se = math.sqrt(max(p, 1e-12) / TR)
            worst_ev = max(worst_ev, abs(emp - p) / se)
    q = cnt / TR
    se = math.sqrt(max(q, 1e-12) / TR)
    worst_lb = max(worst_lb, (lb - q) / se)   # positive and large would refute Q >= Q_lb
    nA += 1
print(f'{TR} runs, {nA} distinct outputs. max |emp P(E_l) - formula| / s.e. = {worst_ev:.2f} (should be ~<4); '
      f'max (Q_lb - Qhat)/s.e. = {worst_lb:.2f} (should be <~3; negative means Qhat above the bound)')
