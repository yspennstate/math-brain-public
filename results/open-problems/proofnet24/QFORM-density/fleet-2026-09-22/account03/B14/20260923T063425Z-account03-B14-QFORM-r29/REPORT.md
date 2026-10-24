SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T06:34:25Z.
attacking: arbitrary-bank square compression: preserve unbounded fragmented supports and translations while replacing the two-coordinate conjugate shear by a whole independent coordinate bank.

# QFORM-ARBITRARY-BANK-SQUARE-LOCALIZATION-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account03/B14`  
Run: `20260923T063425Z-account03-B14-QFORM-r29`  
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREM; FULL QFORM OPEN; full-target continuity OPEN.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact obligation and sources actually used

The B14 obligation is to preserve arbitrary translations, distant fragments, and unbounded supports with no moment bounds through a genuine reduction. This run attacks the newest account04/B14 residual question: replace the two-coordinate conjugate shear by a collective independent coordinate bank before any thin-fiber normalization.

Fresh source control at startup was `yspennstate/math-research-brain@9bb818bc402254e738c7d86b13082b386532c0dd`, OWNER CONTROL revision `2026-09-22.15`. The live corrections were consumed before the proof. In particular this proof does not use pointwise law-uniform Fresnel decay, independence after spectral rotation, an arbitrary-joint coarea bound, normalized conditional density caps, or a uniformly good single physical minor.

Two completed mathematical sources are applied at equations.

1. **Designated partner account04/B14 r7**, read at
   `yspennstate/math-open-problems@ea1c554635a706c9afd727a9263e5b70277ae966`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T051013Z-account04-B14-scale-shear-r7/REPORT.md`.
   Its proof gives the scale-covariant pair-log/square-remainder inequality and optimizes it to the function `H` below. The special two-coordinate shear is used there only to provide a density cap for the scalar square variable.
2. **Rogozin--Ball one-dimensional product projection bound**, as explicitly used and proved-source-pinned in account01/B16, read at
   `yspennstate/math-open-problems@ea1c554635a706c9afd727a9263e5b70277ae966`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260922T190433Z-account01-B16-QFORM-auto11/REPORT.md`:
   for independent cap-one coordinates `V_j` and any nonzero coefficient vector `a`, the scalar `W=a^T V` has a density satisfying
   `||p_W||_infinity <= sqrt(2)/||a||_2`.

The designated partner's finite-mixture localization theorem is also used in Section 5 to state the exact no-loss extreme-law reduction; the main analytic bound itself already works directly for arbitrary cap-one laws.

## 2. The arbitrary-bank theorem

Let `X_1,X_2,V_1,...,V_m` be independent real random variables, each with probability density bounded by one. Let `c,d` be nonzero reals, `a in R^m\{0}`, and let `beta, ell_1, ell_2, gamma` be arbitrary real numbers. Define

`W=a^T V-beta`

and

`Q = 2 c X_1 X_2 + (d/2) W^2 + ell_1 X_1 + ell_2 X_2 + gamma.`        (2.1)

Put

`K_a := sqrt(2)/||a||_2`,

`theta := |c| K_a^2 / |d| = 2|c|/(|d| ||a||_2^2)`,                  (2.2)

and

`H(theta) = 8 sqrt(2) theta^(1/4)` for `0<theta<=1/64`,

`H(theta) = 4 + 2 log(8 sqrt(theta))` for `theta>=1/64`.              (2.3)

### Theorem 2.1 — `QFORM-ARBITRARY-BANK-SQUARE-v1`

The law of `Q` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= |c|^(-1) H(theta). )`                    (2.4)

The bound is uniform in `m`, the coefficient pattern of `a`, `beta`, `ell_1`, `ell_2`, `gamma`, all support locations and diameters, all fragment counts and fragment separations, and all moments. No compact-support or connected-support hypothesis is used.

### Proof

By the product-projection theorem,

`||p_W||_infinity <= K_a = sqrt(2)/||a||_2`.                         (2.5)

The translation `beta` has no effect on this cap.

Normalize the output by `c`. The first two coordinates then form the physical hyperbolic pair `2X_1X_2`, with determinant parameter `D=1` and smallest pair singular value `kappa=1` in the notation of the completed pair-log envelope. The remaining scalar is

`R=(d/(2c)) W^2`.                                                     (2.6)

For every center `t` and every `rho>0`, the inverse image under `w -> (d/(2c))w^2` of `(t-rho,t+rho)` has total Lebesgue length at most

`4 sqrt(|c|/|d|) sqrt(rho)`.                                         (2.7)

Multiplying by (2.5) gives the uniform small-ball estimate

`sup_t P{|R-t|<rho} <= min{1, 4 K_a sqrt(|c|/|d|) sqrt(rho)}`

`= min{1,4 sqrt(theta) sqrt(rho)}.`                                   (2.8)

Now apply the actual quantitative inequality proved inside designated partner account04/B14 r7 before its special conjugate-shear cap is substituted. For every cutoff `r>0`, the pair-log envelope plus layer cake gives

`||p_(Q/c)||_infinity <= 2 sqrt(2)/r + 2 Psi(4 sqrt(2) r sqrt(theta)),` (2.9)

where

`Psi(z)=z` for `0<=z<=1`, and `Psi(z)=1+log z` for `z>=1`.             (2.10)

This is the exact point at which the completed partner result is used. The only input needed to pass from its two-coordinate shear to the present whole bank is the replacement of its scalar cap `(1+|alpha|)^(-1)` by the valid collective cap `K_a` in (2.5); equations (2.7)--(2.8) show the resulting dimensionless parameter explicitly.

Optimization is the same exact calculus as in the partner proof. On the linear branch of `Psi`, the minimizer is

`r_* = 1/(2 theta^(1/4))`,                                            (2.11)

valid exactly for `theta<=1/64`, and (2.9) equals

`8 sqrt(2) theta^(1/4)`.                                              (2.12)

On the logarithmic branch the minimizer is

`r_*=sqrt(2)`,                                                        (2.13)

valid exactly for `theta>=1/64`, and the value is

`4+2 log(8 sqrt(theta))`.                                             (2.14)

Thus `||p_(Q/c)||_infinity<=H(theta)`. Rescaling the output by `c` gives (2.4). Absolute continuity is part of the pair-log mixture conclusion. QED.

## 3. Target-level constant: the bank dimension disappears completely

The homogeneous matrix in (2.1), in the original independent coordinates, is the orthogonal direct sum of

`[[0,c],[c,0]]`

and the rank-one bank block

`(d/2) a a^T`.                                                        (3.1)

Its nonzero eigenvalues are exactly

`c, -c, (d/2)||a||_2^2`.                                             (3.2)

Hence this family satisfies the ORIGINAL three-large-eigenvalue hypothesis exactly when

`|c|>=1`,

`(|d|/2)||a||_2^2 >=1`.                                              (3.3)

Under (3.3),

`theta = 2|c|/(|d|||a||_2^2) <= |c|`.                                (3.4)

The function `H` in (2.3) is increasing: both branches are increasing and agree at `theta=1/64` with value `4`. Since `|c|>=1`, the logarithmic branch applies at `|c|`, so

`||p_Q||_infinity <= H(|c|)/|c|`

`= [4+2log 8 + log |c|]/|c|`.                                        (3.5)

The right side is strictly decreasing for `|c|>=1`, because its derivative is

`-[3+2log 8 + log |c|]/|c|^2 <0`.                                    (3.6)

Therefore the entire target-valid arbitrary-bank family obeys the universal bound

`boxed( ||p_Q||_infinity <= 4+2 log 8 = 8.158883083... . )`           (3.7)

This is independent of bank dimension and remains valid when every individual coefficient `a_j` tends to zero, provided the collective norm in (3.3) supplies the third eigenvalue.

### Diffuse-bank stress test

Take `m=N`,

`a_N = sqrt(2/N) (1,...,1)`, `c=1`, `d=1`.                            (3.8)

Then every individual coefficient is `sqrt(2/N)->0`, while

`(d/2)||a_N||_2^2=1`.                                                 (3.9)

The matrix has eigenvalues `{1,-1,1}` for every `N`, and (3.7) gives the same `<8.159` density bound for all `N`. Any proof that selects one bank coordinate before reciprocal payment would instead see a coefficient of order `N^(-1/2)` and can lose a power of `N`; the collective projection cap avoids that loss.

## 4. Outside conditioning and arbitrary translations

Let `Z` be any further collection of original independent coordinates. Suppose that after conditioning on `Z=z`, the active variables have the form

`Q_z = 2cX_1X_2 + (d/2)(a^T V-beta(z))^2`

`      + ell_1(z)X_1 + ell_2(z)X_2 + gamma(z)`,                       (4.1)

with arbitrary measurable functions `beta,ell_1,ell_2,gamma` of `z`. No boundedness of these functions is assumed.

For every fixed `z`, Theorem 2.1 gives the SAME interval inequality

`P{Q_z in I | Z=z} <= |c|^(-1)H(theta) |I|`.                         (4.2)

Averaging over `z` yields

`P{Q in I} <= |c|^(-1)H(theta)|I|`,                                  (4.3)

with exactly the same constant. Thus arbitrarily large conditioning-generated translations and affine pair terms cost nothing. In particular no tail or moment estimate for `Z`, `beta(Z)`, or the active variables is introduced.

Physical translations of any bank coordinate merely change `beta`; translations of the pair coordinates only alter `ell_1,ell_2,gamma`. Hence all deterministic shifts of the original product law are also free.

## 5. Exact law-localization consequence

Let `D` be the class of all cap-one product laws for the active original coordinates and `F` the class whose one-dimensional marginals are indicators of compact finite unions of intervals of total measure one. Designated partner account04/B14's completed finite-mixture localization theorem implies that every `mu in D` is approximable in total variation by finite convex mixtures of laws from `F`, and every uniform interval inequality transfers with no loss.

Applying it to the actual inequality (4.3) gives

`sup_{mu in D} sup_I P_mu{Q in I}/|I|`

`= sup_{nu in F} sup_I P_nu{Q in I}/|I|`                              (5.1)

for the family (4.1), with the affine parameters still arbitrary. Therefore the constant in (2.4) and (3.7) is insensitive to unbounded support, arbitrarily distant fragments, arbitrarily many fragments, and arbitrary translations. No bounded-diameter reduction and no fixed fragment-count reduction is asserted.

## 6. What this changes and what remains unpaid

This run extends the newest partner result from a **two-coordinate conjugate shear** to an **arbitrary-dimensional independent bank**, with a better structural interpretation:

`theta = |hyperbolic eigenvalue| / |rank-one bank eigenvalue|`.       (6.1)

Thus a completely diffuse rank-one bank is already harmless; one must not select a single bank coordinate. This closes a real aggregate-before-inversion branch and preserves the full rough-law/translation scope.

It does **not** solve the full conjecture. The remaining hard cases include:

- within-bank quadratic curvature of rank greater than one or not aligned with the single compressed direction;
- pair-to-bank cross couplings that cannot be removed before conditioning;
- affine kernel leakage in directions orthogonal to `a`;
- the general no-pivot/N3 structural implication showing that every target matrix enters this or another already-paid branch.

Continuity is not claimed. The argument proves existence of an essentially bounded density in the stated branch. A separate regularity argument would be required for a continuous representative.

## 7. Independent-review status

This is a new supporting theorem and has not received the two end-to-end reviews required for a full candidate solution. The full conjecture remains OPEN / NOT PROVED / NOT DISPROVED.
