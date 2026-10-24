# FOREST B20 handoff — source-invalid lead closure; exact Simpson debt

Run: `20260922T022012Z-b20-forest-r11`  
Outcome: `CANDIDATE_REFUTED` for the current lead's global closure as written; parent FOREST remains `OPEN`.  
Authoritative report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B20/20260922T022012Z-b20-forest-r11/report.md`.

## What changed

The account01/B01 unit-weight `K_n` Hermite theorem survives. The global inference

`unit pNC on K_n -> M(K_n) independence correlated for all positive weights`

is not source-secure. Semple--Welsh define independence correlation at all positive weights and explicitly distinguish it from the unit graph conjecture; their weighted minor closure applies only after independence correlation is known. Later account02/B02 independently reached the same correction.

A sufficient corrected bridge is all-positive-weight Rayleigh on every `K_n`; sparse simple graphs then follow by sending the missing-edge weights to zero. This bridge contains the original target at its boundary, so it is not a routine consequence of the unit complete-graph theorem.

## New exact theorem

For distinct `e,f,g`, freeze all activities except `y_g=t` and write

`P=A+tB`, `P_e=Ae+tBe`, `P_f=Af+tBf`, `P_ef=Aef+tBef`.

Let

`d0=Ae*Af-A*Aef`, `d1=Be*Bf-B*Bef`,
`ce=Ae*B-A*Be`, `cf=Af*B-A*Bf`.

Then

`R_ef(t)=d0+m t+d1 t^2`,

with

`A B m=B^2 d0+A^2 d1-ce cf`.

If `d0,d1>=0`, then `R_ef(t)>=0` for every `t>0` iff

`ce cf <= (B sqrt(d0)+A sqrt(d1))^2`.

At a unit violating parent (`t=1`) one necessarily has the stronger debt

`ce cf > (A+B)(B d0+A d1)`.

This is `FOREST-QUADRATIC-SIMPSON-BRIDGE-20260922`.

## Partner regression

Apply account04/B03's exact local-cone witness: `A=24`, `B=7`, `d0=4`, `d1=1`, `ce=cf=46`. Then

`ce*cf=2116 > 1612=(A+B)(B d0+A d1) > 1444=(B sqrt(d0)+A sqrt(d1))^2`.

Thus the partner witness violates exactly the new quantitative barrier. Full support and local sign/minor constraints cannot force it; a graph-global compatibility law is mandatory.

## Next mathematical action

Combine the prior exact path-cut flux identities `FOREST-PATH-CUT-FLUX-20260922` with the unit debt

`R_eg R_fg > (A+B)(B d0+A d1)`

for every third edge in a minimal counterexample. Seek a graph-global summation/transport inequality paying these simultaneous debts without a graph-size factor. Keep the account04/B03 witness as a mandatory local-only regression.

Brain status: `WITHOUT_VERIFIED_BRAIN`. No full-proof or novelty claim.
