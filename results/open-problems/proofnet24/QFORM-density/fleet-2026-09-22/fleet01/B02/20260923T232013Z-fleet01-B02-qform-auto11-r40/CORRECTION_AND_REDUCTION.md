# fleet01/B02 r40 correction and replacement reduction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T232013Z-fleet01-B02-qform-auto11-r40`  
Status: **CORRECTION / ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN-NOT-REFUTED**

This file is authoritative over the earlier `REPORT.md` in this same immutable run directory wherever the two conflict.

## 1. Correction to the earlier mixed-norm tensorization

The earlier `REPORT.md`, Lemma 3.1, asserted that for a two-dimensional probability density `rho(x,u)` with `rho<=M` and `u`-marginal at most `m_*`,

`||rho||_{L_x^(4/3)(L_u^2)} <= ||rho||_{L_u^2(L_x^(4/3))} <= (M m_*)^(1/4)`.

The first inequality has the Minkowski direction reversed. For `4/3<2`, the valid general inequality is

`||rho||_{L_u^2(L_x^(4/3))} <= ||rho||_{L_x^(4/3)(L_u^2)}`.

Therefore the hard norm needed to pair the `L^(4/3)->L^4` chirp estimate is not controlled by the displayed easy norm. The downstream claims `QFORM-ZEROPIVOT-CHIRP-CRITICAL-MIXEDNORM-v1`, `QFORM-ZEROPIVOT-CHIRP-LOGGLUE-v1`, and the live inequality derived from them are **not established** by the earlier report.

The scalar operator statement from its Lemma 2.1 survives unchanged: for

`(T_delta f)(y)=int k_t(alpha y+beta z) exp(i2t delta yz) f(z) dz`,

with `k_t(s)=hat g_t(2ts)` and `||g_t||_2<=1`, the exact chirp-convolution identity plus Young gives, for every real `delta`,

`||T_delta||_{L^(4/3)->L^4}
 <= sqrt(pi)|alpha beta|^(-1/4)|t|^(-1/2).`                       (1.1)

What fails is the attempted uniform passage from (1.1) to the two-dimensional projected-bank tensor norm.

## 2. Source-valid counterexample to the hard mixed-norm gate

The failure is not merely an artefact of allowing an arbitrary joint density. It already occurs for an exact orthogonal image of **two independent cap-one original coordinates**.

Fix an integer `k>=2`, put `eps=1/k`, and take `R=4`. Let `X,Y` be independent with densities

`f_X(x)=sum_{j=0}^{k-1} 1_[Rj,Rj+eps](x)`,

`f_Y(y)=sum_{l=0}^{k-1} 1_[Rkl,Rkl+eps](y)`.

Each density is between zero and one and has total mass `k eps=1`. Define the orthogonal coordinates

`U=(X+Y)/sqrt(2)`, `V=(X-Y)/sqrt(2)`.

The transformation has absolute Jacobian one, so the joint density `rho_k(u,v)` is exactly the indicator of the union of the `k^2` diamonds obtained by rotating the `k^2` original `eps x eps` rectangles. In particular

`0<=rho_k<=1`, `int rho_k=1`.                                      (2.1)

The `U`-projection centers are proportional to the integers `j+kl`, which are all distinct for `0<=j,l<k`; the `V`-projection centers are proportional to `j-kl`, which are also all distinct. Since `R=4>2eps`, the `U`-projections of the diamonds are pairwise disjoint, and the same is true of their `V`-projections.

For one rotated `eps x eps` square, after translating its `U` coordinate to start at zero, the vertical slice length is

`L_eps(u)=2u`,                         `0<=u<=eps/sqrt(2)`,

`L_eps(u)=2(sqrt(2)eps-u)`,           `eps/sqrt(2)<=u<=sqrt(2)eps`.

Hence every one-dimensional marginal is bounded by

`max L_eps=sqrt(2)eps=sqrt(2)/k<=1`.                                (2.2)

Nevertheless the hard mixed norm diverges. Since the `U`-projections are disjoint,

`||rho_k||_{L_U^(4/3)(L_V^2)}^(4/3)
 = k^2 int_0^(sqrt(2)eps) L_eps(u)^(2/3) du`

`= k^2 * 2 int_0^(eps/sqrt(2)) (2u)^(2/3) du`

`= (6/5) 2^(-1/6) k^2 eps^(5/3)`

`= (6/5) 2^(-1/6) k^(1/3).`                                         (2.3)

Therefore

`boxed:
 ||rho_k||_{L_U^(4/3)(L_V^2)}
 = [(6/5)2^(-1/6)]^(3/4) k^(1/4) -> infinity.`                       (2.4)

By the disjointness of the `V` projections, the same divergence holds after interchanging `U` and `V`.

Thus even the following combined information is insufficient to bound the hard mixed norm uniformly:

- exact provenance as an orthogonal image of two independent original cap-one variables;
- joint density cap one;
- both one-dimensional marginal caps at most one.

This is a source-valid product-law counterexample to the **mixed-norm intermediate gate**, not to QFORM and not to the target-wide integrated-Fourier criterion.

## 3. Why the counterexample hits exactly the attempted tensor step

The scalar estimate (1.1) naturally maps the hub/star coordinate as

`L^(4/3) -> L^4`.

The transverse bilinear Fourier operator

`(S_sigma f)(y2)=int exp(i2t sigma y2 z2)f(z2)dz2`

has the exact Plancherel norm

`||S_sigma||_{2->2}=sqrt(pi/(|t sigma|)).`                             (3.1)

The tensor pairing therefore asks one bank for an outer `L^(4/3)` norm in the star coordinate with an inner `L^2` norm in the transverse coordinate. Formula (2.4) proves that this norm can grow without bound even for the exact product-projection provenance available in the QFORM reduction. Reversing the integration order gives the easier norm, but Minkowski moves in the wrong direction to recover the required one.

Consequently no correction that uses only the projected two-dimensional density cap and its coordinate marginal caps can repair the earlier argument. One needs a genuinely time-integrated estimate or an additional physical-volume resource.

## 4. A clean replacement target: weak-L2 chirp maximal control

The designated fleet02/B02 source

`yspennstate/math-open-problems@612be1591c1aa5edaeb29bb6eceec7963ddbef55`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T212459Z-fleet02-B02-qform-auto11/EARLY.md`

shows that the nonzero-tail star operator is governed by the quadratic maximal transform

`U_g(s)=sup_eta |int g(h) exp(-i(s h^2+eta h)) dh|`,                  (4.1)

and that taking the worst law pointwise gives only the critical `|t|^-1` tensor decay. The preceding B02 r39 route uses the one-dimensional Strichartz `L^4` control of this maximal transform, which gives an integrated estimate but loses a negative power of the nonzero tail.

There is a sharper scale-correct target which, if proved, removes that endpoint loss:

`QFORM-CHIRP-MAXIMAL-WEAKL2-v1:`

`boxed:
 sup_{lambda>0} lambda^2
 |{s in R: U_g(s)>lambda}| <= C_w^2}`                                (4.2)

for every probability density `0<=g<=1` (and the affine-modulated equivalent form).

This is recorded here as an **OPEN supporting lemma**, not as a theorem. Its relevance is exact and elementary:

Suppose the partner reduction gives, for `delta!=0`,

`|phi_Q(t)|
 <= A |t|^(-1) U_g(c t)`,                                            (4.3)

where

`A=pi sqrt(M_Y M_Z)|delta sigma|^(-1/2)`,
`c=|alpha beta/delta|`.                                               (4.4)

If (4.2) holds, weak-`L^2` scaling gives

`|| A U_g(c .) ||_{L^(2,infinity)}
 <= K := pi C_w sqrt(M_Y M_Z)|alpha beta sigma|^(-1/2),`              (4.5)

and **the factor `delta` cancels exactly**.

For completeness, a dyadic Lorentz estimate proves the resulting Fourier `L1` bound. If `V>=0` and `||V||_(2,infinity)<=K`, then on every finite-measure set `I`,

`int_I V <= 2K |I|^(1/2)`.                                            (4.6)

Therefore, for `T>0`, dyadically decomposing `[T,infinity)` gives

`int_T^infinity V(t)/t dt
 <= C_d K T^(-1/2)`,

with

`C_d=2/(1-2^(-1/2)).`                                                 (4.7)

Using `|phi_Q|<=1` on `(0,T)` and symmetry in `t`,

`int_R |phi_Q(t)|dt
 <= 2T+2 C_d K T^(-1/2).`                                             (4.8)

Optimizing at `T=(C_d K/2)^(2/3)` gives

`boxed:
 int_R |phi_Q(t)|dt
 <= 6*2^(-2/3) (C_d K)^(2/3).}`                                      (4.9)

Thus (4.2) would yield

`int_R |phi_Q(t)|dt
 <= C (M_YM_Z)^(1/3)|alpha beta sigma|^(-1/3),`                       (4.10)

uniformly in `delta`, exactly matching the homogeneous scale of the `delta=0` rank-one tensor theorem.

No claim is made here that (4.2) is true. The standard `L_t^4 L_x^infinity` Strichartz estimate gives only a `lambda^-4` superlevel bound, so (4.2) is genuinely stronger and must be proved from the cap-one/probability structure or refuted by one fixed fragmented density.

## 5. Completed partner theorem applied to an actual live inequality

A valid partner result remains available at the exact algebraic endpoint. The completed fleet02/B02 theorem

`QFORM-ZEROPIVOT-RANKONE-CROSS-TENSOR-L1-v1`

is at full commit

`aeaba9e3351623ead11450857c2d014b43664aef`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T200844Z-fleet02-B02-qform-auto11/REPORT.md`.

It proves, when the physical shared hub has zero quadratic coefficient and the literal residual crossing has rank one, with

`T=||c||^2 ||r||^2 ||P_(c^perp) N P_(r^perp)||_F^2>0`,

that

`int_R |phi_Q(t)|dt <=6 pi 2^(2/3) T^(-1/6)`,                         (5.1)

`||p_Q||_infinity <=3*2^(2/3) T^(-1/6)`,                              (5.2)

and the density is continuous and vanishes at infinity.

The newer designated-partner checkpoint at commit `612be1591c1aa5edaeb29bb6eceec7963ddbef55` records an actual live heavy-hub partition with

`D_h >= (8/3125) V1`,                                                 (5.3)

and at the exact zero-pivot rank-one endpoint `D_h=T`. Substitution into (5.1)-(5.2) gives the concrete valid branch

`boxed:
 int_R |phi_Q(t)|dt
 <=6 pi 2^(2/3)(3125/8)^(1/6) V1^(-1/6)
 <80.900 V1^(-1/6),}`                                                (5.4)

`boxed:
 ||p_Q||_infinity
 <=3*2^(2/3)(3125/8)^(1/6) V1^(-1/6)
 <12.876 V1^(-1/6).}`                                                (5.5)

This is an equation-level use of a completed fleet02/B02 result. It survives the mixed-norm correction because it uses the exact `delta=0` `L2->L2` tensor theorem, not the false hard mixed-norm gate.

## 6. Current status

- Full QFORM: **OPEN**.
- Full-target continuity: **OPEN**.
- Target-wide universal `int |phi_Q|`: **OPEN / NOT REFUTED**.
- Earlier r40 hard mixed-norm lemma: **REFUTED** by the explicit product-projection family (2.1)-(2.4).
- Earlier r40 logarithmic glue theorem: **WITHDRAWN / UNPROVED**, because its bank tensorization used the refuted lemma.
- Scalar delta-uniform `L^(4/3)->L^4` chirp estimate (1.1): **VALID supporting lemma**.
- Exact `delta=0`, rank-one partner endpoint (5.4)-(5.5): **VALID Fourier-L1 branch**.
- First new analytic debt: prove or refute `QFORM-CHIRP-MAXIMAL-WEAKL2-v1`, or bypass it with a separate physical `E3/D5` receiver in the very-small nonzero-tail collar.

The construction in Section 2 also explains why simply adding the true low-dimensional projection-density theorem does not repair the mixed-norm route: fragmented original product supports survive an orthogonal two-coordinate projection and can force the required iterated norm to grow like `k^(1/4)`.