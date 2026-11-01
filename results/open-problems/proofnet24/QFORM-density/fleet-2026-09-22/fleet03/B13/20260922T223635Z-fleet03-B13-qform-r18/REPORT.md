SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B13, 2026-09-22T22:36:35Z.
attacking: the extremal-product interface itself, repairing nonattainment and reducing the full essential-density constant to a countable rational finite-grid geometric slab problem without any interval/diameter/fragment-count assumption.

# fleet03/B13 r18 — rational finite-grid witness reduction for the full QFORM slab constant

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Run:** `20260922T223635Z-fleet03-B13-qform-r18`  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET-LEVEL EXTREMAL REDUCTION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction-aware starting point

For each finite `n`, let `D_n` be the product probability laws on `R^n` whose one-dimensional densities satisfy `0<=f_i<=1` and `int f_i=1`. For a real symmetric matrix `A`, write

`q_A(x)=x^T A x`,

and let `s_3(A)` be the third largest singular value of `A`, equivalently the third largest absolute eigenvalue because `A` is symmetric. The owner target is the finiteness of

`C_all := sup P_mu{q_A(X) in I}/|I|`,                         (1.1)

where the supremum ranges over every finite `n`, every `mu in D_n`, every real symmetric `A` with `s_3(A)>=1`, and every nondegenerate bounded interval `I`.

The full conjecture remains OPEN. This run does not use the false law-uniform pointwise quadratic-phase decay, the false arbitrary-joint rank-three coarea lemma, a worst conditional-fiber density, post-rotation independence, a fixed physical minor, a centered interval law, a bounded support diameter, or a uniform fragment-count bound.

There is a fresh source correction relevant specifically to B13. The later fleet04/B13 infinite-space threshold/bathtub argument can fail to attain its threshold: `w(x)=1-exp(-|x|)` is an explicit nonattainment example. The reviewed repair is fleet04/B14's finite-mixture localization. I therefore do **not** use global threshold attainment.

Two compatible completed partner inputs are used at their proved scopes:

1. **Designated partner fleet04/B13, fixed-volume random-set representation**: `yspennstate/math-open-problems@7229e8caa8374eb8e74b07e70cadd0c0ccb05d39`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260922T171018Z-b13-fixed-volume-mixture-r4/REPORT.md`. It gives an exact barycentric representation of every cap-one marginal by unit-measure indicator laws, hence an exact product mixture and an exact transfer of any common extreme-product slab inequality. It also gives the valid continuity-transfer statement when every arbitrary extreme component has a continuous density with one common bound.
2. **Nonattainment repair, fleet04/B14 finite-mixture localization**: `yspennstate/math-open-problems@321ec7899f4972d125d641408512fe9e5e9dcf4c`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260922T201507Z-fleet04-B14-mixture-localization-r4/REPORT.md`. It approximates every cap-one marginal in `L^1` by finite convex mixtures of indicators of compact finite unions of equal-grid intervals of total length one, with product total-variation convergence.

The second theorem supplies the safe finite-grid approximation used below; the first is the designated-partner theorem actually applied to the slab functional.

## 2. The countable extreme class

For each `n`, let `G_n` consist of data `(B,E_1,...,E_n,J)` satisfying:

- `B in Sym_n(Q)` is a rational symmetric matrix and `s_3(B)>1`;
- `J=[u,v]` has rational endpoints `u<v`;
- for each `i`, there is an integer `M_i>=1` such that `E_i` is a finite union of half-open cells
  `[k/M_i,(k+1)/M_i)` with integer `k`, and exactly `M_i` cells are selected, so `|E_i|=1`.

Let `U_i` be independent with density `1_{E_i}` and define

`C_grid := sup_(n,G_n) P{U^T B U in J}/|J|`.                  (2.1)

The class is countable. Importantly, the integers `M_i`, support radii, numbers of connected components, translations and gaps are **not** bounded uniformly.

## 3. Main theorem — exact equality of the full and rational-grid constants

### Theorem 3.1 — `QFORM-COUNTABLE-EXTREME-WITNESS-v1`

`boxed: C_all = C_grid.`                                      (3.1)

Equivalently, the full essential-density conjecture is true with constant `C` if and only if the geometric inequality

`|{x in E_1 x ... x E_n : x^T B x in J}| <= C |J|`           (3.2)

holds for every datum in the countable class `G_n` and every `n`.

More quantitatively, if an admissible datum has slab ratio `R`, then for every `epsilon>0` there is a rational finite-grid datum in some `G_n` with slab ratio at least `R-epsilon`.

### Proof

The inequality `C_grid<=C_all` is immediate: every `1_{E_i}` is an admissible cap-one probability density and every matrix with `s_3(B)>1` is in the owner's target class.

For the reverse inequality, fix one arbitrary admissible datum `(A,mu,I)` with

`I=[t,t+h]`, `h>0`,
`p=P_mu{q_A(X) in I}`,
`R=p/h`,                                                         (3.3)

and fix `epsilon>0`. It is enough to produce a datum in the countable class with ratio `>R-epsilon`.

#### Step 1: create a strict spectral cushion without changing the event

Choose `s>1` so close to one that

`R/s > R-epsilon/4`.                                           (3.4)

Put

`A_s=sA`, `I_s=sI=[st,s(t+h)]`.

Then

`{q_(A_s)(X) in I_s}={q_A(X) in I}`                           (3.5)

exactly, while `|I_s|=s h` and

`s_3(A_s)=s s_3(A)>=s>1`.                                     (3.6)

Thus the spectral threshold now has a genuine open cushion.

#### Step 2: replace the rough product law by one compact rational-grid product indicator

Apply the completed fleet04/B14 finite-mixture theorem to every marginal. It may be implemented on the standard rational mesh `{[k/M,(k+1)/M):k in Z}`: truncate the law with arbitrarily small `L^1` loss, take the grid conditional expectation, and use the hypersimplex identity

`{a in [0,1]^N : sum_j a_j=M}
 = conv{v in {0,1}^N : sum_j v_j=M}`.                          (3.7)

Hence, for arbitrarily small `delta>0`, there is a finite convex mixture of compact rational-grid product-indicator laws whose product density is within `delta` in `L^1` (and therefore in total variation) of `mu`. Choose `delta` so that the slab probability of the mixture is at least

`p-delta > p-(epsilon/8) s h`.                                 (3.8)

The slab probability of that finite mixture is a convex average of the slab probabilities of its product-indicator components. Therefore at least one component, say `E=E_1 x ... x E_n`, satisfies

`P_E{q_(A_s)(U) in I_s} >= p-delta`.                           (3.9)

Each `E_i` is compact up to harmless endpoint choices, is a finite union of rational-grid cells, and has exactly unit measure. This is a supremum/approximation argument, not a claim that an infinite-space bathtub maximizer exists.

The designated fleet04/B13 theorem is applied here at the actual slab functional

`H_I(x)=1_{q_(A_s)(x) in I_s}`.                               (3.10)

Its fixed-volume product-mixture identity proves that uniform slab inequalities on arbitrary unit-measure extreme products average with zero constant loss to every cap-one product law; the B14 finite-mixture theorem refines that exact extreme class to the compact rational-grid approximating class needed for the present countable reduction.

#### Step 3: rationalize the matrix without losing the target or the event

Let `K=E_1 x ... x E_n`. It is bounded. Choose `L<infinity` such that

`||x||_2 <= L` for every `x in K`.                             (3.11)

Pick `eta>0`, to be fixed below. Rational symmetric matrices are dense, so choose `B in Sym_n(Q)` satisfying

`||B-A_s||_op < min{ (s-1)/2, eta/L^2 }`.                     (3.12)

Weyl's singular-value inequality gives

`s_3(B) >= s_3(A_s)-||B-A_s||_op
        > s-(s-1)/2
        =(s+1)/2>1`.                                           (3.13)

Also, uniformly for `x in K`,

`|x^T(B-A_s)x| <= ||B-A_s||_op ||x||_2^2 < eta`.               (3.14)

Consequently

`{x in K:q_(A_s)(x) in I_s}
 subset {x in K:q_B(x) in I_s+[-eta,eta]}`.                    (3.15)

No continuity of a level-set density is needed for this containment.

#### Step 4: rationalize the interval and control the denominator

Choose rational `u<v` such that

`I_s+[-eta,eta] subset J=[u,v]`                               (3.16)

and

`|J| < s h+2eta+zeta`                                         (3.17)

for an arbitrarily small `zeta>0`. By (3.9) and (3.15),

`P_E{q_B(U) in J} >= p-delta`.                                 (3.18)

Choose `eta,zeta` so small that

`(p-delta)/(s h+2eta+zeta) > R-epsilon`.                       (3.19)

This is possible because `(p-delta)/(s h)>R-epsilon/2` after first taking `s` and `delta` sufficiently close/small. The resulting `(B,E_1,...,E_n,J)` lies in the countable class and has ratio `>R-epsilon`.

Since the original datum and `epsilon` were arbitrary, `C_grid>=C_all`. Together with the easy reverse inequality this proves (3.1). QED.

## 4. Strict counterexample witnesses become finite rational data

### Corollary 4.1

Fix any proposed finite constant `C`. If there is any admissible target datum with

`P{X^T A X in I} > C |I|`,                                    (4.1)

then there is a witness with all of the following simultaneously:

- `B` rational symmetric;
- `s_3(B)>1` strictly;
- `J` with rational endpoints;
- every marginal equal to the indicator of a compact finite union of rational intervals of total length one;
- `P{U^T B U in J}>C|J|`.

Proof: let `R` be the strict ratio in (4.1) and apply Theorem 3.1 with `epsilon<(R-C)/2`. QED.

Therefore, if the universal conjecture is false (`C_all=infinity`), there is a sequence of fully finite rational-grid witnesses with ratios tending to infinity. This does not assert that a single input law must itself have an unbounded density.

This is useful for rigorous computation: any **strict** numerical candidate violation can in principle be replaced by finite exact input data before certification. It does not make the infinite supremum decidable, and failure to find such a witness is not a proof.

## 5. Geometric consequence and relation to the live near-null gap

The theorem eliminates two artificial issues from the geometric route:

1. fractional densities need not be treated separately for the essential bound;
2. unbounded/infinite-fragment supports need not be assumed away — they can be approximated by finite rational-grid supports, but with **no uniform bound** on radius or fragment count.

Thus the actual remaining geometric target can be stated on a countable class:

`sup_(n,G_n) |{x in product E_i:q_B(x) in J}|/|J| < infinity`. (5.1)

This is still the same hard problem. In particular it does not upgrade the previous B13 near-null theorem

`P{Q in I} <= 19.760331 sqrt(|I|)`                             (5.2)

to the required linear bound. What it does show is that any strict failure of the desired linear inequality, including in any open spectral collar, may be witnessed after compact rational-grid extremalization rather than by an inaccessible rough law.

The fresh fleet02/B13 same-extreme Fourier-power theorem is compatible with this reduction: positive Fourier-power functionals can also be extremalized to one common finite-fragment product law. Its four-copy linear slab theorem does **not** deconvolve to a one-copy bound; the rank-one square singularity is an explicit control showing why. I do not make that invalid inference here.

## 6. Continuity is logically separate

The equality `C_all=C_grid` proves an equivalence only for the essential `L^infinity`/linear-small-ball constant. Total-variation limits of continuous densities need not be continuous, so the finite-grid reduction alone does not prove the owner's additional continuity request.

Here the designated fleet04/B13 exact fixed-volume mixture is stronger: if every arbitrary unit-measure extreme product law in the full target has a continuous density bounded by one common `C`, its exact barycentric representation and dominated convergence transfer a continuous density with the same bound to every cap-one product law. Thus:

- essential-density target: it suffices to prove the countable rational-grid geometric inequality (3.2);
- continuity target: the currently valid transfer is from **all arbitrary unit-measure extreme products**, unless a future theorem supplies a uniform modulus allowing finite-grid approximation.

Full continuity remains OPEN.

## 7. Deterministic finite check

The accompanying checker implements the exact pairwise dependent-rounding recursion for rational hypersimplex points. For four nontrivial rational test vectors it verifies, using `fractions.Fraction`, that:

- every output vertex is 0/1 with exactly the prescribed integer number of selected cells;
- all convex weights are positive and sum exactly to one;
- the exact weighted reconstruction equals the input vector coordinate by coordinate.

It terminates with `QFORM_B13_R18_HYPERSIMPLEX_CHECK_PASS`. This finite check is only a regression check for the finite-dimensional decomposition; the theorem is the proof above.

## 8. Status and next implication

- `QFORM-COUNTABLE-EXTREME-WITNESS-v1`: **PROVED**.
- fleet04/B13 fixed-volume product mixture: **APPLIED TO THE ACTUAL QFORM SLAB FUNCTIONAL**.
- later threshold-attainment version: **NOT USED** because of the reviewed nonattainment correction.
- fleet04/B14 finite-mixture localization: **APPLIED** to obtain the rational finite-grid refinement.
- full QFORM essential-density conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- full continuity conclusion: **OPEN**.

The next target-relevant B13 implication remains the one-copy geometry, now safely restricted at the supremum level to finite rational-grid products: combine the one-heavy/two-cross-bank collar with same-bank transverse curvature to prove

`|{x in product E_i:q_B(x) in J}| <= C |J|`                   (8.1)

with a constant independent of mesh, radius, translations, gaps and fragment count. A proof that depends on any of those approximation parameters does not pass to the full target.
