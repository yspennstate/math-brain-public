SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-23T03:53:24Z.
attacking: aggregate determinant-entropy certificates which survive arbitrary coordinatewise quadratic tails and arbitrary outside spectrum, using disjoint volume-sampled bases rather than one fixed minor.

# fleet03/B18 r23 — disjoint-volume-basis Fresnel transfer with separable tails

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: literature-to-proof transfer  
Status: `PROVED SUPPORTING TARGET-LEVEL BRANCH / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and why this run changes mechanism

The owner target is unchanged: for arbitrary independent real original-coordinate variables with probability densities at most one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal `L^infinity` bound for the density of `X^T A X`, or give a counterexample. Continuity is tracked separately.

The preceding B18 run closed only the **exact** all-cut-rank-one strict-N3 endpoint. It did not produce a quantitative second singular value for one fixed physical cut. Current corrections explicitly rule out several fixed-minor / fixed-row extraction upgrades. This run therefore does not select a single good three-coordinate minor. It pays an **aggregate distribution of physical three-column bases** and uses relative entropy to retain determinant mass while enforcing the capped-basis marginals needed by the completed Fresnel theorem.

The principal new point is also useful for the full-matrix problem: the capped-basis Fresnel argument is unchanged after multiplication of each input density by an arbitrary unit-modulus phase depending on that **same original coordinate**. Hence arbitrary active diagonal terms, affine terms produced by conditioning, and an arbitrary outside quadratic block can be retained exactly.

## 2. Source-valid analytic input

The completed internal theorem used below is fleet01/B18 `QFORM-FRESNEL-CAPPED-BASIS-WEIGHTS-v1`, canonical source

`yspennstate/math-open-problems@6548356a589d356e4bfa02bfd4f4eb205a72182a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B18/20260922T225705Z-qform-B18-a01-r19/REPORT.md`.

For a rank-three factorization

`B=L^T D L`,

with `L` a real `3 x m` rank-three matrix and `D` invertible symmetric, let `w` be a probability law on nonsingular three-column bases. Write

`alpha_i = P_w(i in S)`,

and

`Z_w = exp(H(w) + E_w log det(L_S)^2)`.

If every `alpha_i<=1/2`, the theorem gives, for independent cap-one original-coordinate inputs,

`||p_(X^T B X)||_infinity <= 3 B_alpha^(2/3) (|det D| Z_w)^(-1/3)
                              <= 3 e (|det D| Z_w)^(-1/3)`,

and a continuous density.

The primary analytic sources match the gates actually used:

1. William Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159--182. The sharp Hausdorff--Young inequality applies to arbitrary complex-valued `L^p` functions. No positivity, moment, support, smoothness, Gaussianity or log-concavity is required.
2. Elliott Lieb, *Gaussian kernels have only Gaussian maximizers*, Inventiones Mathematicae 102 (1990), 179--208, together with Bennett--Carbery--Christ--Tao, *The Brascamp--Lieb inequalities: finiteness, structure and extremals*, GAFA 17 (2008), 1343--1415. These are the Gaussian-exhaustion / Brascamp--Lieb inputs used by the rank-one BL step in the internal theorem.
3. Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889 / arXiv:1507.07949, was rechecked as a product-projection source. It gives `2^(k/2)` caps for `k`-dimensional orthogonal marginals under exactly the cap-one product hypothesis, but it is **not** used here as a substitute for independence after projection.

I also rechecked Herry--Malicet--Poly, arXiv:2303.09488. Their quadratic-form regularity theory assumes iid inputs from a much smoother Gaussian-functional class and asymptotic operator hypotheses, so it is not an exact prior solution of the present arbitrary non-iid cap-one problem.

## 3. Phase-stability lemma: arbitrary coordinatewise tails cost nothing

### `QFORM-CAPPED-BASIS-SEPARABLE-PHASE-v1`

Let `psi_i:R->R` be arbitrary measurable functions. Under the capped-basis hypotheses above, set

`T = X^T L^T D L X + sum_i psi_i(X_i)`.

Then `T` has a continuous density and exactly the same bound

`||p_T||_infinity <= 3 B_alpha^(2/3)(|det D|Z_w)^(-1/3)
                   <=3e(|det D|Z_w)^(-1/3).`                 (3.1)

### Proof

Fix Fourier frequency `t`. In the reviewed Fresnel linearization, the only place the input law of coordinate `i` enters is through the one-dimensional Fourier transform of the coordinate factor. Replace

`f_i(x)`

by

`g_(i,t)(x)=f_i(x) exp(i t psi_i(x)).`

Then `|g_(i,t)|=f_i`. For every exponent `1<=p<=infinity`,

`||g_(i,t)||_p=||f_i||_p<=1`,

because `0<=f_i<=1` and `int f_i=1`. Beckner's Hausdorff--Young inequality is valid for complex-valued functions, so every one-dimensional Fourier `L^(1/alpha_i)` estimate used in fleet01/B18 is unchanged. The Brascamp--Lieb determinant step depends only on the physical linear forms and on `alpha`, not on the phases. Therefore the reviewed characteristic-function bound remains

`|phi_T(t)| <= pi^(3/2) B_alpha |t|^(-3/2)
               (|det D| Z_w)^(-1/2)`                         (3.2)

for `t!=0`, uniformly over all measurable `psi_i`. Combining with `|phi_T|<=1`, the same exact `L^1` integration gives (3.1). Since the majorant in (3.2) is integrable at infinity, Fourier inversion supplies a continuous representative. QED.

This step is important for the owner target: no perturbative continuity in matrix coefficients is asserted. The diagonal / affine terms are retained **exactly** as unit-modulus coordinate phases.

## 4. New aggregate construction: condition two volume bases to be disjoint

Put

`G=LL^T`, `Z_0=det G>0`,

and let `mathcal B` denote all nonsingular three-column bases of `L`. By Cauchy--Binet,

`Z_0 = sum_(S in mathcal B) det(L_S)^2.`

Define the volume-sampling law

`q_S = det(L_S)^2/Z_0.`                                    (4.1)

Let `S,T` be independent samples from `q`, and define the **disjoint-volume probability**

`delta = P_qxq(S cap T = emptyset).`                         (4.2)

Assume `delta>0`. Let `mu` be the law of `(S,T)` conditioned on disjointness, and let `w` be its first marginal.

### Lemma 4.1 — capped marginals

Every coordinate marginal of `w` is at most one half.

Indeed, symmetry of `mu` gives

`P_mu(i in S)=P_mu(i in T)=alpha_i`.

On the disjointness event,

`1_(i in S)+1_(i in T)<=1`.

Taking expectations yields `2 alpha_i<=1`.

### Lemma 4.2 — determinant-entropy score loses at most `delta`

The score of `w` obeys

`Z_w >= Z_0 delta.`                                          (4.3)

Proof: because `det(L_S)^2=Z_0 q_S`,

`log Z_w
 = H(w)+E_w log det(L_S)^2
 = log Z_0 - D_KL(w || q).`                                  (4.4)

On the other hand,

`d mu/d(q x q) = 1_(S cap T=emptyset)/delta`,

so

`D_KL(mu || q x q)=log(1/delta).`                            (4.5)

Relative entropy decreases under the projection `(S,T)->S`; therefore

`D_KL(w||q)<=log(1/delta)`.

Substitution into (4.4) proves (4.3). QED.

No individual determinant is selected. A family may have every fixed physical determinant tending to zero while the aggregate score remains positive.

## 5. Main theorem: disjoint-volume-basis Fresnel certificate with arbitrary separable tail

### `QFORM-DISJOINT-VOLUME-PAIR-FRESNEL-v1`

Under the notation above, for arbitrary measurable coordinatewise `psi_i`, if `delta>0`, then

`T=X^T L^T D L X + sum_i psi_i(X_i)`

has a continuous density satisfying

`boxed:
 ||p_T||_infinity
 <=3e ( |det D| det(LL^T) delta )^(-1/3).`                   (5.1)

Proof: use the conditioned-disjoint basis law `w`. Lemma 4.1 verifies the exact capped-marginal gate of `QFORM-CAPPED-BASIS-SEPARABLE-PHASE-v1`; Lemma 4.2 gives its score. Equation (3.1) then yields (5.1). QED.

If `B=L^TDL` has exact rank three, then

`|pdet B| = |det D| det(LL^T)`.                              (5.2)

Consequently, whenever `|pdet B|>=kappa`,

`||p_T||_infinity <=3e (kappa delta)^(-1/3).`                 (5.3)

For an exact-rank-three owner-target matrix `B`, `kappa>=1` automatically.

## 6. Local full-ambient version: arbitrary outside spectrum is allowed

The previous theorem localizes to a principal original-coordinate packet.

Let `I` be any set of physical coordinates. Suppose its principal block admits

`A_(I,I)=L^T D L + Delta`,                                   (6.1)

where `Delta` is diagonal and the rank-three core `L^T D L` has parameters `kappa,delta` as above. **No restriction is placed on** `A_(I^c,I^c)` or on the cross block `A_(I,I^c)`.

Condition on all outside variables `X_(I^c)=y`. The full quadratic form becomes

`X_I^T L^T D L X_I
 + sum_(i in I) [ Delta_ii X_i^2 + beta_i(y) X_i ]
 + constant(y).`                                              (6.2)

This is exactly the separable-phase theorem, and its Fourier majorant is uniform in `y`. Hence averaging the conditional characteristic functions preserves the same integrable majorant. Therefore the **full ambient law** has a continuous density and

`boxed:
 ||p_(X^T A X)||_infinity
 <=3e (kappa delta)^(-1/3).`                                  (6.3)

Thus arbitrary additional spectrum outside the certified packet, arbitrary couplings to it, and arbitrary diagonal curvature inside it are all absorbed. What is *not* absorbed is an arbitrary additional off-diagonal quadratic term inside the active packet.

A particularly transparent matrix corollary is obtained by taking the core to be the off-diagonal part of a principal block. If

`H_I=A_(I,I)-diag(A_(I,I))`

has rank three, `|pdet H_I|>=kappa`, and its volume-basis disjoint probability is at least `delta`, then (6.3) holds for the full matrix `A`.

## 7. Leverage-collision corollary

The coordinate marginals of the volume law `q` are the usual leverage scores

`c_i = ell_i^T (LL^T)^(-1) ell_i`,

with `sum c_i=3`. For independent volume bases `S,T`,

`E |S cap T| = sum_i c_i^2.`                                  (7.1)

Hence the union bound gives

`1-delta=P(S cap T != emptyset)
 <= E|S cap T|
 =sum_i c_i^2.`                                               (7.2)

Therefore, if

`rho:=sum_i c_i^2<1`,

then

`boxed:
 ||p_T||_infinity
 <=3e [kappa(1-rho)]^(-1/3).`                                 (7.3)

For example, `rho<=3/4` and `kappa>=1` imply

`||p_T||_infinity <=3e 4^(1/3)
 =12.9450103021...`                                           (7.4)

with continuity.

This is only a sufficient corollary; the exact `delta` can be much larger than `1-rho`.

## 8. Explicit co-heavy target family beyond the natural leverage gate

This family shows why the aggregate construction is useful and why it respects the current correction against extracting one uniformly good row/minor.

Take `m=13` physical coordinates and let `R` be the `13 x 3` matrix whose rows are

- `sqrt(3/5)e_1` once;
- `sqrt(1/10)e_1` four times;
- `(1/2)e_2` four times;
- `(1/2)e_3` four times.

Then exactly

`R^T R=I_3.`                                                  (8.1)

Let

`D=diag(1,1,-1)`, `B=R D R^T`.

The three nonzero eigenvalues of `B` are exactly `{1,1,-1}`. Thus this is an exact owner-target core. Its first physical leverage is `3/5>1/2`, so the **natural** volume law fails the capped-basis gate.

Nevertheless the volume law factorizes by the three axis groups. In the first group the choice probabilities are

`(3/5,1/10,1/10,1/10,1/10)`,

and in each of the second and third groups they are `(1/4,1/4,1/4,1/4)`. Two sampled bases are disjoint iff their choices differ in all three groups. Therefore

`delta
 =[1-((3/5)^2+4(1/10)^2)] [1-4(1/4)^2]^2
 =(3/5)(3/4)^2
 =27/80.`                                                     (8.2)

The general theorem already gives

`||p||_infinity <=3e(80/27)^(1/3)=11.7127213370...`.          (8.3)

In this product example the conditioned-disjoint marginal law can be read exactly. In the first group it changes to

`(2/5,3/20,3/20,3/20,3/20)`,

while the two uniform four-point groups stay uniform. Hence every basis marginal is at most `2/5`. Its exact KL divergence from the volume law is

`D_KL = (1/5) log(3/2)`,

so

`Z_w=(2/3)^(1/5).`                                            (8.4)

Using the exact score rather than only `Z_w>=delta` sharpens (8.3) to

`boxed:
 ||p||_infinity
 <=3e (3/2)^(1/15)
 =8.3782854714...`                                            (8.5)

and the density is continuous.

By Section 6, (8.5) remains valid after adding **arbitrary diagonal coefficients on these 13 active coordinates**, embedding the packet into any higher dimension, adding an arbitrary outside symmetric block, and adding arbitrary active--outside couplings. Conditioning turns all such couplings into affine one-coordinate phases and does not change the bound.

Thus this run pays a genuinely co-heavy (`max leverage=3/5`) high-cardinality full-ambient branch without selecting a fixed good physical triple.

## 9. Designated partner fleet04/B18 actually applied

The latest completed designated partner result is fleet04/B18 `QFORM-ISOTROPIC-SHEAR-MIXED-VOLUME-v1`, canonical scientific source

`yspennstate/math-open-problems@24a9362bd3f24a3849021093cf98611f95b5ab04`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260923T001857Z-fleet04-B18-QFORM-r3/REPORT.md`,

with its later general diffuse-frame strengthening at

`yspennstate/math-open-problems@e9eb90e2a7746482fb3ba75bf449b224cbf507ce`.

For the partner's Schur-isotropic packet

`Q_0=(V^T X_res+uX_0)^T D(V^T X_res+uX_0)`,

put `r=||u||`, `n=u/r`, `p_j=||v_j||^2`, `q_j=||(I-nn^T)v_j||^2`. The completed partner theorem constructs an explicit capped basis law with score `Z_w=2r` whenever `p_j+q_j<=1`. It gives the actual inequality

`||p_(Q_0)||_infinity
 <=3e(2r|det D|)^(-1/3).`                                    (9.1)

At its explicit target packet

`r=2`, `D=diag(1,1,-1)`,

with six residual rows given by two copies of each `e_k/sqrt(2)`, the nonzero physical spectrum is `{sqrt(5),1,-sqrt(5)}` and (9.1) gives

`boxed:
 ||p_(Q_0)||_infinity <=3e/4^(1/3)
 =5.1372307428... .`                                          (9.2)

The phase-stability lemma of Section 3 now applies **to the partner's completed basis law itself**. Consequently (9.1)--(9.2) remain valid after arbitrary one-coordinate measurable phases. In matrix language, the partner packet is therefore lifted to the full-ambient statement of Section 6: arbitrary active diagonal perturbations, arbitrary outside spectrum, and arbitrary outside couplings do not change its bound. This is a substantive application of the designated partner result, not a label-only citation.

Continuity also survives because the conditional characteristic-function majorant is uniform and integrable.

## 10. Compatibility with live corrections

This proof does not use any currently refuted interface:

- no independence is asserted after a spectral rotation;
- no arbitrary-joint quadratic coarea theorem is invoked;
- no positive conditional projection-density moment is taken;
- no worst conditional fiber-height supremum is integrated;
- no fixed physical minor, row atom or one-triple determinant is extracted;
- no cross-only Schur certificate is substituted for a true full-pair Schur complement;
- no conditional density cap is promoted to independence;
- no pointwise law-uniform van-der-Corput decay is assumed.

The new basis law is built entirely from determinants of original-coordinate columns. The only independence used is the original product law in the Beckner / Brascamp--Lieb Fourier estimate.

The recent `QFORM-COHEAVY-SINGLE-ROW-EXTRACTION-FALSE-v1` correction is particularly compatible: its lesson is to retain aggregate determinant mass instead of forcing one row atom. The present score `Z_w` does exactly that.

## 11. What this closes and what remains

This run closes the following target-level implication:

> A rank-three original-coordinate principal packet with a dimension-free determinant-volume collision certificate (`kappa delta >= c_0>0`) pays the **full ambient quadratic form**, including arbitrary active diagonal curvature, arbitrary outside quadratic spectrum and arbitrary cross couplings, with a continuous density bounded by `3e c_0^(-1/3)`.

The structural obligation left by the owner target is now sharper. In the low-stable-rank / strict-N3 survivor, one may try to prove that either

1. some product-preserving rank-three completion has `kappa delta` bounded below and enter this theorem;
2. the disjoint-volume probability is very small, which quantitatively means volume-sampled bases collide heavily and should force a localized coloop / nearly-coloop geometry; or
3. route directly to the existing pair, scalar-Schur, ridge, grouped-bank, or two-gradient branches.

This is an aggregate-before-extraction formulation and avoids the already-refuted attempt to force one uniformly good physical minor.

I do **not** claim that `s_3(A)>=1` by itself has yet been proved to force `kappa delta>=c_0`. That is the remaining structural bridge. The unrestricted conjecture remains `OPEN / NOT PROVED`, and unrestricted continuity remains open.

## 12. Source ledger

Primary public sources checked this run:

- Beckner, *Inequalities in Fourier analysis*, Ann. Math. 102 (1975), DOI 10.2307/1970980.
- Lieb, *Gaussian kernels have only Gaussian maximizers*, Invent. Math. 102 (1990), DOI 10.1007/BF01233426.
- Bennett--Carbery--Christ--Tao, *The Brascamp--Lieb inequalities: finiteness, structure and extremals*, GAFA 17 (2008), DOI 10.1007/s00039-007-0619-6.
- Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), DOI 10.1007/s11856-016-1431-5, arXiv:1507.07949.
- Herry--Malicet--Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488; checked and rejected as an exact prior solution because its source class is substantially narrower than the owner target.

No search miss is used as a novelty claim.
