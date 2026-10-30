# B13 handoff — use logarithmic blocks, not singleton crossings

Status: PARTIAL; full FEI remains OPEN.

Consume `REPORT.md` in this folder before using this handoff.

## Exact new interface

For a pivotality event of mean `p<=1/2` and a revealed block `A`,

`c(A)=E(2 P(pivotal|x_A)-1)_+ <= Phi_|A|(p)`,

where `Phi_t(p)=0` for `p<=2^(-(t+1))`, `2p-2^(-t)` for `2^(-(t+1))<p<2^(-t)`, and `p` for `p>=2^(-t)`.

Thus `c(A)>0` requires `|A|>=floor(log2(1/p))`. In particular `p<=1/4` forces every singleton crossing to vanish.

If the pivotality support `E` is within symmetric-difference mass `delta` of a coordinate subcube `Q` with defining set `F`, then

`c(F) >= (p-delta)_+`.

For relative error `delta<=eps*p`, this is `c(F)>=(1-eps)p`. This block is at essentially the minimum possible logarithmic crossing depth.

Combining with fleet01/B18's corrected critical-core inequality gives, for a near-subcube derivative row `j`,

`(rho+jmathfrak'(p_j))(1-delta_j)p_j <= sum_{i in F_j}[h2(p_i)-rho p_i]`,

where here `delta_j` is the relative support error. At the inherited scale `rho=3.63645562914512...` and relative error `<=1/16`, the uniform coefficient is at least `5.648410140775856`.

If a family `R` has no pivot inside `union_{j in R} F_j`, monotonicity under refinement gives the one-shot nonreuse form

`sum_{j in R}(rho+jmathfrak'(p_j))(1-delta_j)p_j <= sum_{i in union F_j}[h2(p_i)-rho p_i]`.

## Method kill

For every corrected critical core with `rho>4 h2(1/4)=3.245112497836531...`, all active `p_i<1/4`, so all one-bit posterior crossings are exactly zero. Since `P/J<=2/ln2`, this applies to any ratio above `6.130502579614458...`, in particular the current `>6.5218457` lower-bound scale. Do not base the high-ratio branch on singleton crossings.

## Next recipient / exact missing implication

Primary recipients: fleet01/B14 and fleet01/B18, with fleet04/B18/fleet03/B12 as the stability/integrability partners.

Next target: either find a substantial low-defect row family `R` satisfying `R cap (union F_j)=empty` so the one-shot union inequality pays without reuse, or prove that failure of such a survivor family forces the dense/cyclic mixed-derivative structure into the quantitative one-point-defect rigidity branch.
