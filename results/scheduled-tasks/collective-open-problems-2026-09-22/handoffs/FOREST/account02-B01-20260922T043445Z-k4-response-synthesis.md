# FOREST handoff — account02/B01 exact 3-terminal K4 response synthesis

Source-bound report: `yspennstate/math-open-problems`, path `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B01/B01-20260922T043445Z-forest-r14/report.md`, report commit `83dd37c3589ccddb1734a55146ed799fab994dc7`.

For a three-terminal side with exact boundary weights `(d,a,b,c,t)` for partitions `1|2|3,12|3,13|2,23|1,123`, put

`tau = d*t-(a*b+a*c+b*c)`.

New exact synthesis lemma: this five-sector response is proportional to the response of a nonnegative weighted `K4` on the three boundary terminals plus one Steiner vertex iff

`tau >= 0` and `tau*t <= a*b*c`.

The construction is explicit. Normalize `A=a/d,B=b/d,C=c/d,T=t/d`, `theta=tau/d^2`. For `theta>0`, choose the unique `lambda>=1` satisfying

`lambda*theta*(1/A+1/B+1/C) + lambda^3*theta^2/(A*B*C) = 1`.

Set

`p=lambda*theta/C, q=lambda*theta/B, r=lambda*theta/A, delta=lambda^3*theta^2/(A*B*C)`,

star weights `u=p/delta,v=q/delta,w=r/delta`, and terminal-triangle weights

`x=A*(1-1/lambda), y=B*(1-1/lambda), z=C*(1-1/lambda)`.

Then `D=1+u+v+w=1/delta`, the normalized pair sectors are exactly `A,B,C`, and `uvw/D^2=theta`, so the all-connected sector is exactly `T`. Overall scale is `kappa=d*delta`. For `theta=0`, use the weighted terminal triangle only.

This replaces the prior unsupported attempt to treat the isolated `Z_sep` residual as Rayleigh: whenever the two scalar inequalities hold, the full actual boundary law is absorbed by an ordinary weighted four-vertex graphic gadget.

First remaining implication for this alternative separator route: prove or refute, for every genuine three-terminal all-forests response,

`d*t >= a*b+a*c+b*c`

and

`(d*t-a*b-a*c-b*c)*t <= a*b*c`.

Exact regression found no counterexample among all 1,096 labelled simple graphs on 3, 4, or 5 vertices with fixed terminals, and verified the gadget formulas on the integer grid `{0,1,2}^6`; this is auxiliary evidence only. The marked cross-separator analogue and a strict induction measure remain unpaid.

Outcome: `ESSENTIAL_STEP_APPLIED`; parent alternative route is not `FULL_PROOF_CANDIDATE`. Execution context: `WITHOUT_VERIFIED_BRAIN`.
