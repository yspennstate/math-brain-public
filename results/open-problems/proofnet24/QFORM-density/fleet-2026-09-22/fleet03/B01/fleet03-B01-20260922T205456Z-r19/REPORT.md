SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-22T20:54:56Z.
attacking: aggregate exterior-mass averaged-frequency smoothing — turn the regularized determinant into a critical half-Riesz bound before single-row logarithms form.

# fleet03/B01 r19 — aggregate exterior-mass half-Riesz smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Oscillatory replacement` / FOURIER  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING THEOREM / TARGET-LEVEL SUBBRANCH CLOSED / FULL QFORM OPEN**.


The full target remains: for every finite dimension, every independent real input vector with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one dimension- and law-independent bound on the density of `X^T A X`, or give a target-valid counterexample. Nothing below claims that full implication.

## 1. Source-pinned inputs and correction discipline

The principal analytic input is the completed regularized-determinant theorem at

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`,
`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

In the exact scope used here it says: for **any** symmetric quadratic form `R(Y)=Y^T S Y+ell^T Y+c`, independent cap-one original coordinates `Y`, any disjoint original-coordinate sets `I,J`, and physical cross block `B=S[I,J]`,

`|phi_R(t)| <= det(I + (4 t^2/(pi^2 e^2)) B B^T)^(-1/8).`        (1.1)

There are no restrictions on the two self blocks, signs, outside couplings, extra spectrum, moments, support, or log-concavity. The proof works in the original product coordinates and does not declare rotated eigen-coordinates independent.

The designated partner result actually applied below is fleet04/B01's signed-Fejer theorem at

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

For a probability law `mu`, it defines

`D_T mu(y)=(1/(2 pi)) integral_{-T}^T (1-|t|/T) Re(e^{-ity} phi_mu(t)) dt`

and proves the exact equivalence

`||p_mu||_infinity = sup_{T>0,y} D_T mu(y)`                         (1.2)

whenever the right side is finite.

All live corrections are preserved. In particular, no law-uniform pointwise quadratic-phase decay is used; the phase-aligned fragmented-support counterexample remains valid. No arbitrary-joint coarea bound, positive conditional-fiber moment, post-rotation independence, fixed good minor, or absolute-Wiener claim is used.

## 2. Aggregate exterior mass gives a fractional Riesz bound

For a positive semidefinite matrix `G`, write `e_k(G)` for the `k`-th elementary symmetric polynomial of its eigenvalues. For a cross block `B`, set

`E_k(B)=e_k(B B^T)`.

Thus `E_k(B)` is the total squared `k x k` minor mass by Cauchy-Binet; it aggregates all physical minors before any inverse scale is paid.

### Theorem 2.1 — `QFORM-EXTERIOR-EK-FRACTIONAL-RIESZ-v1`

Let `R` be any quadratic-plus-affine form in independent cap-one original coordinates and let `B` be any physical cross block of its quadratic matrix between disjoint coordinate sets. Fix an integer `k>=1` with `E_k(B)>0`. For

`0 < alpha < min(1,k/4)`,                                            (2.1)

define

`H_alpha(R)=sup_s E |R-s|^(-alpha)`.

Then

`boxed: H_alpha(R) <= C_(alpha,k) E_k(B)^(-alpha/(2k)),`              (2.2)

where

`C_(alpha,k) = ((pi e/2)^alpha /(2k Gamma(alpha) cos(pi alpha/2)))`
`              * Beta(alpha/(2k), 1/8-alpha/(2k)).`                  (2.3)

This is uniform in the dimension, all input laws, all self blocks, all affine terms, all signs, and all extra spectrum.

#### Proof

Put

`c0 = 4/(pi^2 e^2)`.

The determinant expansion and positivity of every elementary symmetric coefficient give, for every real `t`,

`det(I+c0 t^2 B B^T)
 = sum_{j>=0} (c0 t^2)^j E_j(B)
 >= 1 + c0^k E_k(B) t^(2k).`                                      (2.4)

Combining (2.4) with the source-pinned regularized-determinant estimate (1.1),

`|phi_R(t)| <= (1 + q t^(2k))^(-1/8),`
`q = c0^k E_k(B).`                                                  (2.5)

For `0<alpha<1`, the one-dimensional Riesz kernel has the standard Fourier representation

`|x|^(-alpha)
 = [Gamma(alpha) cos(pi alpha/2)]^(-1)
   integral_0^infinity t^(alpha-1) cos(tx) dt`                      (2.6)

in the Abel/distributional sense. Because of (2.5), the Fourier-side integral is absolutely convergent whenever `alpha<k/4`: near zero its weight is `t^(alpha-1)`, and at infinity it is `O(t^(alpha-1-k/4))`. Abel regularization therefore permits expectation and the limiting Fourier integral to be interchanged, giving for every `s`

`E|R-s|^(-alpha)
 <= [Gamma(alpha) cos(pi alpha/2)]^(-1)
    integral_0^infinity t^(alpha-1)|phi_R(t)| dt.`                  (2.7)

Substitute (2.5). The beta integral, with `u=q t^(2k)`, is

`integral_0^infinity t^(alpha-1)(1+q t^(2k))^(-1/8) dt
 = (1/(2k)) q^(-alpha/(2k))
   Beta(alpha/(2k),1/8-alpha/(2k)).`                                (2.8)

Finally

`q^(-alpha/(2k))
 = c0^(-alpha/2) E_k(B)^(-alpha/(2k))
 = (pi e/2)^alpha E_k(B)^(-alpha/(2k)).`                            (2.9)

Equations (2.7)-(2.9) prove (2.2)-(2.3). QED.

### Why the threshold is mathematically relevant

The condition `alpha<k/4` is the exact integrability threshold delivered by the unconditional regularized-determinant exponent. For `k=2`, the critical half-Riesz exponent `alpha=1/2` is excluded and the beta factor diverges at the endpoint. This matches the familiar logarithmic rank-two obstruction and the explicit two-variable product example from the preceding B01 run. For `k=3`, however, `1/2<3/4`, so the half-Riesz endpoint is strictly inside the paid range.

## 3. Critical three-cross-direction half-Riesz theorem

Set `k=3`, `alpha=1/2` in Theorem 2.1. The constants simplify because `Gamma(1/2)=sqrt(pi)` and `cos(pi/4)=1/sqrt(2)`:

`boxed: H_(1/2)(R) <= C3 E_3(B)^(-1/12),`                           (3.1)

with

`C3 = (sqrt(e)/6) Beta(1/12,1/24)
    = 9.840655864922018... < 9.841.`                                (3.2)

Thus **three aggregate cross directions are enough for the exact half-Riesz potential needed by scalar-Schur smoothing**, even though the same unconditional determinant exponent does not make `phi_R` itself integrable with only three cross directions.

A direct interval consequence, useful when no scalar pivot is available, is: for every interval `I` of length `ell`,

`P(R in I) <= C3 E_3(B)^(-1/12) sqrt(ell/2).`                       (3.3)

Indeed if `I` is centered at `s`, then on `I`, `|R-s|^(-1/2)>=sqrt(2/ell)`.

## 4. Target-level scalar-Schur branch with arbitrary residual self curvature

### Corollary 4.1 — `QFORM-PIVOT-PLUS-E3-CROSS-DENSITY-v1`

Let `Q=X^T A X` satisfy the target input assumptions. Suppose an original coordinate `i` has nonzero physical pivot

`a=A_ii != 0`.

Write `Y=X_{-i}` and complete the square in that **original** coordinate:

`Q = a (X_i + a^(-1) A_{i,-i} Y)^2 + R(Y),`                         (4.1)

where the residual quadratic matrix is the exact Schur complement

`S=A[-i,-i] - a^(-1) A[-i,i] A[i,-i].`                              (4.2)

Assume there are disjoint residual original-coordinate sets `I,J` for which `B=S[I,J]` satisfies `E_3(B)>0`. Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <= C3 |a|^(-1/2) E_3(B)^(-1/12)
 < 9.841 |a|^(-1/2) E_3(B)^(-1/12).`                               (4.3)

#### Proof

Condition on `Y=y`. The translated variable `X_i+a^(-1)A_{i,-i}y` still has a one-dimensional density bounded by one. For either sign of `a`, the conditional density of the square term in (4.1) obeys

`p_{a(X_i+h)^2}(u) <= |a|^(-1/2)|u|^(-1/2)`                        (4.4)

on the appropriate half-line. Therefore, for every scalar `t`,

`p_Q(t)
 <= |a|^(-1/2) E |R(Y)-t|^(-1/2)
 <= |a|^(-1/2) H_(1/2)(R).`                                       (4.5)

Apply (3.1) to the Schur residual. The regularized-determinant theorem retains **all** residual self blocks and extra spectrum, so no curvature is discarded. This proves (4.3). QED.

The conclusion of Corollary 4.1 is essential boundedness. This argument by itself does not prove continuity of the density; continuity remains separate for this branch.

## 5. Designated partner applied to an actual inequality

Apply fleet04/B01's exact signed-Fejer equivalence (1.2) to (4.3). On the branch of Corollary 4.1,

`boxed: sup_{T>0,y} D_T law(Q)(y)
 <= C3 |a|^(-1/2) E_3(B)^(-1/12).`                                (5.1)

This is an actual averaged-frequency estimate at the target density scale. It uses signed Fejer averaging only after the aggregate three-direction smoothing has already removed the single-row logarithmic endpoint. It is therefore compatible with the phase-aligned fragmented-support counterexample and does not resurrect the false pointwise `|t|^(-1/2)` claim.

## 6. Five-direction aggregate density corollary

The same determinant calculation also improves the usual "five singular values" statement to total fifth exterior mass. If `E_5(B)>0`, then (2.5) with `k=5` is integrable, so Fourier inversion gives a **continuous** density vanishing at infinity and

`boxed: ||p_R||_infinity <= C5 E_5(B)^(-1/10),`                    (6.1)

where

`C5 = (e/20) Beta(1/10,1/40)
    = 6.770121056043999... < 6.771.`                                (6.2)

Unlike (4.3), continuity is proved in this five-direction branch because the characteristic function is absolutely integrable.

## 7. What this pays and what remains open

The preceding B01 run showed that a single zero-diagonal physical row gives only a logarithmic signed-Fejer / small-ball endpoint, and the exact product example proves that logarithm cannot be removed from the row hypotheses alone. The present theorem changes mechanism: it aggregates **three exterior cross directions before inversion**. At that level the half-Riesz integral is genuinely finite and the logarithm disappears.

This also complements the current colored-exterior work: aggregate `E_3` is now a directly usable analytic currency, not merely a structural certificate. No individual tiny `3x3` coordinate minor is selected or inverted.

However, the full conjecture is **not** closed. The bare assumption "A has at least three eigenvalues of modulus at least one" has not been proved to force a nonzero physical pivot whose Schur residual contains a cross block with dimension-free lower-bounded `E_3`. Current scalar-Schur synthesis often guarantees only second exterior/cross currency, and rank-one Schur updates can destroy a naive third-direction certificate. The exact next implication is therefore:

`QFORM-SCHUR-THIRD-DIRECTION-AGGREGATION-v1:`

> From the three-large-eigenvalue hypothesis, in every still-unpaid scalar-Schur state, either produce a product-preserving residual cross block with `|a|^6 E_3(B)` bounded below by a universal positive constant (the combination dictated by (4.3)), or descend to one of the already-paid ridge, grouped-square, rank-two-affine, zero-self, or transverse-curvature branches.

A weaker but still useful analytic target is to combine the already-guaranteed `E_2` residual currency with one additional smoothing direction **before** the critical `alpha=1/2` logarithm forms.

Full QFORM remains OPEN. Full continuity remains OPEN.
