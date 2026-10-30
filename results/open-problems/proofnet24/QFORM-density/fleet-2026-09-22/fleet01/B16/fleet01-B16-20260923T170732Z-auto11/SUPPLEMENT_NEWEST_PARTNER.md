# fleet01/B16 supplement — newest completed fleet02/B16 result consumed

A newer designated-partner result completed after the main report was written, so this append-only supplement source-pins and applies it without altering the immutable report.

Newest completed partner:

`yspennstate/math-open-problems@c8258480a0bfb67e9b128e67c477c5c5dcdd38e8`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/fleet02-B16-20260923T163017Z-auto11b/REPORT.md`.

Its proved theorem `QFORM-HUB-SCHUR-DIFFUSE-CROSS2-v1` shows that in the exact-rank-three true-near-coloop chamber with hub leverage `c>63/64`, every residual transverse row norm squared below `1/64`, and nonzero physical hub pivot `A_00`, the exact hub Schur complement is a uniformly diffuse rank-two form and

`H_(1/2)(S) <= 8(64/9)^(1/4)=13.0639452948...`,

hence

`||p_Q||_infinity <=13.0639452949/sqrt(|A_00|).`                  (S.1)

This is an essential bound only in the stated nonzero-pivot branch and intentionally deteriorates as `A_00->0`.

## Actual inequality from the newest partner result

For every such near-coloop form satisfying in addition

`|A_00|>=1/16`,                                                     (S.2)

(S.1) gives the explicit target-level inequality

`boxed: ||p_Q||_infinity <=52.2557811796... <52.256.`              (S.3)

If `R` is **any** quadratic form on additional disjoint original-coordinate variables, then `Q` and `R` are independent and

`p_(Q+R)=p_Q*mu_R`.

Therefore the genuinely arbitrary-dimensional block-direct-sum extension obeys

`boxed: ||p_(Q+R)||_infinity <52.256.`                             (S.4)

The original exact-rank-three block already carries the three eigenvalues of modulus at least one, so adjoining an arbitrary symmetric block preserves membership in the owner's full spectral target. No continuity upgrade is claimed from (S.1).

The same newest partner report also supplies the exact target-valid stress family

`Q_eta = eta(sqrt(c)X_0+sqrt(delta)T)^2
        +2sqrt(1+eta)(sqrt(c)X_0+sqrt(delta)T)U
        +V^2`,

with spectral values `{1+eta,-1,1}` and all leaf atoms shared/diffuse. Although the translation-uniform square envelope diverges logarithmically as `eta->0`, the partner's source-class grouping proves

`||p_(Q_eta)||_infinity <176`                                      (S.5)

for every independent cap-one source law in that family. Consequently, for any additional disjoint quadratic block `R`,

`boxed: ||p_(Q_eta+R)||_infinity <176.`                            (S.6)

This confirms that the square-envelope divergence is a proof-interface obstruction, not a density counterexample.

## Relation to the new fleet01/B16 theorem

The main report's `QFORM-CROSS2-OVERLAP-SQUARE-L1-v1` closes a different overlap mechanism: a nonzero transverse square may share the same source bank as a rank-two crossing pair, provided the active hub-side phase factors through the resulting three-dimensional projection. The newest partner stress family instead has a near-null **single-hub/rank-one** crossing with two small longitudinal innovations; it therefore does not satisfy the rank-two crossing hypothesis of the new theorem. The two results are complementary.

The first unpaid B16 bridge remains the arbitrary two-small-innovation source-adapted hub endpoint: either expose a rank-two crossing plus same-bank transverse square of the proved type, or retain the original unnormalised hub density through the near-null translation while paying the order-one transverse curvature. No conditional projection cap, post-rotation independence, or translation-uniform square envelope is inserted.
