# fleet03/B11 — heavy null-pivot independence compiler for indefinite rank three

**Run:** `20260922T182528Z-fleet03-B11-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner-control revision:** `2026-09-22.11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and correction state

The full conjecture remains open: for independent real coordinates with densities bounded by one and symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal bound for the density of `X^T A X`, or give a genuine counterexample.

This note treats an exact-rank-three indefinite branch with a heavy physical row whose scalar quadratic pivot is exactly zero. It preserves the original-coordinate product structure. It does **not** use the refuted arbitrary-joint coarea bound, conditional projection moments, pointwise law-uniform van-der-Corput decay, diagonal-basis independence, or fiber-supremum closure.

The completed designated partner result applied here is fleet04/B11, canonical source

`yspennstate/math-open-problems@44e7ab6750fbc3dccd77f1dd9e8bdba0bba2f0f5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260922T161514Z-b11-cone-trace-r1/REPORT.md`.

That report proves the exact indefinite cone-trace formula and, in its genuinely separated null-heavy branch, records the quantitative product-provenance estimate with the two-dimensional projection cap `K<=e`. Its cone-tube example also proves why a bare bound on the three-dimensional projected density cannot close the argument.

## 2. A translation-stable hyperbolic-square lemma

### Lemma 2.1

Let `S` be independent of the pair `(V,W)`. Assume `S` has a density `f` with `||f||_infinity<=M`, and `(V,W)` has a joint density `h` with `||h||_infinity<=K`. Let `a,b` be nonzero real numbers and let `H:R->R` be arbitrary measurable. Then

`Y = 2 a S W + b V^2 + H(W)`

has an essentially bounded density satisfying

`||p_Y||_infinity <= 3*2^(2/3) (M K)^(2/3) |a|^(-2/3) |b|^(-1/3).`      (2.1)

In particular the estimate is completely uniform over the correlated translation `H(W)`.

### Proof

Since `(V,W)` is absolutely continuous, `P(W=0)=0`. Conditioning on `(V,W)`, the affine map in `S` gives for almost every `t`

`p_Y(t)=∫∫ h(v,w) [2|a w|]^{-1} f((t-bv^2-H(w))/(2aw)) dv dw.`      (2.2)

Fix `r>0` and split into `|w|>=r` and `|w|<r`.

For `|w|>=r`, use `f<=M` and `∫h=1`:

`I_large <= M/(2|a|r).`                                             (2.3)

For the small strip use `h<=K`. We need the elementary sharp rearrangement estimate

`sup_A ∫_R f(A +/- z^2) dz <= 2 sqrt(M).`                           (2.4)

Indeed, after `y=z^2`, the left side is `∫_0^infinity f(A +/- y)y^{-1/2}dy`; under `0<=f<=M`, `∫f=1`, the decreasing-kernel bathtub bound fills `[0,1/M]`, giving `M∫_0^(1/M)y^{-1/2}dy=2sqrt(M)`.

For fixed nonzero `w`, scaling `z=sqrt(|b|/(2|aw|))v` in (2.4) yields

`∫ f((A-bv^2)/(2aw))dv <= 2 sqrt(M) sqrt(2|aw|/|b|).`              (2.5)

Therefore

`I_small <= [sqrt(2)K sqrt(M)/sqrt(|ab|)] ∫_{|w|<r}|w|^{-1/2}dw`

`          = 4 sqrt(2) K sqrt(M) sqrt(r)/sqrt(|ab|).`               (2.6)

Thus

`p_Y(t) <= A/r + B sqrt(r)`,

with `A=M/(2|a|)` and `B=4sqrt(2)Ksqrt(M)/sqrt(|ab|)`. The optimizer is `r=(2A/B)^(2/3)`, and exact substitution gives

`min_r [A/r+Bsqrt(r)] = 3*2^(2/3)(MK)^(2/3)|a|^(-2/3)|b|^(-1/3)`.

This is (2.1). No regularity of `H` is used. QED.

## 3. Exact heavy null-pivot normal form

Let the exact-rank-three form be

`A = R M R^T`, `R^T R=I_3`,

where `M` is real symmetric and every eigenvalue of `M` has modulus at least `s>0`. Choose a physical row `r_i^T` of `R` with leverage

`h=||r_i||_2^2 > 1/2`

and assume the scalar physical pivot vanishes:

`A_ii = r_i^T M r_i = 0.`                                         (3.1)

Set `e1=r_i/sqrt(h)`. Since the least singular value of `M` is at least `s`,

`kappa:=||M e1||_2 >= s`.

Equation (3.1) says `e1^T M e1=0`, hence `M e1` is orthogonal to `e1`. Put `e2=M e1/kappa` and complete to an orthonormal spectral basis `(e1,e2,e3)`. In this basis

`M = [[0,kappa,0],[kappa,d,e],[0,e,c]].`                            (3.2)

The determinant is exactly

`det M = -kappa^2 c`.                                               (3.3)

Consequently `c!=0`, and because `|det M|>=s^3`,

`kappa^2 |c| = |det M| >= s^3.`                                    (3.4)

This is the determinant-scale payment that is absent in the rank-two logarithmic control.

Write the corresponding spectral linear forms as `(T,W,V)`. The chosen physical row is `(sqrt(h),0,0)`, so

`T = sqrt(h) X_i + U`,

while `W,V` use only the coordinates other than `i`; their coefficient vectors are orthonormal. From (3.2),

`Q = 2 kappa T W + d W^2 + 2e W V + c V^2.`                        (3.5)

Apply the determinant-one shear

`V' = V + (e/c) W`.

Then

`Q = 2 kappa T W + c(V')^2 + H(W)`,

`H(W)=(d-e^2/c)W^2.`                                                (3.6)

The shear has Jacobian one, so every `L^infinity` cap for the joint density of `(W,V)` is inherited unchanged by `(W,V')`.

## 4. New theorem: the separated-leakage null branch is uniformly solved

### Theorem 4.1 — QFORM-HEAVY-NULL-SEPARATED-v1

In the setting of Section 3, assume in addition that the coefficient support of `U` is disjoint from the union of the coefficient supports of `W` and `V`. Then the quadratic form has an essentially bounded density and

`||p_Q||_infinity <= 6 e^(2/3) s^(-1) < 11.687/s.`                 (4.1)

Thus for the target scale `s>=1`,

`||p_Q||_infinity < 11.687.`                                        (4.2)

The same statement holds after negating the form, so it covers both signatures `(+,+,-)` and `(+,-,-)`.

### Proof

The support separation and independence of the original coordinates imply that

`T=sqrt(h)X_i+U`

is independent of `(W,V)`, hence of `(W,V')`. Conditioning on `U` shows that `T` is a mixture of translates of `sqrt(h)X_i`; therefore

`||p_T||_infinity <= h^(-1/2).`                                    (4.3)

No density or moment assumption on `U` is needed.

The completed fleet04/B11 null-heavy argument uses the genuine product-projection theorem for an orthonormal physical pair, giving

`||p_(W,V)||_infinity <= e`.

Because the shear `(W,V)->(W,V')` has determinant one,

`||p_(W,V')||_infinity <= e`.                                      (4.4)

Apply Lemma 2.1 to (3.6) with

`S=T`, `a=kappa`, `b=c`, `M=h^(-1/2)`, `K=e`.

This gives

`||p_Q||_infinity <= 3*2^(2/3)e^(2/3)h^(-1/3) kappa^(-2/3)|c|^(-1/3)`

` = 3*2^(2/3)e^(2/3)h^(-1/3)|det M|^(-1/3)`                       (4.5)

by (3.3). Since `h>1/2`, `h^(-1/3)<2^(1/3)`, and `|det M|>=s^3`. Hence (4.1).

This explicitly applies the completed partner's product-projection/cone-trace interface to a larger actual branch: the physical row need not equal a spectral basis vector (`h` may be any number in `(1/2,1]`), and the arbitrary quadratic translation `H(W)` is paid without changing the constant's scale. QED.

## 5. What this proves about the third direction

For rank two, an opposite-sign saddle can retain a logarithmic density singularity. In the heavy null rank-three geometry, the third direction supplies `c(V')^2`, and the exact identity

`kappa^2|c|=|det M|>=s^3`

prevents both the hyperbolic coupling and the third curvature from being simultaneously weak. Lemma 2.1 then turns the `1/|W|` hyperbolic Jacobian into an integrable `|W|^{-1/2}` strip after averaging against the third square. The optimized large/small-`W` split is precisely the quantitative removal of the rank-two logarithm in this separated-leakage branch.

## 6. Remaining first implication

The theorem deliberately isolates the true unresolved local obstruction. Without support separation, `U`, `W`, and `V` are different orthogonal linear forms of the **same** independent coordinates. Then `T` is not independent of `(W,V')`; the current correction inbox gives explicit non-product triples showing that a bounded conditional scalar density is not a valid substitute for this independence.

Thus the next B11 implication is:

**QFORM-OVERLAP-COMPILER-v1.** For the exact normal form (3.6), retain the genuine orthogonal coefficient identity among `U,W,V` and prove a dimension-free analogue of Lemma 2.1 when the leakage form `U` overlaps the transverse pair. A valid proof must exploit original-coordinate product-linear provenance (for example through grouped-coordinate Brascamp--Lieb, a regularized determinant, or aggregate shear payment), not merely a conditional density cap.

Near-zero but nonzero physical pivots remain another bridge: the orientation-free rank-two half-Riesz theorem controls nonzero pivots with a factor that deteriorates as the pivot tends to zero, while Theorem 4.1 pays the exact-zero separated branch uniformly. A full proof must join these without a gap and must allow arbitrary additional spectrum.

## 7. Regularity and full-target status

The argument proves existence of an essentially bounded density in the stated branch. It does **not** prove continuity here. Continuity remains a separate target unless imported from a theorem whose hypotheses cover this exact `H(W)` extension.

The unrestricted three-large-eigenvalue conjecture remains **OPEN / NOT PROVED**. In particular this report does not claim that support separation is automatic, that a heavy null row must exist, or that exact rank three exhausts the full-rank problem.

## 8. Exact checks

Symbolic verification gives

`det [[0,kappa,0],[kappa,d,e],[0,e,c]] = -c kappa^2`.

The calculus optimizer in Lemma 2.1 simplifies exactly to the coefficient `3*2^(2/3)`, and `6 e^(2/3)=11.6864042463...`.

All statements above preserve arbitrary cap-one input laws and arbitrary support geometry; no Gaussian, log-concave, compact-support, connected-support, or moment hypothesis was introduced.
