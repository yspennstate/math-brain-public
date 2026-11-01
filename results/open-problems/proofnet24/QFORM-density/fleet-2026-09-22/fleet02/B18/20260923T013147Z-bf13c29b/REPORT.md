SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-23T01:31:47Z.
attacking: literature-to-proof transfer for the large-shear Schur-isotropic obstruction, preserving original-coordinate product provenance.

# fleet02/B18 — source-valid aggregate/null-pivot transfer and extreme-shear dual certificate

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Role:** Literature-to-proof transfer  
**Status:** PROVED SUPPORTING TARGET-VALID FAMILY + QUANTITATIVE PAYOFF LEMMA / FULL QFORM OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## 1. First unpaid implication

The latest completed designated-partner result fleet03/B18 r21 leaves the following structural obligation in the arbitrary Schur-isotropic large-shear frame: extract, using disjoint ORIGINAL coordinates, a scalar aggregate aligned with the shear direction which is independent of a transverse two-dimensional product projection, with bounded scalar density and a nondegenerate zero-pivot quadratic determinant; otherwise route the matrix to an already-paid physical-pair/heavy-row/ridge branch.

This report proves the exact analytic payoff once such an aggregate is available, and then applies it to the partner's explicit extreme-shear target family. It does **not** prove the structural extraction for an arbitrary A.

## 2. Source pins actually used

### 2.1 Completed worker kernel

Fleet02/B16, `QFORM-NULL-SCALAR-DEPENDENT-PAIR-v1`, source:

- math-open-problems commit `5bf3d5e6765ecd1dd091fc7d862f6f04211c530f`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260922T232932Z-fleet02-B16-QFORM-auto11/REPORT.md`.

If X has density <=1, is independent of a pair (C,D) with joint density cap M, and beta,gamma are nonzero, then

`Q=2 beta X C + alpha C^2 + 2 delta C D + gamma D^2`

has an essentially bounded density with

`||p_Q||_infinity <= 3 (2M)^(2/3) |beta^2 gamma|^(-1/3)`.        (2.1)

The pair coordinates C,D need not be independent.

### 2.2 Primary projection theorem: Livshyts--Paouris--Pivovarov

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1 (published Israel J. Math. 216 (2016)).

Exact hypotheses used: `f(x)=prod_i f_i(x_i)`, each `f_i>=0`, `||f_i||_1=1`, bounded; E is a k-dimensional orthogonal subspace. The theorem gives numbers gamma_i in [0,1], sum gamma_i=k, and

`||pi_E f||_infinity <= min((n/(n-k))^((n-k)/2), 2^(k/2)) prod_i ||f_i||_infinity^(gamma_i)`.   (2.2)

Thus for cap-one product inputs every two-dimensional orthogonal projection has joint density cap at most 2. No moment, support, log-concavity, smoothness, or post-rotation independence is assumed or inferred. If the source block itself has dimension two, the same cap is immediate from orthogonal change of variables (indeed cap <=1), so the k<n wording causes no endpoint gap.

### 2.3 Primary sharp convolution theorem: Juskevicius--Lee

T. Juskevicius, J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, Theorem 1 and Corollary 1.

For independent random vectors with maximum-density caps K_i, the maximum density of their sum is no larger than that of the corresponding independent centered uniform-ball variables with those caps. In dimension one this is the sharp Rogozin comparison.

For three independent cap-one real variables,

`Y=(X_1+X_2+X_3)/sqrt(3)`,

comparison with three centered unit uniforms gives

`||p_Y||_infinity <= R_0 := 3 sqrt(3)/4`.                      (2.3)

Indeed the density of the sum of three centered unit uniforms at zero is 3/4, and the normalization by 1/sqrt(3) multiplies the peak by sqrt(3).

### 2.4 Completed designated partner actually applied

Fleet03/B18 r21, source:

- math-open-problems commit `c7d99a5becf262e519f50bd221ab49c0bd807534`
- `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B18/20260923T005908Z-fleet03-B18-QFORM-r21/REPORT.md`.

For the target-valid family defined in Section 5 below, its capped-basis/mixed-volume certificate is

`A(r)=3 e ((1+r^2)/(2r))^(1/3)`                                   (2.4)

for every r>0, while full volume sampling gives `<=3e` for `0<r<=1`. The same report proves that for large shear no reweighting inside the capped-basis currency can remove the degeneration; hence a different analytic mechanism is genuinely required.

## 3. Density-cap scaling of the null-pivot kernel

### Lemma 3.1 — `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`

Let S be a real random variable with density cap K<infinity. Let (C,D) be independent of S and have an arbitrary joint probability density with cap M. For real alpha,delta and nonzero beta,gamma,

`Q=2 beta S C + alpha C^2 + 2 delta C D + gamma D^2`

satisfies

`boxed: ||p_Q||_infinity <= 3 (2 M K)^(2/3) |beta^2 gamma|^(-1/3).`   (3.1)

**Proof.** Put `X=K S`. Its density is `x -> K^(-1) p_S(x/K)`, hence is at most one. Rewriting S=X/K replaces beta in (2.1) by beta/K and changes no other coefficient or independence statement. Therefore

`||p_Q||_infinity <= 3(2M)^(2/3) |(beta/K)^2 gamma|^(-1/3)
                   = 3(2MK)^(2/3)|beta^2 gamma|^(-1/3)`.

No rotation of the input product law occurs. QED.

### Corollary 3.2 — LPP pays an extracted two-dimensional product projection

If `(C,D)=V^T X_J` is an orthogonal two-dimensional projection of an ORIGINAL-coordinate cap-one product block disjoint from S, then by (2.2) M<=2, so

`||p_Q||_infinity <= 3 (4K)^(2/3)|beta^2 gamma|^(-1/3).`             (3.2)

In particular, the exact-coloop endpoint of fleet02/B16, where K=1 and `|beta^2 gamma|=|det Lambda|>=1`, improves immediately to

`||p_Q||_infinity <= 3*4^(2/3)=7.559526299369239...`.                (3.3)

This is a source-valid constant improvement, not a new full-target closure.

## 4. Structural payoff criterion for the partner's unpaid step

Suppose a surviving Schur-isotropic branch can be represented, after grouping disjoint ORIGINAL coordinate sets but without declaring spectral coordinates independent, as

`Q=2 beta S C + alpha C^2 + 2 delta C D + gamma D^2 + Z`,

where the displayed triple is formed from one scalar aggregate S and one two-dimensional product projection `(C,D)`, S is independent of `(C,D)`, and any additional term Z has already been removed by legitimate conditioning or belongs to a separately convolved independent block. If

`K:=||p_S||_infinity <= K_0`,  `|beta^2 gamma|>=d_0>0`,

then the displayed nonlinear core is paid at

`3(4K_0)^(2/3)d_0^(-1/3)`                                           (4.1)

using LPP plus Lemma 3.1. Thus the analytic part of the partner's large-shear extraction problem is reduced to the genuinely structural task of producing a bounded-density aggregate and a determinant lower bound while preserving disjoint original-coordinate provenance.

The statement deliberately does not treat an arbitrary non-independent remainder as a convolution or a small perturbation.

## 5. Application: partner r21's extreme-shear family improves to 8.176374

Let the ten original variables be arbitrary independent cap-one laws and define three disjoint flat banks

`Y_1=(X_1+X_2+X_3)/sqrt(3)`,
`Y_2=(X_4+X_5+X_6)/sqrt(3)`,
`Y_3=(X_7+X_8+X_9)/sqrt(3)`.

For r>0 put

`S_r=(r X_0+Y_1)/sqrt(1+r^2)`,
`Q_r=2 S_r Y_2+Y_3^2`.                                             (5.1)

The partner proves that the physical matrix of Q_r has exactly the three nonzero eigenvalues {-1,1,1} for every r>0, so (5.1) is inside the owner's exact target class.

For r>=1, write `s=sqrt(1+r^2)`. The single summand `(r/s)X_0` has density cap `s/r`; convolution with the independent term `Y_1/s` cannot increase an L-infinity norm, hence

`K_r:=||p_{S_r}||_infinity <= s/r = sqrt(1+r^(-2)).`                 (5.2)

By the primary Juskevicius--Lee theorem and (2.3),

`||p_{Y_2}||_infinity, ||p_{Y_3}||_infinity <=R_0=3sqrt(3)/4`.

Because the two banks use disjoint original coordinates, they are genuinely independent, so the joint pair cap is

`M <= R_0^2 = 27/16`.                                               (5.3)

Apply Lemma 3.1 to (5.1) with beta=gamma=1 and alpha=delta=0. For every r>=1,

`C(r):=||p_{Q_r}||_infinity
 <=3(2*(27/16)*K_r)^(2/3)
 =(27/4)(1+r^(-2))^(1/3).`                                         (5.4)

This decreases from `(27/4)2^(1/3)=8.504467...` at r=1 to 27/4 as r tends to infinity.

The completed partner certificate (2.4)

`A(r)=3e((1+r^2)/(2r))^(1/3)`                                      (5.5)

is increasing for r>=1. At r=1 it equals `3e=8.154845...`, below C(1). The two curves meet exactly when

`27 e^3 (1+r^2)/(2r) = (27/4)^3 (1+r^(-2))`,

which after cancelling `1+r^2` gives

`r_* = 729/(32 e^3) = 1.1342116512554006...`.                       (5.6)

Hence

`sup_(r>=1) min(A(r),C(r)) = A(r_*)=C(r_*)
 = 8.176373542022445...`.                                           (5.7)

For 0<r<=1 the partner's full-volume certificate gives `||p_{Q_r}||_infinity<=3e<8.176374`. Therefore

`boxed: sup_(r>0) ||p_{Q_r}||_infinity <= 8.176373543.`              (5.8)

This improves the partner's previous uniform essential bound `27/2^(4/3)=10.714957...` for this target-valid family. The partner's aggregate-pivot theorem still independently supplies continuity (with its weaker continuous bound); the new 8.176374 certificate is asserted here only as an essential-density bound.

## 6. What this changes and what remains open

The full conjecture remains OPEN. The new transfer does two things that are genuinely useful to the live proof map:

1. It turns the partner's qualitative large-shear extraction target into the explicit payoff (4.1), using a primary theorem whose hypotheses exactly match the original product source.
2. On the explicit family where capped-basis entropy is provably insufficient, it combines the completed partner certificate with the null-pivot kernel and a sharp primary rearrangement theorem to improve the uniform bound from 10.715 to 8.176374. Thus the entropy barrier is a barrier only to that certificate, not to bounded density.

The first unpaid implication is still structural: for an arbitrary Schur-isotropic large-shear survivor, produce the required disjoint-coordinate aggregate/projection factorization with K=O(1) and `|beta^2 gamma|` bounded below, or prove that failure forces one of the existing heavy-row, physical-pair, ridge-window, or volume-tail exits. A fixed good minor may not be assumed, and no post-rotation independence is available.

## 7. Source/correction status

Consumed live corrections include: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no arbitrary-joint rank-three coarea bound; no worst conditional-projection-density moment/supremum; no universal single good physical minor; no universal rank-three cross cut; and no replacement of a non-independent remainder by an independent convolution.

Primary-source search misses were not used as novelty evidence. Every theorem used above is either source-matched at its exact hypotheses or an explicitly pinned completed worker theorem. No hidden moment, support, log-concavity, Gaussian, or continuity assumption enters the essential-density estimates.
