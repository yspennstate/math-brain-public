# account02/B15 handoff — regularity + principal-triple localization

**Programme:** `QFORM-DENSITY-3EIG-20260922` revision `2026-09-22.5`  
**Assignment:** `Absolute continuity and regularity`  
**Full target:** `OPEN / NOT PROVED`.

## Canonical scientific source

`yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`

Claim cards: `yspennstate/math-open-problems@8907c032fd7d863f89a27445f4488caa0df1f1d6`.

## Assignment-specific regularity result

Using the completed account03/B17 same-sign-pair theorem, the whole diagonal branch upgrades from merely bounded density to a **bounded uniformly continuous density** with the same constant `pi`.

Choose two same-sign large diagonal terms; their sum has a density `p12` with `||p12||_infinity<=pi`. The third large square term has an `L1` density `g3`. Hence `p123=p12*g3` and

`||tau_h p123-p123||_infinity <= ||p12||_infinity ||tau_h g3-g3||_1 ->0`.

Convolution with the probability law of all remaining independent terms preserves both the sup bound and uniform continuity.

For the fully rotated target, continuity remains separate: the small-ball theorem below proves absolute continuity and `L-infinity`, but no general continuous representative is claimed.

## New local target theorem

For independent `Y1,Y2,Y3`, each density <=1, and a symmetric invertible `3x3` block `B`, every affine quadratic

`Y^T B Y + 2 b^T Y + c`

has density

`||p||_infinity <= (2*pi+3*sqrt(3))/sigma_min(B) < 11.48/sigma_min(B)`.

Proof split:
- near `|By|<=1`: `z=|B|^(1/2)y` reduces to a canonical signature quadratic inside the unit ball; every output interval of length eta cuts volume <=`2*pi*eta`;
- far `|By|>1`: one original coordinate derivative has magnitude >`2/sqrt(3)`; quadratic monotonicity on at most two branches gives `sqrt(3)*eta` per coordinate, total `3*sqrt(3)*eta`.

Therefore if any principal coordinate triple of a high-dimensional `A` has singular gap `kappa`, conditioning all other independent coordinates gives

`||p_{X^TAX}||_infinity <=(2*pi+3*sqrt(3))/kappa`.

## Partner account03/B15 applied

Completed partner source:

`yspennstate/math-open-problems@1ce0598e1c9c4e0681f8f6b86d3dfef990ec5d4e:qform/fleet-2026-09-22/account03/B15/account03-B15-20260922T112830Z/REPORT.md`.

Its exact bathtub reduction says the full target is equivalent to

`|{x in E1 x ... x En : X^TAX in J}| <= C |J|`

for arbitrary measurable unit-measure `E_i` (finite interval unions suffice in supremum). Thus the theorem above closes exactly this geometric statement whenever one principal triple has a uniform singular gap.

## Why fixed-triple localization cannot close the target

For Sylvester orders, choose three normalized Hadamard columns `U` and set `A=UU^T`. Then A has exactly three eigenvalues equal to1, but every row has squared norm `3/n`. For each coordinate triple I,

`trace(A_II)=9/n`, hence `sigma_min(A_II)<=3/n`.

So selecting one triple forces a dimension loss. Yet Cauchy-Binet gives the exact aggregate resource

`sum_{|I|=3} det(A_II)=sum det(U_I)^2=1`.

The next bridge should aggregate many triples/minors rather than choose one: under the partner product-set reduction, prove the shell-volume bound for the flat rank-three projector using the unit determinant mass. Multilinear coarea / Brascamp-Lieb / determinant-weighted averaging are the natural mechanisms.
