# account01/B18 r52 — two physical zero-hubs plus a projected planar right bank

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T095853Z-account01-B18-qform-auto11-r52`  
**Assignment:** literature-to-proof transfer  
**Status:** PROVED SUPPORTING TARGET-LEVEL CHAMBER / LATEST ACCOUNT02-B18 PARTNER APPLIED / FULL QFORM OPEN  
**Continuity:** not asserted for the generic theorem; unrestricted continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-24T09:58:53Z.

attacking: literature-to-proof transfer for the two-physical-hub / projected-planar-right chamber, splicing the fresh account02/B18 transverse-curvature funnel with source-valid marginal-density and planar square smoothing.

## 1. Fresh source and correction boundary

Fresh controls were read from `math-research-brain`; owner control remains revision `2026-09-22.15`, programme revision `2026-09-22.5`, and the full theorem remains OPEN.

The corrections used here are essential:

- orthogonal projections of a product law may be dependent;
- an unconditional joint density cap is not a conditional density cap or independence statement;
- arbitrary bounded joint density does not by itself permit the refuted indefinite rank-three coarea shortcut;
- small nonzero crossing or curvature terms are retained exactly, not deleted;
- no law-uniform pointwise quadratic-phase decay is used.

The latest completed designated partner is account02/B18 run `20260924T091122Z-account02-B18-qform-auto11-r52`, scientific commit

`4fe63a9ccd89f7b3ddd0f69df95e9615318aeeec`.

Its theorem `QFORM-RANK1-COLLAR-FORCES-TRANSVERSE-CURVATURE-v1` says, for an ORIGINAL-coordinate zero-self split

`A=[[0,D],[D^T,C]]`,

with `s=s3(A)`, singular values `d1>=d2>=...` of `D`, top right singular vector `v`, and `P=I-vv^T`,

`boxed: s <= d2 + ||P C P||op.`                                      (1.1)

The proof is deterministic: remove the top rank-one singular piece of `D` and all curvature touching `v`; the removed matrix has rank at most two, while the remainder has norm at most `d2+||PCP||op`.

## 2. Primary literature transfer

### 2.1 Livshyts--Paouris--Pivovarov

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1.

If `Y=(Y_i)` has genuine product density `prod_i f_i` with every `||f_i||inf<=1`, every `k`-dimensional orthogonal marginal has density cap at most

`2^(k/2)`.

The hypotheses match the owner input class: no iid, moments, compact support, centering, symmetry, smoothness or log-concavity assumption occurs. The conclusion is a marginal-density statement only. In particular, for an orthonormal pair `v,w`,

`L=v^T Y,  V=w^T Y`

may be dependent, but their joint density obeys

`||p_(L,V)||inf <=2`.                                                (2.1)

The one-dimensional version gives the normalized scalar-projection cap `sqrt(2)`.

### 2.2 Banks--Garza Vargas--Kulkarni--Srivastava

Primary source: J. Banks, J. Garza Vargas, A. Kulkarni, N. Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, arXiv:2005.08930, Theorem 2.1 and Corollary 2.4 (`Density of Quadratic Forms`).

Their scalar theorem treats a bilinear-affine packet

`X^T Z Y + X^T U + V^T Y + W`

for independent-entry density-capped banks and pays geometric means of singular values of `Z`. Thus the bilinear conditioning mechanism used below is prior literature, not a novelty claim. Their literal theorem does not state arbitrary same-`Y` quadratic curvature. However, in the scalar conditioning proof, an additive function `G(Y)` is only a translation after conditioning on `Y`; the derivation below records this extension directly under the exact owner hypotheses.

## 3. A curved rank-two cross receiver with exact constants

Let `X=(X1,X2)` be two independent ORIGINAL variables with density caps one, and let `Y` be a disjoint product bank. Let `Z=(L,V)` be any orthonormal two-dimensional projection of `Y`, so (2.1) holds. Let

`D=[[a,0],[p,q]]`,  `q!=0`,

and let `G(L,V)` be arbitrary measurable. Then

`T=2 X^T D Z + G(Z)`                                                (3.1)

has

`boxed: ||p_T||inf <= 2 sqrt(pi)/sqrt(|a q|).`                      (3.2)

Proof. Condition on `Z=z`. The normalized scalar projection theorem gives the conditional density cap

`||p_(T|Z=z)||inf <= 1/(sqrt(2)||Dz||).`                            (3.3)

Indeed the coefficient of `X` is `2Dz`, so scaling the `sqrt(2)` normalized cap gives (3.3). Now put `U=DZ`. Since the joint density of `Z` is at most two,

`||p_U||inf <= 2/|det D|=2/|a q|.`                                 (3.4)

For any probability density `g` on `R^2` with `0<=g<=M`, radial rearrangement gives

`int g(u)/||u|| du <= 2 sqrt(pi M).`                                (3.5)

(The extremizer is the cap `M` on a centered disk of area `1/M`.) Averaging (3.3) and applying (3.4)--(3.5) proves (3.2). No independence between `L` and `V` is asserted or needed. QED.

## 4. The source-valid planar chamber

Consider the full active quadratic

`Q = 2a X1 L + 2 X2(p L+q V) + b L^2 + 2c L V + e V^2`,             (4.1)

where `X1,X2` are literal independent original coordinates with density caps one, `L,V` are as in Section 2 and are independent of `(X1,X2)`, and all coefficients are real. The physical active matrix in the order `(X1,X2,L,V)` is

`H=[[0,0,a,0],
    [0,0,p,q],
    [a,p,b,c],
    [0,q,c,e]].`                                                    (4.2)

Relabel the two literal hubs so that the first cross row has at least the Euclidean norm of the second; rotate only the deterministic right active plane so the first row becomes `(a,0)` with `a>0`. This rotation is applied to the already-joint pair only; the probabilistic input used afterward is precisely the LPP joint-density cap, not independence.

Write

`s=s3(H)>0`, `delta=|q|/s`.                                         (4.3)

### 4.1 First deterministic currency: the main crossing is large

Subtract `diag(0_2,C)`, where `C=[[b,c],[c,e]]`. The subtracted matrix has rank at most two, while the remainder is the symmetric cross matrix with operator norm `||D||op`. Therefore

`s <= ||D||op <= ||D||F <= sqrt(2) a`,

so

`boxed: a >= s/sqrt(2).`                                            (4.4)

### 4.2 New planar sharpening of the partner/B06 transverse-curvature budget

The prior fleet theorem of account01/B06 and the fresh account02/B18 partner give triangle-form residual budgets. In the present **two-dimensional active right plane** one can sharpen them exactly.

Define

`R=[[0,0,a,0],
   [0,0,p,0],
   [a,p,b,c],
   [0,0,c,0]].`                                                     (4.5)

Writing `u=e_L` and `z=(a,p,b/2,c)`, one has `R=u z^T+z u^T`, hence `rank(R)<=2`. Moreover

`H-R`

is supported only on the `(X2,V)` plane and equals

`K=[[0,q],[q,e]].`                                                  (4.6)

Consequently, by the rank-two approximation characterization of `s3`,

`boxed: s <= ||K||op = (|e|+sqrt(e^2+4q^2))/2.`                    (4.7)

If `|q|<s`, (4.7) yields

`boxed: |e| >= s-q^2/s = s(1-delta^2).`                             (4.8)

This is deterministic. It does not treat the `q`-term as a random perturbation and it keeps all `b,c,p` exactly.

## 5. Second analytic receiver: pay the transverse square without conditioning a projected coordinate

A prior source-valid optimized planar square-root lemma is pinned at

`math-open-problems@b8cb4aa22c840d8f4fc76bcca6d0cb49d4aeb9f9`

`proofnet24/QFORM-density/interactive/20260923T222500Z-two-physical-leaf-pair-arbitrary-hub/REPORT.md`.

It states: if a cap-one scalar `H0` is genuinely independent of a planar pair `(ell,w)` of joint density cap `K0`, then for arbitrary measurable `r(ell)`,

`||p_(2 H0 ell+r(ell)+w^2)||inf <= 3*2^(2/3) K0^(2/3).`             (5.1)

No conditional density of one projected coordinate given the other is used.

Assume `e!=0` in (4.1), and condition only on the literal original coordinate `X2=x`. Complete the square by setting

`W=V+(c/e)L+(q/e)x`,

`Hx=X1 + [(p-cq/e)/a] x.`                                          (5.2)

Then `Hx` has density cap one and is genuinely independent of `(L,W)`, while

`Q|X2=x = 2a Hx L + (b-c^2/e)L^2 -(q^2/e)x^2 + e W^2.`             (5.3)

The shear/translation `(L,V)->(L,W)` has determinant one, so `(L,W)` still has joint density cap at most two. Scale `ell=aL` and `w=sqrt(|e|)W` (and reflect the output if `e<0`). The planar cap becomes at most `2/(a sqrt(|e|))`. Applying (5.1) uniformly in `x` and averaging gives

`boxed: ||p_Q||inf <= 3*2^(4/3) a^(-2/3)|e|^(-1/3).`               (5.4)

This is the square branch.

## 6. Universal payment for the entire planar chamber

If `q!=0`, Section 3 gives the cross branch

`||p_Q||inf <= 2 sqrt(pi)/sqrt(a|q|).`                              (6.1)

Using (4.4),

`||p_Q||inf <= [2^(5/4)sqrt(pi)]/[s sqrt(delta)].`                  (6.2)

If `0<=delta<1`, combine (4.4), (4.8), and (5.4):

`||p_Q||inf <= [3*2^(5/3)]/[s(1-delta^2)^(1/3)].`                  (6.3)

At `delta=0`, (6.3) applies directly. For `delta>=1`, (6.2) applies. On `(0,1)`, the first right side decreases and the second increases, so their minimum is maximized at their unique crossing `delta_*`, determined by

`pi^3(1-delta_*^2)^2 = 3^6 2^(5/2) delta_*^3.`                      (6.4)

Numerically,

`delta_*=0.1911071429483536143393...`,

and

`C_planar = 2^(5/4)sqrt(pi)/sqrt(delta_*)
          = 9.64326210300941539178... .`                            (6.5)

Therefore:

### Theorem — `QFORM-TWO-PHYSICAL-HUB-PROJECTED-PLANAR-RIGHT-v1`

For every quadratic (4.1) under the source provenance stated above,

`boxed: ||p_Q||inf < 9.644/s3(H).`                                  (6.6)

In particular, if this active block itself has `s3(H)>=1`, then `||p_Q||inf<9.644` for every admissible rough product input law. The theorem permits arbitrary `p,b,c,e`; the second crossing `q` may be arbitrarily small but nonzero and is never deleted.

An independent additive remainder from a disjoint original-coordinate bank can be added without worsening (6.6), by convolution with its probability law.

## 7. Literal application of the fresh designated partner

Now specialize to the fresh account02/B18 rank-one-collar coordinates: the two cross rows are orthogonal singular directions,

`D=diag(d1,d2)`, `d1>=d2>=0`,                                      (7.1)

so in (4.1) `p=0`, `a=d1`, `|q|=d2`. Since the right active plane has dimension two, the fresh partner theorem (1.1) becomes the **actual scalar inequality**

`|e| >= s-d2`,                                                      (7.2)

where again `s=s3(H)`. Also `s<=||D||op=d1`, so `a>=s`.

Put `delta=d2/s`. The literature cross receiver gives

`B_cross(delta)=2sqrt(pi)/(s sqrt(delta))`,                         (7.3)

while applying the optimized planar square receiver to the partner output (7.2) gives

`B_partner(delta)=3*2^(4/3)/(s(1-delta)^(1/3)).`                   (7.4)

For `delta>=1`, (7.3) is already at most `2sqrt(pi)/s`; for `0<=delta<1`, optimize the minimum of (7.3)--(7.4). The crossing solves

`pi^3(1-delta)^2 = 2916 delta^3`,                                  (7.5)

hence

`delta=0.1909314912171633103125...`

and

`boxed: ||p_Q||inf <= 8.11271369788456983227... / s.`               (7.6)

This is a literal completed-partner-to-density splice, not merely a citation.

The planar-specific deterministic sharpening (4.8) improves (7.2) further to `|e|>=s(1-delta^2)`. If one uses that stronger local fact, the corresponding same-family constant is

`boxed: 7.67764351659874073801... / s,`                             (7.7)

with crossing `delta=0.2131836910496417328352...`. Equation (7.6) is retained separately because it is the requested direct application of the designated partner theorem itself.

## 8. What is and is not closed

This run closes the whole chamber in which:

1. a zero-self side consists of two literal ORIGINAL coordinates;
2. the cross map from those two coordinates has right active dimension at most two;
3. the opposite-bank quadratic curvature is supported on that same projected two-dimensional plane.

It is stronger than an exact-rank-one endpoint: the nonzero second crossing is retained and the two cross rows need not be orthogonal.

It does **not** solve the full owner theorem. The global structural compiler still has to obtain such a product-preserving planar packet, or route failures into already-paid higher-rank cross, mixed-hub, ridge, volume, or other source-valid exits. In particular the latest account02/B18 partner survivor may have transverse curvature living in dimension greater than one and may carry a nonzero `d2` tail; (6.6) does not compress arbitrary high-dimensional curvature to a plane.

Continuity is deliberately separate. The argument proves existence of an essentially bounded density in this chamber. No generic `C_0` conclusion is claimed here.

## 9. Novelty discipline

The following ingredients are explicitly prior work and are not claimed as new:

- product-marginal density caps: Livshyts--Paouris--Pivovarov;
- bilinear geometric-mean anticoncentration: Banks--Garza Vargas--Kulkarni--Srivastava and prior fleet transfers;
- optimized planar square-root receiver: pinned prior fleet theorem;
- triangle-form transverse-curvature funnel: prior B06 work and fresh account02/B18 theorem.

The mathematical addition recorded here is the source-valid synthesis for (4.1), including the exact two-dimensional rank-two-approximation sharpening (4.7)--(4.8), and its resulting all-parameter bound (6.6). No publication-novelty claim is made.
