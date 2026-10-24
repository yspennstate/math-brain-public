# r39 post-refresh scope check

Fresh `math-research-brain` main was reread after the proof. The operative owner continuation remains `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; OWNER CONTROL remains revision `2026-09-22.15`; full QFORM remains OPEN.

Relevant live corrections rechecked include the conditional-projection-cap correction `QFORM-2D-PRODUCT-PROJECTION-CONDITIONAL-CAP-MOMENTS-FALSE-v1` and the earlier full-bilinear-completion correction consumed by r38. Neither is used as a premise here. The r39 theorem uses only unconditional marginal projection caps and an unconditional dyadic `L^2(dt)` calculation while retaining the exact rank-two crossing.

An early r39 draft tried to splice the new internal-bilinear theorem into the case of a *small but nonzero* `alpha z^2` coefficient. That splice is not valid: without moment assumptions a small quadratic coefficient is not a uniformly small random perturbation. The canonical `REPORT.md` has been corrected before handoff/publication. Its new theorem is applied only at the exact null ruling `alpha=0`. For `alpha != 0`, continuity comes from the already-proved r38 square theorem. The uniform height in the whole exact-graph true-near-coloop hard branch is inherited independently from r37's essential bound `<128/s`; equality almost everywhere plus continuity transfers that height bound to the continuous representative.

Therefore the supported r39 conclusion is:

- `QFORM-RANK2-CROSS-INTERNAL-BILINEAR-DYADIC-v1` is a new continuous-density theorem in its exact stated scope;
- at the exact null ruling of the r37/r38 exact-graph branch, it gives directly `||p_Q||_infinity <468/s`;
- together with r37 and r38, that exact-graph branch has a continuous representative with `||p_Q||_infinity <=128/s`;
- the punctured double-graph collar `0<rho_S,rho_T<<1` and the arbitrary-additional-spectrum bridge remain open.

No claim of a perturbative extension through nonzero small `alpha` is retained.
