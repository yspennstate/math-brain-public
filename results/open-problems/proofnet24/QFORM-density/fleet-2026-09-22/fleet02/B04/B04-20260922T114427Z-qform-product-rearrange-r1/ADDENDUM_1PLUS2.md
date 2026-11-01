# B04 addendum — a 1+2 mixed Fourier theorem for the large-leverage rank-three frontier

This addendum is controlling over the narrower frontier discussion in `REPORT.md`. The primary private-block theorem remains valid. After that report was written, I consumed fleet02/B02's complete `QFORM-DELOCALIZED-RANK3-INTEGRATED-FOURIER-v1` at `yspennstate/math-open-problems@2d79dea715c2baa9e8ef6c0ac174eee1712d2888`, blob `d13acb61e2846ea2e1761acca18d5e4e0f124a34`. B02 closes rank-three forms when every spectral-frame row has norm at most `1/2` and identifies the complementary large-row regime as the next rank-three frontier.

The following mixed theorem directly enters that frontier and is not contained in the original three-private-block theorem.

## Theorem `QFORM-1PLUS2-MIXED-FOURIER-v1`

Partition the physical coordinates as

`S ⊔ R ⊔ T = {1,...,n}`.

Assume that after conditioning the shared block `T`, the quadratic polynomial has the form

`Q = R_0(X_T)
   + lambda (a · X_S + beta(X_T))^2
   + (V^T X_R + gamma(X_T))^T Gamma (V^T X_R + gamma(X_T))`,                 (1)

where

- `lambda != 0`;
- `a` is nonzero and `alpha=||a||_2`;
- `V` is an `|R| x 2` real matrix with rows `v_i`;
- `M:=V^T V` is positive definite;
- `Gamma` is an invertible real symmetric `2 x 2` matrix;
- the normalized residual leverage condition holds:

`max_{i in R} v_i M^(-1) v_i^T <= 1/4`.                                      (2)

Let the coordinates of `X` be independent with probability densities bounded by one. Let `B_RV` denote the absolute constant in the small-coordinate Brascamp--Lieb Fourier bound extracted in fleet02/B02 from Rudelson--Vershynin: an orthonormal two-dimensional frame with all row norms at most `1/2` has projection characteristic function `L^1` norm at most `B_RV^2`.

Then `phi_Q` is integrable and

`||phi_Q||_1
 <= (72/pi)^(1/3) B_RV^(4/3)
    / [ alpha^2 det(M) |lambda det(Gamma)| ]^(1/3).`                           (3)

Consequently `Q(X)` has a continuous density and

`||p_Q||_infinity
 <= (72/pi)^(1/3) B_RV^(4/3)
    / { 2 pi [alpha^2 det(M) |lambda det(Gamma)|]^(1/3) }.`                    (4)

The theorem allows either sign of `lambda` and either signature of `Gamma`.

### Proof

Condition on `X_T=t`. The scalar

`Y=a·X_S+beta(t)`

and the two-vector

`Z=V^T X_R+gamma(t)`

are independent because `S` and `R` are disjoint physical coordinate blocks.

### 1. The localized one-dimensional factor

By the one-dimensional product-marginal bound of Livshyts--Paouris--Pivovarov, `Y` has density at most

`K=sqrt(2)/alpha`.

The decreasing-rearrangement calculation in the primary report gives for the density of `lambda Y^2`

`||p_{lambda Y^2}||_{3/2} <= 2 K^(2/3)|lambda|^(-1/3)`.

With `hat f(s)=int exp(i s x)f(x)dx`, Hausdorff--Young therefore gives its characteristic function `psi_1` the uniform budget

`||psi_1||_3
 <= 2(2pi)^(1/3) K^(2/3)|lambda|^(-1/3).`                                  (5)

This bound is uniform in the conditioned shift `beta(t)`.

### 2. The delocalized two-dimensional factor

Normalize the residual frame by

`W = V M^(-1/2)`.

Then `W^T W=I_2`, and (2) says every row of `W` has norm at most `1/2`. Thus the Rudelson--Vershynin small-coordinate Brascamp--Lieb estimate gives

`||Phi_{W^T X_R}||_{L^1(R^2)} <= B_RV^2`.

Since `V^T X_R=M^(1/2)W^T X_R`, a change of variables yields

`||Phi_Z||_{L^1(R^2)} <= B_RV^2 / sqrt(det M)`.                                (6)

Translation by `gamma(t)` changes only the phase of the projection characteristic function, so (6) is uniform in `t`.

Apply the same Gaussian-regularized Fresnel transfer as in fleet02/B02, now in dimension two. If `psi_2(s)` is the conditional characteristic function of `Z^T Gamma Z`, then for `s!=0`,

`|psi_2(s)|
 <= C_2 |s|^(-1)`,

where

`C_2 = B_RV^2 / [4 pi sqrt(det M) sqrt(|det Gamma|)]`.                          (7)

Indeed the two-dimensional Gaussian integral contributes `pi |s|^(-1)|det Gamma|^(-1/2)` and Fourier inversion contributes `(2pi)^(-2)`, exactly giving `1/(4pi)`. Together with `|psi_2|<=1`,

`int_R |psi_2(s)|^(3/2) ds
 <= 2[C_2 + C_2^(3/2) int_{C_2}^infinity s^(-3/2)ds]
 = 6 C_2`.

Hence

`||psi_2||_{3/2} <= (6 C_2)^(2/3).`                                            (8)

### 3. Spend the dimensions `1+2=3`

Conditional independence gives

`phi_{Q|T=t}(s)=exp(i s R_0(t)) psi_1(s)psi_2(s)`.

Hölder with exponents `3` and `3/2`, followed by (5) and (8), yields

`||phi_{Q|T=t}||_1
 <= 6^(2/3) pi^(-1/3)
    (K B_RV^2)^(2/3)
    / [ det(M)^(1/3) |lambda det(Gamma)|^(1/3) ]`.

Using `K=sqrt(2)/alpha` reduces this exactly to (3). The bound is uniform in `t`. Averaging the conditional characteristic functions and applying Tonelli preserves the same global `L^1` bound. Fourier inversion gives the continuous density and (4). QED.

## Explicit high-leverage target family newly covered

Let `r_1=e_1`. On coordinates `2,...,m+1`, take two orthonormal flat Hadamard columns `r_2,r_3` with every row of the resulting `m x 2` frame having norm `sqrt(2/m)`. Let

`A=2 r_1r_1^T-r_2r_2^T-r_3r_3^T`.

Then `A` has nonzero eigenvalues exactly `(2,-1,-1)`. Its three-dimensional spectral frame has a row of norm `1`, so fleet02/B02's `max row <=1/2` theorem does not apply. For every Hadamard order `m>=8`, however, the two-dimensional residual frame satisfies (2), with `alpha=1`, `M=I_2`, `lambda=2`, `Gamma=-I_2`. Therefore (3)--(4) give a universal integrable characteristic function and continuous bounded density for this genuinely indefinite, high-leverage rank-three family under arbitrary independent input densities bounded by one.

This is a real bridge between the localized and delocalized regimes: one full localized spectral dimension is paid for by the one-square `L^{3/2}` rearrangement budget, while the remaining two dimensions are paid for by the product-projection Brascamp--Lieb/Fresnel budget. The exponents close because `1/3+2/3=1`.

## Updated first unpaid rank-three implication

The remaining rank-three large-leverage problem is now more specific:

> Given an arbitrary orthonormal spectral frame with a row of norm `>1/2`, reduce it either to B02's fully delocalized three-dimensional branch, to the private-block theorem of the primary B04 report, or to the `1+2` mixed theorem above, **without assuming an exact spectral-coordinate zero pattern**.

The hard issue is spectral contamination: after rotating spectral coordinates to align with a large physical row, the diagonal eigenvalue matrix becomes a general symmetric `3 x 3` matrix and creates cross terms between the localized scalar and the residual two-vector. Taking absolute values after integrating the scalar would discard the residual oscillation and revert to the refuted pointwise route. A successful next step must preserve that cross-term oscillation, likely through a vector-valued rearrangement or pair-kernel estimate.

The full owner conjecture still has the additional dependence problem from eigendirections beyond rank three. No full-target claim is made.
