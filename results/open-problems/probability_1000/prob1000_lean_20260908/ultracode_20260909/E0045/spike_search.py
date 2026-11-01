# Spiked case of the endpoint (d=p-1) conjecture.  Sigma = diag(a,1,...,1)  (a>0, a != 1).
# For any orthogonal T the law of X = T Y depends only on u = first column of T (unit vector):
#     X = sqrt(a) W u + Z_perp,   W ~ N(0,1), Z_perp ~ N(0, I - u u^T) independent.
# Conjecture (endpoint): F(u) := E min_i X_i^2 is minimised at u = e_1, where F = E min(a Z_1^2, Z_2^2, ..., Z_N^2).
# We minimise F(u) over the sphere with Nelder-Mead on a fixed scrambled-Sobol sample (common random numbers),
# then re-evaluate the best u and e_1 on fresh independent scrambles to get an honest estimate with error bars.
import numpy as np, sys, time
from scipy.stats import qmc, norm
from scipy.optimize import minimize
N = int(sys.argv[1]); a = float(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv)>3 else 0
rng = np.random.default_rng(seed)

def sample(m, s):
    S = qmc.Sobol(d=N, scramble=True, seed=s).random_base2(m)
    S = np.clip(S, 1e-12, 1-1e-12)
    return norm.ppf(S)          # standard normals (n, N)

def F_of_u(u, Z):
    u = u/np.linalg.norm(u)
    W = Z @ u                    # N(0,1)
    Zp = Z - np.outer(W, u)      # N(0, I - uu^T)
    X = Zp + np.sqrt(a)*W[:,None]*u[None,:]
    return np.min(X**2, axis=1).mean()

Z = sample(16, 1000+seed)        # 65536 points for the search
base = F_of_u(np.eye(N)[0], Z)
best = (np.inf, None)
t0 = time.time()
for r in range(25):
    u0 = rng.standard_normal(N)
    res = minimize(lambda v: F_of_u(v, Z), u0, method='Nelder-Mead', options={'maxiter':600, 'xatol':1e-5, 'fatol':1e-8})
    u = res.x/np.linalg.norm(res.x)
    if res.fun < best[0]: best = (res.fun, u)
print(f"N={N} a={a}: search sample: F(e1)={base:.6f}  min over u found={best[0]:.6f}  ratio={best[0]/base:.5f}  u={np.round(best[1],3)}  ({time.time()-t0:.0f}s)")
# honest re-evaluation with fresh scrambles (paired differences)
diffs=[]; vals=[]
for s in range(8):
    Zf = sample(18, 5000+100*seed+s)
    fe = F_of_u(np.eye(N)[0], Zf); fu = F_of_u(best[1], Zf)
    diffs.append(fu-fe); vals.append((fe,fu))
diffs=np.array(diffs); vals=np.array(vals)
print(f"  fresh: F(e1)={vals[:,0].mean():.6f}  F(u*)={vals[:,1].mean():.6f}  F(u*)-F(e1)={diffs.mean():+.6f} +- {diffs.std(ddof=1)/np.sqrt(len(diffs)):.6f}")
np.save(f"spike_u_N{N}_a{a}_s{seed}.npy", best[1])
