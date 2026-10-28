# account01/B18 r19 — capped-basis Fresnel transfer for the Schur-isotropic product-projection core

**Run:** `20260922T225705Z-qform-B18-a01-r19`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / DESIGNATED_PARTNER_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and source discipline

The owner target remains open: for arbitrary finite `n`, independent real original-coordinate variables `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite bound on the density of `X^T A X`, or give a valid target counterexample. Continuity is tracked separately.

This report does **not** use independence after rotation, arbitrary-joint coarea, conditional projection-density caps, pointwise law-uniform Fresnel decay, near-zero-as-zero perturbation, or a fixed-good-minor implication. It keeps the original product characteristic function until the Brascamp--Lieb step.


## 2. Primary literature transferred exactly

Two classical inputs are used at their actual hypotheses.

1. **Sharp Hausdorff--Young.** W. Beckner, *Inequalities in Fourier analysis*, Ann. Math. 102 (1975), 159--182, DOI 10.2307/1970980. With Fourier convention

   `fhat(s)=integral exp(-isx) f(x) dx`,

   if `0<alpha<=1/2`, `q=1/alpha`, `p=1/(1-alpha)`, and `f` is a probability density with `0<=f<=1`, then `||f||_p<=1` and Beckner gives

   `||fhat||_(1/alpha)
      <= (2*pi)^alpha
         (1-alpha)^(-(1-alpha)/2)
         alpha^(alpha/2).`                                      (2.1)

   Translation of the Fourier argument does not change this norm.

2. **Gaussian exhaustion for Brascamp--Lieb.** E. Lieb's Gaussian-extremizer theorem, in the formulation/reproof of J. Bennett, A. Carbery, M. Christ, T. Tao, *The Brascamp--Lieb inequalities: finiteness, structure, and extremals*, arXiv:math/0505065. For rank-one maps `B_i z=<ell_i,z>` and exponents `alpha_i`, the BL constant is the supremum of the centered-Gaussian ratio used in Section 3 below.

The Fresnel linearisation and its normalization are the source-checked formula already used in the reviewed QFORM Theorem F package at `yspennstate/math-open-problems@9844891a9fbe96a65e37f71122bf0300b53dcc80:proofnet24/QFORM-density/interactive/20260922T220600Z-claude-review/REVIEW.md`; the present argument changes the BL weights rather than assuming the natural leverage weights.

## 3. New transfer theorem: arbitrary capped basis weights

Let `L` be a real `3 x n` matrix of rank three, with columns `ell_i in R^3`, and let `D` be an invertible real symmetric `3 x 3` matrix. Put

`A=L^T D L`.

Let `B` be the family of three-element column sets `S` for which `det L_S !=0`. Let `w=(w_S)` be **any** probability distribution supported on `B`. Define its coordinate marginals

`alpha_i = sum_(S contains i) w_S`,

so `sum_i alpha_i=3`, and define the determinant-entropy score

`Z_w = exp( H(w) + sum_S w_S log det(L_S)^2 )`,              (3.1)

where `H(w)=-sum_S w_S log w_S` and zero-mass terms are omitted.

### Theorem — `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`

Assume

`alpha_i <= 1/2` for every `i`.                                (3.2)

Then for arbitrary independent original-coordinate variables `X_i` with probability densities bounded by one, the quadratic form

`Q=X^T L^T D L X`

has a bounded **continuous** density and

`boxed:
 ||p_Q||_infinity
 <= 3 B_alpha^(2/3) ( |det D| Z_w )^(-1/3)
 <= 3 e ( |det D| Z_w )^(-1/3),`                              (3.3)

where

`B_alpha = product_(0<alpha_i<=1/2)
          (1-alpha_i)^(-(1-alpha_i)/2).`                       (3.4)

The same proof permits affine terms, since they only translate the one-dimensional Fourier arguments.

### Proof

Diagonalize `D=O diag(lambda_1,lambda_2,lambda_3) O^T` and replace `L` by `O^T L`. Absolute three-column determinants and hence `Z_w` are unchanged. Fresnel linearisation gives for `t!=0`

`|phi_Q(t)|
 <= product_(k=1)^3 (4*pi*|t lambda_k|)^(-1/2)
    integral_(R^3) product_i |fhat_i(<ell_i,z>+tau_i)| dz`,   (3.5)

with harmless translations `tau_i` (zero for the pure quadratic form).

Set `h_i(s)=|fhat_i(s+tau_i)|`. For `alpha_i>0`, write

`h_i=(h_i^(1/alpha_i))^alpha_i`.

The rank-one BL Gaussian formula is

`BL(L,alpha)
 = sup_(d_i>0)
   [ product_i d_i^(alpha_i/2) ]
   / det( sum_i alpha_i d_i ell_i ell_i^T )^(1/2).`           (3.6)

By Cauchy--Binet,

`det( sum_i alpha_i d_i ell_i ell_i^T )
 = sum_(|S|=3) det(L_S)^2 product_(i in S)(alpha_i d_i).`     (3.7)

Use the chosen probability weights `w_S` and weighted AM--GM:

`det(...)
 >= product_S [ det(L_S)^2 product_(i in S)(alpha_i d_i)/w_S ]^w_S
 = Z_w product_i (alpha_i d_i)^alpha_i.`                      (3.8)

Therefore Lieb's theorem yields

`BL(L,alpha)
 <= Z_w^(-1/2) product_i alpha_i^(-alpha_i/2).`               (3.9)

Apply BL to the integral in (3.5), then Beckner (2.1). Since `sum alpha_i=3`, the powers of `alpha_i` cancel exactly:

`integral_(R^3) product_i h_i(<ell_i,z>) dz
 <= BL(L,alpha) product_i ||h_i||_(1/alpha_i)
 <= (2*pi)^3 B_alpha Z_w^(-1/2).`                             (3.10)

Combining (3.5) and (3.10),

`|phi_Q(t)|
 <= pi^(3/2) B_alpha |t|^(-3/2)
    (|det D| Z_w)^(-1/2).`                                    (3.11)

Together with `|phi_Q(t)|<=1`, put

`K=pi^(3/2) B_alpha (|det D|Z_w)^(-1/2)`.

The exact elementary integral is

`integral_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3).`               (3.12)

Hence Fourier inversion gives

`||p_Q||_infinity
 <= (2*pi)^(-1) 6 K^(2/3)
 =3 B_alpha^(2/3)(|det D|Z_w)^(-1/3).`                        (3.13)

Since `0<=alpha<=1/2` and `-(1-alpha)log(1-alpha)<=alpha`,

`log B_alpha <= (1/2) sum_i alpha_i =3/2`,                    (3.14)

which gives the final `3e` bound. Equation (3.11) is integrable at infinity, so Fourier inversion supplies a continuous representative. QED.

### Relation to the natural-leverage theorem

If `w` is volume sampling, `w_S=det(L_S)^2/det(LL^T)`, then `Z_w=det(LL^T)` and its marginals are the usual leverage scores. Thus (3.3) contains the natural-leverage Fresnel branch. The point here is that **one is not forced to use volume-sampling marginals**: any source-valid capped basis distribution can be inserted, paying its exact determinant-entropy score.

## 4. Two-disjoint-basis corollary with a sharper constant

Suppose `S,T` are disjoint three-element column sets with nonzero determinants. Take `w_S=w_T=1/2`. Every active marginal equals exactly `1/2`, so (3.2) holds. Moreover

`Z_w = 2 |det L_S det L_T|`,                                  (4.1)

and `B_alpha=2^(3/2)`. Therefore (3.3) specializes to

`boxed:
 ||p_Q||_infinity
 <=6 [ 2 |det D| |det L_S det L_T| ]^(-1/3).`                (4.2)

This is `QFORM-FRESNEL-TWO-DISJOINT-BASES-v1`.

If `A=L^T D L` has exact rank three and its three nonzero eigenvalues have modulus at least one, then

`|pdet A|=|det D| det(LL^T)>=1`.                              (4.3)

Define the captured two-basis Cauchy--Binet fraction

`theta_(S,T)=2|det L_S det L_T|/det(LL^T).`                   (4.4)

Then (4.2) becomes the target-normalized certificate

`boxed: ||p_Q||_infinity <=6 theta_(S,T)^(-1/3).`             (4.5)

Thus any two disjoint bases carrying a fixed positive fraction of the total determinant volume close the corresponding exact-rank-three branch with a universal constant.

## 5. Actual application of designated partner account02/B18

The completed designated-partner report is

`yspennstate/math-open-problems@0a28faf7bf87a49a9df787eb276b449aee3d9c47:proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260922T221352Z-account02-B18-QFORM-r11/REPORT.md`.

Its theorem `QFORM-ZEROPIVOT-NONISOTROPIC-CLOSURE-v1` closes two of the three exact-rank-three zero-pivot cases. Its only surviving zero-pivot case is Schur-isotropic. In its notation the surviving quadratic form is exactly

`Q=(Y+u X_i)^T D (Y+u X_i)`,                                  (5.1)

where `X_i` is an original scalar independent of the residual original coordinates, `Y=V^T X_-i` for a `3`-dimensional orthogonal projection `V`, and `u^T D u=0`. The partner proves the exact coefficient-map and pseudodeterminant ledger

`L=[u, V^T]`, `LL^T=I+uu^T`,

`A=L^T D L`,

`pdet(A)=det(D) det(LL^T)=det(D)(1+||u||^2).`                 (5.2)

Apply Theorem (3.3) to **this exact partner factorization**. If the partner shear map has any capped basis distribution `w`, then

`boxed:
 ||p_Q||_infinity
 <=3e ( |det D| Z_w )^(-1/3).`                               (5.3)

In particular, if it has two disjoint physical three-coordinate bases `S,T`, then

`boxed:
 ||p_Q||_infinity
 <=6 theta_(S,T)^(-1/3),`                                    (5.4)

with `theta` defined by (4.4). This closes a concrete part of the exact Schur-isotropic branch that the partner report left unpaid. It uses the actual product-projection provenance, not the false arbitrary-joint coarea interface.

## 6. A target-valid high-leverage Schur-isotropic family newly paid by the alternative weights

The alternative-weight clause is not cosmetic. Let

`u=(1,0,1)/sqrt(2)`,
`e=(0,1,0)`,
`v=(1,0,-1)/sqrt(2)`,

so `(u,e,v)` is an orthonormal Euclidean basis and `u^T J u=0` for `J=diag(1,1,-1)`. Define the `3 x 6` coefficient matrix whose columns are

`L=(2u, 2e, 2v, u, e, v)`                                    (6.1)

and put

`D=J/5`, `A=L^T D L`.                                        (6.2)

Then

`LL^T=5 I_3`,                                                  (6.3)

so the three nonzero eigenvalues of `A` are the eigenvalues of `D LL^T=J`, namely

`{1,1,-1}`.                                                    (6.4)

The first physical diagonal is exactly zero because `u^TJu=0`. Removing that coordinate leaves a rank-three residual, and direct Schur algebra gives the partner's third, Schur-isotropic zero-pivot case (`b` lies in the residual range and `b^T C^+ b=0`).

The **natural** leverage scores of the six columns are

`(4/5,4/5,4/5,1/5,1/5,1/5)`,                                 (6.5)

so the ordinary natural-leverage `<=1/2` Fresnel gate fails maximally on the first whole basis.

Nevertheless the first three and last three columns are disjoint bases with

`|det L_{123}|=8`, `|det L_{456}|=1`.                         (6.6)

Take half weight on each basis. Then `alpha_i=1/2` for all six coordinates and

`|det D| Z_w=(1/125)*(2*8*1)=16/125`.                         (6.7)

The two-basis theorem therefore gives, for **every** admissible independent cap-one product input,

`boxed:
 ||p_(X^T A X)||_infinity
 <=6(125/16)^(1/3)
 =11.9055078897615... .`                                      (6.8)

The density is continuous. This is a genuine target instance in the designated partner's previously unpaid Schur-isotropic class, and it is not covered by the natural leverage `<=1/2` gate.

## 7. Correction audit and exact remaining implication

Fresh live corrections were consumed before publication. In particular:

- arbitrary-joint three-dimensional coarea is false;
- bounded conditional projection density does not imply independence;
- positive conditional projection-density moments can diverge;
- exact spectral-bank separation is not forced;
- a small self-curvature block cannot be replaced by zero for free;
- fixed good minors/cross-rank cuts are not guaranteed by the three-large-eigenvalue hypothesis.

The theorem above survives these corrections because it never conditions on a rotated spectral complement and never forgets product provenance: factorization occurs at the characteristic-function level in the **original independent coordinates**.

The first unpaid implication after this run is now more precise for the partner Schur-isotropic core:

> Given `L=[u,V^T]` from (5.2) and target normalization `|det D|det(LL^T)>=1`, either prove that the capped-basis optimization admits `Z_w >= c det(LL^T)` for one universal `c>0`, **or** route the complementary basis-volume concentration regime to an already-paid physical-pivot/hub/localized branch without perturbative replacement.

A universal capped-score lower bound is not asserted here; highly concentrated basis volume can make the score small. The new theorem converts that question into an exact matroid/determinant-volume selection problem and closes every instance for which the score is quantitatively nondegenerate.

No exact prior theorem located in the source audit settles the owner's unrestricted arbitrary-cap-one QFORM target. Kosov's recent polynomial-image regularity theorems require bounded variation and/or moment hypotheses that are absent here; Carbery--Wright/Glazer--Mikulincer likewise impose convexity/log-concavity or normalization assumptions not available for arbitrary fragmented cap-one marginals.

## 8. Source pins

- Fresh brain control: `yspennstate/math-research-brain@a49099111ed329ca3fb78b9b81f3051e5bce06d0`.
- Designated partner account02/B18: `yspennstate/math-open-problems@0a28faf7bf87a49a9df787eb276b449aee3d9c47`, exact path in Section 5.
- Reviewed Fresnel/BL package and sharp-HY refinement: `yspennstate/math-open-problems@9844891a9fbe96a65e37f71122bf0300b53dcc80:proofnet24/QFORM-density/interactive/20260922T220600Z-claude-review/REVIEW.md`.
- Beckner (1975): DOI `10.2307/1970980`.
- Bennett--Carbery--Christ--Tao: arXiv `math/0505065`.

No claim of literature-wide novelty is made. The full target remains **OPEN / NOT PROVED**.
