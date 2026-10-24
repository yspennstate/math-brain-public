import numpy as np, math
# Aldous-Fill Open Problem 4.30: is there universal psi(||g||_inf, t/tau2) -> 0 bounding the
# Kolmogorov distance of S_t/(sigma sqrt t) to Normal(0,1)?
# Candidate NO: Y two-state (rates 0->1 = eps, 1->0 = 1-eps), Z fair sign flipping at rate R/2,
# independent; g = A*Z + B*(Y-eps).
def params(s):
    eps=s**-2.0; R=s**4.0
    A=2*eps+math.sqrt((1-eps)*(1-4*eps)); B=(2-A)/(1-eps)
    return eps,R,A,B
print("Check the algebra first: mean 0, variance 1, sup-norm exactly 2, gap 1")
print(f"{'s':>7} {'eps':>10} {'A':>9} {'B':>9} {'Var g':>10} {'||g||inf':>9} {'sigma^2':>12} {'t/tau2':>8}")
for s in [10,30,100,300,1000]:
    eps,R,A,B=params(s)
    Var=A*A + B*B*eps*(1-eps)
    sup=max(abs(A+B*(1-eps)), abs(-A+B*(1-eps)), abs(A-B*eps), abs(-A-B*eps))
    sig2=2*A*A/R + 2*B*B*eps*(1-eps)
    print(f"{s:>7} {eps:>10.2e} {A:>9.6f} {B:>9.6f} {Var:>10.7f} {sup:>9.6f} {sig2:>12.3e} {s:>8}")
print()
print("Now simulate S_t = int_0^t g dX with t = s, and compare S_t/(sigma sqrt t) to N(0,1).")
rng=np.random.default_rng(2026)
def kolmogorov_to_normal(x):
    x=np.sort(x); n=len(x)
    F=0.5*(1+np.vectorize(math.erf)(x/np.sqrt(2)))
    d1=np.max(np.abs(np.arange(1,n+1)/n - F)); d2=np.max(np.abs(np.arange(0,n)/n - F))
    return max(d1,d2)
for s in [30,100,300,1000]:
    eps,R,A,B=params(s); t=float(s); sig=math.sqrt(2*A*A/R + 2*B*B*eps*(1-eps))
    npaths=20000
    # Y: exact - number of 0->1 jumps in [0,t] is Poisson-ish; simulate holding times
    # integral of (Y - eps) over [0,t]
    S=np.empty(npaths)
    for p in range(npaths):
        # Y starts stationary
        y = 1 if rng.random()<eps else 0
        u=0.0; intY=0.0
        while u<t:
            rate = eps if y==0 else (1-eps)
            w = rng.exponential(1.0/rate)
            dt = min(w, t-u)
            if y==1: intY += dt
            u += dt
            if u<t: y = 1-y
        slow = B*(intY - eps*t)
        # Z: telegraph at rate R/2; Var(int_0^t Z) = (2/R)*t approx; use the exact OU-like variance
        varfast = (A*A)*(2.0*t/R - 2.0*(1-math.exp(-R*t))/(R*R))
        fast = rng.normal(0.0, math.sqrt(max(varfast,0.0)))   # fast part is asymptotically normal
        S[p] = slow + fast
    X = S/(sig*math.sqrt(t))
    print(f"s={s:>5}  t/tau2={s:>5}  sd of normalized S = {X.std():>8.5f}   "
          f"Kolmogorov distance to N(0,1) = {kolmogorov_to_normal(X):.4f}")
