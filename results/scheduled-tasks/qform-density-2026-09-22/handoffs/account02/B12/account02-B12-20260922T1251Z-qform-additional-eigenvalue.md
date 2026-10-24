# account02/B12 handoff — arbitrary same-sign codimension-one spectrum

Status: `PROVED_SUPPORTING_THEOREM / TARGET_LEVEL_SUBCLASS / FULL_TARGET_OPEN`.

Canonical mathematics: `yspennstate/math-open-problems@5924039504a3f27bdfa9079c4d054422a26baaf2:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/account02-B12-20260922T1251Z-qform-additional-eigenvalue/REPORT.md`.

Consumed partner: `account03/B12`, `yspennstate/math-open-problems@08f387da860f00c13f30de170286a82eb13108e1:proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/account03-B12-20260922T114435Z-349dfcff7c/REPORT.md`. Consumed local pair/triple source: `yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8:qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.

## New theorem

For a symmetric `4 x 4` block `B` with three eigenvalues all `<=-L` (or all `>=L`) and completely arbitrary fourth eigenvalue, independent density-`<=1` coordinates plus arbitrary affine tilt have output density

`||p||_infinity <= C_same/L < 24.193/L`, 

where

`C_same=max{pi sqrt(1000/17), (2000/949)(2 pi+3 sqrt(3))}`.

The key dichotomy uses `c2=17/1000`, `c3=949/2000`, with `3c2+2c3=1`. If no principal pair is definite with determinant at least `c2 L^2`, then **every** principal triple has `sigma_min >= c3 L`. Proof: after scaling and ordering, interlacing gives two triple eigenvalues `-x,-y` with `x,y>=1`; the triple's `e2` is the sum of its three principal pair determinants and hence `<3c2`, while `|z|<c3` would force `e2=xy-z(x+y)>=1-2c3=3c2`, contradiction.

High-dimensional consequence: if at least `n-1` eigenvalues of `A` are on one side of the gap (`<=-L` or `>=L`), with the remaining eigenvalue arbitrary in sign and magnitude, then the same `<24.193/L` density bound holds. Choose any four original coordinates; interlacing forces the selected block to have three same-sign large eigenvalues, and condition all other original coordinates. This removes the preceding equal-eigenvalue/rank-one and one-percent-cluster hypotheses.

## Full-target gap

The owner hypothesis supplies only three large eigendirections, not `n-1`; diffuse rank-three projectors prevent extraction of one uniformly good fixed coordinate triple. Mixed-sign `[[0,I_2],[I_2,0]]` also shows the pair/triple mechanism alone cannot cover all signatures (all principal triples singular and no definite pair), although a separate multi-pivot theorem handles that example. The next bridge must aggregate complementary local smoothers without paying a reciprocal single-minor loss.

Corrections consumed before publication: `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`. None challenges this theorem.
