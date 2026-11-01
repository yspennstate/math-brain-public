SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B14, 2026-09-22T18:35:37Z.
attacking: whether the owner-prioritized scalar spectral conditioning `sup_b ||p_{Q3|Q'=b}||_infinity` can be a universal localization interface; construct or rule out a translation/fragment obstruction.

# fleet03/B14 — scalar spectral conditioning is not a universal localization interface

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T183537Z-fleet03-B14-QFORM-r16`  
**Assignment:** translations and localization  
**Status:** `ESSENTIAL_STEP_APPLIED / REFUTED_INTERMEDIATE_INTERFACE / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and live correction state

The full conjecture remains open: for every dimension, every independent real input with marginal density at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal bound for the essential supremum of the density of `X^T A X`, or produce a genuine target counterexample. Continuity is a separate desired conclusion and is not proved here.

The live research state already invalidates the arbitrary-joint rank-three coarea `||rho||_infinity^(2/3)` lemma and the positive conditional projection-density moment route. This report does not use either. It instead tests the newer owner-message proposal to split into a three-eigendirection core `Q3` and scalar remainder `Q'`, and to seek a universal bound on

`M = sup_b ||p_(Q3 | Q'=b)||_infinity`.

The identity obtained by conditioning on `Q'` is valid whenever the relevant conditional densities exist, and a finite `M` would indeed imply a bound for the full output. The theorem below shows that **no universal `M` exists**, even in dimension four, even with four eigenvalues bounded away from zero, even for one-interval input densities, and even though the complete output density is uniformly bounded by an elementary physical definite-pair argument.

## 2. The explicit target-valid family

Fix `0<delta<=1/64`. Let the four independent variables have densities

`X1 ~ Unif[2,3]`,

`X4 ~ Unif[1-delta, 2-delta]`,

`X2,X3 ~ Unif[-1/2,1/2]`.

All four densities are exactly one on an interval of length one.

Define the orthogonal spectral coordinates

`Y1=(X1+X4)/sqrt(2)`, `Y4=(X1-X4)/sqrt(2)`, `Y2=X2`, `Y3=X3`,

and take distinct eigenvalues

`lambda1=1`, `lambda2=2`, `lambda3=-2`, `lambda4=3`.

Thus

`Q = Q3 + Q'`,

`Q3 = Y1^2 + 2 X2^2 - 2 X3^2`,

`Q' = 3 Y4^2`.

In the original independent coordinates the matrix is

`A = [[2,0,0,-1],
      [0,2,0,0],
      [0,0,-2,0],
      [-1,0,0,2]]`.

Its eigenvalues are exactly `{1,2,-2,3}`. Hence this is an exact instance of the owner's full target, with no repeated-eigenvalue ambiguity.

## 3. The full output is uniformly harmless

The physical `(X1,X4)` block is

`B=[[2,-1],[-1,2]]`,

which is positive definite and has determinant `3`. For two independent cap-one variables, completing affine terms and applying the elementary elliptical-annulus area estimate gives

`||p_( [X1,X4] B [X1,X4]^T )||_infinity <= pi/sqrt(3)`.

The remaining random variable `2X2^2-2X3^2` is independent of that physical pair. Convolution with an arbitrary probability law cannot increase an `L^infinity` density norm, so

`boxed( ||p_Q||_infinity <= pi/sqrt(3). )`                                      (3.1)

Thus the construction below is **not** a counterexample to QFORM. It is a counterexample only to the proposed scalar-conditioning proof interface.

## 4. Conditioning on one scalar spectral remainder concentrates the core

Set

`b0=6`.

Then `Q'=b0` corresponds to `Y4=+sqrt(2)` or `Y4=-sqrt(2)`. Because the change `(X1,X4)<->(Y1,Y4)` is orthogonal, the joint density of `(Y1,Y4)` is just the indicator of the rotated rectangle.

At `Y4=+sqrt(2)`, write `X4=t`; then `X1=t+2`. The support restrictions give

`t in [1-delta,1]`.

Hence the allowed `Y1` interval is exactly

`J_delta=[sqrt(2)(2-delta), 2sqrt(2)]`,

of length `sqrt(2) delta`.

At `Y4=-sqrt(2)` the two support conditions are disjoint, so the negative branch contributes zero. In particular the density of `Q'` at `6` is positive:

`p_(Q')(6)=p_(Y4)(sqrt(2))/(6sqrt(2))=(sqrt(2)delta)/(6sqrt(2))=delta/6`.

Therefore the regular conditional law at this ordinary positive-density value is unambiguous (up to the usual a.e. version convention), and

`Y1 | {Q'=6} ~ Unif(J_delta)`.

Let

`Z=Y1^2 | {Q'=6}`.

Its support is

`[2(2-delta)^2, 8]`,

whose length is

`L_delta=8delta-2delta^2`.

Since the conditional density of `Y1` is `1/(sqrt(2)delta)` and `Y1<=2sqrt(2)`, the change of variables `z=y^2` gives throughout this interval

`boxed( p_Z(z) >= 1/(8 delta). )`                                            (4.1)

## 5. Exact logarithmic lower bound from the opposite-sign pair

Let

`D0=X2^2-X3^2`,  `D=2D0`.

For `X2,X3` uniform on `[-1/2,1/2]`, use

`u=X2-X3`, `v=X2+X3`.

The Jacobian is `1/2`, the image is the diamond `|u|+|v|<=1`, and `D0=uv`. For `0<r<=1/8`, restrict the density integral to the first-quadrant segment

`2r <= u <= 1/2`,  `v=r/u`.

On this segment `u+v<=1`, so it lies inside the diamond. The delta-function change of variables therefore gives the rigorous lower bound

`p_(D0)(r) >= (1/2) int_(2r)^(1/2) du/u
            = (1/2) log(1/(4r)).`                                          (5.1)

Scaling by two yields, for `0<s<=1/4`,

`boxed( p_D(s) >= (1/4) log(1/(2s)). )`                                     (5.2)

The pair `(X2,X3)` is independent of `(X1,X4)`, hence `D` remains independent of `Z` after conditioning on `Q'=6`.

## 6. Conditional core density diverges along the admissible family

At the point `8`, convolution and (4.1)-(5.2) give, because `delta<=1/64` implies `L_delta<1/4`,

`p_(Q3 | Q'=6)(8)`

` = int p_Z(z) p_D(8-z) dz`

` >= (1/(8delta)) int_0^(L_delta) (1/4) log(1/(2s)) ds`

` = [L_delta/(32delta)] [ log(1/(2L_delta)) + 1 ]`

` = [(4-delta)/16] [ log(1/(4delta(4-delta))) + 1 ].`                       (6.1)

As `delta -> 0`, the right side is

`(1/4) log(1/delta) + O(1) -> infinity`.

Consequently

`boxed( sup_{admissible laws,A} sup_b ||p_(Q3 | Q'=b)||_infinity = infinity )`  (6.2)

for the proposed scalar spectral split, even with `n=4`, four distinct eigenvalues `{1,2,-2,3}`, and one compact interval for every marginal.

This is stronger than a null-fiber pathology: the conditioning point has `p_(Q')(6)=delta/6>0`, and the displayed lower bound is on a genuine conditional density.

## 7. Translation/localization interpretation and completed partner result applied

Completed partner theorem actually consumed:

`fleet04/B14, QFORM-CENTERED-AFFINE-LOCALIZATION-EQUIVALENCE-v1`, read at
`yspennstate/math-open-problems@e61d28e5a00ca3681f19b8b39a21f9354e2f7a80`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260922T182134Z-fleet04-B14-centered-affine-r3/REPORT.md`.

It proves that the sharp homogeneous target constant is unchanged after passing to compact mean-zero cap-one product inputs while retaining the range-compatible affine term generated by physical coordinate translations, and likewise unchanged on centered compact finite-fragment unit-set inputs.

Apply it here to the concrete bound (3.1). Let `m=E X` and `W=X-m`. Then

`X^TAX = W^TAW + 2(Am)^T W + m^TAm`,

with `Am in Range(A)` (indeed `A` is invertible). The partner theorem therefore transfers the actual inequality with **zero translation tax**:

`boxed( P{W^TAW+2(Am)^TW+m^TAm in I} <= (pi/sqrt(3)) |I| )`                (7.1)

for every interval `I`.

The random variables `Q3` and `Q'` themselves have not changed; they have merely been rewritten as affine quadratics in the centered coordinates. Hence the lower bound (6.1) survives this centering exactly. The scalar-conditioning failure is therefore not caused by uncentered supports, distant tails, moments, or a missing compact localization. It persists inside the partner's canonical centered-affine compact class.

## 8. What is refuted and what replaces it

### Refuted intermediate interface

`QFORM-SCALAR-SPECTRAL-CONDITIONAL-SUP-UNIVERSAL-v1`:

> A universal proof may bound the full output by choosing three large spectral directions, writing `Q=Q3+Q'`, and proving a law- and dimension-uniform bound on `sup_b ||p_(Q3|Q'=b)||_infinity`.

Equation (6.2) disproves that universal intermediate claim. It does **not** disprove the identity obtained by conditioning, and it does **not** disprove QFORM.

### Replacement obligation

Any scalar-conditioning route must average in `b` before taking a worst conditional `L^infinity`, or retain additional product-provenance information preventing the translated-rectangle overlap mechanism above. A valid replacement could be an integrated inequality of the schematic form

`p_Q(t)=int p_(Q')(b) p_(Q3|Q'=b)(t-b) db <= C`,

proved directly with the weight `p_(Q')(b)` still present. In the example above, the bad fiber has weight `p_(Q')(6)=delta/6`, while its conditional peak grows only logarithmically like `log(1/delta)`; their product vanishes. This quantitatively explains why taking `sup_b` destroys the averaging that keeps the full law bounded.

The target-relevant next mechanism is therefore **mass-weighted scalar conditioning / aggregate-before-supremum**, not a uniform conditional density cap.

## 9. Status

- `QFORM-SCALAR-SPECTRAL-CONDITIONAL-SUP-UNIVERSAL-v1`: **REFUTED as a universal proof interface** by the explicit target-valid family above.
- Full output of the same family: **uniformly bounded**, equation (3.1).
- fleet04/B14 centered-affine localization: **applied to the actual inequality** (7.1).
- Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuous-density conclusion for the full target: **OPEN**.
- Native brain receiver use: absent; `WITHOUT_VERIFIED_BRAIN` retained.
