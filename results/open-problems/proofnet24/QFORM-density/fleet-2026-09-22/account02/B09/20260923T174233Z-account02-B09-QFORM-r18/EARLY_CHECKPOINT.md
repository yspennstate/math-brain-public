# B09 early checkpoint — aligned G*=0 endpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

First unpaid implication attacked here: **QFORM-GSTARZERO-ALIGNED-DIFFUSE-HUB-ADAPTATION-v1**.  In the exact `G_*=0` rank-two hub/star normal form, pay the case in which the transverse hub direction is spread over many physical hub coordinates, without conditioning a post-rotation coordinate and without first taking a reciprocal physical pair minor.  The calculations below pay the complementary rank-one aligned / one-physical-hub exit and show exactly why the naive Cauchy--Schwarz/Fresnel continuation loses the needed Fourier power in the diffuse survivor.

## 1. Rank-one aligned curvature: a literal physical-hub exit

Write the rank-two star as

`A[H,I] = P C^T`, `P^T P = I_2`, `G=C^T C>0`, `Z=C G^{-1/2}`,

so `Z^T Z=I_2`.  In the exact aligned rank-one leaf case suppose

`A[I,I] = Lambda + lambda (Z v)(Z v)^T`,

where `Lambda` is diagonal, `|v|=1`, and `lambda != 0`.  For a physical hub coordinate `h in H`, let `p_h` be the `h`-th row of `P` and put

`q_h = G^{1/2} p_h`, `theta_h = |v wedge q_h|^2`.

If `theta_h>0` and every whitened leaf leverage `ell_i=|z_i|^2` is at most `1/2`, then the completed mixed-hub Theorem H from `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` applies with the *single literal original coordinate* `h` as the hub, all other hub coordinates moved to the conditioned outside bank, and leaf mixed rows

`rho_i=((Zv)_i, A_{ih}) = z_i [v, q_h]`.

Because `[v,q_h]` is invertible, the normalized mixed-frame leverage is exactly invariant:

`rho_i^T (sum_j rho_j rho_j^T)^(-1) rho_i = |z_i|^2 = ell_i`,

while

`det(sum_i rho_i rho_i^T) = det([v,q_h]^T[v,q_h]) = theta_h`.

Therefore, with **arbitrary** hub core `A[H,H]`, arbitrary couplings to conditioned coordinates, affine terms and fragmented/unbounded cap-one input supports retained,

`||p_Q||_infinity <= 3*2^(4/3) (|lambda| theta_h)^(-1/3)`,

and directly

`P{Q in L} <= 3*2^(4/3) (|lambda| theta_h)^(-1/3) |L|`.

The characteristic function is integrable in this branch, hence the density is continuous.  No probability squaring is used.

There is an exact aggregate identity

`sum_(h in H) theta_h = v_perp^T G v_perp`,

since `sum_h p_h p_h^T=I_2`.  Thus the result pays every aligned rank-one configuration having one physical hub row carrying a quantitative fraction of the transverse hub currency.  It does **not** justify replacing a diffuse aggregate direction by one coordinate.

## 2. Actual target inequality from Theorem H

Let `a,b` be literal physical hubs and let `u,v` be flat orthonormal Walsh vectors on an `m`-coordinate leaf bank, `m>=4`.  Set

`Q_m = X_a^2 + X_b^2 + 4 X_a <u,Y> + 4 X_b <v,Y> + <v,Y>^2`.

On the aggregate basis `(e_a,u,e_b,v)` the coefficient matrix is the direct sum of

`[[1,2],[2,0]]` and `[[1,2],[2,1]]`,

so the spectrum is

`{(1+sqrt(17))/2, (1-sqrt(17))/2, 3, -1}`;

all four eigenvalues have modulus at least one.  Condition on `X_b` and apply Theorem H with hub `a`, curvature vector `v`, and hub-leaf vector `2u`.  The mixed Gram is `diag(1,4)`, and every mixed leverage is `u_i^2+v_i^2=2/m<=1/2`.  Hence

`||p_(Q_m)||_infinity <= 3*2^(2/3) = 4.762203...`,

and `P{Q_m in L} <= 3*2^(2/3)|L|`, uniformly over every admissible product law.  The dense same-side square `<v,Y>^2` and the nonzero physical hub core are both retained.

## 3. Exact obstruction to the naive square-root-decoupling continuation

Consider the general aligned two-plane phase after whitening,

`Q = F_H(X_H) + 2 (P^T X_H)^T S (Z^T Y) + (Z^T Y)^T R (Z^T Y) + Y^T Lambda Y + linear`,

where `P,Z` have two orthonormal columns, `S` is invertible, `R=R^T` is arbitrary and `Lambda` is diagonal.  Cauchy--Schwarz in the hub bank cancels the arbitrary hub phase and gives `|phi_Q(t)|^2` bounded by the characteristic function of the doubled leaf form on independent copies `Y,Y'`.  In the six-dimensional aggregate coordinates

`u=P^T X_H`, `z=Z^T Y`, `z'=Z^T Y'`,

the non-diagonal low-rank matrix is

`M_6 = [[0,S,-S],[S^T,R,0],[-S^T,0,-R]]`.

Under the orthogonal change `a=(z+z')/sqrt(2)`, `b=(z-z')/sqrt(2)`, this becomes

`[[0,0,sqrt(2)S],[0,0,R],[sqrt(2)S^T,R,0]]`,

which is the bipartite matrix `[[0,K],[K^T,0]]` with `K=[sqrt(2)S; R]` of size `4 x 2`.  Since `S` is invertible, `rank K=2`, hence

`rank M_6 = 4`

**for every aligned same-side matrix `R`**.  Thus even under perfect leverage gates, applying the absolute-value Fresnel/Brascamp--Lieb rank-four estimate after this Cauchy--Schwarz step yields only `|phi_Q(t)|^2 = O(|t|^-2)`, i.e. `|phi_Q(t)|=O(|t|^-1)`.  The Fourier integral is critical and does not give the required linear small-ball bound.  The aligned curvature is exactly spent cancelling the decoupling copy, rather than creating a third post-root smoothing power.

This is a method obstruction, not a counterexample to QFORM.  It shows why the remaining diffuse aligned branch needs an undecoupled/grouped phase-sensitive receiver (or a different real-variable argument), not another absolute square-root decoupling followed by Theorem F.
