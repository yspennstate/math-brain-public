# QFORM B15 — rough ruled trace and continuity closure

**Run:** `20260922T232152Z-account04-B15-ruled-trace-regularity-r5`  
**Account/slot:** account04/B15  
**Status:** `ROUGH_ONE-SHEET_TRACE_PROVED / POINTWISE-C0-CLOSURE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-22T23:21:52Z.

## 1. Target and source state

The owner target remains the universal essential bound for the density of
[
Q=X^TAX
]
when the real coordinates of (X) are independent with probability densities (0le f_ile1), and (A=A^T) has at least three eigenvalues of modulus at least one. Continuity is tracked separately.

Fresh owner control was revision `2026-09-22.15`. The live correction inbox was consumed at blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. In particular, this report does not infer a cone trace from an arbitrary bounded projected density, does not rotate independence, and does not call a half-line theorem a full rank-three theorem.

The ruled calculation comes from
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The rough-product approximation used below was proved in account04/B13 at
`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`,
report blob `63f4e0656fe110e0596254283be8e8e1e8b82ac6`.

The completed account01/B15 results actually applied are:

1. fixed-instance (C_0) closure and leave-one-out stability,
   `yspennstate/math-open-problems@2558c67af7e503879ca96d4454f3a1c277bc3eaa`;
2. the raw-regularity obstruction and exact heat normal form,
   `yspennstate/math-open-problems@39c38206fcf34f616112fe9fa6808161e0472c34`.

## 2. Smooth ruled trace with its Jacobian

Let (R) be an (n	imes3) matrix with orthonormal columns, put (Y=R^TX), and consider the exact rank-three form
[
Q=lambda_1Y_1^2+lambda_2Y_2^2-mu Y_3^2,
qquad lambda_1,lambda_2,muge1.
	ag{2.1}
]
For (s>0), scale to
[
z=(sqrt{lambda_1}y_1,sqrt{lambda_2}y_2,sqrtmu,y_3),
qquad q(z)=z_1^2+z_2^2-z_3^2.
]
The one-sheet level (q=s) has the global ruling
[
Phi_s(	heta,t)
=sqrt{s},e_	heta+t(e_	heta^perp+e_3),
qquad 0le	heta<2pi,quad tinmathbb R.
	ag{2.2}
]
A direct determinant calculation gives the coarea identity
[
delta(q(z)-s),dz=rac12,d	heta,dt.
	ag{2.3}
]
In the original (y)-coordinates the ruling direction is
[
v_	heta=
left(-rac{sin	heta}{sqrt{lambda_1}},
       rac{cos	heta}{sqrt{lambda_2}},
       rac1{sqrtmu}ight).
	ag{2.4}
]
For smooth product inputs, the codimension-two marginal theorem gives the line integral bound (2/|v_	heta|). Its factor (2) cancels the coarea factor (1/2), while the scaling Jacobian is ((lambda_1lambda_2mu)^{-1/2}). Consequently
[
p_Q(s)le C_lambda
:=
(lambda_1lambda_2mu)^{-1/2}
int_0^{2pi}
left(
rac{sin^2	heta}{lambda_1}
+rac{cos^2	heta}{lambda_2}
+rac1mu
ight)^{-1/2}d	heta
lepisqrt2.
	ag{2.5}
]
This derivation is valid for smooth inputs. It is not legitimate to insert an arbitrary version of a rough projected density into the line trace in (2.3).

## 3. Rough-product interval theorem

### Theorem 3.1

For arbitrary independent cap-one input densities and every interval (Jsubset[0,infty)),
[
oxed{Pr{Qin J}le C_lambda |J|lepisqrt2,|J|.}
	ag{3.1}
]

### Proof

The account04/B13 purification theorem states that every cap-one density is an (L^1) limit of finite convex combinations of indicators (1_E), where (E) is a bounded finite union of intervals and (|E|=1). Expanding products shows that it is enough to prove (3.1) for product-indicator inputs.

For such an input, let
[
f_{i,arepsilon}=1_{E_i}*gamma_arepsilon.
]
Each (f_{i,arepsilon}) is a positive analytic-Schwartz probability density, satisfies (|f_{i,arepsilon}|_inftyle1), and converges to (1_{E_i}) in (L^1). Hence
[
left|
igotimes_i f_{i,arepsilon}
-igotimes_i1_{E_i}
ight|_1
lesum_i|f_{i,arepsilon}-1_{E_i}|_1longrightarrow0.
	ag{3.2}
]
Pushforward contracts total variation. Therefore the corresponding laws of (Q) converge in total variation, so the smooth interval estimate passes to every fixed interval without evaluating any rough density on a ruling.

If an endpoint equals zero, first use intervals contained in ((0,infty)) and then let the inner endpoint decrease to zero. There is no atom at zero because the zero set of the nonzero polynomial (2.1) has Lebesgue measure zero and the joint input law is absolutely continuous. This proves (3.1) for product indicators. The finite-mixture approximation then gives it for all cap-one product laws. (square)

Negating (Q) gives the analogous majority-sign one-sheet half-line for signature ((+,-,-)). No statement is made about the opposite, two-sheet half-line.

## 4. Pointwise continuous-representative closure

The preceding theorem is measure domination on a half-line. It does not, by itself, define a pointwise density version. The completed fixed-instance B15 theorem supplies exactly the missing qualitative fact: because (operatorname{rank}A=3), the law of (Q) has a matrix-dependent bounded density
[
p_Qin C_0(mathbb R).
	ag{4.1}
]

### Lemma 4.1

Let (
u=p,dx) with (pin C(mathbb R)). If
[

u(J)le C|J|
	ag{4.2}
]
for every interval (J) contained in an open set (U), then (p(x)le C) for every (xinoverline U).

Indeed, (4.2) gives (ple C) almost everywhere on (U). If (p(x_0)>C) at an interior point, continuity makes the same strict inequality hold on an interval of positive measure, contradicting (4.2). Boundary points follow by continuity from (U).

Applying the lemma with (U=(0,infty)) yields the actual pointwise conclusion
[
oxed{
p_Q(s)le C_lambdalepisqrt2
quad	ext{for every }sge0,
qquad p_Qin C_0(mathbb R).
}
	ag{4.3}
]
Thus the cone vertex is paid without selecting a density value there and without a uniform continuity modulus.

## 5. Application of the latest account01/B15 heat result

Let (mu_+=1_{[0,infty)}mu_Q). From (3.1), (mu_+le C_lambda,dx). Hence at every heat scale
[
oxed{
sup_y(mu_+*gamma_arepsilon)(y)le C_lambdalepisqrt2.
}
	ag{5.1}
]
For the normalized exact rank-three form, the account01/B15 fixed-scale heat identity decomposes as
[
mu_Q*gamma_1
=
mu_+*gamma_1+mu_-*gamma_1,
qquad
mu_-=1_{(-infty,0)}mu_Q.
	ag{5.2}
]
Equation (5.1) completely pays the one-sheet contribution to the positive fixed-scale functional. The unresolved full rank-three heat height is exactly the two-sheet contribution (mu_-*gamma_1), not a regularity or limiting defect.

This application is compatible with account01/B15 r14: that result proves there is no target-uniform (L^1) translation modulus, BV bound, positive Besov bound, or Gaussian desmoothing rate for the raw target densities, even for fixed (A=I_3). None is used here. Only fixed-instance continuity is invoked after interval domination has already been proved.

## 6. Full-target regularity implication

Let (C_*) denote the optimal universal essential density constant over the owner target class. The fixed-instance (C_0) theorem gives a canonical continuous representative for every admissible law. Therefore
[
oxed{
C_*
=
sup_{	ext{target instances}}max_{yinmathbb R}p_Q(y),
qquad p_Qin C_0(mathbb R).
}
	ag{6.1}
]
The equality is exact: an essential bound (p_Qle C) almost everywhere transfers to the continuous representative pointwise by Lemma 4.1 with (U=mathbb R). Conversely, a pointwise bound is an essential bound.

Consequently the separate qualitative continuity problem is closed and costs no extra constant. What remains open is only the universal height. No uniform modulus of continuity, compactness of the raw densities, or uniform desmoothing rate follows or is needed.

## 7. Remaining obstruction and status

For the normalized signature (q=y_1^2+y_2^2-y_3^2), the unresolved side (s=-a^2<0) has coarea formula
[
p_q(-a^2)
=
rac12int_0^inftyint_0^{2pi}
rac{r}{sqrt{r^2+a^2}}
left[
ho(re_	heta,sqrt{r^2+a^2})
+ho(re_	heta,-sqrt{r^2+a^2})
ight]d	heta,dr.
	ag{7.1}
]
This two-sheet hyperboloid has no real rulings. The arbitrary-joint cone-tube correction prevents bounding (7.1) from a projected-density cap alone. Product provenance must control the curved trace jointly.

Thus this run proves:

1. the coarea/Jacobian and marginal-trace calculation for smooth inputs;
2. the rough-product interval transfer without pointwise rough traces;
3. the everywhere pointwise (C_0) one-sheet bound (4.3);
4. the exact one-sheet payment (5.1) inside the account01/B15 heat normal form;
5. the equivalence (6.1), so qualitative continuity adds no further universal cost once height is proved.

The full conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The missing mathematical payment is the convex/two-sheet trace, followed by compilation with arbitrary additional spectral directions.
