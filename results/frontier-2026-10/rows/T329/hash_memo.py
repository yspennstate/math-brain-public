"""T329: memorize n labelled points with O(n/log n) ReLU parameters of O(log n) bits each.

The network: (1) project to one dimension and read off an integer key u by ramp bit extraction; (2) look up the
word z_g of u's group (n/k groups of k consecutive keys) with one layer of 2 ramps per group; (3) evaluate one
shared k-wise independent hash p(u) = sum c_i u^i mod P by Horner, every product of two activations done by bit
extraction and big-M gating; (4) output the parity of <low m bits of p(u), z_g>. The words z_g solve a GF(2)
system per group; it is solvable for every labelling when the group's hash vectors are independent.

Every node is relu(affine combination of earlier nodes), built explicitly; the network is evaluated in exact
integer arithmetic (numpy int64 after the first layer, Fractions for the first layer), and the script checks
every training point, counts nonzero weights and biases, and reports the largest weight in bits.
argv: n d k seed [nevals: evaluate the network on this many random training points; default all]
"""
import sys, math, random
from fractions import Fraction
import numpy as np

n = int(sys.argv[1]); d = int(sys.argv[2]); k = int(sys.argv[3]); seed = int(sys.argv[4])
nevals = int(sys.argv[5]) if len(sys.argv) > 5 else n
rng = random.Random(seed)

# ---------- data: n points on a 2^-12 grid in [0,1]^d, distinct, random labels
pts = set()
while len(pts) < n:
    pts.add(tuple(rng.randrange(4096) for _ in range(d)))
X = [tuple(Fraction(c, 4096) for c in p) for p in pts]
Y = [rng.randrange(2) for _ in range(n)]

# ---------- graph builder: expressions are dicts {node: coeff, None: const}
class Net:
    def __init__(self):
        self.nodes = []          # (expr) for relu nodes; node id = index
        self.params = 0
        self.maxw = 0
    def relu(self, expr):
        nz = [c for c in expr.values() if c != 0]
        self.params += len(nz)
        for c in nz:
            self.maxw = max(self.maxw, abs(int(c)) if Fraction(c).denominator == 1 else
                            max(abs(Fraction(c).numerator), Fraction(c).denominator))
        self.nodes.append(dict(expr))
        return {len(self.nodes) - 1: 1}

def add(*terms):
    out = {}
    for coef, e in terms:
        for kk, v in e.items():
            out[kk] = out.get(kk, 0) + coef * v
    return {kk: v for kk, v in out.items() if v != 0}

def const(c):
    return {None: c}

net = Net()

def mat(e):
    """a nonnegative linear intermediate carried as one node: relu(x) = x for x >= 0 (keeps fan-in O(1))."""
    return net.relu(e)

def istep(e, t):
    """1[x >= t] for integer-valued x: relu(x - t + 1) - relu(x - t)."""
    a = net.relu(add((1, e), (1, const(1 - t))))
    b = net.relu(add((1, e), (1, const(-t))))
    return add((1, a), (-1, b))

def bits(e, L):
    """bits b_{L-1..0} of an integer 0 <= x < 2^L; returns list low->high and the expressions."""
    out = [None] * L
    x = e
    for j in range(L - 1, -1, -1):
        b = istep(x, 2 ** j)
        out[j] = b
        x = mat(add((1, x), (-(2 ** j), b)))
    return out

def times(vbits, u, Umax):
    """v * u for v given by its bits and 0 <= u <= Umax: sum_b relu(2^b u - M(1 - v_b)), M = 2^b Umax."""
    terms = []
    for b, vb in enumerate(vbits):
        M = (2 ** b) * Umax
        terms.append((1, net.relu(add(((2 ** b), u), (M, vb), (1, const(-M))))))
    return add(*terms)

def modP(e, P, Qbits):
    """x mod P for 0 <= x < P 2^Qbits, by extracting the quotient's bits."""
    x = e
    for j in range(Qbits - 1, -1, -1):
        s = istep(x, P * 2 ** j)
        x = mat(add((1, x), (-(P * 2 ** j), s)))
    return x

# ---------- layer 1: integer key from a random projection, rounded by ramp extraction on reals
def make_keys():
    for _ in range(1000):
        a = [rng.randrange(-n * n, n * n) for _ in range(d)]
        proj = sorted(sum(ai * xi for ai, xi in zip(a, x)) for x in X)
        gaps = min(proj[i + 1] - proj[i] for i in range(n - 1))
        if gaps == 0:
            continue
        lo = proj[0]
        scale = Fraction(2) / gaps          # consecutive keys at least 2 apart after scaling
        shift = Fraction(rng.randrange(10 ** 6), 10 ** 6)
        ts = [(p - lo) * scale + shift for p in proj]
        eps = min(min(t - math.floor(t), math.ceil(t) - t if t != math.floor(t) else 1) for t in ts)
        if eps > Fraction(1, 8 * n):
            return a, lo, scale, shift
    raise SystemExit("no projection")

a, lo, scale, shift = make_keys()
eps = Fraction(1, 8 * n)
tvals = [sum(ai * xi for ai, xi in zip(a, x)) * scale - lo * scale + shift for x in X]
Lkey = max(int(t) for t in tvals).bit_length()
# real-input part: ramp of width eps on t; t is an affine function of the input, carried as a Fraction expr
inp = {('x', i): a[i] * scale for i in range(d)}
inp[None] = -lo * scale + shift
key_bits = []
x = inp
first_layer_params = 0
for j in range(Lkey - 1, -1, -1):
    # step_eps(x - 2^j) = relu((x-2^j)/eps) - relu((x-2^j)/eps - 1)
    e1 = add((1 / eps, x), (1, const(-(2 ** j) / eps)))
    r1 = net.relu(e1)
    r2 = net.relu(add((1, e1), (1, const(-1))))
    b = add((1, r1), (-1, r2))
    key_bits.append((j, b))
    x = add((1, x), (-(2 ** j), b))
u = add(*[((2 ** j), b) for j, b in key_bits])     # the integer key
first_params, first_maxw = net.params, net.maxw
net.maxw = 0
u = mat(u)
N = 2 ** Lkey

# ---------- groups of k consecutive keys
keys_true = [int(t) for t in tvals]
order = sorted(range(n), key=lambda i: keys_true[i])
groups = [order[i:i + k] for i in range(0, n, k)]
G = len(groups)
m = k + max(1, math.ceil(math.log2(G))) + 2
P = 2 ** (m + 6)
while True:                                  # a prime above max(N, 2^(m+6))
    P += 1
    P = max(P, N + 1)
    if all(P % q for q in range(2, int(P ** 0.5) + 1)):
        break
Pbits = P.bit_length()

def hashval(c, uu):
    v = 0
    for ci in reversed(c):
        v = (v * uu + ci) % P
    return v % (2 ** m)

def solve_gf2(rows, ys):
    """find z (int bitmask, m bits) with parity(row & z) = y for all rows, or None."""
    piv = []  # (mask, pivotbit, rhs)
    for r, y in zip(rows, ys):
        for pm, pb, py in piv:
            if r >> pb & 1:
                r ^= pm; y ^= py
        if r == 0:
            if y:
                return None
            continue
        pb = r.bit_length() - 1
        piv.append((r, pb, y))
    z = 0
    for pm, pb, py in reversed(piv):
        # bit pb of z chosen so that parity(pm & z) = py, lower pivots already set? process from low pivot up
        pass
    # back-substitute properly: sort pivots by bit ascending and set each pivot bit
    piv.sort(key=lambda t: t[1])
    z = 0
    for pm, pb, py in piv:
        cur = bin(pm & z).count("1") & 1
        if cur != py:
            z ^= (1 << pb)
    # verify (pivot rows have pivot = highest bit, so setting bits in ascending order is consistent)
    return z

tries = 0
while True:
    tries += 1
    c = [rng.randrange(P) for _ in range(k)]
    Z = []
    ok = True
    for g in groups:
        rows = [hashval(c, keys_true[i]) for i in g]
        z = solve_gf2(rows, [Y[i] for i in g])
        if z is None or any((bin(r & z).count("1") & 1) != Y[i] for r, i in zip(rows, g)):
            ok = False; break
        Z.append(z)
    if ok:
        break
import os
if os.environ.get("NEGCTRL"):          # negative control: random words instead of the solved ones; expect about half wrong
    Z = [rng.randrange(2 ** m) for _ in Z]

# ---------- group lookup: Z(u) = sum_j (Z_j - Z_{j-1}) 1[u >= b_j]
bnds = [keys_true[g[0]] for g in groups]
terms = []
prev = 0
for bj, zj in zip(bnds, Z):
    if zj - prev != 0:
        terms.append((zj - prev, istep(u, bj)))
    prev = zj
Zu = mat(add(*terms))
group_params = net.params - first_params

# ---------- shared hash by Horner: v <- (v*u + c_i) mod P
v = const(c[-1])
for ci in reversed(c[:-1]):
    vb = bits(v, Pbits)
    prod = times(vb, u, N - 1)
    v = modP(mat(add((1, prod), (1, const(ci)))), P, Lkey + 1)
hash_params = net.params - first_params - group_params
hb = bits(v, Pbits)[:m]
zb = bits(Zu, m)
ands = [net.relu(add((1, hb[j]), (1, zb[j]), (1, const(-1)))) for j in range(m)]
S = add(*[(1, e) for e in ands])
Sb = bits(S, (m).bit_length())
out = Sb[0]
out_params = len(out)

# ---------- evaluate exactly on all n points
vals = {}
def ev(expr, i):
    s = expr.get(None, 0)
    for kk, cc in expr.items():
        if kk is None:
            continue
        if isinstance(kk, tuple):
            s += cc * X[i][kk[1]]
        else:
            s += cc * vals[kk]
    return s

wrong = 0
evalset = sorted(random.Random(seed + 7).sample(range(n), nevals))
for i in evalset:
    vals = {}
    for nid, e in enumerate(net.nodes):
        s = ev(e, i)
        if isinstance(s, Fraction) and s.denominator == 1:
            s = int(s)
        vals[nid] = s if s > 0 else 0
    yhat = ev(out, i)
    if yhat != Y[i]:
        wrong += 1
    if i == evalset[0]:
        print(f"  point {i}: key {ev(u, i)} (true {keys_true[i]}) out {yhat} label {Y[i]}", flush=True)

nodes = len(net.nodes)
W = net.params + out_params
wbits = math.ceil(math.log2(net.maxw + 1))
print(f"n={n} d={d} k={k} groups={G} m={m} P={P} ({Pbits} bits) key bits={Lkey} seed tries={tries}")
print(f"first layer (projection + key bits): {first_params} params, weights as exact fractions up to ~2^{math.ceil(math.log2(first_maxw+1))} (roundable)")
print(f"relu nodes={nodes} params(nonzero weights+biases)={W} max |integer weight| after layer 1 ~2^{wbits}")
tail_params = W - first_params - group_params - hash_params
print(f"params by part: layer 1 {first_params}, group lookup {group_params} ({group_params/G:.2f} per group), hash {hash_params}, parity readout {tail_params}")
print(f"wrong={wrong} of {len(evalset)} evaluated (all n points satisfy the GF(2) systems by construction)")
print(f"params/n={W/n:.4f}  params*log2(n)/n={W*math.log2(n)/n:.3f}  lower bound n/(B+log2 W)={n/(wbits+math.log2(W)):.0f}")
