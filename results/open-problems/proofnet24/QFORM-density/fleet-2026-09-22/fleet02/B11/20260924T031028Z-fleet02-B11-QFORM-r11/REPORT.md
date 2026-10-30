SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-24T03:10:28Z.
attacking: the nonzero-pivot / mixed-volume indefinite collar; distinguish a real two-sheet analytic obstruction from a proof-norm obstruction, while retaining the rank-two logarithm and spending the third direction before dependence is collapsed.

# fleet02/B11 r11 — the sharp mixed-frame opposite-sign TT* barrier is already paid by an original-product zero-pivot trace

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW CROSS-SOURCE CLOSURE / PROOF-MECHANISM LOCALIZATION / FULL QFORM OPEN**.
Regularity: the main result below proves absolute continuity and an essential density bound. Continuity is not claimed from this argument. Full-target continuity remains separate.

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. No moment, support, log-concavity, iid, diagonal-basis, Gaussian, post-rotation independence, arbitrary-joint coarea, worst conditional projection cap, or perturbative deletion hypothesis is introduced.

## 1. First unpaid implication after fresh control and partner refresh

The inherited zero-pivot near-coloop same-bank puncture is no longer the first B11 debt. A fresh fleet01/B11 source match applies the completed fresh-hub divisible-twist theorem to the Witt normal form and proves, with physical hub leverage `q_h`,

`||p_Q||_(infinity,ess)
 <= 3*2^(4/3) [q_h |mu_1 mu_2 mu_3|]^(-1/3).`                    (1.1)

Thus in the live near-coloop range `q_h>=63/64`, the exact zero-pivot same-bank puncture is paid by `<7.60/s`. This uses the untouched original physical hub before any rotated dependence is collapsed.

The newest compatible designated partner fleet03/B11 r48 supplies a different warning. Its nonlinear residual construction shows that finite `L^3` control of a hyperbolic part and finite `L^(3/2)` control of a same-source square do **not** combine into `L^infinity` from marginal/joint density caps alone. The apparent third square can be hidden in a same-source nonlinear cancellation, leaving the rank-two logarithm. That construction is not a QFORM counterexample because its residual triple is not supplied as an orthogonal linear projection of independent original sources.

Accordingly the first exact-rank-three B11 debt is now the **nonzero physical-pivot double-aligned / ultra-coloop collar**, in the same scope as

`QFORM-PUNCTURED-ULTRACOLOOP-PRODUCT-RECEIVER-v2`,                (1.2)

with arbitrary additional nonseparable spectrum still a separate full-target bridge.

Before attacking (1.2), there is an important route correction. A fresh fleet03/B16 r39 report constructs a strict target-valid mixed-volume family for which the old absolute two-bank TT* kernel is infinite and uses it to motivate a phase-aware mixed-volume descent. The calculation below shows that this specific family is nevertheless uniformly paid by an original-coordinate zero-pivot trace with constant `3`. Thus it is a genuine obstruction to that **Fourier norm**, but it is not an analytic hard survivor and should not be used as evidence that the true post-localization collar needs the same mechanism.

## 2. The r39 sharp mixed frame

Let

`H,X_1,X_2,X_3,X_4`

be arbitrary mutually independent real random variables with probability densities bounded by one. Define

`L=(X_1-X_3)/sqrt(2)`,
`P=(X_1+X_3)/sqrt(2)`,
`S=(X_2+X_4)/sqrt(2)`.                                           (2.1)

The r39 opposite-sign barrier family is

`Q_theta
 = theta H^2 + 2 sqrt(2) H L + 2P^2 + 4LS`,
`theta in R`.                                                     (2.2)

In the deterministic orthonormal carrier `(H,L,P,S)`, its matrix is

`A_theta =
 [[theta, sqrt(2), 0, 0],
  [sqrt(2), 0,       0, 2],
  [0,       0,       2, 0],
  [0,       2,       0, 0]].`                                    (2.3)

The `P` direction is an eigenvector with eigenvalue `2`. The `(L,S)` principal block is

`[[0,2],[2,0]]`,                                                  (2.4)

with eigenvalues `+2,-2`. Cauchy interlacing in the `(H,L,S)` block gives one eigenvalue at least `2` and one at most `-2`. Therefore, for every real `theta`, (2.2) has at least three eigenvalues of modulus at least `2`. It is a strict instance of the owner target for every pivot value, including the nonzero-pivot regime.

The fleet03/B16 r39 calculation chooses the two source banks `{1,2}` and `{3,4}`. Their pure three-volumes vanish while the two mixed Pluecker orientations both have mass `1/2`. For centered unit uniforms the old absolute TT* kernel is infinite because it contains the factor

`[ integral_R |2 sin(u/2)/u| du ]^2 = infinity.`                  (2.5)

Equation (2.5) is correct. The point of this report is that it diagnoses a poor norm at a family that has a much cheaper physical packet.

## 3. Original-coordinate expansion exposes the packet

Expand (2.2) using (2.1):

`2 sqrt(2) H L = 2H(X_1-X_3)`,
`2P^2=(X_1+X_3)^2`,
`4LS=2(X_1-X_3)(X_2+X_4)`.

Hence

`Q_theta
 = theta H^2
 + 2H(X_1-X_3)
 + (X_1+X_3)^2
 + 2(X_1-X_3)(X_2+X_4).`                                       (3.1)

Condition on the **original** coordinates

`(H,X_4)=(h,x_4)`                                                (3.2)

and put

`C=h+x_4`.

The remaining coordinates `X_1,X_2,X_3` stay genuinely independent with the original density caps, and after subtracting the harmless constant `theta h^2`,

`Q_theta-theta h^2
 = (X_1+X_3)^2+2(X_1-X_3)(X_2+C).`                              (3.3)

Now set

`Y=X_2+C`,
`U=(X_1-X_3)/sqrt(2)`,
`V=(X_1+X_3)/sqrt(2)`.                                           (3.4)

The scalar `Y` is independent of `(U,V)` and has density cap one. I do **not** assert that `U,V` are independent. What is available is stronger in the right direction: `(U,V)` is an orthogonal linear image of the two original independent variables `(X_1,X_3)`. Its inverse is

`X_1=(V+U)/sqrt(2)`,
`X_3=(V-U)/sqrt(2)`,                                             (3.5)

whose Jacobian has absolute value one. Therefore the actual joint density is

`g_(U,V)(u,v)
 = f_1((v+u)/sqrt(2)) f_3((v-u)/sqrt(2))`,                       (3.6)

and hence

`boxed: ||g_(U,V)||_infinity <= 1.`                              (3.7)

This is exact original-product provenance, not a generic projected-density abstraction.

Equation (3.3) becomes

`Q_theta-theta h^2 = 2 sqrt(2) YU+2V^2`.                         (3.8)

The coefficient matrix in `(Y,U,V)` is

`B=
 [[0,       sqrt(2),0],
  [sqrt(2),0,      0],
  [0,       0,      2]],`

so

`det B=-4`.                                                       (3.9)

## 4. New closure: `QFORM-SHARP-MIXED-FRAME-OPPOSITESIGN-CLOSURE-v1`

The completed theorem `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1` says: if the first scalar has conditional density cap `K`, the remaining pair has joint density cap `M`, and a nonsingular `3x3` quadratic coefficient matrix has zero first diagonal entry, then

`||p||_(infinity,ess)
 <=3*2^(2/3)(KM)^(2/3)|det B|^(-1/3).`                           (4.1)

Apply (4.1) to (3.8) with

`K=1`, `M=1`, `|det B|=4`.

The powers cancel exactly:

`3*2^(2/3)*4^(-1/3)=3.`                                         (4.2)

Therefore for every conditioning value `(h,x_4)`,

`||p_(Q_theta | H=h,X_4=x_4)||_(infinity,ess) <=3.`             (4.3)

Averaging the conditional laws proves the full-line estimate

`boxed:
 ||p_(Q_theta)||_(infinity,ess) <=3
 for every theta in R.
`                                                                    (4.4)

This is uniform in the source laws and the fresh-hub pivot. The zero-pivot theorem also supplies absolute continuity. It does not by itself supply continuity, so no continuity claim is made here.

### Why the r48 partner obstruction does not contradict (4.4)

The fleet03/B11 r48 falsifier deliberately permits a nonlinear residual dependence that cancels its apparent square. In (3.8), by contrast, the full curved pair `(U,V)` is the explicit orthogonal image (3.5) of two original independent coordinates and has the cap-one joint density (3.6). The argument spends that joint curved trace **before** attempting to separate a hyperbolic `L^3` norm from a square `L^(3/2)` norm. No dependence-safe Young inequality is invoked.

Thus the designated partner result is used here as a route constraint: the valid compiler is the source-preserving curved trace, not the refuted marginal-norm interface.

## 5. The rank-two logarithm is literal inside the same construction

The third direction in (3.8) is genuinely needed. Delete `2V^2`, take `C=0`, and choose `X_1,X_2,X_3` to be centered unit uniforms. Then

`U=(X_1-X_3)/sqrt(2)`

has the triangular density

`p_U(u)=sqrt(2)(1-sqrt(2)|u|),
 |u|<=1/sqrt(2)`,                                                (5.1)

so

`p_U(u)>=1/sqrt(2)`
whenever
`|u|<=1/(2sqrt(2))`.                                             (5.2)

Let

`R=2sqrt(2) U X_2`.                                              (5.3)

For `t!=0`, the product-density formula gives

`p_R(t)
 = integral_R p_U(u)
   p_(X_2)(t/(2sqrt(2)u))
   [2sqrt(2)|u|]^(-1) du.`                                      (5.4)

When `0<|t|<1/2`, the region

`|t|/sqrt(2) <= |u| <=1/(2sqrt(2))`                              (5.5)

lies inside the support constraint `|t/(2sqrt(2)u)|<=1/2`. On that region (5.2) and `p_(X_2)=1` give

`p_R(t)
 >= (1/2) integral_(|t|/sqrt(2))^(1/(2sqrt(2))) du/u
 = (1/2) log(1/(2|t|)).`                                        (5.6)

Hence

`boxed: p_R(t) -> infinity logarithmically as t->0.`             (5.7)

This is an actual independent-product rank-two obstruction, not an arbitrary dependent surrogate.

Restoring the same-source square `2V^2` changes (5.7) to the uniform essential bound (4.4). The mechanism is exact:

`rank-two product log`
`   + cap-one curved pair (U,V) from the SAME two original sources`
`   + one fresh scalar Y`
` -> zero-pivot three-variable trace with |det B|=4`
` -> ||p||_infinity<=3.`                                        (5.8)

The third direction does not first make `U` independent of `V`; it removes the logarithmic endpoint through the two-dimensional curved trace.

## 6. Required pinned `e5f71d79...` source applied to a real inequality

The owner-pinned package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was read at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. A completed result in `COUNTEREXAMPLE_SEARCH.md` says that if an original physical principal `3x3` block has all eigenvalues of modulus at least `sigma`, then after conditioning on the other original coordinates the full quadratic-plus-linear form has density at most

`6 sqrt(pi)/sigma`.                                              (6.1)

For (3.1), condition on `(H,X_4)` as above and order the remaining original triple as `(X_1,X_2,X_3)`. Its quadratic matrix is

`M=
 [[1, 1, 1],
  [1, 0,-1],
  [1,-1, 1]].`                                                   (6.2)

Direct calculation gives

`det M=-4`,
`char_M(lambda)=(lambda-2)(lambda^2-2)`,
`spec(M)={2,+sqrt(2),-sqrt(2)}.`                                 (6.3)

Thus `sigma=sqrt(2)` and the pinned theorem gives the literal full-line bound

`boxed:
 ||p_(Q_theta)||_infinity
 <= 6sqrt(pi)/sqrt(2)
 =3sqrt(2pi)
 =7.519884823893... .
`                                                                    (6.4)

This independently pays the same strict target family. The source-preserving zero-pivot trace improves (6.4) to `3`.

The same pinned package's ruled theorem applies after the conditional affine term is removed by a deterministic translation of the three original coordinates. The conditional matrix (6.2) has signature `(+,+,-)`, so on its one-sheet side the conditional density is bounded by `pi sqrt(2)`. I do **not** transfer that X-ray/ruling bound across the conditional critical value to the opposite two-sheet side. The full-line bound (4.3), not the ruling, pays both sides.

## 7. Consequence for the phase-aware mixed-volume programme

The fleet03/B16 r39 pair of sister families established that identical mixed Pluecker masses can lead to very different behavior of one chosen proof norm. The new calculation adds a necessary qualification:

**the opposite-sign sister that makes the old absolute TT* kernel infinite already contains a fixed nonsingular zero-diagonal original physical triple with determinant `-4`.**              (7.1)

Indeed (6.2) has a zero diagonal at `X_2` and determinant `-4`. It is therefore removed before the fleet reaches the genuine no-localized-packet ultra-coloop survivor.

So (2.5) proves that total mixed volume alone does not control that specific absolute kernel, but it does **not** by itself show that cancellation-preserving TT* is necessary in the final residual branch. Any future barrier meant to constrain `QFORM-PUNCTURED-ULTRACOLOOP-PRODUCT-RECEIVER-v2` must also survive the already-paid physical-triple / pair-area exits.

This is the main structural update from the run: separate

1. a **proof-norm barrier** occurring in an already-paid localized target family, from
2. the genuinely unpaid diffuse nonzero-pivot collar in which every such physical packet has already been removed.

## 8. Exact remaining B11 target

The first unpaid implication is now stated more narrowly as

`QFORM-B11-NONZERO-PIVOT-DIFFUSE-MIXED-COLLAR-v1`:

> In the exact-rank-three indefinite near-coloop survivor after the zero-pivot Witt branch, all quantitative physical-pair / zero-diagonal principal-triple / projected-crossing exits, and the outer pivot estimate have been removed, prove a universal two-sheet essential-density bound in the small nonzero fresh-hub-pivot collar by spending the two disjoint original-product banks and their mixed third-volume currency before any dependence-blind marginal split; or force one of the already-paid exits.

The fleet03/B11 r48 falsifier remains the negative guide: a bare same-bank `L^3 x L^(3/2)` interface is invalid. The fleet03/B16 r39 barrier remains a negative guide only after adding the no-localized-packet hypothesis; its published sharp four-leaf example itself is now paid by (4.4).

Arbitrary additional nonseparable spectrum beyond exact rank three is still a separate full-target bridge. Full QFORM remains OPEN. Full-target continuity remains OPEN.

## 9. Scope and integrity

New mathematical content of this run:

- source-matched closure `QFORM-SHARP-MIXED-FRAME-OPPOSITESIGN-CLOSURE-v1`, equation (4.4), for the r39 strict target barrier family, uniformly in the nonzero hub pivot;
- explicit preservation of the rank-two logarithmic singularity in the same original-product construction, equation (5.6);
- route localization (7.1): the published absolute-TT* divergence example lies in an already-paid zero-diagonal physical-triple branch and therefore does not itself constrain the final diffuse collar.

Completed results actually consumed at equation level:

- fleet03/B11 r48 dependence-blind `L^3 x L^(3/2)` interface falsifier;
- fleet01/B11 Witt-leverage source match closing the zero-pivot near-coloop puncture;
- fleet02/B16 / fleet01/B16 `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1` receiver;
- pinned `e5f71d79...` localized physical-three-coordinate theorem and ruled one-sheet theorem.

No task state, cadence, notification/email, permission, public-release, paid-call, cross-account-authentication, FEI/install/benchmark, remote-workflow, or unrelated-data action is part of this mathematics.
