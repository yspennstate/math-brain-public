# Checks for the proof of L(F_n) = L(F_{n+1}) (OpenAI, 23 Sep 2026), Sections 2 and 4.
# A. Lemma 4.2/4.3: exact moments of Q = T_m T_m^* at delta_e by free reduction, on the actual words
#    p_j = (a b_1)...(a b_j) in F_3 and on abstract free symbols; against Cat_r (m)_r and against the
#    closed-form law of |sum of m+1 free Haar unitaries|^2 (Kesten-McKay on the (m+1)-regular tree).
# B. Lemma 4.2: the cocycle value D w_m = T_m h, letter by letter.
# C. The cutoff inverse: ||h||^2 and ||T_m h - delta_e||^2 from the closed-form law.
# D. Lemma 2.3 / 2.5 in a random matrix model: freeness of conjugates, norm of a free sum.
import math, time, sys
from collections import defaultdict
import numpy as np
from scipy.integrate import quad

t0 = time.time()
def out(*a):
    print(*a, flush=True)

def mul(a, b):
    i = len(a); j = 0; nb = len(b)
    while i > 0 and j < nb and a[i-1] == -b[j]:
        i -= 1; j += 1
    return a[:i] + b[j:]

def inv(a):
    return tuple(-x for x in reversed(a))

def red(a):
    r = []
    for x in a:
        if r and r[-1] == -x:
            r.pop()
        else:
            r.append(x)
    return tuple(r)

def prefixes_actual(m):
    # a = x1, b_j = x2^j x3 x2^-j, p_j = (a b_1)...(a b_j), in F_3
    ps = [()]
    cur = ()
    for j in range(1, m+1):
        bj = (2,)*j + (3,) + (-2,)*j
        cur = mul(mul(cur, (1,)), bj)
        ps.append(cur)
    return ps

def prefixes_abstract(m):
    return [()] + [(j,) for j in range(1, m+1)]

def moments(ps, rmax):
    Q = defaultdict(int)
    for p in ps:
        for q in ps:
            Q[mul(p, inv(q))] += 1
    Q = dict(Q)
    vs = [{(): 1}]
    kmax = (rmax + 1)//2
    for _ in range(kmax):
        v = vs[-1]; nv = defaultdict(int)
        for w, c in v.items():
            for q, cq in Q.items():
                nv[mul(q, w)] += c*cq
        vs.append(dict(nv))
    def ip(u, v):
        if len(u) > len(v): u, v = v, u
        return sum(c*v.get(w, 0) for w, c in u.items())
    res = []
    for r in range(1, rmax+1):
        k = r//2
        res.append(ip(vs[k], vs[r-k]))
    return res

def cat(r):
    return math.comb(2*r, r)//(r+1)

def falling(m, r):
    x = 1
    for i in range(r): x *= (m-i)
    return x

def km_moment(N, r):
    # law of |u_1+...+u_N|^2, u_i free Haar unitaries: t = s^2, s with the Kesten-McKay density of the N-regular tree
    f = lambda s: s**(2*r) * N*math.sqrt(max(4*(N-1) - s*s, 0.0)) / (math.pi*(N*N - s*s))
    v, _ = quad(f, 0, 2*math.sqrt(N-1), limit=400)
    return v

out("== A. moments of Q_m = T_m T_m^* at delta_e ==")
out("m  r  exact(actual words)  exact(free symbols)  Cat_r*(m)_r  exact/(Cat_r m^r)  closed-form law  rel.diff")
worst = 0.0; mism = 0
for m in (1, 2, 3, 4, 5):
    ea = moments(prefixes_actual(m), 6)
    eb = moments(prefixes_abstract(m), 6)
    for r in range(1, 7):
        km = km_moment(m+1, r)
        rd = abs(km - eb[r-1])/eb[r-1]
        worst = max(worst, rd)
        if ea[r-1] != eb[r-1]: mism += 1
        out(m, r, ea[r-1], eb[r-1], cat(r)*falling(m, r), "%.4f" % (eb[r-1]/(cat(r)*m**r)), "%.6f" % km, "%.1e" % rd)
for m in (6, 8, 10):
    ea = moments(prefixes_actual(m), 4)
    eb = moments(prefixes_abstract(m), 6)
    for r in range(1, 7):
        km = km_moment(m+1, r)
        rd = abs(km - eb[r-1])/eb[r-1]
        worst = max(worst, rd)
        if r <= 4 and ea[r-1] != eb[r-1]: mism += 1
        out(m, r, ea[r-1] if r <= 4 else "-", eb[r-1], cat(r)*falling(m, r), "%.4f" % (eb[r-1]/(cat(r)*m**r)), "%.6f" % km, "%.1e" % rd)
out("actual-word counts differing from free-symbol counts:", mism)
out("largest relative difference, exact count vs closed-form law:", "%.2e" % worst)
out("r=2 formula 2N^2-N with N=m+1:", all(moments(prefixes_abstract(m), 2)[1] == 2*(m+1)**2 - (m+1) for m in range(1, 9)))
# exact - Cat_r (m)_r must be O(m^{r-1}): print (exact - Cat_r (m)_r)/m^{r-1}
out("remainder (exact - Cat_r (m)_r)/m^(r-1), m = 4, 6, 8, 10:")
tab = {m: moments(prefixes_abstract(m), 6) for m in (4, 6, 8, 10)}
for r in range(1, 7):
    out(" r=%d " % r, "  ".join("%.3f" % ((tab[m][r-1] - cat(r)*falling(m, r))/m**(r-1)) for m in (4, 6, 8, 10)))
out("time %.1f s" % (time.time()-t0))

out("== B. cocycle value D w_m = T_m h ==")
rng = np.random.default_rng(197)
def lam(g, v):
    r = defaultdict(int)
    for w, c in v.items(): r[mul(g, w)] += c
    return {w: c for w, c in r.items() if c != 0}
def add(u, v, s=1):
    r = defaultdict(int)
    for w, c in u.items(): r[w] += c
    for w, c in v.items(): r[w] += s*c
    return {w: c for w, c in r.items() if c != 0}
def D(word, hs):
    # word: sequence of letters (not necessarily reduced); D(gb) = Dg + lam(g) Db, D(x^-1) = -lam(x^-1) D x
    acc = {}; g = ()
    for l in word:
        if l > 0:
            dl = hs.get(l, {})
        else:
            dl = {w: -c for w, c in lam((l,), hs.get(-l, {})).items()}
        acc = add(acc, lam(g, dl))
        g = mul(g, (l,))
    return acc
bad = 0; ntest = 0
for trial in range(40):
    h = {}
    for _ in range(int(rng.integers(1, 6))):
        L = int(rng.integers(0, 6))
        w = red(tuple(int(rng.choice([1, -1, 2, -2, 3, -3])) for _ in range(L)))
        h[w] = int(rng.integers(-5, 6)) or 1
    hs = {1: h}
    for m in (1, 2, 3, 5, 7):
        ps = prefixes_actual(m)
        letters = []
        for j in range(1, m+1):
            letters += [1] + [2]*j + [3] + [-2]*j
        letters += [1]
        lhs = D(letters, hs)
        rhs = {}
        for p in ps: rhs = add(rhs, lam(p, h))
        # a non-reduced spelling of the same element must give the same value
        k = int(rng.integers(0, len(letters)+1)); x = int(rng.choice([1, 2, 3, -1, -2, -3]))
        lhs2 = D(letters[:k] + [x, -x] + letters[k:], hs)
        ntest += 1
        if lhs != rhs or lhs2 != rhs: bad += 1
out("random h, m in {1,2,3,5,7}: tests", ntest, " failures", bad)
# with h_2 nonzero the identity must fail (control)
hs = {1: {(): 1}, 2: {(): 1}}
letters = [1, 2, 3, -2, 1]
rhs = add({(): 1}, lam(prefixes_actual(1)[1], {(): 1}))
out("control with h_2 != 0: D w_1 == T_1 h ?", D(letters, hs) == rhs)

out("== C. cutoff inverse, from the closed-form law of P = T_m T_m^* (N = m+1) ==")
def dens_s(N):
    return lambda s: N*math.sqrt(max(4*(N-1) - s*s, 0.0)) / (math.pi*(N*N - s*s))
def nu_cdf(d):
    v, _ = quad(lambda s: math.sqrt(max(4 - s*s, 0.0))/math.pi, 0, math.sqrt(d))
    return v
out("total mass (must be 1):", ["%.8f" % quad(dens_s(N), 0, 2*math.sqrt(N-1), limit=400)[0] for N in (2, 3, 11, 101, 10001)])
out(" m      d      ||T h - delta_e||^2 = mu(P < d m)   nu([0,d])   ||h||^2 = int_{P>=dm} 1/P   1/(d m)")
for d in (1e-1, 1e-2, 1e-3):
    for m in (10, 100, 1000, 10000, 1000000):
        N = m+1; f = dens_s(N); top = 2*math.sqrt(N-1); cut = math.sqrt(d*m)
        lo, _ = quad(f, 0, min(cut, top), limit=400)
        hi, _ = quad(lambda s: f(s)/(s*s), min(cut, top), top, limit=400)
        out("%8d %6.0e   %.6f   %.6f   %.3e   %.3e" % (m, d, lo, nu_cdf(d), hi, 1/(d*m)))
out("example: eta = 0.05 needs both squares below eta^2 = 2.5e-3: d = 1e-5 gives nu([0,d]) = %.2e, then m >= 1/(d eta^2) = %.1e" % (nu_cdf(1e-5), 1/(1e-5*2.5e-3)))

out("== D. random matrix model (n x n Haar unitaries) ==")
def haar(n):
    z = (rng.standard_normal((n, n)) + 1j*rng.standard_normal((n, n)))/math.sqrt(2)
    q, r = np.linalg.qr(z)
    return q*(np.diag(r)/np.abs(np.diag(r)))
n = 300
U = [haar(n) for _ in range(3)]
Cm = haar(n)
ev, V = np.linalg.eig(Cm)
S = (V*np.angle(ev)) @ np.linalg.inv(V)      # S = arg(C), spectrum in (-pi, pi]
S = (S + S.conj().T)/2
tr = lambda X: (np.trace(X)/n).real
out("tau(S) = %.4f (0), tau(S^2) = %.4f (pi^2/3 = %.4f), ||S|| = %.4f (pi)" % (tr(S), tr(S@S), math.pi**2/3, np.linalg.norm(S, 2)))
def Ag(word):
    M = np.eye(n, dtype=complex)
    for l in word:
        M = M @ (U[l-1] if l > 0 else U[-l-1].conj().T)
    return M
words = [(), (1,), (2,), (1, 2), (2, 1), (1, -2), (3, 1, 1), (-1,), (1, 2, 3), (2, 2), (-3, 1), (1, 1), (3,), (-2,), (2, 3), (3, 2), (1, 3), (-1, 2), (2, -1), (3, 3)]
Sg = [Ag(w) @ S @ Ag(w).conj().T for w in words]
mx2 = max(abs(tr(Sg[i]@Sg[j])) for i in range(len(words)) for j in range(i))
mx4 = max(abs(tr(Sg[i]@Sg[j]@Sg[i]@Sg[j])) for i in range(6) for j in range(i))
s2 = math.pi**2/3
out("freeness of the S_g (O(1/n) errors expected): max |tau(S_g S_h)| = %.4f (0); max |tau(S_g S_h S_g S_h)| = %.4f (0); tau(S_g^2 S_h^2) = %.3f (sigma^4 = %.3f)"
    % (mx2, mx4, tr(Sg[1]@Sg[1]@Sg[2]@Sg[2]), s2*s2))
out("norm of sum k(g) S_g against 3 pi ||k||_2:")
worstr = 0.0
for name, k in [("one term", np.array([1.0] + [0]*19)), ("two equal", np.array([1.0, 1.0] + [0]*18)),
                ("20 equal", np.ones(20)), ("20 gaussian real", rng.standard_normal(20)),
                ("20 gaussian complex", rng.standard_normal(20) + 1j*rng.standard_normal(20)),
                ("one large + 19 small", np.array([5.0] + [0.2]*19)), ("alternating signs", np.array([(-1.0)**i for i in range(20)]))]:
    M = sum(k[i]*Sg[i] for i in range(20))
    nm = np.linalg.norm(M, 2); l2 = np.linalg.norm(k)
    ratio = nm/(3*math.pi*l2); worstr = max(worstr, ratio)
    out("  %-22s ||sum|| = %8.4f   3 pi ||k|| = %8.4f   ratio %.3f   (2 sigma ||k|| + pi max|k| = %.4f)" % (name, nm, 3*math.pi*l2, ratio, 2*math.sqrt(s2)*l2 + math.pi*np.max(np.abs(k))))
out("largest ratio:", "%.3f" % worstr)
out("== E. amplification arithmetic (6.1): 1+(3-1)/2 = %g, 1+(5-1)/2 = %g ==" % (1+(3-1)/2, 1+(5-1)/2))
out("total time %.1f s" % (time.time()-t0))
