# FOREST handoff — account03/B01 — r11

Outcome: `ESSENTIAL_STEP_APPLIED`; parent FOREST remains `OPEN`; execution context `WITHOUT_VERIFIED_BRAIN`.

Latest complete lead consumed: account01/B01 handoff blob `4cee205cb7d254caf785692838111988a0b8a155` (`FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`). Named partner consumed and applied: account04/B02 handoff blob `b7dfefb859db57dc5f48f44ddc0026693ac05414`, commit `8aa0b17b6f043c6e90a669429ba38032b9b54775` (K4 Hall/transfer-only obstruction). Also checked account04/B01 exact two-terminal substitution result at commit `686787b589421a290feafda74ea9cd77ca42f5ee`.

New exact theorem: the simple unit two-terminal gadget consisting of one direct terminal edge plus three internally-disjoint length-2 terminal paths has `(D,C)=(27,54)`, hence response `C/D=2`. For any STAR-2 Rayleigh instance, first reset marked-edge activities to 1 (Rayleigh difference is independent of them), then replace each remaining weight-2 edge by this gadget. If `d` edges are replaced, the resulting graph is simple and unit-weight and

`Delta_unit = 27^(2d) Delta_STAR2`.

Therefore unrestricted universal STAR-2 is exactly parent-equivalent to unit FOREST. The broad conditional-disconnection statement is parent-equivalent too (adjoin two isolated terminals). The genuinely useful missing implication is **size-controlled STAR-2** inside the minimal-counterexample induction, not universal STAR-2 under another name. The exact gadget expands an `(n-1)`-vertex contraction to `(n-1)+3d`, so it does not itself close minimality when `d>=1`.

Partner application: account04/B02's K4 witness rules out trying to replace this size expansion by an old union/intersection-preserving or transfer-only Hall injection. The next direct coupling must be size-controlled and permit genuine cross-fiber cut/join moves that can change union/intersection.

Exact finite diagnostics: `(C,D)=(54,27)` and 3,972 small labelled substitution/Rayleigh identities checked with zero failures. Canonical full report: `yspennstate/math-open-problems` commit `7690480382f6fe01822dde20492372714b594432` under the assigned account03/B01 FOREST archive.
