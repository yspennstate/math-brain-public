# Projection-product interaction: the proposed conditional 3-D density moment is not uniformly bounded

Run: `20260922T175342Z-fleet03-B16-QFORM-r14`  
Worker: fleet03/B16  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`  
Status: **proved correction to a proposed proof route; full QFORM conjecture remains OPEN**.

## 1. Full target and this run's first unpaid implication

The full target is: for every dimension, every independent real input family with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove that the quadratic form has an essentially bounded density with one universal constant, or give a valid counterexample. Continuity is a separate desired conclusion.

The current owner message proposes, as a route from the exact-rank-three theorem to full rank, a universal bound on

\[
\mathbb E_Z\,\|\rho_{Y\mid Z}\|_\infty^{2/3},
\]

where `Y` denotes three selected spectral coordinates and `Z` the remaining spectral coordinates. This report tests that implication before using it.

The result is negative: the displayed quantity is unbounded already for a four-dimensional independent cap-one product law and a rank-three orthogonal splitting. In fact every positive moment below one is unbounded. This refutes the **standalone normalized conditional-density-moment lemma**, not the quadratic-form bounded-density conjecture.

## 2. Exact fragmented product construction

Let

\[
v=\frac12(1,1,1,1)\in\mathbb R^4,
\qquad E=v^\perp,
\]

and let `U` be any `4 x 3` matrix with orthonormal columns spanning `E`. Define

\[
Y=U^T X,\qquad Z=v^T X=\frac{X_1+X_2+X_3+X_4}{2}.
\]

For an integer `m>=1`, set

\[
E_m=\bigcup_{k=0}^{m-1}[10k,10k+1/m].
\]

Take the independent input densities

\[
f_1=1_{E_m},\qquad f_2=f_3=f_4=1_{[0,1]}.
\]

Each density is between zero and one and integrates to one. Hence the joint input density is the indicator of the product set

\[
\Omega_m=E_m\times[0,1]^3.
\]

Because the map `x -> (U^T x,v^T x)` is orthogonal, the joint density of `(Y,Z)` is

\[
\rho_m(y,z)=1_{\Omega_m}(Uy+vz).
\]

Write `p_m` for the density of `Z`. For every `z` with `p_m(z)>0`, the conditional density of `Y` given `Z=z` is the normalized indicator of the corresponding three-dimensional section. Therefore

\[
\boxed{\|\rho_{Y\mid Z=z}\|_\infty=\frac1{p_m(z)}}. \tag{2.1}
\]

No spectral-coordinate independence is asserted or used.

## 3. The marginal of Z consists of m disjoint identical packets

Conditioning on the component of `E_m` containing `X_1`, write

\[
X_1=10k+U_m,
\]

where `k` has mass `1/m` and, conditional on `k`, `U_m` is uniform on `[0,1/m]` with normalized density `m`. Then

\[
Z=5k+T_m,
\qquad
T_m=\frac{U_m+X_2+X_3+X_4}{2}.
\]

Let `g_m` denote the probability density of `T_m`. Its support has length at most

\[
\frac{3+1/m}{2}<2.
\]

Since consecutive packet translations differ by `5`, these supports are disjoint, and

\[
\boxed{
 p_m(z)=\frac1m g_m(z-5k)
}
\]

on the `k`-th packet.

We also need a uniform upper bound on `g_m`. Let

\[
W=\frac{X_2+X_3+X_4}{2}.
\]

For the Irwin-Hall density of `S=X_2+X_3+X_4`, the exact maximum is `3/4` at `S=3/2`. Scaling by two gives

\[
\|p_W\|_\infty=\frac32.
\]

The variable `T_m` is the sum of `W` and the independent probability variable `U_m/2`; convolution with a probability density cannot increase the `L^infinity` norm. Hence

\[
\boxed{\|g_m\|_\infty\le\frac32.} \tag{3.1}
\]

## 4. Every positive conditional L-infinity moment below one diverges

Fix `0<alpha<1`. From (2.1),

\[
\mathbb E\|\rho_{Y\mid Z}\|_\infty^\alpha
=\int p_m(z)^{1-\alpha}\,dz.
\]

Using the disjoint packet decomposition,

\[
\int p_m^{1-\alpha}
= m\,m^{-(1-\alpha)}\int g_m^{1-\alpha}
= m^\alpha\int g_m^{1-\alpha}.
\]

For `0<=g<=3/2`,

\[
g^{1-\alpha}=g\,g^{-\alpha}\ge (3/2)^{-\alpha}g
\]

on the positive set of `g`. Since `g_m` is a probability density, (3.1) yields

\[
\boxed{
\mathbb E\|\rho_{Y\mid Z}\|_\infty^\alpha
\ge \left(\frac{2m}{3}\right)^\alpha.
} \tag{4.1}
\]

Thus no universal finite bound exists for any fixed `alpha in (0,1)`. In particular, at the exponent required by the proposed rank-three coarea conditioning step,

\[
\boxed{
\mathbb E\|\rho_{Y\mid Z}\|_\infty^{2/3}
\ge \left(\frac{2m}{3}\right)^{2/3}
\longrightarrow\infty.
} \tag{4.2}
\]

Numerically, the prefactor is `(2/3)^(2/3)=0.7631428283688879...`.

This is a source-valid product-law construction: all four original coordinates remain independent and all four input densities satisfy the exact cap-one assumption.

## 5. Application of completed partner mathematics: the failure persists under strong rank-three determinant-bank geometry

The designated partner result is fleet04/B16 run `20260922T161909Z-fleet04-B16-QFORM-r2`, canonical source

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`,

which proves for an exact-rank-three Parseval frame that a row of leverage `c>1/2` and a second row of residual leverage `h>1/2` have pair Gram area

\[
G_{ij}=ch,
\]

and hence, for `A_0=U\Lambda U^T`,

\[
\sum_{k\ne i,j}|\det (A_0)_{\{i,j,k\}}|
=|\det\Lambda|G_{ij}.
\]

For the present projection `E=v^perp`, its projection matrix is

\[
P=I-vv^T,
\]

so every row of `U` has leverage

\[
c=P_{ii}=\frac34,
\]

and for distinct rows

\[
\langle r_i,r_j\rangle=P_{ij}=-\frac14.
\]

The residual leverage of row `j` after row `i` is therefore

\[
h=\frac34-\frac{(1/4)^2}{3/4}
=\frac34-\frac1{12}
=\frac23.
\]

Applying the completed partner identity gives the **actual inequality**

\[
\boxed{G_{ij}=\frac34\cdot\frac23=\frac12.} \tag{5.1}
\]

Consequently, for any exact-rank-three core on this spectral subspace with `|det Lambda|>=1`,

\[
\boxed{
\sum_{k\ne i,j}|\det (A_0)_{\{i,j,k\}}|\ge\frac12.
} \tag{5.2}
\]

Thus the divergence (4.2) is not caused by weak or vanishing rank-three determinant geometry. It occurs on a uniformly nested-heavy, determinant-rich frame. In particular, normalizing the conditional spectral density destroys precisely the original-coordinate product information that the determinant-bank mechanisms need.

For example, take `Lambda=diag(1,1,-1)`. Then `A_0=U Lambda U^T` has exactly three nonzero eigenvalues, all of magnitude one, and null direction `v`; it is a legitimate rank-three target matrix. The current exact-rank-three theorem controls its quadratic-form density, while the proposed conditional `2/3` moment still diverges along the laws above. Hence (4.2) is a failure of the proposed proof interface, not a QFORM counterexample.

## 6. What this rules out and what remains

**Refuted intermediate statement.** There is no universal constant `C` such that every orthogonal split into a three-dimensional spectral subspace `Y` and complementary coordinates `Z` satisfies

\[
\mathbb E_Z\|\rho_{Y\mid Z}\|_\infty^{2/3}\le C
\]

under only independent original-coordinate densities bounded by one. More strongly, no positive moment exponent `alpha in (0,1)` has such a universal bound.

**Not refuted.** The full quadratic-form bounded-density conjecture remains open. The exact-rank-three theorem is not challenged. The construction does not produce an unbounded quadratic-form density.

**Replacement obligation.** Full-rank work must keep the **unnormalized original product fiber weight** coupled to the curved/quadratic payment, or use a global Fourier/small-ball mechanism before taking conditional suprema. A receiver-only normalized conditional-density estimate cannot be the universal bridge from the exact-rank-three theorem to full rank. The most relevant next step for B16 is a weighted outer-pivot/grouped-coordinate inequality in which the packet mass `p_Z(z)` is never divided out before curvature is paid.

## 7. Corrections and scope discipline

This proof uses none of the refuted law-uniform pointwise van-der-Corput bounds, no independence after rotation, no receiver-only bounded projection-density shortcut, and no naive fiber-sup dimension-free integral. It preserves arbitrary fragmented supports. Essential boundedness of the full target is **not** claimed here; continuity is also **not** proved in this run.

The construction is exact and analytic; the accompanying checker only verifies the elementary rational geometry and numerical prefactor and is not the proof.
