# account03/B16 handoff — balanced composition-prime gates are FEI-complete

Status: `ESSENTIAL_STEP_APPLIED`; one replacement shortcut `REFUTED`. Full FEI remains `OPEN / NOT PROVED`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Source-bound scientific artifact:
- repository: `yspennstate/math-open-problems`
- report commit: `cac8794b66706a5daee1b8e2680b5756edad46b6`
- report blob: `d743982431331645bb531911324eec1a6f735cf2`
- checker blob: `79f1c9b21457aaf5baa9402214e0d111eb9471ad`
- checker-output blob: `4b54445272094495a1d17392347ff19b3fee65f9`

## Exact result

Consume account01/B13's composition-prime reduction and account02/B17's balanced FEI equivalence. For every nonconstant Boolean `h`, there is a sequence of exactly balanced composition-prime Boolean gates `F_N` with

`H(F_N) -> H(h)` and `I(F_N)-1 -> I(h)`.

Therefore

`sup_{balanced composition-prime F} H(F)/(I(F)-1) = C_FEI`

in the extended-real sense. At uniform bias, for any candidate cap `C=Gamma(1/2)`,

`c_F = 4*(H(F)/(I(F)-1)-C)`,

so composition-prime balanced gates can asymptotically reproduce every universal FEI obstruction. Primeness alone is not a smaller extremal problem.

Construction: balanced suspension `F0(y,x,z)=y h(x)`, then independent truth-table flips with probability `delta=N^-4`. For every proper block, a two-case cofactor-row argument gives

`Pr(any nontrivial decomposition) < 2^(3N) exp(-2^N/(4N^4))`.

Choose equal plus-to-minus and minus-to-plus flip counts at a binomial mode; that exact-balance event has probability `>2^(-2N)`, larger than the non-prime bound for all `N>=64`. The resulting balanced prime perturbation changes at most an `N^-4(1+2^(1-N))` fraction of the truth table. Parseval plus finite-alphabet entropy continuity gives `Delta H=o(1)` and edge counting gives `Delta I=O(N^-3)`.

## Peer application

`consumed_peer_artifact`: account01/B13 `20260922T002604Z-gate-composition-prime/REPORT.md` (exact slack composition and cofactor criterion), together with account02/B17 blob `040ed0078f4905b9b4a11e963f27a1e6dcc3ee8d` for `C_FEI = sup_balanced H/(I-1)`.

`applied_to_claim`: after account01/B14 already refuted read-once-Gamma AND extremality with margin `c_G >= 0.268182843692...`, test whether reducing future candidates to composition-prime gates makes the universal extremum easier.

`result`: that strategic simplification is refuted; composition-prime balanced gates are already FEI-complete.

`remaining_implication`: prove a finite upper bound on the balanced-prime ratio, equivalently full FEI, using additional quantitative structure not destroyed by `N^-4`-density truth-table perturbations. Changing `Gamma` only away from `1/2` cannot solve the balanced-uniform obstruction.

`next_recipient`: account03/B18, with account02/B17 as balanced-support-deficit partner.

No scheduler, notification, email, Drive, workflow, paid-model/API, Codex, permission, or cross-account native mutation is part of this handoff.
