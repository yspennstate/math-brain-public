SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-22T22:15:48Z.
attacking: the exact-rank-three aggregate principal-triple packet; refine it into three disjoint original-coordinate banks, pay the diffuse core by Fresnel-Brascamp-Lieb, and pay the exact grouped-star endpoint by product-safe bank compression.

# fleet03/B10 r20 — tripartite packet refinement and grouped-star payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Pre-publication control refresh observed:** `yspennstate/math-research-brain@4f39392a513c2c04022f51983ec60bbb00a93717`, same revision  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** new supporting theorems proved; full QFORM remains `OPEN / NOT PROVED`.

## 1. Correction discipline and exact inherited state

The full target is unchanged: independent original coordinates with densities at most one; real symmetric `A`; at least three eigenvalues of modulus at least one; prove one dimension-free `L^infinity` density constant or give a genuine counterexample. No moments, support bounds, Gaussianity, log-concavity, or independence after spectral rotation are used below.

The current proof-first owner request explicitly keeps B10 on the hub/star plus delocalized-component obstruction and forbids treating small dense self-couplings perturbatively. The live correction ledger also keeps the arbitrary-joint rank-three coarea estimate, conditional-projection-height moment interfaces, pointwise Fresnel decay, and reciprocal-single-minor completion unavailable.

This run starts from B10 r19, canonical source

`yspennstate/math-open-problems@322b559872ab4c004ce7b5f4681fb2ffb40376a5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260922T214631Z-fleet03-B10-QFORM-r19/REPORT.md`.

After the cap-one null-bank compression of B10 r15, the exact-rank-three state has

`A = R M R^T`, `R^T R = I_3`,

with

`D := |det M| >= 1/2`, `sigma_min(M) >= 1/2`,

and a distinguished independent cap-one null coordinate of leverage `c>=7/9`. B10 r19 proves that the remaining near-span branch has one of the following two nonnegative determinant packets.

1. **Mixed packet:** for two disjoint complement banks `J,K`, one of

   `E_21 = sum_{i<j in J, k in K} det(r_i,r_j,r_k)^2`,

   `E_12 = sum_{i in J, j<k in K} det(r_i,r_j,r_k)^2`

   is at least `1/128`.

2. **Near-unit null-row packet:** if `c>61/64`, the complete null-row principal-triple bank has physical mass

   `sum_{j<k}|det A_{0jk}| = D c > 61/128`.

The exact designated partner `fleet04/B10` still has no completed current-QFORM report discoverable in the repository. No result is attributed to it. The completed compatible fleet04/B16 theorem is used below at its proved scope; canonical source:

`yspennstate/math-open-problems@58c23c624db350cf44f0c836daa3582eb7e2d266`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260922T161909Z-fleet04-B16-QFORM-r2/REPORT.md`.

Its fixed-pair determinant identity is

`sum_{k != i,j}|det A_{ijk}| = D G_ij`,

where `G_ij = ||r_i wedge r_j||^2`. This is used as an actual inequality, not merely cited.

## 2. A random-split lemma: two-bank exterior mass becomes three independent banks

### Lemma 2.1 — `QFORM-MIXEDBANK-TRIPARTITION-v1`

Let `J,K` be disjoint sets of physical coordinates and define

`E_21(J,K) = sum_{i<j in J, k in K} det(r_i,r_j,r_k)^2`.

There is a partition `J=J_1 disjoint_union J_2` such that

`sum_{i in J_1, j in J_2, k in K} det(r_i,r_j,r_k)^2 >= E_21(J,K)/2`.

The analogous statement holds for `E_12` by splitting `K`.

#### Proof

Assign every index of `J` independently to `J_1` or `J_2` with probability `1/2`. For each unordered pair `{i,j}` the probability that its two endpoints are separated is exactly `1/2`. All summands are nonnegative. Therefore the expected separated triple mass is exactly `E_21/2`; some deterministic partition attains at least the expectation. QED.

This operation is entirely in the ORIGINAL coordinate index set. The three resulting random vectors `X_{J_1}`, `X_{J_2}`, `X_K` are mutually independent because the input coordinates are independent.

### Lemma 2.2 — direct compatible-partner application in the near-unit branch

For the distinguished null row `r_0=sqrt(c) r`, the fleet04/B16 fixed-pair identity gives

`P_0j := sum_{k != 0,j}|det A_{0jk}| = D ||r_0 wedge r_j||^2`.

Summing over `j` and using Parseval,

`sum_j ||r_0 wedge r_j||^2
 = c sum_j ||(I-r r^T)r_j||^2 = 2c`.

Every triple `{0,j,k}` is counted twice in `sum_j P_0j`; hence

`sum_{j<k}|det A_{0jk}| = D c`.

When `c>61/64`, randomly bipartition the complement as `C=C_1 disjoint_union C_2`. Exactly as in Lemma 2.1,

`E[sum_{j in C_1,k in C_2}|det A_{0jk}|] = D c/2 > 61/256`.

Thus one deterministic split satisfies

`sum_{j in C_1,k in C_2}|det A_{0jk}| > 61/256`.

This is the requested concrete use of completed compatible fleet04 mathematics.

### Corollary 2.3 — a universal tripartite packet in every r19 near-span branch

In the mixed branch, r19 gives one spectral packet at least `1/128`; Lemma 2.1 retains at least half. In the near-unit branch, Lemma 2.2 gives a stronger packet. Therefore in every r19 near-span branch there exist three disjoint original-coordinate banks `B_1,B_2,B_3` such that

`T := sum_{i in B_1,j in B_2,k in B_3} det(r_i,r_j,r_k)^2 >= 1/256`.        (2.1)

Since for exact rank three

`|det A_{ijk}| = D det(r_i,r_j,r_k)^2`,

we also have the physical determinant packet

`sum_{i in B_1,j in B_2,k in B_3}|det A_{ijk}| = D T >= 1/512`.          (2.2)

No single determinant atom is selected.

## 3. Mixed-discriminant identity and a uniformly conditioned core

For `g=1,2,3`, set

`H_g = sum_{i in B_g} r_i r_i^T`,

and `G=H_1+H_2+H_3`.

### Lemma 3.1 — exact mixed-discriminant certificate

The coefficient of `xyz` in

`det(x H_1 + y H_2 + z H_3)`

is exactly `T` from (2.1).

#### Proof

Apply Cauchy-Binet to the stacked spectral-row matrix after multiplying rows in bank `B_1,B_2,B_3` by `sqrt(x),sqrt(y),sqrt(z)`, respectively. A three-row minor contributes the product of the corresponding group weights. The coefficient of `xyz` therefore receives exactly those triples with one row from each bank, each with coefficient `det(r_i,r_j,r_k)^2`. QED.

Since all Cauchy-Binet terms in `det G` are nonnegative,

`det G >= T >= 1/256`.                                    (3.1)

Also `0 <= G <= I_3`, because `R^T R=I_3`. If the eigenvalues of `G` are `g_1>=g_2>=g_3>0`, then `g_1,g_2<=1`, so

`lambda_min(G)=g_3 >= g_1 g_2 g_3 = det G >= 1/256`.        (3.2)

Thus the union `S=B_1 union B_2 union B_3` is not merely a determinant-mass packet: it is a uniformly conditioned three-dimensional spectral core.

Whitening only the spectral coefficient geometry,

`R_S = Rtilde G^(1/2)`, `Rtilde^T Rtilde=I_3`,

turns its exact-rank-three quadratic matrix into

`M_S = G^(1/2) M G^(1/2)`.

Consequently

`|det M_S| = D det G >= 1/512`,                             (3.3)

and, using the inherited `sigma_min(M)>=1/2`,

`sigma_min(M_S) >= lambda_min(G) sigma_min(M) >= 1/512`.    (3.4)

This uses no probabilistic rotation. It is only an algebraic representation of the same principal quadratic block on the selected ORIGINAL coordinates.

## 4. The whole diffuse selected-core branch is paid

Let

`ell_i = r_i^T G^(-1) r_i`, `i in S`,

be the normalized leverages of the selected core. They satisfy `sum_{i in S} ell_i=3`.

### Theorem 4.1 — `QFORM-TRIPARTITE-DIFFUSE-CORE-PAYMENT-v1`

If

`ell_i <= 1/2` for every `i in S`,

then the full quadratic form has a bounded density with

`||p_Q||_infinity <= 12 (D det G)^(-1/3) <= 96`.            (4.1)

#### Proof

Condition on every original coordinate outside `S`. The active variables remain independent with their original density caps. The conditional quadratic part is exactly

`A_SS = R_S M R_S^T`;

outside couplings become an arbitrary affine term.

Diagonalize `M` in spectral space only. The completed Fresnel-Brascamp-Lieb Theorem F from

`yspennstate/math-open-problems@7359c982f3fa85f61b99e8768b915cce6e596d36`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

applies with `B=0`, Gram matrix `G`, and exactly the normalized leverage condition above. It gives, uniformly in every conditioned affine shift,

`||p_{Q | X_{S^c}}||_infinity <= 12 (D det G)^(-1/3)`.

Mixing preserves the same bound. Equation (3.3) gives `D det G>=1/512`, whose cube root reciprocal is `8`, proving (4.1). QED.

Because Theorem F obtains an integrable characteristic-function majorant `min(1,C|t|^(-3/2))`, each conditional density in this branch has a continuous representative. The bound is uniform in the outside realization; dominated convergence therefore also gives a continuous representative for the unconditional mixture. Thus **continuity is proved in this diffuse-core branch**, not merely essential boundedness.

A failed diffuse-core gate now has a concrete consequence. If some `ell_i>1/2`, then by (3.2)

`ell_i = r_i^T G^(-1)r_i <= ||r_i||^2/lambda_min(G)`,

so

`||r_i||^2 > lambda_min(G)/2 >= 1/512`.                    (4.2)

Hence the survivor contains an actual constant-size normalized hub inside a uniformly conditioned exact-rank-three core; it cannot hide solely in infinitesimal rows.

## 5. Exact grouped-star endpoint: aggregate before reciprocal minors

The diffuse gate can fail even when every individual physical triple is tiny. The following theorem pays the opposite exact endpoint in which each independent bank carries only one spectral direction.

### Theorem 5.1 — `QFORM-RANKONE-THREEBANK-PAYMENT-v1`

Assume, in addition to (2.1), that each bank has spectral rank one:

`H_g = e_g v_g v_g^T`, `||v_g||=1`, `e_g>0`, `g=1,2,3`.

Then, for arbitrary conditioned coordinates outside `S`, the quadratic form has an essentially bounded density and

`||p_Q||_infinity
 <= 32 sqrt(10) [e^3/(D T)]^(1/3)`.                       (5.1)

In the r20 core, `D T>=1/512`, so

`||p_Q||_infinity <= 256 e sqrt(10) < 2200.567`.            (5.2)

#### Proof

Because `H_g` has rank one, every row in bank `B_g` is collinear with `v_g`: write

`r_i = a_i v_g`, `i in B_g`,

so `sum_{i in B_g} a_i^2=e_g`. Define the genuine original-coordinate bank aggregate

`W_g = sum_{i in B_g} a_i X_i`.

The three random variables `W_1,W_2,W_3` are mutually independent because their coordinate banks are disjoint. By the one-dimensional product-projection lemma proved in fleet02/B11,

`||p_{W_g}||_infinity <= sqrt(e)/sqrt(e_g)`.                (5.3)

Condition on all original coordinates outside `S`. The spectral vector contributed by the active variables is

`Y = v_1 W_1 + v_2 W_2 + v_3 W_3`,

plus a deterministic spectral shift. Therefore the conditional quadratic form is an arbitrary affine perturbation of

`W^T B W`,

where

`B_gh = v_g^T M v_h`.

Let `V` be the `3 x 3` matrix whose rows are `v_g^T`. Then

`|det B| = D det(V)^2`.                                    (5.4)

On the other hand the tripartite exterior mass factors exactly:

`T = e_1 e_2 e_3 det(V)^2`.                               (5.5)

Set `K_g=sqrt(e/e_g)` and `Z_g=K_g W_g`. By (5.3), every `Z_g` has density at most one, and the `Z_g` remain independent. In the `Z` variables the quadratic matrix is

`B_Z = diag(K_g^(-1)) B diag(K_g^(-1))`,

so (5.4)-(5.5) give

`|det B_Z|
 = |det B|/(K_1 K_2 K_3)^2
 >= D T/e^3`.                                               (5.6)

Now apply the completed determinant-only three-coordinate theorem

`QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1`,

canonical source

`yspennstate/math-open-problems@89e6481f4f7ed7d49a77cfcb989ee93572d5d5cd`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260922T190524Z-fleet03-B14-QFORM-r16/REPORT.md`.

It permits arbitrary affine terms and gives

`||p_Q||_infinity <= 32 sqrt(10) |det B_Z|^(-1/3)`.

Substitute (5.6) to obtain (5.1), and then `D T>=1/512` for (5.2). QED.

This theorem is genuinely aggregate-before-inversion. Each bank may contain arbitrarily many tiny coefficients and every individual principal-triple determinant may tend to zero; the entire bank is first compressed to one independent scalar, and only then is a three-variable determinant paid.

The theorem establishes essential boundedness in this endpoint. The cited determinant-localization theorem did not claim continuity, so continuity is **not** newly claimed here.

## 6. What is now left in B10's near-span chamber

Combining Sections 2-5, the r19 near-span obstruction is strictly smaller.

Every such state now contains three disjoint original-coordinate banks with tripartite spectral exterior mass `T>=1/256`, selected-core Gram `G>= (1/256) I_3`, and physical tripartite determinant mass at least `1/512`.

Two large branches are paid:

1. if every selected-core normalized leverage is at most `1/2`, Theorem 4.1 gives `||p_Q||_infinity<=96` and continuity;
2. if each of the three banks is spectrally rank one, Theorem 5.1 gives `||p_Q||_infinity<2200.567` without selecting a local atom.

Therefore a surviving counterexample sequence inside this chamber must simultaneously have

- a normalized selected-core leverage `>1/2` (hence a raw spectral row of squared norm `>1/512`), **and**
- genuine internal transverse geometry in at least one of the three independent banks (spectral rank at least two).

This is precisely a source-valid formulation of the current **hub plus delocalized component with dense self-coupling** debt. It cannot be removed by declaring the transverse part small: bounded-density inputs may live arbitrarily far out, so coefficient-smallness is not a perturbative error estimate.

The next implication is:

**`QFORM-TRIPARTITE-HEAVY-INTERNAL-TRANSVERSE-v1`.** In a uniformly conditioned tripartite core with `T>=1/256`, pay the case of a normalized leverage `>1/2` when at least one independent bank has internal rank at least two, using its actual product-linear provenance before any conditional `L^infinity` supremum. A valid proof may use a hub/Fresnel or overlap-sensitive grouped trace mechanism; it may not collapse the bank to an arbitrary joint density or discard the internal transverse self-coupling perturbatively.

The exact-rank-three theorem is therefore still open, and arbitrary extra spectrum remains a separate full-target debt.

## 7. Regression computation

A bounded seeded checker was run for the algebraic identities only. It verified:

- 250 random three-bank instances of the mixed-discriminant coefficient identity, maximum absolute discrepancy `1.5265566588595902e-16`;
- 250 random rank-one three-bank instances of (5.5), maximum absolute discrepancy `4.163336342344337e-17`;
- 100 finite random `JJK` packets by exhaustive bipartition; every best separated packet was at least one half of the original packet (minimum observed ratio `0.6886837730739556`).

These computations are regression checks, not evidence for any unproved probabilistic implication.

## 8. Status

Proved in this run:

- `QFORM-MIXEDBANK-TRIPARTITION-v1`;
- the direct partner-derived near-unit tripartition inequality;
- `QFORM-TRIPARTITE-GRAM-CERTIFICATE-v1` via (3.1)-(3.4);
- `QFORM-TRIPARTITE-DIFFUSE-CORE-PAYMENT-v1`, with explicit bound `96`;
- `QFORM-RANKONE-THREEBANK-PAYMENT-v1`, with explicit bound `<2200.567` in the live compressed chamber.

Not proved:

- `QFORM-TRIPARTITE-HEAVY-INTERNAL-TRANSVERSE-v1`;
- arbitrary exact-rank-three closure;
- robustness to arbitrary additional spectrum;
- the full owner conjecture.

**Full QFORM conjecture: OPEN / NOT PROVED / NOT DISPROVED.**
