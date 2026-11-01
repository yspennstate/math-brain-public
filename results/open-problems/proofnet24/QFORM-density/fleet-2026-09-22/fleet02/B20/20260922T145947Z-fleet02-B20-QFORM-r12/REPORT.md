# fleet02/B20 — heavy-diagonal Schur descent and localization collar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner revision: `2026-09-22.5`  
Run: `20260922T145947Z-fleet02-B20-QFORM-r12`  
Assignment: Proof closure and keeper / SYNTHESIS  
Classification: `ESSENTIAL_STEP_APPLIED / DIMENSION_DESCENT_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The sole target is the full arbitrary-dimension statement: for every `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^TAX` has a density with one universal finite essential-supremum bound, or give a valid counterexample. Continuity is separate.

This report never rotates the input law and never infers independence after diagonalizing `A`. It does not use the refuted law-uniform pointwise quadratic-phase decay, unrestricted fiber suprema, a generic conditional-cap surrogate for independence, a fixed physical rank-three minor, or an absolute Wiener criterion.

## 2. Fresh completed partner result actually used

The newest completed assigned-partner result located before publication is fleet03/B20 run `20260922T141139Z-fleet03-B20-QFORM-r11`, canonical package

`yspennstate/math-open-problems@7530e8c6ffd7284eb9c8acf1d79f36c335bf4fd6`

with main report path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260922T141139Z-fleet03-B20-QFORM-r11/REPORT.md`.

Its exact scalar-pivot identity is the key input here. Write a target matrix in one original coordinate as

`A=[[a,b^T],[b,C]]`, `a!=0`,

put

`S=C-bb^T/a`, `K=||b||_2/|a|`, `tau=(1+K)^(-2)`.

The partner proves

`boxed: s_2(S)>=tau`,

from the exact congruence

`A=L diag(a,S)L^T`, `L=[[1,0],[b/a,I]]`.

It also proves that if the entire-range projection of `S` has maximum physical row leverage at most `1/32`, then

`||p_Q||_infinity <= 16(1+K)|a|^(-1/2) sqrt[K_0 e/(7 sqrt(2))]`,

where `K_0=sqrt(pi) Gamma(1/4)/Gamma(3/4)`. For a large-spectral row with leverage at least `1/64` and `K<=1`, this is `<130`.

The same report records the dependent-square input needed below: if `R=Y^TSY` has an `L^3` density of norm `M`, then for

`Q=R+a(X_i+b^TY/a)^2`

one has

`||p_Q||_infinity <=4 |a|^(-1/2) M^(3/4)`.

This is source-valid because, conditional on any measurable function of `Y`, `X_i+b^TY/a` is a mixture of translations of the original independent `X_i` law and therefore retains density cap one.

A fresher fleet03/B20 run had only a start record at the final completed-partner check used for the main theorem; no unfinished statement is promoted to a dependency.

## 3. New theorem: exact third-direction retention below the Schur threshold

### Theorem 3.1 — `QFORM-SCHUR-THIRD-DIRECTION-RETENTION-v1`

Assume `s_3(A)>=1` and use the pivot notation above. If

`0<|a|<tau=(1+K)^(-2)`,

then

`boxed: s_3(S)>=tau.`

#### Proof

The partner congruence gives

`s_3(diag(a,S))>=tau`.

The singular values of `diag(a,S)` are the union of the single scalar `|a|` and the singular values of `S`. Because `|a|<tau`, that scalar cannot account for any of the three singular values which are at least `tau`. Hence all three must come from `S`, so `s_3(S)>=tau`. QED.

This one-line spectral observation is the point at which the partner's two-direction reserve becomes a genuine target-dimension descent: below the exact threshold `tau`, the Schur residual itself still satisfies the three-large-eigenvalue hypothesis after rescaling.

## 4. New theorem: a universal density-bound descent with an exact fixed point

Let

`P=1_{ {|A|>=1} }`

be the spectral projection onto the large-eigenvalue subspace and write `c_i=P_ii`. Functional calculus gives `A^2>=P`, hence for the pivot row

`a^2+||b||_2^2=(A^2)_ii>=c_i`.                                      (4.1)

### Theorem 4.1 — `QFORM-HEAVY-DIAGONAL-SCHUR-DESCENT-v1`

Fix

`C_0=512 sqrt(2)`.

Let `A` satisfy the full target spectral hypothesis. Suppose there is an original coordinate `i` such that

1. `c_i>=1/64`;
2. `a=A_ii!=0`;
3. `K=||A_{i,-i}||_2/|a|<=1`;
4. `|a|<tau=(1+K)^(-2)`.

Let `S` be the exact Schur complement at `i`. Then, for every constant `C>=C_0`, the following implication holds:

> if every admissible cap-one product law on the remaining `n-1` original coordinates gives `Y^T(S/tau)Y` a density bounded by `C`, then every admissible cap-one product law for `X^TAX` has a density bounded by the same `C`.

Equivalently, if an `n`-dimensional form satisfying the four displayed hypotheses violates the universal bound `C>=C_0`, then the lower-dimensional target form `S/tau` also violates that same bound.

#### Proof

Because `K<=1`, (4.1) gives

`2a^2 >= a^2+||b||^2 >=1/64`,

so

`|a|>=1/sqrt(128)`.

Also `tau=(1+K)^(-2)>=1/4`, whence

`|a| tau >= 1/(4 sqrt(128)) = 1/(32 sqrt(2)).`                   (4.2)

By Theorem 3.1, `s_3(S)>=tau`, so `S/tau` satisfies the exact three-large-eigenvalue target hypothesis in dimension `n-1`.

Assume its quadratic law has density cap `C`. Scaling back gives the residual

`R=Y^TSY`

a density cap at most `C/tau`. Since every probability density has `L^1` norm one,

`||p_R||_3 <= ||p_R||_infinity^(2/3) <= (C/tau)^(2/3)`.

Apply the partner's dependent-square smoothing estimate to

`Q=R+a(X_i+b^TY/a)^2`:

`||p_Q||_infinity`
` <=4 |a|^(-1/2) (C/tau)^(1/2)`
` =4 sqrt(C)/sqrt(|a|tau)`.

This is at most `C` whenever

`C>=16/(|a|tau)`.

By (4.2),

`16/(|a|tau) <= 512 sqrt(2)=C_0`.

Thus every `C>=C_0` is preserved by the descent. QED.

### Interpretation

The theorem is not a circular claim that the lower-dimensional target is already solved. It is a genuine **counterexample descent**: for any proposed universal cap `C>=512sqrt(2)`, a counterexample in this branch forces a strictly lower-dimensional counterexample with the same cap and with the exact source model preserved. Therefore a minimum-dimensional counterexample to such a cap can never occupy this branch.

No continuity statement is made by this descent step.

## 5. Combined heavy-row collar with the partner's diffuse-Schur theorem

The new descent and the partner's direct diffuse-Schur estimate fit without overlap.

Assume `c_i>=1/64` and `K<=1`. Then a minimum-dimensional counterexample to any cap `C>=C_0` must satisfy both

`boxed: |a|>=tau=(1+K)^(-2)>=1/4`                                  (5.1)

and

`boxed: max_j (P_range(S))_jj >1/32.`                              (5.2)

Indeed, violation of (5.1) triggers Theorem 4.1 and descends dimension. If (5.2) fails, the completed fleet03/B20 theorem gives the explicit direct bound `<130<C_0`.

Thus **heavy large-spectral rows which are diagonal-dominated are no longer a generic residual**. The only minimum-counterexample version of that branch is a large scalar pivot, at least two Schur singular directions of size at least `1/4`, and a physically localized entire Schur range.

This is a stricter source-valid residual than the previous `localized Schur` label.

## 6. Strongest conditional end-to-end assembly after this run

The current correction-safe chain is:

1. fleet03/B19 closes the physical near-diagonal branch and the high-stable-rank off-diagonal branch; any counterexample lies in
   `||A-diag(A)||op>1/4`, `sr(A-diag(A))<32`;
2. fleet02/B08 closes separator-conditioned diffuse selected-frame states under its exact `(eta,mu)` inequality, including full-rank examples invisible to entire-range leverage;
3. fleet02/B19 closes a scalar plus two-sided `2x2` Schur-corrected mixed packet when its overlapping determinant is quantitatively nonzero;
4. fleet04/B20 closes source-realizable disjoint hyperbolic-square aggregate packets;
5. the completed fleet03/B20 theorem closes a heavy diagonal-dominated physical row when its exact Schur residual has diffuse entire range;
6. **this run** removes the complementary small-pivot part of the same heavy diagonal-dominated row by dimension descent with invariant cap `C>=512sqrt(2)`.

Consequently a minimum-dimensional counterexample to `C_0=512sqrt(2)`, if one exists, must be in the low-stable-rank residual and must satisfy at least one of the following structural alternatives:

- **large-eigenspace diffuse:** every large-spectral row has `c_i<1/64`;
- **cross-dominated heavy row:** some `c_i>=1/64` but every usable such row has `K>1`;
- **localized large-pivot Schur:** some `c_i>=1/64`, `K<=1`, `|a|>=tau>=1/4`, and `max diag P_range(S)>1/32`.

The previous near-null cross-bank theorem of fleet02/B20 supplies source-realizable slope banks in an important cross-dominated exact-rank-three subcase; fleet04/B20 pays them when a disjoint square bank survives. The remaining issue is still source-valid entanglement/packet extraction, not a missing analytic estimate for an already extracted packet.

## 7. First unpaid universal implication, now with full hypotheses

### `QFORM-LOW-SR-THREE-WAY-PACKET-EXTRACTION-v1` — OPEN

Let `A` be an arbitrary real symmetric `n x n` target matrix, let `X_i` be arbitrary independent cap-one real inputs, and assume

`||A-diag(A)||op>1/4`, `sr(A-diag(A))<32`, `s_3(A)>=1`.

Assume also that no previously paid near-diagonal, high-stable-rank, separator-diffuse, two-sided-Schur-mixed, or disjoint hyperbolic-square packet is already present.

Prove that one of the three residual alternatives in Section 6 yields, with universal quantitative parameters and using only disjoint original-coordinate sources,

1. a product-compatible scalar + `2x2` Schur-corrected mixed packet covered by fleet02/B19; or
2. a disjoint hyperbolic-square aggregate packet covered by fleet04/B20; or
3. a separator/diffuse block covered by fleet02/B08 or the regularized determinant theorem;

or else produce a valid QFORM counterexample.

In the third residual alternative the hypotheses may now be strengthened for free to

`|a|>=1/4`, `s_2(S)>=1/4`, `max diag P_range(S)>1/32`,

with `c_i>=1/64` and `||b||<=|a|`.

That is the first genuinely unpaid universal implication after the new descent theorem. A proof is not allowed to condition on a transformed leakage variable and call a marginal cap a conditional cap, or to pay a reciprocal tiny physical minor before aggregation.

## 8. Status

- Full QFORM target: `OPEN / NOT PROVED`.
- `QFORM-SCHUR-THIRD-DIRECTION-RETENTION-v1`: `PROVED`.
- `QFORM-HEAVY-DIAGONAL-SCHUR-DESCENT-v1`: `PROVED`.
- New target-level movement: a whole small-pivot heavy-diagonal minimum-counterexample branch is eliminated by exact dimension descent; the surviving localized branch gains the quantitative collar `|a|,s_2(S)>=1/4`.
- No counterexample is claimed.
- No continuity statement is inferred from the descent theorem.

## 9. Source pins

- brain control snapshot used at run start: `yspennstate/math-research-brain@7975bf56c6cb8fac7a47da6e20ab3fd9a5bfa373`, owner revision `2026-09-22.5`;
- newest completed assigned partner used: `yspennstate/math-open-problems@7530e8c6ffd7284eb9c8acf1d79f36c335bf4fd6`, fleet03/B20 r11;
- low-stable-rank assembly: `yspennstate/math-open-problems@6e3c22b4fcc1038ded1aeff8d107be6a76f7df17`, fleet03/B19;
- two-sided Schur mixed endpoint: `yspennstate/math-open-problems@76cf34fabef3bb9c56f48b5463050cf09f25d0b5`, fleet02/B19;
- separator-conditioned diffuse theorem: `yspennstate/math-open-problems@537a79d82a9af69b8fd35a1086538db339cc74eb`, fleet02/B08;
- aggregate hyperbolic-square theorem: `yspennstate/math-open-problems@1f85677029fc5ae27fc69b278620ae89d789efd2`, fleet04/B20;
- previous fleet02/B20 near-null bank/cap-refund report: `yspennstate/math-open-problems@4106b1e129be9007e16d9b7ba94b2415ba251f86`.
