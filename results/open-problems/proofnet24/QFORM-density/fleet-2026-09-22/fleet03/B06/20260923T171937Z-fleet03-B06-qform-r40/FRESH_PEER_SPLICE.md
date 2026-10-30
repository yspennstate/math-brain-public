# Fresh peer splice after the main r40 proof

A newer completed peer report landed after `REPORT.md` was written:

`yspennstate/math-open-problems@585b5a3ca7e887e5cd16f45ea49056d548361dfb`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T173320Z-auto11-heavyrowpromotion/REPORT.md`.

Its theorem `QFORM-ONEHUB-E2-MARGINAL-GATE-REMOVAL-v1` removes the row-marginal gate from the reviewed `k=1, ell=2` projected-crossing receiver. In its exact scope, if one literal original hub has partner row `m` and the projected light crossing `C` has `Z2(C):=e_2(CC^T)>0`, then

`||p_Q||_infinity <= C_E2 (||m||^2 Z2(C))^(-1/6)`,

`C_E2=3*2^(7/6)*exp(1/3)<9.400`,

with a continuous `C_0` density and no row-marginal assumption.

Apply it to the actual r40 heavy row anchor `i`. Let

`m=N[i,K]`,

`C_i=N[J\{i},K](I-P_m)`,

where `P_m` is the orthogonal projection in the physical `K` coefficient space onto `span(m)`. The r40 theorem gives

`||m||^2>226233/33554432`.

Therefore the concrete branch

`e_2(C_i C_i^T)>=2^-20`

is now paid by

`||p_Q||_infinity
 < 3*2^(7/6)*exp(1/3)
   [(226233/33554432) 2^-20]^(-1/6)
 <218`,

with a continuous `C_0` density. All same-bank terms and outside couplings are retained by the cited theorem.

This does **not** close the r40 survivor. In the exact rank-two crossing endpoint, `C_i` has rank at most one and hence `e_2(C_i C_i^T)=0`; in the ultra-thin case this quantity can be arbitrarily small. Thus the genuinely current remaining branch can be sharpened to

`e_2(C_i C_i^T)<2^-20`

for the heavy row anchor, and symmetrically for the heavy column anchor after transposition, in addition to all r40 conclusions (`>19/32` top-plane leverage, robust star and cofactor currencies, and `|A_ia|<1/32` after the paid pair exit).

This fresh source removes the row-marginal gate mentioned in the last paragraph of `REPORT.md`; the missing issue is now the *amount of projected E2 curvature*, not its marginal spread. Full QFORM remains open.
