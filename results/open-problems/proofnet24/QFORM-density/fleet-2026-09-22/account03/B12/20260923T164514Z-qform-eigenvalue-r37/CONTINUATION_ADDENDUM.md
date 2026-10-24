# r37 continuation addendum — applying the projected-crossing theorem to the splitter survivors

A later owner continuation became visible at the final control refresh (`QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`). This addendum consumes its newly required source rather than publishing under the stale source map. The full target remains OPEN.

Source applied: `yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. Its grouped-crossing theorem allows arbitrary internal hub functions and an arbitrary-rank projected light crossing, provided the exact rank of the hub-to-light block, the singular-product gate, projected crossing volume, and every volume row-marginal gate are retained.

We apply it to the ACTUAL original-coordinate balanced cut `I,J` produced in the main r37 report. Recall

    a = 1/(2 sqrt(2)),
    q = N_{A[I,J]}(a),

and each self block has at least `3-q` singular values at least `a`.

## A. The q=2 exact-cross-rank survivor

Assume this survivor has the stronger factual property

    rank B = 2,       B=A[I,J],       s_2(B)>=a.                 (A.1)

Take an SVD `B=U Sigma V^T`. Treat the entire ORIGINAL-coordinate group `X_I` as the grouped hub side, with `W=U^T X_I`. This does NOT assert independence of W's coordinates; the projection-density input in the new theorem gives

    M_H = ||p_W||infinity <= 2.                                  (A.2)

The self quadratic `X_I^T A[I,I] X_I` is absorbed into the theorem's arbitrary measurable hub function F.

Suppose there is an ORIGINAL-coordinate split `J=J_1 union J_2` such that the two-row matrix `Sigma V^T` restricted to `J_2` has rank two and singular-value product

    S >= a^2,                                                     (A.3)

and, writing `Pi` for the row-space projection of that restricted two-row matrix and

    C = A[J_1,J_2](I-Pi),
    F_cross = ||C||_F,

we have

    F_cross >= a,
    max_i ||C_{i,*}||_2^2 / F_cross^2 <= 1/2.                    (A.4)

For the new theorem take `k=2, ell=1`. Then `Z_1=F_cross^2`, the ell-volume row marginals are exactly the ratios in (A.4), and `d=k+ell=3`. Its product-law consequence gives

    ||p_Q||infinity
      <= 3*2^(7/6) (S F_cross)^(-1/3)
      <= 3*2^(7/6) (a^3)^(-1/3)
      = 3*2^(8/3)
      = 19.0488126236....                                        (A.5)

All internal quadratic curvature on I and on either light subbank is retained. Thus an exact-rank-two q=2 survivor is now paid whenever its remaining self curvature supplies one diffuse projected crossing direction at scale a. The unpaid q=2 cases are precisely those where the cross block has additional nonzero tail rank, the rank-two restriction to every candidate J_2 loses singular product, or the projected one-volume is too small/concentrated.

## B. The q=1 exact-cross-rank survivor

Assume instead

    rank B=1,        s_1(B)>=a.                                  (B.1)

Use the same grouped-hub construction with `k=1`; the one-dimensional projection obeys `M_H<=sqrt(2)`. Suppose an ORIGINAL-coordinate split `J=J_1 union J_2` has the restricted hub row nonzero with

    S>=a,                                                        (B.2)

and for

    C=A[J_1,J_2](I-Pi)

its two-volume satisfies

    Z_2=e_2(CC^T)>=a^4,                                         (B.3)

with every two-volume row marginal `alpha_i<=1/2`. Apply the new theorem with `k=1, ell=2`, so again `d=3`. Keeping its exponential factor gives

    ||p_Q||infinity
      <= 3*2^(7/6)*e^(1/3)*M_H^(1/3)*S^(-1/3)*Z_2^(-1/6)
      <= 3*2^(4/3)*e^(1/3)/a
      = 29.8403836927....                                        (B.4)

Thus the q=1 branch is paid whenever its two strong self resources can be realized as a diffuse projected two-volume across an actual light-coordinate split. Again the remaining gap is structural, not a hidden independence step: the splitter theorem alone does not force (B.2)-(B.3).

## C. What changed after the owner continuation

The new grouped-projection theorem converts two previously vague mixed splitter survivors into exact, checkable matrix obligations. For q=2 one needs a rank-two hub/light block plus one diffuse projected crossing direction. For q=1 one needs a rank-one hub/light block plus a diffuse projected two-volume. These conditions are not automatic from the r37 singular-value counts, so this addendum does not close the full theorem.

The continuation's current Claude README and `single_hub_core/REPORT.md` were also read. They reinforce that arbitrary internal hub functions and terms containing the hub projection can be retained, but a small spread coupling or concentrated projected volume remains a genuine obstacle. No refuted pointwise-decay, arbitrary-joint coarea, conditional-cap, or spectral-independence premise is used.
