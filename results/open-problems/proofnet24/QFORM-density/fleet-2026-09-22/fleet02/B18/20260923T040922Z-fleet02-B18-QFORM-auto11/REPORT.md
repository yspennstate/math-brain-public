SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-23T04:09:22Z.
attacking: literature-to-proof transfer for the non-separated Schur-isotropic large-shear survivor, with the one-sheet half paid and the N3 geometry made explicit.

# fleet02/B18 auto11 — one-sheet closure and N3 diffuse-star obstruction for non-separated isotropic shear

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_REDUCTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication and source discipline

The full target remains: for arbitrary independent original-coordinate real random variables with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, iid, Gaussian, or post-rotation-independence assumption is permitted.

This run attacks the first local debt left by the completed designated partner fleet03/B18 report `QFORM-ISOTROPIC-SHEAR-SOURCE-SEPARATED-v1`: the **non-separated** large-shear Schur-isotropic exact-rank-three branch. I apply two source-valid inputs at actual equations:

1. the completed e5f-source ruled-surface theorem (`COUNTEREXAMPLE_SEARCH.md`, Theorem C), which pays the one-sheet side of a rank-three `(2,1)` quadratic form using only a two-dimensional product marginal cap;
2. the fleet03/B18 deterministic shear ledger, which forces `k>=1` and identifies the physical hub couplings in the isotropic basis.

The only external theorem needed by the ruled-surface proof is verified directly from the primary paper:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, Theorem 1.1, arXiv:1507.07949. If `f(x)=prod_i f_i(x_i)` is a product probability density and every `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal is bounded by `2^(k/2)`; in particular every two-dimensional orthogonal marginal is bounded by `2`. The theorem imposes no moments, bounded support, log-concavity, smoothness, or iid assumption. I do **not** infer independence among projected coordinates.

The live corrections `QFORM-TWOSHEET-XRAY-ONLY-FALSE` and `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` are binding below: a two-dimensional marginal/X-ray cap pays the ruled one-sheet geometry but cannot simply be reused as a conditional-independence substitute on the two-sheet side.

## 2. Canonical non-separated isotropic shear

Use the completed fleet03/B18 canonical representation

`Q=(Y+u X_0)^T D (Y+u X_0)`,                                  (2.1)

where `X_0` is one original coordinate, independent of the residual original-coordinate product vector `X_R`, `Y=V^T X_R`, `V^T V=I_3`, `D=D^T` is nonsingular, and

`u^T D u=0`.                                                     (2.2)

Write `r=||u||>0`, `n=u/r`, `kappa=||Dn||`, and choose an orthonormal coefficient-space basis `(n,e_2,e_3)` with `e_2=Dn/kappa`. Then

`D=[[0,kappa,0],[kappa,a,b],[0,b,c]]`.                          (2.3)

The partner ledger proves that the three nonzero physical eigenvalues of `A` equal those of

`B=(I+uu^T)^(1/2) D (I+uu^T)^(1/2)
   =[[0,k,0],[k,a,b],[0,b,c]],`                                 (2.4)

where

`k=sqrt(1+r^2) kappa`.                                          (2.5)

If the three nonzero eigenvalues all have modulus at least one, then

`k>=1`,                                                         (2.6)

and also `|c|>=1`. These facts use only the physical spectral normalization, not product-law assumptions.

Because `D` is nonsingular and has the nonzero isotropic vector `u`, it is indefinite. Since `L=[u,V^T]` has full row rank and `LL^T=I+uu^T>0`, the nonzero inertia of `A=L^T D L` equals the inertia of `(LL^T)^(1/2)D(LL^T)^(1/2)`. Hence `A` has signature `(2,1)` or `(1,2)` on its range.

## 3. New reduction: the whole one-sheet half-line is already paid

### Theorem `QFORM-ISOTROPIC-SHEAR-ONESHEET-v1`

Assume (2.1)--(2.2), exact rank three, and all three nonzero eigenvalues of `A` have modulus at least one. No source-separation assumption is made. Choose `sigma in {+1,-1}` so that `sigma A` has two positive and one negative nonzero eigenvalues. Then the output density satisfies

`boxed: p_Q(t) <= pi sqrt(2)  for a.e. t with sigma t >=0.`       (3.1)

No continuity claim is needed for this reduction.

### Proof

Write the nonzero eigenvalues of `sigma A` as `lambda_1,lambda_2,-mu`, with all three positive magnitudes at least one. The completed e5f-source ruled theorem applies directly to the **actual physical product input** and gives for every `s>=0`

`p_(sigma Q)(s)
 <= (lambda_1 lambda_2 mu)^(-1/2)
    integral_0^(2pi)
      [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2)
      dtheta
 <= pi sqrt(2).`                                                (3.2)

The geometric proof uses line rulings of the one-sheet hyperboloid and only the two-dimensional orthogonal-marginal cap `2`; that cap is exactly the primary LPP theorem above. Since `p_(sigma Q)(s)=p_Q(sigma s)`, (3.1) follows. QED.

**Consequence.** The non-separated large-shear debt is not a full-line problem. Any remaining blow-up must occur on the **minority-sign / two-sheet half-line**. This is a real narrowing of the fleet03/B18 r22 gap, and it uses the required e5f completed result at the target density inequality itself.

## 4. New N3 implication: a Schur-isotropic survivor must have a diffuse physical star

Now impose the no-pivot pair condition at some threshold `tau in (0,1]`:

`|A_ii A_jj-A_ij^2| < tau` for every physical pair `i!=j`.       (4.1)

The diagonal part of N3 is not needed for the following lemma.

Let `v_j in R^3` be the `j`-th residual row of `V`, and put

`q_j=<v_j,e_2>`.                                                  (4.2)

Because `V^T V=I_3`,

`sum_j q_j^2=1`.                                                  (4.3)

The physical hub coordinate is `0`. From (2.2), `A_00=0`, while from (2.3)

`A_0j=u^T D v_j=r kappa q_j`.                                   (4.4)

Therefore its two-coordinate principal determinant is exactly

`det A[{0,j}] = -A_0j^2=-(r kappa)^2 q_j^2`.                    (4.5)

Combining (4.1), (4.5), and the partner spectral ledger (2.5)--(2.6), for `r>=1` we obtain

`r kappa = [r/sqrt(1+r^2)] k >= 1/sqrt(2)`,                     (4.6)

so

`boxed: max_j q_j^2 < 2 tau.`                                   (4.7)

Equivalently the shear direction `e_2` is necessarily delocalized across original residual coordinates. In physical coefficients,

`sum_j A_0j^2=(r kappa)^2 >=1/2`,                               (4.8)

while every `|A_0j|<sqrt(tau)`. Hence every N3 Schur-isotropic large-shear survivor carries at least order `tau^(-1)` leaves in its hub star; more precisely the number of nonzero star leaves is strictly larger than `1/(2tau)`.

This is a product-preserving structural statement in the **original coordinates**. No spectral rotation is used to claim independence. It also explains why the already-paid exact source-separated example with one large hub edge is not representative of the N3 survivor: N3 forces that edge mass to fragment.

## 5. Exact target-valid stress family showing the diffuse-star scaling is real

The preceding implication is not vacuous. For every `r>=1` and every Hadamard order `m>=4`, let `V` be the first three normalized columns of a real Walsh--Hadamard matrix of order `m`, so each residual row is

`v_j=(eps_{j1},eps_{j2},eps_{j3})/sqrt(m)`, `eps_{jk} in {+1,-1}`, (5.1)

and `V^T V=I_3`. Put

`s=sqrt(1+r^2)`,
`u=r e_1`,
`D_r=[[0,1/s,0],[1/s,0,0],[0,0,1]]`,                           (5.2)

and set `A=L^T D_r L` with `L=[u,V^T]`. Then

`diag(s,1,1) D_r diag(s,1,1)
  =[[0,1,0],[1,0,0],[0,0,1]],`                                  (5.3)

so the nonzero spectrum of `A` is exactly

`{-1,1,1}`                                                       (5.4)

for every `m` and `r`. Thus this is a genuine target family.

For independent arbitrary cap-one inputs, writing `Y=V^T X_R`, the output is

`Q_{m,r}=2/s (Y_1+rX_0)Y_2 + Y_3^2`.                            (5.5)

The three aggregates `Y_1,Y_2,Y_3` are generally dependent because each uses the same residual original coordinates. Every Hadamard row has all three components nonzero, so no residual row is parallel to `e_1` or orthogonal to `e_1`; the designated partner's exact source-separation hypothesis fails at **every** row.

Nevertheless all physical local pivots become small. Indeed

`A_00=0`,
`|A_0j|=r/(s sqrt(m)) <=1/sqrt(m)`,                              (5.6)

and for residual indices `i,j`,

`A_ij=s^(-1)(v_i1 v_j2+v_i2 v_j1)+v_i3 v_j3`,

so

`|A_ij| <=3/m`, `|A_ii|<=3/m`.                                  (5.7)

Therefore

`|det A[{0,j}]| <=1/m`,                                         (5.8)

and for residual pairs

`|A_ii A_jj-A_ij^2| <=18/m^2`.                                 (5.9)

For every fixed `tau>0`, choosing

`m > max{1/tau, 3/tau, sqrt(18/tau)}`                            (5.10)

puts the family inside the diagonal-and-pair no-pivot class N3 while retaining the exact target spectrum (5.4). Moreover `q_j^2=1/m`, so the diffuse-star estimate (4.7) has the correct `tau`-scale up to constants.

By Theorem 3, **even for this genuinely mixed-source N3 family**,

`p_{Q_{m,r}}(t) <= pi sqrt(2)` for a.e. `t>=0`                  (5.11)

(the sign orientation here is already `(2+,1-)`). Thus any unresolved behavior of this explicit family is confined to `t<0`, the two-sheet side.

## 6. Direct attack on the first remaining implication

The first unpaid local implication is now:

> **`QFORM-N3-DIFFUSE-STAR-TWOSHEET-v1`**: for a target-valid Schur-isotropic form satisfying `r>=1`, the N3 pair bounds, and hence (4.7)--(4.8), prove a universal bound on the minority-sign/two-sheet density, while retaining the original product-linear provenance of `(Z_1,Z_2,Z_3)`.

The obvious shortcut is unavailable. The partner gives a bounded two-dimensional marginal for the transverse pair, but `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` proves that bounded pair density plus bounded conditional scalar density cannot replace genuine scalar/pair independence in a hyperbolic-square kernel. Likewise `QFORM-TWOSHEET-XRAY-ONLY-FALSE` shows that an abstract X-ray cap does not control the two-sheet trace. The new information that those counterexamples do **not** encode is the exact diffuse-star identity

`A_0j=r kappa q_j`, `sum q_j^2=1`, `max q_j^2<2tau`,              (6.1)

coming from the physical no-pivot hypothesis. A viable next transfer must spend this coefficient-level product provenance before conditioning destroys it; the e5f mixed-hub/Fresnel machinery is the natural receiver if the remaining residual curvature can be decomposed into its admissible low-rank-plus-diagonal form, otherwise a new two-sheet product-trace estimate is needed.

I did not promote a conditional-cap argument, an arbitrary-joint coarea inequality, or a post-rotation independence assertion.

## 7. Status and source pins

**Full target change:** `OPEN -> OPEN`.

**Mathematical change:** the non-separated Schur-isotropic large-shear survivor is now split sharply into (i) a completely paid one-sheet half-line with universal constant `pi sqrt(2)`, and (ii) a two-sheet-only debt; inside N3 the latter necessarily has a quantitatively diffuse original-coordinate hub star with `||q||_infinity^2<2tau`. The Hadamard family (5.1)--(5.5) shows that this mixed-source N3 geometry actually occurs and is not removed by the partner's source-separation theorem.

Source pins used:
- required e5f package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `COUNTEREXAMPLE_SEARCH.md` Theorem C;
- completed designated partner: fleet03/B18 `20260923T032156Z-fleet03-B18-QFORM-r22/REPORT.md`, read from current math-open-problems mainline snapshot before this report;
- primary theorem: Livshyts--Paouris--Pivovarov, arXiv:1507.07949v2, Theorem 1.1, DOI 10.1007/s11856-016-1431-5;
- live corrections consumed before publication include `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, and the arbitrary-joint/conditional-moment failures recorded in `CURRENT_RESEARCH.md`.

Independent end-to-end review: **not performed**. This is a supporting reduction, not a claim of the full theorem.
