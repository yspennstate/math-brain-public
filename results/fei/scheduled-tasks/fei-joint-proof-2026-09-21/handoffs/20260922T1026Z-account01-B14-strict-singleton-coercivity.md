# FEI handoff — account01/B14 strict singleton coercivity

**Status:** `ESSENTIAL_STEP_APPLIED`; **full FEI remains OPEN**.  
**Scientific source:** `yspennstate/math-open-problems` commit `730731281a24e70b01b4021a90ff758575414db1`, report blob `adca61a48bafc98053c66a939f41b742319f4e81`, path `proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T101243Z-strict-singleton-coercivity/REPORT.md`.

## Exact consumed peer

Applied account04/B17 `20260922T092422Z-biased-booleanity-gap`, creation commit `603b35e74227d1c2d8ee34c0c527c439c686e30b`, report blob `f7a069e0e44ab05ff574807e72973c131c960ca8`.  Its exact sparse two-flip family has `q_k=2^(2-k)` and `I-1=(k-2)q_k`; the single full-active Booleanity equation loses influence-relative strength on that family.  Also used the exact account02/B12 Bernstein floor `r0=1999313322941/16492674416640000000` from checker blob `7a1b97039601ea02aeb634df84ba974c56228cf3`, output blob `2f589b293d3525f70e1843c2a6eefdebd5be659b`.

## New theorem

For the universally safe direction

`eta(p)=phi(1-2p)`, `phi(m)=1-m^4-(113009/5000000)(1-m^2)^3`,

reveal any genuine active original coordinate with bias `t`.  With child means `a,b`, `delta=Pr(G0!=G1)`, `d=|a-b|`, and `P_+,P_-` the positive/negative pivotal-fiber masses,

`S >= r0*d*t(1-t)*(2-d) + (delta-d/2)*eta(t)`

and equivalently

`S >= 4 r0 t(1-t)|P_+-P_-|(1-|P_+-P_-|) + 2 min(P_+,P_-) eta(t)`.

The local surplus is zero at an interior bias iff that coordinate is pointwise inactive or the entire current gate is exactly that literal (up to sign).  Telescoping over literal restrictions therefore gives the complete global zero set:

`L_eta(G;p)=0` iff `G` is constant/literal/negated literal after deleting dummies.

Hence every genuinely multi-input gate has `L_eta>0` at every interior product bias.

If the effective arity is `m>=2` and every active bias lies in `[rho,1-rho]`, then

`L_eta(G;p) >= 4 r0 rho^m (1-rho)(1-rho^(m-1)) > 0`.

Thus any bounded nonnegative base potential can be repaired on every fixed-arity compact interior bias strip by a finite scaling of `eta`.  A failure of every finite scaling can only escape through growing effective arity and/or a biased boundary.

## Application to peer obstruction

On the exact balanced uniform sparse two-flip family,

`L_eta=(1-epsilon)(I-1)=(1-epsilon)(k-2)2^(2-k)`.

So this physical singleton currency remains exactly influence-relative where the peer's one-equation Booleanity certificate collapses; the sparse-defect obstruction does not refute it.

## Remaining owner-target implication

This is not the requested all-gate extremality theorem.  The first unpaid target-level inequality is the arity/boundary-uniform comparison

`[-D_{Gamma^dagger}(G;p)]_+ <= K L_eta(G;p)`

with one finite dimension-independent `K`, or a genuine Boolean gate/bias sequence for which that ratio diverges.  Such a finite `K` would make `Gamma^dagger+K eta` an all-gate potential and prove FEI.  The new theorem isolates the only possible failure modes but does not close them.

No half-band positive-current estimate, uncharged labels, every-coordinate entropy payment, or finite-test-to-universal inference is used.
