# Exhaustive check, over all monotone Boolean functions on n <= 6 variables, of the strengthened (O'Donnell-Tan) step:
#   Delta+_v = H+(f) - (H+(f_0) + H+(f_1))/2,   H+(f) = sum_{A nonempty} P(A) log2(1/P(A)),   Var(D_v f) = Inf_v - Inf_v^2.
#  (S1) Delta+_v <= phi(Inf_v^2) + Inf_v (2/ln2 + Psi(4m/Inf_v - 2))          every coordinate
#  (S2) Delta+_v <= 8.80 Var(D_v f)                                           every coordinate with Inf_v >= 1/2
#  (S3) H+(f) <= Cplus(w) (I(f) - Var(f)) for every f whose minterms all have size <= w (w = its DNF width),
#       Cplus(w) = max(8.80, 2 (1.0615 + 2/ln2 + Psi(2^(w+1) - 4))); also for CNF width via maxterms.
# Also checks the identity Delta+_v = phi(Inf^2) + sum_{T nonempty} tau(fhat(T), fhat(T+v)).
import sys, time, numpy as np
from multiprocessing import Pool
from mono_enum import monotone_masks, walsh, phi

JSC = 2 / np.log(2)
def Psi(r):
    r = np.maximum(r, 0.0); return np.log2(np.e * (r + 2 * np.sqrt(r) + 2))
def Cplus(w):
    return max(8.80, 2 * (1.0615 + JSC + float(Psi(np.array(2.0 ** (w + 1) - 4)))))

def widths(mk, n):
    """DNF width (largest minterm) and CNF width (largest maxterm) of each monotone mask."""
    N = 1 << n
    pc = np.array([bin(s).count('1') for s in range(N)])
    bits = ((mk[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(bool)
    # minterms: points x with f(x)=1 and f(x - e_i)=0 for all i in x
    mint = bits.copy()
    for i in range(n):
        has = (np.arange(N) >> i) & 1 == 1
        lower = np.arange(N) & ~(1 << i)
        mint[:, has] &= ~bits[:, lower[has]]
    dnfw = np.where(mint.any(1), (mint * pc[None, :]).max(1), 0)
    # maxterms: complements of maximal zeros: points x with f(x)=0 and f(x + e_i)=1 for all i not in x
    maxz = ~bits
    for i in range(n):
        hasnot = (np.arange(N) >> i) & 1 == 0
        upper = np.arange(N) | (1 << i)
        maxz[:, hasnot] &= bits[:, upper[hasnot]]
    cnfw = np.where(maxz.any(1), (maxz * (n - pc)[None, :]).max(1), 0)
    return dnfw, cnfw

def analyse(args):
    mk, n = args
    N = 1 << n
    G = walsh(mk, n)
    P = G * G
    Hp = phi(P[:, 1:]).sum(1)                      # H+ : nonempty sets
    pc = np.array([bin(s).count('1') for s in range(N)], dtype=np.float64)
    I = (P * pc[None, :]).sum(1)
    Var = 1.0 - P[:, 0]
    q = (1.0 + G[:, 0]) / 2.0
    m = np.minimum(q, 1.0 - q)
    w1 = w2 = 0.0; wid = 0.0; worst1 = worst2 = None
    for v in range(n):
        idx0 = np.array([s for s in range(N) if not (s >> v) & 1])
        a = G[:, idx0]; b = G[:, idx0 | (1 << v)]
        inf = (b * b).sum(1)
        # H+ of restrictions: spectra (a +- b)^2 over T (T subset of [n]-v), nonempty T only
        hp0 = phi(((a + b) ** 2)[:, 1:]).sum(1); hp1 = phi(((a - b) ** 2)[:, 1:]).sum(1)
        dplus = Hp - 0.5 * (hp0 + hp1)
        # identity check
        tau = (phi(a * a) + phi(b * b) - 0.5 * (phi((a + b) ** 2) + phi((a - b) ** 2)))[:, 1:].sum(1)
        ident = dplus - (phi(inf ** 2) + tau)
        wid = max(wid, float(np.abs(ident).max()))
        rel = inf > 1e-14
        infs = np.where(rel, inf, 1.0)
        b1 = phi(inf ** 2) + inf * (JSC + Psi(4 * m / infs - 2))
        r1 = np.where(rel, dplus / np.where(b1 > 0, b1, 1.0), 0.0)
        k = int(np.argmax(r1))
        if r1[k] > w1: w1 = float(r1[k]); worst1 = (int(mk[k]), v, float(dplus[k]), float(b1[k]))
        big = inf >= 0.5
        vd = inf - inf ** 2
        r2 = np.where(big & (vd > 1e-14), dplus / np.where(vd > 1e-14, 8.80 * vd, 1.0), 0.0)
        k = int(np.argmax(r2))
        if r2[k] > w2: w2 = float(r2[k]); worst2 = (int(mk[k]), v, float(dplus[k]), float(vd[k]))
    dw, cw = widths(mk, n)
    res = {}
    for w in range(1, n + 1):
        for name, width in (('dnf', dw), ('cnf', cw)):
            sel = (width <= w) & (I - Var > 1e-14)
            if sel.any():
                r = Hp[sel] / (Cplus(w) * (I - Var)[sel])
                res[(name, w)] = float(r.max())
    return w1, worst1, w2, worst2, wid, res

if __name__ == '__main__':
    try:
        import psutil
        p = psutil.Process(); p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); p.cpu_affinity(list(range(2, 16)))
    except Exception as e:
        print('priority/affinity not set:', e)
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    print('Cplus(w):', ['%.3f' % Cplus(w) for w in range(1, 7)])
    for n in [int(t) for t in sys.argv[1].split(',')]:
        t0 = time.time()
        masks = monotone_masks(n)
        jobs = [(masks[s:s + 50000], n) for s in range(0, len(masks), 50000)]
        W1 = W2 = WID = 0.0; X1 = X2 = None; RES = {}
        with Pool(workers) as pool:
            for w1, x1, w2, x2, wid, res in pool.imap_unordered(analyse, jobs):
                if w1 > W1: W1, X1 = w1, x1
                if w2 > W2: W2, X2 = w2, x2
                WID = max(WID, wid)
                for k, v in res.items(): RES[k] = max(RES.get(k, 0.0), v)
        print('n %d: %d functions (%.1f s); identity error %.2e' % (n, len(masks), time.time() - t0, WID))
        print('   S1 max Delta+/bound = %.6f at %s' % (W1, X1))
        print('   S2 max Delta+/(8.80 Var(D)) over Inf >= 1/2 = %.6f at %s' % (W2, X2))
        print('   S3 max H+/(Cplus(w)(I-Var)):', ', '.join('%s w=%d: %.4f' % (k[0], k[1], v) for k, v in sorted(RES.items())), flush=True)
