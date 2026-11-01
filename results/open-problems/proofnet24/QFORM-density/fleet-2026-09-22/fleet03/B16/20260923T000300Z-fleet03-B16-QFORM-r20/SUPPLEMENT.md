# QFORM-HALF-RIESZ-RECEIVER-REPLACEMENT-v1

This supplement records the positive replacement suggested by `QFORM-PROJECTION-CAP-NONZERO-PIVOT-BARRIER-v1`.

## Lemma: half-Riesz is a dependence-safe receiver invariant

Let `X` have a probability density bounded by one and be independent of a random pair `(D,W)`. Let `a!=0`, and put

`Q=a(X+D)^2+W`.

Assume

`K := sup_t E|W-t|^{-1/2} < infinity`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= |a|^{-1/2} K`.                         (1)

### Proof

Condition on `(D,W)=(d,w)`. Translation does not change the density cap of `X+d`. The pushforward of a cap-one scalar density under `x -> a x^2` has density bounded by

`|a|^{-1/2}|s|^{-1/2}`

on the appropriate sign half-line: there are at most two roots and the derivative at a root has magnitude `2 sqrt(|a s|)`. Therefore the conditional density of `Q` at `t` is bounded by

`|a|^{-1/2}|t-w|^{-1/2}`.

Average over `(D,W)` and take the supremum in `t`. This proves (1). No independence between `D` and `W` is required.

## Application to a genuine product projection

Let `Z` have independent cap-one coordinates, `U^T U=I_2`, and let `H` be invertible symmetric. Put

`W=(U^T Z)^T H(U^T Z)+b^T Z`.

The completed theorem `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` gives

`sup_t E|W-t|^{-1/2} <= 128 |det H|^{-1/4}`

for arbitrary `b`, and the sharper constant `16 sqrt(30)` when `b` belongs to `range(U)`, including `b=0`.

Consequently, for an independent cap-one scalar `X` and an arbitrary shift `D=D(Z)`, (1) yields

`||p_{a(X+D)^2+W}||_infinity
 <=128 |a|^{-1/2}|det H|^{-1/4}`,                           (2)

or `16 sqrt(30)` in place of `128` in the in-range affine case.

For the fixed model from the main report,

`Q=X^2+2(U_1 U_2)`,

where `(U_1,U_2)=U^T Z` is a genuine two-dimensional projection of the original independent product source, take

`H=[[0,1],[1,0]]`, `|det H|=1`, `b=0`, `a=1`, `D=0`.

Then

`||p_Q||_infinity <=16 sqrt(30)`.

Thus the exact same normalized quadratic matrix that admits arbitrarily large peaks for arbitrary cap-one *dependent* plane laws is uniformly bounded when the plane law retains genuine product-projection provenance. The discriminator is the half-Riesz estimate, not the projected `L^infinity` height.

## What remains unpaid

In the near-null coloop model, completing a nonzero scalar pivot gives a rank-two Schur form with determinant `det H = det B/a`. Bound (2) then scales like

`|a|^{-1/2}|det H|^{-1/4}
 = |a|^{-1/4}|det B|^{-1/4}`,

so it still blows up as `a->0`. The null-pivot theorem has a finite cap-based bound, but the main report proves that one cannot bridge the two regimes using only the projected density cap.

The remaining target-relevant problem is therefore to exploit the **joint relation** between the linear coupling and the rank-two Schur half-Riesz geometry before taking the scalar-root supremum. This is a genuinely stronger product-provenance question, not a missing constant in the projection theorem.
