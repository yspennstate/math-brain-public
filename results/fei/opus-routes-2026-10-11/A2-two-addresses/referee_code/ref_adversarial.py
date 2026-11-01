"""Adversarial families for the two-address class (exact K2 membership, exact sign of H - c* I).

(1) X008 rebuilt from ONE_BIT_ENDPOINT.md section 3 (six variables): Booleanity, H = 5, I = 17/8, membership,
    exact row analysis at |C| = 4 (Lemmas 1-6 on a row the n <= 5 enumeration never sees).
(2) Parity lifts f(x,z) = g(x_1 z, ..., x_k z) of every g on k <= 4 variables (n <= 5): membership for every pair.
(3) X002 selector splice (uniform spectrum) for m = 3, 5.
(4) X009 sparse bent perturbation F(t,y) = g(y)(1 - 2 t 1_{y=0}) for m = 2, 4, 6 (bent g), plus one-point flips
    of bent functions with extra coordinates.
(5) Structured random K2 candidates at n = 6..10: the 2-bit fibre at x is chosen by a random decision tree on x;
    each leaf is either a signed character chi_T(y) times a random character on x, or a bent fibre whose four
    signs are random characters of x (sign product -1 enforced).  Exact membership test, then exact sign of
    H - c* I for every member, plus the exact chain H - c* I <= Phi <= 0 (route's Phi) on a subsample.
(6) Corollary A' (signed-character selectors, any number of addresses): H <= 4 (I - Inf_y) on random members
    with |y| = 2..4."""
import sys, json, random, itertools, time
from fractions import Fraction
import numpy as np
from refk2 import walsh_int, LogLin, H_minus_cI_exact, in_K, rows_of, is_product_law_int, H_float, I_exact
from ref_rows import analyse_row

t0 = time.time()
out = {}
random.seed(20261012)


def bits(z, n):
    return [-1 if (z >> i) & 1 else 1 for i in range(n)]


def K2_pairs(W, n):
    return [A for A in itertools.combinations(range(n), 2) if in_K(W, n, A)]


def exact_report(f, n):
    W = walsh_int(np.array(f, dtype=np.int64))
    Q, Itot = H_minus_cI_exact(W, n)
    return W, Q, Itot


# ---------------- (1) X008
g = [1, -1, -1, 0, -1, 0, 0, 1, -1, -1, -1, 0, -1, 0, 0, 1]
gW = walsh_int(np.array(g, dtype=np.int64))
print("X008 g: 16 ghat =", list(gW))
h = {}
for k, low in enumerate((3, 5, 6), start=1):
    h[k] = [1 if (x & 7) == low else 0 for x in range(16)]
assert all((g[x] != 0) + h[1][x] + h[2][x] + h[3][x] == 1 for x in range(16))
n = 6
F = []
for z in range(1 << n):
    y1, y2 = bits(z, 2)
    x = z >> 2
    F.append(g[x] + y1 * h[1][x] + y2 * h[2][x] + y1 * y2 * h[3][x])
assert all(v in (1, -1) for v in F)
W, Q, Itot = exact_report(F, n)
Hx = H_float(W, n)
infl = [sum(Fraction(int(W[S]) ** 2, 4 ** n) for S in range(1 << n) if (S >> i) & 1) for i in range(n)]
print("X008: H =", Hx, " I =", Itot, " influences =", [str(v) for v in infl], " H/I =", Hx / float(Itot))
print("X008 in K2 with pair (0,1):", in_K(W, n, (0, 1)), "; sign(H - c* I) =", Q.sign())
rows, C = rows_of(W, n, (0, 1))
for t in range(4):
    res = analyse_row(rows[t], 4, n, bin(t).count("1"))
    print(f"   row T={t}: w={res['w']} r={res['r']} pairs={res['pairs']} nu'={res['nup']} odd={res['odd']} "
          f"ec={res['ec']} zero_one={res['zero_one']}")
out["X008"] = dict(H=Hx, I=str(Itot), ratio=Hx / float(Itot), sign=Q.sign())

# ---------------- (2) parity lifts
lift_members = 0
lift_tested = 0
lift_bad = 0
lift_max = 0.0
for k in (2, 3, 4):
    n = k + 1
    for code in range(1 << (1 << k)):
        gv = [1 - 2 * ((code >> x) & 1) for x in range(1 << k)]
        f = []
        for zz in range(1 << n):
            xs = bits(zz, n)
            zbit = xs[k]
            arg = 0
            for i in range(k):
                if xs[i] * zbit == -1:
                    arg |= 1 << i
            f.append(gv[arg])
        W = walsh_int(np.array(f, dtype=np.int64))
        if np.count_nonzero(W[1:]) == 0:
            continue
        lift_tested += 1
        if not K2_pairs(W, n):
            continue
        lift_members += 1
        Q, Itot = H_minus_cI_exact(W, n)
        if Q.sign() > 0:
            lift_bad += 1
        lift_max = max(lift_max, H_float(W, n) / float(Itot))
print(f"parity lifts (k<=4): tested {lift_tested}, in K2 {lift_members}, violations {lift_bad}, max H/I {lift_max:.6f}",
      f"{time.time()-t0:.0f}s", flush=True)
out["parity_lifts"] = dict(tested=lift_tested, in_K2=lift_members, violations=lift_bad, max_ratio=lift_max)

# ---------------- (3) X002
for m in (3, 5):
    nb = m - 1
    def b(t):
        s = 0
        for i in range(0, nb, 2):
            s += t[i] * t[i + 1]
        return -1 if s % 2 else 1
    n = m + 1
    f = []
    for zz in range(1 << n):
        yb = [(zz >> i) & 1 for i in range(m)]
        sel = (zz >> m) & 1
        tt = [(yb[i] + yb[m - 1]) % 2 for i in range(m - 1)]
        g0 = b(tt)
        f.append(g0 if sel == 0 else (-1) ** yb[m - 1] * g0)
    W = walsh_int(np.array(f, dtype=np.int64))
    pr = K2_pairs(W, n)
    Q, Itot = H_minus_cI_exact(W, n)
    print(f"X002 m={m}: n={n} H={H_float(W, n):.4f} I={Itot} in K2: {bool(pr)} sign(H-c*I)={Q.sign()}")
    out[f"X002_m{m}"] = dict(H=H_float(W, n), I=str(Itot), inK2=bool(pr), sign=Q.sign())

# ---------------- (4) X009 and one-point flips of bent functions
for m in (2, 4, 6):
    n = m + 1
    f = []
    for zz in range(1 << n):
        yb = [(zz >> i) & 1 for i in range(m)]
        t = (zz >> m) & 1
        s = sum(yb[i] * yb[i + 1] for i in range(0, m, 2)) % 2
        gval = -1 if s else 1
        if t == 1 and all(v == 0 for v in yb):
            gval = -gval
        f.append(gval)
    W = walsh_int(np.array(f, dtype=np.int64))
    pr = K2_pairs(W, n)
    Q, Itot = H_minus_cI_exact(W, n)
    print(f"X009 m={m}: n={n} H/I={H_float(W, n)/float(Itot):.4f} pairs in K2: {pr[:3]}{'...' if len(pr)>3 else ''} "
          f"sign(H-c*I)={Q.sign()}")
    out[f"X009_m{m}"] = dict(ratio=H_float(W, n) / float(Itot), K2_pairs=len(pr), sign=Q.sign())
# one-point flips: bent b on 4 bits times extra variables, flip k points
flip_members = 0; flip_bad = 0; flip_max = 0.0; flip_tested = 0
for extra in (0, 1, 2):
    n = 4 + extra
    base = []
    for zz in range(1 << n):
        yb = [(zz >> i) & 1 for i in range(4)]
        base.append(-1 if (yb[0] * yb[1] + yb[2] * yb[3]) % 2 else 1)
    for kflip in (1, 2, 3):
        cnt = 0
        for pts in itertools.combinations(range(1 << n), kflip):
            cnt += 1
            if cnt > 2500:
                break
            f = list(base)
            for p in pts:
                f[p] = -f[p]
            W = walsh_int(np.array(f, dtype=np.int64))
            flip_tested += 1
            if not K2_pairs(W, n):
                continue
            flip_members += 1
            Q, Itot = H_minus_cI_exact(W, n)
            if Q.sign() > 0:
                flip_bad += 1
            flip_max = max(flip_max, H_float(W, n) / float(Itot))
print(f"bent flips: tested {flip_tested}, in K2 {flip_members}, violations {flip_bad}, max H/I {flip_max:.6f}",
      f"{time.time()-t0:.0f}s", flush=True)
out["bent_flips"] = dict(tested=flip_tested, in_K2=flip_members, violations=flip_bad, max_ratio=flip_max)

# ---------------- (5) structured random K2 candidates
BENT_PATTERNS = [s for s in itertools.product((1, -1), repeat=4) if s[0] * s[1] * s[2] * s[3] == -1]


def random_tree(m, depth):
    """random decision tree on x in {0..2^m-1}: returns a function x -> leaf id and the leaves' free coordinates"""
    leaves = []
    def build(fixed, d):
        free = [i for i in range(m) if i not in fixed]
        if d == 0 or not free or random.random() < 0.25:
            leaves.append(dict(fixed=dict(fixed), free=free))
            return
        i = random.choice(free)
        for v in (0, 1):
            fx = dict(fixed); fx[i] = v
            build(fx, d - 1)
    build({}, depth)
    def leaf_of(x):
        for k, L in enumerate(leaves):
            if all(((x >> i) & 1) == v for i, v in L["fixed"].items()):
                return k
        raise RuntimeError
    return leaves, leaf_of


def chi(x, S):
    return -1 if bin(x & S).count("1") % 2 else 1


struct_stats = {}
chain_checked = 0
for m in (4, 5, 6, 7, 8):
    n = m + 2
    tested = members = bad = 0
    best = 0.0
    budget_t = time.time()
    while tested < (400 if m <= 6 else 150) and time.time() - budget_t < 70:
        leaves, leaf_of = random_tree(m, random.randint(1, 4))
        spec = []
        for L in leaves:
            fmask = sum(1 << i for i in L["free"])
            if random.random() < 0.5:
                T = random.randrange(4)
                S = random.randrange(1 << m) & fmask if fmask else 0
                spec.append(("char", T, S, random.choice((1, -1))))
            else:
                # bent fibre: four signs = sign_k * chi_{S_k}(x) with product of the four constant signs fixed
                Ss = [random.randrange(1 << m) & fmask if fmask else 0 for _ in range(4)]
                # sign product of chi's must be +1 pointwise: force S_3 = S_0 ^ S_1 ^ S_2
                Ss[3] = Ss[0] ^ Ss[1] ^ Ss[2]
                pat = random.choice(BENT_PATTERNS)
                spec.append(("bent", Ss, pat))
        f = []
        for zz in range(1 << n):
            y1, y2 = bits(zz, 2)
            x = zz >> 2
            sp = spec[leaf_of(x)]
            chis = [1, y1, y2, y1 * y2]
            if sp[0] == "char":
                _, T, S, sg = sp
                f.append(sg * chi(x, S) * chis[T])
            else:
                _, Ss, pat = sp
                v = sum(Fraction(pat[k] * chi(x, Ss[k]), 2) * chis[k] for k in range(4))
                f.append(int(v))
        assert all(v in (1, -1) for v in f)
        W = walsh_int(np.array(f, dtype=np.int64))
        tested += 1
        if np.count_nonzero(W[1:]) == 0:
            continue
        if not in_K(W, n, (0, 1)):
            continue
        members += 1
        Q, Itot = H_minus_cI_exact(W, n)
        if Q.sign() > 0:
            bad += 1
            print("VIOLATION", m, f)
        best = max(best, H_float(W, n) / float(Itot))
        if chain_checked < 60 and m <= 6:
            rows, C = rows_of(W, n, (0, 1))
            Phi = LogLin()
            for t in range(4):
                res = analyse_row(rows[t], m, n, bin(t).count("1"))
                if res is None:
                    continue
                Phi.add(res["web"])
                d = LogLin().add(res["web"]).add(res["we"], -1)
                assert d.sign() >= 0
            assert Phi.sign() <= 0, "Phi > 0"
            chain_checked += 1
    struct_stats[m] = dict(n=n, tested=tested, members=members, violations=bad, max_ratio=best)
    print(f"structured random m={m} (n={n}): tested {tested}, members {members}, violations {bad}, max H/I {best:.6f}",
          f"{time.time()-t0:.0f}s", flush=True)
out["structured_random"] = struct_stats
out["chain_checked"] = chain_checked
print("exact chain H - c*I <= Phi <= 0 checked on", chain_checked, "structured members (m <= 6)")

# ---------------- (6) Corollary A': signed-character selectors with any |y|
sel_stats = {}
for k in (2, 3, 4):
    for m in (3, 4, 5):
        n = k + m
        tested = members = bad = 0
        worst = -1e9
        tt = time.time()
        while tested < 150 and time.time() - tt < 25:
            leaves, leaf_of = random_tree(m, random.randint(1, 3))
            # distinct or repeated T's on leaves
            Ts = [random.randrange(1 << k) for _ in leaves]
            Ss = [random.randrange(1 << m) & sum(1 << i for i in L["free"]) for L in leaves]
            sg = [random.choice((1, -1)) for _ in leaves]
            f = []
            for zz in range(1 << n):
                y = zz & ((1 << k) - 1)
                x = zz >> k
                lf = leaf_of(x)
                f.append(sg[lf] * chi(x, Ss[lf]) * chi(y, Ts[lf]))
            W = walsh_int(np.array(f, dtype=np.int64))
            tested += 1
            A = tuple(range(k))
            if not in_K(W, n, A):
                continue
            members += 1
            # exact: H - 4 (I - Inf_y) <= 0 ; Inf_y = sum_S |S cap y| p(S)
            D = 4 ** n
            Q = LogLin()
            I_rest = Fraction(0)
            for S in range(1 << n):
                w_ = int(W[S])
                if w_ == 0:
                    continue
                p = Fraction(w_ * w_, D)
                Q.q0 += p * 2 * n
                Q.add_log2_int(-2 * p, abs(w_))
                I_rest += p * bin(S >> k).count("1")
            Q.q0 -= 4 * I_rest
            s_ = Q.sign()
            if s_ > 0:
                bad += 1
            worst = max(worst, float(Q))
        sel_stats[f"k{k}_m{m}"] = dict(tested=tested, members=members, violations=bad, max_H_minus_4Ired=worst)
        print(f"Cor A' |y|={k} m={m}: tested {tested}, members {members}, violations {bad}, max H-4(I-Inf_y) {worst:+.4f}",
              flush=True)
out["corollary_Aprime"] = sel_stats
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "ref_adversarial.json", "w", encoding="utf-8"), indent=1, default=str)
print(f"done {time.time()-t0:.0f}s")
