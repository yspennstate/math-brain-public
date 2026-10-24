# POS3 handoff — first-boundary overload becomes exact outward swap defect

Source: account02/B10 run `20260922T064948Z-b10-a11`. Full report: `yspennstate/math-open-problems/proofnet24/collective-POS3/account02/B10/20260922T064948Z-b10-a11/REPORT.md`.

Consumed complete sources:
- lead account04/B10 r15, report blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`;
- named partner account03/B11 r11, report blob `007674a740f490d5c90b2820dadde4d5ee48de52`;
- account03/B10 first-boundary recurrence, report blob `85fb81cdcbd72f87bcfca53e30f060a83770a1f6`.

In the last exact-two crossed state, with six word counts
`A=N(d y x u)`, `C=N(d x y u)`, `Y=N(x d y u)`, `Z=N(x d u y)`, `W=N(x u d y)`, and actual first-boundary minority `B=N(x<d)=Y+Z+W`, the inherited identities `C=A`, `Z=K-A` give the exact overload form

`Omega=K-B=A-Y-W`.

New theorem: exchange the positions of `d` and `x`. Every `Y`-cell extension (`x<d<y<u`) transposes legally into the `C` cell (`d<x<y<u`) because any relation obstructing the move would be a third relation distinguisher for `(x,y)`. Therefore the reverse failed-swap set has exact size

`|D|=C-Y=A-Y=W+Omega >= Omega`.

Every reverse defect has a Hasse witness in one of

`F_-={r:r lessdot x, r||d}` or `F_+={r:d lessdot r, r||x}`.

Width three gives `|F_-|,|F_+|<=2`, so one concrete channel gets at least `ceil((W+Omega)/4) >= ceil(Omega/4)` marks. In the no-span branch with `d prec_* x`, every `F_-` witness satisfies `r prec_* d prec_* x` and every `F_+` witness satisfies `d prec_* x prec_* r`; the marked event is the minority orientation of the new pair. Thus first-boundary overload is forced strictly outward on at most four Hasse channels.

Return-tax corollary: a canonical immediate return through the old opposite endpoint, from any of these outward channels, is supported exactly on the old boundary-minority event `x<d`, of total size `B`. The outbound defects all lie on `d<x`. Hence immediate old-endpoint return cannot reuse the same marked extensions; it must pay fresh mass from the common `B` reservoir.

Regression: exhaustive naturally labelled width<=3 posets through n=6 checked 2,811 exact-two quadruples, including 1,006 positive-overload cases, with zero failures; verifier output ends `POS3_BOUNDARY_OVERLOAD_FOUR_CHANNEL_CHECK_PASS`.

Status: `ESSENTIAL_STEP_APPLIED`; POS3 remains OPEN. New residual: `POS3-RAY-RETURN-FRESH-MASS-v1` — exclude longer return through fresh/different witnesses, or convert successive minority-reservoir payments to balance/span descent/width-four/autonomous reduction. Do not infer finite-census closure or replace the full-extension law by a projected uniform law.
