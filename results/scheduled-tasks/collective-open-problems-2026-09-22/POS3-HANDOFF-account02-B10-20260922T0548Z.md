# POS3 handoff — account02/B10 — 20260922T0548Z

Outcome: `ESSENTIAL_STEP_APPLIED`  
Parent POS3 status: `OPEN / NOT PROVED`  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Complete sources consumed

- campaign lead account04/B10: `proofnet24/collective-POS3/account04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md` — bridged branch contains a unique cover carrying `Pr(x<a<y)>1/3`, and a no-balanced candidate forces at least two external witness channels.
- named partner account03/B11: `proofnet24/collective-POS3/account03/B11/20260922T044349Z-account03-B11-pos3-r11/REPORT.md`, blob `337b660656cf3df6fc194a4be79b4801bfc99b97` — amplified outer pair `(d,u)` with `Pr(d<u)>5/6`; its mandatory third distinguisher gives span descent, a second canonical blocker, or a shadow Hasse sandwich `>1/3`.
- compatible account04/B19: `proofnet24/collective-POS3/account04/B19/B19-20260922T041629Z-auto11/REPORT.md` — source of the crossed outer amplification.

A newer account03/B11 intermediate output appeared on shared main after the derivation (`20260922T055219Z-middle-heavy-fibre-output.json`), but no newer complete partner report was consumed or promoted in this handoff.

## New exact theorem

In the partner's amplified outer branch let `d||u`, `Pr(d<u)>5/6`, and

`D=Pred(u)\Pred(d)`, `U=Succ(d)\Succ(u)`.

If a **second lower canonical blocker** `ell in Max(D)` occurs, then `ell lessdot u` and `ell||d`. If strict strong-majority span descent inside `(d,u)` is excluded, one must have `ell prec_* d`, so `Pr(ell<d)>2/3`. Since `ell<u` is forced,

`Pr(ell<d<u) = Pr(ell<d) + Pr(d<u) - 1 > 1/2`.

Order-dually, a second upper canonical blocker `r in Min(U)` satisfies `d lessdot r`, `r||u`; after span descent is excluded,

`Pr(d<u<r) = Pr(d<u) + Pr(u<r) - 1 > 1/2`.

Thus the partner's trichotomy sharpens to:

1. strong-majority span descent; or
2. a canonical second-blocker Hasse sandwich with full-extension mass `>1/2`; or
3. a shadow Hasse sandwich with mass `>1/3`.

No deletion/projection law is uniformized.

## Exact adversarial calibration

A width-three 9-point poset with reduction

`0<6, 0<7, 1<4, 2<3, 2<7, 3<6, 4<5, 5<7, 6<8`

has `353` linear extensions. For `(d,u,x,ell,y)=(3,7,5,0,6)`,

`Max(Pred(7)\Pred(3))={0,5}`,
`Min(Succ(3)\Succ(7))={6}`,

and

`Pr(3<7)=333/353`, `Pr(0<3)=242/353`, `Pr(0<3<7)=222/353>1/2`.

Both adjacent incomparable endpoint pairs are still strongly oriented; the poset has a balanced escape pair `Pr(5<6)=200/353`. Hence a superheavy sandwich alone does **not** force local endpoint balance. The next proof must use simultaneous witness/global width-three structure.

Verifier terminator: `POS3_SECOND_BLOCKER_SUPERHEAVY_CHECK_PASS`.

## First unpaid implication

`POS3-SUPERHEAVY-RECYCLING-v1`: in a cardinality-minimal width-three no-balanced candidate, couple at least two witness channels and prove that a canonical second-blocker sandwich `>1/2`, or a bridge/shadow cover sandwich `>1/3`, cannot propagate to the next canonical layer without a balanced pair, strict span descent, a four-antichain, or a proper autonomous/ordinal reduction.

Complete proof and exact verifier/output are in `proofnet24/collective-POS3/account02/B10/20260922T0548Z-b10-pos3-auto11/`.
