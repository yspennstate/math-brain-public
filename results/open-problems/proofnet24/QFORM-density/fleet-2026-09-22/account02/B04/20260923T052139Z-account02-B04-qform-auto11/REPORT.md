SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T05:21:39Z.
attacking: entropy-optimized two-volume Fourier rearrangement on a physical rank-two cross packet, compared against ridge certificates on the same rotated indefinite target matrix.

# account02/B04 — entropy-reweighted rank-two half-Riesz closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING THEOREM / EXPLICIT TARGET-VALID ESTIMATE / RIDGE-CERTIFICATE OBSTRUCTION / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The first unpaid B04 implication is now

`QFORM-RANK2-MINOR-SUPPORT-FRACTIONAL-MATCHING-OR-HUB-v1`:

> In every remaining low-cross-rank/no-pivot survivor of the full three-large-eigenvalue problem, prove that an original-coordinate rank-two physical packet either admits an entropy-efficient probability weight on its nonzero physical `2x2` minors with every row marginal bounded away from one (ideally at most `1/2`), or that failure of such a fractional-matching weight forces an original-coordinate hub/coloop configuration compatible with an already-completed grouped-square, mixed-hub, pair-log, or null-coloop mechanism.

This is now the structural debt. The analytic rank-two endpoint itself can be paid even when the *canonical* two-volume law is almost completely concentrated on one physical row and every current ridge certificate fails.

Full QFORM remains OPEN. No continuity claim is made for the new square-peel branch below.

## 2. Source-pinned inputs and corrections

The required Claude source was consumed at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

The exact completed ingredient used below is Theorem D's arbitrary-minor-weight determinant/weighted-AM-GM step: canonical squared-minor volume weights can be replaced by an arbitrary probability weight on nonzero minors, with the determinant scale replaced by

`exp(E_w log det^2 + H(w))`.

The rank-two fractional time integration is the completed `QFORM-VOLUME-MARGINAL-WEIGHTED-RIESZ-v1` / fractional-volume compiler in

`yspennstate/math-open-problems@da12fa65ddad431624952613e034f1a4d783098b`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T013054Z-auto11/REPORT.md`,

whose proof uses the same determinant datum followed by sharp Hausdorff--Young and a fractional-Riesz kernel. I extend only the determinant input from canonical weights to arbitrary weights; all later constants are unchanged.

The designated partner `account03/B04` was read through its latest completed r25 theorem at

`yspennstate/math-open-problems@37ba54a65abfdcb49595a6aa820567ac20da4f41`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T045000Z-account03-B04-qform-r25/REPORT.md`,

and its r24 ridge review at the same repository state, path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260923T034739Z-r24/REPORT.md` (the independently checked ridge source is pinned elsewhere at commit `a11e719b61c4be07fae4e2dcfa4d88d31812d0d9`). The latest r25 three-volume gate is inapplicable to the rank-two stress matrix below because its physical `E_3` is exactly zero; the partner-checked ridge gate is applied below as an exact obstruction calculation.

Corrections preserved: law-uniform pointwise scalar quadratic-phase decay is false; spectral rotation does not preserve input independence; arbitrary-joint rank-three coarea and positive conditional projection-cap moments are false; naive fiber suprema can lose dimension; no uniformly good local minor, single Schur rank-two extraction, or rank-three physical cross cut follows from the target spectrum alone. None is used.

## 3. New theorem: arbitrary-weight rank-two half-Riesz

Let `I,J` be disjoint sets of ORIGINAL independent coordinates. After conditioning any other original coordinates, write the active quadratic-plus-affine polynomial as

`R=F(X_I)+2 X_I^T M X_J+G(X_J)`,

where `F,G` may contain arbitrary within-bank quadratic and affine terms. Let `w_{S,T}` be any probability law supported on nonzero physical `2x2` minors `M_{S,T}`. Define

`alpha_i=P_w(i in S)`, `beta_j=P_w(j in T)`,

and the entropy-adjusted two-volume

`G_2(w)=exp( sum_{S,T} w_{S,T} log det(M_{S,T})^2 + H(w) )`.      (3.1)

### Theorem `QFORM-ENTROPY-WEIGHTED-RANK2-HALFRIESZ-v1`

If `1<=q<2` and

`max_i alpha_i <= q/2`,                                            (3.2)

then

`boxed:
 sup_s E|R-s|^(-1/2)
 <= [4 sqrt(2e) q^(-1/4)/(2-q)] G_2(w)^(-1/8).`                  (3.3)

Consequently, if `Z` is one further untouched original coordinate, independent of the residual bank and of density cap one, then for every `a!=0` and arbitrary measurable shift `m` depending on the residual variables,

`Q=a[Z+m]^2+R`

satisfies

`boxed:
 ||p_Q||_infinity
 <= [4 sqrt(2e) q^(-1/4)/(2-q)]
    |a|^(-1/2) G_2(w)^(-1/8).`                                  (3.4)

The conclusion is essential boundedness / absolute continuity; continuity is not asserted here.

### Proof

The e5 decoupling step gives, with an independent copy on the `J` bank and `D=X_J-X_J'`,

`|phi_R(t)|^2 <= E_D prod_i |psi_i(2t(MD)_i)|`.                  (3.5)

For `q>=1`, raise the product to `q` and use Jensen. The Brascamp--Lieb datum has row exponents `alpha_i` and coordinate exponents `1-beta_j`. For positive Gaussian parameters, the diagonal-plus-PSD determinant expansion gives

`det(D_J+M^T D_I M)
 >= sum_{|S|=|T|=2} det(M_ST)^2 prod_{i in S} d_i prod_{j notin T} e_j.`  (3.6)

Apply weighted AM-GM using the *arbitrary* probability weight `w`:

`sum x_ST >= prod (x_ST/w_ST)^(w_ST)
 = G_2(w) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j).`           (3.7)

Thus the Gaussian BL constant is bounded by

`G_2(w)^(-1/2)
 prod_i alpha_i^(-alpha_i/2)
 prod_j (1-beta_j)^(-(1-beta_j)/2).`                             (3.8)

This is exactly the arbitrary-weight version of the completed e5 determinant step, now at `k=2`.

The sharp Hausdorff--Young row estimate in the completed rank-two fractional compiler applies because `q/alpha_i>=2`. The row-marginal factors cancel (3.8), while the row and column entropy factors contribute at most `e^2`. Since `sum alpha_i=2`, one obtains

`E F_t^q <= e^2 q^(-1) (pi/|t|)^2 G_2(w)^(-1/2)`,               (3.9)

and hence

`|phi_R(t)|
 <= min{1,
 [e^2 q^(-1) pi^2 G_2(w)^(-1/2)]^(1/(2q)) |t|^(-1/q)}.`        (3.10)

The exponent `1/q` is strictly larger than `1/2` because `q<2`. Integrating the half-Riesz time weight exactly as in the completed fractional compiler gives (3.3):

`H_{1/2}(R)
 <= 4 sqrt(2e) q^(-1/4)(2-q)^(-1) G_2(w)^(-1/8).`

Finally the dependence-safe scalar-square peel gives

`p_Q(t)<=|a|^(-1/2) E|t-R|^(-1/2)`

uniformly in the random shift `m`, proving (3.4). No rotated random coordinate is declared independent and no one-dimensional pointwise Fresnel bound is used. QED.

## 4. Exact global entropy optimization on a concentrated physical rank-two packet

Let `theta=pi/8` and let

`V=[[cos theta,-sin theta],[sin theta,cos theta]]`.

In four ORIGINAL left coordinates and two ORIGINAL right coordinates define the physical cross block

`M=R V`,

where the rows of `R` are

`r1=8 e1`,
`r2=e2`,
`r3=(e1+e2)/sqrt(2)`,
`r4=(e1-e2)/sqrt(2)`.                                           (4.1)

The fixed coefficient rotation `V` is part of the matrix, not a change of random variables. Every physical entry of `M` is nonzero. Right multiplication by `V` preserves singular values and absolute minors.

The six squared physical `2x2` minors, indexed by left-row pairs, are

`d12^2=64`, `d13^2=d14^2=32`,
`d23^2=d24^2=1/2`, `d34^2=1`,                                  (4.2)

so

`Z_2=e_2(M^T M)=130`.                                           (4.3)

The canonical squared-minor law has row-one marginal

`p=alpha_1=64/65`,                                               (4.4)

row-two marginal `1/2`, and rows three/four marginal `67/260`. Thus the canonical law is almost a row coloop and at its first admissible exponent `q=128/65` the fractional constant is already near its logarithmic endpoint.

### Exact optimization over all admissible weights for fixed q

For any minor weight,

`log G_2(w)=log 130-KL(w||w_vol)`.                               (4.5)

Put `c=q/2`. For `1<=q<=128/65`, the KL-minimizing law under all constraints `alpha_i<=c` is the I-projection obtained by imposing `alpha_1=c` and preserving the canonical conditional proportions among row-one and non-row-one edges:

`w12=c/2`,
`w13=w14=c/4`,
`w23=w24=(1-c)/4`,
`w34=(1-c)/2`.                                                   (4.6)

Indeed its other row marginals are

`alpha_2=1/2`,
`alpha_3=alpha_4=3/4-c/2`,                                      (4.7)

which are at most `c` for every `c>=1/2`. The KL chain rule then proves global optimality, with

`KL_min(q)=D_Ber(q/2 || 64/65)`,

`G_opt(q)=130 exp[-D_Ber(q/2 || 64/65)].`                        (4.8)

For `q>=128/65` the canonical law itself is admissible and maximizes `G`, so `G_opt(q)=130`.

The full certificate to minimize is therefore

`B(q)=4 sqrt(2e) q^(-1/4)(2-q)^(-1) G_opt(q)^(-1/8).`           (4.9)

For `1<=q<=128/65`, differentiating gives

`d/dq log B
 = -1/(4q)+1/(2-q)
   +(1/16) log[ q(1-p)/((2-q)p) ], p=64/65.`                    (4.10)

Its derivative is strictly increasing because

`d^2/dq^2 log B
 =1/(4q^2)+1/(2-q)^2
  +(1/16)[1/q+1/(2-q)]>0.`                                      (4.11)

At `q=1`,

`d/dq log B
 =3/4-(3/8)log 2
 =0.4900698072...>0.`                                           (4.12)

Hence `B(q)` is strictly increasing throughout this interval. Above `128/65`, `G` is constant and the elementary prefactor is also increasing. Therefore the **global optimum over all admissible minor weights and all `1<=q<2` is q=1**.

At `q=1` the unique optimum is

`w12=w34=1/4`,
`w13=w14=w23=w24=1/8`,                                         (4.13)

all four row marginals equal `1/2`, and

`boxed: G_2,opt=32.`                                             (4.14)

This is an exact entropy repair of an almost-coloop canonical volume law.

## 5. Genuinely rotated indefinite target form and explicit bound

Let `Z,X_1,...,X_4,Y_1,Y_2` be arbitrary independent real random variables with probability densities at most one, and set

`Q_*=Z^2+2 X^T M Y`,                                             (5.1)

with the physical `M` from Section 4. Its symmetric matrix is

`A_*= [1] direct_sum [[0,M],[M^T,0]].`

Since

`M^T M` has eigenvalues `65` and `2`,                            (5.2)

the exact spectrum of `A_*` is

`{1, sqrt(65), -sqrt(65), sqrt(2), -sqrt(2), 0, 0}.`            (5.3)

Thus `A_*` is genuinely rotated, indefinite, and has five eigenvalues of modulus at least one. All eight physical cross coefficients are nonzero.

Applying Theorem 3 with `a=1`, `q=1`, and the globally optimal weight (4.13) gives, for **every** admissible product input law,

`boxed:
 ||p_(Q_*)||_infinity
 <= 4 sqrt(2e) 32^(-1/8)
 =2^(15/8) sqrt(e)
 =6.047536285398243... .`                                       (5.4)

For comparison, keeping the unmodified canonical two-volume law forces `q=128/65` and gives the much worse certified bound

`139.24785655729167...`.                                        (5.5)

So the entropy optimization is not cosmetic: it removes the near-logarithmic endpoint loss on this same physical matrix.

## 6. Partner-checked ridge mechanism applied to the same obstruction

The latest account03/B04 r25 three-volume gate has no input here because `rank(M)=2` and `E_3(M^T M)=0`. More significantly, the partner-checked ridge family fails on the same target matrix for **every** regularization scale.

Write `g=gamma^2`. The left ridge matrix

`K_gamma=MM^T(gamma^2 I+MM^T)^(-1)`

has maximum physical diagonal

`k_1=64/(65+g)`,                                                 (6.1)

and effective dimension

`Theta=65/(65+g)+2/(2+g)`.                                      (6.2)

The square-assisted ridge theorem needs some `1<=q<=2` with

`max diag K_gamma<=q/2`, `Theta>4q/3`.                           (6.3)

If `k_1<=1/2`, then `g>=63` and

`Theta<=65/128+2/65=0.5385817307...<4/3`,                       (6.4)

so (6.3) fails.

If `k_1>1/2`, every admissible `q` satisfies `q>=2k_1`. But

`Theta/k_1
 =65/64 +(65+g)/(32(2+g))
 <=65/32
 =2.03125
 <8/3.`                                                         (6.5)

Therefore

`Theta < (8/3)k_1 <=4q/3`,                                      (6.6)

again contradicting (6.3). Thus **no square-assisted ridge certificate exists at any `gamma,q`**. The direct partner-reviewed ridge density criterion requires the stronger `Theta>2q`, so it fails a fortiori.

This is the requested same-matrix mechanism comparison: optimized admissible physical-minor weights give the explicit universal bound (5.4), while the current ridge family has no admissible certificate at all. The obstruction is high physical ridge leverage concentrated in one row, not weak spectral scale.

The calculation also explains why the latest partner r25 spectral-commuting third-volume theorem and the present result are complementary rather than competing: r25 pays sufficiently spread *three-volume* tails, while (3.4) can pay an exact rank-two packet by deliberately redistributing two-volume weight away from a near-coloop row.

## 7. What changed in the proof map

The previous B04 frontier treated high marginal / near-coloop geometry mainly through ridge regularization or physical rank-two excision. The new theorem shows that a third option exists before a hub reduction: **entropy reweight the physical two-minor support**. A canonical volume law may have marginal arbitrarily close to one even though its support contains a perfectly balanced fractional matching whose entropy-adjusted volume is quantitatively large.

For this stress matrix the canonical marginal is `64/65`, yet the balanced law has `G_2=32` and gives density below `6.048`. Conversely, the partner-checked ridge gate fails at every scale. Therefore a future structural compiler should inspect the support/entropy geometry of physical `2x2` minors before declaring a concentrated canonical volume law to be an unavoidable hub.

What remains unpaid is quantitative and structural: under only `s_3(A)>=1`, prove that every low-cross-rank survivor either exposes such a balanced two-minor law with `G_2` at target scale or has a genuine support deficiency (fractional-matching obstruction) that yields an original-coordinate hub/coloop packet already controlled by a completed grouped mechanism. No assertion of such an exhaustive split is made here.

## 8. Verification scope

A deterministic check file records the physical matrix entries, singular values, six squared minors, canonical marginals, optimized weights, `G_2=32`, the two density constants, and the ridge inequalities. Those checks support arithmetic only; the proof is Sections 3-6.

No literature novelty claim is made. No public release, scheduler mutation, notification, email, cross-account authentication, paid call, installation, FEI or benchmark work is involved.
