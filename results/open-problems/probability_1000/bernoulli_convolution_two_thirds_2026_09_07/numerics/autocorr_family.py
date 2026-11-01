# Iterating hat_mu(xi) = c(xi) hat_mu(2 xi/3) n times gives, for every n,
#   I = (3/2)^n int prod_{i=1..n} cos^2(pi (3/2)^i eta / 3) |hat_mu(eta)|^2 d eta,
# and expanding the cosine product into frequencies turns each identity into an exact LINEAR relation among the
# autocorrelations A(t) = int f(x) f(x+t) dx (A(t) = 0 for |t| >= 1 since f lives on [0,1]).
#   n = 1 :  A(0) = 3 A(1/2)
#   n = 2 :  (7/9) A(0) = A(1/2) + A(3/4) + A(1/4)/2
# Check both against the solver density, and derive/check n = 3 numerically by direct expansion.
import numpy as np, itertools, math
R = 3*2**19
c = np.full(R, 1.0/R); edges = np.arange(R+1)/R
for _ in range(90):
    F = np.concatenate([[0.0], np.cumsum(c)]); new = np.zeros(R)
    for B in (0,1):
        a = (3*edges[:-1]-B)/2; b = (3*edges[1:]-B)/2
        new += 0.5*(np.interp(b, edges, F, left=0, right=1) - np.interp(a, edges, F, left=0, right=1))
    c = new/new.sum()
f = c*R; dx = 1.0/R
def A(t):
    if abs(t) >= 1: return 0.0
    sh = int(round(abs(t)*R))
    return float(np.sum(f[:R-sh]*f[sh:])*dx)
A0 = A(0.0)
print(f"A(0) = ||f||_2^2 = {A0:.6f}")
print(f"n=1 identity  A(0) = 3 A(1/2):     {A0:.6f}  vs  {3*A(0.5):.6f}   rel {abs(A0-3*A(0.5))/A0:.2e}")
lhs2 = (7/9)*A0; rhs2 = A(0.5) + A(0.75) + A(0.25)/2
print(f"n=2 identity  (7/9)A(0) = A(1/2)+A(3/4)+A(1/4)/2:   {lhs2:.6f}  vs  {rhs2:.6f}   rel {abs(lhs2-rhs2)/lhs2:.2e}")
# general n by symbolic expansion of prod cos^2(pi (3/2)^i eta/3) into cos(2 pi t eta) terms
def identity_terms(n):
    # cos^2(pi w eta) = 1/2 + (1/2) cos(2 pi (w/2) * 2 eta)... work with cos(2 pi t eta): cos^2(pi w eta) = 1/2 + 1/2 cos(2 pi (w/2)(2 eta))
    # simpler: cos^2(pi w eta) = 1/2 + 1/2 cos(2 pi w eta * 1) with t = w  -> since cos(2 pi w eta) = cos(2 pi (w) eta)
    terms = {0.0: 1.0}
    for i in range(1, n+1):
        w = (1.5**i)/3.0                      # cos^2(pi w eta), w = (3/2)^i / 3
        new = {}
        for t, co in terms.items():
            new[t] = new.get(t, 0.0) + co*0.5
            for s in (t + w, t - w):
                new[abs(s)] = new.get(abs(s), 0.0) + co*0.25
        terms = new
    return terms
for n in (1, 2, 3, 4):
    terms = identity_terms(n); scale = 1.5**n
    tot = sum(co*A(t) for t, co in terms.items())
    print(f"n={n}: (3/2)^n * sum c_t A(t) = {scale*tot:.6f}   vs A(0) = {A0:.6f}   rel {abs(scale*tot-A0)/A0:.2e}   ({len(terms)} lags, {sum(1 for t in terms if t < 1)} inside support)")
