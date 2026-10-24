# r22 parameter addendum — the anchored E3/E2 shadow at every threshold 1/2 <= h < 2/3

This addendum strengthens the fixed `h=3/5` choice in `REPORT.md`. It uses exactly the same hypotheses and preserves the same correction boundary.

## Theorem — `QFORM-ANCHORED-E3-H-PARAMETERIZED-SHADOW-v1`

Use the notation of Sections 3–6 of the r22 report. Thus `G>0` is a third-volume determinant bank anchored at a fixed physical row `i` and column `a`; the residual row-pair law has marginals `rho_k` summing to two; `R_i=||M[i,:]||_2`; and Theorem 3.1 constructs a fractional physical second-volume packet of mass `G/R_i^2`, avoiding row `i`, whose normalized residual row-pair law is exactly the same law.

Fix any

`1/2 <= h < 2/3`.

If

`max_(k!=i) rho_k <= h`,

then the full ambient quadratic form has a continuous density satisfying

`||p_Q||_infinity <= C(h) G^(-1/[2(2+h)]) R_i^((1-h)/(2+h))`,

where

`C(h)
 = e(2+h)/[(2-3h)sqrt(2h)]
   * h^[h/(2(2+h))]
   * (1-h)^[(1-h)/(2(2+h))].`

If in addition `G>=cF^6` and `R_i<=F`, the powers cancel exactly and

`||p_Q||_infinity <= C(h)c^(-1/[2(2+h)])F^(-1).`

### Proof

Use the anchored order-three packet and its exact order-two shadow. In the mixed-order theorem choose

`w=h`, `q=2h`, `r=2+h`.

At the anchor row, the mixed inclusion marginal is exactly `h=q/2`; at every residual row it is exactly `rho_k<=h=q/2`, because the order-three and shadow order-two packets have identical residual row-pair marginals. The Hausdorff–Young condition is therefore satisfied. Also `q>=1` since `h>=1/2`, and

`q<r/2 <=> 2h<(2+h)/2 <=> h<2/3`.

The mixed determinant coefficient is

`K_h=h^(-h)(1-h)^(-(1-h)) G R_i^(-2(1-h)).`

Substitution into the fractional-packet mixed-order theorem gives the displayed formula for `C(h)`. Finally,

`G^(-1/[2(2+h)]) R_i^((1-h)/(2+h))
 <= c^(-1/[2(2+h)]) F^[-3/(2+h)+(1-h)/(2+h)]
 = c^(-1/[2(2+h)])F^(-1).`

QED.

## Matching core-or-diffuse compiler

Define `H_h={k:rho_k>h}` and `delta_h=sum_(k notin H_h)rho_k`. Since `sum rho_k=2` and `h>=1/2`, one has `|H_h|<=3`.

If `delta_h<=1/2`, the residual pair lies entirely in `H_h` with probability at least `1/2`; among at most three heavy pairs, one therefore has determinant-law mass at least `1/6`. Exactly as in Theorem 5.1 of the report, the designated partner account02/B07 one-sided cross-fiber theorem gives

`||p_Q||_infinity <= 3sqrt(e)(6/G)^(1/6)`,

with a continuous density.

Thus if neither the flat-shadow branch nor the small-tail physical-row-triple branch pays on a side, that side has a residual hub of marginal `>h` and a light marginal tail `>1/2`.

If this happens on both row and column sides, choose hubs `u,v`. Their joint inclusion probability in the same anchored third-minor law obeys

`P(u in R, v in C) > 2h-1`.

Hence the fixed two-row/two-column third-volume bank satisfies

`G_(i,u;a,v) > (2h-1)G.`

This gives a tunable tradeoff between the analytic mixed-order constant and the determinant mass localized on the final double-pair bank. Examples:

- `h=0.55`: `C(h)=16.4995187631`, double-pair fraction `>0.10`;
- `h=0.60`: `C(h)=28.3425230588`, double-pair fraction `>0.20`;
- `h=0.625`: `C(h)=45.0124274277`, double-pair fraction `>0.25`.

The endpoint `h=2/3` is excluded because the mixed characteristic-function decay becomes exactly `|t|^-1`, so the present absolute Fourier-inversion receiver loses integrability there. This makes the threshold barrier transparent rather than accidental.

The full QFORM conjecture and global continuity remain open. The surviving structural target is still `QFORM-DOUBLEPAIR-ANCHOR-BANK-RECEIVER-v1`, now with a free `h` parameter available for downstream optimization.
