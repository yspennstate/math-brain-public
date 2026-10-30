# fleet02/B10 early checkpoint — null-hub union-graph receiver

Programme `QFORM-DENSITY-3EIG-20260922`; run `20260923T111853Z-fleet02-B10-QFORM-auto11`. Full QFORM remains OPEN.

First unpaid implication attacked: `QFORM-NULL-HUB-THREEBANK-PACKET-TO-LINFINITY-v1` from designated partner fleet03/B10, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T101459Z-fleet03-B10-QFORM-r23/REPORT.md`.

Partner state: exact rank three `A=RMR^T`, `R^TR=I_3`, `D=|det M|>=1`, one ORIGINAL null hub `u_0=sqrt(h) r`, `h>55/64`, `r^TMr=0`; complementary rows `u_j=t_jr+y_j`, `y_j in r^perp`, with `sum y_jy_j^T=I_2`, `sum t_jy_j=0`. The partner's completed three-bank split gives disjoint ORIGINAL banks `C=S sqcup Y sqcup Z` with

`rho_S M_2(G_Y,G_Z) >= (2/81) rho`,

hence `M_2(G_Y,G_Z)>=2/81`, where `G_G=sum_{j in G} y_jy_j^T` and `M_2(H,K)=tr(adj(H)K)`.

Put `T=Y sqcup Z`, `G_T=G_Y+G_Z`. In dimension two,

`det G_T = det G_Y + det G_Z + M_2(G_Y,G_Z) >= 2/81`.        (E1)

Define the union-bank longitudinal innovation

`tau_T^2 = dist(t_T, col(Y_T))^2`,

where `Y_T` is the coefficient matrix with rows `y_j^T`. If `tau_T=0`, there is a deterministic `a in r^perp` such that `t_j=a dot y_j` for every `j in T`.

Condition only on the ORIGINAL coordinates in `S` and on any additional exact `r`-collinear rows. Then the remaining random variables are the genuinely independent hub scalar `X_0` and the two-dimensional transverse bank projection

`P_T=sum_{j in T} y_j X_j`.

The normalized projection `G_T^{-1/2}P_T` is a two-dimensional orthonormal product projection, so the completed weighted affine-fiber Brascamp--Lieb theorem gives

`||p_{P_T}||_infinity <= e / sqrt(det G_T) <= 9e/sqrt(2)`.       (E2)

When `tau_T=0`, the spectral contribution of bank `T` equals `(a dot P_T)r+P_T`. Thus, in variables `(x,p)` with `x=X_0`, the homogeneous spectral map is

`B(x,p)=sqrt(h)x r + (a dot p)r+p`,

and `det B=sqrt(h)`. Hence the conditional homogeneous quadratic matrix is `H=B^TMB`, with

`H_xx=0`,  `|det H|=hD>=55/64`.                                    (E3)

Fleet01/B11's completed dependence-safe null-scalar/arbitrary-pair theorem applies because `X_0` is genuinely independent of the whole dependent pair `P_T`; no independence inside `P_T` is asserted. Combining (E1)--(E3),

`||p_Q||_infinity <= 3*2^(2/3)*(9e/sqrt(2))^(2/3)*(64/55)^(1/3) < 33.504`.   (E4)

This is a new paid endpoint of the designated partner's three-bank survivor. It is not a conditional-density surrogate: the only conditioning is on disjoint original-coordinate banks.

Required newest-Claude ruled theorem is also consumed at its exact scope: for signature `(2,1)`, the one-sheet side already satisfies `ess sup_{s>=0} p_Q(s)<=pi sqrt(2)` (sign reversed for `(1,2)`), so the genuinely unpaid geometry is the convex/two-sheet side.

Next: stress whether the packet forces `tau_T=0` or a fixed positive lower bound. It does not; construct an exact Parseval target family with constant packet, `tau_T>0` arbitrarily small, and all individual physical pivots/minors tending to zero.