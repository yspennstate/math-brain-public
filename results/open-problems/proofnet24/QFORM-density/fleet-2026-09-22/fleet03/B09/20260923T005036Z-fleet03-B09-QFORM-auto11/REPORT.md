SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T00:50:36Z.
attacking: the double-null two-sided shear chamber: recover the missing linear null-pivot smoothing after a product-destroying shear by a mass-sensitive slice Hausdorff-Young estimate.

# fleet03/B09 auto11 — the exact double-null two-sided shear obstruction is paid by linear slice smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Assignment: Bilinear block mechanism.  
Outcome: `NEW_SUPPORTING_THEOREM / PREVIOUS EXACT DOUBLE-NULL OBSTRUCTION CLOSED / FULL_QFORM_OPEN`.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and fresh route choice

The unrestricted target remains open: for every dimension, every independent real input vector with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal bound for the density of `X^T A X`, or give a target-valid counterexample. Continuity is a separate desired conclusion.

The previous B09 run paid a **one-sided null linear pivot plus rank-two cross block** by adding a missing Fourier half-power. Before duplicating the two-sided extension, I searched the current QFORM corpus and found that fleet01/B11 had already proved `QFORM-TWOSIDED-SHEAR-MIXED-v1`: after a product-aware shear, any nonzero residual scalar square curvature `a_L` or `a_R` yields a continuous density bound

`||p_Q||_infinity <= C_* |a_L|^(-1/5)|det B|^(-2/5)`,

with `C_*<7.326`, and symmetrically on the right. Its source is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/QFORM-B11-20260922T144348Z-r11/REPORT.md`.

That report also exhibited a literal target-class **double-null** matrix where both shear curvatures vanish. It left endpoint boundedness in that chamber unpaid. This run attacks exactly that first missing implication rather than re-proving the generic two-sided theorem.

No post-rotation independence, law-uniform pointwise Fresnel decay, arbitrary-joint coarea, conditional spectral-density moment, fiber supremum, compact-support assumption, or square-root small-ball decoupling is used.

A completed peer theorem is applied below at an actual inequality: fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, source

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For a one-dimensional normalized linear projection of an original cap-one product source it gives density cap at most `sqrt(e)`. The designated fleet04/B09 current-QFORM artifact was still absent at the initial fresh check, so no designated-partner theorem is fabricated or awaited.

## 2. The physical five-coordinate chart

Let `x,u_1,u_2,v_1,v_2` be five distinct original coordinates. They are independent and each has a probability density at most one. Write `u=(u_1,u_2)` and `v=(v_1,v_2)`. After conditioning every other original coordinate, the most general active quadratic-plus-linear expression is

`q(x,u,v)
 = a x^2 + 2x(beta+r^T u+s^T v)
   +u^T C u+2 gamma^T u+2u^T Bv
   +v^T Dv+2 delta^T v+c_0`,                                      (2.1)

where `C,D` are symmetric `2x2` matrices and `B` is an invertible `2x2` physical cross block.

Set

`kappa=B^(-T)s`,
`a_L=a-2r^T kappa+kappa^T C kappa`,
`r_L=r-C kappa`,
`beta_L=beta-gamma^T kappa`.                                      (2.2)

Make the volume-preserving integration-variable change

`u'=u+kappa x`, so `u=u'-kappa x`.                                (2.3)

Because `B^T kappa=s`, the `x-v` term cancels exactly. Direct expansion gives

`q=a_L x^2+2x(beta_L+r_L^T u')+F(u')+2u'^T Bv+G(v)+c_0`,           (2.4)

for explicit quadratic-plus-linear `F,G` independent of `x`.

The shear does **not** preserve independence. Instead, the transformed left density is exactly

`h(x,u')=f_x(x)f_{u_1}(u'_1-kappa_1x)f_{u_2}(u'_2-kappa_2x)`.      (2.5)

This provenance is the resource used below.

## 3. A mass-sensitive linear slice lemma

Assume now the exact double-null scalar-curvature condition

`a_L=0`,                                                             (3.1)

but retain

`r_L !=0`.                                                           (3.2)

Put

`c(u')=beta_L+r_L^T u'`.                                             (3.3)

Let

`m(u')=integral_R h(x,u') dx`.                                       (3.4)

Since each original density is at most one and `f_x` has mass one,

`0<=h<=1`, `0<=m<=1`, and `integral_R2 m(u')du'=1`.                  (3.5)

For fixed `u'`, define

`K_{u'}(t)=integral_R h(x,u') exp(2it c(u')x) dx`.                    (3.6)

### Lemma 3.1 — linear slice `L^4` bound

For `c(u')!=0`,

`||K_{u'}||_(L^4(dt))
 <= pi^(1/4)|c(u')|^(-1/4)m(u')^(3/4)`.                              (3.7)

### Proof

With Fourier convention `hat g(xi)=integral g(x)e^(ixi x)dx`, interpolation between `L^1->L^infinity` and Plancherel gives

`||hat g||_4 <=(2pi)^(1/4)||g||_(4/3)`.                              (3.8)

The change `xi=2c(u')t` contributes `(2|c(u')|)^(-1/4)`. Because `0<=h<=1`,

`||h(.,u')||_(4/3)
 <=( integral h(x,u')dx )^(3/4)=m(u')^(3/4)`.                        (3.9)

Combining (3.8)-(3.9) gives (3.7). `QED`

Define

`H(t)^2=integral_R2 |K_{u'}(t)|^2 du'`.                              (3.10)

Minkowski and (3.7), using `m^(3/2)<=m`, give

`||H||_4^2
 =||integral |K_{u'}|^2du'||_2
 <=integral ||K_{u'}||_4^2du'
 <=pi^(1/2) integral |c(u')|^(-1/2)m(u')du'.                         (3.11)

Thus the entire issue is a **negative half moment of one genuine original-coordinate linear projection**, not a conditional spectral density.

## 4. Paying the moving linear zero from the original product source

Under the probability density `m`, the random vector `U'` has exactly the law

`U'=U+kappa X`,                                                      (4.1)

where `X,U_1,U_2` are the original independent coordinates. Hence

`r_L^T U'
 =r_L^T U+(r_L^T kappa)X`.                                          (4.2)

Set

`w=[ ||r_L||_2^2+(r_L^T kappa)^2 ]^(1/2)>0`.                         (4.3)

The coefficient vector in (4.2), normalized by `w`, is a one-dimensional orthogonal projection of the three-coordinate original product source. Applying the completed fleet02/B06 affine-fiber Brascamp--Lieb theorem at this exact inequality yields the density cap

`||p_{c(U')}||_infinity <= L:=sqrt(e)/w`.                            (4.4)

Translation by `beta_L` does not change the cap.

For any probability density `g<=L`, the symmetric decreasing rearrangement (equivalently the one-dimensional bathtub principle) gives

`integral |z|^(-1/2)g(z)dz
 <=L integral_{-1/(2L)}^{1/(2L)} |z|^(-1/2)dz
 =2sqrt(2L)`.                                                        (4.5)

Using (4.5) in (3.11),

`||H||_4
 <=2^(3/4)pi^(1/4)L^(1/4)`.                                      (4.6)

This is the missing product-provenance payment. The shear created dependence between `x` and `u'`, but its exact slice masses restore an integrable time resource without pretending that the sheared coordinates are independent.

## 5. Rank-two bilinear Plancherel and the `O(|I|)` endpoint

The right density is `f_{v_1}(v_1)f_{v_2}(v_2)<=1`; multiplying it by the unit-modulus phase `exp(itG(v))` gives an `L^2` amplitude of norm at most one. Applying the exact rank-two bilinear Plancherel inequality to the `u'` and `v` variables gives, for `t!=0`,

`|phi_q(t)|
 <=pi |t|^(-1)|det B|^(-1/2) H(t)`.                                 (5.1)

For any `T>0`, Holder with exponents `4/3` and `4`, together with

`integral_{|t|>T}|t|^(-4/3)dt=6T^(-1/3)`,                            (5.2)

gives

`integral_{|t|>T}|phi_q(t)|dt
 <=D T^(-1/4)`,                                                      (5.3)

where

`D=pi^(5/4) 2^(3/4)6^(3/4)|det B|^(-1/2)L^(1/4)`.                   (5.4)

On `|t|<=T`, use only `|phi_q(t)|<=1`. Therefore

`integral_R |phi_q(t)|dt <=2T+D T^(-1/4)`.                           (5.5)

The exact optimizer is

`T=(D/8)^(4/5)`,                                                     (5.6)

and (5.5) becomes `10(D/8)^(4/5)`. Fourier inversion now proves a bounded continuous density (indeed one vanishing at infinity) with

`||p_q||_infinity
 <= C_lin L^(1/5)|det B|^(-2/5)`,                                   (5.7)

where

`C_lin=5*3^(3/5)/2^(6/5)=4.2073317954...`.                           (5.8)

Substituting the peer cap (4.4) yields the physical target-scope theorem.

### Theorem 5.1 — `QFORM-DOUBLE-NULL-LINEAR-SHEAR-v1`

In the five-original-coordinate chart (2.1), assume `B` is invertible, `a_L=0`, and `r_L!=0`. Define `w` by (4.3). Then after arbitrary conditioning on every outside original coordinate, the conditional law has a continuous density bounded uniformly by

`boxed:
 ||p_Q||_infinity
 <= C_phys [ w |det B|^2 ]^(-1/5),
 C_phys=C_lin e^(1/10)=4.6498207430... .
`                                                                        (5.9)

Consequently the unconditional law also has a continuous density and for every interval `I`,

`boxed:
 P(Q in I) <=4.650 [w |det B|^2]^(-1/5)|I|.
`                                                                        (5.10)

No probability squaring or square-root loss in `|I|` occurs.

The right-handed analogue follows by interchanging `u` and `v`.

## 6. The fleet01/B11 exact double-null obstruction is now paid

Fleet01/B11 used

`C=D=0`, `B=I_2`, `r=s=e_1`, `a=2`,                                (6.1)

with zero affine terms. Then

`kappa=e_1`, `a_L=0`, `r_L=e_1`, `w=sqrt(2)`, `|det B|=1`.             (6.2)

The exact transformed form is

`q=2x u'_1+2u'_1v_1+2u'_2v_2`,                                      (6.3)

where `u'=u+e_1x`. In this special case one can improve (4.4): `u'_1=u_1+x` has density at most one by Young's inequality, hence `L<=1`. Thus (5.7) gives the sharper explicit bound

`boxed: ||p_q||_infinity <= C_lin <4.208.`                            (6.4)

The coefficient matrix is

`M=[[2,1,0,1,0],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [1,1,0,0,0],
    [0,0,1,0,0]]`,                                                   (6.5)

with characteristic polynomial

`lambda(lambda-3)(lambda-1)(lambda+1)^2`;                            (6.6)

its spectrum is `{3,1,-1,-1,0}`. Therefore this is a literal target-class matrix, not merely a toy below the spectral threshold. The previous report used it to prove that `a_L` or `a_R` need not be nonzero. The new theorem shows that the same exact obstruction nevertheless has a universally bounded **continuous** output density for every admissible independent cap-one input law.

This is a substantive endpoint upgrade: the former report had only finite-`p` control in its canonical null chart, while (6.4) is `L^infinity` and directly linear in interval length.

## 7. Exact structural narrowing of the only survivor

The same left shear yields an elementary algebraic fact. Suppose instead

`a_L=0` and `r_L=0`.                                                  (7.1)

Then `r=C kappa`; and `a_L=0` implies

`a=kappa^T C kappa`.                                                  (7.2)

Let the five-variable quadratic coefficient matrix in the order `(x,u,v)` be

`M_5=[[a,r^T,s^T],[r,C,B],[s,B^T,D]]`.                               (7.3)

Because `B^T kappa=s`, (7.1)-(7.2) give the exact kernel identity

`boxed: M_5 (1,-kappa,0)^T=0.`                                       (7.4)

Therefore an invertible rank-two physical cross packet plus a scalar pivot has the following complete **left-shear local routing**:

* if `a_L!=0`, the completed fleet01/B11 theorem pays it;
* if `a_L=0` but `r_L!=0`, Theorem 5.1 pays it;
* if `a_L=r_L=0`, the scalar direction is an exact quadratic kernel direction of this five-coordinate packet and contributes no new quadratic rank.

The last alternative is not yet a full-QFORM solution: the remaining four-coordinate block and all outside coordinates can still carry the three large spectral directions, and a dimension-free global extraction/aggregation argument is still required. But the **analytic two-sided double-null endpoint itself is no longer unpaid** for a genuine invertible physical `2x2` cross packet.

## 8. What this does and does not prove

This theorem is local in five original coordinates but stable under arbitrary outside conditioning, so all outside quadratic coefficients and couplings are allowed. It proves a continuous density and a true `O(|I|)` interval bound whenever its quantitative packet is present. It does not assert that the bare three-large-eigenvalue hypothesis forces a uniformly conditioned five-coordinate packet; known diffuse examples forbid such a naive single-minor extraction.

The new first B09 structural debt is therefore

`QFORM-DOUBLE-NULL-TRANSVERSE-OR-KERNEL-AGGREGATION-v1`:

from the global three-large-eigenvalue hypothesis, aggregate disjoint original-coordinate banks so that either (i) a paid rank-two packet has nonzero square shear curvature, (ii) the exact-zero curvature leaves a nonzero linear slice coefficient and Theorem 5.1 pays it, (iii) a transverse/mixed-hub or higher-rank packet is paid by existing bank theorems, or (iv) the resulting exact kernel directions can be eliminated without losing the three-large-eigenvalue hypothesis at a universal quantitative scale.

The unrestricted QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. Continuity **is proved** in Theorem 5.1's exact scope.

## 9. Finite checks

The constants are

`C_lin=5*3^(3/5)/2^(6/5)=4.207331795423248...`,

`C_phys=C_lin*e^(1/10)=4.649820742996774...`.

For (6.5), symbolic factorization gives

`det(lambda I-M)=lambda(lambda-3)(lambda-1)(lambda+1)^2`.

A small exact checker is stored beside this report.

## 10. Corrections and status

Corrections explicitly preserved include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`, `QFORM-CROSSMINOR-ALONE-FALSE`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`. No refuted interface is used.

Repository transport and theorem consumption occurred; no authenticated native brain receiver retrieval/ingestion was observed. Status therefore remains `WITHOUT_VERIFIED_BRAIN`.
