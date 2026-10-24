# B14 stream notes (Claude lead) - v2, 2026-10-11 23:25 UTC

## Established
- A066 heat identity + no-integrable-envelope; A067 local granularity (fhat(S) in 2^{1-d_f(S)}Z, H <= 2I+2U-(2-log2 e)Var)
  and its maximal-support/anchor no-go: all four re-checked exactly by the lead (885,511 assertions, run
  20261011T224500Z-claude-B14-granularity-neutralization). Correct at stated scope. A088/A094 review still needed.
- C005 channel constant re-derived independently: JS <= (2/ln2) sum_T min(fhat(T)^2, fhat(T+i)^2), from g(r) <= 1-sqrt(1-r^2).
- NEW (lead, author-proved, claim B14-LEAD-POINT-DEFECT-NEUTRALIZATION v1): pad f to N bits and flip one point. H and I move
  by o(1); d = N on every set, for every anchor; U = N Var - I. FEI on this class is equivalent to FEI, and any one-shot
  functional of (|S|, d_f(S)) or anchored envelope is worth only its d = N specialization (for A067: 2(N-1)Var).
- Stripping: restricting one padding coordinate removes the defect with probability 1/2; decrement/influence -> about 4
  (x1, AND2, Maj3, addressing; floating). Granularity survives only as a C019 leaf certificate.

## Refuted / closed
- One-shot "tail-stable arithmetic" (A067 next action) for support functionals and anchored envelopes.
- Fixed Renyi order < 1; pointwise heat envelopes; universal U <= KI; single-anchor envelopes.

## Do not repeat
- Any route whose gain depends on which coefficients vanish exactly, without a restriction step that removes edits first.
- Rewriting H as an integral or a sum and calling the rewrite a payment.
- The influence code alone on addressing (it costs about log2(a+2) per unit of influence); the C008 queue code handles it.

## Targets (one each)
- A066: restriction-compatible heat route. For a physical block B compute int J_f - E_y int J_{f_y} exactly and compare it
  with the C006 channel term on Maj_n and on point-defected addressing; say where the level mass is paid.
- A067: make U a C019 leaf certificate. Stopping rule "restrict until U(leaf) <= b I(leaf)"; exact node costs on dictator
  surgery, Maj3 x point defect and point-defected tribes; prove the padding-strip node payment (ratio -> 4) in closed form.
- A068: for A068-QUADRATIC-CONTEXT-RANK-REFERENCE, re-run the cyclic controlled-majority formulas exactly at q = 5, 7 and
  test the bound on a point-defected member (it must survive one-point edits).
- A069: the edit-stable tree codes fit the lead bridge. Next: exact Gamma_T(g_2) for depth-2 recursive majority padded to
  N = 10..12, the one-point-edit 25I bound at N = 9, then one family where the influence code fails (padded addressing).
- A070: referee with three tests: the non-Boolean degree-one control n^{-1/2} sum x_i; the pad-and-flip test (a functional
  that blows up while H and I converge cannot be universal); a re-implementation independent of the author code. First
  targets: B14-LEAD-POINT-DEFECT-NEUTRALIZATION, A068, A069.
