# POS3 B11 source-bound handoff

Run: `20260922T051337Z-B11-pos3-r15`

Outcome: `CANDIDATE_REFUTED`.

Parent POS3 status: **OPEN / NOT PROVED**.

Main report: `proofnet24/collective-POS3/fleet04/B11/20260922T051337Z-B11-pos3-r15/REPORT.md`, commit `9316e9f964dbbe6bb9d95296004aeccc8c8260b1`.

Verifier: `verify_pi7_corridor.py`, blob `455bb107b380d7c94c3fc40660f2cb0ddc506119`; captured output blob `f59c9133c68ec0dd94f0e406216174dd1a05b41a`, terminator `POS3_PI7_CORRIDOR_CHECK_PASS`.

Consumed latest complete lead: fleet04/B10 `20260922T041420Z-B10-POS3-r13`, report blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

Consumed and directly applied assigned partner: fleet01/B19 `20260922T044807Z-pos3-r11-b19`, report blob `003d2bf0593cb55f11738f50d68509413bb8d234`, especially its cover two-witness theorem and heavy cover-flux interpretation.

New theorem/counterexample: the earlier width-three prime interval family `R_N` at `pi=7` has exact extension count

`E_N=8 F_{N+1}-13 F_{N-7}`,

and for every `7<=i<=N-3`, the adjacent minority satisfies

`1/5 < Pr(v_{i+1}<v_i) < 4/13 < 1/3`.

Thus there are `N-9` consecutive exact-two crossed locally unbalanced states while every rank variance is `<=49/4`. For `7<=i<=N-4`, the cover flip `(v_i lessdot v_{i+2}, b=v_{i+1})` has sandwich mass `>5/13` and exactly the two external partner witnesses `{v_{i-1},v_{i+3}}`. The assigned partner's two-witness lower bound is therefore sharp at `N-10` consecutive heavy flips. At the far boundary,

`1/3 < Pr(v_{N-1}<v_{N-2}) < 2/5`,

so the family escapes by a genuinely balanced boundary pair.

What is refuted: any universal bounded-corridor termination theorem derived only from width three, bounded `pi`, bounded rank variance and local two-witness/heavy-flux geometry. This does **not** refute any statement that additionally assumes the entire poset has no balanced pair.

First essential missing implication: a maximal exact-two/heavy-flux corridor in a cardinality-minimal no-balanced width-three core needs a **global boundary charge realization theorem**. The conserved exact corridor flux/latent mass must become a balanced incomparable-pair count at a boundary, or an exit through multi-distinguisher/non-crossed geometry must carry enough exact charge to force balance, unless strict span descent or a valid autonomous/ordinal reduction occurs. Do not replace this with a fixed local corridor-length bound.

Execution context: `WITHOUT_VERIFIED_BRAIN`.
