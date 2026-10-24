SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-22T21:58:05Z.
attacking: literature-to-proof transfer for a fully diffuse three-bank zero-pivot branch, retaining original-coordinate product provenance and applying the completed account04/B18 zero-pivot theorem before sharpening its near-fiber estimate by a source-valid negative-moment comparison.

# account03/B18 r18 — JL/CKT negative moments + three-bank zero-pivot smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / PARTNER_RESULT_APPLIED / FULL TARGET OPEN`

The owner target remains open: for every finite `n`, independent real original-coordinate variables `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one dimension-free finite bound on the essential supremum of the density of `X^T A X`, or give a valid target counterexample. Continuity is tracked separately.

Fresh control at this run was `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`. The live corrections against post-rotation independence, arbitrary-joint coarea, positive conditional projection-density moments, worst conditional-density gates, fixed-good-minor extraction, pointwise law-uniform quadratic-phase decay, and near-zero-half-Riesz perturbation remain binding. None is used below.

## 1. Primary-source audit

### 1.1 Juškevičius--Lee: exact small-ball rearrangement

T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, Theorem 1: if independent `R^d` random vectors have density caps `K_i`, then the probability that their sum lies in any measurable set is at most the corresponding probability for independent centered uniform-ball variables of density `K_i`, with the target set replaced by a centered ball of the same Lebesgue measure. In dimension one, for every interval of length `2r`, this is a translation-uniform small-ball comparison with centered uniform intervals.

Source: https://arxiv.org/abs/1503.09190 and theorem text https://arxiv.org/html/1503.09190v2 .

No moments, centering, compact support, connected support, log-concavity, or identical-law assumption is imposed on the original variables.

### 1.2 Chasapis--König--Tkocz: exact negative-moment comparison for the uniform comparator

G. Chasapis, H. König and T. Tkocz, *From Ball's cube slicing inequality to Khinchin-type inequalities for negative moments*, J. Funct. Anal. 281 (2021), Paper 109185; arXiv:2011.12251. Their Theorem 1 states that for `0<p<1`, independent `U_i~Unif[-1,1]`, and arbitrary real coefficients `a_i`,

`E |sum_i a_i U_i|^{-p} <= C_p (sum_i a_i^2)^(-p/2)`,

where

`C_p=max{c_2(p),c_infty(p)}`,

`c_2(p)=2^(1-p/2)/[(1-p)(2-p)]`,

`c_infty(p)=(3/2)^(p/2) Gamma((1-p)/2)/sqrt(pi)`.

Source: https://arxiv.org/abs/2011.12251 and theorem text https://arxiv.org/html/2011.12251v1 .

This theorem itself is only about uniform comparators. It is transferred to arbitrary cap-one input laws below only after the Juškevičius--Lee small-ball comparison, not by silently changing the source hypotheses.

At `p=1/2`,

`C_{1/2}=c_infty(1/2)=2.2637525548355823496...`.

### 1.3 Livshyts--Paouris--Pivovarov: exact product marginal cap

G. Livshyts, G. Paouris and P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889; arXiv:1507.07949. For a product probability density `prod f_i` with every `||f_i||_infinity<=1`, every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. In particular, for a nonzero coefficient vector `a`,

`||p_{<a,X>}||_infinity <= sqrt(2)/||a||_2`.

Source: https://arxiv.org/abs/1507.07949 .

### 1.4 Banks--Garza-Vargas--Kulkarni--Srivastava: useful but not silently transferable

Theorem 2.1 of Banks--Garza-Vargas--Kulkarni--Srivastava, arXiv:2005.08930, treats

`q(X,Y)=X^T Z Y + X^T U + V^T Y + W`

for two genuinely independent random arrays with independently distributed bounded-density entries, and its non-Gaussian bound depends on singular values/rank of the bilinear matrix `Z`. Corollary 2.4 improves the scalar `k=1` case. This does **not** license replacing an arbitrary same-side quadratic remainder by a bilinear term after a rotation, so I do not use it for that purpose.

Source: https://arxiv.org/abs/2005.08930, Section 2.

## 2. New literature-transfer lemma: translation-uniform fractional potential for any cap-one linear bank

### Lemma 2.1 — `QFORM-JL-CKT-LINEAR-NEGATIVE-MOMENT-v1`

Let `X_1,...,X_m` be independent real random variables with probability densities bounded by one, and let `a in R^m` be nonzero. Put

`S=sum_i a_i X_i`.

For every `0<p<1`,

`boxed: sup_t E|S-t|^{-p} <= 2^p C_p ||a||_2^{-p}.`             (2.1)

In particular,

`boxed: sup_t E|S-t|^{-1/2}
       <= sqrt(2) C_{1/2} ||a||_2^{-1/2}.`                       (2.2)

Numerically the front constant in (2.2) is

`sqrt(2) C_{1/2}=3.201429564905224...`.

#### Proof

For every `i` with `a_i!=0`, the variable `a_i X_i` has density cap `1/|a_i|`. By Juškevičius--Lee Theorem 1 in dimension one, for every `r>0` and every center `t`,

`P(|S-t|<r) <= P(|T|<r)`,                                      (2.3)

where

`T=sum_i a_i Z_i`, `Z_i iid Unif[-1/2,1/2]`.

This is exactly the source theorem: the centered comparator interval for density cap `1/|a_i|` has length `|a_i|`.

For `0<p<1`, the layer-cake identity and Tonelli give

`E|S-t|^{-p}=p integral_0^infty r^{-p-1} P(|S-t|<r) dr`
`             <= E|T|^{-p}.`                                  (2.4)

Write `Z_i=U_i/2` with `U_i iid Unif[-1,1]`. Chasapis--König--Tkocz Theorem 1 then gives

`E|T|^{-p}=2^p E|sum_i a_i U_i|^{-p}`
`          <=2^p C_p ||a||_2^{-p}.`                            (2.5)

This proves (2.1), uniformly over the translation `t`. No property of the original variables beyond independence and their density caps has been added. QED.

## 3. A dependence-safe refinement of the partner zero-pivot theorem

The designated completed partner result is account04/B18 r2, canonical scientific source

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

It applies the completed zero-pivot `1+2` theorem: a cap-one scalar independent of an arbitrary two-dimensional vector of joint density cap `M`, under a nonsingular symmetric zero-pivot `3x3` quadratic matrix `K`, gives a continuous density bounded by

`6 M^(2/3)|det K|^(-1/3)`.                                     (3.1)

The following proposition keeps its exact proof architecture but records the two scalar quantities actually spent by the argument. It therefore extends the partner theorem without introducing new independence.

### Proposition 3.1 — `QFORM-ZEROPIVOT-NH-SCALAR-v1`

Let `S` be independent of `Y=(Y_1,Y_2)`. Assume

`||p_S||_infinity <= N`,

`sup_t E|S-t|^{-1/2} <= H`,

and `Y` has arbitrary joint density bounded by `M`. Let

`K=[[0,ell^T],[ell,B]]`

be a nonsingular real symmetric `3x3` matrix. Allow arbitrary affine terms in `(S,Y)`. Then the resulting quadratic polynomial has a continuous density and

`boxed: ||p_Q||_infinity
 <=3 N^(1/3)(M H)^(2/3)|det K|^(-1/3).`                         (3.2)

#### Proof

An orthogonal change only inside the two-dimensional `Y` variable preserves its joint density cap and scalar-vector independence. Write `ell=(L,0)` with `L>0` and

`B=[[b11,b12],[b12,beta]]`.

Because `K` is nonsingular,

`det K=-L^2 beta`,                                               (3.3)

so `beta!=0`.

The affine coefficient of `S` is absorbed by translating the first `Y` coordinate. A determinant-one affine shear/translation inside `Y` removes the mixed `uv` and linear `v` terms, preserving the joint density cap. Thus it is enough to treat

`Q=beta w^2+A(u)+2LuS`,                                        (3.4)

where the transformed joint density `g(u,w)` is still at most `M`. Put `m(u)=integral g(u,w)dw`.

For fixed `(u,w)`, integration in `S` gives the unnormalised `u`-slice output density

`h_u(t) <= N m(u)/(2L|u|).`                                    (3.5)

For fixed `(S,u)`, the two roots of the map `w -> beta w^2` give

`h_u(t)
 <= M/sqrt(|beta|) E|t-A(u)-2LuS|^{-1/2}`
` <= M H /sqrt(2|beta|L) |u|^{-1/2}.`                          (3.6)

Split the `u` integral at `|u|=r`. Using (3.6) inside and (3.5) outside,

`p_Q(t)
 <= [2 sqrt(2) M H/sqrt(|beta|L)] sqrt(r)
    + N/(2Lr).`                                                 (3.7)

For `A/r+B sqrt(r)`, optimization at `r^(3/2)=2A/B` gives

`min =3*2^(-2/3) A^(1/3)B^(2/3)`.

Substitution into (3.7), followed by (3.3), is exactly (3.2).

For almost every fixed `u!=0`, (3.4) is a convolution of two `L^1` pushforward densities, hence continuous in `t`. Equations (3.5)--(3.6) supply an integrable `u`-majorant after splitting at any fixed positive radius, so dominated convergence gives a continuous full density. QED.

As a consistency check, the original partner theorem is recovered exactly from `N=1` and the elementary cap-one scalar bound `H<=2sqrt(2)`: equation (3.2) becomes `6 M^(2/3)|det K|^(-1/3)`.

## 4. Direct application of the designated partner, then the literature sharpening

Before sharpening, apply account04/B18 literally. Let `I,J,K` be pairwise disjoint original-coordinate banks and

`S=<a,X_I>`, `U=<b,X_J>`, `V=<c,X_K>`,

with nonzero coefficient vectors `a,b,c`. The three bank variables are genuinely independent because their supports are disjoint original coordinate sets.

LPP gives

`N_S<=sqrt(2)/||a||`,
`N_U<=sqrt(2)/||b||`,
`N_V<=sqrt(2)/||c||`.

Thus `(U,V)` has joint density cap

`M<=2/(||b||||c||).`                                            (4.1)

Scale `S` by its density cap and apply the completed account04/B18 zero-pivot theorem. If `K_0` is any nonsingular symmetric zero-pivot `3x3` coefficient matrix, the direct partner splice gives

`boxed: ||p_Q||_infinity
 <=12 [||a||^2||b||^2||c||^2 |det K_0|]^(-1/3).`               (4.2)

This is an actual application of the completed partner result, not merely a citation.

Now insert Lemma 2.1 into Proposition 3.1. We have

`H_S<=sqrt(2) C_{1/2} ||a||^(-1/2)`.                            (4.3)

Equations (3.2), (4.1), (4.3) and the LPP cap for `S` yield the sharper theorem.

### Theorem 4.1 — `QFORM-JL-CKT-THREEBANK-ZEROPIVOT-v1`

Under the preceding disjoint-original-bank hypotheses, for any nonsingular symmetric zero-pivot `K_0` and arbitrary affine terms in the three aggregate bank variables,

`boxed: ||p_Q||_infinity
 <= C_* [||a||^2||b||^2||c||^2 |det K_0|]^(-1/3),`             (4.4)

where

`C_*=6*2^(1/6)*C_{1/2}^{2/3}`
`   =11.611158458837989697... .`                                (4.5)

The density is continuous.

The same estimate holds after conditioning outside these banks whenever all dependence on the three active banks factors through `(S,U,V)` and the conditioned coefficient matrix `K_0` is fixed: the bound is uniform in the resulting affine translations, so averaging the conditional continuous densities preserves the L-infinity estimate. Continuity after an arbitrary outside mixture is **not** asserted without an additional domination argument in the outside parameter; the unconditional no-outside theorem above is continuous.

## 5. Target-normalized fully diffuse stress family

The theorem is not a fixed-heavy-coordinate statement. For every `m>=1`, split `3m` original coordinates into three disjoint blocks of size `m`, and set

`a=b=c=m^(-1/2)(1,...,1)`.

Let `W` have these three disjoint unit bank vectors as columns and set

`K_0=[[0,1,1],[1,0,1],[1,1,0]]`,
`A_m=W K_0 W^T`.

Because `W^T W=I_3`, the nonzero spectrum of `A_m` is exactly

`{2,-1,-1}`,

and `det K_0=2`. Hence this is an exact rank-three instance of the owner's target for every `m`. Every nonzero physical matrix coefficient is `1/m`, so no uniformly heavy original-coordinate coefficient or fixed physical minor survives as `m->infinity`.

Theorem 4.1 gives, for every choice of independent original-coordinate probability densities bounded by one,

`boxed: ||p_{X^T A_m X}||_infinity
 <= C_* 2^(-1/3)
 =9.2157825760644413... .`                                     (5.1)

The density is continuous. This is a genuine aggregate-before-inversion branch and strictly improves the direct partner/LPP constant `12*2^(-1/3)=9.524406...` on this family.

## 6. Quantifier and correction audit

- Original coordinates remain independent; no independence is asserted after a general spectral rotation.
- JL is used on independent one-dimensional summands before aggregation. CKT is used only on JL's independent centered-uniform comparators.
- LPP is used only for product-measure linear marginals, exactly as stated.
- The nonlinear zero-pivot step is the designated account04/B18 proof architecture, extended only by exposing the scalar density cap `N` and the scalar translation-uniform half-Riesz quantity `H` actually used in its two estimates.
- No arbitrary bounded 3D joint law is substituted for product provenance.
- No positive conditional projection-density moment, worst conditional density, fixed good minor, pointwise Fresnel decay, moment assumption, support assumption, Gaussianity, or log-concavity is used.
- The newest near-zero-half-Riesz correction is irrelevant: the theorem assumes an exact zero pivot in the three-bank coefficient matrix and makes no perturbative claim.

## 7. What this does and does not solve

This run closes a new fully diffuse, product-preserving three-bank zero-pivot class and supplies a reusable translation-uniform negative-moment interface for arbitrary cap-one linear banks. It does **not** prove that the bare condition `s_3(A)>=1` always yields such a three-bank zero-pivot factorization. Current correction examples forbid replacing that missing structural implication by a uniformly good fixed minor/triple.

The next full-target implication is therefore structural/aggregate:

`QFORM-THREEBANK-CERTIFICATE-OR-PAID-BRANCH-v1`:

from an arbitrary symmetric `A` with `s_3(A)>=1`, either enter one of the already completed physical-pair/scalar-pivot/ridge/three-cross branches, or construct disjoint original-coordinate aggregate banks whose effective `3x3` core has an exact zero pivot and satisfies a dimension-free lower bound on

`||a||^2 ||b||^2 ||c||^2 |det K_0|`.

The current fixed-minor counterexamples show that the certificate, if true, must be genuinely aggregate rather than a bounded-cardinality coordinate selection.

**Full QFORM:** OPEN / NOT PROVED.  
**Continuity:** PROVED for Theorem 4.1 without arbitrary outside mixing; OPEN for the unrestricted target.

## 8. Source pins

Primary literature:
- Juškevičius--Lee, arXiv:1503.09190.
- Chasapis--König--Tkocz, arXiv:2011.12251, JFA 281 (2021), 109185.
- Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Israel J. Math. 216 (2016), 877--889.
- Banks--Garza-Vargas--Kulkarni--Srivastava, arXiv:2005.08930, Section 2.

Designated partner proof actually applied:
- `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Fresh control source for this run:
- `yspennstate/math-research-brain@38b2e0766a6d8394cb53e9a7fe3c4520770d3309`, OWNER CONTROL revision `2026-09-22.15` at mathematical start. Final control/correction refresh is recorded separately in the run receipt.
