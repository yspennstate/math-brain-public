SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T03:01:25Z.
attacking: scalar-pivot plus aggregate Schur-cross-volume gluing, with arbitrary rough product laws retained.

# account03/B13 r22 — aggregate cross-three-volume plus one original scalar upgrades L3 to Linfinity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED TARGET-RELEVANT SUPPORTING THEOREMS / FULL QFORM OPEN / FULL CONTINUITY OPEN**

## 1. Exact scope and source-safe dependencies

The owner target remains the full statement for every finite `n`, arbitrary independent real coordinates with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, log-concavity, diagonal-basis, or post-rotation-independence hypothesis is used below.


The following completed mathematics is actually used.

1. **Previous account03/B13 cross-three-volume L3 theorem.** `yspennstate/math-open-problems@77bd4ea475a11a505c6990630cbdfebdcce0fd8f`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T013555Z-account03-B13-qform-r21/REPORT.md`. For any disjoint ORIGINAL-coordinate cross block `M` of a quadratic-plus-affine form, with

   `Z3=e_3(M^T M)>0`,

   arbitrary same-side quadratic terms, outside couplings and signs are allowed and

   `||p||_3 < 6.787 Z3^(-1/9)`.                                      (1.1)

   The underlying proof works first on arbitrary unit-measure product indicators and then transfers to all cap-one product laws.

2. **Previous account03/B13 entropic-three-volume / six-hub theorem and account03/B06 one-row/E2 characteristic-function bound.** These are already assembled in the r21 source. For every `L>0`, a cross block with three-volume `Z3` is either paid in `Linfinity` by

   `||p||_infinity <= 6 sqrt(e) exp(L/6) Z3^(-1/6)`,                  (1.2)

   or some hub row has aggregate currency

   `kappa=r^2 E >= ((1-exp(-L))/6) Z3`,                              (1.3)

   and

   `|phi(t)| <= min{1,C0 kappa^(-1/8)|t|^(-3/4)}`,

   `C0=2^(-1/2) pi^(3/4) e^(5/8)`.                                  (1.4)

3. **Designated partner account04/B13 no-attainment purification.** `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`. For every bounded measurable product kernel `K`, the supremum over arbitrary cap-one mass-one marginals equals the supremum over indicators of bounded finite unions of intervals of measure one. This is equality of suprema, not an attained bathtub maximizer; there is no uniform support diameter or fragment count.

The current volume-stability package `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, path `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`, is compatible context: it pays row-diffuse three-volume directly in `Linfinity`, while the theorem below is useful precisely because it makes no row-volume marginal assumption once one genuine original scalar square is available.

No refuted pointwise law-uniform quadratic-phase decay, arbitrary-joint coarea bound, positive conditional projection-density moment, fiber-sup estimate, bounded-diameter reduction, or universally good single minor is used.

## 2. A new three-quarter small-ball theorem for every positive cross three-volume

The r21 theorem gave an `L3` density, hence an `h^(2/3)` slab estimate. The same dichotomy in fact gives a stronger direct `h^(3/4)` estimate.

### Lemma 2.1 — Gaussian conversion of a `|t|^(-3/4)` envelope

Suppose a real random variable `Y` has characteristic function satisfying

`|phi_Y(t)| <= D |t|^(-3/4)` for every `t!=0`.

Then every interval `J` of length `h>0` satisfies

`P(Y in J) <= G D h^(3/4)`,                                         (2.1)

where

`G=e^(1/8) 2^(1/8) Gamma(1/8)/sqrt(2pi)
 =3.71405110123522...`.

**Proof.** If `c` is the midpoint of `J`, then on `J`,

`1_J(x) <= e^(1/8) exp(-(x-c)^2/(2h^2))`.

The Fourier transform of the Gaussian under the convention of the source reports is

`sqrt(2pi) h exp(-h^2 t^2/2)`.

Therefore

`P(Y in J)
 <= e^(1/8) h/sqrt(2pi)
    int_R |phi_Y(t)| exp(-h^2t^2/2) dt`

`<= e^(1/8) D h/sqrt(2pi)
    int_R |t|^(-3/4) exp(-h^2t^2/2) dt`.

The final integral is

`2^(1/8) Gamma(1/8) h^(-1/4)`,

which proves (2.1). QED.

### Theorem 2.2 — `QFORM-CROSS-3VOLUME-SLAB-THREEQUARTER-v1`

For every original-coordinate cross block `M` with

`Z3=e_3(M^T M)>0`,

every quadratic polynomial in independent cap-one original coordinates having this cross block obeys

`boxed: P(Q in J) < 14.486 Z3^(-1/8) |J|^(3/4)`                      (2.2)

for every interval `J`. All same-side quadratic terms, outside couplings, affine terms and signs are arbitrary.

**Proof.** Apply the r20/r21 dichotomy with a free parameter `L>0`.

In the paid branch, (1.2) and `min(1,x)<=x^(3/4)` give

`P(Q in J)
 <= (6 sqrt(e))^(3/4) exp(L/8) Z3^(-1/8)|J|^(3/4)`.                 (2.3)

In the hub branch, (1.3), (1.4), and Lemma 2.1 give

`P(Q in J)
 <= B [6/(1-exp(-L))]^(1/8)
       Z3^(-1/8)|J|^(3/4)`,                                        (2.4)

where

`B=G C0=11.577887698221343...`.

Equalizing the constants in (2.3) and (2.4) gives

`R=6 B^8/(6sqrt(e))^6=2067.259347023794...`,

`L_*=log(1+R)=7.634462637351169...`,

and the common value

`14.485199899718856... <14.486`.

This proves (2.2). QED.

This theorem is still not a density-cap theorem: exponent `3/4` is sublinear. Its role below is diagnostic; the decisive closure comes from combining the stronger r21 `L3` statement with a genuine original-coordinate scalar square.

## 3. New half-Riesz interpolation from `L3` density to a bounded square-smoothed density

### Lemma 3.1 — `QFORM-L3-HALF-RIESZ-v1`

Let `R` be a real random variable with probability density `p_R in L3(R)` and

`||p_R||_3 <= H`.

Then

`boxed:
 sup_t E |t-R|^(-1/2)
 <= C_R H^(3/4),
 C_R=4 sqrt(pi/(2 sqrt(3)))
    =3.809251227455829... .}`                                      (3.1)

**Proof.** Fix `lambda>0`. Pointwise,

`|u|^(-1/2)
 <= lambda + (|u|^(-1/2)-lambda)_+`.

Holder with exponents `3` and `3/2` gives

`int |u|^(-1/2) p_R(t-u) du
 <= lambda
   +H ||(|u|^(-1/2)-lambda)_+||_(3/2)`.                             (3.2)

A direct beta-integral computation gives

`int_R (|u|^(-1/2)-lambda)_+^(3/2) du
 = (3pi/2) lambda^(-1/2)`.                                         (3.3)

Indeed after `x=lambda sqrt(u)` the positive-half-line integral becomes a beta integral `B(1/2,5/2)`.

Thus (3.2) is

`<= lambda + H (3pi/2)^(2/3) lambda^(-1/3)`.

Optimizing at

`lambda=[H(3pi/2)^(2/3)/3]^(3/4)`

gives exactly

`4 sqrt(pi/(2sqrt(3))) H^(3/4)`.

The estimate is translation-uniform. QED.

This is the scale needed for a square kernel: under dilation of the residual quadratic form, `H` scales with exponent `-2/3`, and `H^(3/4)` therefore supplies one additional inverse square-root scale.

## 4. Main theorem: one original scalar pivot plus any positive Schur cross-three-volume gives Linfinity

Let `k` be an ORIGINAL coordinate and write the general quadratic-plus-affine polynomial as

`Q(x,z)=a x^2 +2x( c^T z + beta )
        + z^T Bz +2d^Tz + gamma`,                                  (4.1)

where `x=X_k`, `z=(X_i)_{i!=k}`, and `a=A_kk`.

Assume `a!=0`. Complete only this original scalar square:

`Q=a(x+ell(z)/a)^2+R(z)`,                                           (4.2)

with `ell(z)=c^Tz+beta` and

`R(z)=z^T S z +2d_*^Tz+gamma_*`,

`S=B-a^(-1)cc^T`.                                                   (4.3)

The variables in `z` remain mutually independent because no rotation or random-coordinate change has been made.

Choose disjoint ORIGINAL-coordinate subsets `I,J` among the residual coordinates and put

`M=S[I,J]`,

`Z3=e_3(M^T M)`.                                                     (4.4)

### Theorem 4.1 — `QFORM-SCALAR-SCHUR-CROSS3-LINF-v1`

If `a!=0` and `Z3>0`, then the law of `Q` has a density satisfying

`boxed:
 ||p_Q||_infinity
 <16.018 |a|^(-1/2) Z3^(-1/12)
 =16.018 (|a|^6 Z3)^(-1/12).}`                                     (4.5)

All other entries of the Schur complement, all outside couplings and all affine terms are arbitrary. The original coordinates may have arbitrary independent one-dimensional probability densities bounded by one, with arbitrary fragmented and unbounded supports.

In particular, if the chosen Schur cross block has `s_3(M)>=sigma>0`, then `Z3>=sigma^6` and

`boxed: ||p_Q||_infinity <16.018 (|a| sigma)^(-1/2).}`               (4.6)

**Proof for extreme products.** First let every marginal be an indicator of an arbitrary bounded finite union of intervals of total measure one. By r21 applied to the residual quadratic-affine polynomial `R(z)`,

`||p_R||_3 < 6.787 Z3^(-1/9)`.                                      (4.7)

Fix `z`. The shifted scalar `X_k+ell(z)/a` still has a density bounded by one. The elementary change of variables for a square gives, for either sign of `a`, the conditional density bound

`p_{Q|Z=z}(t)
 <= |a|^(-1/2)|t-R(z)|^(-1/2)`                                     (4.8)

for almost every `t`. The two square roots contribute at most the two cap-one values divided by the Jacobian, giving exactly the coefficient one in (4.8).

Average (4.8) over `z` and use Lemma 3.1:

`p_Q(t)
 <= |a|^(-1/2) E|t-R|^(-1/2)`
 <= C_R |a|^(-1/2)||p_R||_3^(3/4)`

`< C_R 6.787^(3/4)
   |a|^(-1/2) Z3^(-1/12)`.

The numerical constant is

`C_R 6.787^(3/4)=16.017620617959683...<16.018`,

proving (4.5) for every extreme product.

For (4.6), if `lambda_1>=lambda_2>=lambda_3` are the top three eigenvalues of `M^TM`, then

`Z3=e_3(M^TM)>=lambda_1 lambda_2 lambda_3>=sigma^6`.

**Actual application of the designated account04/B13 partner theorem.** For an interval `J0`, the just-proved extreme-product estimate gives

`|{x in product E_i : Q(x) in J0}|
 <16.018 |a|^(-1/2) Z3^(-1/12)|J0|`                                 (4.9)

for every tuple of bounded finite-union unit-measure sets `E_i`. Apply account04/B13 Corollary 2.2 to the bounded kernel

`K(x)=1_{Q(x) in J0}`.

Its exact no-attainment supremum identity transfers (4.9), with **zero constant loss**, to every admissible cap-one product law. Therefore

`P(Q in J0)
 <16.018 |a|^(-1/2) Z3^(-1/12)|J0|`                                (4.10)

for every interval. Lebesgue differentiation yields an absolutely continuous output law with the essential density bound (4.5). This completes the proof. QED.

The partner result is applied here to an actual new slab inequality; it is not merely cited as background. No optimizer, single interval, centered law, bounded support diameter, or bounded fragment count is introduced.

## 5. Why this theorem is not a duplicate of the direct cross-rank-three Fresnel exit

The completed account03/B18 cross-block theorem gives a very strong direct `Linfinity` estimate when the entire cross block can be paid by the product of **all nonzero singular values**. The current theorem pays instead the aggregate order-three currency

`Z3=e_3(M^TM)=sum_(|S|=|T|=3) det(M_ST)^2`.

Thus (4.5) remains meaningful when `M` has many additional arbitrarily tiny nonzero singular values: only its aggregate three-volume enters. The price is the presence of one genuine original scalar pivot outside the residual cross block. This complements, rather than replaces, the direct Fresnel theorem and the row-diffuse volume-stability theorem.

Homogeneity is exact. Under `A -> sA`, one has `a->sa`, `M->sM`, `Z3->s^6Z3`, and the right side of (4.5) scales as `|s|^-1`, exactly as an output density must.

There is also a bordered-minor identity useful for future structural work. For row and column triples `I,J` disjoint from `k`,

`det A[{k} union I,{k} union J]
 = a det S[I,J]`.                                                    (5.1)

Hence

`a^2 Z3
 = sum_(|I|=|J|=3) det A[{k} union I,{k} union J]^2`                (5.2)

for the selected residual cut. Equation (5.2) shows that the new currency is an aggregate family of original-coordinate bordered four-minors rather than a chosen reciprocal tiny minor. The remaining factor of `|a|` in (4.5) is genuine in the present square-smoothing proof and cannot simply be discarded in the no-pivot regime.

## 6. Relation to the full no-pivot target

The full conjecture is not solved here. The current synthesis reduces full QFORM to the fixed strict no-pivot problem N3, where every physical scalar pivot and every physical `2x2` principal determinant is small. Theorem 4.1 supplies a new exit from that class only when some nonzero scalar pivot `a` has a Schur complement with enough aggregate cross-three-volume to keep

`|a|^6 e_3(M^TM)`                                                     (6.1)

uniformly away from zero for some residual physical cut.

If every such currency is tiny, (4.5) alone gives no universal constant. That failure is a concrete structural condition, not a proof obstruction hidden inside an inverse individual minor.

The first unpaid B13 implication is therefore:

**`QFORM-N3-SCALAR-SCHUR-THREEVOLUME-OR-PAID-SKELETON-v1`.** In the strict no-pivot extreme-product class, prove that either

1. some original scalar pivot and residual physical cut have universal-scale currency (6.1), so Theorem 4.1 pays the branch; or
2. simultaneous failure of all such currencies forces one of the already completed row-diffuse volume-stability, exact-null-coloop, rank-two tube/grouped-bank, determinant-pair, mixed-hub/Fresnel, or finite-core mechanisms.

This implication must be proved at the matrix/product level; small Schur coefficients cannot be deleted as a random perturbation on arbitrary unbounded supports.

The exact-null scalar endpoint `a=0` is not covered by Theorem 4.1 and should not be re-proved here; the live fleet already has a separate exact-null-coloop kernel at its stated scope.

## 7. Regularity status

Theorem 4.1 proves **absolute continuity and an essentially bounded density**. It does **not** prove that this density has a continuous representative. Conditional square densities can inherit roughness from the arbitrary one-dimensional input density, and the no-attainment mixture transfer alone does not preserve continuity. Full continuity remains separately OPEN.

Theorem 2.2 is only a fractional small-ball estimate and by itself does not establish an `Linfinity` density.

## 8. Deterministic checks

The run checker `check_constants.py` and recorded `CHECK_OUTPUT.txt` verify the beta-integral arithmetic and constants:

- `C0=3.1173205167723097...`;
- Gaussian conversion `G=3.71405110123522...`;
- optimized three-quarter slab parameter `L_*=7.634462637351169...`;
- optimized small-ball constant `14.485199899718856...`;
- half-Riesz constant `C_R=3.809251227455829...`;
- final scalar-Schur density constant `16.017620617959683...`;
- `int_R (|u|^-1/2-1)_+^(3/2)du=3pi/2`.

The recorded output terminates `QFORM_B13_R22_CHECK_PASS`. These checks corroborate constants only; the proofs are Sections 2--4.

## 9. Status

New proved supporting results:

1. `QFORM-CROSS-3VOLUME-SLAB-THREEQUARTER-v1`, equation (2.2);
2. `QFORM-L3-HALF-RIESZ-v1`, equation (3.1);
3. `QFORM-SCALAR-SCHUR-CROSS3-LINF-v1`, equations (4.5)--(4.6), with zero-loss arbitrary-law transfer using the designated account04/B13 theorem.

Full QFORM: **OPEN / NOT PROVED**.  
Full continuous-density conclusion: **OPEN / NOT PROVED**.
