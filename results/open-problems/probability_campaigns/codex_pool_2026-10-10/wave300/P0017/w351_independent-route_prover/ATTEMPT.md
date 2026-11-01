# P0017: conditional variance route

Checkpoint 2026-10-10. Independent approach saved in APPROACH_PRECOMMITTED.md before any peer proposed proof was read. No peer proof has been used.

The target is a universal Poincare constant for every isotropic log-concave probability measure in every dimension, including uniform laws on convex bodies. Original source: Randomstrasse101: Open Problems of 2025, arXiv:2603.29571v1, Entry 13, Conjecture 30. Its covariance-scaled Cheeger statement is h_mu >= c/sqrt(||Cov(mu)||_op); in isotropic position it asks for a universal positive h_mu. The log-concave Poincare formulation is recorded exactly in Bizeul--Klartag--Lehec, arXiv:2610.05474v1, definition (5) and Theorem 1.1. October preprints claim the complete target; this packet does not independently certify their proofs or claim novelty. Current openness is UNKNOWN. SOURCE_STATUS.json separates source verification from mathematical verification.

L0 (affine normalization): for positive-definite covariance Sigma, X=m+Sigma^(1/2)Y makes Y isotropic and preserves log-concavity. For locally Lipschitz f with finite variance and covariance-weighted energy, put g(y)=f(m+Sigma^(1/2)y). Then Var(g(Y))=Var(f(X)) and |grad_y g|^2=grad_x f^T Sigma grad_x f almost everywhere. An assumed isotropic bound with constant C therefore yields the covariance-weighted bound with the same C. Conversely, Sigma=I gives the isotropic bound. This reduction proves no universal C.

## Attempt and exact two-block lemma (L1)

Let (U,V) have a joint probability law. On its mean-zero L2 space, define orthogonal conditional-expectation projections P f=E[f|U], Q f=E[f|V]. Suppose the maximal correlation between mean-zero U-measurable and V-measurable square-integrable functions is at most rho<1. Precisely, |E[a(U)b(V)]| <= rho ||a||2 ||b||2 for all such a,b. Then

Var(f) <= (E Var(f|U) + E Var(f|V))/(1-rho).

Proof: put a=Pf, b=Qf, S=||a||2^2+||b||2^2. Projection identities give S=<f,a+b>. Maximal correlation gives ||a+b||2^2 <= (1+rho)S. Cauchy--Schwarz therefore gives S<=||f||2 sqrt((1+rho)S), hence S<=(1+rho)||f||2^2 (also if S=0). Now E Var(f|U)+E Var(f|V)=2||f||2^2-S >= (1-rho)||f||2^2. Centering f proves the assertion.

If U,V are Euclidean coordinate blocks, if their conditional laws satisfy Poincare bounds M_U and M_V almost everywhere, and if f is admissible on each slice, integration of those bounds gives

Var(f) <= [M_U E|grad_U f|^2 + M_V E|grad_V f|^2]/(1-rho)
         <= max(M_U,M_V)/(1-rho) E|grad f|^2.

No independence is assumed or manufactured by multiplying conditional estimates. This is a proved special case under additional hypotheses, not a proof of KLS. The route requires uniform control of a genuine dependence operator and of conditional energies.

## Exact simplex obstruction (L2)

For every n>=2, put N=n+1 and take a regular simplex in the n-dimensional hyperplane H={z in R^N: sum z_i=0}, with vertices

v_i=sqrt(N(N+1))(e_i-N^(-1)1), i=0,...,N-1.

The Euclidean structure is the inherited structure on H; identify H isometrically with R^n. Let X=sum_i alpha_i v_i, where alpha is uniform on the standard simplex, i.e. Dirichlet(1,...,1). Then EX=0, Cov_H(X)=I_H, and the law is log-concave.

Proof of normalization: E alpha_i=1/N, E alpha_i^2=2/[N(N+1)], and E alpha_i alpha_j=1/[N(N+1)] for i!=j. The vertex sum is zero and sum_i v_i v_i^T=N(N+1)P_H, so E XX^T=P_H. These Dirichlet moments follow directly by integrating monomials on the standard simplex (the integral of product alpha_i^k_i, normalized to probability, is (N-1)! product k_i!/(N-1+sum k_i)!).

Choose the unit axis e=(v_0-v_1)/L, where L^2=2N(N+1), and write X=T e+Y with Y perpendicular to e. The vertices v_0,v_1 have the same projection w; the other projected vertices, together with w, are affinely independent. Indeed, lifting any affine dependence of those projections gives an affine combination of the original vertices parallel to v_0-v_1; affine independence of the original vertices forces all coefficients of v_j for j>=2 and the coefficient of w to vanish. Thus conditioning on Y fixes alpha_2,...,alpha_(N-1) and s=alpha_0+alpha_1. Conditional on Y, alpha_0 is uniform on [0,s] (the original barycentric density is constant and the linear slice has constant Jacobian). Since e.v_0=L/2, e.v_1=-L/2 and e.v_j=0 for j>=2,

T|Y is uniform on [-Ls/2,Ls/2].

Consequently Var(T|Y)=L^2 s^2/12 and its exact one-dimensional Poincare constant is c(Y)=L^2 s^2/pi^2. For an interval of length ell, the sharp constant ell^2/pi^2 follows by the cosine Fourier expansion, or by the first nonconstant Neumann eigenfunction sin(pi t/ell) on its centered form. The interval result is used only for this explicit uniform slice.

Every projected neighborhood with s close to 1 has positive measure. Therefore

ess sup Var(T|Y)=N(N+1)/6,
ess sup c(Y)=2N(N+1)/pi^2.

These diverge quadratically in dimension although the original law is isotropic. Isotropy and log-concavity therefore do NOT imply a universal conditional Poincare bound in an arbitrary prescribed coordinate direction. This refutes a sufficient hypothesis needed by the straightforward conditional route, not the KLS conclusion and not the possibility of a carefully selected basis.

## Why averaging the slice constant also fails (L3)

For n>=2, S=alpha_0+alpha_1 has Beta(2,n-1) distribution. Its second moment is 6/[N(N+1)]. Hence

E Var(T|Y)=1, E c(Y)=12/pi^2,
(ess sup c)/(E c)=N(N+1)/6,
P(S>1-delta)=n delta^(n-1)-(n-1)delta^n, 0<delta<1.

The unconditional average conditional constant stays bounded while the essential supremum diverges. It is nevertheless false that

E Var(f(X)|Y) <= (E c(Y)) E|partial_e f(X)|^2

for every admissible f. To see this, choose a nonzero smooth amplitude a(y) compactly supported in an interior projected neighborhood where s(y)>1-delta, and put

f(te+y)=a(y) sin(pi t/[L s(y)]).

The slice is centered. Conditional integration gives E[f|Y]=0, E[f^2|Y]=a(Y)^2/2, and E[|partial_e f|^2|Y]=a(Y)^2 pi^2/[2L^2 s(Y)^2]. Therefore the ratio of the two integrated quantities is

(L^2/pi^2) E[a(Y)^2]/E[a(Y)^2/S^2]
  >= (L^2/pi^2)(1-delta)^2.

Such projected neighborhoods exist for every delta>0 and have positive measure; the compact support stays away from s=0, so the function and its full gradient are bounded on the simplex and have finite energy. A Lipschitz extension provides an admissible function on all of H. Letting delta decrease to zero shows that the optimal constant in this directional conditional-energy inequality is ess sup c(Y), not E c(Y). Already n=2 and delta<1-sqrt(1/2) give a ratio larger than E c(Y). The large transverse gradients of these test functions are retained in the global Poincare energy; no counterexample to global KLS is asserted.

## Nonlinear dependence despite isotropy (L4)

In the same example, E[T|Y]=0, so T is uncorrelated with every linear functional of Y. That does not make the coordinate blocks independent or their maximal correlation zero. Let a(T)=T^2-1 and b(Y)=E[T^2|Y]-1=L^2 S^2/12-1. Then E[ab]=E[b^2], and Dirichlet moments give

Var(T^2)=(N-1)(5N+6)/[(N+2)(N+3)],
Var(E[T^2|Y])=(N-2)(7N+9)/[3(N+2)(N+3)].

Proof: E S^4=120/[N(N+1)(N+2)(N+3)] and E[T^4|Y]=L^4 S^4/80. Substitute L^2=2N(N+1), E T^2=1 and E S^2=6/[N(N+1)] into the two variances. Thus the maximal correlation between functions of T and functions of Y satisfies

rho >= sqrt((N-2)(7N+9)/[3(N-1)(5N+6)]) > 0,

with lower bound tending to sqrt(7/15). This is a derived nonlinear dependence calculation, not an assumed product structure. It identifies why a zero-covariance shortcut cannot justify L1 with rho=0.

## Single hardest remaining gap

Derive a dimension-independent estimate for the weighted, correlated conditional-energy expression using the FULL Euclidean gradient (including transverse energy) for every isotropic log-concave law. Neither a uniform conditional constant nor replacing the conditional constant by its average is valid. Maximal-correlation/approximate-tensorization hypotheses have not been derived from isotropy and log-concavity. The packet stops at this exact gap; the complete target is not independently proved here.

NEXT: Check the normalization and localized directional-energy inequality independently; assess a transverse-energy estimate that controls rare long fibers.
