# QFORM B17 — unequal opposite cube banks lie strictly below the 3sqrt(2) obstruction

Run: `20260923T134058Z-fleet01-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet01/B17`  
Assignment: sharp constant and witnesses  
Classification: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. New theorem

Let `U_0,U_1,...,U_m,V_1,...,V_n` be independent `Unif[-1/2,1/2]` variables. Let

`a in R^m`, `b in R^n`, `||a||_2=||b||_2=1`,

and put

`S_a=sum_i a_i U_i`, `T_b=sum_j b_j V_j`.

For arbitrary `alpha,beta,gamma >= 1`, define

`Q = alpha U_0^2 + beta S_a^2 - gamma T_b^2`.

Equivalently, in the original physical coordinates,

`A_{a,b}=diag(alpha, beta aa^T, -gamma bb^T)`.

Its nonzero spectrum is exactly

`{alpha,beta,-gamma}`,

so every member satisfies the target three-large-eigenvalue hypothesis. The two rank-one bank blocks are generally non-diagonal in the original physical coordinates; no post-rotation independence is invoked.

### Theorem `QFORM-UNEQUAL-CUBE-BANKS-CENTERED-HEAVY-BARRIER-v1`

The law of `Q` has a continuous density, its global maximum occurs at zero, and

`||p_Q||_infinity = p_Q(0) <= K_cone <= K_sec < 3 sqrt(2)`,

where

`K_cone = pi sqrt(2)/3 + 2 int_{1/2}^1 du/(sqrt(u)sqrt(1-u^2))`

`= 3.81729234609...`,

and the completely elementary closed-form envelope is

`K_sec = pi(5sqrt(2)-2)/3 - 2sqrt(3)(sqrt(2)-1)`

`= 3.87553192410... < 3sqrt(2)`.

Thus **even when the two opposite rank-one cube banks have completely different dimensions and leverage profiles**, the centered-heavy three-eigenvalue branch stays uniformly below the existing `3sqrt(2)` obstruction.

This is stronger in scope than the previously closed identical-bank centered-heavy subcase, but it does **not** allow an arbitrary cap-one law on `U_0`; that arbitrary-heavy/unequal-bank combination remains unpaid.

## 2. Product-coordinate ingredients

Let `h_0,k_0` be the densities of `S_a,T_b`. Each `a_iU_i` and `b_jV_j` is uniform on a centered interval. Convolution preserves one-dimensional symmetric unimodality, hence `h_0,k_0` are even and nonincreasing on `[0,infinity)`.

The source-pinned Rogozin--Ball projection theorem gives, for every unit coefficient vector,

`||h_0||_infinity <= sqrt(2)`, `||k_0||_infinity <= sqrt(2)`.

A second application to the normalized self-difference gives the stronger `L^2` controls. If `S_a'` is an independent copy, then

`||h_0||_2^2 = p_{S_a-S_a'}(0)`.

But `(S_a-S_a')/sqrt(2)` is again a unit-direction projection of a centered unit cube, with coefficient vector `(a,-a)/sqrt(2)`. Therefore

`||h_0||_2^2 <= 1`.

Likewise

`||k_0||_2^2 <= 1`.

The product-projection source used here is pinned at

`yspennstate/math-open-problems@18fb381e300dd86514835d27eedcf2507ab09227`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T130245Z-fleet03-B02-QFORM-r11/REPORT.md`,

which records the Rudelson--Vershynin/Rogozin--Ball bound `sqrt(2)` for a unit linear projection of independent cap-one coordinates.

## 3. Scaling to the target eigenvalues

Set

`X=sqrt(alpha)U_0`, `Y=sqrt(beta)S_a`, `Z=sqrt(gamma)T_b`,

and let `f,h,k` be their densities. Then

`||f||_infinity = alpha^(-1/2)`,

`||h||_infinity <= sqrt(2/beta)`,

`||k||_infinity <= sqrt(2/gamma)`,

while

`||h||_2^2 <= beta^(-1/2)`, `||k||_2^2 <= gamma^(-1/2)`.

Both `f,h,k` are even and nonincreasing on the positive half-line.

## 4. Global mode is exactly at zero

Write

`A=X^2+Y^2`, `B=Z^2`, so `Q=A-B`.

For `t>0`, the density of `A` has the polar representation

`a_A(t)=(1/2) int_0^{2pi} f(sqrt(t)cos(theta)) h(sqrt(t)sin(theta)) dtheta`.

For every fixed `theta`, both absolute arguments increase with `sqrt(t)`, so symmetric unimodality makes the integrand nonincreasing in `t`. Therefore `a_A` is nonincreasing on `(0,infinity)`.

Similarly,

`b_B(t)=k(sqrt(t))/sqrt(t)`, `t>0`,

is nonincreasing.

The density of `Q=A-B` is their one-sided cross-correlation. For `s>=0`,

`p_Q(s)=int_0^infinity a_A(s+r)b_B(r)dr <= int_0^infinity a_A(r)b_B(r)dr=p_Q(0)`.

For `tau>=0`,

`p_Q(-tau)=int_0^infinity a_A(r)b_B(r+tau)dr <= p_Q(0)`.

Hence

`||p_Q||_infinity=p_Q(0)`.

This step is where centered symmetric-unimodal physical laws are used. It is not available for an arbitrary fragmented heavy law in the unequal-bank case.

Since `A` and `B` each have `L^1` densities, `p_Q=a_A * check(b_B)` is continuous. This continuity statement is only for the present explicit family; unrestricted QFORM continuity remains separate and open.

## 5. Cone integral and two-norm estimate

At the cone tip,

`p_Q(0)=int_R int_R f(x) h(y) k(sqrt(x^2+y^2))/sqrt(x^2+y^2) dx dy`.

Because `f<=alpha^(-1/2)`, enlarge its finite support to the whole line and use polar coordinates:

`p_Q(0) <= (4/sqrt(alpha)) int_0^1 I(u)/sqrt(1-u^2) du`,

where

`I(u)=int_0^infinity h(ur)k(r)dr`.

The `L^infinity` estimate gives

`I(u) <= ||h||_infinity int_0^infinity k(r)dr <= 1/sqrt(2 beta)`.

Cauchy--Schwarz and the `L^2` controls give

`I(u) <= [int_0^infinity h(ur)^2dr]^(1/2)[int_0^infinity k(r)^2dr]^(1/2)`

`<= 1/[2 sqrt(u) (beta gamma)^(1/4)]`.

Therefore, for `alpha,beta,gamma>=1`,

`I(u) <= min{1/sqrt(2), 1/(2sqrt(u))}`.

The two bounds cross exactly at `u=1/2`. Consequently

`p_Q(0)`

`<= 4 int_0^{1/2} [1/sqrt(2)] du/sqrt(1-u^2)`

`   +4 int_{1/2}^1 [1/(2sqrt(u))] du/sqrt(1-u^2)`

`= pi sqrt(2)/3 + 2 int_{1/2}^1 du/[sqrt(u)sqrt(1-u^2)]`

`=:K_cone`.

This is the sharper constant naturally produced by the two projection norms; no artificial split above `u=1/2` is needed.

## 6. Elementary closed bound below 3sqrt(2)

On `[1/2,1]`, the convex function `u^(-1/2)` lies below the chord through the endpoints:

`u^(-1/2) <= (2sqrt(2)-1)+2(1-sqrt(2))u`.

Thus

`int_{1/2}^1 du/[sqrt(u)sqrt(1-u^2)]`

`<= (2sqrt(2)-1) int_{1/2}^1 du/sqrt(1-u^2)`

`   +2(1-sqrt(2)) int_{1/2}^1 u du/sqrt(1-u^2)`

`= (2sqrt(2)-1)pi/3 +(1-sqrt(2))sqrt(3)`.

Substitution gives

`K_cone <= K_sec := pi(5sqrt(2)-2)/3 - 2sqrt(3)(sqrt(2)-1)`.

For a decimal-free strict comparison, use `pi<22/7` and `sqrt(3)>5/3`. Because the second term is negative,

`K_sec < (22/21)(5sqrt(2)-2) -(10/3)(sqrt(2)-1)`

`=(40sqrt(2)+26)/21`.

Finally

`(40sqrt(2)+26)/21 < 3sqrt(2)`

is equivalent to `26<23sqrt(2)`, which is immediate after squaring. Hence

`K_sec<3sqrt(2)`.

## 7. Exact unequal rotated stress matrix

A concrete finite source-valid example is

`a=(1,1)/sqrt(2)`,

`b=(2,1,2)/3`,

with `alpha=beta=gamma=1`. Then in six original physical coordinates,

`A = diag(1, aa^T, -bb^T)`

is exactly

```
[ 1     0     0      0      0      0   ]
[ 0    1/2   1/2     0      0      0   ]
[ 0    1/2   1/2     0      0      0   ]
[ 0     0     0     -4/9   -2/9   -4/9 ]
[ 0     0     0     -2/9   -1/9   -2/9 ]
[ 0     0     0     -4/9   -2/9   -4/9 ]
```

and has spectrum exactly

`{1,1,-1,0,0,0}`.

Both active bank eigenvectors are non-coordinate directions, with different dimensions and different leverage profiles. The theorem gives the global density inequality

`||p_{U_0^2 + ((U_1+U_2)/sqrt(2))^2 - ((2V_1+V_2+2V_3)/3)^2}||_infinity <= K_sec < 3sqrt(2)`.

This is an exact rotated-bank stress family, not a diagonal/pi calculation. It is block-rotated rather than fully dense across all physical coordinates; no stronger geometry is claimed.

## 8. Required application of fleet02/B17

The latest completed designated partner result was read from the immutable source

`yspennstate/math-open-problems@7cb56c211d314add5639e4f29d0f1058c53deebd`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/fleet02-B17-20260923T131455Z/REPORT.md`.

Its theorem `QFORM-ONE-HEAVY-MAJORITY-ALL-BANKS-BARRIER-v1` states that for every unit `a` and **arbitrary** independent density `0<=f<=1`,

`sup_f ||p_{X_f^2+S_a^2-T_a^2}||_infinity`

`= p_{U^2+S_a^2-T_a^2}(0)`.

Apply the new cone estimate above to the right-hand side with `b=a` and `alpha=beta=gamma=1`. This gives the actual improved partner inequality

`boxed: sup_{a,f} ||p_{X_f^2+S_a^2-T_a^2}||_infinity <= K_cone <= K_sec < 3sqrt(2).`

Numerically, only as a scale check,

`K_cone=3.81729234609...`,

`K_sec=3.87553192410...`,

whereas the partner's previous elementary constant was

`K_*=(pi/2)(sqrt(2)+2^(1/4))=4.08944363712...`.

So this run does not merely cite the partner: it feeds the partner's exact arbitrary-heavy extremizer reduction into a sharper cone inequality and strictly improves the completed all-bank constant.

Combining the two theorems pays two complementary faces:

1. **identical opposite banks + arbitrary cap-one heavy law:** global density `<=K_sec<3sqrt(2)`;
2. **arbitrary unequal opposite centered-cube bank profiles + centered unit-interval heavy law:** global density `<=K_sec<3sqrt(2)`.

The intersection is much larger than the old diagonal control, but neither statement implies the other.

## 9. Sharp-constant consequence and surviving gap

The source-pinned diffuse periodic cube construction at

`yspennstate/math-open-problems@15e9504309108d37a6c5f8bcacebac07eb4fe1ff`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260922T123638Z-fleet01-B17-qform-diffuse-edgeworth-v1/REPORT.md`,

has exact finite matrices with nonzero spectrum `{1,1,-1}` and densities satisfying

`p_{Q_m}(0)=3sqrt(2)[1-c/m+O(m^-2)]`

with `c>0`. Hence every universal target constant must still obey

`C_univ >= 3sqrt(2)`.

The new theorem says the entire centered-heavy unequal rank-one-bank architecture is separated from that lower obstruction by a fixed gap. Together with the partner theorem, even arbitrary fragmentation of the heavy law cannot close that gap when the two opposite banks are identical.

Therefore a witness above `3sqrt(2)`, if one exists, must use a mechanism outside both paid faces. The first sharp-witness debt is now the genuinely asymmetric combination:

**arbitrary cap-one heavy law + unequal opposite bank laws/profiles**, especially with non-collinear/shared-coordinate intermediate-leverage rows or additional active spectrum.

Nothing here proves that `3sqrt(2)` is the unrestricted sharp universal constant. A witness above it would refute sharpness at `3sqrt(2)` but would not by itself refute existence of a larger universal QFORM constant.

## 10. Correction discipline

The argument stays in original physical product coordinates. It does not use:

- the refuted arbitrary-joint coarea density bound;
- post-rotation independence;
- a conditional-density moment bound;
- a pointwise stationary-phase estimate;
- a bounded-fragment-count reduction;
- a universal good coordinate minor or single Schur-pivot premise.

The live small-pivot/rowwise-split correction concerns a different structural mechanism and is not invoked. The exact spectrum of the stress family is checked before the density estimate.

Full QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN and separate**.
