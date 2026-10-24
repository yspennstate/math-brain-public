SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T06:20:09Z.
attacking: heavy non-coloop two-sheet branch — route residual longitudinal curvature through a disjoint product bank and isolate the exact same-coordinate overlap obstruction.

# account02/B05 r23 — support-separated heavy-row closure and the overlap obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed for the new theorem; the conclusion is an essential density bound.

## 1. Exact obligation and source pins

The current B05 obligation is the uncovered indefinite convex/two-sheet curved integral, with original-coordinate product structure retained. The immediately preceding account02/B05 r22 closed the exact leverage-one coloop endpoint and left the heavy non-coloop residual-curvature state open.

Required newest Claude package actually used:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its Theorem C is applied, rather than reproved: for every exact-rank-three signature `(+,+,-)` form with active eigenvalue magnitudes at least one, and every interval `J` in the majority-sign one-sheet half-line,

`P(Q in J) <= pi sqrt(2) |J|`.                                      (1.1)

The source proves (1.1) by the exact ruled parametrisation and a two-dimensional product-projection marginal bound. Thus the one-sheet side is already paid at rough-input interval level. The present report attacks the opposite/full-line branch.

Immediate account02/B05 predecessors used:

- r21: `yspennstate/math-open-problems@c661893c05a7fd40d7f1e9b0a0a81a6f08f242a6`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T035943Z-account02-B05-QFORM-r21/REPORT.md`, theorem `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1`;
- r22: current source path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T043344Z-account02-B05-QFORM-r22/REPORT.md`, whose inverse certificate is rederived below rather than assumed as a black box.

Rank-two fractional receiver:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`. In the zero-affine case, for an orthonormal two-dimensional projection `Y` of a cap-one product law and invertible symmetric `S`,

`sup_t E |Y^T S Y-t|^(-1/2) <=16 sqrt(30)|det S|^(-1/4)`.            (1.2)

Latest compatible designated partner actually applied:

`account03/B05`, source read from current math archive at `yspennstate/math-open-problems@195447da931f086720afaa12ac902ed7d33dd32e`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T050645Z-account03-B05-QFORM-r21/REPORT.md`. Its six-coordinate global-curvature gate and escaped-curvature lemma are applied in Section 7.

Live corrections retained throughout: no post-rotation independence, no arbitrary-joint three-dimensional coarea bound, no unrestricted fiber supremum, no conditional-density-cap substitute for independence, and no treatment of a small matrix coefficient as a small random quadratic perturbation.

## 2. New support-separated heavy-row normal form

Let

`A=R Lambda R^T`, `R^T R=I_3`,                                     (2.1)

be an exact-rank-three target matrix: all three eigenvalues of `Lambda` have modulus at least one. Write the physical rows of `R` as `r_j in R^3`. Suppose one original coordinate `i` is heavy:

`c=||r_i||^2 >=1/2`.                                                 (2.2)

Choose the first active basis vector

`e1=r_i/sqrt(c)`.                                                     (2.3)

Assume the residual physical rows admit the exact **support separation**

`{j!=i}=J0 disjoint_union Jperp`,                                    (2.4)

where every `r_j`, `j in J0`, is parallel to `e1`, while every `r_j`, `j in Jperp`, lies in `e1^perp`.

This is an original-coordinate condition, not a spectral-independence assertion.

Parseval gives

`sum_j r_j r_j^T=I_3`.                                               (2.5)

Taking the `e1` component and the transverse block in (2.5),

`sum_(j in J0) r_j r_j^T=(1-c)e1e1^T`,                              (2.6)

while the transverse coefficient vectors on `Jperp` form a two-dimensional Parseval frame.

Hence the first active scalar is exactly

`S=sqrt(c) X_i + sqrt(1-c) U`,                                      (2.7)

where, if `c<1`, `U` is a normalized linear projection of the product bank `J0`; for `c=1` the second term is absent. The transverse active pair `(C,D)` is an orthonormal two-dimensional projection of the disjoint product bank `Jperp`.

Because the banks are disjoint original coordinates,

`S independent of (C,D)`.                                           (2.8)

Also convolution with the `J0` term cannot increase the cap of `sqrt(c)X_i`, so

`L:=||p_S||inf <=1/sqrt(c)<=sqrt(2)`.                               (2.9)

The two-dimensional product-projection estimate used in the required newest source gives

`M:=||p_(C,D)||inf<=2`.                                              (2.10)

Now rotate only inside `e1^perp` so that the cross vector from `e1` points along the first transverse axis. This rotates the already-dependent pair `(C,D)` as a pair; it never makes its coordinates independent. In the resulting active basis,

`B=[[a,beta,0],
    [beta,alpha,delta],
    [0,delta,gamma]]`.                                               (2.11)

The eigenvalues of `B` are those of `Lambda`, hence

`||B^(-1)||op<=1`, `|det B|>=1`,                                    (2.12)

and

`a^2+beta^2=||Be1||^2>=1`.                                          (2.13)

The target form is exactly

`Q=[S,C,D] B [S,C,D]^T`.                                             (2.14)

## 3. Large scalar curvature: square peel plus rank-two half-Riesz

Assume

`|a|>1/16`.                                                          (3.1)

Complete the square only in the genuinely independent scalar `S`:

`Q=a(S+(beta/a)C)^2 + [C,D] H [C,D]^T`,                             (3.2)

where

`H=[[alpha-beta^2/a,delta],[delta,gamma]]`,
`det H=det B/a`.                                                      (3.3)

For a scalar density cap `L`, the translated-square kernel gives, for a.e. `t`,

`p_Q(t)<=L |a|^(-1/2) E |t-[C,D]H[C,D]^T|^(-1/2)`.                  (3.4)

Apply (1.2) to the orthonormal product projection `(C,D)` and use (3.3):

`||p_Q||inf
 <=16 sqrt(30) L |a det B|^(-1/4)
 <=16 sqrt(30) sqrt(2) (1/16)^(-1/4)
 =32 sqrt(60)
 <247.871`.                                                          (3.5)

No support or moment bound is used.

## 4. Near-null scalar, substantial direct transverse curvature

Assume

`|a|<=1/16`, `|gamma|>=1/2`.                                        (4.1)

From (2.13),

`beta^2>=255/256`.                                                   (4.2)

The r21 scalar/dependent-pair theorem is stated for a scalar cap one. Normalize `S'=L S`, so `S'` has density cap at most one. The transformed coefficient matrix is

`B'=diag(1/L,1,1) B diag(1/L,1,1)`,                                 (4.3)

therefore

`beta'=beta/L`, `det B'=det B/L^2`,                                 (4.4)

and

`|beta'^2 gamma det B'|^(-1/6)
 =L^(2/3)|beta^2 gamma det B|^(-1/6)`.                              (4.5)

Applying r21 with pair-density cap `M<=2`, then (2.12), (4.1), (4.2), gives

`||p_Q||inf
 <=31 M^(2/3)L^(2/3)|beta^2 gamma det B|^(-1/6)
 <=31*2^(2/3)*(sqrt(2))^(2/3)*((255/256)*(1/2))^(-1/6)
 <69.639`.                                                           (4.6)

This step retains genuine scalar-versus-pair independence from (2.8); it does not infer it from a conditional cap.

## 5. Near-null scalar and small direct transverse curvature

First suppose

`0<|a|<=1/16`, `|gamma|<1/2`.                                       (5.1)

Let `x=B^(-1)e3`. By (2.12), `||x||<=1`. The first and third equations in `Bx=e3` are

`a x1+beta x2=0`,
`delta x2+gamma x3=1`.                                               (5.2)

Thus

`|x2|<=|a|/|beta|`,

and

`1<=|delta||x2|+|gamma||x3|
  <=|a delta|/|beta|+|gamma|`,                                      (5.3)

so

`|a delta|/|beta|>1/2`.                                              (5.4)

The cofactor identity is

`(B^(-1))_31=beta delta/det B`.                                     (5.5)

Again (2.12) implies

`|det B|>=|beta delta|`.                                             (5.6)

Multiplying (5.6) by `|a|` and using (5.4), (4.2),

`|a det B|>|a beta delta|>beta^2/2>=255/512`.                       (5.7)

Now repeat the scalar-square/rank-two half-Riesz estimate (3.4):

`||p_Q||inf
 <=16 sqrt(30)L |a det B|^(-1/4)
 <=16 sqrt(60)(512/255)^(1/4)
 <147.530`.                                                          (5.8)

Finally consider `a=0`. Invertibility gives `beta gamma!=0` and

`det B=-beta^2 gamma`.                                               (5.9)

The exact-null scalar/dependent-pair endpoint incorporated in r21, after the same normalization (4.3), gives

`||p_Q||inf
 <=31 M^(2/3)L^(2/3)|det B|^(-1/3)
 <=31*2^(5/6)
 <55.236`.                                                           (5.10)

Thus no singular loss occurs as the heavy row becomes null, provided the longitudinal residual bank remains physically disjoint from the transverse bank.

## 6. Main theorem and exact-rank-three reduction

### Theorem 6.1 — `QFORM-HEAVY-ROW-SUPPORT-SEPARATED-CLOSURE-v1`

Under (2.1)--(2.4), with arbitrary independent input densities bounded by one,

`boxed: ||p_(X^T A X)||inf <248.`                                   (6.1)

The proof is the exhaustive split (3.1), (4.1), (5.1), and `a=0`; the worst constant is (3.5).

This strictly extends the preceding leverage-one coloop theorem: `c=1` is the special case with no longitudinal residual bank `J0`. The new theorem allows every `c in [1/2,1]` and an arbitrarily large diffuse longitudinal bank, as long as it is disjoint in original-coordinate support from the transverse product bank.

A useful exact-rank-three corollary now reads:

- if every leverage is at most `1/2`, the required newest source Theorem F gives `||p_Q||inf<=12`;
- if a heavy row has the support separation (2.4), Theorem 6.1 gives `<248`.

Therefore an unpaid exact-rank-three instance must contain a heavy row `c>1/2` for which residual longitudinal and transverse spectral coefficients occur on some of the **same original coordinates**. This same-coordinate overlap is the precise point where `(S,C,D)` ceases to split as an independent scalar and dependent pair.

Define, after the heavy-row alignment, residual coefficients

`r_j=u_j e1+v_j`, `v_j in e1^perp`,                                 (6.2)

and the overlap currency

`Omega_i=sum_(j!=i) |u_j| ||v_j||`.                                 (6.3)

Parseval still gives `u` orthogonal to each transverse coefficient column globally, but this cancellation does not imply probabilistic independence. Theorem 6.1 is exactly the endpoint `Omega_i=0`. A proof uniform as `Omega_i downarrow0` is nonperturbative because the input supports and moments are unrestricted; a small coefficient cannot be discarded as a small random quadratic error.

## 7. Designated-partner result applied to a real full-target inequality

The latest compatible account03/B05 report supplies a six-coordinate global-curvature exit. If a set `P` of six original coordinates has

`s_3(A_PP)>=s>0`,                                                    (7.1)

then, after conditioning the complement and retaining all interpacket couplings inside `P`, its fixed-dimensional theorem gives

`||p_Q||inf <=1500(8+log 6)/s`.                                    (7.2)

In particular, at the concrete threshold `s=1/2`,

`boxed: s_3(A_PP)>=1/2  =>  ||p_Q||inf <29376.`                     (7.3)

Thus a remaining arbitrary-dimensional full-target proof may legitimately restrict to the class in which every six-coordinate packet under consideration has third singular value below `1/2`; this is a real target-level exit, not a heuristic.

The same partner report proves the complementary escaped-curvature identity. For a block split

`A=[[M,C],[C^T,D]]`,                                                 (7.4)

if `s_3(A)>=1` and `s_3(M)=epsilon<1`, then

`||C||op+||D||op>=1-epsilon`,                                       (7.5)

hence

`max(||C||op,||D||op)>=(1-epsilon)/2`.                              (7.6)

At `epsilon<1/2`, at least one escaped resource is at least `1/4`. This applies directly to the current obstruction: local two-sheet curvature cannot simply disappear when a chosen packet loses its third direction; it must escape through outside self-curvature or cross coupling. The new theorem pays one exact routing of that escaped resource — a disjoint residual longitudinal bank plus transverse product bank — while (7.5) shows why conditioning the outside resource away is not a valid general strategy.

The partner also gives an exact target-valid stress example `J_3 direct_sum (-J_3) direct_sum [1]`: three locally perfect indefinite packets can collapse to global rank two if their interpacket couplings are paid separately, while the outside square restores the third target eigenvalue. This is consistent with (7.5) and rules out tensorizing local packet estimates after conditioning away the escaped third curvature.

## 8. First unpaid implication

`QFORM-TWOSHEET-HEAVY-ROW-OVERLAP-COAREA-v1`:

For an exact-rank-three survivor with a heavy row `c>1/2`, write the residual active coordinates as

`Y1=sqrt(c)X_i+u^T Z`,
`(Y2,Y3)=V^T Z`,                                                     (8.1)

where `X_i` is independent of the residual product vector `Z`, the columns of `[u,V]` are mutually orthogonal, `||u||^2=1-c`, and `V^T V=I_2`. Prove a full-line interval bound uniform in the **same-coordinate overlap** between `u` and the rows of `V`, including the singular limit `Omega_i downarrow0`, without:

1. declaring the orthogonal linear forms independent;
2. conditioning one projected coordinate and using an unbounded conditional density cap;
3. replacing the reciprocal-shear curved trace by a worst fiber supremum; or
4. treating the overlap coefficients as a small random perturbation.

Equivalent acceptable exits are a product-sensitive Carleson/coarea estimate for the reciprocal-shear transform, or a reduction of the overlap resource to account03/B05's three-arm Frobenius packet with its same-side quadratic curvature retained.

The exact support-separated endpoint is now paid; the remaining missing factor is **same-original-coordinate longitudinal/transverse overlap**, not heavy leverage itself and not coarse two-dimensional transverse concentration.

## 9. Status

- Full arbitrary-dimensional QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Required rough-input ruled one-sheet theorem: **source-applied at (1.1), already paid**.
- New heavy non-coloop support-separated exact-rank-three class: **proved here, density `<248`**.
- Latest account03/B05 six-coordinate global-curvature gate: **applied at (7.3)**.
- Latest account03/B05 escaped-curvature lemma: **applied at (7.5)--(7.6)**.
- Independent review of Theorem 6.1: **PENDING**.
- First unpaid B05 implication: **heavy-row same-coordinate overlap / reciprocal-shear curved coarea**.
