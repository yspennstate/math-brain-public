SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T03:09:12Z.
attacking: falsify any puncture-interpolation argument that uses only the r46 factorial L^m bound plus bounded low-dimensional residual marginals, then isolate the genuinely product-linear input still needed.

# Early calculation: curved-cancellation residual law

Fix 0<epsilon<1 and let H,U,V,W be independent Uniform[-1/2,1/2] variables (density one). For W != 0 set

T = U - V^2/(2 epsilon W),

with an arbitrary definition on the null event W=0. Then the residual triple (T,W,V) has joint density

rho(t,w,v)=1_{|w|<=1/2, |v|<=1/2, |t+v^2/(2 epsilon w)|<=1/2},

because (u,w,v)->(t,w,v) is a Jacobian-one triangular map. Hence ||rho||_infinity=1. Moreover each coordinate one- and two-dimensional marginal has density <=1: integrate the indicator over a subset of an interval of length one.

Consider

Q_epsilon = 2 H W + 2 epsilon T W + V^2.

Substitution gives the exact cancellation

Q_epsilon = 2 W (H + epsilon U).

The matrix in coordinates (H,T,W,V) is

A_epsilon = [[0,0,1,0],[0,0,epsilon,0],[1,epsilon,0,0],[0,0,0,1]],

with eigenvalues +sqrt(1+epsilon^2), -sqrt(1+epsilon^2), 1, 0. Thus its algebra matches the three-large-eigenvalue puncture normal form: with q=1/(1+epsilon^2), kappa=sqrt(1+epsilon^2), c=1, one has kappa^2 c=1+epsilon^2=|product of the three nonzero eigenvalues| and sqrt((1-q)/q)=epsilon.

Let S=H+epsilon U. For 0<epsilon<1, its density equals one on |s|<=(1-epsilon)/2. Since W is independent Uniform[-1/2,1/2], for 0<|y|<(1-epsilon)/2 the product-density formula yields

p_{Q_epsilon}(y) >= log((1-epsilon)/(2|y|)),

so the output density is unbounded logarithmically.

This is NOT a QFORM counterexample because T,W,V are dependent and have not been realized as an orthogonal linear projection of independent cap-one coordinates. It is a counterexample to the intermediate interface that replaces that product-linear provenance by: joint density cap one + all coordinate 1D/2D marginal caps one + the exact puncture coefficient identities + the r46 factorial L^m estimate. The next positive mechanism must use the linear product-projection/convolution structure itself.
