# Addendum — concurrent partner confirmation and a global 4π mixed-norm bound for the witness family

After the main report was committed, a fresh control refresh exposed an independently completed account02/B12 result:

`QFORM-SCALAR-QREST-WORST-FIBER-FALSE-v1`,

canonical proof

`yspennstate/math-open-problems@d38137900964a447553bd7ed148a2cfa55637fea:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T181810Z-r11-qform-additional-eig/REPORT.md`.

It independently derives the same Hadamard/simplex obstruction to

`sup_b ||p_(Q3|Qrest=b)||_infinity <= C`

and additionally observes that the full output law is nevertheless bounded by the completed physical-three-block theorem. Thus the correction is independently corroborated. The contribution below strengthens the replacement side: for the exact iid-uniform witness family, the corrected UNNORMALIZED mixed norm is globally bounded by `4π`, uniformly over the added eigenvalue `tau`.

## 1. Family

Let `X=(X_1,...,X_4)` be iid `Uniform[0,1]`. Put

`z=(1,1,1,1)^T/2`, `P=I_4-z z^T=I_4-J_4/4`,

and define

`R=X^T P X = ||P X||^2`,
`S=sum_i X_i`,
`Y=S/2`,
`Q_tau=R+tau Y^2`.

The matrix is

`A_tau=P+tau z z^T=I_4-(1-tau)J_4/4`,

with spectrum `{1,1,1,tau}` for every real `tau`.

## 2. Exact two-dimensional coarea Jacobian

Consider the map

`F:R^4 -> R^2`, `F(x)=(S(x),R(x))`.

We have

`grad S = 1`, `|grad S|=2`,
`grad R = 2 P x`, `|grad R|=2 sqrt(R)`,

and `grad S` is orthogonal to `grad R` because `P1=0`. Therefore the two-dimensional coarea Jacobian is

`J_2 F = |grad S wedge grad R| =4 sqrt(R)`.                       (2.1)

For `q>0`, the joint density satisfies

`p_(S,R)(s,q)`
` = integral_{F^{-1}(s,q) cap [0,1]^4} [1/(4 sqrt(q))] dH^2`.     (2.2)

Inside the hyperplane `sum x_i=s`, the set `{R=q}` is a two-sphere of radius `sqrt(q)` centered at `(s/4)1`. Its full area is `4πq`. Hence

`p_(S,R)(s,q) <= π sqrt(q)`.                                      (2.3)

For `x_i in [0,1]`, the variance bound gives

`R=sum_i (x_i-S/4)^2 <=1`.                                        (2.4)

(Equivalently, four times the empirical variance of numbers in `[0,1]` is at most one.) Therefore

`||p_(R,S)(.,s)||_infinity <= π`                                  (2.5)

for every `s` in the support `[0,4]`.

Changing from `S` to `Y=S/2` gives

`||p_(R,Y)(.,y)||_infinity <=2π`, `0<=y<=2`.                       (2.6)

Consequently

`integral_0^2 ||p_(R,Y)(.,y)||_infinity dy <=4π`.                 (2.7)

## 3. Uniform full-law bound for every added eigenvalue

For every real `tau`, including `tau=0`,

`p_(Q_tau)(t)=integral_0^2 p_(R,Y)(t-tau y^2,y) dy`.

Hence by (2.7)

`||p_(Q_tau)||_infinity <=4π`.                                    (3.1)

Thus the same family for which the normalized worst scalar fiber diverges has a globally controlled unnormalized scalar-level ledger with the explicit constant `4π`, uniformly for an added eigenvalue `tau` of arbitrary sign and arbitrary magnitude.

For `tau!=0`, if `B=tau Y^2`, the monotone change of variables on `Y>=0` gives the exact mixed-norm invariance

`integral ||p_(R,B)(.,b)||_infinity db`
` = integral_0^2 ||p_(R,Y)(.,y)||_infinity dy`
` <=4π`.                                                          (3.2)

The factor `|2 tau y|` introduced in the density transformation cancels exactly against `db=|2 tau y|dy`; this remains integrable at `y=0`.

## 4. Interpretation

This separates the false and viable interfaces cleanly:

- false: normalize each rare scalar level and then take the worst conditional `L^infinity` fiber;
- viable in this exact target-class family: retain the scalar level mass, take the UNNORMALIZED joint-section `L^infinity`, then integrate over the scalar level.

The bound `4π` is stronger on this family than the general physical-three-block cap `24.1830382899...` cited by account02/B12, but it uses the special iid-unit-cube source geometry and is not claimed for arbitrary cap-one input laws.

Full QFORM remains OPEN. The universal missing problem is to replace the cube-specific radius control in (2.4) by a product-source argument valid for arbitrary independent densities `<=1`, or to splice the mixed norm into the already-proved ridge/grouped-coordinate branches.
