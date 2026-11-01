# P0427 numerics: (A) two-job no-arrival problem, formula vs Monte Carlo, direction of the optimum
#                 (B) stationary problem with Poisson arrivals: relative value iteration, check
#                     max-optimal allocation >= GREEDY* allocation and Delta1 >= Delta2 in every state.
import numpy as np, math, sys
rng = np.random.default_rng(12345)

def V_two_job(b, n, s1, s2):
    r1, r2 = s1(b), s2(n-b)
    return (2 + r1/s2(n) + r2/s1(n))/(r1+r2)

def mc_two_job(b, n, s1, s2, N=400000):
    r1, r2 = s1(b), s2(n-b)
    t1 = rng.exponential(1/r1, N); t2 = rng.exponential(1/r2, N)
    first = np.minimum(t1, t2)
    # survivor: if class1 done first (t1<t2) class 2 remains, finishes at rate s2(n)
    rem = np.where(t1 < t2, rng.exponential(1/s2(n), N), rng.exponential(1/s1(n), N))
    return np.mean(2*first + rem), np.std(2*first+rem)/math.sqrt(N)

print("=== (A) two jobs, no arrivals ===")
n = 4
cases = {
 "attempt example (kinked)": (lambda b: min(b, math.sqrt(b)) if b>0 else 0.0, lambda b: min(b, b**0.75) if b>0 else 0.0),
 "power p1=0.3,p2=0.7":       (lambda b: b**0.3, lambda b: b**0.7),
 "power p1=0.5,p2=0.9":       (lambda b: b**0.5, lambda b: b**0.9),
 "Amdahl p1=0.5,p2=0.9":      (lambda b: 1/((1-0.5)+0.5/b) if b>0 else 0.0, lambda b: 1/((1-0.9)+0.9/b) if b>0 else 0.0),
}
grid = np.linspace(1e-6, n-1e-6, 400001)
for name,(s1,s2) in cases.items():
    R = np.array([s1(b)+s2(n-b) for b in grid])
    V = np.array([V_two_job(b,n,s1,s2) for b in grid])
    bT = grid[np.flatnonzero(R >= R.max()-1e-12).max()]   # GREEDY*: largest throughput maximizer
    bS = grid[V.argmin()]
    print(f"{name:28s} b_T={bT:.4f}  b*={bS:.4f}  V(b_T)={V_two_job(bT,n,s1,s2):.6f}  V(b*)={V.min():.6f}  b*>=b_T: {bS>=bT-1e-6}")
    m,se = mc_two_job(bT,n,s1,s2); print(f"    MC at b_T: {m:.4f} +- {se:.4f}   formula {V_two_job(bT,n,s1,s2):.4f}")
    m,se = mc_two_job(bS,n,s1,s2); print(f"    MC at b* : {m:.4f} +- {se:.4f}   formula {V_two_job(bS,n,s1,s2):.4f}")
    # first-order condition check at b* (smooth cases): s2'(n-b)-s1'(b) = (d/2)(s2(n-b)s1'(b)+s1(b)s2'(n-b))
    h=1e-6; d = 1/s1(n)-1/s2(n)
    s1p = (s1(bS+h)-s1(bS-h))/(2*h); s2p = (s2(n-bS+h)-s2(n-bS-h))/(2*h)
    print(f"    FOC residual at b*: {s2p - s1p - (d/2)*(s2(n-bS)*s1p + s1(bS)*s2p):+.2e}   (should be ~0 for smooth cases with interior b*)")

print()
print("=== (B) stationary problem with Poisson arrivals, relative value iteration ===")
def run_B(p1, p2, lam1, lam2, n=4, N=30, A=81, alpha=0.0, iters=4000):
    s1 = lambda k: k**p1; s2 = lambda k: k**p2
    acts = np.linspace(0, n, A)                       # servers to class 1
    X1, X2 = np.meshgrid(np.arange(N+1), np.arange(N+1), indexing='ij')
    # rate arrays r1[x1,x2,a], r2[x1,x2,a]; class i pooled rate = x_i s_i(a_i/x_i), zero if x_i=0
    with np.errstate(divide='ignore', invalid='ignore'):
        r1 = np.where(X1[...,None]>0, X1[...,None]*s1(acts[None,None,:]/np.maximum(X1[...,None],1)), 0.0)
        r2 = np.where(X2[...,None]>0, X2[...,None]*s2((n-acts)[None,None,:]/np.maximum(X2[...,None],1)), 0.0)
    thr = r1+r2
    Lam = lam1+lam2+thr.max()+1.0
    V = np.zeros((N+1,N+1))
    cost = (X1+X2).astype(float)
    for it in range(iters):
        Vup1 = np.empty_like(V); Vup1[:-1,:] = V[1:,:]; Vup1[-1,:] = V[-1,:]      # arrival blocked at truncation
        Vup2 = np.empty_like(V); Vup2[:,:-1] = V[:,1:]; Vup2[:,-1] = V[:,-1]
        Vdn1 = np.empty_like(V); Vdn1[1:,:] = V[:-1,:]; Vdn1[0,:] = V[0,:]
        Vdn2 = np.empty_like(V); Vdn2[:,1:] = V[:,:-1]; Vdn2[:,0] = V[:,0]
        Q = cost[...,None] + lam1*Vup1[...,None] + lam2*Vup2[...,None] + r1*Vdn1[...,None] + r2*Vdn2[...,None] + (Lam-lam1-lam2-thr)*V[...,None]
        Vn = Q.min(axis=2)/(Lam+alpha)
        if alpha == 0: Vn = Vn - Vn[0,0]                 # relative value iteration
        if np.abs(Vn-V).max() < 1e-11: V = Vn; break
        V = Vn
    # final Q with converged V
    Q = cost[...,None] + lam1*Vup1[...,None] + lam2*Vup2[...,None] + r1*Vdn1[...,None] + r2*Vdn2[...,None] + (Lam-lam1-lam2-thr)*V[...,None]
    tol = 1e-9
    opt_max = np.array([[acts[np.flatnonzero(Q[i,j] <= Q[i,j].min()+tol).max()] for j in range(N+1)] for i in range(N+1)])
    opt_min = np.array([[acts[np.flatnonzero(Q[i,j] <= Q[i,j].min()+tol).min()] for j in range(N+1)] for i in range(N+1)])
    gstar   = np.array([[acts[np.flatnonzero(thr[i,j] >= thr[i,j].max()-tol).max()] for j in range(N+1)] for i in range(N+1)])
    gmin    = np.array([[acts[np.flatnonzero(thr[i,j] >= thr[i,j].max()-tol).min()] for j in range(N+1)] for i in range(N+1)])
    M = N-5   # interior of truncation
    sl = (slice(1,M), slice(1,M))
    D1 = V[1:M,1:M]-V[0:M-1,1:M]; D2 = V[1:M,1:M]-V[1:M,0:M-1]
    print(f"p=({p1},{p2}) lam=({lam1},{lam2}) alpha={alpha} it={it}: "
          f"maxOPT>=GREEDY* all: {(opt_max[sl]>=gstar[sl]-1e-12).all()}  minOPT>=minGREEDY all: {(opt_min[sl]>=gmin[sl]-1e-12).all()}  "
          f"D1>=D2 all: {(D1>=D2-1e-9).all()}  D2>0 all: {(D2>0).all()}  "
          f"states where OPT differs from GREEDY*: {(np.abs(opt_max[sl]-gstar[sl])>1e-9).sum()} of {(M-1)**2}  max excess a*-aG*: {(opt_max[sl]-gstar[sl]).max():.3f}")
    return V, opt_max, gstar
for (p1,p2,l1,l2,al) in [(0.3,0.7,0.5,0.5,0.0),(0.5,0.9,1.0,1.0,0.0),(0.3,0.7,0.5,0.5,0.2),(0.2,0.95,1.5,0.3,0.0),(0.6,0.8,0.3,1.2,0.0)]:
    run_B(p1,p2,l1,l2,alpha=al)
# also a kinked (piecewise) speedup pair with arrivals, coarse grid so that the kinks are on the grid
print("kinked pair min(k,sqrt k) / min(k,k^0.75) with arrivals:")
def run_B2(lam1, lam2, n=4, N=30, A=81, iters=4000):
    s1 = lambda k: np.minimum(k, np.sqrt(k)); s2 = lambda k: np.minimum(k, k**0.75)
    acts = np.linspace(0, n, A)
    X1, X2 = np.meshgrid(np.arange(N+1), np.arange(N+1), indexing='ij')
    r1 = np.where(X1[...,None]>0, X1[...,None]*s1(acts[None,None,:]/np.maximum(X1[...,None],1)), 0.0)
    r2 = np.where(X2[...,None]>0, X2[...,None]*s2((n-acts)[None,None,:]/np.maximum(X2[...,None],1)), 0.0)
    thr = r1+r2; Lam = lam1+lam2+thr.max()+1.0; V = np.zeros((N+1,N+1)); cost=(X1+X2).astype(float)
    for it in range(iters):
        Vup1 = np.empty_like(V); Vup1[:-1,:] = V[1:,:]; Vup1[-1,:] = V[-1,:]
        Vup2 = np.empty_like(V); Vup2[:,:-1] = V[:,1:]; Vup2[:,-1] = V[:,-1]
        Vdn1 = np.empty_like(V); Vdn1[1:,:] = V[:-1,:]; Vdn1[0,:] = V[0,:]
        Vdn2 = np.empty_like(V); Vdn2[:,1:] = V[:,:-1]; Vdn2[:,0] = V[:,0]
        Q = cost[...,None] + lam1*Vup1[...,None] + lam2*Vup2[...,None] + r1*Vdn1[...,None] + r2*Vdn2[...,None] + (Lam-lam1-lam2-thr)*V[...,None]
        Vn = Q.min(axis=2)/Lam; Vn -= Vn[0,0]
        if np.abs(Vn-V).max() < 1e-11: V=Vn; break
        V = Vn
    Q = cost[...,None] + lam1*Vup1[...,None] + lam2*Vup2[...,None] + r1*Vdn1[...,None] + r2*Vdn2[...,None] + (Lam-lam1-lam2-thr)*V[...,None]
    tol=1e-9; M=N-5; sl=(slice(1,M),slice(1,M))
    opt_max = np.array([[acts[np.flatnonzero(Q[i,j] <= Q[i,j].min()+tol).max()] for j in range(N+1)] for i in range(N+1)])
    gstar   = np.array([[acts[np.flatnonzero(thr[i,j] >= thr[i,j].max()-tol).max()] for j in range(N+1)] for i in range(N+1)])
    D1 = V[1:M,1:M]-V[0:M-1,1:M]; D2 = V[1:M,1:M]-V[1:M,0:M-1]
    print(f"  lam=({lam1},{lam2}) it={it}: maxOPT>=GREEDY* all: {(opt_max[sl]>=gstar[sl]-1e-12).all()}  D1>=D2 all: {(D1>=D2-1e-9).all()}  differs in {(np.abs(opt_max[sl]-gstar[sl])>1e-9).sum()} states; state(1,1): OPT {opt_max[1,1]:.3f} GREEDY* {gstar[1,1]:.3f}")
run_B2(0.5,0.5); run_B2(0.0,0.0)
