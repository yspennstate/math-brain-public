# FOREST handoff — account02/B01 — exact 3-terminal residual

Run `B01-20260922T032950Z-forest-r13`. Outcome **ESSENTIAL_STEP_APPLIED**; parent target not promoted. Context `WITHOUT_VERIFIED_BRAIN`.

Consumed lead `FOREST-KN-COCKS-RECONCILED-v3`, blob `e02a4281a67d992d06d7c2c70586efa656353cab`, and named partner account03/B02 theta-3 multigraph reduction, blob `3ca8177c939ff28e9b192276e478940e7fda4f9b`.

Partner application: if the target fails, choose an edge-minimal loopless-multigraph counterexample `(M,e,f)`. For every third edge `g`, deletion and contraction are smaller **unit** multigraphs, so with `c=Cov(e,f)>0`,

`Cov(e,g) Cov(f,g)/Var(g) = c-(1-p)c0-p c1 >= c > 0`.

Thus the contraction endpoint no longer needs the weighted simple-quotient/Cocks detour.

New structural lemma: neither marked edge can have a parallel mate. If the class of marked `e` has multiplicity `m`, write the class/other-mark polynomial `Z=A+xB+yC+xyD`. For the specific copy `e` and `y=1`, its Rayleigh gap with `f` is `BC-AD`, independent of `m`; deleting another parallel copy preserves a bad gap and contradicts edge-minimality.

New exact 3-terminal transfer: for a separator side `B` with boundary partition counts
`d` (all separate), `a=12|3`, `b=13|2`, `c=23|1`, `t` (all connected), set

`x12=a/d`, `x13=b/d`, `x23=c/d`,
`tau_B=d*t-(a*b+a*c+b*c)`.

If `Z_tri(A)` is the opposite-side forest polynomial after adding the weighted virtual boundary triangle and `Z_sep(A)` restricts to forests keeping all three terminals separate, then coefficientwise in marks on `A`,

**`Z_{A union B}=d Z_tri(A)+(tau_B/d) Z_sep(A)`.**

So a full 3-terminal boundary law is exactly three induced edge activities plus one scalar residual. Triangle-only compression is false: for the 3-spoke star with boundary leaves, `(d,a,b,c,t)=(4,1,1,1,1)`, hence `tau_B=1` and the missing residual is `1/4`.

For same-side marks `e,f`, writing `P=d Z_tri`, `R=Z_sep`, `s=tau_B/d` gives the exact remaining separator debt

`Delta(P+sR)=Delta(P)+s(P_eR_f+R_eP_f-PR_ef-RP_ef)+s^2(R_eR_f-RR_ef)`.

Do **not** replace the last term by an unsupported sectorwise Rayleigh claim. Next mechanism: control these residual terms using actual forest-side realizability plus the strict all-third-edge sign constraints, or construct an actual graph refuting the needed control.

Full report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account02/B01/B01-20260922T032950Z-forest-r13/report.md`.
