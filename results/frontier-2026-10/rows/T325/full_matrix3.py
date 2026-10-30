"""T325 L = 6 follow-up to full_matrix2.py: are the full-descent end values below the scalar minima a
property of the risk or a fit to the 30 sampled S? Saves the end points, measures their distance from scalars and scores them on
fresh S (not symmetrised) against the best scalar minimum and the polynomial floor on the same fresh S.
Original header of full_matrix2.py follows.
T325 Target 2 probe (CPU, float64, small): do full d x d preconditioners turn the scalar-step spurious minima into saddles?
Predictor residual P(S) = (I - G_L S) ... (I - G_1 S), S = X^T X / N, X ~ N(0,1)^{N x d}, N = d/q. Risk (per coordinate, isotropic w):
  R(G) = mean_S [ tr(P P^T)/d + sigma^2 q tr((I-P) S^{-1} (I-P)^T)/d ],  the matrix analogue of the scalar risk (= it when G_l = g_l I).
(A) scalar-class minima on the same pooled spectrum; (B) Hessian of the full-matrix risk at each scalar minimum, embedded as G_l = g_l I;
(averaged over the signed-permutation group, so the scalar points are exact critical points)
(C) L-BFGS on full matrices from small random init and from each scalar minimum plus a 1e-3 kick."""
import sys, numpy as np, torch
from scipy.optimize import minimize
torch.set_num_threads(2); torch.set_default_dtype(torch.float64)
d, q, sig2, L, M = int(sys.argv[1]), float(sys.argv[2]), 0.25, int(sys.argv[3]), int(sys.argv[4])
N = int(round(d/q)); rng = np.random.default_rng(int(sys.argv[5]))
X = rng.standard_normal((M, N, d)); S = np.einsum('mni,mnj->mij', X, X)/N
import itertools
# exact invariance under the signed permutations (their commutant is the scalars, so G = g I is a critical point of the averaged risk)
Rs = []
for perm in itertools.permutations(range(d)):
    for sg in itertools.product((1, -1), repeat=d):
        R0 = np.zeros((d, d)); R0[np.arange(d), perm] = sg; Rs.append(R0)
Rs = np.array(Rs); S = np.einsum('rij,mjk,rlk->rmil', Rs, S, Rs).reshape(-1, d, d); M = len(S)
ev = np.linalg.eigvalsh(S).ravel(); lam = sig2*q
St = torch.tensor(S); Sinv = torch.linalg.inv(St); I = torch.eye(d)

def scal(g):
    P = np.prod(1 - np.outer(ev, g), 1)
    R = np.mean(P**2 + lam*(1 - P)**2/ev)
    dP = np.stack([-ev*np.prod(np.delete(1 - np.outer(ev, g), l, 1), 1) for l in range(L)], 1)
    return R, np.mean((2*P - 2*lam*(1 - P)/ev)[:, None]*dP, 0)

def full(Gflat):
    G = Gflat.reshape(L, d, d); P = I.expand(M, d, d)
    for l in range(L):
        P = (I - G[l] @ St) @ P
    Q = I - P
    return (P*P).sum((1, 2)).mean()/d + lam*torch.einsum('mij,mjk,mik->m', Q, Sinv, Q).mean()/d

# polynomial floor on the pooled spectrum
V = np.stack([ev**k for k in range(1, L + 1)], 1)
A = V.T @ V/len(ev) + lam*(V/ev[:, None]).T @ V/len(ev); c = np.linalg.solve(A, -V.mean(0)); Pf = 1 + V @ c
print(f"d={d} q={q} N={N} L={L} M={M} seed={sys.argv[5]}: polynomial floor {np.mean(Pf**2 + lam*(1-Pf)**2/ev):.7f}", flush=True)
mins = {}
for k in range(100):
    r = minimize(scal, rng.uniform(0, 6/ev.max(), L), jac=True, method="L-BFGS-B", options=dict(maxiter=5000, gtol=1e-12, ftol=1e-15))
    mins.setdefault(round(r.fun, 6), np.sort(r.x))
gbest = mins[min(mins)]
print(f"  scalar minima found: {sorted(mins)}; best {min(mins)} steps {np.round(gbest,3)}", flush=True)
# fresh test set
rt = np.random.default_rng(12345)
Xt = rt.standard_normal((4000, N, d)); Stt = np.einsum('mni,mnj->mij', Xt, Xt)/N
evt = np.linalg.eigvalsh(Stt).ravel()
StT = torch.tensor(Stt); SinvT = torch.linalg.inv(StT)
def risk_on(G, SS, SI):
    P = I.expand(len(SS), d, d)
    for l in range(L):
        P = (I - G[l] @ SS) @ P
    Q = I - P
    return ((P*P).sum((1, 2)).mean()/d + lam*torch.einsum('mij,mjk,mik->m', Q, SI, Q).mean()/d).item()
Vt = np.stack([evt**k for k in range(1, L + 1)], 1)
At = Vt.T @ Vt/len(evt) + lam*(Vt/evt[:, None]).T @ Vt/len(evt); ct = np.linalg.solve(At, -Vt.mean(0)); Pft = 1 + Vt @ ct
print(f"  fresh S (4000): polynomial floor {np.mean(Pft**2 + lam*(1-Pft)**2/evt):.7f}", flush=True)
for key, g in sorted(mins.items()):
    Gs = torch.stack([gl*I for gl in g])
    print(f"  scalar min {key}: fresh risk {risk_on(Gs, StT, SinvT):.7f}", flush=True)
ends = []
for k in range(3):
    def fg(x):
        t = torch.tensor(x, requires_grad=True); f = full(t); f.backward(); return f.item(), t.grad.numpy().copy()
    x0 = 0.05*rng.standard_normal(L*d*d)
    rr = minimize(fg, x0, jac=True, method="L-BFGS-B", options=dict(maxiter=20000, gtol=1e-11, ftol=1e-15))
    G = torch.tensor(rr.x).reshape(L, d, d)
    off = [float(torch.linalg.norm(G[l] - torch.trace(G[l])/d*I)/torch.linalg.norm(G[l])) for l in range(L)]
    sv = [np.round(np.linalg.svd(G[l].numpy(), compute_uv=False), 3).tolist() for l in range(L)]
    print(f"  random init {k}: train end {rr.fun:.7f} | fresh risk {risk_on(G, StT, SinvT):.7f} | non-scalar fraction per layer "
          f"{np.round(off,3).tolist()}", flush=True)
    print(f"     singular values per layer {sv}", flush=True)
    np.save(f"fm3_end{k}.npy", rr.x)
