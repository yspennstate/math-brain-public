# FOREST source-bound handoff — account02/B01 `B01-20260922T090454Z-forest-r17`

Outcome: `ESSENTIAL_STEP_APPLIED`. Execution: `WITHOUT_VERIFIED_BRAIN`. Parent target remains OPEN.

Source-bound input: lead account01/B01 `20260922T050946Z-b01-forest-auto11` (`FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`) localized triangle contractions to `STAR-2`. Named partner account03/B02 `20260922T050248Z-B02-forest-r13` supplies the unit theta-3 simple↔loopless transfer; partner `20260922T080202Z-B02-forest-r11` supplies the exact three-edge-cut nonnegativity formula.

Main advance: `STAR-2` is paid without a weighted theorem. Replace every labelled loopless-multigraph edge by three internally disjoint length-two paths. Projection has local lift counts `L0=L1=27`; choosing a distinguished physical half-edge in each marked gadget gives conditional means `1/3` and `5/9`, hence

`Cov_simple(A_e,A_f)=(4/81) Cov_multigraph(e,f)`.

Thus the source simple problem is equivalent to the unit loopless-multigraph problem. In an edge-minimal loopless counterexample `(M,e,f)`, deletion and contraction of **every** third edge `g` are smaller unit instances, so

`Cov(e,g)Cov(f,g)/Var(g) >= Cov(e,f)>0`,

or `rho_eg rho_fg >= rho_ef=:a>0` for every `g`.

Consequences proved in the full report:

1. The positive-covariance graph on labelled edges of `M` is a matching. In particular every third edge is strictly negatively correlated with both bad marks.
2. If `{e,f}` is an entire two-edge cut, with `N=Z_LZ_R` and `B=C_LC_R`, then exactly
   `Z_e Z_f-Z Z_ef = N B >=0`.
   Hence `M-{e,f}` is connected and `M` has no coloop.
3. Applying the partner triad formula to a bridge cut of `G0=M-{e,f}` shows each bridge is crossed by exactly one of `e,f`. Therefore the bridge-block tree of `G0` is the edge-disjoint union of the marked endpoint paths `P_e` and `P_f`; if both are nonempty they meet in exactly one block.
4. Applying the lead rank-homogeneous complete-log-concavity row budget to **all** third edges gives
   `T_e+T_f+a^2+(m-2)a<1`,
   with `T_h=Cov(X_h,|F|)^2/((R-E|F|)p_h(1-p_h))`.

First remaining implication: `ALL-EDGE-MATCHING-INCONSISTENCY / BRIDGE-PATH-CLOSURE-v1` — rule out an actual loopless graphic law satisfying the all-edge Simpson product bounds, global positive matching, connected `M-{e,f}`, the two-path bridge skeleton, and the rank budget; or construct a genuine graph realizing all constraints and positive `Cov(e,f)`.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B01/B01-20260922T090454Z-forest-r17/report.md`.
Regression: `theta3_cut2_check.py` / `.out`, ending `THETA3_AND_CUT2_REGRESSION_PASS`.
