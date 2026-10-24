# Early substantive checkpoint — circular family is paid by the transverse-null-hub theorem

Source actually consumed: designated partner account02/B18 r28, `yspennstate/math-open-problems@71636c1be698996cc0fe90b91f872efdb6c11860`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/account02-B18-20260923T120424Z-r28/REPORT.md`.

Partner family, for integer m>=3:

- residual Parseval rows `v_j=m^(-1/2)(1,sqrt(2)cos theta_j,sqrt(2)sin theta_j)`, `theta_j=2 pi j/m`;
- hub row `u_0=m e_1`;
- `D_m=[[0,(1+m^2)^(-1/2),0],[(1+m^2)^(-1/2),0,0],[0,0,1]]`;
- `A_m=U D_m U^T`, whose nonzero spectrum is exactly `{-1,1,1}`;
- `Q_m=(2/sqrt(1+m^2))(Y_1+mX_0)Y_2+Y_3^2`.

New application.  The completed transverse-null-hub compiler in account03/B18 r28 (`2c5b53442c3d74999f0ced62aa1001c01b24007c`) applies literally with

`u=m e_1`, `r=m`, `n=e_1`, `n^T D_m n=0`, and

`q_j=||P_(e_1^perp)v_j||^2=(2/m)(cos^2 theta_j+sin^2 theta_j)=2/m`.

Hence for every m>=4 the gate `max q_j<=1/2` holds.  Since `|det D_m|=1/(1+m^2)`, the theorem yields the full-real-line, continuous-C0 estimate

`||p_(Q_m)||_infinity <=3*2^(4/3)[m^2/(1+m^2)]^(-1/3)
 =3*2^(4/3)((1+m^2)/m^2)^(1/3)`.

This is decreasing for m>=4; at m=4 it equals `7.713844771974705...`, tending to `3*2^(4/3)=7.55952629936924...`.

The exceptional m=3 can be paid by the exact-zero-pivot three-independent-original-coordinate theorem quoted in the designated partner report. Condition on one residual coordinate and retain the hub plus two residual coordinates, say angles `2pi/3,4pi/3`. Their 3x3 row matrix R has `det R=sqrt(3)`, while `det D_3=-1/10`, so the active principal matrix K has

`|det K|=(det R)^2 |det D_3|=3/10`, and its hub pivot is exactly zero.

Thus the source theorem gives

`||p_(Q_3)||_infinity <=12(3/10)^(-1/3)=12(10/3)^(1/3)=17.92561898622866...`,

with continuity (arbitrary affine terms from the conditioned coordinate are within the theorem's scope).

Therefore the entire partner circular family m>=3 is paid on the whole real line by one dimension-free constant `12(10/3)^(1/3)<17.926`, and continuously.  On t>=0 the partner's inherited ruled one-sheet estimate `p(t)<=pi sqrt(2)` remains sharper.

This does NOT prove full QFORM.  It removes this exact target-valid stress family from the unpaid list and shows that the scalar-bank compiler barrier does not obstruct a mixed-Fresnel/null-hub payment retaining all three residual spectral dimensions.
