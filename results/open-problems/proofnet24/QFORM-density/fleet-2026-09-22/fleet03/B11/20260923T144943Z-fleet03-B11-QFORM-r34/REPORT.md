SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T14:49:43Z.
attacking: exact-rank-three indefinite diffuse-leverage geometry via determinantal-triple disjointness, a literal original-coordinate cut, and grouped rank-three cross smoothing.

# fleet03/B11 r34 — a 1/3-leverage exact-rank-three exit

## Status

This run proves a new target-valid supporting theorem for genuinely rotated exact-rank-three signatures `(2,1)` and `(1,2)`. It converts diffuse spectral leverage directly into one literal original-coordinate cut whose physical cross block has quantitative rank-three singular volume. The completed grouped-cross theorem then gives a bounded continuous density.

The full QFORM conjecture remains OPEN because arbitrary additional nonseparable spectrum is not removed here, and the exact-rank-three branch with a physical spectral leverage at least `1/3` remains outside the new theorem. No continuity claim is made beyond the branch actually covered below.

Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Inputs actually used


The analytic compiler used below is the completed fleet03/B09 theorem
`QFORM-GROUPED-CROSS-RANK-r-SMOOTHING-v1`, canonical source
`yspennstate/math-open-problems`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T104947Z-fleet03-B09-QFORM-r30/REPORT.md`.
For a disjoint original-coordinate cut with physical cross block `B` of rank `r>2`,

`||p_Q||_inf <= e r/(r-2) Delta_r(B)^(-1/r)`,

where `Delta_r(B)` is the product of the nonzero singular values. Same-side quadratic terms and all affine terms are arbitrary, and the density is continuous.

The designated partner fleet04/B11 result actually applied below is
`QFORM-EXTENSION-MASS-SECOND-MOMENT-v1`, canonical source
`yspennstate/math-open-problems@30555c1ca97752e10f5089ccd95f8514c704be5a`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260923T131400Z-fleet04-B11-extension-mass-r6/REPORT.md`.

## 2. Setup

Assume for this theorem that the full matrix has exact rank three,

`A = R M R^T`,  `R^T R = I_3`,

with `M` real symmetric invertible. For the assigned indefinite cases its signature is `(2,1)` or `(1,2)`. Put

`s = min_a |lambda_a(M)| > 0`,
`c_i = ||r_i||_2^2`,  `q = max_i c_i`,

where `r_i^T` is row `i` of `R`.

For each physical triple `K`, define

`v_K = det(R_K)^2`.

Cauchy--Binet gives

`sum_{|K|=3} v_K = det(R^T R)=1`.                         (2.1)

Thus `v_K` is a probability distribution on physical triples. Its one-coordinate inclusion marginals are exactly the frame leverages:

`sum_{K contains i} v_K = c_i`.                            (2.2)

One proof of (2.2) is the projection-DPP identity; elementarily, expand `det(R^T D R)` to first order when the `i`th diagonal weight in `D` is varied.

## 3. New deterministic theorem — disjoint determinantal triples force a cross cut

Let `K,L` be independent random triples with law `v`. Define

`D = P(K cap L = emptyset)`.

### Lemma 3.1 — disjoint-mass lower bound

`boxed: D >= 1 - sum_i c_i^2 >= 1-3q.`                    (3.1)

### Proof

By the union bound,

`P(K cap L != emptyset) <= E |K cap L|`.

Independence and (2.2) give

`E |K cap L| = sum_i P(i in K)P(i in L)=sum_i c_i^2`.

Finally `sum_i c_i=3`, hence

`sum_i c_i^2 <= q sum_i c_i = 3q`.

This proves (3.1). QED.

### Lemma 3.2 — one literal source-coordinate cut

There exists a partition of the ORIGINAL coordinates

`[n]=S disjoint_union T`

such that, with

`G_S=R_S^T R_S`, `G_T=R_T^T R_T=I-G_S`,

one has

`boxed: det(G_S) det(G_T) >= D/64.`                         (3.2)

### Proof

Choose a Bernoulli half-cut: every original coordinate is placed in `S` independently with probability `1/2`, with `T` its complement. Cauchy--Binet gives

`det G_S = sum_{K subset S, |K|=3} v_K`,
`det G_T = sum_{L subset T, |L|=3} v_L`.

Therefore

`E[det G_S det G_T]
 = sum_{K,L} v_K v_L P(K subset S, L subset T)`.

The probability is zero unless `K,L` are disjoint. If they are disjoint, their six distinct coordinates must receive prescribed colors, so the probability is exactly `2^(-6)=1/64`. Hence

`E[det G_S det G_T]=D/64`.

Some literal cut attains at least its expectation. QED.

## 4. Cross singular volume identity

For the cut from Lemma 3.2, let

`B=A[S,T]=R_S M R_T^T`.

Because `B` has rank at most three, its squared rank-three singular volume is

`Delta_3(B)^2 = e_3(B B^T)`.

Cauchy--Binet on all physical `3 x 3` cross minors gives the exact factorization

`boxed:
Delta_3(B)^2
 = |det M|^2 det(G_S)det(G_T).`                             (4.1)

Indeed

`det B[I,J]=det(R_I) det(M) det(R_J)`

for `I subset S`, `J subset T`, `|I|=|J|=3`; summing the squares factors into the two Cauchy--Binet sums.

Combining (3.1), (3.2), and `|det M|>=s^3` yields

`boxed:
Delta_3(B)
 >= (s^3/8) sqrt(1-3q),`                                    (4.2)

whenever `q<1/3`. In particular the cut has actual physical cross rank three.

## 5. Density theorem for the diffuse exact-rank-three branch

Apply `QFORM-GROUPED-CROSS-RANK-r-SMOOTHING-v1` with `r=3` to the literal source-coordinate cut from Section 4. The two banks are disjoint sets of original independent coordinates, so no post-rotation independence is used. Equations (4.2) and the grouped-cross theorem give

`||p_Q||_inf
 <= 3e Delta_3(B)^(-1/3)
 <= 6e/[s (1-3q)^(1/6)].`

Thus:

### Theorem `QFORM-EXACT-RANK3-DIFFUSE-LEVERAGE-CROSS-CUT-v1`

For every exact-rank-three target

`A=RMR^T`, `R^TR=I_3`, `min |lambda(M)|=s`,

of signature `(2,1)` or `(1,2)` (indeed, for any invertible signature), if

`q=max_i ||r_i||^2 <1/3`,

then `Q=X^TAX` has a continuous density satisfying

`boxed:
||p_Q||_inf <= 6e s^(-1) (1-3q)^(-1/6).`                    (5.1)

No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis assumption, or pointwise one-dimensional oscillatory decay is used.

A convenient fixed threshold is `q<=1/4`. Then

`1-3q>=1/4`

and

`boxed:
||p_Q||_inf <= 6e 4^(1/6)/s
 = 6e 2^(1/3)/s
 = 20.5489229713.../s.`                                     (5.2)

For the target normalization `s>=1`, this is `<20.549`.

This substantially enlarges the previously paid very-diffuse leverage window: the remaining exact-rank-three obstruction is now confined to a physical coordinate with leverage at least `1/3` if one lets the constant in (5.1) vary with the gap to `1/3`, or at least `1/4` if one uses the clean fixed constant (5.2).

## 6. Why the third direction removes the rank-two logarithm in this branch

For independent centered unit uniforms,

`T=2XY`

has

`p_T(t)=log(1/(2|t|))`,  `0<|t|<1/2`,

so opposite-sign rank two has a genuine logarithmic singularity.

The new argument identifies the third direction without rotating the product law. The determinantal triple distribution finds a literal cut `S|T` with three nonzero singular directions in the physical cross block. The grouped-cross proof then works jointly on the two independent original-coordinate banks and gives

`|phi_Q(t)| <= C |t|^(-3/2)`

by a single `L^2`/Plancherel calculation in the three-dimensional grouped cross variable. This is integrable. With only two cross directions the same calculation gives the endpoint `|t|^(-1)`, exactly the logarithmic failure. Thus the smoothing here is genuinely a three-direction joint effect, not a false product of three pointwise van-der-Corput factors.

## 7. Designated partner fleet04/B11 applied to an actual inequality

Use the genuinely rotated Parseval tetrahedral frame

`R=(1/2) [[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]]`

and `M=diag(1,1,-1)`. Then `R^TR=I`, every row leverage is `3/4`, and

`A=RMR^T
 = [[1/4,1/4,1/4,-3/4],
    [1/4,1/4,-3/4,1/4],
    [1/4,-3/4,1/4,1/4],
    [-3/4,1/4,1/4,1/4]].`

For the physical pair `S={1,4}`,

`g_S=||r_1 cross r_4||^2=1/2`,
`|det M|=1`.

The two extensions `k=2,3` each have

`d_{S,k}=|det A[S union {k},S union {k}]|=1/4`.

Hence the partner identity gives the actual overlap-two star value

`W_2(S)=(1/2)^2-2(1/4)^2=1/8.`                              (7.1)

The same completed partner report contains the area-compiler inequality

`||p_Q||_inf <=128 sqrt(2)/(s sqrt(g_S)).`

Here `s=1`, so this specific rotated indefinite form satisfies

`boxed: ||p_Q||_inf <=256.`                                  (7.2)

This bound is intentionally not advertised as sharp; it is an actual application of the designated partner result to the high-leverage complement, where the new diffuse theorem does not apply because `q=3/4`.

## 8. What remains

For exact rank three, the new theorem reduces B11's genuinely hard indefinite geometry to the **heavy-leverage branch** `max_i ||r_i||^2 >=1/3` (or `>=1/4` for the fixed `<20.549` exit). If the corresponding physical diagonal is not small, the existing scalar-Schur/half-Riesz branch is already available. The sharp remaining B11 step is therefore the heavy **near-null** physical coordinate: aggregate its star and residual two-plane curvature without paying one tiny minor.

For the full owner target, arbitrary additional nonseparable spectrum is still a separate bridge. The exact-rank-three theorem above cannot simply be applied to a selected spectral three-frame after discarding the rest, because the omitted quadratic part is not independent noise.

Continuity is proved in the branch (5.1) through the grouped-cross Fourier compiler. The unrestricted full-target continuity statement remains OPEN.

## 9. Verification scope

The accompanying deterministic checker verifies:

1. the tetrahedral frame is Parseval;
2. its leverage and pair area are `3/4` and `1/2`;
3. its physical matrix and extension masses are exactly as stated;
4. `W_2=1/8`;
5. the fixed-threshold constant is `6 e 2^(1/3)=20.5489229713...`;
6. a random finite Parseval-frame test numerically checks the cross-volume factorization (4.1) for many literal cuts.

The finite checker is not the proof of Lemmas 3.1--3.2 or the analytic grouped-cross theorem.
