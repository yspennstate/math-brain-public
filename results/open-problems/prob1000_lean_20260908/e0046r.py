"""Real case of Bandeira 1.2: alpha_R(n) = E[(1/n) sum sigma_i(X/sqrt n)], X real n x n N(0,1).  Monte Carlo with
common random numbers is useless for monotonicity at 1e-4; use exact quadrature for n=1,2 and MC for the shape."""
import numpy as np
from scipy import integrate
print("alpha_R(1) = E|g| = sqrt(2/pi) =", np.sqrt(2/np.pi))
# n=2: eigenvalues of W = X X^T, real Wishart(2,2): density c |l1-l2| (l1 l2)^{-1/2} e^{-(l1+l2)/2}; E (sqrt l1 + sqrt l2)/2^{3/2}
f = lambda l1,l2: abs(l1-l2)*(l1*l2)**-0.5*np.exp(-(l1+l2)/2)
Z,_ = integrate.dblquad(lambda l2,l1: f(l1,l2), 0, np.inf, 0, np.inf)
M,_ = integrate.dblquad(lambda l2,l1: (np.sqrt(l1)+np.sqrt(l2))*f(l1,l2), 0, np.inf, 0, np.inf)
print("alpha_R(2) exact quadrature =", M/Z/2**1.5)
rng = np.random.default_rng(46)
for n in (2,3,4,6,8,12,20,40):
    reps = int(2e6//(n*n)); reps=max(reps,2000)
    s = np.zeros(reps)
    for i in range(reps):
        X = rng.standard_normal((n,n)); s[i] = np.linalg.svd(X, compute_uv=False).mean()/np.sqrt(n)
    print(f"alpha_R({n:2d}) MC = {s.mean():.5f} +- {s.std()/np.sqrt(reps):.5f}")
print("limit 8/(3pi) =", 8/(3*np.pi))
