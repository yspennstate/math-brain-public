# fleet02/B01 r45 — early checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full conjecture OPEN.
Run: `20260923T150414Z-fleet02-B01-qform-r45`.

First unpaid implication attacked: `QFORM-N3-TWO-BY-TWO-HEAVY-VOLUME-ROUTING-v1` from the preceding B01 handoff.

Fresh source pins already read:
- owner control/main at start: `yspennstate/math-research-brain@fd81539dba2a07d187f5df4099b0e1205c995cc5`, control revision `2026-09-22.15`;
- required Claude base: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`;
- compatible current state observed at `yspennstate/math-open-problems@f244f8aa9c088839b59e33c57f200a3aa18ca7c8`;
- preceding B01 r44 report: `yspennstate/math-open-problems@31608e4193b3ba491084081cb7c000e254c01a82`;
- one-anchor three-volume theorem: `yspennstate/math-open-problems@59ccddd0766b466b30abd645926887f907b0bcd7`;
- newest designated partner fleet03/B01: `yspennstate/math-open-problems@ed79f4a518a9f683a679d70193d6a2a72fb05ff2`.

## New analytic compiler under proof

Let `M=A[I,J]`, let `Omega` be any selected family of physical `3x3` minors all containing one fixed original row `h`, let

`Z_h=sum_(R,C in Omega) det M[R,C]^2>0`,

and normalize the squared-minor weights. Suppose every non-anchor selected row marginal is at most `1/2`. Write `a=M[h,:]`, `R=||a||_2`.

The completed one-anchor theorem gives the pointwise joint-Fourier tail

`|phi_Q(t)| <= 2 pi^(5/4) e^(5/8) R^(1/4) Z_h^(-1/4) |t|^(-5/4)`.

Independently, integrating the same ORIGINAL hub first and using the cap-one one-dimensional projection density plus Plancherel gives

`|phi_Q(t)| <= 2^(1/4) sqrt(pi) R^(-1/2) |t|^(-1/2)`.

The first bound is integrable but worsens with a large anchor; the second is nonintegrable but improves with the same anchor. Splitting the frequency integral at their crossover cancels `R` exactly and yields the scale-free candidate

`||p_Q||_infinity <= 6*2^(3/4)*e^(5/12) Z_h^(-1/6) < 15.307 Z_h^(-1/6)`.

This is a joint averaged-frequency replacement and does not assert any law-uniform scalar quadratic-phase decay.

## Intended application to r44 heavy-volume survivor

For the full three-volume law with total `Z=e_3(M^TM)`, if one row has marginal `alpha_h>=43/64`, select the minors containing `h`, so `Z_h=alpha_h Z`. If its conditional partner-row marginals are all at most `1/2`, the candidate theorem gives

`||p_Q||_infinity < 16.356 Z^(-1/6)`.

Otherwise some second row `r` satisfies

`P(h,r both in S)>alpha_h/2>=43/128`.

Hence the row-pair three-volume mass is `>43Z/128`. Applying the same argument after transposition gives the column analogue. Thus, if neither orientation is paid, the old `<=2 x <=2` heavy class sharpens to a quantitative two-row/two-column exterior-two anchor packet.

Proof constants and the exact wedge identity are being checked before final publication.
