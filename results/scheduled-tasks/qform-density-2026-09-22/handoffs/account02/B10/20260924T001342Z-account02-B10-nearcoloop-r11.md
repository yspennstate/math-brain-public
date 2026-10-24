# account02/B10 handoff — conditional hyperbolic-square receiver

Programme `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.15`. Full QFORM remains OPEN.

Canonical mathematics: `yspennstate/math-open-problems@d11a83e445576f8563997083670387aa18a331e5`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260924T001342Z-account02-B10-nearcoloop-r11/REPORT.md`.

## New theorem

`QFORM-CONDITIONAL-HYPERBOLIC-SQUARE-RECEIVER-v1`: if

`p_{Z,Y}(z,y) <= K_Z p_Y(y)`, `||p_Y||_inf<=K_Y`, and `W` is independent of `(Z,Y)` with `||p_W||_inf<=K_W`, then for nonzero `s,d`,

`Q0=2sZY+bY^2+2cYW+dW^2`

satisfies

`||p_Q0||_inf <= 4 sqrt(2) K_W sqrt(K_Z K_Y)/sqrt(|sd|)`.

The proof completes the W-square, absorbs the residual Y-square into a Y-dependent translation of Z, and uses the cap-K half-potential inequality `sup_a E|V-a|^{-1/2}<=2sqrt(2K)` twice. Z and Y need not be independent.

## Near-coloop chamber closed

For exact rank three with `sigma_min(M)>=1`, a physical hub `u0=sqrt(c)e`, `c>63/64`, exact null spectral pivot `e^TMe=0`, one mixed original bank `B` with rows `t_i e+y_i u`, and a disjoint clean transverse bank `C` with rows `w_j v`, Parseval yields unit transverse coefficient norms. With

`Z=sqrt(c)H+sum_B t_iX_i`, `Y=sum_B y_iX_i`, `W=sum_C w_jX_j`,

we have

`Q=2rZY+aY^2+2bYW+dW^2`, `r>=1`, `|d|>=1`.

The latest compatible partner account03/B10 result supplies the actual adapted-hub inequality `p_{Z,P}<=c^{-1/2}p_P`; marginalizing gives `p_{Z,Y}<=c^{-1/2}p_Y`. Ball--Rogozin gives `K_Y,K_W<=sqrt(2)`. Therefore

`||p_Q||_inf <= 8*2^(1/4)c^(-1/4) < 9.552`.

This pays arbitrary dependence between longitudinal leakage and the hyperbolic transverse scalar when they share the same original bank. Independence is used only for the clean square bank, justified by disjoint ORIGINAL physical coordinates.

A concrete diffuse family uses 128 balanced-sign mixed rows in B and 64 clean e3 rows in C; all transverse leverages are <=1/64<1/61, and with `M=[[0,1,0],[1,0,0],[0,0,1]]` the exact nonzero spectrum is `{-1,1,1}`. The new all-level bound is `<9.552` for arbitrary cap-one source laws.

## Required pinned source applied

From `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, the completed ruled signature-(2,1) theorem applies to that same concrete family and gives

`p_Q(s)<=pi*sqrt(2)<4.443` for every `s>=0`.

Thus the source theorem directly pays the majority-sign side; the new receiver pays the two-sheet side in this one-mixed-bank chamber.

## Corrections enforced

No post-rotation independence; no conditional-cap-as-independence shortcut; no raw fiber-supremum payment; no perturbative deletion of a small random quadratic coefficient without moment/support assumptions; continuity remains separate.

## First unpaid implication

`QFORM-EXACT-NULL-BIDIRECTIONAL-MIXED-BANK-RECEIVER-v1`: allow both transverse banks to carry longitudinal leakage. Then `(T_B,Y)` share B and `(T_C,W)` share C; coefficient orthogonality from Parseval does not imply independence for arbitrary non-Gaussian product sources. Extend the conditional hyperbolic-square receiver while retaining both original-coordinate banks and without paying the leakage scale.

This strictly narrows the partner's generic `QFORM-TWOBANK-MIXEDROW-TRIANGULAR-RECEIVER-v1`: one-sided contamination is paid; bidirectional contamination remains.
