Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated GPT-6 selector, reasoning-effort selector, guaranteed-duration field, or applied-run attestation, so I do not claim otherwise. F0002 NO MOVEMENT: `gamma_sym = POSITIVE_UNMEASURED -> POSITIVE_UNMEASURED`; inherited stagnation count remains `UNKNOWN`; methods #6 DEFORM TO A SOLVABLE POINT, #14 FIND THE GROUP ACTING, #27 SWAP THE QUANTIFIERS.**

# R03 HARD OUTSIDE — F0002: pivot-row gluing forces every source-scale affine null vector to be almost fully supported

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source gate, and why the stale native title is not reopened

I continued the canonical R03 assignment **F0002**, not the stale native-title F0001 target. Before research I recovered/read:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/F0002.md`;
- newest complete own report `runs/R03/20260918T0710Z_53_f0002_squareclass_neutral_localization.md`;
- the relevant F-intake/attempt history and the terminal F0001 handoff `runs/R03/20260917T1907Z_41_third_stuck_handoff_f0097.md`;
- newest neighboring random-matrix report recovered in this run, `research7_2026-09-17/R7-07/runs/2026-09-18/2026-09-18T062200Z__report.md` (F0003, random-regular adjacency singularity).

The terminal F0001 report source-matched Vu's nonsymmetric Conjecture 2.2 and preserved the exact normalization

`P(det B_n=0) = (1+o(1)) n(n-1) 2^(1-n) = (2+o(1)) n^2 2^(-n)`.

It also preserved the exact nontrivial remainder metric

`r(n)=2^n P(det B_n=0, T_n^c)`, with closure equivalent to `r(n)=o(n^2)`, and handed F0001 off after its third HARD stuck episode. Its retained finite envelope is still `r(10)=222.6104736743...` exactly and `r(11)<=523.4894710902...`. The owner policy says R03 must not return to that target without an explicit reassignment. I therefore do not reset that history merely because the inaccessible native title still names it.

For completeness, I rechecked the requested F0001 source-navigation paper Jain--Sah--Sawhney, arXiv:2010.06554. Its current arXiv abstract still distinguishes the two regimes: for a finite-support law **not uniform on its support** it proves the precise elementary-mechanism asymptotic, while for a law **uniform on its support** it gives only `(1+o_n(1))^n` precision relative to an equal-row/column event plus a sharp compressible analysis. Thus this source check does not remove the recorded F0001 handoff.

The current exclusive R03 source is instead **F0002**: Van H. Vu, *Recent progress in combinatorial random matrix theory*, arXiv:2005.02797, Section 3, Conjecture 3.3. If `A_n` is symmetric with iid uniform Rademacher upper-triangular entries,

`q_n^sym = P(det A_n=0)`,

and the exact source target is

`q_n^sym = (1/2+o(1))^n = 2^(-n+o(n)).`

Fresh primary-literature checks on 2026-09-18 recovered no base-`1/2` theorem. Campos--Jenssen--Michelen--Sahasrabudhe, arXiv:2105.11384 / JAMS 38 (2025), prove `q_n^sym <= exp(-c n)` for an unspecified absolute `c>0`. Yi Han, arXiv:2506.01155 / JLMS 113 (2026), proves for mean-zero unit-variance subgaussian symmetric matrices

`P(rank A <= n-k) <= exp(-c' k n),  1<=k<=c sqrt(n)`.

A bounded fresh exact-model search did not recover a later source-matching theorem. This is dated negative evidence, not a novelty certificate.

The frozen metric remains

`gamma_sym = sup{ gamma in [0,1] : q_n^sym <= 2^{-(gamma-o(1))n} }`.

The checked published theorem statements certify positivity but do not expose a numerical constant usable here, so the honest value remains `POSITIVE_UNMEASURED`; target `gamma_sym=1`.

## 2. State inherited from runs 51--53

Run 51's switching normalization and run 52's affine filter reduce the source-rate conjecture to a symmetric `0/1` problem. For a uniform symmetric `m x m` `0/1` matrix `C_m`, let `E_m^aff` be the event that

1. `corank(C_m)=1`;
2. its kernel is spanned by `v` with `1^T v != 0`;
3. `C_m` has no zero row.

Write `r_m=P(E_m^aff)`. Run 52 proved that the source-rate conjecture is equivalent to

`r_m <= 2^(-m+o(m))`.

Equivalently, in the inverse-core formulation, for an invertible symmetric `0/1` matrix `D`,

`T(D)=#{0!=z in {0,1}^d : z^T D^{-1}z in {0,1}, 1^T D^{-1}z !=1}`

satisfies the source target iff `E T(D_d)=2^{o(d)}`.

Run 53 then proved two facts that are deliberately not reset here:

- there are deterministic cores with exponentially large `T(D)`, namely direct sums of the unimodular block

  `D0=[[1,1,1],[1,1,0],[1,0,1]]`,

  for which `T(D0^{direct-sum k}) >= 3^k-1`;
- the affine remainder from kernel supports up to almost `(1/2)sqrt(m log_2 m)` is already `o(2^-m)`.

The question this run was whether the pointwise-rich obstruction actually survives random cross-block gluing, and whether the support sieve can be pushed from `sqrt(m log m)` all the way to `m-o(m)` without another hyperplane-class enumeration.

## 3. Method #6 — deform the direct-sum obstruction: modular rich cores are superexponentially rare

The exponential pointwise obstruction in run 53 tensorizes only because the core is exactly block diagonal. That structure has enormous codimension in the random symmetric ensemble.

Let `B_b(d)` be the event that a uniform symmetric `d x d` `0/1` matrix is permutation-similar to a block diagonal matrix all of whose blocks have size at most `b`.

Fix a set partition with block sizes `s_1,...,s_k`. Every cross-block upper-triangular entry must be zero. The number of forced independent zero entries is

`M = sum_{i<j} s_i s_j = (d^2 - sum_i s_i^2)/2`.

If every `s_i<=b`, then `sum_i s_i^2 <= b d`, so

`M >= (d^2-bd)/2`.

There are at most `d^d` set partitions, hence

`P(B_b(d)) <= d^d 2^{-(d^2-bd)/2}.`                         (C323)

Since always `T(D)<=2^d`,

`E[T(D) 1_{B_b(d)}] <= 2^{d+d log_2 d-(d^2-bd)/2}.`         (C324)

Consequently, for every fixed `delta>0`, if `b<=(1-delta)d`, the entire contribution of such decomposable cores is

`2^{-Omega_delta(d^2)}`.

In particular, the explicit rich family `D0^{direct-sum k}` from run 53 and every permutation of it is superexponentially negligible under the random-core law. The pointwise obstruction is real, but its simplest tensorization mechanism cannot carry the expected richness.

This does **not** prove that every rich core is close to block diagonal. It removes one concrete extremal mechanism and says what any dangerous rich family must do differently: it must remain rich after a macroscopically connected cross-block deformation.

## 4. Methods #14 and #27 — quotient supports by permutations, then choose pivot rows before the surviving line

This is the main new theorem of the run.

Let `C_m` be uniform symmetric `0/1`, and suppose `E_m^aff` occurs. Let `v` span its kernel and write

`S=supp(v)`,  `s=|S|`,  `t=m-s`.

After a simultaneous permutation of coordinates,

`C_m = [[A,X],[X^T,E]]`,

where `A` is symmetric `s x s`, `X` is `s x t` with iid Bernoulli(1/2) entries, and `E` is symmetric `t x t`; these three collections of upper-triangular/cross entries are independent. Put

`K=ker(A)`, `r=dim K`.

Because `(v_S,0)` spans the **entire** kernel of `C_m`,

`K intersect ker(X^T) = span(v_S)`,                         (4.1)

so this intersection is exactly one-dimensional and its generator has all `s` coordinates nonzero.

Permutation symmetry means that every support `S` of size `s` has the same distribution; we may analyze one support and multiply by `binom(m,s)`. This avoids run 53's union over all possible cube-hyperplane sections.

### C325 — pivot-row gluing lemma

Let `K` be any fixed `r`-dimensional real subspace of `R^s`, and let `x_1,...,x_t` be iid uniform vectors in `{0,1}^s`. Put

`L = K intersect x_1^perp intersect ... intersect x_t^perp`.

Let

`p_s = 2^{-s} binom(s,floor(s/2)).`

Then

`P(dim L=1 and the nonzero vectors of L have full support)`

`<= binom(t,r-1) p_s^(t-r+1),`                              (C325)

with the event impossible if `r>t+1`.

#### Proof

On the event in question, the restrictions of `x_1,...,x_t` to `K` span an `(r-1)`-dimensional subspace of `K^*`. Therefore some `r-1` of them form a basis of that span. Union over the `binom(t,r-1)` choices of pivot positions.

Fix one choice and condition on the pivot rows. If their restrictions are not independent, this choice contributes nothing. If they are independent, their common annihilator in `K` is a line. If that line is not full-support, this choice again contributes nothing. Otherwise let `u` be its full-support generator. Every one of the remaining `t-r+1` independent Bernoulli rows must satisfy

`x . u = 0`.

Writing `2x_i-1` as Rademacher signs turns this into one atom of a Rademacher sum with `s` nonzero coefficients. Erdős--Littlewood--Offord gives

`P(x.u=0) <= p_s`.

Independence of the remaining rows gives `p_s^(t-r+1)`. Summing over pivot sets proves C325. QED.

The key gain over run 53 is conceptual: **sparse directions elsewhere in `ker(A)` no longer hurt the estimate.** We first choose the `r-1` pivot rows that cut `K` down to the actual surviving line; only that line needs to have full support, which is forced by the definition of `S`.

## 5. C326 — source-scale affine singularity is concentrated on support `m-O(m/log m)`

For every fixed `epsilon>0`,

`P(E_m^aff and m-|supp(v)| >= (2+epsilon)m/log_2 m)`

`= o(2^-m).`                                                (C326)

Thus, up to a source-scale negligible event, every nontrivial affine corank-one kernel vector has

`|supp(v)| > m - (2+epsilon)m/log_2 m`.

This moves the rigorous localization from run 53's `~sqrt(m log m)` lower support cutoff to **within `O(m/log m)` of full support**.

### Proof

Fix `epsilon>0` and set

`alpha = epsilon/[2(2+epsilon)]`.

For a fixed support `S`, condition on `A` and let `r=corank(A)`.

### Case I: `r <= alpha t`

By C325,

`P_X((4.1) | A) <= binom(t,r-1) p_s^(t-r+1).`

We sum over supports and over possible `r` only as an upper bound; no independence between different `r` is asserted.

There are two elementary size regimes.

**(i) `s <= m/(log m)^2`.** Here `r<=s=o(m)`, `log_2 binom(m,s)=o(m)`, and the pivot-set factor also has logarithm `o(m)`. On `E_m^aff`, support one and two are impossible (run 53), so `s>=3` and `p_s<=3/8`. Since `t-r+1=m-o(m)`, the contribution is at most

`2^{-(log_2(8/3)-o(1))m}=o(2^-m).`

**(ii) `s > m/(log m)^2`.** Then

`p_s <= C/sqrt(s)`

for an absolute `C`. If `t=o(m)`, the support count satisfies

`log_2 binom(m,t) <= t log_2(em/t)=o(m)`

through the critical range `t >= (2+epsilon)m/log_2 m`, and the pivot factor is also `2^{o(m)}`. At the smallest allowed `t`,

`(t-r+1)(1/2)log_2 s`

`>= (1-alpha)(1+epsilon/2)m - o(m)`

`= (1+epsilon/4)m-o(m).`

Hence the contribution is `2^{-(1+epsilon/4-o(1))m}`.

If instead `t` is not `o(m)`, then `t log s = Omega(m log m)` in this regime, while both the support choice and pivot factors are at most exponential in `m`; the negative Littlewood--Offord exponent is superlinear and the contribution is again `o(2^-m)`.

Thus Case I is source-scale negligible.

### Case II: `r > alpha t`

Because `r<=s`, this inequality forces

`s > alpha t`, hence `s > [alpha/(1+alpha)]m`;

so the principal block has linear size.

Let

`B = J_s - 2A`.

Then `B` is a uniform symmetric Rademacher matrix. Since `rank(B)<=rank(A)+1`,

`corank(B) >= r-1`.

Apply Han's 2026 large-corank theorem. If `r-1 <= c sqrt(s)`, its probability is at most

`exp(-c'(r-1)s)`.

Because `r>alpha t` and `t >= (2+epsilon)m/log_2 m`, the exponent is `Omega(m^2/log m)`.

If `r-1 > c sqrt(s)`, apply Han's theorem at `k=floor(c sqrt(s)/2)` instead; the event `corank(B)>=r-1` implies `corank(B)>=k`, and the probability is

`exp(-Omega(s^(3/2))) = exp(-Omega(m^(3/2))).`

Either estimate remains superexponentially smaller than `2^-m` after union over all at most `2^m` support sets. Hence Case II is also source-scale negligible.

Combining the cases proves C326. QED.

### Why the constant `2` appears

At a nearly full support, one outside coordinate supplies one independent Bernoulli orthogonality equation. A full-support coefficient vector has atom probability about `s^-1/2`. Thus `t` outside coordinates cost approximately

`s^{-t/2}`.

The threshold for this cost to reach `2^-m` is

`t ~ 2m/log_2 m`.

C326 makes this heuristic rigorous after paying for supports, pivot rows, and high internal corank.

## 6. Consequence for the run-52 exact richness reduction

Run 52's exact identity converts `r_m=P(E_m^aff)` into the nontrivial part of the average inverse-core richness. C326 therefore says that the portion of that exact average coming from switching representatives whose affine null vector has at least `(2+epsilon)m/log_2 m` zero coordinates is `o(1)` after the natural `2^m` renormalization.

So the source conjecture has now been reduced further: any source-scale obstruction must live in the **near-full-support window**

`m - |supp(v)| <= (2+o(1)) m/log_2 m`,

up to the already-negligible sectors proved in runs 52--54.

This is still **PARTIAL**. An exponential-rate theorem or a support localization does not prove Vu's base-`1/2` conjecture. The remaining problem is the near-full-support exact-corank-one sector, where only `o(m)` coordinates are absent and ordinary support entropy is too small to help.

## 7. What the three methods actually did

- **#6 DEFORM TO A SOLVABLE POINT:** the explicit exponentially rich direct-sum obstruction from run 53 collapses under generic cross-block deformation; any bounded-block tensorized realization is `2^{-Omega(d^2)}` rare. This removes a concrete bad family from the average problem but does not characterize all rich cores.
- **#14 FIND THE GROUP ACTING:** simultaneous coordinate permutations quotient all supports of a fixed size into one orbit. Conditioning on the actual principal block `A` replaces the old union over cube hyperplanes by one `binom(m,s)` orbit factor.
- **#27 SWAP THE QUANTIFIERS:** instead of choosing a candidate null line and asking all cross rows to hit it, first choose the `r-1` pivot rows that determine the surviving line inside `ker(A)`, then force the remaining rows to annihilate that line. This yields C325 and, after a large-corank split, C326.

No exact checker was manufactured: C323--C326 are symbolic theorem-sized claims with complete proofs on the page, and this run makes no finite enumeration claim.

## 8. Remaining obstruction and next methods

The fixed metric did not move:

`gamma_sym : POSITIVE_UNMEASURED -> POSITIVE_UNMEASURED`.

The inherited stagnation count remains `UNKNOWN`; I do not manufacture a numerical streak.

The simplest remaining source-relevant sector is now:

`E_m^aff` with `corank(C_m)=1` and

`m-|supp(v)| <= (2+epsilon)m/log_2 m`.

A proof must extract another `2^{-o(m)}`-compatible mechanism inside this very thin boundary layer. The natural next question is whether deleting the `t=O(m/log m)` zero coordinates creates a recursive singular principal minor whose **type** can be counted with subexponential multiplicity, rather than merely saying that the minor is singular.

Next methods, all unused so far on F0002: **#3 PROVE SOMETHING STRONGER, #21 ASK WHO ELSE HAS THIS SHAPE, #29 ADD THE POINTS AT INFINITY.** The intended stronger statement is a recursive/projective classification of the near-full-support kernel line under successive principal-coordinate deletion, with comparison to sparse matroid-circuit / random-graph-core arguments rather than another pointwise quadratic Littlewood--Offord estimate.

## 9. Model/scheduler control and permission boundary

The exposed task-control surface still has prompt/title, schedule/timing, enablement, and relative-start controls, but no binding model-family field and no reasoning-effort field. Therefore GPT-6/maximum remains prompt-only and cannot be honestly attested from this run. Making it enforceable would require an authorized product/backend task surface exposing those selectors and authenticated completed-run telemetry.

The repository also preserves that an earlier P26 modification returned `You cannot modify this task`, while a different authorized context later succeeded in updating P26. The lawful workaround for any currently denied task is the owning/authorized task-management context or platform support; no duplicate task, permission bypass, or repository-only pseudo-fix is valid.

No scheduler state, shared root ledger, peer file, email, Drive item, public posting, workflow, purchase, or permission was changed in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R03
  lane: HARD_OUTSIDE
  target: F0002
  source: "Vu, arXiv:2005.02797, Conjecture 3.3"
  status: OPEN_PARTIAL
  fixed_metric: gamma_sym
  metric_before: POSITIVE_UNMEASURED
  metric_after: POSITIVE_UNMEASURED
  movement: NO_MOVEMENT
  stagnation_count: UNKNOWN
  methods: [6, 14, 27]
  new_claims:
    - C323_bounded_block_decomposition_probability
    - C324_bounded_block_richness_contribution
    - C325_pivot_row_gluing_lemma
    - C326_affine_kernel_near_full_support_localization
  strongest_new_quantitative_reduction: "P(E_m^aff and m-|supp(v)| >= (2+epsilon)m/log_2 m)=o(2^-m) for every fixed epsilon>0"
  source_closed: false
  checker_created: false
  next_methods: [3, 21, 29]
  predecessor_F0001: HANDED_OFF_DO_NOT_REOPEN_WITHOUT_REASSIGNMENT
  predecessor_F0097: HANDED_OFF_DO_NOT_REOPEN_WITHOUT_REASSIGNMENT
```
