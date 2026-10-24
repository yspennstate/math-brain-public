# account02/B10 — rank-three coupled case: isotropic-heavy cascade and unbounded peeling obstruction

**Run:** `20260922T154900Z-account02-B10-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Rank-three coupled case; complementary constructions/source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED` + local `CANDIDATE_REFUTED`; full QFORM target remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication and result of this run

The live exact-rank-three debt is not merely a small diagonal pivot. Prior account02/B10 r12 reduced a heavy row to a strong original-product hyperbolic coupling, but its residual bank is correlated. The first unpaid implication was whether heavy rows can be peeled/conditioned a bounded number of times until either (i) a quantitative nonisotropic pivot theorem fires or (ii) the remaining rank-three frame is diffuse.

This run gives two exact advances.

1. **Two-level cascade narrowing.** Combining the independently reviewed conditional-whitening theorem of account02/B08 with the named partner account03/B10 nonisotropic-pivot proof yields a quantitative dichotomy: outside a near-coloop branch, failure of all already-paid branches forces *two* original physical rows to be quantitatively heavy and near-isotropic, with an explicit residual leverage relation.
2. **Unbounded-peeling falsifier.** For every integer `K>=2` there is an exact target matrix with spectrum `{1,-1,1}` and a chain of `K` original physical rows such that, after successively conditioning the preceding rows and whitening, the next row has leverage `2/3` (until the final leverage-one row) and diagonal pivot exactly zero. Hence no universal finite number of heavy-row deletion/whitening steps can by itself force diffuseness or a nonzero-pivot endpoint. The same family is nevertheless uniformly paid by a completed disjoint-bank theorem, so it is not a counterexample to QFORM.

The surviving obligation is therefore `QFORM-ISOTROPIC-HEAVY-CASCADE-BANK-AGGREGATION-v1`: aggregate an entire near-isotropic heavy cascade/ray before reciprocal local-minor or scalar-pivot payment, or prove that departure from such a ray creates a previously paid shear/cross-bank branch.

## 2. Sources and corrections consumed

Fresh owner control remained QFORM-only, revision `2026-09-22.5`. The full conjecture is: for independent real cap-one densities and symmetric `A` with at least three eigenvalues of modulus at least one, bound the density of `X^T A X` by one universal constant. No moment, support, sign, or post-rotation independence assumption is used here.

The following completed mathematics is used at proof level.

- **Named partner account03/B10:** `QFORM-RANK3-NONISOTROPIC-PIVOT-v1`, canonical source `yspennstate/math-open-problems@5ce98ee83b2fef75136f10cdd0e89741f017d3e0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/account03-B10-20260922T141643Z-r11/REPORT.md`. Its displayed proof gives, for an exact rank-three factorization `A=U Lambda U^T`, a physical row of leverage `ell>0` and nonzero pivot `d=A_ii`,
  `||p_Q||_infinity < 97 [|d| ell |det Lambda|]^(-1/4)`.
  The proof itself uses only invertibility of the spectral `Lambda` after the pivot: equations (2.3)--(2.5) and Lemma 3.1 depend on `det Lambda`, not on a lower bound for each individual eigenvalue. I use that homogeneous displayed argument below after conditioning.
- **account02/B08:** independently reviewed physical-block/conditional-whitening theorem, canonical source `yspennstate/math-open-problems@84657e690f8411d99602ddc772b622686c3874ed`, handoff `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account02/B08/B08-20260922T124007Z-r11.md`. For singleton conditioning with original row leverage `c<1`, it gives residual Gram determinant `1-c`, exact whitened leverages, and a diffuse residual bound `3e[(1-c)|det Lambda|]^(-1/3)` when every whitened residual leverage is at most `1/2`.
- **account03/B09:** `QFORM-THREE-BANK-CROSS-SQUARE-v1`, canonical source `yspennstate/math-open-problems@4f16e93d27fca487ce6cd32801ddcaff6238e577`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/account03-B09-20260922T144807Z-qform11/REPORT.md`. On normalized disjoint banks `Q=2UV+W^2`, it yields `||p_Q||_infinity<=8sqrt(2)`.

Live corrections retained include the false law-uniform pointwise oscillatory route, no post-rotation independence, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`. In particular no conditional marginal cap is substituted for genuine product provenance.

## 3. Exact original-coordinate conditioning identity

Let

`A=U Lambda U^T`, `U^T U=I_3`,

with `Lambda` invertible symmetric. Split original coordinate indices into a conditioned set `S` and complement `C`, and assume

`G := I_3-U_S^T U_S = U_C^T U_C`

is positive definite. Put `B=A_CC=U_C Lambda U_C^T`. For fixed `X_S=x`, the cross term in the conditional quadratic is

`2 X_C^T U_C Lambda U_S^T x`.

Define

`h(x)=U_C G^{-1} U_S^T x`.

Then

`B h = U_C Lambda U_C^T U_C G^{-1}U_S^T x = U_C Lambda U_S^T x`.

Therefore

`Q | (X_S=x) = (X_C+h(x))^T B (X_C+h(x)) + kappa(x)`

for a deterministic scalar `kappa(x)`. The transformation on `X_C` is coordinatewise translation by fixed constants, so conditioned on `X_S=x` the variables in `C` remain independent with exactly their original density caps.

Whiten the residual frame by

`U_tilde=U_C G^(-1/2)`, `Lambda_tilde=G^(1/2) Lambda G^(1/2)`.

Then `U_tilde^T U_tilde=I_3`, `B=U_tilde Lambda_tilde U_tilde^T`, and

`det Lambda_tilde = det(G) det(Lambda)`.                                             (3.1)

For a singleton `S={i}`, write `v=u_i`, `L=||v||^2`, `rho=1-L`. Then `G=I-vv^T`, `det G=rho`, and for every `j!=i`

`c_j := ||G^(-1/2)u_j||^2 = ||u_j||^2 + (u_j dot v)^2/rho`.                     (3.2)

Equation (3.2) is the reviewed B08 singleton formula; the general translation identity above records why all later density bounds remain uniform under the conditioning.

## 4. Two-level isotropic-heavy cascade lemma

Assume now the target-normalized exact-rank-three case

`A=U Lambda U^T`, `|lambda_1|,|lambda_2|,|lambda_3|>=1`,

so `|det Lambda|>=1`. Let `L=max_i ||u_i||^2` and choose `i` attaining it; put `d_i=A_ii`.

### 4.1 Already-paid top-level branches

If `L<=1/2`, the reviewed diffuse theorem gives

`||p_Q||_infinity <= 3e`.                                                        (4.1)

Suppose `L>1/2`. If `|d_i|>=1/64`, the named partner theorem gives

`||p_Q||_infinity <97[(1/64)(1/2)|det Lambda|]^(-1/4)
                    <=97*128^(1/4)<327`.                                         (4.2)

Thus assume `|d_i|<1/64`. If `rho=1-L<1/64`, this is the explicit **near-coloop isotropic** branch and is left to the cascade aggregation obligation.

### 4.2 Condition the heavy row when `rho>=1/64`

Assume `rho>=1/64`. Condition on `X_i` and use Section 3. The residual spectral determinant is

`|det Lambda_tilde|=rho |det Lambda|>=rho`.                                      (4.3)

If every residual whitened leverage `c_j<=1/2`, B08 gives uniformly in the conditioned value

`||p_{Q|X_i}||_infinity <=3e [rho |det Lambda|]^(-1/3)
                           <=3e rho^(-1/3)
                           <=12e<32.62`.                                          (4.4)

Averaging the conditional densities preserves the same bound.

Otherwise choose `j` with `c_j>1/2`. Its residual quadratic pivot is still the original physical diagonal `d_j=A_jj`: whitening changes the factorization, not the principal entry of `B=A_CC`.

If `|d_j|>=rho/8`, re-run the homogeneous displayed partner argument on the residual exact-rank-three factorization. From (4.3),

`|d_j| c_j |det Lambda_tilde| >= (rho/8)(1/2)rho = rho^2/16`,

hence uniformly in `X_i`

`||p_{Q|X_i}||_infinity <97 (rho^2/16)^(-1/4)
                         =194/sqrt(rho)
                         <=1552`.                                                 (4.5)

Again mixture over `X_i` preserves this bound.

Therefore failure of all branches (4.1)--(4.5) forces

`L in (1/2,63/64]`, `|d_i|<1/64`,
`c_j>1/2`, and `|d_j|<rho/8`.                                                     (4.6)

Moreover Cauchy--Schwarz gives

`(u_j dot u_i)^2 <= L ||u_j||^2=(1-rho)||u_j||^2`.

Using (3.2),

`c_j <= ||u_j||^2 + [(1-rho)/rho]||u_j||^2 = ||u_j||^2/rho`.

Thus the second row is quantitatively heavy already in the original frame:

`||u_j||^2 >= rho c_j > rho/2 >=1/128`.                                         (4.7)

This is the promised two-level narrowing: a hard exact-rank-three instance outside the near-coloop branch cannot merely have one troublesome heavy row; it contains a second original physical row carrying at least `1/128` leverage and a diagonal pivot smaller than the natural residual determinant scale.

## 5. Arbitrarily long zero-pivot heavy cascade

The tempting next claim would be that repeating the preceding step only a universal number of times must eventually reach a paid branch. That claim is false.

Fix any integer `K>=2`. In spectral coordinates take

`Lambda_0 = [[0,1,0],[1,0,0],[0,0,1]]`,

whose eigenvalues are `{1,-1,1}`. Let `e_1,e_2,e_3` be the standard basis. Define `K` physical rows on the isotropic ray `e_1` with squared lengths

`w_k=2/3^k` for `1<=k<K`,
`w_K=1/3^(K-1)`.                                                                (5.1)

Then `sum_k w_k=1`. Add two physical rows `e_2/sqrt(2)` and two rows `e_3/sqrt(2)`. The resulting row matrix `U` satisfies `U^T U=I_3`, hence

`A_K=U Lambda_0 U^T`

has exactly the three nonzero eigenvalues `{1,-1,1}` and is a target-valid exact-rank-three matrix.

Every `e_1`-ray row is exactly isotropic:

`u_k^T Lambda_0 u_k=0`,                                                         (5.2)

and every pair of such rows also has zero physical matrix entry.

Now condition successively on the first `k-1` ray coordinates and whiten the remaining frame. Before conditioning row `k`, the unconditioned squared spectral mass on `e_1` is

`R_k=sum_{s=k}^K w_s = 1/3^(k-1)`.                                              (5.3)

Therefore the next whitened leverage is exactly

`w_k/R_k=2/3` for `k<K`, and `w_K/R_K=1`.                                       (5.4)

The whitened spectral matrix is a congruence of `Lambda_0`, so the next ray row still has diagonal pivot zero. Hence for any prescribed finite peeling depth `m`, choose `K>m`; the first `m` deletion/whitening steps all present a leverage-`2/3`, zero-pivot physical row. Neither the diffuse `<=1/2` branch nor any nonzero-pivot theorem can fire on that ray during those steps.

This is an exact target-level counterexample to the **intermediate structural claim** that bounded-depth heavy-row peeling must terminate in a diffuse or nonisotropic-pivot state. It is not a counterexample to the density conjecture.

## 6. Why the falsifier is still uniformly paid

The three spectral directions of Section 5 are supported on three disjoint original-coordinate banks. Put

`Z_1=sum_{k=1}^K sqrt(w_k) X_k`,
`Z_2=(Y_1+Y_2)/sqrt(2)`,
`Z_3=(W_1+W_2)/sqrt(2)`.

The three variables are independent because their physical coordinate banks are disjoint, and

`Q_K=2 Z_1 Z_2 + Z_3^2`.                                                        (6.1)

The coefficient vectors in all three banks have Euclidean norm one. Applying account03/B09 `QFORM-THREE-BANK-CROSS-SQUARE-v1` with effective coefficients `B=C=1` gives

`||p_{Q_K}||_infinity <=8sqrt(2)<11.314`                                        (6.2)

for arbitrary independent cap-one physical input laws, uniformly in `K`.

Thus the family separates the mechanisms cleanly: every finite local peeling rule can be made to keep seeing an isotropic heavy row, while global bank aggregation closes the whole family with a fixed constant.

## 7. Consequence and next exact implication

The exact-rank-three programme should not spend further effort trying to prove bounded-depth heavy-row deletion. The new structural target is:

**`QFORM-ISOTROPIC-HEAVY-CASCADE-BANK-AGGREGATION-v1`.** Starting from the hard state (4.6)--(4.7), aggregate all successive near-isotropic heavy rows before paying local reciprocal determinants. Prove one of:

1. their spectral row directions remain close enough to one isotropic ray that their original physical coordinates can be compressed into a product-linear bank while two transverse banks retain a square/cross-square certificate; or
2. quantitative angular departure creates a nontrivial cross/shear/overlap-one energy that fires an existing paid branch; or
3. a nonisotropic pivot or a diffuse residual appears with a quantitative constant.

The exact family in Section 5 shows that any valid proof must permit arbitrarily many rows in the first alternative. This is the first unpaid implication after this run. Full QFORM remains OPEN.

## 8. Verification status

`VERIFY.py` beside this report checks the exact rational identities (5.1)--(5.4), the Parseval frame and target spectrum numerically for `K=2,...,12`, the zero pivots/zero within-ray entries, and the stated numerical constants. The arbitrary-`K` proof is the displayed geometric-series calculation above; the finite checker is regression only and is not used as closure.
