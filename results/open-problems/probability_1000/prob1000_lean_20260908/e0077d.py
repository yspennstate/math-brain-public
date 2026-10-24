"""Fast check of the three identities the proof rests on, on random MMPPs incl. cyclic ones.
(a) c^2 from the survey's (6): c^2+1 = 2 (pi C 1)(pi C^-1 1);  (b) c^2 = 2 lam* E[T^pi] - 1;
(c) survival P(T^pi>t) = pi e^{Ct} 1 >= exp(-lam* t) for every t (the Jensen bound);
(d) whether log-survival is convex (DHR of T^pi) - a STRONGER statement we do not need."""
import numpy as np
from scipy.linalg import expm, null_space
rng = np.random.default_rng(7)
def gen(m, kind):
    Q = np.zeros((m,m))
    if kind=='dense': Q = rng.exponential(1.0,(m,m))
    elif kind=='cyclic':
        for i in range(m): Q[i,(i+1)%m] = rng.exponential(1.0)
        Q += 1e-3*rng.exponential(1.0,(m,m))
    else:
        Q[:] = 1e-2*rng.exponential(1.0,(m,m))
        for i in range(m): Q[i,(i+1)%m] += rng.exponential(1.0)
    np.fill_diagonal(Q,0); np.fill_diagonal(Q,-Q.sum(1)); return Q
ts = np.concatenate([np.linspace(0,2,41)[1:], np.linspace(2,30,57)[1:]])
worst_b = 0; worst_c = 0; worst_d = 0; n=0; rec=None
for k in range(600):
    m = int(rng.choice([2,3,4,5,6,8])); kind = rng.choice(['dense','cyclic','skew'])
    Q = gen(m,kind); v = null_space(Q.T); pi = v[:,0]; pi = pi/pi.sum()
    if pi.min()<=0: continue
    lam = rng.exponential(1.0,m)*rng.choice([0.02,1,50])
    if rng.random()<0.3: lam = np.full(m,1e-3); lam[rng.integers(m)] = 100*rng.exponential()
    C = Q-np.diag(lam); one=np.ones(m); lamstar = pi@lam
    c2_a = 2*(pi@C@one)*(pi@np.linalg.solve(C,one)) - 1
    ETpi = pi@np.linalg.solve(-C,one)
    c2_b = 2*lamstar*ETpi - 1
    worst_b = max(worst_b, abs(c2_a-c2_b))
    f = np.array([pi@expm(C*t)@one for t in ts])
    ok = f > 1e-290
    lf = np.where(ok, np.log(np.where(ok,f,1.0)), 0.0)
    g = np.where(ok, lf + lamstar*ts, 0.0)
    gap = g.min()
    if gap < worst_c: worst_c = gap; rec=(m,kind,float(ts[np.argmin(g)]), float(lamstar))
    d2 = np.diff(lf,2)  # uniform-ish only within each segment; crude
    seg = np.diff(lf[:40],2)/ (ts[1]-ts[0])**2
    if seg.min() < worst_d: worst_d = seg.min(); recd=(m,kind,float(lamstar), np.round(lam,3).tolist())
    n+=1
print("instances", n)
print("(a)=(b) max |c2 diff|          :", worst_b)
print("(c) min over t of log f + lam* t:", worst_c, rec, "   (>= 0 up to fp is the Jensen bound)")
print("(d) min second diff of log f    :", worst_d, recd, "  (<0 means T^pi is NOT always DHR)")
