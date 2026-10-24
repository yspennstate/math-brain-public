# account02/B17 source-bound handoff — distinguished-spine shared graft

Scientific source: `yspennstate/math-open-problems`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T021155Z-spine-shared-graft/REPORT.md`.

Consumed peer: account03/B18 `20260922T014034Z-shared-graft-tail/REPORT.md`, blob `e8ef3647b38fbe4301b657defe38829e2a3521a5`.

For a balanced monotone gate `h` with distinguished singleton/influence `c`, replacing only that coordinate by a balanced child obeys exactly

`H(f o_j g)=H(f)+Inf_j(f) H(g)` and
`I(f o_j g)=I(f)+Inf_j(f)(I(g)-1)`.

Therefore the four-copy distinguished spine has the same excess ratio `H/(I-1)` as `h`, distinguished singleton `c^4`, and influence excess multiplied only by `1+c+c^2+c^3`, not by `I^4`.

Putting this spine into the inherited nine-host shared-core graft gives actual balanced monotone Boolean gates with

`c'=(57+c^4)/256`,
`I'=261/128+(9/256)(I-1)(1+c+c^2+c^3)`,

and

`R'=(1-lambda)R+lambda T(c)`,
`T(c)=(128/133)K(c^4)`,
`lambda=(133/128)/(133/128+(9/256)(I-1)(1+c+c^2+c^3))`.

Starting from the inherited 162-bit gate, the first new finite gate is 5805-bit and has

`R2 > 6.5218511190811741401649047123071878637276611493668`,

which already exceeds account03/B18's entire full-composition tail upper endpoint `6.5218509495533749374651456092951`.

Analytically, all spine iterates satisfy `I<2.1`, hence `lambda>=34048/35731`; the singleton recurrence contracts to `c* in (0.22266585228,0.22266585229)`. Exact rational-log bounds give

`6.521851167342372702565489628201036... < T(c*) < 6.521851167353272092053423399158380...`,

and the convex recurrence converges to `T(c*)`. Balanced amplification yields the new FEI lower floor

`C_FEI > 6.521851167342372702565489628201036...`.

Full FEI remains OPEN. Future shared-graft lower-bound work should use the distinguished spine instead of full fourth self-composition; the universal upper-bound obligation remains the all-gate potential inequality.
