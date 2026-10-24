# account01/B12 — scalar-Qrest conditioning fails under one added eigenvalue; corrected mixed-norm interface

Run: `20260922T182048Z-account01-B12-QFORM-r15`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Additional eigenvalue control  
Status: `REFUTED_INTERMEDIATE_MECHANISM / PROVED_REPLACEMENT_IDENTITY / FULL_TARGET_OPEN`  
Execution memory label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source state and exact target

The full target remains OPEN: for every `n`, independent real `X_i` with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound on the essential supremum of the density of `X^T A X`, or give a genuine target counterexample.

Fresh control consumed before the mathematics: `yspennstate/math-research-brain@ced020f1463b04c309fa1e58559451b84f3c31b3`, OWNER CONTROL revision `2026-09-22.11`; refreshed before publication at a later main commit. The current owner message promotes the scalar-conditioning gate

`sup_b ||p_(Q3 | Qrest=b)||_infinity <= C`

as a high-value common target. The live correction set already refutes the arbitrary-joint coarea lemma and the positive conditional moment gate obtained by conditioning on the full spectral complement. The calculation below shows that the stronger scalar-conditioned `L^infinity` gate is also false, even after adding only one SMALL eigenvalue to an exact rank-three core.

This refutes a proof interface, not the QFORM conjecture.

## 2. Explicit target-class matrix

Let `X_1,...,X_4` be independent `Uniform[0,1]`; their densities are exactly one. Let

`O=(1/2) [[1,1,-1,-1], [1,-1,1,-1], [1,-1,-1,1], [1,1,1,1]]`.

Then `O` is orthogonal. Write `Y=OX`, so

`Y_4=(X_1+X_2+X_3+X_4)/2`.

Fix any `eta` with `0<eta<1`; for a concrete source-valid value one may take `eta=1/128`. Put

`A=O^T diag(1,1,1,eta) O = I_4-(1-eta) u u^T`,

where `u=(1,1,1,1)/2`. Thus `A` is genuinely non-diagonal for `eta!=1` and has spectrum

`{1,1,1,eta}`.

For `eta=1/128`, explicitly,

`A_ii=385/512`, `A_ij=-127/512` for `i!=j`.

The target hypothesis is satisfied by the three eigenvalues equal to one. Define

`Q3=Y_1^2+Y_2^2+Y_3^2`,
`B=Qrest=eta Y_4^2`,
`Q=Q3+B`.

The added spectral direction is rank one and SMALL. The point is that normalized conditioning on its scalar quadratic output can nevertheless be arbitrarily singular.

## 3. Exact conditional geometry near the cube vertex

Fix `y in (3/2,2)` and condition on `Y_4=y`. Set

`Z_i=1-X_i`,
`h=sum_i Z_i = 4-2y`.

Then `0<h<1`. On this event `Z_i>=0` and `sum Z_i=h`; because `h<1`, the upper constraints `Z_i<=1` are automatic. Since the product density of `X` is constant on the cube and the conditioning hyperplane is linear, the regular conditional law of `Z` is the uniform probability measure on the three-dimensional simplex

`Delta_h={z_i>=0: sum_i z_i=h}`.

Equivalently,

`Z=h W`,

where `W` is uniform on `Delta_1={w_i>=0: sum_i w_i=1}` (the Dirichlet(1,1,1,1) law).

For the first three Hadamard rows, the row sums are zero, hence

`Y_j=-(OZ)_j`, `j=1,2,3`,

while `(OZ)_4=h/2`. Orthogonality gives the exact identity

`Q3=sum_{j=1}^3 Y_j^2`
`   = ||Z||_2^2-h^2/4`
`   = h^2 T`,

where

`T=sum_{i=1}^4 W_i^2-1/4`.

On `Delta_1`, `T` has range exactly `[0,3/4]`: the minimum is at the barycenter `(1/4,...,1/4)` and the maximum at the vertices. The pushforward law of `T` is absolutely continuous. Indeed on the three-dimensional affine hyperplane `sum w_i=1`, the gradient of `sum w_i^2` vanishes only at the barycenter, a set of three-dimensional measure zero; the coarea theorem gives absolute continuity.

Therefore the conditional law of `Q3` given `Y_4=y` is an absolutely continuous probability law supported in an interval of length `3h^2/4`. Consequently every version of its conditional density satisfies, for almost every such `y`,

`||p_(Q3 | Y4=y)||_infinity >= 4/(3 h^2)`.          (3.1)

This lower bound uses only total mass one and support length; no estimate of the detailed density is needed.

## 4. Refutation of the scalar-Qrest uniform conditional cap

On the whole support of the inputs, `Y_4>=0`. Hence the map

`y -> b=eta y^2`

is one-to-one on the interval `y in (3/2,2)`. Conditioning on `B=b` is therefore the same as conditioning on

`Y_4=sqrt(b/eta)`.

For

`b in (9 eta/4, 4 eta)`

put

`h(b)=4-2 sqrt(b/eta)`.

By (3.1), for almost every such `b`,

`||p_(Q3 | B=b)||_infinity >= 4/[3 h(b)^2]`.       (4.1)

As `b` increases to `4 eta`, `h(b)` decreases to zero. Hence

`ess sup_b ||p_(Q3 | Qrest=b)||_infinity = infinity`.              (4.2)

The divergence occurs on positive-measure intervals approaching the edge, so it is not an artifact of changing a regular conditional distribution on a null set.

### Classification

`QFORM-SCALAR-QREST-UNIFORM-CONDITIONAL-CAP-FALSE-v1`.

The statement

`sup_b ||p_(Q3 | Qrest=b)||_infinity <= C`

cannot be a universal proof gate under the bare QFORM hypotheses. It already fails for four independent uniform coordinates and the non-diagonal target-class matrix with spectrum `{1,1,1,1/128}`.

This does NOT refute bounded density of `Q=Q3+Qrest`; it refutes only the normalized scalar-conditioning interface.

## 5. Why normalization is the problem: the correct exact mixed-norm identity

Let `B` be any real random variable and suppose `(Q3,B)` has a joint density. The convolution-along-the-diagonal identity is

`p_Q(t)=integral p_(Q3,B)(t-b,b) db`.

Therefore

`||p_Q||_infinity`
` <= integral ||p_(Q3,B)(.,b)||_infinity db`                       (5.1)
` = integral p_B(b) ||p_(Q3 | B=b)||_infinity db`,                 (5.2)

whenever conditional densities are used on the right. Thus the scale-correct replacement gate is the unnormalized mixed norm

`integral p_B(b) ||p_(Q3 | B=b)||_infinity db <= C`,              (5.3)

not the uniform normalized conditional cap.

The cube-vertex example explains the difference quantitatively. Let `H=sum_i Z_i`. For `0<h<1`, the Irwin-Hall density is

`p_H(h)=h^3/6`.                                                     (5.4)

The conditional density blow-up in (4.1) is of order `h^{-2}`, while the scalar level-set mass is of order `h^3`; their product has a spare factor `h` and is integrable.

One can make this explicit from above. The intrinsic three-volume of `Delta_1` is `1/3`, so `W` has density `3` with respect to three-dimensional Hausdorff measure in the hyperplane. Writing `V=W-(1/4,...,1/4)`, `T=||V||^2`. The coarea formula and the area bound by the full two-sphere give

`p_T(t) <= [3/(2 sqrt(t))] * 4 pi t`
`       = 6 pi sqrt(t)`
`       <= 3 pi sqrt(3)`.                                         (5.5)

Hence, for `0<h<1`,

`||p_(Q3 | H=h)||_infinity <= 3 pi sqrt(3)/h^2`,                   (5.6)

and so the UNNORMALIZED joint section satisfies

`||p_(Q3,H)(.,h)||_infinity`
` <= (h^3/6) * [3 pi sqrt(3)/h^2]`
` = (pi sqrt(3)/2) h`.                                            (5.7)

In particular the entire top-vertex edge contributes at most

`integral_0^1 ||p_(Q3,H)(.,h)||_infinity dh <= pi sqrt(3)/4`       (5.8)

to the corrected mixed norm. Thus the exact example that destroys the normalized `sup_b` gate is benign for the weighted/unnormalized interface.

This is the useful replacement for future scalar-conditioning attempts: retain the level-set mass before taking an `L^infinity` norm.

## 6. Designated partner result actually applied

I consumed the complete account02/B12 theorem

`QFORM-REDUNDANT-MIXED-PACKET-SPIKE-STABILITY-v1`,

canonical proof

`yspennstate/math-open-problems@262393f45fe00095aa7d64d7ebf894c26279715a:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T175624Z-account02-B12-QFORM-r11/REPORT.md`.

Its exact rank-one specialization is the following actual added-eigenvalue inequality. If disjoint ORIGINAL-coordinate sets `I0,J0` of size four satisfy

`s_4(A0[I0,J0]) >= sigma >0`,

and

`A=A0+R+S`,

where `rank R<=1` has arbitrary sign and magnitude and `||S||op<=delta<sigma`, then

`||p_(X^T A X)||_infinity`
` <= 3*4^(1/3)/(sigma-delta)`                                     (6.1)
` = 4.7622031559.../(sigma-delta),`

and the density is continuous. In particular, with `delta=0`, ONE arbitrary added eigenvalue is completely absorbed at cost

`4.7622031559.../sigma`.                                           (6.2)

This theorem is source-valid because it spends the rank perturbation on a redundant physical cross packet before selecting a final determinant. It shows that an added eigenvalue is not intrinsically problematic; what fails in Sections 3-4 is specifically the normalized scalar-conditioning replacement when no such redundant packet is available.

## 7. Exact old/new missing implication

Old proposed common gate (now refuted):

`sup_b ||p_(Q3 | Qrest=b)||_infinity <= C`.

New source-valid gate sufficient for the same diagonal-mixing identity:

`integral ||p_(Q3,Qrest)(.,b)||_infinity db`
` = integral p_(Qrest)(b) ||p_(Q3 | Qrest=b)||_infinity db <= C`.  (7.1)

The first universal missing implication is therefore to prove (7.1), or an equivalent unnormalized level-set estimate, directly from the original-coordinate product source and the three-large-eigenvalue geometry. It must aggregate the product level-set mass BEFORE normalizing a rare scalar slice. The existing ridge/grouped-coordinate and mixed-packet branches remain valid scoped endpoints.

## 8. Target status and regularity

Full QFORM status: OPEN.

This report proves a correction to a proof route and an exact replacement identity; it is not a target-level counterexample. The explicit matrix itself is target-class and its output is expected to have a bounded density. No claim about a universal continuous density follows from the new correction. The partner mixed-packet branch (6.1) does prove continuity in its stated scope.

No Gaussianity, log-concavity, moment, support-connectedness, post-rotation independence, pointwise van-der-Corput decay, unrestricted joint coarea bound, or full spectral-complement conditional cap is used.
