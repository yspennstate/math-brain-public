SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T17:56:58Z.
attacking: source-valid coefficient-sensitive random-slope smoothing, applying the latest account02/B18 zero-edge kernel with Juškevičius--Lee sharp rearrangement rather than the coarser universal projection cap.

# account01/B18 r35 — sharp rearrangement averages the partner random-slope kernel

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Literature-to-proof transfer  
**Status:** `PROVED SUPPORTING TARGET-LEVEL SHARPENING / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved for the new functional theorem and the target-valid family below; full-target continuity remains open.

## 1. Scope, source pins, and correction boundary

The unrestricted owner target remains OPEN: for every dimension, arbitrary independent real original-coordinate inputs with one-dimensional probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal finite output-density bound for `X^T A X`, with continuity tracked separately.

Fresh QFORM controls and corrections were consumed before this proof. In particular this report uses no independence after spectral rotation, no arbitrary-joint coarea estimate, no conditional-density-as-independence substitution, no positive moment of a worst conditional projection cap, no law-uniform pointwise quadratic-phase decay, no fixed-good-minor extraction, and no deletion of a small coefficient.

The latest completed designated-partner report actually applied is

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T170538Z-account02-B18-auto11/REPORT.md`,

read with blob

`f635d6b1462630689d0debd1c24649c2a2272a6e`.

Its random-slope theorem says that for independent cap-one real variables `U,V`, real `b`, and nonzero `a,t`,

`Z=a U^2+bU+2tV`

has density bounded by

`H_a(t):=min{ (2|t|)^(-1), sqrt(2/(|a||t|)) }`.                    (1.1)

It then averages this only through the generic one-dimensional projection cap `sqrt(2)/||g||_2`, obtaining the universal coefficient-blind estimate `6 e^(-1/3)(|a| ||g||_2^2)^(-1/3)`. The present run keeps the exact coefficient profile by inserting a sharp primary rearrangement theorem before averaging.

### Primary literature input

T. Juskevicius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190 (2015), Theorem 1. If `Y_j` are independent real random variables with density maxima at most `K_j`, then for every measurable set `S`, the probability that `sum Y_j` lies in `S` is at most the probability that the sum of independent centered uniform variables of density `K_j` lies in the centered interval having the same Lebesgue measure as `S`. In one dimension the comparison variables are uniform on `[-1/(2K_j),1/(2K_j)]`.

The hypotheses match the owner source class exactly after deterministic rescaling of each original coordinate: no moments, bounded support, iid assumption, log-concavity, smoothness, centering, or symmetry is added.

For comparison, Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, gives the profile-blind cap `sqrt(2)` for a normalized one-dimensional orthogonal projection of a cap-one product density. That theorem remains valid, but sharp rearrangement can do better for the expectation of the singular kernel (1.1).

## 2. Functional Rogozin/Juskevicius--Lee transfer

### Theorem 2.1 — `QFORM-ZEROEDGE-ROGOZIN-FUNCTIONAL-v1`

Let

`U,V,Z_1,...,Z_m`

be mutually independent real random variables, each having a probability density bounded by one. Let `a !=0`, let `g=(g_1,...,g_m) !=0`, let `eta in R`, and let `B(Z),C(Z)` be arbitrary real measurable functions. Put

`H=eta+sum_j g_j Z_j`                                                   (2.1)

and

`T=2 U H+a V^2+B(Z)V+C(Z)`.                                             (2.2)

Let `U_1^*,...,U_m^*` be independent `Uniform[-1/2,1/2]` variables and define

`H_g^* = sum_j g_j U_j^*`,                                               (2.3)

with zero coefficients omitted. Then `T` has a continuous density vanishing at infinity and

`boxed:
 ||p_T||_infinity <= E H_a(H_g^*)`,                                      (2.4)

where

`H_a(x)=min{(2|x|)^(-1), sqrt(2/(|a||x|))}` for `x!=0`.                  (2.5)

This is a coefficient-sensitive refinement of the partner's cap-only random-slope average.

### Proof, step 1: conditional partner kernel

Condition on `Z=z`. Except on the null event `H(z)=0`, the only remaining random variables are the genuinely independent ORIGINAL coordinates `U,V`, both still cap one. The conditioned form is

`2 H(z) U+aV^2+B(z)V+C(z)`.

After swapping the names of the partner's square and linear variables and ignoring the deterministic output shift `C(z)`, the partner theorem (1.1) gives

`||p_(T|Z=z)||_infinity <= H_a(H(z))`.                                  (2.6)

The scalar `H` is absolutely continuous because at least one coefficient `g_j` is nonzero and the corresponding scaled input has a density; hence `P(H=0)=0`.

Averaging conditional densities therefore gives

`||p_T||_infinity <= E H_a(H)`.                                         (2.7)

The problem is now purely one-dimensional: control an even decreasing singular function of a sum of independent bounded-density summands.

### Proof, step 2: sharp rearrangement of every centered small ball

For each nonzero coefficient `g_j`, the scaled variable `Y_j=g_j Z_j` has density maximum at most

`K_j=1/|g_j|`.                                                          (2.8)

The Juskevicius--Lee comparison variable of density `K_j` is precisely `g_j U_j^*` up to an irrelevant reflection. The deterministic translation `eta` does not cause a gap: for every `r>0`, the event

`|eta+sum_j Y_j|<r`

is the event that `sum_j Y_j` falls in an interval of length `2r`; Theorem 1 compares every measurable set to the centered interval of the same measure. Therefore

`P(|H|<r) <= P(|H_g^*|<r)` for every `r>0`.                              (2.9)

The function `H_a(x)` is even, nonnegative, and decreasing in `|x|`. Using its layer-cake representation, every superlevel set is a centered interval. Integrating (2.9) over the layer parameter gives

`E H_a(H) <= E H_a(H_g^*)`.                                             (2.10)

Combining (2.7) and (2.10) proves the essential bound (2.4).

### Proof, step 3: finiteness and continuity

The comparator `H_g^*` has a bounded density: if there is one nonzero coefficient it is uniform on a finite interval, while with several coefficients it is a convolution of such bounded densities. Near zero the smaller term in (2.5) is `sqrt(2/(|a||x|))`, whose singularity is locally integrable. Hence

`E H_a(H_g^*)<infinity`.                                                (2.11)

For fixed `z` with `H(z)!=0`, the conditional density is the convolution of the density of `2H(z)U` with the pushforward density of the quadratic `aV^2+B(z)V`; it is therefore a `C_0(R)` function. The integrable majorant in (2.6), together with (2.10)-(2.11), allows dominated convergence in `z`. Thus the averaged density `p_T(t)=E p_(T|Z)(t)` is continuous and tends to zero as `|t|->infinity`.

This continuity statement is separate from the essential bound and uses no pointwise law-uniform characteristic-function decay.

## 3. Exact application to the latest account02/B18 target family

The designated partner's latest report studies the family

`G=(X_1+X_2)/sqrt(2)`,
`W=(X_1-X_2)/sqrt(2)`,                                                (3.1)

`Q_theta=2(X_0+theta W)G+X_3^2`, `theta in R`,                       (3.2)

for arbitrary independent cap-one original inputs `X_0,...,X_3`. The partner verifies that the physical quadratic matrix has spectrum

`{-sqrt(1+theta^2), 0, 1, sqrt(1+theta^2)}`.                         (3.3)

Hence it is inside the owner's target for every real `theta`: exactly three eigenvalues have modulus at least one. The partner's whole-line certificate is

`||p_(Q_theta)||_infinity <=6e^(-1/3)=4.299187863442736...`.        (3.4)

Theorem 2.1 gives a sharper exact coefficient-profile average. Condition on `(X_1,X_2)`. Then

`Q_theta = X_3^2+2G X_0+2theta WG`.                                  (3.5)

The last term is only a deterministic output translation under this conditioning. Thus the partner kernel with `a=1` gives

`||p_(Q_theta | X_1,X_2)||_infinity <= H_1(G)`,                      (3.6)

where

`H_1(x)=min{(2|x|)^(-1),sqrt(2/|x|)}`.                              (3.7)

By Theorem 2.1/Juskevicius--Lee, the expectation is maximized by replacing `X_1,X_2` with independent centered unit uniforms. Write

`G_*=(U_1+U_2)/sqrt(2)`, `U_1,U_2 iid Uniform[-1/2,1/2]`.            (3.8)

Its density is the exact triangular law

`p_*(x)=sqrt(2)(1-sqrt(2)|x|) 1_{|x|<=1/sqrt(2)}.`                   (3.9)

The two terms in `H_1` meet at `x=1/8`. Therefore

`E H_1(G_*)`
`=2 int_0^(1/8) sqrt(2)(1-sqrt(2)x) sqrt(2/x) dx`
` +2 int_(1/8)^(1/sqrt(2)) sqrt(2)(1-sqrt(2)x) (2x)^(-1) dx`.       (3.10)

The first integral is

`2sqrt(2)-1/6`,                                                      (3.11)

and the second is

`(5sqrt(2)/2)log 2 - sqrt(2)+1/4`.                                  (3.12)

Thus

`boxed:
 ||p_(Q_theta)||_infinity
 <= 1/12+sqrt(2)+(5sqrt(2)/2) log 2
 =3.9481922543777963...                                             (3.13)
`

for **every** `theta in R` and **every** admissible independent cap-one original-coordinate input law.

This improves the latest designated-partner certificate (3.4) by

`1 - 3.9481922543777963 / 4.299187863442736
 =0.0816423055...`,                                                  (3.14)

i.e. about **8.16 percent**.

Call (3.13) `QFORM-PARTNER-THETA-FAMILY-ROGOZIN-v1`.

Moreover Theorem 2.1 proves that this family has a continuous `C_0` density. Thus the sharper constant and continuity are both paid on the entire real line; no one-sheet/two-sheet split is needed.

## 4. Why this is source-valid and what it does not prove

The source-valid chain is exact:

1. after conditioning on the residual original block, the partner kernel uses two genuinely independent original variables;
2. Juskevicius--Lee is applied to the remaining ORIGINAL independent scaled summands, exactly at its bounded-density hypotheses;
3. no projected coordinates are declared independent;
4. no conditional density cap is promoted to independence;
5. no small coefficient is deleted;
6. no unrestricted joint-density coarea bound appears.

The result is a theorem for the full family (3.2), not a finite computation or numerical heuristic. It is nevertheless only a **supporting target-level family**, not the full conjecture.

The literature audit found no exact published theorem among the checked primary sources that directly supplies the owner's full arbitrary non-iid cap-one quadratic-form statement. The LPP marginal theorem is linear and profile-blind; Juškevicius--Lee is sharp for sums but must be coupled to a valid nonlinear receiver such as the partner's kernel. Recent polynomial-image regularity results offer powerful dimension-free estimates under additional regularity/structural hypotheses and therefore were not treated as an exact solution. This is a hypothesis comparison, not a novelty claim from search absence.

## 5. Remaining mathematical debt

The sharp rearrangement transfer can be reused whenever a completed conditional receiver produces an even decreasing function of one original-source linear statistic. It therefore suggests replacing generic projection-cap averaging by exact uniform-sum comparison in other one-hub collars.

However it does **not** by itself close the present general null-hub punctured collar. The local state still left by the latest fleet reductions includes a heavy witness with

`q_i>1/2`, `0<|g_i|<1/64`,                                         (5.1)

outside the already-paid diffuse, moderate-edge, exact-zero-edge, and exact source-separated twist branches. The small nonzero edge cannot be set to zero. A next useful implication is a coefficient-sensitive receiver that retains that nonzero edge and yields an even decreasing slope kernel to which Theorem 2.1's rearrangement mechanism can be applied.

The unrestricted full-matrix structural bridge from three large eigenvalues into a universally paid packet also remains open.

## 6. Classification

`QFORM-ZEROEDGE-ROGOZIN-FUNCTIONAL-v1`: **PROVED SUPPORTING ANALYTIC THEOREM**.

`QFORM-PARTNER-THETA-FAMILY-ROGOZIN-v1`: **PROVED SUPPORTING TARGET-LEVEL FAMILY**, with continuous `C_0` density and universal constant `<3.949`.

`QFORM-FULL`: **OPEN / NOT PROVED**.
