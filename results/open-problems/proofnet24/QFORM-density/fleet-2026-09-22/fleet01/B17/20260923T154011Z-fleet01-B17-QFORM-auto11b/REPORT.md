SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T15:40:11Z.
attacking: the one-heavy genuinely coupled N3 Gaussianized family; prove a uniform cone-tip gap below 3sqrt(2) for the full rotation parameter and apply fleet02/B17's newest separated-bank theorem to an actual exact-spectrum comparator.

# QFORM B17 — uniform cone-tip gap for the full one-heavy coupled N3 family

Run: `20260923T154011Z-fleet01-B17-QFORM-auto11b`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING ANALYTIC STRESS-FAMILY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Full-target continuity remains separate. Execution is `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

For `0<a<=1`, put `d=sqrt(1-a^2)` and let

`Q_a = -a X^2 + 2 d X B + a B^2 + C^2`,

where `B,C` are independent `N(0,1/12)`, independent of `X`, and `X` ranges over all probability densities `0<=f<=1`.

Fleet03/B17 proved the exact cone-tip optimizer

`sup_f p_{Q_a}(0)=C(a)`, uniquely attained by `X~Unif[-1/2,1/2]`, and supplied exact finite product approximants with nonzero spectrum `{1,1,-1}`.  The missing implication was an analytic uniform ceiling in `a`.

This report proves

`boxed( sup_{0<a<=1} C(a) <= (C_- + 3sqrt(2))/2 < 3sqrt(2) )`,

where

`C_- = sqrt(6 pi) erf(sqrt(3/2)) = 3.9801056750420088...`.

Numerically,

`(C_-+3sqrt(2))/2 = 4.111373181080647...`,

leaving the explicit gap

`3sqrt(2) - (C_-+3sqrt(2))/2 = 0.131267506038638...`.

Using only fleet03's elementary endpoint certificate `C_-<97/24`, one gets the entirely elementary uniform bound

`C(a) < 97/48 + 3sqrt(2)/2 = 4.142153676892976... < 3sqrt(2)`.

Thus the entire one-macroscopic-coordinate/shared-diffuse N3 **cone-tip** mechanism is uniformly subcritical.  This is not a global off-tip theorem.

## 2. Exact N3 source and cone coordinates

Use the physical `(X,B,C)` matrix

`M_a = [[-a,d,0],[d,a,0],[0,0,1]]`.

It satisfies `M_a^2=I_3`, hence has eigenvalues `{1,1,-1}`.  Let

`c=sqrt((1+a)/2)`, `s=sqrt((1-a)/2)`.

A unit negative eigenvector and a unit positive eigenvector in the `(X,B)` plane are

`n=(c,-s,0)`, `p=(s,c,0)`.

Together with `e_3=(0,0,1)`, the two circles of unit null directions are

`omega_+(theta)=( n + cos(theta) p + sin(theta)e_3)/sqrt(2)`,
`omega_-(theta)=(-n + cos(theta) p + sin(theta)e_3)/sqrt(2)`.

Their `X`-coordinate squares are

`z_+(theta)=(c+s cos(theta))^2/2`,
`z_-(theta)=(-c+s cos(theta))^2/2`.

The two have the same distribution under uniform `theta`, so define

`Z_a=(c+s cos(Theta))^2/2`, `Theta~Unif[0,2pi]`.

For the centered interval optimizer, the joint physical density is

`rho(x,b,c0)=1_{|x|<=1/2} (2pi v)^(-1) exp(-(b^2+c0^2)/(2v))`, `v=1/12`.

On a unit ray whose squared `X` coordinate is `z`, the physical strip cuts the ray at `r=1/(2sqrt(z))` and the Gaussian exponent is `-6(1-z)r^2`.  Define, continuously at the endpoints,

`g(z)=int_0^{1/(2sqrt(z))} exp(-6(1-z)r^2) dr`, `0<z<=1`,

`g(0)=int_0^infinity exp(-6r^2)dr`.

Spherical coarea for a unit-signature quadratic form gives `|grad_S q|=2` on the null cone; each circle has speed `1/sqrt(2)`.  Consequently

`boxed( C(a)=6sqrt(2) E[g(Z_a)] ).`                                         (2.1)

This representation is exactly equivalent to fleet03's angular `F_a` formula, but it makes the orientation dependence one-dimensional.

## 3. The radial reward g is increasing

The key elementary fact is

`boxed( g'(z)>=0 on (0,1), hence g(z)<=g(1)=1/2 ).`                           (3.1)

Proof.  Put

`L=1/(2sqrt(z))`, `k=6(1-z)`, `eta=kL^2=3(1-z)/(2z)`, `E=exp(-eta)`.

Differentiating and integrating by parts gives

`g'(z) = [2 z^(3/2) g(z)-E]/[4 z^(3/2)(1-z)]`.

With `r=Lu`,

`2 z^(3/2)g(z) = z int_0^1 exp(-eta u^2)du`.

Also `z=1/(1+2eta/3)`.  Since `exp(t)>=1+t`,

`int_0^1 exp(-eta u^2)du`
` = exp(-eta) int_0^1 exp(eta(1-u^2))du`
` >= exp(-eta)[1+eta int_0^1(1-u^2)du]`
` = exp(-eta)(1+2eta/3)`
` = E/z`.

Therefore the numerator in `g'` is nonnegative.  It is strictly positive for `0<z<1`.  This proves (3.1).

At the midpoint,

`g(1/2)=int_0^{1/sqrt(2)} exp(-3r^2)dr`
`       = sqrt(pi)/(2sqrt(3)) erf(sqrt(3/2))`,

and hence

`6sqrt(2) g(1/2)=sqrt(6pi) erf(sqrt(3/2))=C_-`.                              (3.2)

## 4. At most half of the null circle can enter z>1/2

For `0<a<1`, `c>=s>=0` and `c-s>=0`, so `c+s cos(theta)` is nonnegative.  Therefore

`Z_a>1/2  iff  c+s cos(Theta)>1`
`             iff cos(Theta)>(1-c)/s`.

The threshold `(1-c)/s` belongs to `[0,1]`: nonnegativity is clear and `(1-c)<=s` follows from `c+s>=1`, because `(c+s)^2=1+2cs>=1`.

Thus

`boxed( P(Z_a>1/2)<=1/2 ).`                                                   (4.1)

At `a=1`, `s=0` and `Z_1=1/2` deterministically.

## 5. Uniform cone-tip ceiling

Split according to `Z_a<=1/2`.  By monotonicity of `g`,

`g(Z_a)<=g(1/2)` on the first event, while globally `g(Z_a)<=1/2` by (3.1).  Hence for `0<a<1`, using (4.1),

`E g(Z_a)`
` <= g(1/2) + (1/2-g(1/2)) P(Z_a>1/2)`
` <= [g(1/2)+1/2]/2`.

The same final bound also holds at `a=1`, since there `E g(Z_1)=g(1/2)<[g(1/2)+1/2]/2`.

Multiply by `6sqrt(2)` and use (3.2):

`boxed( C(a) <= [C_-+3sqrt(2)]/2,  0<a<=1. )`                               (5.1)

Fleet03 proved `C_-<97/24<3sqrt(2)`.  Therefore

`C(a) < 97/48 + 3sqrt(2)/2 < 3sqrt(2)`

uniformly in the full coupled rotation parameter.  The last inequality is exactly the already-certified comparison `97/24<3sqrt(2)` divided by two and added to `3sqrt(2)/2`.

This closes the specific next implication left open in fleet03/B17's 15:04Z handoff: `sup_{0<a<1} C(a)<3sqrt(2)` analytically, with no numerical monotonicity assumption.

## 6. Exact finite provenance and scope

Fleet03's exact finite family uses one physical row `r`, `m` rows `b/sqrt(m)`, and `m` rows `c/sqrt(m)` with a Parseval frame `R_m`.  Therefore

`A_{a,m}=R_m diag(1,1,-1) R_m^T`

has nonzero spectrum exactly `{1,1,-1}` for every `m`, and for centered unit-interval physical coordinates

`Q_{a,m}=-aX^2+2sqrt(1-a^2)X B_m+aB_m^2+C_m^2`.

For each fixed `a>0`, fleet03 proved `p_{Q_{a,m}}(0)->C(a)`.  Combining with (5.1), every fixed-angle one-heavy N3 sequence has limiting cone tip uniformly separated from `3sqrt(2)` by the explicit constant above.

What is **not** proved here:

- no global-in-output bound for the coupled interior `0<a<1`;
- no uniform-in-`a,m` local-CLT transfer as `a=a_m` degenerates;
- no theorem for two or more macroscopic shared rows;
- no unrestricted QFORM continuity claim;
- no claim that `3sqrt(2)` is the unrestricted sharp universal constant.

The strongest source-valid universal lower obstruction remains `C_univ>=3sqrt(2)` from exact diffuse cube frames.

## 7. Required fleet02/B17 result applied to an actual inequality

Newest designated partner source read in this run:

`yspennstate/math-open-problems@2f227775f53ca554a645737b9dbad18e25437d74`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T151331Z-fleet02-B17-QFORM-auto11/REPORT.md`.

That theorem proves, for arbitrary cap-one heavy `X_f`, centered unit-interval rank-one banks, and coefficients at least one,

`||p_(alpha X_f^2 + lambda S_a^2 - mu T_b^2)||_infinity`
` <= K_* := (pi/2)(sqrt(2)+2^(1/4)) < 3sqrt(2)`.

Apply it to the concrete finite profiles

`a_vec=(1,1)/sqrt(2)`, `b_vec=(2,1,2)/3`,

with

`S=(U_1+U_2)/sqrt(2)`,
`T=(2V_1+V_2+2V_3)/3`,
`Q_sep=X_f^2+S^2-T^2`.

The physical matrix is

`A_sep=diag(1, a_vec a_vec^T, -b_vec b_vec^T)`,

so its nonzero spectrum is exactly `{1,1,-1}`.  The partner theorem gives the actual target-level inequality

`boxed( ||p_Qsep||_infinity <= K_* = 4.089443637123813... < 3sqrt(2). )`

This is a global comparator, whereas (5.1) controls the cone tip of the genuinely coupled N3 family.  The comparison isolates the remaining unpaid mechanism: if one-heavy N3 can challenge `3sqrt(2)`, it must do so through an **off-zero coupled peak**, not through the cone tip.

## 8. Corrections preserved

No use is made of any refuted route: no law-uniform stationary-phase decay, no arbitrary-joint coarea bound, no post-rotation independence, no positive conditional-cap moment premise, no bounded-fragment-count reduction, no universal single physical minor/cross-cut, and no claim that the diagonal `pi` constant is universal.

Sources pinned for this report:

- fleet03/B17 one-heavy N3 optimizer and endpoint certificate: `math-open-problems@4e3db9a1284f35692c3d8b1c279aedb5dd5cc626`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T150436Z-fleet03-B17-QFORM-auto11/REPORT.md`;
- designated fleet02/B17 newest unequal-bank global theorem: `math-open-problems@2f227775f53ca554a645737b9dbad18e25437d74`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T151331Z-fleet02-B17-QFORM-auto11/REPORT.md`.
