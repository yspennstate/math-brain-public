"""(1) one-point flips of width-2 tribes up to n=16: prime functions with rho_0 above 6;
   (2) spectral block defect eps(f) = min over blocks A of 1 - sigma_1(M_A)^2/||M_A||_F^2,
       M_A[S_A,S_B] = fhat(S_A u S_B), S_A nonempty in A, S_B in B  (eps = 0 iff A is a block)."""
import sys, json, time
import numpy as np
sys.path.insert(0, '.')
from core import polite, stats, is_prime, tt_from_pred, walsh_int, relevant, find_blocks
polite()
out = open('../logs/flips_and_defect.log', 'w')
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()
def dnf(n, terms):
    return tt_from_pred(n, lambda b: any(all(b[i] for i in T) for T in terms))

log('== (1) width-2 tribes and one-point flips')
for sN in (8,):
    n = 2 * sN
    t = dnf(n, [(2*i, 2*i+1) for i in range(sN)])
    s = stats(t)
    log('tribes w2 s%d: rho0=%.6f H/I=%.5f prime=%s' % (sN, s['rho0'], s['ratio'], is_prime(t)))
    for x in (0, int('01' * sN, 2), int('0001' * (sN // 2), 2)):
        t2 = t.copy(); t2[x] = -t2[x]
        t0 = time.time()
        s2 = stats(t2); pr = is_prime(t2)
        log('  flip x=%s: rho0=%.6f H/I=%.5f prime=%s (%.0fs)' % (format(x, '0%db' % n), s2['rho0'], s2['ratio'], pr, time.time() - t0))

def eps_defect(t, maxA=None):
    t = np.ascontiguousarray(t, dtype=np.int8)
    N = t.shape[0]; n = int(round(np.log2(N)))
    W = walsh_int(t) / N
    rel = relevant(t); k = len(rel)
    best = (np.inf, None, None)
    for mask in range(1, 1 << k):
        A = [rel[j] for j in range(k) if (mask >> j) & 1]
        if len(A) < 2 or len(A) > k - 1: continue
        B = [i for i in range(n) if i not in A]
        # index sets
        a = np.arange(1, 1 << len(A)); b = np.arange(1 << len(B))
        SA = np.zeros(a.size, dtype=np.int64); SB = np.zeros(b.size, dtype=np.int64)
        for j, i in enumerate(A): SA |= ((a >> j) & 1) << i
        for j, i in enumerate(B): SB |= ((b >> j) & 1) << i
        M = W[SA[:, None] | SB[None, :]]
        fro = float((M * M).sum())
        if fro < 1e-15: continue
        s1 = np.linalg.norm(M, 2) ** 2
        e = 1 - s1 / fro
        if e < best[0]:
            best = (e, tuple(A), fro - s1)
    return best

log('== (2) spectral block defect')
rows = []
cands = {}
cands['C_10 cycle 2-DNF (prime, rho0 5.297)'] = dnf(10, [(i, (i+1) % 10) for i in range(10)])
cands['P_10 path 2-DNF'] = dnf(10, [(i, i+1) for i in range(9)])
cands['tribes w2 s5 (composite)'] = dnf(10, [(2*i, 2*i+1) for i in range(5)])
t = cands['tribes w2 s5 (composite)'].copy(); t[0] = -t[0]
cands['tribes w2 s5, point 0 flipped'] = t
r7 = [l for l in open('../logs/search_rho0_n7_s12.log') if 'prime=True' in l][0]
tab7 = r7.split('P7[')[1].split('|')[0]
cands['n=7 annealed prime, rho0 5.0866'] = np.array([-1 if ch == '1' else 1 for ch in tab7], dtype=np.int8)
cands['J6 maximiser (6.347)'] = np.array([-1 if ch == '1' else 1 for ch in json.load(open('../logs/search_J_n6_s1.json'))[0]['table']], dtype=np.int8)
rng = np.random.default_rng(5)
cands['random balanced n=8'] = np.array(rng.permutation([1] * 128 + [-1] * 128), dtype=np.int8)
cands['MAJ5 (prime)'] = tt_from_pred(5, lambda b: b.sum() >= 3)
for name, t in cands.items():
    s = stats(t)
    e, A, absd = eps_defect(t)
    var = 1 - s['mean'] ** 2
    log('%-40s n=%2d rho0=%.4f prime=%s  eps=%.5f (block %s)  defect weight=%.3e  defect/Var=%.3e  minInf=%.4f' % (
        name, s['n'], s['rho0'], is_prime(t), e, A, absd, absd / var, s['Inf'][s['Inf'] > 1e-12].min()))
