# account02/B04 — two-cross Schur bridge with arbitrary extra spectrum

Run: `20260922T141554Z-account02-B04-QFORM-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
Assignment: Product Fourier rearrangement  
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The target remains: for every dimension, every independent real coordinate family whose one-dimensional probability densities satisfy `0<=f_i<=1`, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove a universal finite bound on the density of `X^TAX`, or give a genuine counterexample. No moment, support, identical-law, sign, diagonal-basis, log-concavity, or post-rotation-independence assumption is added.

The first unpaid implication is now:

> **`QFORM-SCHUR-TWO-CROSS-SELECTION-v1`.** Starting only from the three-large-eigenvalue hypothesis, show that either some nonzero original-coordinate scalar pivot `a` has a Schur complement with an original-coordinate cut carrying two singular values at least `sigma` and cross-range leverage below `q/2` for some `q<3/2`, with `|a| sigma` bounded below universally, or the form falls into an already controlled diffuse/aggregate/hyperbolic/fresh-bank mechanism.

The theorem proved below pays the entire analytic part of that implication once such a pivot-plus-two-cross certificate exists. In particular it does **not** require the Schur complement to have rank two and pays no reciprocal cost for arbitrary additional small singular/eigen directions.

This is a genuine strengthening of the previous B04 scalar-pivot bridge. The live `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` correction blocks an argument that demands rank exactly two after one pivot, while `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` blocks demanding three large cross directions. The new mechanism needs only **two** certified cross directions after the pivot.

## 2. Source-pinned dependencies and corrections

Fresh prepublication control: `yspennstate/math-research-brain@d56596e0c81b1e51a69c6c84cf3fb4fe88efb882`, owner revision `2026-09-22.5`, README blob `433b2d57345823967480245b59a7c47d51019c37`, live correction-inbox blob `337bc9adc6b8ed81d688dd32367c68c4b9b2a636`.

Required corrections consumed: the law-uniform scalar pointwise-decay claim is false; fiber-supremum bounds can lose dimension; rotations do not preserve coordinate independence; a good cross minor alone is not exhaustive; a single rank-two Schur extraction is not forced; generic conditional density caps are not independence; and a rank-three original-coordinate cross cut is not forced. None of those refuted statements is used positively.

Named partner actually applied: `account03/B04`, canonical report

`yspennstate/math-open-problems@55e0a30b6ac56934614a5416056cae2e4a6dc77e:proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T135303Z-r11/REPORT.md`, blob `77ac63575c79c5ced9f38da81aa450e68973e15d`.

That report independently PASSes the regularized product-space determinant estimate and gives its fractional-`q` form. The underlying source is

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

For any original-coordinate cut `I,J`, `B=A[I,J]`, and `1<=q<2`, if the diagonal of the projection onto `range(B)` on the `I` side is at most `q/2`, the proved estimate is

`|phi_A(t)| <= det(I + 2q t^2 B B^T/(pi^2 e^2))^(-1/(4q)).`       (2.1)

It is uniform over all within-block quadratic phases and outside couplings. It therefore preserves original-coordinate product structure and does not invoke false scalar pointwise decay.

A second source-valid dependency is account01/B11's completed dependent-square lemma,

`yspennstate/math-open-problems@e06922bfa31bbd225cdce6ee6aea563254e62563:proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`.

If `R` has a density with `||p_R||_3=M`, and the conditional law of `V` given `R=r` has density at most one a.e., then for `a!=0`,

`||p_(R+aV^2)||_infinity <= 4 |a|^(-1/2) M^(3/4).`                (2.2)

Below the conditional cap is not assumed generically: it comes from one untouched original coordinate entering additively after scalar square completion.

## 3. Two cross singular directions already give an L3 Schur density

### Theorem 3.1 — `QFORM-REGDET-TWO-CROSS-L3-v1`

Let `W` have independent real coordinates with densities bounded by one. Let `S` be any real symmetric matrix, of arbitrary rank and with arbitrary signs/eigenvalue sizes. Suppose there is a cut of original coordinates `I,J` and let

`B=S[I,J]`.

Assume, for some `1<=q<3/2`,

1. the coordinate diagonal of `P_range(B)` on the `I` side is at most `q/2`;
2. `B` has at least two singular values at least `sigma>0`.

For `R=W^T S W`, its law has an `L^3` density satisfying

`||p_R||_3
 <= (2pi)^(-2/3)
    [ (pi e/(sqrt(2q) sigma)) sqrt(pi)
      Gamma(3/(4q)-1/2)/Gamma(3/(4q)) ]^(2/3).`                  (3.1)

All additional singular directions of `B`, and all additional eigenvalue directions of `S`, are free in this estimate.

### Proof

Apply the partner-validated determinant estimate (2.1) directly to the actual Schur residual `S`. Keeping only the two factors corresponding to singular values at least `sigma` gives

`|phi_R(t)| <= (1+beta^2 t^2)^(-1/(2q)),`                       (3.2)

where

`beta = sqrt(2q) sigma/(pi e).`

This is a product-space estimate, not a one-dimensional law-uniform Fresnel assertion.

To phrase the integration in rearrangement form, let `g(t)=(1+beta^2t^2)^(-1/(2q))`. Since `g` is symmetric decreasing in `|t|` and `|phi_R|<=g`, decreasing rearrangement gives

`|phi_R|^*(s) <= g^*(s) = (1+beta^2 s^2/4)^(-1/(2q)).`           (3.3)

Thus the `L^(3/2)` norm is paid by an integrated rearranged envelope rather than by any false pointwise scalar decay mechanism. Equivalently, integrating (3.2) directly,

`int_R |phi_R(t)|^(3/2) dt
 <= beta^(-1) sqrt(pi)
    Gamma(3/(4q)-1/2)/Gamma(3/(4q)).`                            (3.4)

The gamma integral is finite exactly because `q<3/2`.

Inverse Hausdorff--Young, with `p(y)=(2pi)^(-1) int e^(-ity)phi(t)dt`, gives

`||p_R||_3 <= (2pi)^(-2/3)||phi_R||_(3/2)`,

which is (3.1). QED.

For `q=1`, this becomes

`||p_R||_3
 <= (2pi)^(-2/3)
    [ (pi e/(sqrt(2) sigma)) sqrt(pi)
      Gamma(1/4)/Gamma(3/4) ]^(2/3).`                            (3.5)

The rank-two opposite-sign logarithmic singularity is compatible with this theorem: `L^3` is the correct intermediate regularity, and no `L^infinity` bound is claimed before the third square is used.

## 4. Scalar pivot + two cross directions closes with arbitrary extra spectrum

### Theorem 4.1 — `QFORM-SCALAR-PIVOT-EXTRA-SPECTRUM-BRIDGE-v1`

Let `X=(W,Z)` have independent real coordinates with densities bounded by one, and partition a real symmetric matrix as

`A = [[C,b],[b^T,a]],   a!=0.`

Let

`S=C-bb^T/a`

be the scalar Schur complement. Suppose `S` satisfies the hypotheses of Theorem 3.1 for some `1<=q<3/2` and `sigma>0`. Then `Q=X^TAX` has an essentially bounded density and

`boxed(
 ||p_Q||_infinity
 <= C_piv(q) / sqrt(|a| sigma),
)`                                                               (4.1)

where

`C_piv(q)
 =2^(5/4) e^(1/2) pi^(1/4) q^(-1/4)
  [Gamma(3/(4q)-1/2)/Gamma(3/(4q))]^(1/2).`                      (4.2)

In particular, under the clean leverage hypothesis `max diag P_range(B)<=1/2`, one may take `q=1` and obtain

`boxed(
 ||p_Q||_infinity
 <= 8.979886418 / sqrt(|a| sigma).
)`                                                               (4.3)

### Proof

Complete the square in the **original** coordinate `Z`:

`Q = W^T S W + a (Z+a^(-1)b^T W)^2 = R+aV^2.`                  (4.4)

By Theorem 3.1, `R` has the `L^3` density bound (3.1). Conditional on `R=r`, the shift `a^(-1)b^TW` can be random, but `Z` is independent of all of `W`; therefore `V=Z+a^(-1)b^TW` conditional on `R=r` is a mixture of translations of the original density of `Z`, and its conditional density is still at most one. This is the source-valid fresh-noise situation, not the refuted generic conditional-cap substitution.

Apply (2.2) to (4.4):

`||p_Q||_infinity <= 4|a|^(-1/2)||p_R||_3^(3/4).`               (4.5)

Substitution of (3.1), followed by `beta=sqrt(2q)sigma/(pi e)`, simplifies exactly to (4.1)-(4.2). QED.

The structural gain is important: the partner's earlier exact-rank-two Schur theorem required the whole Schur complement to have rank two. The present theorem requires only two certified cross singular directions inside an arbitrary-rank Schur residual. Every additional small singular value is retained in the determinant and may simply be discarded as a factor at most one; no reciprocal product of small eigenvalues occurs.

## 5. Explicit genuinely rotated indefinite 65-coordinate instance

Index 64 original residual coordinates by `x in {0,1}^6`. Define a `64 x 4` Walsh frame by

`U_x = (1, (-1)^(x_1), (-1)^(x_2), (-1)^(x_3))/8.`              (5.1)

The columns are orthonormal and every residual physical row has leverage `4/64=1/16`. Put

`Lambda_S=diag(2,-2,1/4,-1/4),`

`S=U Lambda_S U^T.`                                               (5.2)

Let `u_3` denote the Walsh column carrying eigenvalue `+1/4`, take

`a=2,   b=(1/2)u_3,`

and define the full `65 x 65` matrix

`A = [[S+(1/a)bb^T, b],[b^T,a]].`                                (5.3)

Every one of the 64 pivot couplings is nonzero, equal in modulus to `1/16`; the form is therefore genuinely rotated and coupled in the original independent coordinates. Pivoting the last original coordinate recovers the Schur complement exactly as `S`.

### Exact target spectrum

The Walsh directions with residual eigenvalues `2`, `-2`, and `-1/4` remain eigenvectors of `A`. On the span of `u_3` and the last coordinate, the matrix is

`[[3/8,1/2],[1/2,2]],`

whose eigenvalues are

`(19+sqrt(233))/16,   (19-sqrt(233))/16.`                         (5.4)

Hence `A` is indefinite and has at least three target-scale eigenvalues:

`2, -2, (19+sqrt(233))/16`,

all with modulus at least one. No diagonal-basis independence is used.

### The product-space certificate

Partition the 64 residual original coordinates by an **unused** Walsh bit, say

`I={x:x_4=0},  J={x:x_4=1}.`

Because the four selected Walsh columns do not depend on `x_4`,

`U_I^T U_I=U_J^T U_J=(1/2)I_4.`                                  (5.5)

Therefore the cross block `B=S[I,J]` has nonzero singular values

`1, 1, 1/8, 1/8.`                                                (5.6)

Moreover `range(B)=range(U_I)` and each cross-range leverage equals

`u_x^T ((1/2)I_4)^(-1)u_x = 2(1/16)=1/8 <1/2.`                  (5.7)

Thus Theorem 4.1 applies with `q=1`, `sigma=1`, and `a=2`. For **every** independent input law with coordinate densities bounded by one,

`boxed(
 ||p_(X^T A X)||_infinity
 <= 2^(3/4) sqrt(e) pi^(1/4)
    sqrt(Gamma(1/4)/Gamma(3/4))
 < 6.350.
)`                                                               (5.8)

This example deliberately includes two extra small Schur eigenvalues `+1/4,-1/4`; the estimate is insensitive to them and does not assume they are independent additive noise.

## 6. Exact numerical evaluation used

Only the displayed constants were numerically evaluated. The exact code/output used was:

```python
import mpmath as mp
mp.mp.dps = 50
G = mp.gamma(mp.mpf('0.25'))/mp.gamma(mp.mpf('0.75'))
C = 2**(mp.mpf(5)/4)*mp.sqrt(mp.e)*mp.pi**(mp.mpf(1)/4)*mp.sqrt(G)
print(G)
print(C)
print(C/mp.sqrt(2))
```

Output:

```text
2.9586751191886388923108213577277195664748981960579788
8.9798864170227788127517101128712418760176546000550927
6.3497385797617763104562311718815158351214982183490898
```

No numerical experiment is used as proof.

## 7. Conditional end-to-end route after this result

A source-valid conditional route to full QFORM is now:

1. the full-range diffuse regime is paid by the reviewed regularized-determinant/MSS theorem;
2. rank-three diffuse and several localized/aggregate branches are already paid by source-pinned team results;
3. if a nonzero scalar original-coordinate pivot leaves **two** quantitatively large cross directions with leverage `q/2`, Theorem 4.1 pays the branch even with arbitrary residual rank and arbitrarily small additional eigenvalues;
4. therefore the remaining hard work is structural selection/aggregation: prove `QFORM-SCHUR-TWO-CROSS-SELECTION-v1` or route every failure of it into an existing hyperbolic-bank, fresh-square cascade, diagonal, or diffuse mechanism;
5. finally, transfer the exact-rank/selected-core closure through arbitrary additional spectral directions outside already certified cuts. The regularized determinant theorem shows how to do this whenever the cross certificate survives; a completely general structural extraction remains unpaid.

The Fourier-frame family from the preceding B04 run already shows why step 4 cannot demand a universally large scalar pivot, while the live local-cross correction shows it cannot simply demand three large cross singular values. The new theorem lowers the analytic certificate after one pivot to two directions, matching the amount of curvature needed for an `L^3` base that one fresh original-coordinate square can smooth to `L^infinity`.

## 8. Status

- Full QFORM conjecture: `OPEN`.
- `QFORM-REGDET-TWO-CROSS-L3-v1`: `PROVED` under the stated original-coordinate cross certificate.
- `QFORM-SCALAR-PIVOT-EXTRA-SPECTRUM-BRIDGE-v1`: `PROVED` under the stated scalar-pivot plus two-cross certificate.
- Explicit rotated indefinite 65-coordinate target instance: `PROVED` with density bound `<6.350` for arbitrary independent density-`<=1` inputs.
- First unpaid implication: `QFORM-SCHUR-TWO-CROSS-SELECTION-v1`.
- Classification: `ESSENTIAL_STEP_APPLIED`.
- No full-solution or novelty claim is made.
