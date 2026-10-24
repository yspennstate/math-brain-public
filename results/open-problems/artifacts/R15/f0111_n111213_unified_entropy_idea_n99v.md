# R15 idea-before-code note: unify the remaining N=11,12,13 dimension-30 F0111 cells

Status: retained F0111 screen only; **PENDING / SELF_CHECK_ONLY / NOT CLAIMED**. Native I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; it is not reopened here.

Methods for this route: **#5 ADD A PARAMETER AND DIFFERENTIATE**, **#13 FIND WHAT ONLY INCREASES**, **#18 SAY IT IN ANOTHER LANGUAGE**. The immediately preceding complete run used #11/#15/#24, so this triple is nonconsecutive.

## Carried state

The exact scalar-envelope reduction leaves, for `n=30`, full-support two-level Hessian-null exact quadratic contacts on the `z=1+s>1` branch,

- `N=|K| in {11,12,13}` after the complete elimination of the `N=14` cell;
- the exact scalar requirements `L_K <= N < U_K`, equivalently `Q_K<29` together with the block-capacity bounds;
- rational coarse strips
  - N=11: `11/25 < delta < 5/11`, `0<s<s_11<0.009292`;
  - N=12: `12/25 < delta < 1/2`, `0<s<s_12<0.014404`;
  - N=13: `13/25 < delta < 7/13`, `0<s<s_13<0.012637`.

The N=14 proof combined the exact residual-Gram compression

`2U=(b^2/a^2)T-x+A_J x^2`,
`2V=T-y+A_K y^2`,
`W=(b/a)T+A_JK x y`,
`T<=y(N-L_K)`,

with a heavy-coordinate alternative and the exact contact identity

`E=sum_{i<j} B_ij q_i q_j = k log S - sum_i r_i log r_i`.

The goal now is not to repeat three bespoke cell calculations. The route is to add `N` as a discrete parameter and find one monotone envelope that proves the same entropy-energy contradiction simultaneously for N=11,12,13.

## New route

For fixed scalar `(delta,s,N)`, define the capacity endpoint

`Tcap_N = y (N-L_K)`

and the corresponding aggregate maxima

`U_N=( (b^2/a^2)Tcap_N - x + A_J x^2 )/2`,
`V_N=( Tcap_N - y + A_K y^2 )/2`,
`W_N=( (b/a)Tcap_N + A_JK x y )`.

Treat `N` as a parameter only through `Tcap_N`. These three bounds are affine increasing in `N`. By contrast, the scalar-feasible delta window shifts with N. The hope is to prove that the **worst entropy-energy margin is monotone in N after transporting delta to a common normalized cell coordinate**. That would reduce all three cells to one endpoint calculation.

A useful normalized coordinate is

`delta = delta_lo(N) + theta (delta_hi(N)-delta_lo(N))`, `0<=theta<=1`,

with `delta_lo=(N/25)` and `delta_hi=(N-6)/N` for N=11,12,13. The scalar upper boundary is determined by `Q_K=29` and `U_K=N`; rather than solve it exactly, use a rational roof `s<=sbar_N` and, if needed, a slanted lower delta wall `delta>=dline_N(s)` obtained from `U_K=N` as in the N=14 run.

The first target inequality is a **uniform heavy-coordinate exclusion**

`r_* >= 1-C s  => contradiction`

with one rational `C` valid for all N=11,12,13. As in N=14, set `r=1-Cs`, `ell=x-r`, `e=r(1-A_J r)` and

`Delta_N = s(x-2 ell)/b - (b/a)Tcap_N - A_JK ell y`.

If `Delta_N>0` and `Delta_N^2>e Tcap_N`, residual-Gram Cauchy excludes `r_*>=1-Cs`. Because `Tcap_N` is increasing in N, this step is hardest at the largest capacity, but the feasible delta interval also changes; a common-C proof may still exist.

For the complementary entropy step, write `c=(1-r_*)/s>C`. Use

- `q_j <= log(29/Q_K)` on K;
- `L=log S <= log(C_S/s)` from exact bounds on `-k/s`;
- light-J coordinate bound `q_i <= log(C_S(c+C_x))`;
- aggregate coefficient bounds `U_N,V_N,W_N`;
- entropy lower bound from the heavy mass and the K/J defect.

The desired scalar gap is of the form

`G_N(c,delta,s) := E_lower_entropy - E_upper_coeff > 0`.

Method #5: differentiate G in c and normalized theta; if the derivatives have fixed sign, the proof reduces to finitely many boundary points.

Method #13: identify the monotone quantity among `N`, `theta`, `s` after rational normalization. If the gap worsens monotonically toward one corner, that corner certifies the whole family.

Method #18: regard the residual-Gram side as a one-dimensional transportation/capacity problem in `T`, and the contact side as Shannon entropy. The proof should compare a capacity-limited quadratic energy with the minimal entropy compatible with the same defect, rather than track individual coordinates.

## Success criterion for this run

A useful success is either:

1. one exact theorem eliminating all N=11,12,13 cells; or
2. a genuinely stronger reduction proving a common heavy-coordinate exclusion plus an exact monotonicity principle that leaves only finitely many rational endpoint inequalities.

Only after this route is mathematically fixed should any symbolic/exact checker be written. Numerical samples alone do not move the theorem.