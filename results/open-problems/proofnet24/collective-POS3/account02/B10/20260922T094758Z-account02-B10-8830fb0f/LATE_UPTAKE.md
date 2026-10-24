# Late cross-account uptake — account01/B10 r14

After `REPORT.md` was immutably written, fresh shared-main movement exposed the completed handoff for **account01/B10 r14**, scientific source commit `c77745610cc78470562ef9dfefb383aa553b4c6f`, report blob `6a456462cd7fb38ebc96ded63fbc8682dae2a55d`, path `proofnet24/collective-POS3/account01/B10/20260922T095221Z-b10-pos3-r14/REPORT.md`.

That run independently derives the same canonical two-out / at-most-one-in Hasse gate and additionally identifies, for each outgoing cover `r_i`, the exact full-law row atom

`h_i := Pr(p<q<r_i) = Pr(p<q)+Pr(q<r_i)-1`.

The equality is exact because `p<r_i` is forced, so for the three relative orders of `p,q,r_i` the two complementary tails are precisely `q<p` and `r_i<q`.

Apply this to the notation of the present report. Let

`epsilon=Pr(q<p)<1/3`, `alpha_i=Pr(r_i<q)<1/3`,

and, when the unique reverse cover `s` exists,

`delta=Pr(s<p)`.

The present run proved

`delta < 2 epsilon - 1/3`.

The account01/B10 row identity gives

`h_i = 1-epsilon-alpha_i > 2/3-epsilon`.

Therefore each outgoing heavy row individually dominates the entire reverse reservoir by the strict margin

`h_i-delta > 1-3epsilon > 0`.                                  (A.1)

So the canonical barrier has not only two outgoing Hasse labels versus at most one reverse label; it has two **full-extension row packets**, each strictly larger than the entire exact reverse defect reservoir. Any future literal reset charge must therefore discard positive full-law mass on either outgoing row, unless it changes to a genuinely new noncanonical witness structure or takes an authorized terminal/descent outcome.

This does not yet prove global non-reuse because a later noncanonical gate may recode the same extensions under different witnesses. It sharpens `POS3-CANONICAL-Y-GATE-SPLICE-v1` to the exact question of whether those recodings can preserve both row packets without span descent, balance, or a proper autonomous/ordinal reduction.

Status remains `ESSENTIAL_STEP_APPLIED`; POS3 remains open.
