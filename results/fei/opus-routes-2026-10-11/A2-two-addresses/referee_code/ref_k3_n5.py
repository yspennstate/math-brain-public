"""Independent check of A2-E-k3: three spectral addresses at n = 5 (addresses y = coordinates 0,1,2; C = {3,4}).

Method (different from the route's): f <-> four fibres F_x (Boolean functions of y, one per x in {+-1}^2).
Row T is g_T(x) = Fhat_x(T).  A law on two bits is product iff q00 q11 = q01 q10; for the squared Walsh law of a
row with values g00, g01, g10, g11 this is equivalent (derivation in REFEREE.md) to
      (g00 g11 - g01 g10) * (g00^2 + g11^2 - g01^2 - g10^2) = 0 .
So the class condition is pointwise in (pair (F00,F11), pair (F01,F10)): for every T,
      a_T = c_T  or  b_T = d_T,  a = G00 G11, b = G00^2 + G11^2, c = G01 G10, d = G01^2 + G10^2.
F00 is reduced to orbit representatives under y-translations, y-permutations and negation (each preserves H, I and
the class); F11, F01, F10 range over all 256 fibres.  Max H/I is computed in floats and the maximisers are
checked exactly against H/I(AND_4) = (6 - (49/32) log2 7) / (1/2)."""
import itertools, json, sys, time
from fractions import Fraction
import numpy as np
from refk2 import walsh_int, LogLin, H_float, in_K

t0 = time.time()
# fibres: Boolean functions of 3 bits, index y in 0..7 (bit i = y_i = -1)
FIB = np.array([[1 - 2 * ((k >> y) & 1) for y in range(8)] for k in range(256)], dtype=np.int64)
G = walsh_int(FIB)          # G[k][T] = sum_y F(y) chi_T(y)  (8 * Fhat)


def orbit_reps():
    perms = list(itertools.permutations(range(3)))
    seen = set()
    reps = []
    for k in range(256):
        if k in seen:
            continue
        orb = set()
        for t in range(8):
            for pm in perms:
                for neg in (0, 1):
                    kk = 0
                    for y in range(8):
                        src = y ^ t                    # f'(pi(y)) = f(y xor t) xor neg
                        z = 0
                        for i in range(3):
                            if (y >> i) & 1:
                                z |= 1 << pm[i]
                        val = (k >> src) & 1
                        val ^= neg
                        if val:
                            kk |= 1 << z
                    orb.add(kk)
        seen |= orb
        reps.append(k)
    return reps


reps = orbit_reps()
print("orbit representatives of the x=00 fibre:", len(reps), flush=True)
popT = np.array([bin(T).count("1") for T in range(8)])
Uw = np.array([0, 1, 1, 2])           # |U| for U in {}, {3}, {4}, {3,4}
CH = np.array([[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, 1, -1], [1, -1, -1, 1]])  # rows U, cols x=(b3,b4) as 00,01,10,11
count = 0
best = 0.0
best_combo = None
ties = []
for F00 in reps:
    for F11 in range(256):
        a = G[F00] * G[F11]
        b = G[F00] ** 2 + G[F11] ** 2
        c = G[:, None, :] * G[None, :, :]
        d = G[:, None, :] ** 2 + G[None, :, :] ** 2
        ok = ((a[None, None, :] == c) | (b[None, None, :] == d)).all(axis=2)
        i01, i10 = np.nonzero(ok)
        if len(i01) == 0:
            continue
        count += len(i01)
        # rows: g_T(x) * 8 for x = 00, 01, 10, 11 ; shape (V, 8 T, 4 x)
        R = np.stack([np.broadcast_to(G[F00], (len(i01), 8)), G[i01], G[i10], np.broadcast_to(G[F11], (len(i01), 8))], axis=2)
        Wc = np.einsum('vtx,ux->vtu', R, CH)       # 32 * ghat_T(U)
        p = (Wc.astype(np.float64) / 32.0) ** 2
        It = (p * (popT[None, :, None] + Uw[None, None, :])).sum(axis=(1, 2))
        with np.errstate(divide="ignore", invalid="ignore"):
            Ht = -(np.where(p > 0, p * np.log2(np.where(p > 0, p, 1)), 0)).sum(axis=(1, 2))
        valid = It > 0
        rat = np.where(valid, Ht / np.where(valid, It, 1), 0)
        j = int(np.argmax(rat))
        if rat[j] > best + 1e-12:
            best = float(rat[j])
            best_combo = (F00, int(i01[j]), int(i10[j]), F11)
        near = np.nonzero(rat > 3.4024755)[0]
        for jj in near[:5]:
            if len(ties) < 50:
                ties.append((F00, int(i01[jj]), int(i10[jj]), F11))
print("functions with F00 a representative:", count, " max H/I =", best, f"{time.time()-t0:.0f}s", flush=True)


def build(combo):
    F00, F01, F10, F11 = combo
    fib = {0: F00, 1: F01, 2: F10, 3: F11}   # x index = b3 + 2*b4 ? -> define x = (b3, b4) with code 2*b3 + b4
    f = []
    for z in range(32):
        y = z & 7
        b3 = (z >> 3) & 1
        b4 = (z >> 4) & 1
        k = fib[2 * b3 + b4]
        f.append(1 - 2 * ((k >> y) & 1))
    return f


# exact comparison with AND_4 at the near-maximisers
and4 = LogLin(Fraction(6), {7: Fraction(-49, 32)})   # H(AND_4); I = 1/2
exact_eq = 0
viol = 0
for combo in ties + [best_combo]:
    f = build(combo)
    W = walsh_int(np.array(f, dtype=np.int64))
    assert in_K(W, 5, (0, 1, 2)), "rebuilt function not in the 3-address class"
    D = 4 ** 5
    Hx = LogLin()
    Itot = Fraction(0)
    for S in range(32):
        w_ = int(W[S])
        if w_ == 0:
            continue
        pp = Fraction(w_ * w_, D)
        Hx.q0 += pp * 10
        Hx.add_log2_int(-2 * pp, abs(w_))
        Itot += pp * bin(S).count("1")
    # H/I - H4/(1/2) = (H - 2 I H4)/I : sign of H - 2 I H(AND_4)
    diff = LogLin().add(Hx).add(and4, -2 * Itot)
    s_ = diff.sign()
    if s_ == 0:
        exact_eq += 1
    if s_ > 0:
        viol += 1
print("near-maximisers checked exactly:", len(ties) + 1, " equal to H/I(AND_4):", exact_eq, " exceeding it:", viol)
json.dump(dict(reps=len(reps), count=count, max_ratio=best, exact_equal=exact_eq, exceeding=viol),
          open(sys.argv[1] if len(sys.argv) > 1 else "ref_k3_n5.json", "w", encoding="utf-8"), indent=1)
