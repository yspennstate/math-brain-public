"""E0078 = Asanjarani-Nazarathy Conjecture 4.2: T^pi >=_st T^alpha, i.e. (pi - alpha) e^{Ct} 1 >= 0 for all t,
equivalently the hazard of T^pi never exceeds lambda*.  Adversarial search: random + hill-climb on
min_t (pi-alpha)e^{Ct}1 / S(t)  (normalised), over cyclic/skew/dense Q and extreme rates."""
import numpy as np
from scipy.linalg import expm, null_space
rng = np.random.default_rng(78)
ts = np.concatenate([np.geomspace(1e-3, 1, 16), np.linspace(1.2, 40, 40)])
def stat(Q):
    v = null_space(Q.T); p = v[:,0]; p = p/p.sum(); return p if p.min()>0 else None
def score(Q, lam):
    pi = stat(Q)
    if pi is None: return None
    C = Q - np.diag(lam); one = np.ones(len(lam)); ls = pi@lam
    if ls <= 0: return None
    al = pi*lam/ls
    worst = 0.0; tw = None
    for t in ts:
        E = expm(C*t); S = pi@E@one
        if S < 1e-280: break
        v = (pi-al)@E@one / S          # >= 0 is the conjecture; = 1 - hazard(t)/lambda*
        if v < worst: worst = v; tw = t
    return worst, tw
def rand_inst(m):
    kind = rng.choice(['dense','cyclic','skew','twoscale'])
    Q = np.zeros((m,m))
    if kind=='dense': Q = rng.exponential(1,(m,m))
    elif kind=='cyclic':
        for i in range(m): Q[i,(i+1)%m] = rng.exponential(1)
        Q += 1e-4*rng.exponential(1,(m,m))
    elif kind=='skew':
        Q = 1e-2*rng.exponential(1,(m,m))
        for i in range(m): Q[i,(i+1)%m] += rng.exponential(1)
    else:
        Q = rng.exponential(1,(m,m)) * rng.choice([1e-3,1,1e3],(m,m))
    np.fill_diagonal(Q,0); np.fill_diagonal(Q,-Q.sum(1))
    lam = rng.exponential(1,m) * rng.choice([1e-3,1,1e3],m)
    return Q, lam, kind
best = (0.0, None)
rec = []
for k in range(500):
    m = int(rng.choice([2,3,4,5,6]))
    Q, lam, kind = rand_inst(m)
    r = score(Q, lam)
    if r is None: continue
    w, tw = r
    rec.append(w)
    if w < best[0]:
        best = (w, (m, kind, tw, Q.round(4).tolist(), lam.round(4).tolist()))
import sys; sys.stdout.flush()
print("random instances:", len(rec), " min normalised (pi-alpha)e^{Ct}1/S :", best[0])
print("worst instance:", best[1])
# hill-climb from the 30 worst random instances
def perturb(Q, lam):
    m = len(lam)
    Q2 = Q.copy(); np.fill_diagonal(Q2, 0)
    Q2 = Q2 * np.exp(0.3*rng.normal(size=Q2.shape)); np.fill_diagonal(Q2, 0); np.fill_diagonal(Q2, -Q2.sum(1))
    lam2 = lam * np.exp(0.3*rng.normal(size=m))
    return Q2, lam2
starts = []
for k in range(120):
    m = int(rng.choice([3,4,5,6])); Q, lam, kind = rand_inst(m); r = score(Q, lam)
    if r: starts.append((r[0], Q, lam))
starts.sort(key=lambda x: x[0])
hc_best = 0.0; hc_rec = None
for w0, Q, lam in starts[:6]:
    cur = w0; cQ, cl = Q, lam
    for it in range(60):
        Q2, l2 = perturb(cQ, cl); r = score(Q2, l2)
        if r and r[0] < cur: cur, cQ, cl = r[0], Q2, l2
    if cur < hc_best: hc_best = cur; hc_rec = (cQ.round(5).tolist(), cl.round(5).tolist())
print("hill-climb min:", hc_best)
print("hill-climb worst instance:", hc_rec)
