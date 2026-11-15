"""Independent checks of 'The stationary cover time of reversible chains on three and four states'
(yspennstate/stationary-cover-time-four-states at 984b772). Own code; uses only the repo's evidence files as data.
Usage: python referee_check.py <path to repo clone>
"""
import sys, json, gzip, itertools, random
from fractions import Fraction as Fr
import sympy as sp

REPO = sys.argv[1]
random.seed(20261114)

def solve_lin(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c] / M[c][c]
                M[r] = [M[r][k] - f * M[c][k] for k in range(n + 1)]
    return [M[i][n] / M[i][i] for i in range(n)]

def cover_reward(n, w, h, r):
    """E_x[sum over steps t < C of r(X_t)] for the chain with conductances w (dict on pairs) and holding h.
    Exact, by first-step equations on (state, visited set)."""
    m = [sum(w.get(frozenset((x, y)), 0) for y in range(n) if y != x) + h[x] for x in range(n)]
    P = [[(h[x] if x == y else w.get(frozenset((x, y)), 0)) / m[x] for y in range(n)] for x in range(n)]
    full = frozenset(range(n))
    E = {}
    for size in range(n, 0, -1):
        for V in itertools.combinations(range(n), size):
            V = frozenset(V)
            if V == full:
                for x in V:
                    E[(x, V)] = Fr(0)
                continue
            idx = sorted(V)
            A = [[(1 if i == j else 0) - P[x][y] for j, y in enumerate(idx)] for i, x in enumerate(idx)]
            b = [r[x] + sum(P[x][y] * E[(y, V | {y})] for y in range(n) if y not in V) for x in idx]
            sol = solve_lin(A, b)
            for i, x in enumerate(idx):
                E[(x, V)] = sol[i]
    return [E[(x, frozenset([x]))] for x in range(n)], m

def stat_cover(n, w, h):
    Ex, m = cover_reward(n, w, h, [Fr(1)] * n)
    return sum(m[x] * Ex[x] for x in range(n)) / sum(m), Ex, m

def rnd_w(n, zero_ok=False):
    while True:
        w = {}
        for e in itertools.combinations(range(n), 2):
            v = Fr(random.randint(0 if zero_ok else 1, 9), random.randint(1, 5))
            if v:
                w[frozenset(e)] = v
        # connected?
        seen, st = {0}, [0]
        while st:
            x = st.pop()
            for y in range(n):
                if y not in seen and w.get(frozenset((x, y)), 0):
                    seen.add(y); st.append(y)
        if len(seen) == n:
            return w

out = []
def say(s):
    print(s); out.append(s)

# A. n=3 closed form and its Schur/AM-GM split
a, b, c = sp.symbols('a b c', positive=True)
sym = a**2*b + a**2*c + b**2*a + b**2*c + c**2*a + c**2*b
Q = 4*(a**3 + b**3 + c**3) - sym - 6*a*b*c
split = (a**3 + b**3 + c**3 + 3*a*b*c - sym) + 3*(a**3 + b**3 + c**3 - 3*a*b*c)
say(f"A1 Q equals Schur bracket + 3*(AM-GM bracket): {sp.expand(Q - split) == 0}")
bad = 0
for _ in range(40):
    av, bv, cv = [Fr(random.randint(1, 30), random.randint(1, 7)) for _ in range(3)]
    if random.random() < 0.3:
        av = Fr(0)
    w = {frozenset((0, 1)): av, frozenset((0, 2)): bv, frozenset((1, 2)): cv}
    w = {k: v for k, v in w.items() if v}
    E, _, _ = stat_cover(3, w, [Fr(0)] * 3)
    Qv = Q.subs({a: av, b: bv, c: cv})
    pred = 3 + Fr(str(Qv)) / (2 * (av + bv + cv) * (av*bv + bv*cv + cv*av))
    bad += (E != pred)
say(f"A2 eq (three) against an exact first-step solve, 40 random weightings (some with a zero edge): mismatches {bad}")

# B. occupation identity (Prop 2) on n = 3, 4, 5
for n in (3, 4, 5):
    worst_sym, neg, idbad, exbad = 0, 0, 0, 0
    for _ in range(4 if n == 5 else 8):
        w = rnd_w(n, zero_ok=True)
        zero = [Fr(0)] * n
        EC, Ex, q = stat_cover(n, w, zero)
        N = [[None] * n for _ in range(n)]
        for y in range(n):
            col, _ = cover_reward(n, w, zero, [Fr(1) if z == y else Fr(0) for z in range(n)])
            for x in range(n):
                N[x][y] = col[x]
        K = [[N[x][y] / q[y] for y in range(n)] for x in range(n)]
        worst_sym += sum(K[x][y] != K[y][x] for x in range(n) for y in range(n))
        neg += sum(K[x][y] < 0 for x in range(n) for y in range(n))
        exbad += sum(sum(K[x][y] * q[y] for y in range(n)) != Ex[x] for x in range(n))
        h = [Fr(random.randint(0, 6), random.randint(1, 3)) for _ in range(n)]
        ECh, Exh, mh = stat_cover(n, w, h)
        W, Wh = sum(q), sum(mh)
        c0 = (n - 1) * sum(Fr(1, k) for k in range(1, n))
        lhs = Wh * (ECh - c0)
        rhs = W * (EC - c0) + sum(h[x] * (2 * Ex[x] - c0) for x in range(n)) + \
            sum(h[x] * K[x][y] * h[y] for x in range(n) for y in range(n))
        idbad += (lhs != rhs)
        idbad += sum(Exh[x] != sum(K[x][y] * mh[y] for y in range(n)) for x in range(n))
    say(f"B n={n}: K asymmetric entries {worst_sym}, negative entries {neg}, (Kq)_x != E_xC {exbad}, identity (holding) mismatches {idbad}")

# C. Remark 3 numbers
w = {frozenset((0, 1)): Fr(1), frozenset((0, 2)): Fr(1, 100), frozenset((1, 2)): Fr(1, 100)}
E0, _, _ = stat_cover(3, w, [Fr(0)] * 3)
E1, _, _ = stat_cover(3, w, [Fr(0), Fr(0), Fr(1)])
say(f"C remark: without holding {float(E0):.4f}, with h_3 = 1 {float(E1):.4f}")

# D. F rebuilt from eq (F), compared with evidence/four_polynomial.json
X = sp.symbols('x0:6')
R_, *gens = sp.ring('x0:6', sp.ZZ)
xs = gens
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
wv = {frozenset(e): xs[i] for i, e in enumerate(edges)}
qv = [sum(wv[frozenset((i, j))] for j in range(4) if j != i) for i in range(4)]
Wp = sum(qv)
def lap(S):
    return [[qv[i] if i == j else -wv[frozenset((i, j))] for j in S] for i in S]
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def adj3(M):
    C = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rr = [r for r in range(3) if r != i]; cc = [k for k in range(3) if k != j]
            minor = M[rr[0]][cc[0]]*M[rr[1]][cc[1]] - M[rr[0]][cc[1]]*M[rr[1]][cc[0]]
            C[j][i] = (-1)**(i+j) * minor
    return C
taus = set()
A = R_(0)
for S in itertools.combinations(range(4), 3):
    M = lap(S); taus.add(det3(M)); Ad = adj3(M); qS = [qv[i] for i in S]
    A += sum(qS[i]*Ad[i][j]*qS[j] for i in range(3) for j in range(3))
say(f"D1 det L_S equal for the four 3-sets (matrix-tree): {len(taus) == 1}")
tau = taus.pop()
pairs = list(itertools.combinations(range(4), 2))
Dl = {p: qv[p[0]]*qv[p[1]] - wv[frozenset(p)]**2 for p in pairs}
Bl = {p: qv[p[0]]*qv[p[1]]*(qv[p[0]] + qv[p[1]] + 2*wv[frozenset(p)]) for p in pairs}
Rr = R_(1)
for p in pairs:
    Rr *= Dl[p]
S2 = R_(0)
for p in pairs:
    t = Bl[p]
    for p2 in pairs:
        if p2 != p:
            t *= Dl[p2]
    S2 += t
F = 2*A*Rr - 2*tau*S2 - 9*Wp*tau*Rr
terms = dict(F.terms())
negs = sum(1 for v in terms.values() if v < 0)
degs = {sum(k) for k in terms}
say(f"D2 F: {len(terms)} terms, {negs} negative, degrees {sorted(degs)}")
ev = json.load(open(f"{REPO}/evidence/four_polynomial.json"))
evd = {}
for t in ev['terms']:
    e, co = (t[0], t[1]) if isinstance(t, list) else (t['exp'], t['coef'])
    evd[tuple(e)] = int(co)
say(f"D3 repo four_polynomial.json variables {ev['variables']}; identical to rebuilt F: {evd == {tuple(k): int(v) for k, v in terms.items()}}")
# value check against the solver at random points
bad = 0
for _ in range(6):
    vals = [random.randint(1, 9) for _ in range(6)]
    w = {frozenset(e): Fr(vals[i]) for i, e in enumerate(edges)}
    E, _, _ = stat_cover(4, w, [Fr(0)] * 4)
    num = Fr(int(F(*vals))); den = 2 * Fr(int(Wp(*vals))) * Fr(int(tau(*vals))) * Fr(int(Rr(*vals)))
    bad += (E - Fr(11, 2) != num / den)
say(f"D4 E_pi C - 11/2 = F/(2 W tau R) at 6 random integer points: mismatches {bad}")

# E. equality case: every connected spanning proper edge subset of K4, unit conductances
cnt, mn = 0, None
for k in range(3, 6):
    for E_ in itertools.combinations(range(6), k):
        w = {frozenset(edges[i]): Fr(1) for i in E_}
        seen, st = {0}, [0]
        while st:
            x = st.pop()
            for y in range(4):
                if y not in seen and frozenset((x, y)) in w:
                    seen.add(y); st.append(y)
        if len(seen) < 4:
            continue
        val = stat_cover(4, w, [Fr(0)] * 4)[0]
        fval = int(F(*[1 if i in E_ else 0 for i in range(6)]))
        cnt += 1
        mn = val if mn is None else min(mn, val)
        assert (val > Fr(11, 2)) == (fval > 0), (E_, val, fval)
say(f"E1 {cnt} connected spanning proper subgraphs of K4: min E_pi C {mn} = {float(mn):.4f} > 11/2, F > 0 on each")

# F. cone files: nonnegativity, z0^14 zj^2 and zj^16 coefficients, orbit coverage
man = json.load(open(f"{REPO}/evidence/cone_manifest.json"))
orders, total, negc, sq_bad, top_bad = [], 0, 0, 0, 0
for cone in man['cones']:
    o = cone['order']; orders.append(tuple(o))
    data = json.load(gzip.open(f"{REPO}/evidence/cones/{cone['file']}"))
    co = {tuple(e): int(v) for e, v in data}
    total += len(co); negc += sum(v < 0 for v in co.values())
    for j in range(1, 6):
        e = [0]*6; e[0] = 14; e[j] = 2
        sq_bad += co.get(tuple(e), 0) <= 0
        Eset = [edges[o[k]] for k in range(j, 6)]
        seen, st = {0}, [0]
        while st:
            x = st.pop()
            for (u, v) in Eset:
                for (s, t) in ((u, v), (v, u)):
                    if s == x and t not in seen:
                        seen.add(t); st.append(t)
        if len(seen) == 4:
            e = [0]*6; e[j] = 16
            top_bad += co.get(tuple(e), 0) <= 0
    # spot check: G_o(z) = F(x(z)) at random z
    z = [random.randint(0, 4) for _ in range(6)]
    x = [0]*6
    for k in range(6):
        x[o[k]] = sum(z[:k+1])
    g = 0
    for e, v in co.items():
        t = v
        for i in range(6):
            t *= z[i] ** e[i]
        g += t
    assert g == int(F(*x)), cone['file']
cover = set()
for o in orders:
    for perm in itertools.permutations(range(4)):
        img = [edges.index(tuple(sorted((perm[edges[i][0]], perm[edges[i][1]])))) for i in o]
        cover.add(tuple(img))
say(f"F1 cones: {len(orders)} files, {total} coefficients, {negc} negative; G_o(z)=F(x(z)) at a random z in every cone")
say(f"F2 z0^14 zj^2 coefficient not positive in {sq_bad} (cone, j) pairs; z_j^16 not positive on a connected tail in {top_bad}")
say(f"F3 orderings covered by the 30 representatives under S4: {len(cover)} of 720")
open('referee_check.out', 'w').write('\n'.join(out) + '\n')
