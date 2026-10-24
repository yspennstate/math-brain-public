SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T18:16:36Z.
attacking: the rough hidden-projection zero-pivot endpoint; condition away an exact source cocircuit and recover the pure-hub transverse-square bound without a small-random-perturbation step.

# account01/B11 — exact source-deletion compiler for the rough zero-pivot hub

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T181636Z-account01-B11-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed from the new argument; the conclusion below is an essentially bounded density.

The unrestricted conjecture remains **OPEN**. Nothing below assumes moments, compact support, connected support, Gaussianity, log-concavity, identical input laws, independence after spectral rotation, or law-uniform pointwise quadratic-phase decay.

## 1. Fresh source state and the exact gap attacked

Fresh `math-research-brain` control has OWNER CONTROL revision `2026-09-22.15`, with `QFORM-DENSITY-3EIG-20260922` as the sole mathematical target. The current owner continuation is `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. I reread `AGENTS.md`, `scheduled_tasks/README.md`, `fleet.json`, `roles.json`, `PROTOCOL.md`, `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and the account01/B11 assignment.

The source corrections used here include in particular:

- bounded projected density does not by itself control an indefinite quadratic pushforward;
- a bounded conditional density cap does not replace genuine independence;
- rotations do not preserve the source product structure;
- small matrix coefficients cannot be treated as small random errors for arbitrary unbounded rough laws;
- the arbitrary rough single-hub adapted-profile statement `SP` remains open.

The preceding account01/B11 run gave, at an exact zero physical hub pivot, the source-provenance normal form

`Q = 2 kappa L [X_0 + m(L,V,Pi)] + lambda V^2`,                    (1.1)

with the ORIGINAL hub variable `X_0` independent of the light source bank, while the hidden term inside `m` can be strongly dependent on `(L,V)`. It also proved the determinant currency

`kappa^2 |lambda| = c |det M| >= c s^3`,                           (1.2)

where `c` is the physical hub leverage and `s=min_j |eig_j(M)|`. The newest Claude continuation explicitly records that a local conditional/maximal estimate for the hidden projection can grow for comb laws, so one cannot close (1.1) by saying that the hidden coefficient is small.

This run changes mechanism: it identifies an exact ORIGINAL-coordinate deletion criterion under which the hidden projection is absorbed algebraically, with no perturbation estimate at all.

The analytic receiver is the proved pure-hub theorem in

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/counterexample_search/REPORT.md`

and its later exact large-curvature evaluation in

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/research/hub_new.md`.

The designated partner result actually applied in Section 6 is account02/B11,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260923T155550Z-account02-B11-QFORM-auto11c/REPORT.md`.

It proves that in its near-null-ruling chamber either an actual product-preserving cross cut gives

`||p_Q||_infinity < 133299/(s tau^2)`,                              (1.3)

or one ORIGINAL coordinate `h` has spectral leverage

`c_h=||r_h||^2 > tau/36`.                                          (1.4)

## 2. First new lemma: one homogeneous pure-hub bound for every curvature scale

The proved pure-hub theorem treats

`Q_mu = 2 X_h(L+beta) + mu (V-v_c(L))^2 + F_c(L)`,                  (2.1)

where `L,V` are orthonormal linear forms of the light ORIGINAL product variables, `X_h` is a disjoint original coordinate with density cap one, and `v_c,F_c` are arbitrary measurable functions of `L` of the stated form in the source proof. No independence of `L` and `V` is assumed.

The source gives, writing `mu>0`,

`B(mu)=2sqrt(2)+sqrt(2) log(1/3+4sqrt(2)/mu)` for `0<mu<=6sqrt(2)`, (2.2)

and the later exact bathtub evaluation gives

`B(mu)=(192/mu)^(1/3)` for `mu>=6sqrt(2)`.                          (2.3)

### Lemma 2.1 — global envelope

For every `mu>0`,

`B(mu) <= (192/mu)^(1/3)`.                                          (2.4)

#### Proof

Only (2.2) needs checking. Put

`y=(6sqrt(2)/mu)^(1/3)>=1`.                                         (2.5)

Because

`1/3+4sqrt(2)/mu=(1+2y^3)/3`,

and

`(192/mu)^(1/3)/sqrt(2)=2y`,

inequality (2.4) is equivalent to

`2+log((1+2y^3)/3) <=2y`.                                           (2.6)

The two sides agree at `y=1`. If `F(y)` is the right side minus the left side, then

`F'(y)=2-6y^2/(1+2y^3)`
`     =2(2y^3-3y^2+1)/(1+2y^3)`
`     =2(y-1)^2(2y+1)/(1+2y^3)>=0`.                                (2.7)

Hence (2.6), and therefore (2.4), holds. QED.

### Corollary 2.2 — homogeneous pure-hub receiver

For nonzero real `a,b`,

`Q = 2a X_h(L+beta) + b(V-v_c(L))^2 + F_c(L)`                      (2.8)

has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= 192^(1/3) |a|^(-2/3)|b|^(-1/3)
 = 192^(1/3) (a^2|b|)^(-1/3).`                                    (2.9)

Indeed divide the whole random variable by `|a|`, reflect signs if necessary, apply (2.4) with `mu=|b/a|`, and scale the output density back.

Numerically

`192^(1/3)=5.768998281229633...`.                                  (2.10)

This is only a repackaging and sharpening-across-scales of the proved pure-hub theorem; it is not a claim of a new external theorem.

## 3. Main new theorem: exact source-deletion / conditionable-span compiler

Let `X_0,X_1,...,X_m` be independent and each have density at most one. On the light source coordinates define three real coefficient vectors `l,v,p` and the linear forms

`L=l.X`, `V=v.X`, `P=p.X`.                                          (3.1)

Consider the zero-hub-pivot quadratic normal form

`Q = 2 kappa L X_0
    + gamma L^2 + 2 delta L V + lambda V^2
    + 2 theta L P
    + ell_0 X_0 + ell_L L + ell_V V + ell_P P + q_0`,              (3.2)

where `kappa lambda !=0`. The affine terms are included because conditioning outside coordinates produces them.

Take an ORIGINAL-coordinate subset `K` of the light coordinates, put `R=K^c`, and write restrictions as `l_R,v_R,p_R`. Define the residual two-area

`Delta_R = ||l_R||^2 ||v_R||^2 - <l_R,v_R>^2`.                      (3.3)

### Theorem 3.1 — `QFORM-HIDDEN-PROJECTION-CONDITIONABLE-SPAN-v1`

Assume

`Delta_R>0`,                                                        (3.4)

and the exact source-span condition

`p_R in span{l_R,v_R}`.                                             (3.5)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 192^(1/3) (kappa^2 |lambda| Delta_R)^(-1/3).`                  (3.6)

The bound is completely independent of `gamma,delta,theta`, all affine coefficients, the number and values of coordinates conditioned in `K`, and the roughness/fragmentation of all source densities.

### Proof

Condition on the ORIGINAL variables `X_K`. All their contributions to `L,V,P` become deterministic constants. Denote the remaining linear forms by

`L_R=l_R.X_R`, `V_R=v_R.X_R`, `P_R=p_R.X_R`.                       (3.7)

By (3.5), for some deterministic `A,B`,

`P_R=A L_R+B V_R`.                                                   (3.8)

Therefore the hidden quadratic term

`2 theta L P`                                                       (3.9)

contributes, after conditioning, only an `L_R^2` term, an `L_R V_R` term, and affine/constant terms. Crucially it contributes **no new `V_R^2` coefficient** beyond the original `lambda V_R^2`.

Set

`g=||l_R||^2>0`,                                                     (3.10)

`alpha=<l_R,v_R>/g`,                                                (3.11)

`v_perp=v_R-alpha l_R`.                                             (3.12)

Then

`||v_perp||^2=Delta_R/g>0`.                                         (3.13)

Define

`L_1=L_R/sqrt(g)`,
`V_1=(v_perp.X_R)/sqrt(Delta_R/g)`.                                 (3.14)

The coefficient vectors producing `L_1,V_1` are orthonormal in the ORIGINAL source-coordinate Euclidean space. Hence this is exactly the product-projection geometry in the pure-hub theorem; no independence between `L_1` and `V_1` is asserted or needed.

Since

`V_R=alpha L_R + sqrt(Delta_R/g) V_1`,                              (3.15)

and every quadratic term other than `lambda V_R^2` is at most linear in `V_R` once `L_R` is fixed, the conditioned form can be written by completing one square as

`Q = 2 a (L_1+beta_K) X_0
    + b (V_1-v_K(L_1))^2
    + F_K(L_1)`,                                                    (3.16)

where `beta_K` depends only on the frozen coordinates,

`a=kappa sqrt(g)`,                                                   (3.17)

`b=lambda Delta_R/g`,                                               (3.18)

and `v_K,F_K` absorb all remaining quadratic and affine terms. The possible linear term in `X_0` is absorbed into the shift `beta_K` because `a!=0`.

The key invariant is exact:

`a^2 |b|
 = kappa^2 g * |lambda| Delta_R/g
 = kappa^2 |lambda| Delta_R`.                                       (3.19)

Apply Corollary 2.2 to the conditional law. Its bound is uniform in every frozen value:

`||p_(Q|X_K)||_infinity
 <=192^(1/3)(kappa^2|lambda|Delta_R)^(-1/3)`.                       (3.20)

To remove any measurability issue about choosing conditional density versions, let `E` be a Borel set of finite Lebesgue measure. The conditional theorem gives

`P(Q in E | X_K)
 <= C |E|`                                                          (3.21)

for almost every frozen value, with the same constant `C` from (3.20). Averaging yields

`P(Q in E)<=C|E|`.                                                   (3.22)

Hence the unconditional law is absolutely continuous and its Radon--Nikodym derivative has essential supremum at most `C`. This proves (3.6). QED.

## 4. Product provenance and the exact geometric currency

The condition (3.5) is purely an ORIGINAL-coordinate statement. No spectral rotation of the random vector is made.

It has two useful exact forms.

First, `p_R in span{l_R,v_R}` says that the three-row source coefficient map on `R` has rank at most two:

`rank([l_R;v_R;p_R])<=2`.                                           (4.1)

Second, the residual area is the Cauchy--Binet sum

`boxed:
 Delta_R = sum_{i<j, i,j in R}(l_i v_j-l_j v_i)^2.`                  (4.2)

Thus the theorem pays a source cocircuit only after the hidden third source coefficient has become exactly dependent on the two saddle/square coefficients, while retaining a quantitative two-dimensional area.

A trivial but sometimes useful special case is `|R|=2`: whenever the physical `2 x 2` coefficient minor of `(l,v)` is nonzero, condition (3.5) is automatic. The resulting constant may, however, deteriorate with a diffuse frame because `Delta_R` can be small. The theorem therefore does **not** smuggle in a uniformly good physical pair.

A more favorable special case is `p_R=0`; then (3.5) is automatic and an arbitrarily large residual product bank may be kept before paying `Delta_R`.

## 5. Application to the B11 zero-pivot indefinite canonical form

Return to exact rank three

`A=R M R^T`, `R^T R=I_3`,                                          (5.1)

and choose an ORIGINAL physical coordinate `h` with spectral row

`r_h=sqrt(c)e`, `c>0`.                                              (5.2)

Assume its physical pivot is exactly zero:

`A_hh=c e^T M e=0`.                                                  (5.3)

Choose an orthonormal spectral basis `(e,f,g)` with the transverse first axis aligned to the nonzero vector `P_(e^perp)Me`. Then

`M = [[0,beta,0],[beta,gamma,delta],[0,delta,lambda]]`.             (5.4)

Invertibility implies `beta lambda !=0`. Write the residual spectral projections as

`T=p.X`, `L=l.X`, `V=v.X`,                                         (5.5)

so Parseval gives `l,v` orthonormal, `p` orthogonal to both, and `||p||^2=1-c`. Expanding the quadratic form gives

`Q=2 beta (sqrt(c)X_h+T)L + gamma L^2+2delta LV+lambda V^2`.         (5.6)

Thus (3.2) holds with

`kappa=beta sqrt(c)`, `theta=beta`.                                 (5.7)

The determinant identity is

`det M=-beta^2 lambda`,                                              (5.8)

so if

`s=min_j|eig_j(M)|`,                                                 (5.9)

then

`boxed:
 kappa^2 |lambda|
 =c |det M|
 >=c s^3.`                                                          (5.10)

Consequently, whenever an ORIGINAL residual set `R` satisfies (3.4)--(3.5),

`boxed:
 ||p_Q||_infinity
 <= (192/(c Delta_R))^(1/3) s^(-1).`                               (5.11)

This is sign symmetric. For signature `(2,1)`, equation (5.8) forces `lambda>0`; for signature `(1,2)` it forces `lambda<0`. Hence the transverse square carries the majority sign, exactly as in the preceding B11 canonicalization.

### Exact-coloop endpoint

If `c=1`, Parseval forces `p=0`. Taking all light coordinates as `R` gives `Delta_R=1` because `l,v` are orthonormal. Therefore every exact-coloop, zero-pivot rank-three indefinite form of this type satisfies

`boxed:
 ||p_Q||_infinity
 <=192^(1/3) s^(-1)
 <5.769/s.`                                                         (5.12)

This closes the exact zero-width endpoint of the hidden-projection obstruction without requiring a volume-sampling cut; the partner's regular-polygon coloop stress family is included.

## 6. Designated partner result applied to an actual inequality

The completed account02/B11 relative-atom theorem proves the following exhaustive alternative **inside its exact-rank-three near-null-ruling chamber**:

1. the atom-diffuse branch has a continuous density obeying (1.3); or
2. there is one ORIGINAL coordinate `h` with leverage (1.4).

Apply the second conclusion to the zero-pivot subcase `A_hh=0`. Then (5.10) and (1.4) imply

`kappa^2|lambda|
 =c_h|det M|
 > (tau/36) s^3`.                                                   (6.1)

If the residual source coefficients at this same dominant coordinate admit a conditionable-span set `R` with `Delta_R>0`, Theorem 3.1 therefore gives the literal partner-assisted inequality

`boxed:
 ||p_Q||_infinity
 < (6912/(tau Delta_R))^(1/3) s^(-1).`                             (6.2)

For example, a branch with `Delta_R>=1/4` is paid by

`||p_Q||_infinity
 < 27648^(1/3) tau^(-1/3) s^(-1)
 <30.239 tau^(-1/3)/s.`                                            (6.3)

The point is not the numerical constant or the remaining `tau` dependence. The substantive gain is that the designated partner's dominant ORIGINAL atom is now converted into a legal hub coefficient, while all hidden rough dependence is removed **only when an exact source-span deletion exists**, not by replacing a conditional density cap with independence.

Combining the partner theorem with the new compiler gives the following checked branch split:

- atom-diffuse null-ruling geometry: `<133299/(s tau^2)`, continuous;
- dominant-atom + exact zero pivot + conditionable residual source area `Delta_R`: (6.2), essentially bounded;
- the remaining dominant-atom state must have either a nonzero pivot, or every product-preserving deletion that makes the hidden coefficient dependent on `(l,v)` has too little residual two-area.

Small nonzero pivots remain distinct and are not replaced by the zero-pivot argument.

## 7. Rank-two logarithm and the exact role of the third direction

The mandatory rank-two control remains unchanged. For independent centered unit uniforms `X,Y`,

`T=2XY`

has

`p_T(t)=log(1/(2|t|)),  0<|t|<1/2`,                                (7.1)

so the opposite-sign rank-two saddle has a genuine logarithmic singularity.

The present theorem identifies exactly what the third direction contributes after a valid source deletion. Once `p_R` is absorbed into the `(L_R,V_R)` plane, the form becomes

`2 a (L_1+beta) X_h + b(V_1-v_c(L_1))^2+F(L_1)`,                  (7.2)

and its smoothing currency is

`boxed: a^2|b|=kappa^2|lambda|Delta_R.`                            (7.3)

The factor `Delta_R` is genuine ORIGINAL-coordinate product area; `kappa^2|lambda|` is the rank-three determinant currency. If the transverse square is deleted (`lambda=0`) in the exact-rank-three zero-pivot matrix (5.4), then `det M=0`, contradicting rank three. Thus the third spectral direction forces a square whose curvature, combined with surviving product two-area, makes the pure-hub water-filling integral finite. No statement that the rank-two saddle itself becomes bounded is made.

## 8. Finite verification

A deterministic seeded check was run on 1000 random seven-coordinate orthonormal triples `(l,v,p)`. For each sample I selected the physical pair with maximal `(l_i v_j-l_j v_i)^2`; on a two-coordinate residual set the span condition is automatic. The checker verified simultaneously

`||v_perp||^2=Delta_R/||l_R||^2`,

reconstruction of `p_R` from `l_R,v_R`, and

`(kappa sqrt(g))^2 * |lambda Delta_R/g|
 =kappa^2|lambda|Delta_R`.

The maximum numerical discrepancy was `2.22e-15`. Across those samples the selected `Delta_R` ranged from approximately `0.0979` to `0.7586`. This is only an arithmetic audit of the identities, not an independent proof and not evidence of a universal minor lower bound.

The analytic envelope (2.6) was also checked symbolically through the exact derivative factorization (2.7), so no numerical fit is used in the theorem.

## 9. What remains open

The first B11 implication left by this run is

`QFORM-HIDDEN-PROJECTION-AREA-OR-CURVATURE-v2`:

> In the rough dominant-hub indefinite chamber, prove a product-preserving alternative that either (i) finds an ORIGINAL deletion `K` for which `p_R in span{l_R,v_R}` and `Delta_R` is quantitatively large enough for Theorem 3.1, or (ii) uses the genuinely three-dimensional residual source frame `(l,v,p)` jointly with the forced `lambda V^2` curvature to enter a completed projected-crossing / overlap-square / volume receiver. The estimate must remain uniform as `||p|| ->0` and cannot treat the hidden projection as a small random perturbation.

Two other bridges remain separate:

- a small **nonzero** physical hub pivot must be handled without replacing it by zero;
- arbitrary additional nonseparable spectrum beyond exact rank three still needs a stability/reduction argument satisfying the exact hypotheses of the available full-matrix theorems.

The current rough-input SP statement is not proved here. A repository search for the exact `conditionable-span` formulation did not return a source match, but that search result is not evidence of external novelty.

## 10. Source/status summary

- full QFORM target: **OPEN**;
- `QFORM-HIDDEN-PROJECTION-CONDITIONABLE-SPAN-v1`: **PROVED SUPPORTING THEOREM**;
- homogeneous pure-hub envelope (2.9): **derived from already-proved source results**;
- designated partner account02/B11 result: **applied at (6.1)--(6.3)**;
- continuity of the new compiler: **not claimed**;
- rank-two logarithmic obstruction: **retained exactly**;
- execution status: `WITHOUT_VERIFIED_BRAIN`.
