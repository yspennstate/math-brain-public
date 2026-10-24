# FEI handoff — account03/B04 -> account01/B01

Result: `FEI-B04-POINCARE-NEARZERO-TRICHOTOMY-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Full FEI: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Source-bound input

Consumed the completed account02/B12 selector-debit report at commit `4ccd51ad517f425a529daa52c3352905b86ea69d`, using only its exact selector/disagreement identities and not its now-refuted numerical candidate. No completed compatible FEI result from newly assigned partner `account04/B04` was present at the fresh snapshot; the worker proceeded without waiting, as the owner order permits.

Canonical new mathematics is in `yspennstate/math-open-problems`:
`proofnet24/P03-fei/fleet-2026-09-22/account03/B04/20260922T103904Z-nearzero-poincare-trichotomy/REPORT.md`.

## Exact delta

For a Boolean gate split on selector bias `s`, with child Poincare gaps `W0,W1`, disagreement `d`, and child output-probability difference `Delta=q1-q0`,

`W=(1-s)W0+sW1+s(1-s)[d-Delta^2]`.

Since `|Delta|<=d`, the local defect satisfies `d-Delta^2 >= d(1-d)`. Thus under full-support product bias `W=0` iff the gate is constant or a literal/negated literal.

If `W<=epsilon` and `s in [alpha,1-alpha]`, then

`min(d,1-d) <= 2 epsilon/[alpha(1-alpha)]`.

In the near-dictator branch,

`1-|Delta| <= 3 epsilon/[alpha(1-alpha)]`,

so the two child output laws are quantitatively close to opposite constants. The first nonzero local denominator is `s(1-s)d+O(d^2)` on the irrelevant branch and exactly `s(1-s)(2 tau-e-tau^2)` on the dictator branch, where `e=1-d` and `tau=1-|Delta|`.

## Boundary warning that changes the proof obligation

Near-zero `W` has a third mechanism: selector-bias collapse. For genuine XOR with first bias `p` fixed and selector bias `s->0`,

`W=s(1-s)V_p -> 0`

while `d-Delta^2=V_p` stays order one. Its exact gate-margin quotient is

`-[Gamma(p)+Gamma(s)-Gamma(p+s-2ps)]/[s(1-s)V_p]`.

Therefore a universal near-zero quotient proof must explicitly control boundary contractions/one-sided regularity; it cannot infer local Poincare equality merely from `W` being small.

For the quadratic safe direction `c u(1-u)`, the source identity gives `D -> D+cW`, so on `W>0` the quotient `-D/W` translates by exactly `-c`; no singularity comes from that direction itself.

## Next unpaid implication

`FEI-B04-BOUNDARY-QUOTIENT-v1`: for the current shaped candidate or another finite-cap potential, prove a uniform upper bound on the boundary-contraction quotient after reducing to the live child, with child defects and selector entropy retained. The interior denominator is now quantitatively classified.

Primary recipient: `account01/B01`. Assigned partner for subsequent B04 work: `account04/B04` when a completed compatible result appears.

No full FEI proof or novelty claim. `full_brain_connected=false`.
