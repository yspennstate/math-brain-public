SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T15:05:38Z.
attacking: the target-scale L2-to-Linfinity near-coloop debt by retaining the genuine physical pivot Fourier factor inside the right-plane Fresnel integral, then spending one offending physical row separately when the augmented leverage gate fails.

# fleet03/B03 r36 — genuine-pivot augmented Fresnel and one-anchor near-coloop receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREMS / STRICT AUGMENTED NEAR-COLOOP COLLAR ADVANCED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The owner target remains open. Nothing below assumes Gaussianity, log-concavity, moments, compact or connected support, independence after a spectral rotation, a uniform pointwise quadratic-phase decay, an arbitrary-joint coarea inequality, or a conditional density cap for a duplicated sum/difference coordinate. All Fourier factorisations are performed in ORIGINAL independent coordinates. The independent-copy identity is used only for the whole output variable.

## 1. Fresh source-valid inputs actually used


The mathematical sources actually used below are:

1. **Newest Claude physical Fourier/Brascamp--Lieb package**

   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

   For a cap-one probability density `f` and any coordinatewise unit-modulus twist, its twisted characteristic function `Psi` satisfies

   `int_R |Psi(s)|^p ds <= 4 pi/sqrt(p),  p>=2`.                    (1.1)

   The same source supplies the rigorous damped Fresnel linearisation and the physical rank-one Brascamp--Lieb mechanism. These are integrated estimates; no law-uniform pointwise scalar quadratic-phase decay is used.

2. **Immediate B03 predecessor r35**

   `yspennstate/math-open-problems@47f5fd760f92c306e2105c2de46bf1859d47f56d`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T142318Z-fleet03-B03-QFORM-r35/REPORT.md`.

   It kept the full right-bank dependent pair `(V,H_R)` and reached target-scale finite `L^p` / half-Riesz estimates, but its `|t|^{-1}` endpoint did not prove `L^infinity`.

3. **Target-scale exact-cancellation whole-copy theorem r29**

   `yspennstate/math-open-problems@d68b1a4cf96f02c6afa77ed994fab5feab43f084`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T090012Z-fleet03-B03-QFORM-r29/REPORT.md`.

   At exact angular cancellation it proves a target-scale `L^2_t` characteristic-function integral and a target-scale half-Riesz whole-copy integral. This report does not replace that endpoint; it attacks the strict collar where one can recover an integrable power.

4. **Designated partner fleet04/B03**

   `yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`.

   Its valid elementary lemma is

   `P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`.                           (1.2)

   Its later-refuted weighted-`L^2` compiler is NOT used.

5. **One-anchor determinant mechanism used as an analogue, not as a black box**

   fleet02/B09 r13 proves a one-compulsory-row three-volume hybrid. The new theorem in Section 6 is a two-dimensional Fresnel analogue and is proved from scratch below; it is not an invocation of that theorem.

## 2. Exact physical packet and source spectral identities

The still-relevant exact-rank-three one-sided packet has the original-coordinate representation

`Q = a^(-1) H^2 + 2 sigma U V`,                                    (2.1)

where

`H = a X_i + h_L.X_L + h_R.X_R + h_K.X_K`,
`U = u.X_L`, `V=v.X_R`,                                             (2.2)

and the original banks `{i}`, `L`, `R`, `K` are disjoint. On the right bank

`h_R = beta v + m q`, `v perp q`, `||v||=||q||=1`, `m>0`.          (2.3)

The one-sided state has

`m=rho y`, `rho^2=a^2+||k||^2`, `y^2>1/2`,                          (2.4)

and the exact spectral identities used below are

`gamma |sigma| >= s_3(A)^2`,
`gamma sigma^2 = s_1(A)s_2(A)s_3(A) >= s_3(A)^3`,
`gamma=rho^2/|a|`.                                                   (2.5)

The scalar projection theorem already in the source gives

`L:=||p_U||_infinity <= sqrt(e)`.                                   (2.6)

The r32/r34 reductions show that after the disjoint-volume and near-three-coordinate exits, the difficult angular collar is a near-coloop physical row. This report does not assume the collar itself is the whole theorem; it advances this currently isolated packet.

## 3. New theorem I — augment the Fresnel plane by the genuine physical pivot

The key observation is that the physical pivot `X_i` was previously hidden inside the Fresnel square. Its ordinary characteristic function can instead be left inside the two-dimensional physical Fourier integral, where it contributes a new actual source row.

For `t!=0`, the source damped-Fresnel identity, with the damping removed exactly as in the source proof, gives

`|phi_Q(t)|
 <= sqrt(|a|/(4 pi |t|))
    int_R |chi_i(a s)|
       int_R p_U(u)
          prod_(j in R) |Psi_j(s h_j+2t sigma u v_j)| du ds`.        (3.1)

Here `chi_i` is the ordinary characteristic function of the genuine original coordinate `X_i`. All arbitrary dependence of the remaining left-bank state on `U` is absorbed in a conditional complex amplitude of modulus at most `p_U(u)` before (3.1); no conditional density cap is asserted.

Use the true marginal cap `p_U<=L` and set `eta=2t sigma u`. Then

`|phi_Q(t)|
 <= [L sqrt(|a|)/(4 sqrt(pi)|sigma|)] |t|^(-3/2) I_aug`,            (3.2)

where

`I_aug = int_R2 |chi_i(a s)|
                prod_(j in R)|Psi_j(h_j s+v_j eta)| ds deta`.        (3.3)

Introduce the genuine augmented ORIGINAL-coordinate coefficient rows

`b_0=(a,0)`,
`b_j=(h_j,v_j)=(beta v_j+m q_j,v_j)`, `j in R`.                     (3.4)

Their Gram matrix is

`G_aug=sum b_k b_k^T
      =[[a^2+beta^2+m^2, beta],[beta,1]]`,                           (3.5)

so

`det G_aug=a^2+m^2`.                                                 (3.6)

Put

`theta=m^2/(a^2+m^2)`.                                               (3.7)

A direct inversion of (3.5) gives the normalized row leverages

`ell_0=b_0^T G_aug^(-1)b_0=1-theta`,                                (3.8)

and, for each right physical row,

`boxed: ell_j=v_j^2+theta q_j^2.`                                    (3.9)

### Theorem 3.1 — `QFORM-GENUINE-PIVOT-AUGMENTED-FRESNEL-v1`

Assume

`max{1-theta, max_(j in R)(v_j^2+theta q_j^2)} <= 1/2`.              (3.10)

Then

`I_aug <= (4 pi)^2/sqrt(a^2+m^2)`,                                  (3.11)

and therefore

`boxed:
 |phi_Q(t)| <= min{1,
   K_aug |t|^(-3/2)},
 K_aug=4 pi^(3/2)L sqrt(|a|)/(|sigma|sqrt(a^2+m^2)).
}`                                                                     (3.12)

Consequently `Q` has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3)L^(2/3)
   [sigma^2(a^2+m^2)/|a|]^(-1/3).
}`                                                                     (3.13)

### Proof

Under (3.10), every normalized row has leverage at most one half. Apply geometric rank-one Brascamp--Lieb to the tight frame `G_aug^(-1/2)b_k`. For row `k` with leverage `ell_k`, use exponent `1/ell_k>=2` and (1.1). The rescaling factor `ell_k^(-1/2)` cancels the `sqrt(ell_k)` in the source Hausdorff--Young bound exactly as in the completed physical-plane theorem. Since the leverages sum to two, the product of the row norm bounds is `(4pi)^2`. Restoring the Jacobian `det(G_aug)^(-1/2)` proves (3.11). Substituting into (3.2) proves (3.12).

For `K>0`,

`int_R min(1,K|t|^(-3/2))dt=6K^(2/3)`.                              (3.14)

Fourier inversion gives

`||p||_inf <=(2pi)^(-1)6K_aug^(2/3)`,                               (3.15)

which simplifies to (3.13). The envelope is in `L^1`, so the density is continuous and vanishes at infinity. QED.

### Target-normalized consequence

By `a^2+m^2>=m^2=rho^2 y^2` and (2.5),

`sigma^2(a^2+m^2)/|a|
 >= gamma sigma^2 y^2
 >=s_3(A)^3 y^2
 >s_3(A)^3/2`.                                                       (3.16)

Using `L<=sqrt(e)`,

`boxed:
 ||p_Q||_infinity
 <3*2^(5/3)e^(1/3) s_3(A)^(-1)
 =13.2923797904... s_3(A)^(-1).
}`                                                                     (3.17)

This is a full linear interval estimate on this branch:

`P(Q in I)<13.293 s_3(A)^(-1)|I|`.                                  (3.18)

## 4. Assigned whole-copy integrated estimate and partner application

The pointwise theorem immediately gives a quantitative whole-copy estimate, and this is where the assignment's independent-copy identity is used. Let `Q'` be an independent copy of the ENTIRE output. Then

`|phi_Q(t)|^2=E exp(i t(Q-Q'))`.                                     (4.1)

No duplicated coordinate is rewritten as an independent sum and difference.

For the envelope (3.12), with threshold `T=K_aug^(2/3)`, direct integration gives

`boxed:
 int_R |phi_Q(t)|^2 dt <=3 K_aug^(2/3),
}`                                                                     (4.2)

and

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=(24/5) K_aug^(1/3).
}`                                                                     (4.3)

By Plancherel,

`||p_Q||_2^2 <= [3/(2pi)]K_aug^(2/3).`                              (4.4)

Now apply the completed designated fleet04/B03 collision lemma (1.2):

`boxed:
 P(|Q-Q'|<=eps)
 <=(3/pi)K_aug^(2/3) eps.
}`                                                                     (4.5)

The coefficient in (4.5) equals the right side of the density estimate (3.13), so under the target normalization it is `<13.293/s_3(A)`. This is an equation-level use of the designated partner. The partner's invalid weighted-`L^2` compiler is not used.

## 5. New theorem II — if the pivot row itself is too heavy, pay it in real space

The augmented BL gate (3.10) first requires `theta>=1/2`. The complementary case has a simple target-scale payment that does not require any Fourier pointwise decay.

### Lemma 5.1 — scalar half-Riesz from a density cap

If `Y` has density at most `M`, then

`boxed: sup_s E|Y-s|^(-1/2) <=2 sqrt(2M).`                          (5.1)

Indeed, with the layer-cake identity

`E|Y-s|^(-1/2)=int_0^infinity P(|Y-s|<lambda^(-2)) d lambda`,        (5.2)

use `P<=min(1,2M lambda^(-2))` and integrate at the crossover `sqrt(2M)`.

If independent `U,V` have density caps `M_U,M_V`, conditioning on `U` and applying (5.1) to the scaled variable `cUV` gives

`sup_s E|s-cUV|^(-1/2)
 <=2sqrt(2M_V/|c|) E|U|^(-1/2)
 <=8 sqrt(M_U M_V/|c|).`                                            (5.3)

### Theorem 5.2 — `QFORM-PIVOT-HEAVY-HYPERBOLIC-HALFRIESZ-v1`

In the packet (2.1), if

`theta=m^2/(a^2+m^2)<1/2`,                                         (5.4)

then

`boxed:
 ||p_Q||_infinity
 <=4sqrt(2) sqrt(M_U M_V) |a sigma|^(-1/2).
}`                                                                     (5.5)

For the current cap-one product projections, `M_U,M_V<=sqrt(e)`, and the source spectral relations imply

`boxed:
 ||p_Q||_infinity <8 sqrt(e) s_3(A)^(-1)
 =13.1897701656... s_3(A)^(-1).
}`                                                                     (5.6)

This branch proves essential boundedness. Continuity is not claimed by this proof.

### Proof

Condition on every original coordinate except the genuine pivot `X_i`. Then

`Q=a(X_i+H_0/a)^2+2sigma UV`,                                       (5.7)

where the shift is fixed under that conditioning. The conditional density of the square term obeys

`p_{a(X_i+c)^2}(w)<=|a|^(-1/2)|w|^(-1/2)`                           (5.8)

on its support. Averaging and applying (5.3) with `c=2sigma` gives (5.5).

If (5.4), then `m^2<a^2`. Since `m=rho y` and `y^2>1/2`,

`a^2/rho^2>y^2>1/2`.                                                (5.9)

Hence, from `gamma|sigma|>=s_3(A)^2`,

`|a sigma|
 =(a^2/rho^2)(gamma|sigma|)
 >s_3(A)^2/2`.                                                       (5.10)

Together with `M_U,M_V<=sqrt(e)`, this gives (5.6). QED.

Thus the augmented near-coloop problem may henceforth assume `theta>=1/2`.

## 6. New theorem III — spend one offending physical row separately

When `theta>=1/2`, Theorem 3.1 can still fail because one physical right row has augmented leverage above one half. Rather than throw away that row or invert a small individual minor, spend it in Plancherel and pay the remainder by two determinant measures.

### Abstract two-dimensional statement

Let `Y_k` be independent cap-one variables with (possibly twisted) characteristic functions `Psi_k`, and let `b_k in R^2` be coefficient rows spanning `R^2`. Fix a distinguished anchor row `h`. Put

`Z_1=sum_(j!=h) det(b_h,b_j)^2`.                                    (6.1)

Assume `Z_1>0`, and define anchor-partner probabilities

`alpha_j=det(b_h,b_j)^2/Z_1`, `j!=h`.                               (6.2)

Also define the low-row second volume

`Z_0=sum_(j<k, j,k!=h) det(b_j,b_k)^2`.                              (6.3)

Assume `Z_0>0`, and let `lambda_j` be the row marginals of the squared-determinant probability distribution on low-row pairs:

`lambda_j= [sum_(k!=h,j) det(b_j,b_k)^2]/Z_0`.                      (6.4)

### Theorem 6.1 — `QFORM-FRESNEL-ONE-ANCHOR-2VOLUME-v1`

If

`max_(j!=h) alpha_j<=1/2`,
`max_(j!=h) lambda_j<=1/2`,                                         (6.5)

then

`boxed:
 int_R2 |Psi_h(b_h.z)| prod_(j!=h)|Psi_j(b_j.z)| dz
 <=8 sqrt(2) pi^2 (Z_1 Z_0)^(-1/4).
}`                                                                     (6.6)

### Proof

Write

`R(z)=prod_(j!=h)|Psi_j(b_j.z)|`.

Cauchy--Schwarz with respect to the positive measure `R(z)dz` gives

`I^2 <= I_2 I_0`,                                                    (6.7)

where

`I_2=int |Psi_h(b_h.z)|^2 R(z)dz`,
`I_0=int R(z)dz`.                                                    (6.8)

For `I_2`, use the determinant-weight Brascamp--Lieb expansion supported only on the physical bases `{h,j}` with probabilities `alpha_j`. The anchor exponent is exactly one; every low-row exponent is `alpha_j<=1/2`. Plancherel gives

`int |Psi_h(s)|^2 ds <=2pi`,                                        (6.9)

while (1.1) with `p=1/alpha_j` gives the low-row norm. The usual Gaussian determinant/entropy cancellation gives

`I_2 <=8 pi^2 Z_1^(-1/2)`.                                         (6.10)

For `I_0`, use squared-determinant volume sampling on the low-row physical pairs. The leverage assumption `lambda_j<=1/2` and (1.1) give

`I_0 <=16 pi^2 Z_0^(-1/2)`.                                        (6.11)

Taking the square root of (6.10)(6.11) proves (6.6). QED.

### Apply Theorem 6.1 to the actual augmented Fresnel rows

Return to (3.4) and choose an offending right physical row `r` as the anchor; the low set contains the genuine pivot row `b_0=(a,0)` and all other right rows.

The total two-volume of the augmented frame is

`E_2=sum_(j<k)det(b_j,b_k)^2=det G_aug=a^2+m^2`.                    (6.12)

For the anchor `r`, the anchor volume is

`boxed:
 Z_1=a^2 v_r^2+m^2 eta_r,
 eta_r=v_r^2+q_r^2.
}`                                                                     (6.13)

Indeed `det(b_0,b_r)^2=a^2v_r^2` and orthonormality of `(v,q)` gives

`sum_(j!=r)det((h_r,v_r),(h_j,v_j))^2=m^2 eta_r`.                   (6.14)

The complementary low-row two-volume is therefore

`boxed:
 Z_0=a^2(1-v_r^2)+m^2(1-eta_r).
}`                                                                     (6.15)

Define

`delta=Z_0/(a^2+m^2)`.                                               (6.16)

Then the anchor leverage in the augmented frame is `1-delta`, and

`sqrt(Z_1Z_0)=(a^2+m^2)sqrt(delta(1-delta)).`                        (6.17)

Under the two diffusion gates (6.5), Theorem 6.1 inserted into (3.2) yields

`boxed:
 |phi_Q(t)|<=min{1,K_r |t|^(-3/2)},
 K_r=2sqrt(2) pi^(3/2)L sqrt(|a|)
     [|sigma|(Z_1Z_0)^(1/4)]^(-1).
}`                                                                     (6.18)

Hence `Q` has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <=6 L^(2/3)
    [ |a|/(sigma^2 sqrt(Z_1Z_0)) ]^(1/3).
}`                                                                     (6.19)

Using (6.17), (2.5), `a^2+m^2>=rho^2 y^2`, and `L<=sqrt(e)`,

`boxed:
 ||p_Q||_infinity
 <6(2e)^(1/3)
 [delta(1-delta)]^(-1/6)s_3(A)^(-1).
}`                                                                     (6.20)

For example, throughout

`1/16 <=delta<1/2`,                                                   (6.21)

we obtain the explicit target-scale bound

`||p_Q||_infinity <16.929 s_3(A)^(-1)`.                             (6.22)

The same envelope gives

`int |phi_Q|^2 <=3K_r^(2/3)`,
`int |t|^(-1/2)|phi_Q|^2 <=(24/5)K_r^(1/3)`,                         (6.23)

and the designated partner collision lemma gives

`P(|Q-Q'|<=eps)< ||p_Q||_infinity eps`                               (6.24)

with the right side of (6.19) as coefficient.

## 7. What has actually been narrowed

The strict near-coloop collar is now split without any illegal rotation or conditional density transfer:

1. **Pivot-heavy side** `theta<1/2`: paid by Theorem 5.2 with `<13.190/s_3(A)`; essential boundedness.

2. **Augmented diffuse side** `theta>=1/2` and every augmented physical leverage at most `1/2`: paid by Theorem 3.1 with `<13.293/s_3(A)` and a continuous density.

3. **One augmented-heavy row, but neither its partner determinant law nor the complementary low-frame determinant law is concentrated:** paid by Theorem 6.1. If the residual augmented area fraction `delta` is bounded below, this is uniformly target-scale and continuous.

The remaining B03 debt is therefore no longer the undifferentiated statement “convert endpoint L2 to L∞”. It is the genuinely sharper structural/analytic endpoint:

`QFORM-AUGMENTED-COLOOP-OR-DETERMINANT-CONCENTRATION-ENDPOINT-v1`:

> in the exact one-sided packet, after the already-paid branches above, either `delta ->0` for an actual augmented physical anchor (a true near-coloop of the pivot/right frequency frame), or one of the two physical determinant sampling laws in Theorem 6.1 has a row marginal above one half. Pay those concentrated states with a constant stable at the exact coloop, without deleting the small transverse term.

At `delta=0` an exact-coloop result already exists elsewhere in the fleet, but the present `delta^{-1/6}` collar estimate is not by itself uniform as `delta downarrow0`; no continuity-of-proof shortcut is claimed. The exact-cancellation r29 target-scale `L^2` theorem remains available at that endpoint.

## 8. Relation to earlier B03/fleet02 results and non-duplication

Theorem 3.1 is distinct from the earlier fleet02/B03 `QFORM-HUB-DENSITY-AUGMENTED-BL-v1`. That theorem inserts the grouped-hub density as an auxiliary row `(0,tau)` and loses integrability at its critical auxiliary leverage. Here the auxiliary row is the **genuine physical pivot transform** `chi_i(a s)`, namely row `(a,0)`, and its `L^p` credit comes from the original scalar law itself.

Theorem 6.1 is also distinct from fleet02/B09's one-anchor three-volume cross-block theorem. Section 6 proves a two-dimensional Fresnel version tailored to the physical square/hyperbolic packet; its two currencies are the anchor pair-volume `Z_1` and complementary low-plane volume `Z_0`.

The r29 exact-cancellation theorem remains stronger exactly at the collision/half-Riesz endpoint because it is uniform where the present strict-collar `L^1_t` estimate can blow up. The results are complementary rather than replacements.

## 9. Status against the owner target

The unrestricted arbitrary-dimensional theorem is still **OPEN**. No valid target counterexample is produced. Full-target continuity is still **OPEN**; continuity is proved on the `L^1_t` branches of Theorems 3.1 and 6.1, while Theorem 5.2 gives only an essentially bounded density.

The core progress of this run is that the near-coloop B03 obstruction has acquired a new genuine source coordinate in the time integral and a one-anchor escape mechanism. The only residual states are now explicit augmented-coloop/determinant-concentration states, rather than a generic failure of the decoupled time integral.
