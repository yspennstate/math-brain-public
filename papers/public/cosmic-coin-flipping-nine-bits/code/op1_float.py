"""Rigorous floating-point certificate for Mossel-O'Donnell Open Problem 1 at given n.

With e = t/(2(1+t)), t in (0, inf), e^d (1-e)^(n-d) = t^d (2+t)^(n-d) / (2(1+t))^n, so for a function F
p(x) = q_x(t) / (2(1+t))^n with q_x(t) = sum_y F(y) t^d(x,y) (2+t)^(n-d(x,y)), a polynomial with NONNEGATIVE integer
coefficients.  R_k(t) = sum_x [ q1_x(t)^k - qF_x(t)^k ] equals 2^(n-1) (2(1+t))^(nk) (P_k(MAJ1) - P_k(F)).
For balanced F the coefficients of t^0, t^(nk) and t^(nk-1) of R_k vanish exactly (they are 2^(nk)|F^-1(1)|,
2^((n-1)k) 2^n and k 2^((n-1)(k-1)) n 2^(n-1) 2^n times the same constant for every balanced F).  If every other
coefficient is > 0, then R_k > 0 on (0, inf), i.e. P_k(MAJ1) > P_k(F) on (0, 1/2).
Floating point: all q-coefficients are exact (integers <= 4^n <= 2^18); powers and sums of nonnegative numbers computed with
m roundings have relative error <= m u / (1 - m u) (Higham, Lemma 3.1); m <= (k-1)(n+2) + N + 1 here.  A computed
coefficient c = A - B is certified positive when c > 2 gamma (A + B), gamma = 4 m u / (1 - m u) (a factor 4 to spare).
Usage: python op1_float.py n kmin kmax [outfile]
"""
import sys, time, json
import numpy as np

n = int(sys.argv[1]); KMIN = int(sys.argv[2]); KMAX = int(sys.argv[3]); out = sys.argv[4] if len(sys.argv) > 4 else None
N = 1 << n
pref = [[bin(x >> (n - 1 - m)).count('1') for m in range(n)] for x in range(N)]   # prefix sums, bit n-1 leftmost
up = [0] * N; down = [0] * N
for x in range(N):
    px = pref[x]
    for y in range(N):
        if all(a <= c for a, c in zip(px, pref[y])):
            up[x] |= 1 << y; down[y] |= 1 << x
FULL = (1 << N) - 1
comp = lambda x: (N - 1) ^ x
funcs = []
def rec(IN, OUT):
    if IN & OUT:
        return
    und = FULL & ~(IN | OUT)
    if not und:
        funcs.append(IN); return
    x = (und & -und).bit_length() - 1
    rec(IN | up[x], OUT | down[comp(x)])
    rec(IN | up[comp(x)], OUT | down[x])
t0 = time.time()
sys.setrecursionlimit(10000)
rec(0, 0)
print(f"n={n}: {len(funcs)} antisymmetric left-monotone functions ({time.time()-t0:.0f}s)", flush=True)

def table(F):
    return np.frombuffer(F.to_bytes(N // 8, 'little'), dtype=np.uint8)
Fall = np.unpackbits(np.stack([table(F) for F in funcs]), axis=1, bitorder='little')  # (M, N) uint8
assert (Fall.sum(1) == N // 2).all() and (Fall + Fall[:, ::-1] == 1).all()
dict1 = (np.arange(N) >> (n - 1)) & 1
idx1 = np.where((Fall == dict1).all(1))[0]
assert len(idx1) == 1

d = np.array([[bin(x ^ y).count('1') for y in range(N)] for x in range(N)])
Ind = np.stack([(d == j) for j in range(n + 1)], axis=-1).astype(np.float64).reshape(N, N * (n + 1))
C = np.zeros((n + 1, n + 1))                   # C[j] = coefficients of t^j (2+t)^(n-j)
for j in range(n + 1):
    poly = np.array([1.0])
    for _ in range(n - j):
        poly = np.convolve(poly, [2.0, 1.0])
    C[j, j:j + len(poly)] = poly

def qcoef(Fb):
    cnt = (Fb.astype(np.float64) @ Ind).reshape(len(Fb), N, n + 1)
    return cnt @ C                               # (B, N, n+1), exact integers

def power_sums(q):
    """S[k] = sum_x q_x^k coefficient vectors, k = 1..KMAX, computed by repeated convolution."""
    B = q.shape[0]; S = {}
    cur = q.copy()
    for k in range(2, KMAX + 1):
        L = cur.shape[2]
        new = np.zeros((B, N, L + n))
        for i in range(n + 1):
            new[:, :, i:i + L] += cur * q[:, :, i:i + 1]
        cur = new
        if k >= KMIN:
            S[k] = cur.sum(axis=1)
    return S

u = 2.0 ** -53
S1 = power_sums(qcoef(Fall[idx1]))
res = {'n': n, 'count': len(funcs), 'by_k': {}}
fails = {k: [] for k in range(KMIN, KMAX + 1)}
minmargin = {k: np.inf for k in range(KMIN, KMAX + 1)}
BATCH = 200
for s in range(0, len(funcs), BATCH):
    Fb = Fall[s:s + BATCH]
    S = power_sums(qcoef(Fb))
    for k in range(KMIN, KMAX + 1):
        m = (k - 1) * (n + 2) + N + 1
        gamma = 4 * m * u / (1 - m * u)
        A = S1[k][0][None, :]; Bk = S[k]
        c = A - Bk
        mid = slice(1, n * k - 1)               # coefficients 1 .. nk-2
        ok = (c[:, mid] > 2 * gamma * (A[:, mid] + Bk[:, mid])).all(1)
        isd = np.arange(s, s + len(Fb)) == idx1[0]
        bad = np.where(~ok & ~isd)[0]
        fails[k].extend(int(s + b) for b in bad)
        rel = (c[:, mid] / (A[:, mid] + Bk[:, mid])).min(1)
        rel[isd] = np.inf
        minmargin[k] = min(minmargin[k], float(rel.min()))
    if (s // BATCH) % 100 == 0:
        print(f"  {s + len(Fb)}/{len(funcs)} ({time.time()-t0:.0f}s) fails so far " +
              str({k: len(v) for k, v in fails.items()}), flush=True)
for k in range(KMIN, KMAX + 1):
    res['by_k'][k] = {'fails': len(fails[k]), 'fail_idx': fails[k][:50], 'min_rel_margin': minmargin[k]}
    print(f"k={k}: certified {len(funcs) - 1 - len(fails[k])} of {len(funcs) - 1}, "
          f"smallest (A-B)/(A+B) over middle coefficients {minmargin[k]:.3e}", flush=True)
if out:
    res['fail_tables'] = {k: [hex(funcs[i]) for i in v[:50]] for k, v in fails.items()}
    json.dump(res, open(out, 'w'), indent=1)
print(f"done ({time.time()-t0:.0f}s)")
