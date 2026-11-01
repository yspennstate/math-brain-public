# First-moment diagonal bound in a plain walk model, with and without U-detour constraints.
# Walks: d forward steps (+1 level), d backward (-1). Level-L hyperplane is Euclidean distance L/sqrt(d).
# Edge factor phi(theta) = E[e^{-theta t} 1{t <= min of K indep Gamma(3)}]; K=0 gives 1/(1+theta).
# A pair of steps (only every other edge carries detours): per-step factor sqrt(phi0*phiK).
# Bound: need d*phi_step*(z+1/z) <= 1 with z<1; mu >= sqrt(d) * sup_theta (-log z)/theta.
import sys, mpmath as mp
mp.mp.dps = 30
d = int(sys.argv[1])
def phiK(th, K):
    if K == 0: return 1/(1+th)
    return mp.quad(lambda t: mp.e**(-(1+th)*t) * (mp.e**(-t)*(1+t+t*t/2))**K, [0, 1, 5, mp.inf])
def s_of(th, K, every):
    p = phiK(th,0) if K==0 else (phiK(th,0)*phiK(th,K))**0.5 if every==2 else phiK(th,K)
    A = 1/(d*p)            # need z + 1/z = A
    if A < 2: return None
    z = (A - mp.sqrt(A*A-4))/2
    return -mp.log(z)/th
def best(K, every):
    f = lambda th: -(s_of(th,K,every) or 0)
    ths = [x/4 for x in range(1, 400)]
    vals = [(s_of(t,K,every) or 0, t) for t in ths]
    v,t = max(vals)
    return float(v*mp.sqrt(d)), t
b0 = best(0,1); print(d, "plain walk bound", b0)
for K in (2*(d-1)-2, 2*(d-1)-4):
    for ev in (2,1):
        b = best(K, ev); print(d, "K=%d every=%d"%(K,ev), b, "rel gain %.4f"%(b[0]/b0[0]-1))
