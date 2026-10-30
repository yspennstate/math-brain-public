# B17 source-bound FEI handoff — distinguished-spine shared graft

Source run: `fleet02/B17/20260922T021155Z-spine-shared-graft/REPORT.md`.

Consumed other-account source: fleet03/B18
`20260922T014034Z-shared-graft-tail/REPORT.md`, blob
`e8ef3647b38fbe4301b657defe38829e2a3521a5`.

For a balanced monotone gate `h` with distinguished singleton/influence `c`,
one-coordinate substitution gives exactly

`H(f o_j g)=H(f)+Inf_j(f) H(g)` and
`I(f o_j g)=I(f)+Inf_j(f)(I(g)-1)`.

Therefore the 4-copy distinguished spine `P4(h)` has
`H(P4)=H(h)(1+c+c^2+c^3)`,
`I(P4)-1=(I(h)-1)(1+c+c^2+c^3)`,
the same excess ratio `H/(I-1)`, and distinguished singleton `c^4`.

Feeding `P4(h)` into the inherited nine-host shared-core transform yields the
actual-Boolean recurrence

`c'=(57+c^4)/256`,
`I'=261/128+(9/256)(I-1)(1+c+c^2+c^3)`,

and, with `R=H/(I-1)`, `T(c)=(128/133)K(c^4)`,

`R'=(1-lambda)R+lambda T(c)`,

`lambda=(133/128)/(133/128+(9/256)(I-1)(1+c+c^2+c^3))`.

Starting from the inherited 162-bit `F1`, the first spine step is an actual
5805-bit balanced monotone gate and satisfies

`R2 > 6.5218511190811741401649047123071878637276611493668`,

already above the B-lead full-composition **entire tail upper endpoint**
`6.5218509495533749374651456092951`.

Moreover `I_t<2.1` for every spine iteration, hence
`lambda_t >= 34048/35731 > .9528`.  The singleton map is a contraction and its
fixed point lies in `[0.22266585228,0.22266585229]`.  Exact rational-log
enclosures plus the inherited `|K'|<19` bound give

`6.521851167342372702565489628201036... < T(c*) <
 6.521851167353272092053423399158380...`.

The convex recurrence therefore converges to `T(c*)`.  Balanced amplification
of each finite gate gives the new certified FEI lower floor

`C_FEI > 6.521851167342372702565489628201036...`.

This is a lower-bound/adversarial construction only; full FEI is OPEN.
Use this recurrence instead of the full fourth self-composition recurrence in
future shared-graft lower-bound work.  The remaining universal proof obligation
is still a finite-center all-gate potential (or equivalent dimension-independent
upper bound) surviving this family.
