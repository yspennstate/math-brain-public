from functools import lru_cache
from fractions import Fraction
import sys

# P13 / C0021 exact self-check for B6, B18, B24.
# Finite claims concern the explicit lifted state S4=L(S3).
# Dynamic-programming expectations use integers scaled by 2^81; this is exact
# because a depth-4 ternary formula has 81 leaves, so every fair-bit decision
# tree has a dyadic expected cost with denominator dividing 2^81.  Each /2
# below is additionally checked for exact divisibility.

sys.setrecursionlimit(10_000_000)
SCALE = 1 << 81

# Canonical hash-consed ternary states. IDs 0,1,2 are unresolved leaf,+,-.
children = [None, None, None]
node_id = {}

def norm3(a, b, c):
    if (a == 1) + (b == 1) + (c == 1) >= 2:
        return 1
    if (a == 2) + (b == 2) + (c == 2) >= 2:
        return 2
    key = tuple(sorted((a, b, c)))
    z = node_id.get(key)
    if z is None:
        z = len(children)
        node_id[key] = z
        children.append(key)
    return z

U = norm3(0, 0, 0)      # untouched bottom MAJ3 block
P = norm3(1, 0, 0)      # (+,u,u)
M = norm3(2, 0, 0)      # (-,u,u)
X = norm3(1, 2, 0)      # (+,-,u)
ACTIVE = {P, M, X}

@lru_cache(None)
def queries(t):
    if t == 0:
        return ((1, 2),)
    if t in (1, 2):
        return ()
    ch = children[t]
    out = set()
    for i, c in enumerate(ch):
        if i and c == ch[i - 1]:
            continue
        for cp, cm in queries(c):
            aa = list(ch); bb = list(ch)
            aa[i] = cp; bb[i] = cm
            out.add((norm3(*aa), norm3(*bb)))
    return tuple(sorted(out))

@lru_cache(None)
def active_count(t):
    if t in ACTIVE:
        return 1
    if t in (0, 1, 2, U):
        return 0
    return sum(active_count(c) for c in children[t])

@lru_cache(None)
def posterior(t):
    if t == 1:
        return Fraction(1)
    if t == 2:
        return Fraction(0)
    if t == 0:
        return Fraction(1, 2)
    a, b, c = (posterior(x) for x in children[t])
    return a*b + a*c + b*c - 2*a*b*c

# Exact unrestricted optimal value, used only on height <=3 child states.
@lru_cache(None)
def Vsmall(t):
    if t in (1, 2):
        return Fraction(0)
    return min(Fraction(1) + (Vsmall(a) + Vsmall(b))/2 for a, b in queries(t))

# B18 alphabet transition check.
assert set(queries(U)) == {(P, M)}
assert set(queries(P)) == {(1, X)}
assert set(queries(M)) == {(X, 2)}
assert set(queries(X)) == {(1, 2)}

# Recover S3 and lift every unresolved macro-leaf to an untouched bottom block.
b = norm3(2, 0, 0)
s3 = norm3(norm3(2, U, U), norm3(b, b, b), norm3(b, b, U))

def lift(t):
    if t in (1, 2):
        return t
    if t == 0:
        return U
    return norm3(*(lift(x) for x in children[t]))

s4 = lift(s3)
assert posterior(s3) == posterior(s4) == Fraction(31, 256)
assert abs(2*posterior(s4)-1) == Fraction(97, 128)
assert Vsmall(s3) == Fraction(547983, 65536)

# B6: V_K is the exact optimum subject to at most K simultaneously active
# bottom blocks (P/M/X) on every reachable state.
cap_calls = {}

def make_vcap(K):
    @lru_cache(None)
    def vi(t):
        cap_calls[K] = cap_calls.get(K, 0) + 1
        if t in (1, 2):
            return 0
        best = None
        for a, b in queries(t):
            if active_count(a) <= K and active_count(b) <= K:
                num = vi(a) + vi(b)
                assert num % 2 == 0
                z = SCALE + num // 2
                if best is None or z < best:
                    best = z
        assert best is not None
        return best
    return vi

v1i = make_vcap(1)(s4)
v2i = make_vcap(2)(s4)
V1 = Fraction(v1i, SCALE)
V2 = Fraction(v2i, SCALE)
assert V1 == Fraction(2739915, 131072)
assert V1 == Fraction(5, 2) * Vsmall(s3)  # forced-block completion
assert V2 == Fraction(1377453593, 67108864)
assert V1 - V2 == Fraction(25382887, 67108864)
assert V2 < V1
assert cap_calls[1] == 53157
assert cap_calls[2] == 410001

# B24: an explicit deterministic interleaving policy. At each top state,
# choose a child query that is optimal within that child and minimizes the
# exact whole-child lottery continuation R; ties use the checker's canonical
# integer-state order. This gives a completely specified zero-error policy.
@lru_cache(None)
def child_opt_moves(c):
    if c == 0:
        return ((1, 2),)
    xs = [(Fraction(1) + (Vsmall(a)+Vsmall(b))/2, a, b) for a, b in queries(c)]
    z = min(v for v, a, b in xs)
    return tuple((a, b) for v, a, b in xs if v == z)

@lru_cache(None)
def lottery(ws, qs):
    ws = tuple(Fraction(x) for x in ws)
    qs = tuple(Fraction(x) for x in qs)
    @lru_cache(None)
    def g(st):
        if sum(x == 1 for x in st) >= 2 or sum(x == 0 for x in st) >= 2:
            return Fraction(0)
        best = None
        for i in range(3):
            if st[i] == -1:
                sp = list(st); sm = list(st)
                sp[i] = 1; sm[i] = 0
                z = ws[i] + qs[i]*g(tuple(sp)) + (1-qs[i])*g(tuple(sm))
                if best is None or z < best:
                    best = z
        return best
    init = tuple(-1 if 0 < qs[i] < 1 else int(qs[i] > Fraction(1,2)) for i in range(3))
    return g(init)

@lru_cache(None)
def R(t):
    if t in (1, 2):
        return Fraction(0)
    ch = children[t]
    return lottery(tuple(Vsmall(c) for c in ch), tuple(posterior(c) for c in ch))

@lru_cache(None)
def base_policy(t):
    ch = children[t]
    best = None
    for i, c in enumerate(ch):
        if c in (1, 2):
            continue
        if i and c == ch[i-1]:
            continue
        for cp, cm in child_opt_moves(c):
            aa = list(ch); bb = list(ch)
            aa[i] = cp; bb[i] = cm
            a = norm3(*aa); b = norm3(*bb)
            h = Fraction(1) + (R(a)+R(b))/2
            cand = (h, a, b)
            if best is None or cand < best:
                best = cand
    assert best is not None
    return best[1], best[2]

@lru_cache(None)
def Ebase(t):
    if t in (1, 2):
        return Fraction(0)
    a, b = base_policy(t)
    return Fraction(1) + (Ebase(a)+Ebase(b))/2

@lru_cache(None)
def hit3(t):
    if active_count(t) >= 3:
        return Fraction(1)
    if t in (1, 2):
        return Fraction(0)
    a, b = base_policy(t)
    return (hit3(a)+hit3(b))/2

E = Ebase(s4)
assert E == Fraction(10885886259, 536870912)
assert V2 - E == Fraction(133742485, 536870912) > 0
H3 = hit3(s4)
assert H3 == Fraction(2054614931, 2147483648)

# Reachable-state interleaving-width histogram for the explicit policy.
seen = set(); stack = [s4]
while stack:
    t = stack.pop()
    if t in seen:
        continue
    seen.add(t)
    if t not in (1, 2):
        stack.extend(base_policy(t))
hist = {}
for t in seen:
    k = active_count(t)
    hist[k] = hist.get(k, 0) + 1
expected_hist = {0:54, 1:290, 2:638, 3:848, 4:752, 5:515, 6:276, 7:95, 8:24, 9:3}
assert len(seen) == 3495
assert hist == expected_hist
assert max(hist) == 9

# Since this explicit unrestricted policy beats the exact optimum over all
# width<=2 policies, no unrestricted optimal policy can have width <=2.
assert E < V2

print('C0021 B6/B18/B24 exact self-check')
print('S4_q', posterior(s4))
print('S4_abs_m', abs(2*posterior(s4)-1))
print('S3_V', Vsmall(s3))
print('cap1_value', V1)
print('cap2_value', V2)
print('cap1_minus_cap2', V1-V2)
print('cap1_dp_states', cap_calls[1])
print('cap2_dp_states', cap_calls[2])
print('explicit_policy_value', E)
print('cap2_minus_explicit', V2-E)
print('explicit_hit_width_ge_3_probability', H3)
print('explicit_reachable_states', len(seen))
print('explicit_width_histogram', sorted(hist.items()))
print('explicit_max_width', max(hist))
print('CONCLUSION any unrestricted optimum for S4 has interleaving width at least 3')
print('ALL_EXACT_B6_B18_B24_CHECKS_PASS')
