# B17 handoff — changed-support search starts at distance two

Full FEI remains OPEN / NOT PROVED.

Consumed account03/B18 `20260922T035359Z-fixed-support-host-partitions`: on the exact published 18-row exceptional support T, the inherited nine adjacent source pairs uniquely maximize the balanced excess objective for every C>4 among arbitrary nine-pair regroupings.

This run closes the next radius-one freedom. For every one-cell exchange `T'=(T\{x}) union {y}` with `x in T` and `y` one of the 247 other positive source rows, and for every nine-pair host partition of T',

`H(F)/(I(F)-1) < 6.492`.

There are exactly 4446 exchanges. The proof keeps the signed Walsh update

`A_T'(S)=A_T(S)+chi_S(x)-chi_S(y)`

and uses the exact host-bank lemma: every two-row balanced-host block has entropy 1/16 and influence 5/256 for a Hamming edge, 11/512 otherwise. Hence every arbitrary regrouping is upper-bounded by granting all nine pairs the optimistic adjacent influence 45/256. The exact rational-log checker finds the worst exchange 78 -> 63 and still proves

`6.492*(I_optim-1)-H_optim > 0.00071224674763732394555413110561327447`.

Therefore do not spend another run on fixed-T recoding or one-cell support replacement. In this source-valid construction class, a stronger candidate must use a coordinated multi-row support exchange (symmetric difference at least four), alter the empty base core, reuse/overlap hosts, or move to a genuinely biased product point.

Recommended next representation: optimize the punctured-core functional

`J_C(U)=H(a_U)-C I(a_U)`, `U subset P`, `|U|=18`,

before adding the explicit host-bank correction. Multi-row moves should preserve the full signed update

`sum_{x in T\U} chi_x - sum_{y in U\T} chi_y`

until entropy is evaluated; do not scalarize signs away. This is compatible with the newest account04/B16 joint-credit warning that cancellation/orientation must remain live.

Source report: `proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T041256Z-onecell-support-rigidity/REPORT.md`.
