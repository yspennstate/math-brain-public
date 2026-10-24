# FOREST handoff — account01/B03 — full-radius overlap reconnection

Run `20260922T052013Z-b03-forest-r11-d011c5`; outcome **ESSENTIAL_STEP_APPLIED**; parent FOREST remains **OPEN**; context `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B03/20260922T052013Z-b03-forest-r11-d011c5/report.md`.

Consumed lead account01/B01 `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, blob `4cee205cb7d254caf785692838111988a0b8a155`, retaining its withdrawal of the fixed-graph Cocks bridge. Named OTHER-account result applied: partner account02/B01 K4 response synthesis, blob `082008f849c3c0f0ab93356e9d6116f21531386d`; also consumed the partner's newer two-cut influence budget blob `6e4a41368ef6c32c2a9a0634ab1096dda8c85553`.

## New full-radius reconnection existence lemma

Let `G0=G-{e,f}`, `N` all forests of `G0`, `A` the e-addable forests, `B` the f-addable forests, and `D` the jointly-addable forests. Exact cancellation gives

`Delta>=0  <=>  |(N\A) x D| <= |A x (B\D)|`.

For every domain pair `(F,H) in (N\A) x D`, take the unique e-path `P` in `F`, contract H-components, and loop-erase the induced quotient walk to a simple path `R` joining the quotient endpoints of e. Let `S` be the corresponding crossing edges of `P`.

- If the two quotient endpoints of f are not both on `R`, transfer all of `S`: `F'=F\S in A` and `H'=H union S in B\D` because e is blocked in `H'` while f is addable.
- If both quotient endpoints of f lie on `R`, delete from `S` one edge `s` on their subpath and transfer `S\{s}`. Then e and f are each addable to `H'`, but they connect the same two components, so `H'` is exactly an overlap-cycle state `Q subset B\D`. The transferred set is nonempty because otherwise quotient e and f would be parallel, contradicting `H in D`.

This covers disconnected H, adjacent marks and repeated H-components along the original path. It proves every residual domain pair has a legal reconnection target. It does **not** prove the count inequality: the missing step is Hall/fiber-capacity control.

## Bounded-radius no-go on general graphs

A universal radius-two transfer-only rule is false. On vertices `a,b,x,y,c,d`, with marked `e=ab`, `f=cd` and base edges only `a-x,x-y,y-b`, take F to be the full 3-edge path and H empty. This is a residual domain pair. Transferring at most two available base edges cannot block e or f in the second coordinate, so no target in `B\D` is reached; transferring the full length-3 quotient path succeeds. This does not refute the separate K_n radius-two Hall candidate.

## Partner K4 synthesis gate sharpened

For a 3-terminal response `v=(d,a,b,c,t)`, put `tau=dt-(ab+ac+bc)` and `sigma=abc-tau*t`. Account02/B01's exact K4 synthesis is equivalent to `tau,sigma>=0`. For an edge activity w, `v(w)=v0+w v1` gives

`tau(w)=tau0+P_tau*w+tau1*w^2`,

where `P_tau=d0*t1+d1*t0-(a0*b1+a1*b0+a0*c1+a1*c0+b0*c1+b1*c0)`, and

`sigma(w)=sigma0+S1*w+S2*w^2+sigma1*w^3`.

Exact exhaustive regression for every labelled simple graph on n=3,...,7 (2,131,016 graphs; 22,271,180 graph/present-edge splits) found zero failures of `tau>=0`, `sigma>=0`, `P_tau>=0`, or `sigma'(w)>=0` for all w>=0. A stronger coefficientwise route is false: `S2<0` in 41,544 instances; smallest witness has edges `{04,05,13,15,23,25,34}`, g=15, and `sigma(w)=162+536w-30w^2+92w^3`.

Recommended next step for this slot: prove a Hall/weighted-shadow bound for the variable-radius quotient-path reconnection, stratified by path length and the interval positions of f's endpoints. Do not impose a uniform radius bound on sparse graphs.
