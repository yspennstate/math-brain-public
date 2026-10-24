# Deterministic checks for endpoint Beta localization

Run: `20260924T053625Z-account02-B14-QFORM-auto11`.

## 1. Exact Beta integral

For `d>0`, `s>0`,

`I(d,s)=int_{|u|<sqrt(s/d)} du/sqrt(s-d u^2)`.

With `u=sqrt(s/d) sin(theta)`, `du=sqrt(s/d)cos(theta)dtheta`, so

`I(d,s)=d^(-1/2) int_{-pi/2}^{pi/2} dtheta = pi/sqrt(d)`.

Thus the endpoint constant in the same-sign two-square compiler is exactly `pi/sqrt(ad)` after the first square contributes `a^(-1/2)`.

## 2. Active submeasure sharpness

Let `0<m<=1`,

`rho_W(w)=1_{[-1/2,1/2]}(w)`, `rho_U(u)=1_{[-m/2,m/2]}(u)`.

The product measure has total mass `m`. For `0<s<m^2/4`, the entire circle `w^2+u^2=s` lies in the rectangle because `sqrt(s)<m/2<=1/2`. Therefore

`p_{W^2+U^2}(s)=int delta(s-w^2-u^2) dw du`.

Using polar coordinates,

`=int_0^{2pi}int_0^infinity delta(s-r^2) r dr dtheta = (1/2)(2pi)=pi`.

Hence the density height is independent of the active submeasure mass. No estimate `||p||inf <= C m^gamma` with a fixed `gamma>0` can hold uniformly for this endpoint class.

## 3. Finite-p norm obstruction

For `R>=2`, define

`f_R(u)=1_{[-1/(2R),1/(2R)]}(u) + R^(-1)1_[2,R+1](u)`.

Mass:

`int f_R = 1/R + (R-1)/R = 1`.

For every finite `p>1`,

`||f_R||_p^p = 1/R + (R-1)/R^p -> 0`.

If `W~Unif[-1/2,1/2]` and `U_R~f_R`, then for `0<s<1/(4R^2)` the circle `w^2+u^2=s` lies inside the height-one central tooth and does not meet the remote tail. Hence

`p_{W^2+U_R^2}(s)=pi`.

So no same-sign endpoint theorem can replace the active `L^infinity` cap by a positive power of any fixed finite `L^p` norm. In particular, the `L^2` collision-energy improvement available for a linear slope bank cannot be transplanted to an active square carrier.

For reference,

`||f_R||_2^2=(2R-1)/R^2`,

which is `0.0199` at `R=100` and `0.001999` at `R=1000`, while the quadratic-output density still equals `pi` arbitrarily close to zero.

## 4. Exact-target matrix check

Take

`A_*=[[2,1,0],[1,2,0],[0,0,-1]]`.

The first block has eigenvalues `3,1`, so

`spec(A_*)={3,1,-1}`.

The corresponding form is

`Q=2W^2+2WU+2U^2-Y^2`

` = 2(W+U/2)^2 + (3/2)U^2 - Y^2`.

Thus the same-sign compiler has `a=2`, `d=3/2`, `sqrt(ad)=sqrt(3)` and gives

`||p_Q||inf <= pi/sqrt(3) = 1.8137993642342178...`.

The fixed Claude-source Theorem A applies to the same three-dimensional matrix with `sigma=1` and gives

`||p_Q||inf <= 6 sqrt(pi) = 10.634723105433096...`.

## 5. Fragment-first bookkeeping check

For

`E_N = union_{j=1}^N [4^j,4^j+1/N]`, `f_N=1_{E_N}`,

the aggregate law is a cap-one probability. The whole same-sign theorem gives `pi/sqrt(3)` independently of `N`.

If the active `U` law is split into its tooth submeasures, each tooth has mass `1/N` but unnormalised density cap one. The finite-measure endpoint theorem therefore gives the full `pi/sqrt(3)` certificate on each tooth, so summing the certificates costs

`N pi/sqrt(3)`.

For the countable comb with tooth lengths

`m_j=6/(pi^2 j^2)`,

one has `sum_j m_j=1`, but each tooth still has cap one, so separate endpoint payment has divergent certificate sum `sum_j pi/sqrt(3)=infinity`, while the aggregate law remains cap one and the whole same-sign theorem still gives `pi/sqrt(3)`.
