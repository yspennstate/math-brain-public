SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-24T04:12:05Z.
attacking: the near-coloop endpoint by replacing the rho-degenerate disjoint three-volume currency with the actual physical hub-partner direction and an orthogonal transverse direction, then applying the designated fleet04/B10 three-bank split in that fixed basis.

# Early calculation — endpoint-stable hub-partner frame

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T041205Z-fleet03-B10-QFORM-r28`  
Status: supporting exact geometry; full exact rank three and full QFORM remain OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Start from B10 r27's live near-coloop state. Thus `A=RMR^T`, `R^TR=I_3`, `sigma_min(M)>=1`, `D=|det M|>=1`; one ORIGINAL hub row is `u_0=sqrt(h)e`, `h>63/64`, `rho=1-h in (0,1/64)`, and leaf rows are `u_i=t_i e+p_i` with

`sum t_i^2=rho`, `sum t_i p_i=0`, `sum p_i p_i^T=I_2`, `max_i ||p_i||^2<1/61`.

Relative to `e direct_sum e^perp`, write `M=[[alpha,m^T],[m,N]]`, `|alpha|<1/16`. Put `s=||m||`. Since `sigma_min(M)>=1`, `s^2+alpha^2=||Me||^2>=1`, hence `s^2>255/256`. Choose an orthonormal transverse basis `(v,q)` with `m=sv`, and write `p_i=x_i v+y_i q`. Then the coefficient vectors `t,x,y` satisfy

`||t||^2=rho`, `||x||=||y||=1`, `t perpendicular x,y`, `x perpendicular y`.

Define the actual unscaled physical hub partner on the leaves

`B_i=alpha t_i+s x_i`, `gamma^2=||B||^2=s^2+alpha^2 rho`, `r=B/gamma`.

Then `r perpendicular y`, `||r||=||y||=1`, and the physical hub star is `A_{0i}=sqrt(h) B_i`. In particular

`sum_i A_{0i}^2=h gamma^2 > (63/64)(255/256)=16065/16384`.

More importantly, the two-frame `(r,y)` is uniformly diffuse THROUGH the puncture. Indeed

`|r_i| <= |x_i|+(|alpha|/s)|t_i| < |x_i|+1/(8 sqrt(255))`,

so

`r_i^2+y_i^2 < (1/sqrt(61)+1/(8 sqrt(255)))^2 <1/54`.

For the last strict inequality, `sqrt(15555)>1247/10`, hence

`1/61+1/16320+1/(4 sqrt(15555)) < 1/61+1/16320+5/2494 =22915907/1241413440 <1/54`.

Thus the endpoint obstruction is not collapse or concentration of the actual hub partner: together with the untouched transverse direction it is a far-better-than-half-leverage original-product frame.

A second exact normalization exposes the remaining third direction. Let

`eta=alpha sqrt(rho)/gamma`, `theta=s/gamma`,

and, with `z` the normalized component of `t` perpendicular to `r`, one has

`t/sqrt(rho)=eta r+theta z`, `x=theta r-eta z`, `eta^2+theta^2=1`,

with `(r,z,y)` orthonormal as coefficient vectors on the original leaves.

This is the mechanism change for r28: stop paying the leaf three-volume `rho`; work with the noncollapsing star/transverse two-frame and keep the exact third-direction compatibility visible rather than discarding it as a small random perturbation.
