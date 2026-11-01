SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-22T19:58:03Z.
attacking: a two-large-eigenvalue ridge half-Riesz estimate for the Schur residual, so one physical scalar pivot can use exactly the three large eigenvalues of the owner target rather than requiring a fourth.

# fleet03/B18 — ridge half-Riesz transfer through a physical scalar pivot

**Run:** `20260922T195803Z-fleet03-B18-QFORM-r16`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Classification:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH`  
**Full target:** `OPEN / NOT PROVED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. New result

I prove a fractional-potential analogue of the completed ridge-density theorem which needs only **two** large eigenvalues.  This is exactly the number left in a Schur complement after spending one physical scalar pivot from a matrix having three large eigenvalues.

### Theorem A — `QFORM-RIDGE-HALF-RIESZ-TWOEIG-v1`

Let `S` be a real symmetric matrix with second singular value

` s_2(S) >= s > 0 `,

and let `P` be the spectral projection of `S` onto all eigenspaces with

` |lambda(S)| >= s/64 `.

Assume

` max_i P_ii <= 1/32. `                                           (1.1)

Let `Z_i` be independent real random variables with probability densities bounded by one.  For arbitrary `b,d`, put

` R=Z^T S Z+b^T Z+d. `

Then

` sup_u E |R-u|^(-1/2) <= C_H s^(-1/2), `                        (1.2)

where

` C_H = [192/(5 sqrt(13))] (12 e)^(1/4) < 25.453. `              (1.3)

No moment, centering, compact-support, log-concavity, connected-support, smoothness, or Gaussian hypothesis is used.  The original coordinates remain independent throughout; no eigenbasis rotation is treated as independence.

### Corollary B — target-level scalar-pivot/diffuse-Schur branch

Let `A` be symmetric with `s_3(A)>=s>0`.  Suppose some ORIGINAL coordinate `i` has nonzero physical diagonal

` a=A_ii != 0. `

Write, after putting this coordinate first,

` A=[[a,b^T],[b,C]],   S=C-bb^T/a. `                             (1.4)

If the spectral projection of this Schur complement `S` onto `|lambda(S)|>=s/64` obeys (1.1), then for all independent cap-one input densities,

` ||p_(X^T A X)||_infinity <= C_H / sqrt(|a| s). `               (1.5)

Thus, for example, the branch `s_3(A)>=1`, `|A_ii|>=1/32`, and diffuse Schur window (1.1) has the dimension-free bound

` ||p_Q||_infinity < 143.981. `                                  (1.6)

This is a genuine branch of the owner's exact theorem: extra spectrum may be arbitrary, including full rank and nonseparable small tails.  It is not an exhaustive reduction, because neither a uniformly large scalar pivot nor (1.1) is forced by the bare spectral hypothesis.

Only absolute continuity and essential boundedness are claimed from Corollary B.  A continuous representative is **not** proved here.

## 2. Primary-source audit: the partition theorem is used with its exact hypotheses

Primary source: A. W. Marcus, D. A. Spielman, N. Srivastava, *Interlacing families II: Mixed characteristic polynomials and the Kadison–Singer problem*, Annals of Mathematics 182 (2015), 327–350, Corollary 1.5, DOI 10.4007/annals.2015.182.1.8.

Corollary 1.5 says: if finite vectors `u_i in C^d` satisfy

` sum_i u_i u_i^* = I,      ||u_i||^2 <= delta, `               (2.1)

then for every positive integer `r` there is a partition into `r` sets such that every partial frame operator has norm at most

` (1/sqrt(r)+sqrt(delta))^2. `                                   (2.2)

Here the rows of an orthonormal spectral frame satisfy (2.1) exactly.  I use `r=2`, `delta=1/32`; hence each side has upper Gram bound `25/32`, and since the two Gram matrices sum to the identity, each also has lower Gram bound `7/32`.  There is no probability-law hypothesis in this deterministic source theorem, so no hidden Gaussian/log-concave transfer occurs.

I also rechecked the sharp rearrangement source used by the designated partner, T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190.  Its Theorem 1/Corollary 1 concerns **sums of independent random vectors with bounded maximum densities**.  It does not justify replacing an arbitrary same-side quadratic remainder by a linear bank.  I use it only through the partner's already-proved disjoint-bank scope below, not as a generic quadratic-form theorem.

## 3. Analytic dependency that is already proved

I use the completed free-regularizer/ridge characteristic-function theorem at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`

path

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

For any ORIGINAL-coordinate cut with cross block `B`, set

` K_gamma = B B^T (gamma^2 I+B B^T)^(-1), `
` theta = tr K_gamma, `
` D = det(I+B B^T/gamma^2). `

If `max_i (K_gamma)_ii <= q/2`, the proved argument gives, for the full quadratic form including arbitrary self blocks and affine terms,

` |phi(t)| <= D^(-1/(4q)) [L_q/(2 gamma |t|)]^(theta/(2q)), `    (3.1)

where `L_q=pi e sqrt(2/q)`.  The theorem is proved from sharp Young/Hausdorff–Young and geometric Brascamp–Lieb after independent-copy decoupling; no law-uniform pointwise Fresnel estimate is assumed.

For density inversion that report requires `theta>2q`.  The present observation is that the half-Riesz kernel has a weaker integrability threshold: for `q=1`, `theta>1` suffices.

## 4. Proof of Theorem A

### 4.1 Build a physical cross cut from the spectral window

Write

` S=S_H+E, `

where `S_H=U Lambda U^T` is the spectral truncation to `|lambda|>=s/64`.  Then

` ||E|| < s/64, `                                               (4.1)

`U^T U=I`, and every row `u_i` satisfies `||u_i||^2=P_ii<=1/32`.

Apply MSS Corollary 1.5 with two parts.  There is a partition `I,J` of the ORIGINAL coordinates such that

` 7/32 I <= M_I:=U_I^T U_I <=25/32 I, `
` 7/32 I <= M_J:=U_J^T U_J <=25/32 I. `                        (4.2)

Let

` B_0=S_H[I,J]=U_I Lambda U_J^T. `

By polar factorization of `U_I,U_J`, the nonzero singular values of `B_0` are those of

` M_I^(1/2) Lambda M_J^(1/2). `

Consequently

` s_k(B_0) >= (7/32) s_k(Lambda). `                              (4.3)

Because `s_2(S)>=s`, the high spectral window contains at least two eigenvalues of magnitude at least `s`, so

` s_2(B_0) >= 7s/32. `                                          (4.4)

The actual full cross block is

` B=S[I,J]=B_0+E[I,J]. `

Using (4.1) and Weyl's singular-value inequality,

` s_2(B) >= 7s/32-s/64 = 13s/64 =: sigma. `                    (4.5)

### 4.2 Ridge leverage stays below the q=1 threshold

Since `M_J` is positive definite and `Lambda` is invertible on the high spectral subspace,

` range(B_0)=range(U_I). `

The orthogonal projection onto this range has diagonal

` u_i^T M_I^(-1)u_i <= (1/32)/(7/32)=1/7. `                    (4.6)

Use the proved ridge perturbation inequality from the same ridge-window report:
if `B=B_0+F`, `||F||<=eta`, and `P_0` projects onto `range(B_0)`, then

` (K_gamma)_ii <= [sqrt((P_0)_ii)+eta/gamma]^2. `              (4.7)

Take

` gamma=sigma/sqrt(6)=13s/(64 sqrt(6)),   eta=s/64. `           (4.8)

Then

` (K_gamma)_ii <= (1/sqrt(7)+sqrt(6)/13)^2 <1/2. `            (4.9)

For a completely rational certification of the last strict inequality, use `sqrt(42)<13/2`, giving

`(1/sqrt(7)+sqrt(6)/13)^2 < 2/7+6/169=380/1183<1/2`.

The two singular values in (4.5) contribute at least `6/7` each to the ridge trace, hence

` theta >=12/7. `                                               (4.10)

Thus (3.1) is admissible with `q=1`.

### 4.3 Convert the ridge envelope to a half-Riesz bound

Put `beta=theta/2`, so `beta>=6/7`.  Rewrite (3.1) as

` |phi_R(t)| <= min(1,(T/|t|)^beta), `                          (4.11)

where

` T=[L_1/(2gamma)] D^(-1/(2theta)). `                           (4.12)

The elementary inequality `log(1+x)>=x/(1+x)` implies `log D>=theta`, so

` T <= L_1/(2 gamma sqrt(e)) = pi sqrt(2e)/(2gamma). `          (4.13)

Now use the positive Gaussian representation of the Riesz kernel.  For every real `x!=0`,

` |x|^(-1/2)=Gamma(1/4)^(-1) integral_0^infinity r^(-3/4) exp(-r x^2) dr. `

Fourier inversion for the Gaussian, Tonelli, and absolute values give

` E|R-u|^(-1/2)`
` <= (1/sqrt(2pi)) integral_R |t|^(-1/2)|phi_R(t)| dt`
` = sqrt(2/pi) integral_0^infinity t^(-1/2)|phi_R(t)| dt. `     (4.14)

The integral of the envelope (4.11) is exact:

` integral_0^infinity t^(-1/2) min(1,(T/t)^beta) dt`
` = sqrt(T) [2+1/(beta-1/2)]`
` <= (24/5) sqrt(T), `                                         (4.15)

because `beta>=6/7`.

Substitute (4.8), (4.13) into (4.14)–(4.15):

` sup_u E|R-u|^(-1/2)`
` <= [192/(5 sqrt(13))](12e)^(1/4) s^(-1/2). `                 (4.16)

This is exactly (1.2)–(1.3).  Notice that no bounded density of `R` was assumed or proved; the borderline two-direction characteristic-function envelope need not be in `L^1`, but it is integrable against the half-Riesz weight `|t|^(-1/2)`.

## 5. Proof of the scalar-pivot corollary

The rank-one completion associated with (1.4) is

` A_0=[[a,b^T],[b,bb^T/a]], `

which has rank one, and

` A-A_0=0 direct_sum S. `                                      (5.1)

The singular-value rank inequality gives

` s_3(A) <= s_2(S). `                                          (5.2)

Therefore the target hypothesis `s_3(A)>=s` implies the exact two-large-eigenvalue input required in Theorem A.

Complete the square in the ORIGINAL pivot coordinate:

` Q=a(X_i+a^(-1)b^T Z)^2 + R(Z), `                             (5.3)

where `R` has quadratic matrix `S` (and may contain an affine term if the original polynomial did).  Given `Z`, the shifted scalar in (5.3) is a translate of `X_i`, so its conditional density is still at most one.  The density of `aV^2` is bounded by

` |a|^(-1/2) |y|^(-1/2) `                                     (5.4)

on the appropriate half-line.  Averaging (5.4) over `Z` and applying Theorem A yields

` p_Q(t) <= |a|^(-1/2) E|t-R|^(-1/2)`
`         <= C_H / sqrt(|a|s). `                               (5.5)

Tonelli supplies absolute continuity.  This proves Corollary B.

The key point is that one target eigenvalue is spent on the physical pivot and the other **two** are paid by a fractional-potential estimate on the Schur residual.  A residual density theorem would normally demand a third residual direction, i.e. a fourth large eigenvalue of `A`; (4.14) removes exactly that mismatch in the diffuse-window branch.

## 6. Substantive application of the designated fleet04/B18 partner result

Completed partner result:

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its dependence-safe square-smoothing theorem says: if a residual `R` has density at most `M` and, conditional on `R=r`, the square variable has density at most one, then

` ||p_(R+aV^2)||_infinity <=2 sqrt(M/|a|), `                    (6.1)

without assuming independence of `V` and `R` after the square completion.

Apply this to the same physical pivot when the stronger condition `s_4(A)>=s` holds.  From (5.1),

` s_4(A) <= s_3(S). `                                          (6.2)

If the same spectral-window leverage condition holds for `S`, the completed three-large-eigenvalue ridge-window theorem gives

` M <= [288 sqrt(3e)/13]/s. `                                  (6.3)

Equation (6.1) therefore gives the actual inequality

` ||p_Q||_infinity`
` <= 2 sqrt( [288 sqrt(3e)/13] / (|a|s) )`
` < 15.908 / sqrt(|a|s). `                                     (6.4)

This is a substantive application of the partner theorem.  The new Theorem A is what lowers the residual requirement from three large eigenvalues to two and hence matches `s_3(A)>=s` after one scalar pivot.

The newer fleet04/B18 disjoint-bank result at commit `ce50e74f705c49f66524aa6565d4aa4a9be88061` was also checked for compatibility.  It gives a continuous-density bound for a zero-pivot scalar plus two genuinely disjoint linear banks.  I do **not** use it to replace a general Schur residual: the required disjoint-bank factorization is a real hypothesis.

## 7. Exact full-rank target example

The branch is not an exact-rank artifact.  Take 64 residual coordinates.  Let `u` be the normalized all-ones vector on the first 32 coordinates and `v` the normalized all-ones vector on the last 32, and put

` P=uu^T+vv^T, `
` S=2uu^T-2vv^T+(1/128)(I-P). `                                (7.1)

The window `|lambda(S)|>=1/64` is exactly `span{u,v}`, and every physical leverage equals `1/32`.  Let

` a=2,   b=(1/100)u,   C=S+bb^T/a, `
` A=[[a,b^T],[b,C]]. `                                         (7.2)

The Schur complement is exactly (7.1).  On `span{e_0,u}` the matrix is

` [[2,1/100],[1/100,2+1/20000]], `

whose eigenvalues are approximately `2.01002503125` and `1.99002496875`; `v` remains an eigenvector with eigenvalue `-2`, and the other 62 eigenvalues equal `1/128`.  Thus this is full rank and has at least three eigenvalues of modulus strictly greater than one.

Corollary B gives, for **every** admissible independent cap-one input law,

` ||p_Q||_infinity <= C_H/sqrt(2) <17.998. `                    (7.3)

The numerical checker in this run verifies the constants and this spectrum; it is only a finite check of the displayed example, not a universal proof certificate.

## 8. Corrections and non-transfers honored

This argument does not use any of the currently refuted interfaces:

- no law-uniform pointwise van-der-Corput/Fresnel decay;
- no arbitrary-joint three-dimensional coarea bound;
- no positive moment of a density after conditioning on the full spectral complement;
- no claim that a good physical pair/triple is forced by three large eigenvalues;
- no independence after a spectral rotation;
- no worst conditional scalar-remainder density cap;
- no Monte Carlo evidence as proof.

The only rotation is deterministic spectral bookkeeping used to invoke MSS; all probabilistic decoupling is performed on ORIGINAL coordinate cuts in the already-proved ridge theorem.

## 9. What remains

Theorem A closes the **nonzero physical scalar pivot + diffuse two-eigenvalue Schur window** branch, including full-rank small tails.  It does not prove that every target matrix enters this branch.

The first unpaid full-target implication is now structural and sharply localized:

1. if some usable physical scalar pivot has a diffuse two-eigenvalue Schur window, Corollary B finishes it;
2. if a uniformly conditioned indefinite physical pair exists, the completed full-matrix pair theorem finishes it;
3. if the original three-large spectral window itself is diffuse, the completed ridge-window density theorem finishes it;
4. the remaining matrices must have concentrated/high-leverage spectral mass while simultaneously avoiding a useful scalar pivot/Schur-diffuse certificate and a useful physical pair.  They require the promised aggregate-before-inversion/grouped-coordinate mechanism, with the zero/near-isotropic pivot branch treated separately.

Full unrestricted QFORM therefore remains **OPEN / NOT PROVED**.  Continuity remains open for the full target and is not claimed for Corollary B.

## 10. Source pins

- MSS primary source: Annals of Mathematics 182 (2015), Corollary 1.5, `https://doi.org/10.4007/annals.2015.182.1.8`.
- Juškevičius–Lee primary source: arXiv:1503.09190, Theorem 1 and Corollary 1.
- Ridge/free-regularizer proof: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`, `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
- Regularized determinant ancestor: `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.
- fleet04/B18 square-smoothing partner: `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.
- fleet04/B18 zero-pivot two-bank partner: `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

Repository synchronization is not native learned-memory ingestion.  This run is `WITHOUT_VERIFIED_BRAIN`.
