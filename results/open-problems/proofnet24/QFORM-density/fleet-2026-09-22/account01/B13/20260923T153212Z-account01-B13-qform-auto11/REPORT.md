SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B13, 2026-09-23T15:32:12Z.
attacking: leverage-cascade/anchored-volume closure using the latest account02/B13 result, while preserving the exact extremal-product reduction.

# account01/B13 — exterior-volume marginals force a genuine physical pivot

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: extremal product laws / analytic derivation and exact structural identities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full continuity: **OPEN**.

## 1. Sources and corrections consumed


The argument below does **not** use any of the known-invalid interfaces: no law-uniform pointwise quadratic oscillatory decay, no independence after rotation, no arbitrary-joint coarea bound, no conditional projection-density moment bound, no single-interval/centered-uniform extremality, and no bounded fragment-count or bounded-diameter reduction.

The designated partner result actually applied is account02/B13 r29:

`yspennstate/math-open-problems@6d77eb1e452afcd8c4f779344b5602118223d42a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T145505Z-account02-B13-leveragecascade-r29/REPORT.md`.

Its exact input used below is Theorem 7.1 (`QFORM-FIVE-DEEP-STAR-TO-BIHUB-v1`). For an actual symmetric physical leaf block `R`, spectral projection `P_tau=1_{|R|>=tau}`, and a five-deep leverage set `H`, if an actual slab ratio `rho` satisfies

`rho > C_*/tau`,  with  `C_* = 16 sqrt(60 pi)`,                         (1.1)

then for the actual physical cross block

`M = R[H,H^c]`                                                       (1.2)

one has

`s_3(M) > tau sqrt(3/128)`,                                         (1.3)

and the natural squared-3-minor volume law has a physical row marginal `>2/3` and a physical column marginal `>2/3`. The partner also proves more than one third of the squared 3-minor mass is jointly anchored on such a row/column pair. I only need the column marginal for the new pivot extraction.

## 2. Exact extremal-product reduction, with no shape claim

Let

`F = { f:R-> [0,1] measurable : integral f = 1 }`.

For every nonnegative measurable kernel `K:R^n->[0,infinity]`,

`sup_{f_1,...,f_n in F} integral K(x) prod_i f_i(x_i) dx`

` = sup_{|E_1|=...=|E_n|=1} integral_{prod_i E_i} K(x) dx`.           (2.1)

### Proof

For a fixed nonnegative measurable `g` on `R`, the one-dimensional bathtub principle gives

`sup_{f in F} integral g f = sup_{|E|=1} integral_E g`.              (2.2)

For bounded `g`, choose a threshold `t` for its decreasing rearrangement: take all of `{g>t}` and, if needed, a measurable subset of `{g=t}` to make total measure one. Replacing any fractional mass of `f` below that threshold by unused capacity above it cannot decrease the integral. For general nonnegative `g`, apply the bounded statement to `min(g,m)` and let `m` increase to infinity.

Now freeze `f_2,...,f_n` and apply (2.2) to the function obtained by integrating `K` in the other coordinates. Then freeze the first indicator and optimize the second coordinate, and continue. Tonelli applies because the kernel is nonnegative. This proves (2.1) without asserting attainment of the full product supremum.

For the QFORM slab kernel

`K(x)=1_{x^T A x in J}`,                                             (2.3)

(2.1) says that a universal geometric inequality for arbitrary unit-measure product sets is exactly enough for arbitrary independent cap-one laws.

Moreover, for this bounded kernel the supremum is unchanged if each `E_i` is required to be a bounded finite union of intervals. Indeed, by regularity of Lebesgue measure every finite-measure set can be approximated in symmetric difference by such a set of the same measure; and

`| prod_i E_i triangle prod_i F_i | <= sum_i |E_i triangle F_i|`      (2.4)

when all factors have measure one. Thus slab integrals converge. The number of components and the diameter are **not uniform** and may diverge along the approximation. Nothing here implies a single interval or a centered uniform law is extremal.

## 3. A general exterior-volume marginal energy theorem

This is the new exact structural lemma.

Let `M` be a real `p x q` matrix of rank at least `k`. Put

`Z_k(M)=e_k(M^T M)`

`       = sum_{|S|=|T|=k} det(M[S,T])^2`.                           (3.1)

Use the normalized weights

`w_{S,T}=det(M[S,T])^2/Z_k(M)`.                                    (3.2)

Let

`alpha_i = sum_{S contains i,T} w_{S,T}`,                           (3.3)

`beta_j  = sum_{S,T contains j} w_{S,T}`                            (3.4)

be the row and column volume marginals. If `s_k(M)` is the k-th singular value, then

`boxed: alpha_i <= k ||M[i,:]||_2^2 / s_k(M)^2`,                    (3.5)

`boxed: beta_j  <= k ||M[:,j]||_2^2 / s_k(M)^2`.                    (3.6)

### Proof

Write an SVD

`M=U diag(sqrt(lambda_1),...,sqrt(lambda_r)) V^T`,

with `lambda_1>=...>=lambda_r>0`; thus `lambda_k=s_k(M)^2`.

After summing over column subsets by Cauchy--Binet, the row-subset law has weights

`det((MM^T)[S,S])/e_k(lambda)`.

Expanding in the eigenbasis shows that its marginal kernel is

`Pi_k^row = U diag(pi_1,...,pi_r) U^T`,                              (3.7)

where

`pi_a = lambda_a e_{k-1}(lambda without lambda_a)/e_k(lambda)`.      (3.8)

For completeness, the elementary symmetric polynomials satisfy

`k e_k(lambda)`
` = sum_{|T|=k-1} (prod_{a in T} lambda_a) sum_{b notin T} lambda_b`
` >= lambda_k e_{k-1}(lambda)`.                                    (3.9)

The inequality holds because a `(k-1)`-set misses at least one of the top `k` indices, whose eigenvalue is at least `lambda_k`. Hence

`pi_a <= lambda_a e_{k-1}(lambda)/e_k(lambda)`
`     <= k lambda_a/lambda_k`.                                     (3.10)

Therefore, in PSD order,

`Pi_k^row <= (k/lambda_k) MM^T`.                                   (3.11)

Taking the `i`-th diagonal gives (3.5). Applying the same argument to `M^T` gives (3.6). No probabilistic independence and no rotated random variables enter; this is a deterministic identity/inequality for physical coefficient blocks.

### Pinned-column identity

A useful exact refinement, not needed for the main pivot constant, is the following. Fix a column `j`, let `v=M[:,j]`, and let

`N=P_{v^perp} M[:,{columns except j}]`.

Then Gram-Schur factorization and Cauchy--Binet give

`boxed: beta_j Z_k(M) = ||v||_2^2 e_{k-1}(N^T N)`.                  (3.12)

Thus a large exterior-volume column marginal is not merely combinatorial: it is exactly a product of physical column energy and a transverse `(k-1)`-volume.

## 4. Apply the partner's five-deep bi-hub to an actual inequality

Now take the exact partner situation (1.1)--(1.3). Here `M` has exactly five physical rows because `|H|=5`, and `k=3`.

The partner theorem supplies an actual physical column `j in H^c` with

`beta_j > 2/3`.                                                     (4.1)

Apply (3.6):

`2/3 < beta_j <= 3 ||M[:,j]||_2^2/s_3(M)^2`,

so

`||M[:,j]||_2^2 > (2/9) s_3(M)^2`.                                (4.2)

Using the partner's quantitative cross singular value (1.3),

`||M[:,j]||_2^2 > (2/9)(3/128) tau^2 = tau^2/192`.                (4.3)

Because this column has only five entries, some physical `g in H` satisfies

`boxed: |R_{g j}| = |M_{g j}| > tau/sqrt(960)`.                    (4.4)

This is an actual original-coordinate coefficient; no spectral rotation has been made.

## 5. Exact scalar-or-indefinite-pair dichotomy

Put

`m=R_{g j}`, `a=R_{gg}`, `c=R_{jj}`,

and consider the genuine physical `2 x 2` principal block

`B=[[a,m],[m,c]]`.                                                  (5.1)

There are two exhaustive cases.

### Case A: a scalar pivot is already large

If

`max(|a|,|c|) >= |m|/2`,                                          (5.2)

then by (4.4) there is an original-coordinate scalar pivot with

`boxed: max(|R_{gg}|,|R_{jj}|) > tau/sqrt(3840)`.                  (5.3)

### Case B: both scalar diagonals are small

If

`|a|,|c| < |m|/2`,                                                 (5.4)

then

`det B = ac-m^2 <0`,                                               (5.5)

and more quantitatively

`|det B| > (3/4)m^2`.                                              (5.6)

Also the operator norm is bounded by the maximum absolute row sum,

`||B||_op < (3/2)|m|`.                                             (5.7)

Since the product of the two singular values is `|det B|`,

`sigma_min(B)=|det B|/sigma_max(B) > |m|/2`.                       (5.8)

Therefore

`boxed: B is invertible indefinite and sigma_min(B) > tau/sqrt(3840)`. (5.9)

The split at `1/2` is optimal for this elementary dichotomy: if the scalar threshold is `theta |m|`, the complementary pair lower bound is `(1-theta)|m|`, and `min(theta,1-theta)` is maximized at `theta=1/2`.

## 6. Main new consequence: five-deep high ratio cannot remain pivotless

### Theorem — `QFORM-FIVE-DEEP-BIHUB-TO-PHYSICAL-PIVOT-v1`

Let `rho` be an actual QFORM slab ratio. Let `R` be an actual physical symmetric leaf block and `P_tau=1_{|R|>=tau}`. Suppose the partner's leverage peeling reaches five physical centers `H` and

`rho > 16 sqrt(60 pi)/tau`.                                       (6.1)

Then there are physical coordinates `g in H`, `j in H^c` such that **either**

1. a genuine original-coordinate scalar pivot satisfies

   `max(|R_{gg}|,|R_{jj}|) > tau/sqrt(3840)`,                     (6.2)

**or**

2. the genuine original-coordinate pair `R[{g,j},{g,j}]` is invertible indefinite and

   `sigma_min(R[{g,j},{g,j}]) > tau/sqrt(3840)`.                  (6.3)

In the self-normalized form, because

`16 sqrt(60 pi)/sqrt(3840) = 2 sqrt(pi)`,                          (6.4)

(6.1) implies that the scalar/pair pivot furnished above has scale

`boxed: > 2 sqrt(pi)/rho`.                                        (6.5)

This is a target-level structural consequence for arbitrary cap-one product laws. By Section 2 it equivalently holds when testing arbitrary measurable unit-product indicators, and bounded finite-union indicators suffice by approximation with no uniform fragment/diameter control.

### Interpretation

The partner r29 left three outcomes at a spectral scale `tau`: termination after at most four high-leverage physical centers, residual projection rank below three, or a five-deep branch producing a third-volume bi-hub. The theorem above removes the possibility that the five-deep branch is simultaneously **physically pivotless**. A fifth high-leverage center at a scale above `16sqrt(60pi)/rho` necessarily produces either a real scalar Schur pivot or an invertible indefinite physical pair, in the original coordinates.

At any fixed `tau>0`, a sequence with `rho -> infinity` that enters the five-deep branch therefore has a **fixed-scale** physical pivot `>tau/sqrt(3840)` for all sufficiently large ratios. The near-zero physical-pivot obstruction can survive only in the partner's at-most-four-center / residual-rank-below-three alternatives.

## 7. What is still unpaid

This is **not** the full QFORM theorem. A physical pivot by itself does not permit deleting the higher-rank Schur remainder, and congruence/Schur elimination does not automatically preserve two large spectral magnitudes at a universal scale. The remaining implication is now

`QFORM-FOUR-CENTER-OR-PIVOT-SCHUR-CLOSURE-v1`:

> combine the partner's at-most-four-center/rank-below-three branch with the new physical-pivot theorem, and in the pivot branch transport enough exterior-volume or fractional-trace currency through the genuine scalar/pair Schur complement to invoke an already-paid rank-two affine-half-Riesz, pair-log, ridge, or grouped-coordinate receiver, without rotating product variables or discarding the residual as a small random perturbation.

The exact pinned identity (3.12) is the natural next interface: the high-volume physical column is accompanied by a transverse order-two exterior volume before any inversion. The next run should try to transport that identity through the actual scalar/pair Schur complement rather than repeat the leverage cascade.

## 8. Status

Full QFORM: **OPEN**.  
Continuity: **OPEN**.  
New proved supporting results this run:

* exact extremal-product supremum reduction (restated with proof and finite-union approximation scope);
* `QFORM-EXTERIOR-MARGINAL-ENERGY-v1`, equations (3.5)--(3.6), all exterior orders `k`;
* exact pinned-column identity (3.12);
* `QFORM-FIVE-DEEP-BIHUB-TO-PHYSICAL-PIVOT-v1`, equations (6.2)--(6.5), obtained by applying the completed account02/B13 partner theorem to an actual inequality.

A brute-force diagnostic over random small matrices numerically checked the order-three marginal bound; it is not used in the proof. No counterexample to QFORM was found.
