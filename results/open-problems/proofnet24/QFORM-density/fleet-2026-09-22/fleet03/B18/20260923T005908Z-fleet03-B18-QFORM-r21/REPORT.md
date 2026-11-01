SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T00:59:08Z.
attacking: extreme-shear and high-row-leverage closure for the exact-rank-three Schur-isotropic branch, using source-valid projection/restricted-invertibility inequalities and fleet04/B18 r3 at an explicit inequality.

# fleet03/B18 r21 — an entropy barrier for capped-basis Fresnel and an aggregate-before-pivot escape

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / MECHANISM_BARRIER / PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction boundary

The target remains: for every finite `n`, independent real original-coordinate variables with probability densities at most one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a dimension- and law-uniform finite essential density bound for `X^T A X`, or give a target-valid counterexample. Continuity is an additional desired conclusion and is recorded separately.

This report uses no moments, support hypotheses, log-concavity, Gaussianity, post-rotation independence, arbitrary-joint coarea estimate, positive conditional projection-density moment, fixed-good-minor extraction, or law-uniform pointwise van-der-Corput estimate. The live correction inbox was consumed before derivation.

The completed designated-partner inputs actually used are:

1. **fleet04/B18 r3**, `QFORM-ISOTROPIC-SHEAR-MIXED-VOLUME-v1`, canonical report `yspennstate/math-open-problems@24a9362bd3f24a3849021093cf98611f95b5ab04:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260923T001857Z-fleet04-B18-QFORM-r3/REPORT.md`. In the Schur-isotropic shear factorization

   `Q=(Y+u X_0)^T D (Y+u X_0)`, `Y=V^T X'`, `V^T V=I_3`, `u^T D u=0`,

   write `r=||u||`, `n=u/r`, `p_j=||v_j||^2`, and `q_j=||(I-nn^T)v_j||^2`. If `p_j+q_j<=1` for every residual row, its half residual-three-volume / half shear-two-volume basis distribution satisfies the capped-marginal Fresnel theorem and gives

   `||p_Q||_infinity <= 3e (2r |det D|)^(-1/3)`,

   with a continuous density.

2. **fleet04/B18 r2**, canonical report `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061:proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`. If a cap-one scalar `X` is independent of two normalized linear banks `U=<u,X_I>`, `V=<v,X_J>` on disjoint original-coordinate blocks, and `K` is a nonsingular symmetric zero-pivot `3x3` matrix, then

   `||p_((X,U,V)^T K (X,U,V))||_infinity
      <= 6 [R(u)R(v)]^(2/3) |det K|^(-1/3)`,

   and the density is continuous. Here `R(.)` is the sharp centered-uniform comparator maximum density from Juškevičius--Lee.

The source-pinned capped-basis theorem used to audit r3 is fleet01/B18 r19, `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, whose primary analytic inputs are Beckner's sharp Hausdorff--Young inequality (Ann. Math. 102 (1975), DOI 10.2307/1970980) and Lieb's Gaussian exhaustion for Brascamp--Lieb in the Bennett--Carbery--Christ--Tao formulation (arXiv:math/0505065). It states that for `A=L^T D L`, rank `L=3`, any probability law `w` on nonsingular three-column bases with coordinate marginals at most `1/2` gives

`||p_Q||_infinity <=3 B_alpha^(2/3)(|det D| Z_w)^(-1/3)
                    <=3e(|det D|Z_w)^(-1/3)`,

where

`Z_w=exp(H(w)+sum_S w_S log det(L_S)^2)`.

The primary maximum-density source transferred in r2 is T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190. Its one-dimensional sharp Rogozin consequence compares a sum of independent bounded-density variables to centered uniform summands with the same individual density caps. Livshyts--Paouris--Pivovarov, arXiv:1507.07949, independently gives the general normalized one-dimensional product-marginal cap `sqrt(2)`.

## 2. Exact entropy ceiling for every capped-basis distribution on a one-shear frame

Consider the coefficient frame

`L=[u,v_1,...,v_m]`, `V^T V=I_3`, `u=r n`, `||n||=1`, `r>0`.

There are exactly two types of three-column bases:

- residual triples `S` not containing the shear column `0`;
- shear bases `{0,j,k}` containing it.

Put `d_S=det(L_S)^2`. By Cauchy--Binet,

`sum_(S not containing 0) d_S = det(V^T V)=1`,              (2.1)

and, projecting the residual frame to `n^perp`,

`sum_(j<k) d_{0jk}=r^2`.                                    (2.2)

The second identity can also be read by subtracting (2.1) from

`sum_(all bases S) d_S=det(LL^T)=det(I+uu^T)=1+r^2`.

Let `w` be **any** probability distribution on nonsingular bases and let

`beta=sum_(bases containing 0) w_S`.

Its shear-coordinate marginal is exactly `beta`. Hence every distribution admissible for the capped-basis theorem has

`0<=beta<=1/2`.                                               (2.3)

### Theorem 2.1 — `QFORM-ONE-SHEAR-CAPPED-ENTROPY-BARRIER-v1`

For every such `w`,

`Z_w <= exp(h(beta)) r^(2 beta)`,                             (2.4)

where `h(beta)=-beta log beta-(1-beta)log(1-beta)`. Consequently

`boxed:
 max_(w: alpha_i<=1/2) Z_w
 <= { 1+r^2,  0<r<=1;
      2r,       r>=1. }`                                     (2.5)

For `r>=1`, if the fleet04/B18 r3 condition `p_j+q_j<=1` holds, its half/half mixed-volume law attains the upper bound `Z_w=2r`. Thus **r3 is globally score-optimal among every capped-basis distribution, not merely among the particular two volume laws that motivated its construction.**

#### Proof

Write `B_0` for residual bases and `B_1` for shear bases. For a group `B_g`, let its total probability mass be `m_g` and its total determinant-square mass be `D_g`. The log-sum/Kullback--Leibler inequality gives

`sum_(S in B_g) w_S log(d_S/w_S)
 <= m_g log(D_g/m_g)`.                                      (2.6)

Indeed, after normalizing `w_S/m_g` and `d_S/D_g`, the difference between the right and left sides is `m_g` times a KL divergence.

Here `(m_0,m_1)=(1-beta,beta)` and `(D_0,D_1)=(1,r^2)` by (2.1)--(2.2). Since

`log Z_w=sum_S w_S log(d_S/w_S)`,

(2.6) yields

`log Z_w <=(1-beta)log(1/(1-beta))+beta log(r^2/beta)
          =h(beta)+2 beta log r`,                            (2.7)

proving (2.4).

The derivative of the right side of (2.7) is

`log( r^2(1-beta)/beta )`.

The unconstrained maximizer is

`beta_*=r^2/(1+r^2)`.                                       (2.8)

If `r<=1`, then `beta_*<=1/2` and substitution gives `Z<=1+r^2`. If `r>=1`, the cap (2.3) forces the maximum to the endpoint `beta=1/2`, giving `Z<=2r`. This proves (2.5).

For the r3 mixed-volume law, `beta=1/2`; inside each group the weights are proportional to the determinant squares, so equality holds in both KL inequalities (2.6). Its residual-coordinate marginals are `(p_j+q_j)/2<=1/2`, hence it is admissible and `Z=2r`. QED.

### Consequence 2.2 — what reweighting can and cannot fix

For `0<r<=1`, the full volume-sampling law has `beta=beta_*` and score `1+r^2`. Its residual-coordinate marginals are

`alpha_j=(p_j+r^2 q_j)/(1+r^2)`,                             (2.9)

while `alpha_0=r^2/(1+r^2)`. Thus whenever these marginals are at most `1/2`, the capped-basis theorem yields

`||p_Q||_infinity
 <=3e (|det D|(1+r^2))^(-1/3).`                             (2.10)

For an exact-rank-three target, `|det D|(1+r^2)=|pdet A|>=1`, so this branch is uniformly bounded by `3e` and continuous.

For `r>=1`, however, no rearrangement of basis weights within the same capped-basis Fresnel theorem can produce a score larger than `2r`. Therefore an extreme-shear target family with `|det D|` of order `r^-2` necessarily makes every bound whose only geometric currency is `|det D|Z_w` deteriorate like `r^(1/3)`. The next section gives an exact target family realizing this situation and then closes it by changing analytic mechanism.

## 3. A target-valid extreme-shear family where the capped-basis score is provably insufficient

Let `X_0,...,X_9` be arbitrary independent real random variables, each with a probability density bounded by one. Form three disjoint flat three-coordinate banks

`Y_1=(X_1+X_2+X_3)/sqrt(3)`,
`Y_2=(X_4+X_5+X_6)/sqrt(3)`,
`Y_3=(X_7+X_8+X_9)/sqrt(3)`.

For `r>0` put `s=sqrt(1+r^2)` and

`S_r=(r X_0+Y_1)/s`,
`Q_r=2 S_r Y_2+Y_3^2`.                                     (3.1)

This is a genuine quadratic form in the ten original independent coordinates.

To match the r3 shear notation, use

`u=r e_1`,

and let the residual frame contain three copies each of

`e_1/sqrt(3)`, `e_2/sqrt(3)`, `e_3/sqrt(3)`.

Then `V^T V=I_3`. With

`D_r=[[0,1/s,0],[1/s,0,0],[0,0,1]]`,                       (3.2)

we have

`Q_r=(Y+uX_0)^T D_r (Y+uX_0)`,
`u^T D_r u=0`,
`|det D_r|=1/(1+r^2)`.                                     (3.3)

Moreover

`G=LL^T=diag(1+r^2,1,1)`,

and

`G^(1/2) D_r G^(1/2)
 =[[0,1,0],[1,0,0],[0,0,1]]`.                              (3.4)

Hence the physical matrix of `Q_r` has exactly three nonzero eigenvalues

`{-1,1,1}`                                                   (3.5)

for **every** `r>0`. It therefore satisfies the owner's exact spectral hypothesis with equality, even as `r` tends to infinity.

For the three `e_1` residual rows, `(p_j,q_j)=(1/3,0)`. For each of the six transverse rows, `(p_j,q_j)=(1/3,1/3)`. Thus

`p_j+q_j<=2/3<1`                                             (3.6)

for all residual coordinates, and fleet04/B18 r3 applies for every `r`:

`||p_(Q_r)||_infinity
 <=3e ((1+r^2)/(2r))^(1/3).`                                (3.7)

By Theorem 2.1, for `r>=1` the r3 score `Z=2r` is already the **largest possible score of any capped-basis distribution**. Since `|det D_r|=1/(1+r^2)`, every certificate using only the fleet01/B18 quantity `|det D|Z_w` has

`|det D_r|Z_w <=2r/(1+r^2)`,                                (3.8)

which tends to zero. In particular, even the optimistic version of that certificate with the Hausdorff--Young factor replaced by its lower floor `B_alpha>=1` cannot give a uniform constant from this currency alone: its numerical expression is at least

`3 ((1+r^2)/(2r))^(1/3) -> infinity`.                        (3.9)

Equation (3.9) is a **mechanism barrier**, not a lower bound on the true density. The next argument shows the actual density is uniformly bounded.

## 4. Aggregate before pivot: the same extreme-shear family has a uniform continuous density bound

The source-valid escape is to combine the shear coordinate with the collinear residual bank **before** paying the nonlinear zero-pivot determinant.

### Lemma 4.1 — maximum densities of the three flat banks

Juškevičius--Lee's sharp rearrangement theorem applies because each bank is a sum of genuinely independent original-coordinate variables. For

`a=(1,1,1)/sqrt(3)`,

its centered-uniform comparator has maximum density

`R(a)=3sqrt(3)/4`.                                          (4.1)

This is the exact calculation already source-checked in fleet04/B18 r2: the density of the sum of three unit uniforms at zero is `3/4`, and scaling by `1/sqrt(3)` multiplies the peak by `sqrt(3)`.

Thus

`||p_(Y_2)||_infinity, ||p_(Y_3)||_infinity
 <= R_0:=3sqrt(3)/4`.                                       (4.2)

For `r>=1`, the summand `rX_0/s` alone has density cap `s/r`; convolution with the independent `Y_1/s` cannot raise an `L^infinity` norm. Hence

`||p_(S_r)||_infinity <= L_r:=s/r=sqrt(1+r^(-2))<=sqrt(2)`. (4.3)

This uses only Young's elementary `L^infinity*L^1` contraction. No moment or support condition is present.

### Theorem 4.2 — `QFORM-EXTREME-SHEAR-AGGREGATE-PIVOT-v1`

For every `r>=1`, every admissible product input in (3.1) gives a **continuous** density satisfying

`boxed:
 ||p_(Q_r)||_infinity
 <=6 (27/16)^(2/3) ((1+r^2)/r^2)^(1/3)
 <=27/2^(4/3)
 =10.714957100785... .`                                     (4.4)

As `r->infinity`, the displayed bound improves to

`27/2^(5/3)=8.50446708679...`.                               (4.5)

#### Proof — actual use of fleet04/B18 r2

The aggregate `S_r` depends only on the original-coordinate block `{0,1,2,3}`. The banks `Y_2` and `Y_3` use disjoint blocks `{4,5,6}` and `{7,8,9}`. Therefore `S_r` is genuinely independent of the pair `(Y_2,Y_3)`; this is original-coordinate independence, not independence after rotation.

Let

`X=L_r S_r`.

By (4.3), `X` has density at most one. Equation (3.1) becomes

`Q_r=2 L_r^(-1) X Y_2+Y_3^2`.

In variables `(X,Y_2,Y_3)` the symmetric zero-pivot coefficient matrix is

`K_r=[[0,L_r^(-1),0],
      [L_r^(-1),0,0],
      [0,0,1]]`,

so

`|det K_r|=L_r^(-2)`.                                       (4.6)

Now apply fleet04/B18 r2 exactly at its proved hypotheses, with the two normalized banks having sharp rearrangement factors `R_0,R_0`. Its inequality gives

`||p_(Q_r)||_infinity
 <=6 (R_0^2)^(2/3) |det K_r|^(-1/3)
 =6 (27/16)^(2/3) L_r^(2/3)`.                               (4.7)

Substitute `L_r^2=(1+r^2)/r^2`. For `r>=1`, `L_r^2<=2`; hence

`6 (27/16)^(2/3) 2^(1/3)
 =27/2^(4/3)`,

which proves (4.4). The r2 theorem supplies continuity. QED.

### Small-shear completion of the same family

For `0<r<=1`, the full volume-sampling law is admissible. Indeed its shear marginal is `r^2/(1+r^2)<=1/2`; each `e_1`-bank coordinate has leverage `1/[3(1+r^2)]`; and each transverse coordinate has leverage exactly `1/3`. Thus (2.10), together with `|det D_r|(1+r^2)=1`, gives

`||p_(Q_r)||_infinity <=3e=8.154845485377...`,              (4.8)

again with continuity.

Combining (4.4) and (4.8), the **entire extreme-shear family** (3.1), for every `r>0`, satisfies the distribution-free continuous-density estimate

`boxed:
 ||p_(Q_r)||_infinity <=27/2^(4/3)<10.715.`                  (4.9)

This is a concrete implication that was not available from the r3 target-normalized bound alone: the family remains controlled uniformly as the shear tends to infinity, even though the globally optimal capped-basis determinant-entropy currency tends to zero after multiplication by `|det D_r|`.

## 5. What the calculation says about the remaining full proof

Theorems 2.1 and 4.2 isolate a genuine mechanism boundary.

1. In the one-shear Schur-isotropic frame, **basis reweighting is exhausted** on the large-shear side. The fleet04/B18 r3 half/half law is score-optimal for every `r>=1`; trying a more clever capped-basis distribution cannot repair the `r^(1/3)` target-normalized loss when `|det D|~r^-2`.

2. The loss is not evidence against the conjecture. In a target-valid saturating family the correct operation is to **aggregate the shear coordinate with the collinear residual product bank first**, obtaining a scalar with a source-valid density cap, and only then invoke the nonlinear zero-pivot theorem. That changes the determinant from the small spectral-coordinate `det D_r` to the order-one hyperbolic determinant after normalization.

3. Therefore the next structural implication should not ask for a stronger universal lower bound on `|det D|Z_w`. It should show that whenever the large-shear capped-basis currency is small, enough of the residual spectral mass is aligned with the shear direction to construct a genuine original-coordinate aggregate independent of a transverse two-bank smoother, or route the failure of such alignment to one of the existing heavy-row/physical-pair/ridge branches.

The exact arbitrary-frame version of that alignment-to-disjoint-banks extraction remains unpaid. The live fixed-minor and fixed-cross-cut corrections prohibit replacing it by one favorable bounded coordinate tuple.

## 6. Primary-source audit

- **Beckner, 1975.** The sharp Hausdorff--Young theorem is used only through the already proved capped-basis theorem, with exponents `1/alpha_i>=2`. It imposes no probabilistic moment or support condition.
- **Bennett--Carbery--Christ--Tao / Lieb.** Gaussian exhaustion identifies the rank-one Brascamp--Lieb constant used in the capped-basis theorem; it is a deterministic integral inequality and adds no random-law assumption.
- **Juškevičius--Lee, 2015.** The sharp maximum-density rearrangement applies to sums of independent real bounded-density variables. Here it is used only on the disjoint original-coordinate banks `Y_2,Y_3`, where independence is genuine.
- **Livshyts--Paouris--Pivovarov, 2016.** Their product-marginal theorem would also give the coarser universal one-dimensional cap `sqrt(2)` for normalized aggregates. It is consistent with (4.3), but the flat-bank Juškevičius--Lee constant is sharper for the two transverse banks.

No searched source was found that directly states the owner's unrestricted three-large-eigenvalue theorem under only arbitrary independent cap-one marginals. This report therefore makes no external novelty claim.

## 7. Status

- New entropy-barrier theorem: proved.
- fleet04/B18 r3: applied and shown score-optimal within the entire capped-basis certificate class for `r>=1` under its row-cap hypothesis.
- fleet04/B18 r2: applied to an actual target-valid extreme-shear family, yielding the uniform continuous bound (4.9).
- Full arbitrary-dimensional QFORM conjecture: **OPEN / NOT PROVED**.
- Full-target continuity: **OPEN**; continuity is proved for the family and branches stated above.
