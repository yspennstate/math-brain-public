SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B12, 2026-09-22T21:29:24Z.
attacking: exact stability of the completed three-disjoint-bank theorem under an added spectral direction, and an exact diffuse-frame falsifier for any uniform exact-bank extraction from the three-large-eigenvalue hypothesis.

# fleet02/B12 r18 — additional-eigenvalue control

Status: SUPPORTING THEOREM + EXACT STRUCTURAL FALSIFIER PROVED. Full QFORM remains OPEN. Execution context: WITHOUT_VERIFIED_BRAIN.

## Source pins




`Q = Y^T M Y + 2 Y^T C Z + psi(Z)`,   `s_min(M) >= s > 0`,

then `||p_Q||_infinity < 296/s`, with arbitrary outside completion/coupling and without any independent-convolution assumption.

The current correction inbox was read at the pinned control commit. This report does not use corrected-away worst-fiber, fixed-minor, cross-minor-alone, rotated-independence, or per-direction oscillatory shortcuts.

## Theorem A — aligned rank-one spectral-direction stability

Let `T_1,T_2,T_3` be disjoint original-coordinate banks, `Z` the remaining original coordinates, and let `u_j` be the normalized bank vectors in the partner theorem. Suppose

`Q_0 = Y^T M Y + 2 Y^T C Z + psi(Z)`,   `Y_j = u_j^T X_{T_j}`,

with `s_min(M)=s_0>0`. Add a rank-one quadratic direction `tau (v^T X)^2` such that on each bank

`v_{T_j} = alpha_j u_j`,

while `v_Z` is arbitrary. Put `alpha=(alpha_1,alpha_2,alpha_3)^T`. Then exactly, in ORIGINAL coordinates,

`v^T X = alpha^T Y + v_Z^T Z`,

so the perturbed form is again a partner-theorem form, with

`M_tau = M + tau alpha alpha^T`,
`C_tau = C + tau alpha v_Z^T`,
`psi_tau(Z) = psi(Z) + tau (v_Z^T Z)^2`.

Therefore, whenever `s_min(M_tau)>=s_tau>0`,

`||p_Q||_infinity < 296/s_tau`.

This is source-valid: the only conditioning/aggregation is over disjoint ORIGINAL-coordinate banks; the dependent quadratic remainder is absorbed by the partner mixed-norm theorem rather than convolved as if independent.

Two quantitative consequences are immediate.

1. General both-sign perturbation: Weyl gives

`s_min(M_tau) >= s_0 - |tau| ||alpha||_2^2`.

Thus if `|tau| ||alpha||_2^2 <= (1-eta)s_0`, then

`||p_Q||_infinity < 296/(eta s_0)`.

The spectral amplitude `|tau|` itself may be arbitrarily large provided its physical overlap with the three bank statistics is correspondingly small.

2. Definite-core no-loss / leverage form. If `M >= s_0 I` and `tau>=0`, then `M_tau>=M`, so the arbitrary added direction costs nothing: `||p_Q||_infinity <296/s_0` for every `tau>=0`, however large. If `tau=-beta<0` and

`beta alpha^T M^{-1} alpha <= 1-eta`,

then for every `y`, Cauchy--Schwarz in the `M` metric gives

`beta (alpha^T y)^2 <= beta(alpha^T M^{-1}alpha)(y^T M y) <= (1-eta)y^T M y`,

hence `M-beta alpha alpha^T >= eta M >= eta s_0 I` and again

`||p_Q||_infinity <296/(eta s_0)`.

The sign-reversed statement holds for `M<=-s_0 I`. This is a genuine stability theorem for adding smaller/larger rank-one directions of either sign, with the exact physical-overlap price exposed.

## Theorem B — no uniform exact three-bank extraction, even with one arbitrary extra eigenvalue

For every fixed real `tau` and every `epsilon>0`, there are arbitrarily large `n` and a real symmetric `n x n` matrix `A` with

`spec(A) = {1,1,1,tau,0,...,0}`

(`tau=0` understood with only the three nonzero unit eigenvalues) such that every exact representation of the fleet03/B12 three-disjoint-bank type has

`s_min(M) < epsilon`.

This includes a smaller fourth eigenvalue (`tau=+/-1/2`), a larger fourth eigenvalue (`|tau|>1`), and either sign. Moreover one may take `|tau_n|=sqrt(n)->infinity` while every exact bank core still has `s_min(M)->0`.

### Construction

Let `theta_i=2 pi i/n`, `i=0,...,n-1`, with `n>=5`. Define the `n x 3` Fourier frame

`r_i = (1/sqrt(n), sqrt(2/n) cos theta_i, sqrt(2/n) sin theta_i)`

and let `R` have rows `r_i`. The three columns of `R` are orthonormal. For a phase `phi`, set

`w_i = sqrt(2/n) cos(2 theta_i + phi)`.

For `n>=5`, `w` is a unit vector orthogonal to all three columns of `R`. Put

`A = R R^T + tau w w^T`.

Hence the spectrum is exactly `{1,1,1,tau,0,...,0}`.

The entries obey the uniform physical-coordinate bound

`A_ij = [1+2 cos(theta_i-theta_j) + 2 tau cos(2theta_i+phi)cos(2theta_j+phi)]/n`,

so

`|A_ij| <= (3+2|tau|)/n`.                                           (1)

### Every exact bank must be a singleton

Write `P=RR^T`. For distinct `i,j`, put `Delta=theta_j-theta_i`, `c=cos Delta`, `k=1+2c`, and

`a=cos(2theta_i+phi)`, `b=cos(2theta_j+phi)`.

The two-coordinate principal determinant is

`det A[{i,j}] = [9-k^2 + 2 tau G_ij(phi)]/n^2`,

where

`G_ij(phi)=3(a^2+b^2)-2kab`.

For `tau>=0`, `P[{i,j}]` is positive definite and the rank-one update is positive semidefinite, so every such determinant is positive.

For `tau<0`, `G_ij` is a nonconstant affine function of one cosine. Indeed with `d=2 Delta` and `u=2(2theta_i+phi)+d`,

`G_ij(phi) = (3-k cos d) + (3 cos d-k) cos u`.

The coefficient of `cos u` can vanish only when

`3 cos(2Delta) = 1+2 cos Delta`,

i.e. `(3 cos Delta+2)(cos Delta-1)=0`. Distinct indices exclude `cos Delta=1`; and `cos Delta=-2/3` is impossible for `Delta=2 pi m/n`, since `2 cos Delta` is an algebraic integer whereas `-4/3` is a nonintegral rational. Thus, for each pair, determinant zero excludes only finitely many phases. A phase outside the finite union over all pairs makes every `2 x 2` principal block nonsingular.

Now suppose an exact partner representation uses a bank `T_j` with at least two coordinates. Inside that bank the quadratic matrix is exactly

`A[T_j,T_j] = M_jj u_j u_j^T`,

which has rank at most one. But the chosen construction has a nonsingular two-coordinate principal subblock inside every `T_j` of size at least two, hence rank at least two: contradiction. Therefore every bank is a singleton.

Because the partner theorem normalizes `u_j`, a singleton statistic has coefficient `+/-1`. Thus for singleton banks `I={i_1,i_2,i_3}`, the core `M` is just a diagonal sign conjugate of the physical principal block `A[I,I]`. By (1),

`||M||_op <= ||M||_infinity <= 3(3+2|tau|)/n`.

Consequently

`s_min(M) <= 3(3+2|tau|)/n`.                                      (2)

Given any `epsilon>0`, choose `n>3(3+2|tau|)/epsilon` (and, for `tau<0`, a nonexceptional phase). This proves the claim.

For the genuinely growing additional eigenvalue `tau_n=+/-sqrt(n)`, (2) gives

`s_min(M) <= 9/n + 6/sqrt(n) -> 0`,

while `|tau_n|->infinity` and the other three eigenvalues stay exactly `1,1,1`.

## Interpretation and remaining implication

The partner theorem is strong enough to absorb arbitrary outside quadratic completion once a uniformly conditioned exact three-bank core is present. Theorem A quantifies a useful class of added eigendirections that preserve such a core. Theorem B shows that the global hypothesis `s_3(A)>=1` cannot supply that core by exact disjoint-bank extraction at any universal scale: a diffuse Fourier frame can make every admissible exact bank singleton and every resulting `3 x 3` core vanish in norm, even while a fourth eigenvalue is smaller, larger, opposite-sign, or diverging in magnitude.

This is NOT a counterexample to QFORM. It is a counterexample to the stronger reduction “three large eigenvalues force an exact fleet03/B12 three-bank core with `s_min(M)>=c>0`.” The next bridge must therefore be approximate/overlapping aggregation: retain several bank statistics, or control the factorization error jointly before any reciprocal `s_min` payment. Exact one-scalar-per-bank extraction is insufficient.

Target-level movement: OPEN -> OPEN.
Mechanism-level movement: proved aligned-spike stability and ruled out uniform exact three-bank extraction, including under an arbitrarily large fourth eigenvalue of either sign.
