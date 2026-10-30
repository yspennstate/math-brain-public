# QFORM B17 — Gaussian spectral-slack rigidity and dense rotated witnesses

Run: `20260923T233601Z-fleet01-B17-QFORM-auto11`  
Account/slot: `fleet01/B17`  
Status: `PROVED_SUPPORTING_SHARP_WITNESS_THEOREM`; unrestricted QFORM remains **OPEN**; unrestricted continuity remains **OPEN**; `WITHOUT_VERIFIED_BRAIN`.

## 1. Result in one line

For an isotropic Gaussian rank-three limit of signature `(2,1)` with eigenvalue magnitudes `a,b,c >= 1`, the cone-tip density admits an exact angular formula and obeys the sharp fixed-spectral-excess inequality

`p(0) <= 6/sqrt(2+S)` for variance `1/12`, where `S=(a-1)+(b-1)+(c-1)`.

Equality for fixed `S` occurs exactly when the two same-sign eigenvalues stay at threshold and all excess is put into the lone-sign eigenvalue: `(a,b,c)=(1,1,1+S)` (up to reversing all signs / relabelling the two equal-sign directions). This one-parameter family is globally tip-maximal, not merely cone-tip controlled. It has an explicit entrywise-dense rotated finite product-cube realization with exact nonzero spectrum `{1,1,-(1+delta)}` for every finite repetition count and every `0 <= delta < 1`.

At `delta=0` this recovers the source-valid lower obstruction `C_univ >= 3 sqrt(2)`. More importantly for sharp-proof design, any Gaussianized rank-three near-extremizer with spectral excess bounded away from zero has a quantitative gap below `3 sqrt(2)`.

## 2. Exact Gaussian cone-tip formula

Let

`G=(G_1,G_2,G_3) ~ N(0,sigma^2 I_3)`

and

`Q_{a,b,c}=a G_1^2+b G_2^2-c G_3^2`,  `a,b,c>0`.

At output zero,

`p_{a,b,c}(0)=int delta(a x^2+b y^2-c z^2) phi_sigma(x,y,z) dx dy dz`.

Make the exact change of variables

`u=sqrt(a)x`, `v=sqrt(b)y`, `w=sqrt(c)z`.

The Jacobian is `(abc)^(-1/2)` and the quadratic surface becomes `u^2+v^2-w^2=0`. In cylindrical coordinates

`u=r cos(theta)`, `v=r sin(theta)`,

integration in `w` against `delta(r^2-w^2)` contributes the two roots `w=+/-r`, each with derivative magnitude `2r`; the cylindrical Jacobian `r` cancels the resulting reciprocal `r`. Hence

`p_{a,b,c}(0)`

` = [1/(4 pi sigma^2 sqrt(abc))]`

`   * int_0^{2pi} [cos^2(theta)/a + sin^2(theta)/b + 1/c]^(-1/2) dtheta`

and therefore

**(2.1)**

`p_{a,b,c}(0)`

` = [1/(4 pi sigma^2)] int_0^{2pi}`

`   dtheta / sqrt(ab + bc cos^2(theta) + ac sin^2(theta)).`

This formula is rotation-invariant because the Gaussian source is isotropic, so it applies to every orthogonal conjugate of `diag(a,b,-c)`.

For `a=b=c=1`, the denominator is identically `sqrt(2)` and

`p_{1,1,1}(0)=1/(2 sqrt(2) sigma^2)`.

At the cube-CLT variance `sigma^2=1/12`,

**(2.2)** `p_{1,1,1}(0)=3 sqrt(2)`.

## 3. Sharp spectral-excess inequality

Assume now `a,b,c >= 1` and set

`alpha=a-1`, `beta=b-1`, `gamma=c-1`, `S=alpha+beta+gamma`.

For

`D(theta)=ab+bc cos^2(theta)+ac sin^2(theta)`,

a direct expansion gives

`D(theta)-(2+S)`

` = alpha sin^2(theta)+beta cos^2(theta)`

`   + alpha beta + beta gamma cos^2(theta)+alpha gamma sin^2(theta)`

` >= 0`.

Substitution into (2.1) yields

**Theorem A (sharp fixed-excess cone-tip bound).**

`p_{a,b,c}(0) <= 1/[2 sigma^2 sqrt(2+S)]`.

For `sigma^2=1/12`,

**(3.1)** `p_{a,b,c}(0) <= 6/sqrt(2+S)`.

For fixed `S`, equality in the integral bound requires the displayed nonnegative remainder to vanish for every `theta`. This forces `alpha=beta=0`; conversely `a=b=1, c=1+S` makes `D(theta)=2+S` identically. Thus the fixed-excess optimizer is exact:

**(3.2)**

`sup_{a,b,c>=1, a+b+c-3=S} p_{a,b,c}(0)=6/sqrt(2+S)`,

attained by `(a,b,c)=(1,1,1+S)`.

In particular, if a Gaussian rank-three cone tip is at least `(1-eta) 3sqrt(2)`, then necessarily

**(3.3)**

`S <= 2[(1-eta)^(-2)-1]`.

So Gaussianized near-sharp witnesses must have all three active eigenvalue magnitudes approaching the threshold surface. A reduction that introduces a fixed positive spectral slack cannot remain sharp.

Along the exact optimizer line `c=1+delta`,

`6/sqrt(2+delta)=3sqrt(2)(1+delta/2)^(-1/2)`

` =3sqrt(2)[1-delta/4+3delta^2/32+O(delta^3)]`.

The first sharpness loss is therefore `delta/4` in relative density.

## 4. The optimizer line is globally tip-maximal

The previous section is a cone-tip theorem. For the optimizing line it upgrades to the actual global norm.

Let

`Q_delta=G_1^2+G_2^2-(1+delta)G_3^2`, `delta>=0`.

Put

`W=G_1^2+G_2^2`, `V=(1+delta)G_3^2`.

Then `W` is exponential with rate `lambda=1/(2sigma^2)`, while `V` has the scaled chi-square-one density, which is strictly decreasing on `(0,infinity)`.

For `t>=0`, independence gives

`p_{Q_delta}(t)=int_0^infinity f_W(t+v)f_V(v)dv`

`                 =e^{-lambda t} p_{Q_delta}(0)`.

For `r>0`,

`p_{Q_delta}(-r)=int_0^infinity f_W(u)f_V(u+r)du`

`                  <=int_0^infinity f_W(u)f_V(u)du`

`                  =p_{Q_delta}(0)`.

Therefore

**Theorem B (global spectral-slack stress family).**

`||p_{Q_delta}||_infty=p_{Q_delta}(0)=1/[2 sigma^2 sqrt(2+delta)]`.

At `sigma^2=1/12`,

**(4.1)** `||p_{Q_delta}||_infty=6/sqrt(2+delta)`.

This is an exact global statement, not a numerical cone-tip sample.

## 5. Exact entrywise-dense rotated finite product realization

Use the rational orthogonal matrix

`O=(1/7) [[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`

and the tetrahedral Parseval block

`R0=(1/2) [[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1]]`.

Direct multiplication gives

`O^T O=I_3`, `R0^T R0=I_3`.

For `0 <= delta < 1`, let

`B_delta=O^T diag(1,1,-(1+delta)) O`.

Its spectrum is exactly `{1,1,-(1+delta)}`. The physical four-coordinate core is

`M_delta=R0 B_delta R0^T`

`=(1/196) *`

`[[-95-121d,  71+11d, -105-77d,  61+55d],`

` [ 71+11d, 145-d,      -35+7d,   39-5d ],`

` [-105-77d, -35+7d,     49-49d, 119+35d],`

` [ 61+55d,  39-5d,     119+35d,  97-25d]]`,

where `d=delta`.

Every displayed entry is nonzero throughout `0 <= delta < 1`. Thus this is not a diagonal witness and not a sparse physical-coordinate artifact.

For `m>=1`, stack `m` copies of `R0/sqrt(m)` to obtain `R_m in R^{4m x 3}`. Then

`R_m^T R_m=I_3`,

and define

`A_{m,delta}=R_m B_delta R_m^T`.

Every physical entry of `A_{m,delta}` is one of the entries of `M_delta/m`, hence every entry is nonzero. Its exact nonzero spectrum is

**(5.1)** `spec_nonzero(A_{m,delta})={1,1,-(1+delta)}`.

Take the `4m` physical coordinates independent `Unif[-1/2,1/2]`. Writing the inputs in four-coordinate blocks `X^(ell)`,

`Y_m=R_m^T X=(1/sqrt(m)) sum_{ell=1}^m R0^T X^(ell)`.

Each summand is centered with covariance `I_3/12`, so the multivariate CLT gives

`Y_m => G ~ N(0,I_3/12)`.

Therefore

`X^T A_{m,delta} X = Y_m^T B_delta Y_m`

` => G^T B_delta G`

and isotropy identifies the limit with `Q_delta` from Section 4.

No density convergence is required for the lower obstruction. If `p_{m,delta}` denotes a finite-stage density, then for each `h>0`,

`||p_{m,delta}||_infty >= P(|Q_{m,delta}|<=h)/(2h)`.

Weak convergence and continuity of the limiting law at `+/-h` imply

`liminf_m ||p_{m,delta}||_infty >= P(|Q_delta|<=h)/(2h)`.

Letting `h downarrow 0` gives

**(5.2)**

`liminf_m ||p_{m,delta}||_infty >= 6/sqrt(2+delta)`.

At `delta=0`,

**(5.3)** `C_univ >= 3sqrt(2)`.

The new information is the exact spectral-slack rigidity and dense one-parameter stress family; the lower obstruction itself was already known in the programme.

## 6. Required application of completed partner fleet02/B17 result

Consumed completed partner source:

`yspennstate/math-open-problems@082c1e2c3e02ce50f8f215d0f6d1e88120a30831`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T225735Z-fleet02-B17-QFORM-auto11/REPORT.md`.

Its proved theorem states that for three disjoint centered-unit-interval banks with `m_j>=2` and aligned signature `{1,1,-1}`, the actual **global** output density norm is attained at zero. I apply that theorem to a concrete finite target instance, rather than merely cite it abstractly.

Let `U_{jk}` (`j=1,2,3`, `k=1,2`) be six independent `Unif[-1/2,1/2]` variables and

`Y_j=(U_{j1}+U_{j2})/sqrt(2)`.

Set

`Q_2=Y_1^2+Y_2^2-Y_3^2`.

Its physical matrix is

`A_2=diag(J_2/2, J_2/2, -J_2/2)`

and has exact nonzero spectrum `{1,1,-1}`. The partner theorem gives the actual equation

**(6.1)** `||p_{Q_2}||_infty=p_{Q_2}(0)`.

Now compute the right side exactly. The common bank density is

`g(y)=sqrt(2)(1-sqrt(2)|y|)_+`.

Cone coarea gives

`p_{Q_2}(0)=int_0^{2pi} int_0^infinity`

`             g(r cos theta)g(r sin theta)g(r) dr dtheta`.

Set `t=sqrt(2)r`. Because `0<=|cos theta|,|sin theta|<=1`, the support cutoff from `g(r)` already forces `0<=t<=1`. By quadrant symmetry,

`p_{Q_2}(0)`

`=8 int_0^{pi/2} int_0^1`

`  (1-t cos theta)(1-t sin theta)(1-t) dt dtheta`.

The inner integral equals

`1/2-(cos theta+sin theta)/6+(sin theta cos theta)/12`.

Using

`int_0^{pi/2} cos=1`, `int_0^{pi/2} sin=1`, `int_0^{pi/2} sin cos=1/2`,

we get the exact value

**(6.2)** `p_{Q_2}(0)=2pi-7/3=3.949851973846253...`.

Combining (6.1) and (6.2),

**(6.3)**

`||p_{Q_2}||_infty=2pi-7/3 < 3sqrt(2)`.

This is a concrete use of the completed partner theorem at an actual target inequality. It is a control family, not the main rotated theorem above.

## 7. Consequences for a proposed sharp proof

1. `3sqrt(2)` remains the strongest source-valid lower obstruction in this branch.
2. Within the rank-three isotropic Gaussian CLT regime, threshold spectrum is rigid: if the total excess of the three active absolute eigenvalues is `S>0`, the cone tip loses at least the explicit factor `sqrt(2/(2+S))`.
3. The loss is sharp at fixed `S`, realized by putting all excess into the lone-sign eigenvalue.
4. The sharp fixed-excess optimizer has a globally tip-maximal limiting law and an exact finite entrywise-dense rotated cube realization. Hence this constraint is not a diagonal-coordinate artifact.
5. A proof strategy that perturbs/rescales the three active eigenvalues away from unit threshold must track that loss if it aims at the sharp constant.
6. This does **not** rule out an off-zero peak for a general rough product law, several macroscopic shared rows, non-Gaussian/non-CLT diffuse limits, additional active spectrum, or the remaining genuinely nonaligned two-sheet configurations.
7. It does not prove `C_univ=3sqrt(2)`; it only sharpens the witness-side geometry.

## 8. Corrections and scope preserved

The live correction inbox was read before this proof. In particular this report respects:

- `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`: no universal `C=pi` claim is used; the valid lower obstruction is `3sqrt(2)`.
- `QFORM-TWOSHEET-XRAY-ONLY-FALSE`: no generic two-sheet X-ray cap is used. Global tip maximality in Section 4 uses the actual independent exponential-minus-chi-square structure; Section 6 uses the partner's proved aligned-bank convolution theorem.
- no post-rotation independence is asserted for the finite dense family; independence is retained only in the original physical coordinates. The Gaussian limit is rotated only after the CLT, where isotropy makes that legal.
- density boundedness and continuity are kept separate. The scoped Gaussian and finite aligned-bank laws above have continuous representatives, but no unrestricted continuity claim is made.

## 9. Source pins

Owner programme: `QFORM-DENSITY-3EIG-20260922`, live owner continuation revision `2026-09-22.15`.

Startup control head observed: `dccb7b946cb35dee432bc582b99e4e85d33688f9`.

Fresh control head before publication write: `ece2ebddbe98699118bf529b44432865e9d60992`.

Partner theorem actually applied: `math-open-problems@082c1e2c3e02ce50f8f215d0f6d1e88120a30831`, exact report path listed in Section 6.

This report is a supporting theorem/witness calculation. Full QFORM and full-target continuity remain open.
