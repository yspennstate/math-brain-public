"""Three spectral addresses (k = 3), n = 5: A = 3 y-bits, C = 2 x-bits. Exhaustive over all f (fibers b_x, x in
{0,1,2,3}, each a Boolean function on 3 bits), with the fiber at x = 0 reduced to orbit representatives under
y-translations, y-permutations and negation (each preserves H, I and the conditional-product property for the
same A). Row T: G_T(x) = sum_y b_x(y) chi_T(y); R_T(U) = sum_x G_T(x) chi_U(x); fhat(T u U) = R_T(U)/32.
Row law on 2 bits is product iff R(0)^2 R(3)^2 == R(1)^2 R(2)^2. Floats for logs (evidence)."""
import numpy as np, numba as nb, itertools, math, json, sys, time

def fiber_walsh():
    W = np.zeros((256, 8), dtype=np.int64)
    for b in range(256):
        for T in range(8):
            s = 0
            for y in range(8):
                v = -1 if (b >> y) & 1 else 1
                chi = -1 if bin(T & y).count("1") % 2 else 1
                s += v * chi
            W[b, T] = s
    return W

def orbit_reps():
    seen = set(); reps = []
    for b in range(256):
        if b in seen:
            continue
        reps.append(b)
        for perm in itertools.permutations(range(3)):
            for a in range(8):
                for neg in (0, 1):
                    nb_ = 0
                    for y in range(8):
                        z = 0
                        for k in range(3):
                            if y >> k & 1:
                                z |= 1 << perm[k]
                        v = (b >> (y ^ a)) & 1
                        v ^= neg
                        if v:
                            nb_ |= 1 << z
                    seen.add(nb_)
    return reps

@nb.njit(cache=True)
def popc(x):
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c

@nb.njit(cache=True)
def run(W, reps):
    best = 0.0; bestf = np.zeros(4, dtype=np.int64); count = 0
    R = np.zeros((8, 4), dtype=np.int64)
    chi = np.array([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]], dtype=np.int64)  # chi[U][x]
    for ri in range(len(reps)):
        b0 = reps[ri]
        for b1 in range(256):
            for b2 in range(256):
                for b3 in range(256):
                    ok = True
                    for T in range(8):
                        g0 = W[b0, T]; g1 = W[b1, T]; g2 = W[b2, T]; g3 = W[b3, T]
                        for U in range(4):
                            R[T, U] = g0 * chi[U, 0] + g1 * chi[U, 1] + g2 * chi[U, 2] + g3 * chi[U, 3]
                        if R[T, 0] * R[T, 0] * R[T, 3] * R[T, 3] != R[T, 1] * R[T, 1] * R[T, 2] * R[T, 2]:
                            ok = False
                            break
                    if not ok:
                        continue
                    count += 1
                    H = 0.0; I = 0.0
                    for T in range(8):
                        for U in range(4):
                            if R[T, U] != 0:
                                p = R[T, U] * R[T, U] / 1024.0
                                H -= p * math.log2(p)
                                I += p * (popc(T) + popc(U))
                    if I > 0 and H / I > best + 1e-12:
                        best = H / I
                        bestf[0] = b0; bestf[1] = b1; bestf[2] = b2; bestf[3] = b3
    return best, bestf, count

if __name__ == "__main__":
    t0 = time.time()
    W = fiber_walsh(); reps = np.array(orbit_reps(), dtype=np.int64)
    print("orbit reps of 3-bit functions:", len(reps), flush=True)
    best, bestf, count = run(W, reps)
    print("K_3 at n=5: functions (row-0-fiber reduced):", count, " max H/I =", best, " fibers", list(bestf),
          " time", round(time.time() - t0, 1))
    with open(sys.argv[1], "w", encoding="utf-8") as fh:
        json.dump(dict(max_ratio=best, fibers=[int(v) for v in bestf], count=int(count)), fh)
