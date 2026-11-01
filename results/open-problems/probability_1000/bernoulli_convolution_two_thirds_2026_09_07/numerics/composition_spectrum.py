# The self-similar variable D satisfies D = eps/3 + (2/3) D', eps in {0,+-1} with weights (1/2,1/4,1/4).
# Composition (transfer) operator on test functions:  (C phi)(t) = sum_eps p_eps phi(eps/3 + (2/3) t).
# The three branches map the disk |t| <= R into |t| <= (2/3)R + 1/3, strictly inside for R > 1, so C is
# compact on analytic functions there: discrete spectrum, eigenvalue 1 on constants.
# QUESTION: what is the second eigenvalue?  The route needs it below 2/3 = 0.6667.
# Compute it by representing phi in a Chebyshev basis on [-1,1] and building the matrix of C.
import numpy as np
def cheb_nodes(n):
    return np.cos(np.pi*np.arange(n)/(n-1))
def cheb_vander(x, n):
    # T_j(x) for j = 0..n-1
    V = np.zeros((len(x), n)); V[:,0] = 1.0
    if n > 1: V[:,1] = x
    for j in range(2, n): V[:,j] = 2*x*V[:,j-1] - V[:,j-2]
    return V
for n in (24, 40, 60, 80):
    x = cheb_nodes(n)
    V = cheb_vander(x, n)          # values of basis at nodes
    Vi = np.linalg.inv(V)          # coefficients from values
    # action: (C phi)(x_k) = sum_eps p_eps phi(eps/3 + (2/3) x_k)
    M = np.zeros((n, n))
    for p, eps in ((0.5, 0.0), (0.25, 1.0), (0.25, -1.0)):
        y = eps/3.0 + (2.0/3.0)*x
        M += p*cheb_vander(y, n)   # values of basis at the pulled-back points
    A = Vi @ M                      # matrix in the coefficient basis? build value->value instead
    Aval = M @ Vi                   # values -> values
    ev = np.linalg.eigvals(Aval)
    ev = ev[np.argsort(-np.abs(ev))]
    print(f"n={n:3d}: top eigenvalues |lam| = " + ", ".join(f"{abs(v):.6f}" for v in ev[:6]))
print("\nthe route needs the second eigenvalue < 2/3 = 0.666667")
