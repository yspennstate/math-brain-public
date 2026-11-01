# B03 QFORM r18 — isotropic cross-bank half-Riesz estimate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet03/B03`  
Run: `20260922T190034Z-fleet03-B03-QFORM-r18`  
Execution status: `WITHOUT_VERIFIED_BRAIN`  
Full target status: **OPEN / NOT PROVED**.  
Continuity: **not proved** by the new theorem below.

## 1. Target and mechanism change

The full owner target is a universal essential-density bound for `Q=X^T A X` when the original coordinates are independent, each input density is at most one, and `A` has at least three eigenvalues of absolute value at least one. No rotation of the input coordinates is allowed to create fictitious independence.

The preceding B03 run proved a fractional-collision closure when, after one physical square pivot, the residual has an original-coordinate cross bank with at least three singular values bounded below. Its determinant envelope reaches a logarithmic endpoint when only two effective cross directions remain. This run changes mechanism: instead of taking absolute values of the residual characteristic function, it integrates the product law directly on an **isotropic original-coordinate bank** and obtains a uniform half-Riesz potential. This gives a signed critical-time estimate and linear small-ball scaling even for rank-one or rank-two cross banks.

The theorem does **not** assume the invalid conditional-cap statement for sum/difference variables, does not use law-uniform pointwise quadratic-phase decay, and does not rotate the independent coordinates.

## 2. Product-projection input used

I use the completed worker result `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` from fleet02/B06:

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,  
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

Its needed consequence is: if `V` is an `m x k` matrix with orthonormal columns and `Y=V^T X` for independent cap-one coordinates, then

`||p_Y||_infinity <= exp(k/2)`.

For `k=1`, scaling gives the scalar projection bound

`||p_(a^T X)||_infinity <= exp(1/2)/||a||_2`, `a != 0`.                       (2.1)

For `k=r`, an orthonormal `r`-dimensional projection has density cap `exp(r/2)`. This is a weighted physical-fiber integral, not the refuted unrestricted fiber supremum.

## 3. Two bathtub estimates

### Lemma 3.1 — one-dimensional half-Riesz bathtub

If a real probability density `g` satisfies `0<=g<=K`, then uniformly in `s`,

`int |x-s|^(-1/2) g(x) dx <= 2 sqrt(2K)`.                                   (3.1)

Proof. The kernel is symmetric decreasing around `s`. The cap-one rearrangement/bathtub extremizer is `g=K` on the centered interval of length `1/K`. Therefore

`K int_{-1/(2K)}^{1/(2K)} |x|^(-1/2) dx = 2 sqrt(2K)`.

### Lemma 3.2 — r-dimensional radial half-Riesz bathtub

Let `Z` have a probability density on `R^r` bounded by `K`, and let `v_r=pi^(r/2)/Gamma(r/2+1)` be the unit-ball volume. Then for every `z0`,

`E ||Z-z0||_2^(-1/2) <= [2r/(2r-1)] (K v_r)^(1/(2r)).`                     (3.2)

Proof. The radial decreasing rearrangement is `K 1_{B(0,R)}` with `K v_r R^r=1`. Thus

`K r v_r int_0^R rho^(r-3/2) d rho`
`= [r/(r-1/2)] K v_r R^(r-1/2)`
`= [2r/(2r-1)] (K v_r)^(1/(2r))`.

Both inequalities remain valid for arbitrary fragmented source densities because they are applied only after legitimate linear projection bounds.

## 4. Main theorem — isotropic cross-bank half-Riesz estimate

### Theorem 4.1 — `QFORM-ISOTROPIC-CROSSBANK-HALF-RIESZ-v1`

Partition original independent coordinates into three disjoint blocks `(U,V,W)`. Each scalar coordinate has a probability density bounded by one. Let `T` be a fixed real `p x q` matrix of rank `r>=1`, with positive singular values `sigma_1,...,sigma_r`, and define

`Delta_r = product_{j=1}^r sigma_j`.

Let `b(W)` be any measurable `R^p`-valued function and `c(V,W)` any measurable real-valued function. Define

`R = 2 U^T T V + b(W)^T U + c(V,W)`.                                      (4.1)

Then for every `s in R`,

`E |R-s|^(-1/2) <= C_r Delta_r^(-1/(2r)),`                                 (4.2)

where

`C_r = [4r/(2r-1)] sqrt(e) v_r^(1/(2r)).`                                  (4.3)

In particular,

`C_1 = 4 sqrt(2e) = 9.326575926388497...`,

`C_2 = (8/3) sqrt(e) pi^(1/4) = 5.853335820621322...`.                       (4.4)

The theorem allows an arbitrary self-quadratic or other measurable contribution in `(V,W)` through `c`; the essential structural hypothesis is that the active `U` bank is **isotropic in the residual**, i.e. `U` enters only linearly after the other blocks are fixed.

### Proof

Condition first on `(V,W)=(v,w)`. The random variable in `U` is the scalar linear projection

`a(v,w)^T U + c(v,w)`,

with

`a(v,w)=2Tv+b(w)`.

If `a=0`, the pointwise conditional half-potential is infinite, so one cannot take a conditional supremum. Instead keep its exact dependence on `a`. By (2.1), whenever `a!=0` the conditional scalar density is bounded by `sqrt(e)/||a||`. Lemma 3.1 therefore gives

`E_U[ |R-s|^(-1/2) | V=v,W=w ]`
`<= 2 sqrt(2) e^(1/4) ||2Tv+b(w)||^(-1/2)`.                                (4.5)

The right side is interpreted as `+infinity` at a zero coefficient, but the next bank average is finite and hence shows that the zero set has no harmful contribution.

Take an SVD `T=L Sigma M^T`, where `L` and `M` have `r` orthonormal columns and `Sigma=diag(sigma_1,...,sigma_r)`. Orthogonal projection can only reduce Euclidean norm, so

`||2Tv+b(w)|| >= || 2 Sigma M^T v + L^T b(w) ||`.                          (4.6)

For fixed `w`, put `Z=M^T V`. By the cited weighted affine-fiber theorem,

`||p_Z||_infinity <= exp(r/2)`.                                             (4.7)

Hence

`Y_w = 2 Sigma Z + L^T b(w)`

has an `r`-dimensional density bounded by

`K_r = exp(r/2)/(2^r Delta_r)`.                                             (4.8)

Applying Lemma 3.2 at the origin gives

`E_V ||2TV+b(w)||^(-1/2)`
`<= [2r/(2r-1)] [v_r exp(r/2)/(2^r Delta_r)]^(1/(2r)).`                    (4.9)

This is uniform in `w`; average over `W`. Multiplying (4.9) by the factor in (4.5) and using

`exp(r/2)^(1/(2r))=e^(1/4)`, `2^(-r/(2r))=2^(-1/2)`,

cancels the `sqrt(2)` and yields exactly

`[4r/(2r-1)] sqrt(e) v_r^(1/(2r)) Delta_r^(-1/(2r))`.

This proves (4.2). In particular, the argument is valid at `r=1`: a rank-one hyperbolic bank has a logarithmically singular **density**, but its half-Riesz potential is nevertheless uniformly finite. That is precisely the critical smoothing needed after one independent square pivot. QED.

## 5. Signed critical-time form

Let `eta_R(t)=E exp(i t R)` and

`H_R(s)=E |R-s|^(-1/2)`.

Under the Fourier convention `hat f(t)=int exp(-itx)f(x)dx`, the tempered-distribution transform of `|x|^(-1/2)` is

`hat k(t)=sqrt(2 pi) |t|^(-1/2)`.

For `epsilon>0`, define the absolutely convergent signed integral

`I_epsilon(s) = (1/sqrt(2 pi)) int_R exp(-epsilon t^2) |t|^(-1/2)`
`                 Re( exp(-its) eta_R(t) ) dt`.                            (5.1)

Multiplication by `exp(-epsilon t^2)` in frequency is convolution by the normalized Gaussian

`g_epsilon(x)=(4 pi epsilon)^(-1/2) exp(-x^2/(4epsilon))`.

Therefore

`I_epsilon = g_epsilon * H_R`.                                              (5.2)

Theorem 4.1 implies the **signed integrated-time estimate**

`0 <= I_epsilon(s) <= C_r Delta_r^(-1/(2r))`                              (5.3)

for every `epsilon>0` and `s`. This is exactly the kind of integrated estimate that survives the live correction to pointwise oscillatory decay. No bound on the absolute integral

`int |t|^(-1/2) |eta_R(t)| dt`

is asserted; at low rank it can have endpoint divergence while the signed quantity (5.1) stays bounded.

## 6. Square-pivot transducer and linear small-ball scaling

### Corollary 6.1 — `QFORM-PIVOT-ISOTROPIC-BANK-DENSITY-v1`

Let `Z` be one additional original coordinate, independent of `(U,V,W)`, with density at most one. Suppose

`Q = a (Z+h(U,V,W))^2 + R`, `a!=0`,                                       (6.1)

where `R` has the form (4.1). Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= C_r |a|^(-1/2) Delta_r^(-1/(2r)).`                    (6.2)

Consequently, for every interval `I`,

`P(Q in I) <= C_r |a|^(-1/2) Delta_r^(-1/(2r)) |I|`.                       (6.3)

Proof. Conditional on `(U,V,W)`, the square pushforward satisfies

`p_{a(Z+h)^2}(y) <= |a|^(-1/2) |y|^(-1/2)`

on the appropriate half-line. Thus

`p_Q(y) <= |a|^(-1/2) E |y-R|^(-1/2)`,

and Theorem 4.1 gives (6.2). Mixture of the conditional square densities supplies absolute continuity. QED.

### Quadratic-form interpretation

Take a physical pivot coordinate `p` with `A_pp=a!=0` and form its Schur residual

`B=A_{-p,-p}-A_{-p,p}A_{p,-p}/a`.

If the remaining original coordinates admit disjoint blocks `(I,J,K)` such that

`B_{I,I}=0`

and the cross block `T=B_{I,J}` has rank `r>=1`, then conditioning on `X_K` puts the residual exactly into (4.1). Hence (6.2) applies with the singular-value product of `B_{I,J}`. All `J-J`, `J-K`, and `K-K` quadratic terms are absorbed into `c(V,W)`, while `I-K` terms become `b(W)^T U`.

For example, a unit pivot followed by a rank-one hyperbolic bank with singular value at least one has

`||p_Q||_infinity <= 4 sqrt(2e) < 9.327`.                                  (6.4)

This is a genuine all-dimensions, arbitrary-fragmented-law branch; it is not a Gaussian or finite-search statement.

## 7. Application of a completed other-worker result

The exact signed-Fejer interface from fleet04/B01,

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,  
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`,

states that for a law with density cap `M`, its Fejer averages satisfy `D_T mu(y)<=M` for every `T,y`, and conversely the supremum of these averages equals the essential density norm. Applying it to (6.2) gives the actual Fourier-side inequality

`D_T law(Q)(y) <= C_r |a|^(-1/2) Delta_r^(-1/(2r))`                        (7.1)

for every `T>0,y`. Thus the new direct half-Riesz proof supplies a dimension-free signed-time bound in a branch where the absolute endpoint integral is not the right object.

The designated assignment partner is `fleet04/B03`. At the startup scan there was no `handoffs/fleet04/B03` directory and no canonical current-QFORM artifact at the corresponding math-open-problems path, so no result from that exact slot was fabricated. The completed compatible fleet04/B01 theorem above and fleet02/B06 projection theorem were applied instead. This should be replaced by an actual fleet04/B03 dependency if one appears before a later run publishes a stronger synthesis.

## 8. Relation to live corrections and full-target debt

This theorem does not use any of the following refuted mechanisms:

- law-uniform pointwise van-der-Corput/Fresnel decay;
- independence of sum and difference variables after the independent-copy transform;
- a uniform conditional density cap after conditioning on a conjugate variable;
- a fixed finite-coordinate Tonelli/Holder/Plancherel closure;
- a universally well-conditioned physical principal minor.

It also respects the newer correction that an arbitrary 3D joint-density coarea bound of the claimed `||rho||_infinity^(2/3)` type is false: the proof uses the original product law through the weighted affine-fiber projection theorem and then integrates an exact scalar linear form.

The unrestricted owner conjecture remains open. The exact unpaid structural implication after this run is:

> Given only three eigenvalues of `A` with absolute value at least one, force either an already-completed diffuse/ridge/principal-block branch, or a physical pivot whose Schur residual contains a quantitatively large **isotropic** original-coordinate bank as above, or develop a replacement that tolerates a nonzero self block on the active bank.

The live counterexample to `single Schur rank-two extraction` means one cannot simply assert the first alternative. The next B03 mechanism should therefore attack the first non-isotropic extension: one low-rank self block plus a transverse bank, keeping product provenance before any conditional supremum.

## 9. Arithmetic checks

The constants from (4.3) are

- `C_1 = 9.326575926388497...`,
- `C_2 = 5.853335820621322...`,
- `C_3 = 5.023887637343903...`.

For the scalar test `U,V ~ Uniform[-1/2,1/2]`, `R=2UV`, the exact value at `s=0` is

`E|2UV|^(-1/2)=4 sqrt(2)=5.656854249... < C_1`,

consistent with the rank-one theorem. This is a check only, not a proof substitute.
