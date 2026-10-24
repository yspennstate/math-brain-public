# QFORM-ONE-HEAVY-MAJORITY-ALL-FINITE-BANKS-NOESCAPE-v1

Run: `20260923T045156Z-account02-B17-QFORM-auto11`
Programme: `QFORM-DENSITY-3EIG-20260922`
Status: NEW SUPPORTING THEOREM. The unrestricted QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

## 1. Exact source-valid branch

For every integer `m>=1`, let

`A_m = diag(1,J_m/m,-J_m/m)`.

Its exact nonzero spectrum is `{1,1,-1}`. Put an arbitrary probability density `0<=f<=1` on the singleton coordinate and independent centered unit intervals on the two `m`-coordinate banks. Write

`S_m=m^(-1/2) sum_(i=1)^m U_i`, `T_m=m^(-1/2) sum_(i=1)^m V_i`,

where all `U_i,V_i` are independent `Unif[-1/2,1/2]`. Then

`Q_(m,f)=X_f^2+S_m^2-T_m^2`.

I use the completed predecessor theorem `QFORM-ONE-HEAVY-MAJORITY-EXACT-EXTREMIZER-v1`, `yspennstate/math-open-problems@189fc052089ae2d3237bc0865b290b01b26a6513`, which proves for every finite `m`

`sup_(0<=f<=1, int f=1) ||p_(Q_(m,f))||_infinity = C_m := p_(U^2+S_m^2-T_m^2)(0)`,

where `U~Unif[-1/2,1/2]`. Thus it remains only to bound this scalar all-uniform quantity.

## 2. New angular lemma

Let `h_m` be the density of `S_m`. It is even and nonincreasing on `[0,infinity)`, since it is a normalized convolution of centered interval densities. The density of `T_m^2` at `z>0` is

`h_m(sqrt(z))/sqrt(z)`.

Therefore

`C_m = int_(|u|<=1/2) int_R h_m(s) h_m(sqrt(u^2+s^2))/sqrt(u^2+s^2) ds du`.  (2.1)

Use polar coordinates `u=r cos(theta)`, `s=r sin(theta)`. The radial Jacobian cancels the factor `1/r`, and the physical constraint `|u|<=1/2` is `r<=(2|cos(theta)|)^(-1)`. Since the integrand is nonnegative, dropping that radial cutoff gives

`C_m <= int_0^(2pi) int_0^infinity h_m(r|sin(theta)|) h_m(r) dr dtheta`.  (2.2)

The set `{|sin(theta)|<1/2}` in `[0,2pi)` has measure `2pi/3`, and its complement has measure `4pi/3`. Monotonicity of `h_m` therefore yields

`C_m <= (2pi/3) h_m(0) int_0^infinity h_m(r)dr + (4pi/3) int_0^infinity h_m(r)h_m(r/2)dr`.

Because `h_m` is even and normalized,

`C_m <= (pi/3) h_m(0) + (4pi/3) I_m`,

where

`I_m := int_0^infinity h_m(r)h_m(r/2)dr`.  (2.3)

There is an exact probabilistic interpretation of the second term. If `S_m'` is an independent copy of `S_m`, then

`p_(S_m-2S_m')(0) = int_R h_m(2x)h_m(x)dx = I_m`,  (2.4)

where the last equality follows from evenness and the substitution `r=2x`.

## 3. Ball/Rogozin projection bounds close every finite bank

For independent centered unit intervals, the sharp one-dimensional projection bound gives

`||p_(sum_j a_j U_j)||_infinity <= sqrt(2)/||a||_2`.  (3.1)

This is the standard Rogozin/Ball cube-slicing endpoint and is also recorded in the QFORM archive, e.g. account03/B02 report blob `675acba5de420f04d0faba155f6a706a97e73a27`.

For `S_m`, the coefficient vector is `m^(-1/2)(1,...,1)`, whose Euclidean norm is one. Hence

`h_m(0)=||h_m||_infinity <= sqrt(2)`.  (3.2)

For `S_m-2S_m'`, the `2m`-coordinate coefficient vector is

`m^(-1/2)(1,...,1,-2,...,-2)`,

whose Euclidean norm is `sqrt(5)`. Thus

`I_m=p_(S_m-2S_m')(0) <= sqrt(2/5)`.  (3.3)

Substituting (3.2)-(3.3) into (2.3) gives, uniformly for every `m>=1`,

`C_m <= C_bank := (pi sqrt(2)/3)(1+4/sqrt(5)) = 4.130184516931749... < 3sqrt(2)`.  (3.4)

The strict comparison is elementary and does not rely on decimals. Since `pi<22/7`, it is enough to show

`22(1+4/sqrt(5))<63`,

equivalently `88<41sqrt(5)`; squaring gives `7744<8405`.

Combining (3.4) with the predecessor exact-extremizer theorem proves

`sup_(m>=1) sup_(0<=f<=1,int f=1) ||p_(X_f^2+S_m^2-T_m^2)||_infinity <= (pi sqrt(2)/3)(1+4/sqrt(5)) < 3sqrt(2)`.  (3.5)

Thus the entire exact finite one-heavy majority-sign equal-bank family is excluded as a witness above the current `3sqrt(2)` lower obstruction. This is stronger than the preceding separate calculations for `m=1,2` and stronger than the large-`m` Edgeworth argument: no intermediate finite-bank overshoot exists in this branch.

## 4. Required newest-Claude result applied

At `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md` Theorem C proves the ruled one-sheet estimate

`p_Q(s)<=pi sqrt(2), s>=0`,

for exact rank-three signature `(+,+,-)` forms (with the later source clarification on allowable linear terms). In the present source-valid branch the exact-extremizer theorem places the global optimum at `s=0`, so Theorem C gives the genuine finite inequality

`C_m<=pi sqrt(2)`.

The new angular/projection argument sharpens that applicable source bound to (3.4), crossing below `3sqrt(2)`. The fact that the more general `pi sqrt(2)` source constant does not itself cross the candidate sharp threshold is a limitation of that auxiliary proof constant, not a QFORM counterexample.

## 5. Designated partner result applied

The latest completed `account03/B17` result is `math-open-problems@0a23c8b4c6e8f1ce727bd99d55ed6258ce18ade2`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T033115Z-account03-B17-QFORM-r24/REPORT.md`. It proves that an exact fully rotated three-bank family with order-`1/m` remote fragmented mass at distance `Theta(sqrt(m))` has, for `a=c=1`, global limiting ceiling

`2.4870582495390534... < 3sqrt(2)`.

Together with (3.5), two complementary candidate escapes are now excluded: arbitrary cap-one fragmentation of one macroscopic majority-sign coordinate for every finite bank size, and fixed-activity remote fragmentation of the partner's genuinely rotated three-bank architecture.

## 6. Scope and next unpaid implication

This theorem does not prove the full universal QFORM bound and does not prove that `3sqrt(2)` is the universal sharp constant. It uses a special exact matrix family and fixed centered-unit-interval bank laws, while allowing the singleton heavy law to be completely arbitrary under the cap-one hypothesis. No post-rotation independence, hidden moments, bounded support for the arbitrary heavy law, arbitrary-joint coarea estimate, or law-uniform pointwise oscillatory decay is used.

The finite-bank scalar obstruction is now fully paid. A sharp witness above `3sqrt(2)`, if one exists, must leave this one-heavy majority equal-bank mechanism. The next B17 search should use at least two genuinely non-collinear/shared-coordinate macroscopic rows, a multiscale/growing-activity fragmentation not reducible to the partner's compound-Poisson bank shifts, or another coupled geometry. A witness above `3sqrt(2)` would refute that proposed sharp constant but would still not by itself refute existence of a larger universal QFORM constant.
