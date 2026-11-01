# fleet01/B18 r20 — LPP-to-Plancherel full-bank transfer and leverage-collision closure

**Run:** `20260923T002242Z-qform-B18-a01-r20`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / DESIGNATED_PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, source discipline, and what is not claimed

The owner target remains open: for arbitrary finite `n`, independent real original-coordinate random variables `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `Q=X^T A X`; continuity is a separate desired conclusion.

This report proves a new source-valid branch for **exact rank three** and applies it to the designated partner fleet02/B18's only remaining zero-pivot Schur-isotropic core. It does not solve arbitrary extra spectrum and it does not claim the full conjecture.

The proof does not use any of the live false interfaces: no independence after rotation, no arbitrary-joint coarea theorem, no conditional projection-density cap, no positive conditional-density moment, no pointwise law-uniform quadratic-phase decay, no near-zero-as-zero replacement, and no localization to one physical pair before aggregation. The aggregation below occurs first on disjoint original-coordinate banks.


## 2. Primary literature transferred at its exact hypotheses

The external theorem used is:

G. Livshyts, G. Paouris, P. Pivovarov, **On sharp bounds for marginal densities of product measures**, Israel J. Math. 216 (2016), 877–889; arXiv:1507.07949, DOI 10.1007/s11856-016-1431-5.

Their theorem applies exactly to the present source class: if `X=(X_1,...,X_m)` has product density `prod f_i` with every `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. No moments, bounded support, centering, iid assumption, smoothness, symmetry, or log-concavity are needed.

The second analytic input is ordinary Plancherel with Fourier convention

`phat(z)=integral exp(i <z,y>) p(y) dy`,

so

`integral |phat(z)|^2 dz=(2*pi)^k integral |p(y)|^2 dy`.

The transfer below uses LPP to put each **whole original-coordinate bank** in `L^2` before the Fresnel integral is estimated. This is deliberately different from selecting one physical minor and from conditioning on a rotated fiber.

## 3. New theorem: two independent full-rank banks give a continuous target density

Let `L` be a real `3 x n` rank-three coefficient matrix with columns `ell_i`, let `D=D^T` be an invertible `3 x 3` matrix, and put

`A=L^T D L`.

Let `I,J` be disjoint subsets of original coordinate indices. Write

`L_I=(ell_i)_(i in I)`, `L_J=(ell_i)_(i in J)`,

and their bank Gram matrices

`G_I=L_I L_I^T`, `G_J=L_J L_J^T`.

Assume both are positive definite. All coordinates outside `I union J` are allowed and no hypothesis is imposed on their columns.

### Theorem 3.1 — `QFORM-TWO-FULL-BANK-L2-v1`

For arbitrary independent input coordinates with densities bounded by one,

`Q=X^T L^T D L X`

has a bounded continuous density and

`boxed:
 ||p_Q||_infinity
 <= 6 [ |det D| sqrt(det G_I det G_J) ]^(-1/3).`              (3.1)

### Proof

Let

`Y_I=L_I X_I`, `Y_J=L_J X_J`.

The two random vectors are independent because the banks are disjoint original-coordinate sets. Since `G_I>0`, the whitened coefficient map

`S_I=G_I^(-1/2)L_I`

has orthonormal rows. LPP in dimension three therefore gives the density of `G_I^(-1/2)Y_I` the cap `2^(3/2)`. Changing variables yields

`||p_(Y_I)||_infinity <= 2^(3/2) / sqrt(det G_I).`             (3.2)

Since `p_(Y_I)` is a probability density,

`||p_(Y_I)||_2^2 <= ||p_(Y_I)||_infinity`,

and Plancherel gives

`||phat_(Y_I)||_2
 <= (2*pi)^(3/2) 2^(3/4) (det G_I)^(-1/4).`                  (3.3)

The same estimate holds with `I` replaced by `J`.

The exact three-dimensional Fresnel linearisation for `t!=0` gives

`|phi_Q(t)|
 <= (4*pi*|t|)^(-3/2) |det D|^(-1/2)
    integral_(R^3) |phat_(Y_I)(z) phat_(Y_J)(z)| dz,`           (3.4)

because every remaining disjoint original-coordinate factor is a characteristic function of modulus at most one. The harmless signature phase of `D` disappears in absolute value.

Cauchy--Schwarz and (3.3) give

`integral |phat_(Y_I) phat_(Y_J)|
 <= (2*pi)^3 2^(3/2)
    (det G_I det G_J)^(-1/4).`                                  (3.5)

Hence

`|phi_Q(t)|
 <= K |t|^(-3/2),`

where

`K=2^(3/2) pi^(3/2) |det D|^(-1/2)
   (det G_I det G_J)^(-1/4).`                                   (3.6)

Together with `|phi_Q(t)|<=1`,

`integral_R |phi_Q(t)| dt
 <= integral_R min(1,K|t|^(-3/2)) dt
 =6 K^(2/3).`                                                    (3.7)

Fourier inversion therefore gives a continuous representative and

`||p_Q||_infinity
 <= (2*pi)^(-1) 6K^(2/3)
 =6 [|det D| sqrt(det G_I det G_J)]^(-1/3).`

This proves (3.1). QED.

### Scope note

The proof aggregates whole independent physical banks before taking absolute values. It therefore survives `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1`: no single local pair is selected and no local half-Riesz payment is demanded.

## 4. Exact-rank-three normalization

Let

`G=L L^T`.

The nonzero eigenvalues of `A=L^T D L` are those of the symmetric congruence `G^(1/2) D G^(1/2)`, so

`|pdet A|=|det D| det G.`                                        (4.1)

If the three nonzero eigenvalues of `A` have modulus at least one, then `|pdet A|>=1`.

Define the two-bank determinant fraction

`Theta(I,J)= sqrt(det G_I det G_J) / det G.`                     (4.2)

Theorem 3.1 immediately becomes the target-normalized certificate

`boxed:
 ||p_Q||_infinity <= 6 Theta(I,J)^(-1/3).`                       (4.3)

Thus any two disjoint full-rank original-coordinate banks carrying a fixed determinant fraction pay the exact-rank-three target with continuity.

This is an aggregate statement: `det G_I` is the Cauchy--Binet sum of the squared determinants of **all** physical bases inside bank `I`. No reciprocal single minor appears.

## 5. New leverage-collision corollary: random partition aggregates all disjoint basis pairs

The preceding theorem can be converted into a basis-free criterion.

Let

`q_S = det(L_S)^2 / det G`                                      (5.1)

for three-element physical bases `S`; Cauchy--Binet says `(q_S)` is a probability distribution. Let `S,T` be independent samples from `q` and write

`p_disj = P(S cap T = emptyset).`                               (5.2)

### Corollary 5.1 — `QFORM-VOLUME-BASIS-COLLISION-v1`

For an exact-rank-three target as above, if `p_disj>0`, then

`boxed:
 ||p_Q||_infinity <= 12 p_disj^(-1/6),`                          (5.3)

and the density is continuous.

#### Proof

Assign every physical column independently to bank `I` or bank `J` with probability `1/2`. Cauchy--Binet gives

`det G_I det G_J
 = sum_(S,T) det(L_S)^2 det(L_T)^2
   1_(S subset I) 1_(T subset J).`

Only disjoint `S,T` can contribute. For a fixed disjoint pair, the probability of the required six assignments is `2^(-6)`. Therefore

`E[det G_I det G_J]
 = 2^(-6) (det G)^2 p_disj.`                                    (5.4)

Some deterministic partition consequently satisfies

`sqrt(det G_I det G_J)/det G >= (1/8) sqrt(p_disj).`             (5.5)

Apply (4.3):

`||p_Q||_infinity
 <= 6 (8/sqrt(p_disj))^(1/3)
 =12 p_disj^(-1/6).`

QED.

### Corollary 5.2 — leverage-square criterion

Let

`lambda_i = ell_i^T G^(-1) ell_i`                               (5.6)

be the leverage scores. Under the volume-sampling law `q`,

`P(i in S)=lambda_i`.                                           (5.7)

For two independent volume bases,

`P(S cap T != emptyset)
 <= sum_i P(i in S and i in T)
 = sum_i lambda_i^2.`                                           (5.8)

Hence if

`sum_i lambda_i^2 <= 1-eta` for some `eta>0`, then

`p_disj >= eta`

and

`boxed:
 ||p_Q||_infinity <= 12 eta^(-1/6).`                            (5.9)

Continuity again follows.

This is genuinely different from the natural-leverage `max lambda_i<=1/2` Fourier gate: (5.9) can allow a physical leverage strictly larger than `1/2`, provided the rest of the determinant mass is sufficiently diffuse.

## 6. Edmonds base-packing transfer: the exact zero-collision obstruction is low-complexity

For completeness, the finite matroid base-packing theorem of Edmonds says that a rank-`r` matroid on ground set `E` has `k` disjoint bases iff

`k(r(E)-r(U)) <= |E\U|` for every `U subset E`.                 (6.1)

Apply it with the rank-three vector matroid of the columns of `L` and `k=2`. If `p_disj=0`, then there are no two disjoint physical bases, so there is a subset `U` for which

`|E\U| < 2(3-r(U)).`                                            (6.2)

Thus one of the following exact vector configurations occurs:

- `r(U)=2` and at most one column lies outside one plane;
- `r(U)=1` and at most three columns lie outside one line;
- `r(U)=0` and at most five nonzero columns exist.

This does **not** solve the quantitative regime `p_disj` small but nonzero. It does show that the zero endpoint of the new criterion is not an amorphous high-dimensional failure: it collapses to a low-complexity vector-matroid obstruction that should be routed to physical-pivot/hub arguments rather than to another diffuse-bank estimate.

## 7. Actual application to designated partner fleet02/B18

The designated partner report is

`yspennstate/math-open-problems@0a28faf7bf87a49a9df787eb276b449aee3d9c47:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260922T221352Z-fleet02-B18-QFORM-r11/REPORT.md`.

It closes two zero-pivot exact-rank-three cases and leaves only the Schur-isotropic case

`Q=(Y+u X_0)^T D (Y+u X_0)`,                                   (7.1)

with `X_0` an original scalar independent of the residual original coordinates and `Y=V^T X_res`, where

`V^T V=I_3`,

`L=[u,V^T]`,

`L L^T=I+uu^T`,

`pdet(A)=det(D)(1+||u||^2)`,                                   (7.2)

and the zero-pivot isotropy is `u^T D u=0`.

This is exactly a factorization to which Theorem 3.1 and Corollary 5.2 apply. Let `lambda_i` be the leverage scores of the physical columns of this **exact partner map** `L`. If

`sum_i lambda_i^2 <=1-eta`,                                    (7.3)

then, because the partner target has `|pdet(A)|>=1`,

`boxed:
 ||p_Q||_infinity <=12 eta^(-1/6),`                             (7.4)

and `p_Q` is continuous.

This closes a concrete portion of the partner's only remaining zero-pivot case and does so while permitting a high-leverage zero-diagonal physical coordinate. It is an actual use of the partner factorization/pseudodeterminant ledger, not a citation-only reference.

## 8. Explicit high-leverage Schur-isotropic family paid by the new branch

The leverage-square condition is nonempty beyond the old natural-leverage gate.

Let `e_1,e_2,e_3` be the standard basis of `R^3`, put

`u=2e_1`, `G=I+uu^T=diag(5,1,1)`,                              (8.1)

and

`B=[[0,1,0],[1,0,0],[0,0,1]]`,

`D=G^(-1/2) B G^(-1/2)
  =[[0,1/sqrt(5),0],[1/sqrt(5),0,0],[0,0,1]].`                 (8.2)

Then `u^T D u=0`, `det D=-1/5`, and the nonzero eigenvalues of `A=L^T D L` are exactly the eigenvalues of

`G^(1/2) D G^(1/2)=B`,

namely `{-1,1,1}`. Hence this is a target-valid Schur-isotropic zero-pivot family.

For an integer `m>=1`, realize the residual Parseval frame `V` by two disjoint banks, each containing `m` copies of each vector

`e_j/sqrt(2m)`, `j=1,2,3`.                                     (8.3)

Each residual bank has Gram matrix `I/2`, while the full residual frame has Gram `I` as required by (7.2).

The special physical coordinate has leverage

`lambda_0=u^T G^(-1)u=4/5>1/2`,                                (8.4)

so the natural-leverage `<=1/2` gate fails.

Nevertheless the two residual banks in (8.3), with the special column adjoined to either one of them, give

`det G_I=det(uu^T+I/2)=9/8`,

`det G_J=det(I/2)=1/8`,

`sqrt(det G_I det G_J)=3/8`.                                   (8.5)

Since `|det D|=1/5`, Theorem 3.1 gives the uniform all-law bound

`boxed:
 ||p_Q||_infinity
 <= 6 (40/3)^(1/3)
 =14.227573217960252...`                                        (8.6)

for every `m`, with continuity.

Thus a physical zero-pivot direction may carry leverage `4/5`, beyond the natural cap, while diffuse original-coordinate banks still pay the quadratic trace without selecting one tiny basis determinant.

For reference, the leverage-square sum in this family is

`sum_i lambda_i^2
 =16/25 + 51/(50m).`                                             (8.7)

Hence the basis-collision corollary alone already supplies a dimension-free bound for every `m>=3`; the explicit bank partition (8.5) is sharper and works for all `m`.

## 9. Relation to the previous fleet01/B18 capped-basis theorem

The previous r19 theorem (`QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`) used Beckner plus rank-one Brascamp--Lieb with a capped distribution over physical three-column bases. The present theorem uses a different literature transfer: LPP is first applied to whole physical banks, and Plancherel/Cauchy--Schwarz is then performed at bank level.

A two-bank decomposition can be encoded into a capped basis distribution by half-mixing the volume-sampling laws of the two banks, so the scopes are related. The present result nevertheless supplies:

1. the clean aggregate formula (3.1) directly in terms of bank Gram determinants;
2. the sharper constant `6` for this `L^2 x L^2` specialization;
3. the random-partition identity (5.4), which converts the problem to the collision probability of two volume-sampled bases;
4. the leverage-square sufficient condition (5.9), which allows individual leverage greater than one half;
5. the exact Edmonds description of the `p_disj=0` endpoint.

No claim of literature novelty is made; these are source-valid deductions assembled for the owner target.

## 10. Literature audit: no exact prior full-target solution identified

The source search again found the LPP theorem, which matches the marginal step exactly. General polynomial anti-concentration papers such as Meka--Nguyen--Vu do not, from their stated hypotheses/conclusions, supply the required `O(epsilon)` concentration uniformly for the present arbitrary cap-one continuous product class and arbitrary rotated quadratic form. Recent polynomial-image regularity results located in the search impose additional moment/regularity assumptions. None was used as a substitute for the missing owner implication.

A search miss is not novelty evidence and is not recorded as such.

## 11. Fresh correction audit and first unpaid implication

The live correction set was re-read before publication. In particular the argument is compatible with:

- `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`;
- `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`;
- `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`;
- `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`;
- `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`;
- `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`;
- `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`;
- the newer `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1` source event observed on fresh main.

The reason is structural: all aggregation is over disjoint original-coordinate banks **before** the Fourier absolute value; no rotated conditional law is assigned a fictitious cap or independence property.

The exact unpaid implication after this run is quantitative, not qualitative:

> In the partner Schur-isotropic projected-product core, control the regime in which two independent volume-sampled physical bases have very small disjointness probability (`p_disj ->0`), equivalently highly concentrated determinant mass. Either route that concentration to an already-paid physical-pivot/hub branch with a uniform quantitative threshold, or develop a collision/oscillatory mechanism that spends the high-leverage isotropic coordinate without requiring a second disjoint full-rank bank.

At `p_disj=0`, Edmonds reduces the vector geometry to the low-complexity cases in Section 6. The hard gap is a **uniform quantitative interpolation** between that degenerate endpoint and the bank-diffuse branch proved here.

## 12. Exact source pins

- Designated partner: `yspennstate/math-open-problems@0a28faf7bf87a49a9df787eb276b449aee3d9c47`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260922T221352Z-fleet02-B18-QFORM-r11/REPORT.md`.
- Prior own capped-basis theorem: `yspennstate/math-open-problems@a9812cdd26a9dd066638b0e6f0dccf3dbdce2ab8`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.
- LPP primary source: arXiv:1507.07949; Israel J. Math. 216 (2016), 877–889; DOI 10.1007/s11856-016-1431-5.
- Matroid base packing theorem: Edmonds' finite matroid base-packing theorem, used only for the exact `p_disj=0` structural endpoint; the inequality is written explicitly in (6.1).

Manual scope review: no credentials, machine-local paths, scheduler identifiers, email addresses, private unrelated data, public release actions, or permission expansions are included.
