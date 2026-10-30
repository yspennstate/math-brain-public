SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-23T21:19:45Z.
attacking: the zero-pivot localized rank-three branch by a product-preserving linear-square rearrangement that never divides by the scalar pivot.

# fleet03/B04 — zero-pivot three-coordinate receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement / product-space inequalities  
Status: `NEW SUPPORTING THEOREM / ZERO-PIVOT LOCALIZED BRANCH / FULL TARGET OPEN`  
Execution status: `WITHOUT_VERIFIED_BRAIN`  
Continuity: proved for the theorem below (`C_0`); full-target continuity remains OPEN.

The unrestricted conjecture is not proved here. This run changes mechanism from the immediately preceding scalar-pivot/C1-overlap work: it treats a literal zero diagonal pivot directly, retaining the product provenance needed to avoid the corrected arbitrary-joint coarea failure.

## 1. The theorem

Let `S={0,1,2}` be three ORIGINAL coordinates. Condition on every coordinate outside `S`, so the conditional form on these three variables is

`q(x)=x^T B x + 2 b^T x + c`,

where `B=A[S,S]` is fixed, the affine vector `b` may depend arbitrarily on the conditioned outside coordinates, and `X_0,X_1,X_2` remain independent with one-dimensional densities at most one.

Assume

`B_00=0`,  `D=|det B|>0`.

### Theorem — `QFORM-ZERO-PIVOT-3COORD-LINEAR-SQUARE-v1`

For every affine term `b` and every admissible product input law,

`boxed:
  ||p_q||_infinity <= 3*2^(2/3) D^(-1/3).`

The conditional density has a continuous representative vanishing at infinity. Therefore the FULL ambient quadratic form, after averaging over the outside original coordinates, also has a continuous `C_0` density satisfying the same bound.

No moment, support, log-concavity or smoothness hypothesis is used. The proof never rotates the random vector and then calls the rotated coordinates independent. It rotates only the two-dimensional `(X_1,X_2)` density as a joint density, keeping the pointwise cap inherited from `f_1 f_2<=1`, while `X_0` stays independent of that entire pair.

## 2. Proof

Write the first row of `B` as

`(0, ell_1, ell_2)`

and set `r=sqrt(ell_1^2+ell_2^2)`. Since `det B !=0`, `r>0`. Apply an orthogonal change of variables only inside the `(x_1,x_2)` plane, choosing coordinates `(y,z)` with the `y`-axis parallel to `(ell_1,ell_2)`. The joint density `g(y,z)` of `(Y,Z)` is merely the rotated product density; it need not factor, but

`0<=g<=1`,  `integral g=1`.

The variable `X_0` remains independent of `(Y,Z)`. Translating `y` absorbs the affine coefficient of `x_0`. Completing the square in `z`, with a `y`-dependent translation, puts the conditional form into

`q = 2 r X_0 Y + gamma W^2 + H(Y)`,

where `H` is a real quadratic polynomial and the translated joint density of `(Y,W)` is still at most one. In the orthonormal basis `(x_0,y,z)`, the matrix is

`[[0,r,0],[r,*,*],[0,*,gamma]]`,

hence

`boxed: D=r^2 |gamma|.`

Let `p_Y` be the density of `Y`. For almost every `y` with `p_Y(y)>0`, the conditional density of `W|Y=y` is bounded by

`m_y=1/p_Y(y)`.

Conditional on `Y=y`, `X_0` and `W` are independent. The linear variable `2 r y X_0` has a probability density `h_y` satisfying

`||h_y||_infinity <= c_y=1/(2 r |y|)`

for `y!=0`. The variable `gamma W^2` has a density bounded on its supporting half-line by

`m_y / sqrt(|gamma| |u|)`.

We use the elementary decreasing-rearrangement fact

`sup_{h>=0, integral h=1, ||h||_infinity<=c}
 integral_0^infinity h(t-u) u^(-1/2) du <= 2 sqrt(c)`.

Indeed the maximum is attained by filling the highest part of the decreasing kernel, i.e. by a density `c` on an interval of length `1/c` adjacent to zero. Therefore, for almost every `y!=0`,

`||p_(q|Y=y)||_infinity
 <= min{ 1/(2 r |y|),
          sqrt(2)/(p_Y(y) sqrt(|gamma| r |y|)) }.`

After multiplying by `p_Y(y)` and averaging in `y`, for every output point `s`,

`p_q(s)
 <= integral_R min{ p_Y(y)/(2 r |y|),
                     C |y|^(-1/2) } dy`,

where

`C=sqrt(2)/sqrt(|gamma| r)`.

For any `R>0`, use the second branch on `|y|<=R` and the first branch on `|y|>R`:

`p_q(s) <= 4 C sqrt(R) + 1/(2 r R).`

The optimizing value satisfies

`R^(3/2)=1/(4 r C)`.

At that value,

`p_q(s)
 <= 6*2^(-1/3) |gamma|^(-1/3) r^(-2/3)
 = 3*2^(2/3) (r^2 |gamma|)^(-1/3)
 = 3*2^(2/3) D^(-1/3).`

This is uniform in every affine term produced by the outside conditioning, so averaging gives the same bound for the full ambient form.

For continuity, for a.e. `y!=0` the conditional density is the convolution of two `L^1` densities and is therefore in `C_0`. The integrable majorant used above is independent of the output point. Dominated convergence first gives continuity of the averaged density and then its vanishing at infinity. QED.

## 3. Why this is correction-safe

The current correction ledger rules out arbitrary-joint rank-three coarea and warns that a bounded projection density alone is insufficient. This proof uses neither. The only rotated object is the two-dimensional joint density of `(X_1,X_2)`, for which the cap `g<=1` follows directly from the original product density and the unit Jacobian. The decisive extra fact is that the untouched original coordinate `X_0` remains independent of the whole rotated pair. The conditional convolution is therefore genuine.

The result also does not divide by `B_00`: it is specifically a zero-pivot theorem. Thus it complements, rather than rephrases, scalar-Schur receivers whose constants deteriorate as a physical diagonal pivot tends to zero.

## 4. Explicit genuinely rotated indefinite example

Take

`B_* = [[0,2,2],[2,0,2],[2,2,0]] = 2(J_3-I_3)`.

This is not diagonal in the independent coordinates. Its eigenvectors are non-coordinate directions; exactly,

`spec(B_*)={4,-2,-2}`,

so all three eigenvalues have absolute value at least two and the target spectral hypothesis is satisfied. Also

`det B_*=16`.

Hence for EVERY independent cap-one triple,

`boxed:
 ||p_(X^T B_* X)||_infinity
 <= 3*2^(2/3)*16^(-1/3)
 = 3*2^(-2/3)
 = 1.8898815748423097... .`

The density is continuous and vanishes at infinity.

The same estimate survives arbitrary additional coordinates and arbitrary couplings to them, provided this exact principal `3x3` block is retained: condition on those outside original coordinates and use the affine-uniform theorem above.

## 5. Actual peer-result consumption

The designated `fleet04/B04` partner still has no completed current-QFORM canonical report or shared handoff visible in the authorized repositories, so no partner theorem is fabricated.

I nevertheless applied the completed fleet theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` from the current research ledger to an actual slice of the same example. Conditioning on `X_0=x_0`, the remaining `(X_1,X_2)` quadratic matrix is

`Lambda=[[0,2],[2,0]]`,  `|det Lambda|=4`,

with arbitrary affine vector `(4x_0,4x_0)`. The peer theorem therefore gives the explicit, translation-uniform inequality

`sup_t E_{X_1,X_2}|4 X_1 X_2 +4x_0(X_1+X_2)-t|^(-1/2)
 <=128*4^(-1/4)=64 sqrt(2)=90.50966799187809... .`

That peer inequality is valid but does not by itself produce the zero-pivot density bound; the new linear-square rearrangement above is what closes the three-coordinate zero-pivot slice without inserting a fourth scalar square.

## 6. Remaining implication

Full QFORM remains OPEN. This theorem pays a useful localized zero-pivot class, but the bare three-large-eigenvalue hypothesis does not force one principal triple with determinant bounded below. The next B04 step is an aggregate-before-inversion version: volume-sample zero/near-zero-pivot physical triples and retain the product-space rearrangement before selecting a local reciprocal determinant, or route failure into the already-paid grouped-bank/ridge/star branches.

No scheduler, notification, email, public-release, paid-API, cross-account authentication, or task-state change is made by this report.
