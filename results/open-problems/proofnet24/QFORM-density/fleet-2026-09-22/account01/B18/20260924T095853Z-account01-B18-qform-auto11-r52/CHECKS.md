# account01/B18 r52 checks

Marker: `QFORM_B18_R52_PLANAR_CHAMBER_CHECK_PASS`

## 1. Exact matrix identities

For

`H=[[0,0,a,0],[0,0,p,q],[a,p,b,c],[0,q,c,e]]`,

set

`R=[[0,0,a,0],[0,0,p,0],[a,p,b,c],[0,0,c,0]]`.

With `u=(0,0,1,0)^T` and `z=(a,p,b/2,c)^T`, direct expansion gives

`R=u z^T+z u^T`,

hence `rank(R)<=2`.

Also

`H-R` is zero off the `(X2,V)` indices and its active block is

`K=[[0,q],[q,e]]`.

The two eigenvalues of `K` are

`(e +/- sqrt(e^2+4q^2))/2`,

so

`||K||op=(|e|+sqrt(e^2+4q^2))/2`.

Thus `s3(H)<=||K||op`. If `|q|<s=s3(H)`, squaring the inequality after isolating the positive square-root term gives

`|e|>=s-q^2/s`.

## 2. Main-cross lower bound

Subtracting the right self block gives the symmetric cross matrix

`[[0,D],[D^T,0]]`, `D=[[a,0],[p,q]]`.

The subtraction target has rank at most two, hence

`s3(H)<=||D||op<=||D||F`.

After choosing the larger physical cross row as the first row,

`p^2+q^2<=a^2`,

so `||D||F<=sqrt(2)a` and `a>=s/sqrt(2)`.

## 3. Radial reciprocal integral

If `g` is any probability density on `R^2` with `0<=g<=M`, radial rearrangement puts the cap `M` on a centered disk of radius `R=(pi M)^(-1/2)`. Therefore

`int g(u)/||u|| du <= M * 2pi R = 2sqrt(pi M)`.

With the LPP pair cap `2`, the transformed density cap for `U=DZ` is `M=2/|det D|`; multiplying by the conditional normalized-linear cap factor `1/sqrt(2)` gives exactly

`2sqrt(pi)/sqrt(|det D|)`.

## 4. Square completion

At fixed `X2=x`, put

`W=V+(c/e)L+(q/e)x`,

`Hx=X1+[(p-cq/e)/a]x`.

Expanding gives exactly

`2a Hx L +(b-c^2/e)L^2-(q^2/e)x^2+eW^2`

`=2aX1L+2pxL+2qxV+bL^2+2cLV+eV^2`.

The map `(L,V)->(L,W)` has determinant one. Scaling `(L,W)` to `(aL,sqrt(|e|)W)` therefore changes a pair density cap `2` to at most

`2/(|a|sqrt(|e|))`.

Applying the pinned planar bound `3*2^(2/3)K^(2/3)` yields

`3*2^(4/3)|a|^(-2/3)|e|^(-1/3)`.

## 5. Optimizer constants

For the general planar chamber define

`A=2^(5/4)sqrt(pi)`, `B=3*2^(5/3)`.

The cross branch is `A delta^(-1/2)/s`; the square branch is `B(1-delta^2)^(-1/3)/s` on `0<delta<1`.

The unique crossing satisfies

`pi^3(1-delta^2)^2=3^6*2^(5/2)delta^3`.

High-precision numerical root and value:

`delta_*=0.1911071429483536143393120682551099734053610010222391`

`C_planar=9.6432621030094153917812454881497240104910931644188564`.

For the literal fresh-partner splice, the branches are

`2sqrt(pi)delta^(-1/2)/s`,

`3*2^(4/3)(1-delta)^(-1/3)/s`.

The crossing equation is

`pi^3(1-delta)^2=2916 delta^3`,

with

`delta_partner=0.19093149121716331031245926923572304130326749679015182`,

`C_partner=8.1127136978845698322619928836029023315585617305295173`.

Using the planar-specific exact residual `1-delta^2` instead gives

`delta_orth_exact=0.21318369104964173283517597191162922912234938912650972`,

`C_orth_exact=7.6776435165987407380048116957572682712109618013942714`.

## 6. Numerical algebra regression

A 10,000-sample random regression drew positive `a`, a second cross row `(p,q)` with Euclidean norm at most `a`, and arbitrary Gaussian `b,c,e`. For every sample it checked

`s3(H)<=sqrt(2)a`,

`s3(H)<= (|e|+sqrt(e^2+4q^2))/2`,

and, whenever `|q|<s3(H)`,

`|e|>=s3(H)-q^2/s3(H)`.

Maximum observed violations of the first two inequalities were `0`; the minimum slack in the third was approximately `1.14e-6` (positive). These are regression checks only; the proof is the exact rank-two approximation argument above.

## 7. Scope checks

PASS: all conditioning is on literal original coordinates (`X2` only in the square branch).

PASS: the right-plane rotation is used only after replacing the right projected pair by its valid unconditional joint density cap; no independence of the rotated pair is asserted.

PASS: the nonzero crossing `q` is retained in both the deterministic and analytic calculations.

PASS: arbitrary coefficients `p,b,c,e` remain in the theorem.

PASS: no arbitrary-joint indefinite coarea estimate is invoked.

PASS: no generic continuity claim is made.
