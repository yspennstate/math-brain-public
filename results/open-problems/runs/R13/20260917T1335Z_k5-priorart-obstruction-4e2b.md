Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED**—not verified GPT-6 maximum. **NO MOVEMENT in the fixed upper-envelope metric `B_R13(n)` this run; a corrected exact finite comparison was added: `K_5^* >= (4+sqrt(142))/9`, narrowing the certified five-column interval to `1.7684861430... <= K_5^* <= 1.9142135624...`. Methods actually used: #22 READ THE FAILURES, #2 ATTACK THE NEGATION FIRST, #8 DISCRETIZE.**

# R13 — Boolean Komlós: recover and certify the missing five-column lower obstruction

Run ID: `20260917T1335Z_k5-priorart-obstruction-4e2b`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and fixed metric

The target remains the **real Boolean** Komlós signing problem: for a deterministic real `m x n` matrix `A` with every column of Euclidean norm at most one, choose `epsilon in {-1,+1}^n` minimizing `||A epsilon||_infinity`. Complex phases, rank-two/vector colorings, and average-case statements are not substitutes.

The frozen tracked quantity remains the complete certified pointwise **upper** envelope `B_R13(n)`. I continued from the newest complete R13 report

`runs/R13/20260917T1323Z_n5-weighted-sharp-7d3c.md`

at commit `8b5dccb9f117a4c36af11ab9ebef53707b2beea0`. That report moved the metric and reset supported stagnation to zero. Therefore this first unchanged upper-envelope run has supported stagnation count **1**.

The retained upper envelope is unchanged:

- `B_R13(1)=1`;
- `B_R13(2)=sqrt(2)`;
- `B_R13(3)=(sqrt(11)+sqrt(2))/3`;
- `B_R13(4)=sqrt(3)`;
- for `5<=n<=75`,
  `B_R13(n) <= min{sqrt(3n/4), (sqrt(2)+1/2)*sqrt(ceil(n/5))}`;
- for `n>=76`, `B_R13(n) < 3 sqrt(2 pi)` from Guo--Fang--Lu.

The later finite entries are upper certificates unless separately proved exact.

Before research I recovered/read the required current surfaces: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042 intake record, the newest R13 report/artifacts, and current neighboring track state. `QUEUE.md` still treats Boolean Komlós as assigned R13 work, not a free reserve target. No shared root or peer file was edited.

## 2. Method #22 — read the failures: an overlooked 2019/2024 source

A fresh exact-constant search found a source not recorded in the preceding R13 finite-`n` history:

- S. B. Belhaouari and R. AlQudah, *The Disprove of the Komlos Conjecture*, Preprints.org v1 (2019), DOI `10.20944/preprints201902.0059.v1`, with v2 posted 9 July 2019;
- later published as S. B. Belhaouari and R. AlQudah, *Evaluation of the Komlos Conjecture Using Multi-Objective Optimization*, **Contemporary Mathematics 5(3) (2024), 3484--3516**, DOI `10.37256/cm.5320244110`.

The published abstract states small-dimensional values including a claimed

`K(5)=(4+sqrt(142))/9`.

The accessible 2019 derivation, however, supplies an explicit five-vector construction and concludes a **lower bound** at this value. I did not recover a source-matching rigorous universal five-column upper bound from that argument. Moreover, the same paper's global conclusion that the Komlós constant diverges is incompatible with the current Guo--Fang--Lu dimension-free Boolean theorem. Therefore I do **not** import its `K(5)=...` equality claim as KNOWN. I instead isolated and independently checked the part that is valid: its explicit five-column obstruction.

Current source navigation was also refreshed on 17 September 2026:

1. Bansal--Jiang, arXiv:`2508.03961v2`, gives the earlier full **Boolean** `\widetilde O((log n)^(1/4))` scale (with the 2026 exposition arXiv:`2608.28452`).
2. Guo--Fang--Lu, arXiv:`2609.11189v1`, submitted 10 September 2026, states the unrestricted deterministic **real Boolean** theorem with constant `3 sqrt(2 pi)`.
3. Guillen--Kobzar, arXiv:`2609.15071`, submitted 14 September 2026, concerns unit-modulus complex phases / rank-two vector discrepancy, not Boolean signs.

A later April 2026 BMC Bioinformatics paper by Kabbani--Belhaouari--Aupetit et al. still cites the 2024 paper's Lemma 1 to state a growing Komlós lower bound. That claim predates and is now incompatible with the September 2026 dimension-free Boolean theorem. This is additional reason to audit the old finite claims directly rather than inherit them wholesale.

## 3. Method #2 — attack the claimed five-dimensional equality first

Let

`K0=(4+sqrt(142))/9`,

`a=K0/4`,

`b=K0/2-1/4=(-1+2 sqrt(142))/36`.

Consider the real `5 x 5` matrix

```
A0 = [  0    -a    -a    -a     a ]
     [ 1/2    0     0     b     b ]
     [-1/2    b     0     0     b ]
     [-1/2   -b     b     0     0 ]
     [-1/2    0    -b     b     0 ].
```

This is the explicit pattern reconstructed from the accessible 2019 five-dimensional construction.

### R13-C30 — exact five-column lower obstruction

Every column of `A0` has Euclidean norm exactly one, and for **every** `epsilon in {-1,+1}^5`,

`||A0 epsilon||_infinity = K0`.

Consequently the true arbitrary-row five-column Komlós constant satisfies

`boxed: K_5^* >= (4+sqrt(142))/9 = 1.7684861430903316...`.

Together with the preceding R13 upper certificate,

`boxed: (4+sqrt(142))/9 <= K_5^* <= sqrt(2)+1/2`.

The current certified interval width is about `0.1457274192827636`.

### Exact verification

The checker works entirely in `Q(sqrt(142))`; no floating-point comparison is used. It verifies:

- all five column norm squares are exactly `1`;
- all 16 antipodal Boolean sign classes (equivalently all 32 signings) have discrepancy exactly `K0`;
- the five rows are active on `2,4,4,4,4` projective classes respectively;
- there are 18 row/class equality incidences, with 14 classes active once and two active twice.

Thus the old source's explicit five-dimensional construction is a valid lower obstruction even though its global divergence conclusion is not usable.

## 4. Method #8 — discretize the *right* five-column problem

The finite-dimensional problem has a useful exact projective-cover reformulation that isolates precisely what remains to prove.

Let

`S_n = {s in {-1,+1}^n : s_1=1}`

be the `2^(n-1)` antipodal sign classes. Define `c_n` as the infimum, over finite families of rows `r_alpha in R^n` satisfying

`for every s in S_n, there exists alpha with |r_alpha . s| >= 1`,

of

`max_{1<=j<=n} sum_alpha r_{alpha,j}^2`.

It is enough to use at most `2^(n-1)` rows, because from any cover one may retain one witness row for each projective class.

### R13-C31 — exact row-cover equivalence

If `K_n^*` denotes the true worst-case Boolean Komlós constant for exactly `n` columns and arbitrary row dimension, then

`boxed: K_n^* = 1/sqrt(c_n)`.

**Proof.** If a matrix has discrepancy at least `D`, divide all its rows by `D`. Every projective class is then covered at level one, while each coordinate energy is at most `1/D^2`; hence `c_n<=1/D^2`, so `D<=1/sqrt(c_n)`. Conversely, any level-one projective cover with maximum coordinate energy `c` becomes a legitimate Komlós matrix after dividing all rows by `sqrt(c)`: its columns have Euclidean norm at most one and every Boolean signing has some row of absolute value at least `1/sqrt(c)`. Taking infima/suprema gives equality. QED.

For `n=5`, the old exactness claim is therefore equivalent to one concrete semialgebraic covering inequality:

`boxed: every projective cover of {-1,+1}^5/{+/-1} has`

`max_j sum_alpha r_{alpha,j}^2 >= c0`,

where

`c0 = 1/K0^2 = 79/98 - 2 sqrt(142)/49 = 0.3197397841708985...`.

The Belhaouari--AlQudah matrix gives equality on the **upper** side of this covering optimization, so the only missing global step is to prove that no other oriented projective cover has energy below `c0`.

This is substantially more precise than the old symmetry heuristic: it says exactly what a computer-assisted or analytic proof of `K_5^*=K0` must certify.

## 5. A new exact local optimality certificate for the obstruction

The lower construction is not merely a random feasible cover. Its projective incidence pattern is exactly dual-optimal inside one natural oriented partition cell.

Index the 16 projective signs lexicographically as

`s_j=(1,s_2,s_3,s_4,s_5)`, `j=0,...,15`, with each tail coordinate ordered `-1,+1`.

Normalize the five rows by `K0`, and assign the 16 classes to the five rows in blocks

`{1,14}`, `{3,7,15}`, `{0,2,4,6}`, `{8,9,10,11}`, `{5,12,13}`,

orienting each assigned sign so its row dot product is `+1`.

Set

`Lambda=diag(x,y,y,y,y)`,

where

`x=-1/7 + 16 sqrt(142)/497`,

`y= 2/7 -  4 sqrt(142)/497`.

Then `x>0`, `y>0`, and `x+4y=1`.

For each of the five blockwise quadratic programs

`min r^T Lambda r  subject to r.t >= 1 for all assigned oriented t`,

the corresponding normalized row of `A0` satisfies the KKT equations with nonnegative multipliers. Writing

`alpha0=1/28-sqrt(142)/994 >0`,

`C=9/98-135 sqrt(142)/27832 >0`,

one may take block multipliers

`(alpha0,alpha0)`, `(C,0,C)`, `(0,C,C,0)`, `(0,C,C,0)`, `(C,C,0)`.

Because each objective is strictly convex and every constraint is linear, these KKT identities prove exact blockwise optimality. Summing the five optimum weighted costs gives

`sum_i r_i^T Lambda r_i = c0`.

Since for any realization of this same oriented partition

`max_j E_j >= sum_j lambda_j E_j`,

this proves:

### R13-C32 — fixed-partition exactness

For the displayed oriented partition, the minimum possible maximum coordinate energy is **exactly** `c0`; the normalized Belhaouari--AlQudah rows attain it.

This does **not** prove the global `n=5` upper bound, because another oriented partition could in principle have smaller maximum coordinate energy. But it makes the remaining obligation sharply finite/combinatorial: defeat all other oriented partitions, rather than optimize this extremizer further.

## 6. What the three routes said

**#22 READ THE FAILURES.** Success: recovered a missed 2019/2024 prior-art source and separated its valid explicit `n=5` obstruction from its unusable global divergence conclusion. The finite lower matrix is real prior art and must be cited in any future R13 finite-`n` manuscript.

**#2 ATTACK THE NEGATION FIRST.** Partial success: the published equality claim was not accepted on authority. Independent exact checking validates only the lower direction at present. I did not find a source-matching rigorous proof that every five-column instance is bounded by `K0`, so `K_5^*=K0` remains **UNVERIFIED**.

**#8 DISCRETIZE.** Success at the structural level: C31 converts exact five-column Komlós into a 16-projective-class row-cover energy problem, and C32 proves the recovered extremal combinatorial type is exactly optimal in its own cell. The missing step is now global comparison across the other oriented cover types.

The natural next run should attack that exact finite cover problem—not add another generic Komlós lemma. A promising implementation is branch-and-bound over oriented projective partitions, using diagonal quadratic dual certificates of the C32 type and symmetry under signed coordinate permutations. If that exhaustive certificate succeeds, it would prove `K_5^*=K0`; if it finds a lower-energy cover, it would refute the 2024 exact `K(5)` claim and produce a stronger lower obstruction/candidate extremizer.

## 7. Exact artifact

Checker:

`artifacts/R13/20260917T1335Z_k5-priorart-obstruction-4e2b_checker.py`

creation/readback commit:

`dac3e6a91c4749108d0e6041ce6217c5a733724d`.

Archived executed output:

`artifacts/R13/20260917T1335Z_k5-priorart-obstruction-4e2b_output.txt`

creation/readback commit:

`1b55e78c545b3e130234cef46502292df67726ff`.

The local execution ended `BELHAOUARI_ALQUDAH_K5_OBSTRUCTION_EXACT_PASS`. This is a **self-check**, not an independent outside audit.

## 8. Status and audit discipline

Status remains **PARTIAL / NO UPPER-METRIC MOVEMENT / NEW EXACT FINITE LOWER OBSTRUCTION + FINITE REDUCTION**.

The two existing R12/P26 PASS audits concern the Guo--Fang--Lu universal `3 sqrt(2 pi)` theorem, not C30--C32 or the previous finite-`n` upper refinements. No finite `n=5` equality is called proved or closed here.

The universal Boolean existence problem is now claimed solved externally by Guo--Fang--Lu, but the R13 frozen metric remains quantitative `B(n)`, so finite and constant optimization remains meaningful. Complex/rank-two results are still excluded from the real Boolean metric.

## 9. Runtime/model-control status

The exposed task interface still has no native model-family or reasoning-effort selector; it exposes prompt/title/schedule/enabled/timing controls only. Therefore `GPT-6 / maximum` remains prompt text rather than authenticated runtime configuration. This run is honestly labeled GPT-5.6 Sol / reasoning UNVERIFIED.

The historical `You cannot modify this task` behavior remains ownership/context dependent. The legitimate remedy is an authorized task/workspace-owner context or platform support exposing the native controls; duplication or permission bypass is not an acceptable workaround. No scheduler change was attempted.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Boolean Komlos; E0042/Bandeira Open Problem 0.1; Bansal-Jiang arXiv:2508.03961v2; Guo-Fang-Lu arXiv:2609.11189v1; Belhaouari-AlQudah 2019/2024 finite-n source recovered"
  target: "complete real Boolean unit-column discrepancy upper envelope B_R13(n)"
  metric_before: "B_R13 upper envelope from 20260917T1323Z_n5-weighted-sharp-7d3c"
  metric_after: "UNCHANGED"
  movement: "no upper-envelope movement"
  auxiliary_exact_comparison: "(4+sqrt(142))/9 <= K_5^* <= sqrt(2)+1/2"
  auxiliary_lower_bound: "K_5^* >= (4+sqrt(142))/9"
  auxiliary_cover_constant_upper_witness: "c_5 <= 79/98 - 2*sqrt(142)/49"
  fixed_partition_result: "same oriented 2,3,4,4,3 partition has exact min max-coordinate energy c0"
  methods: [22, 2, 8]
  status: "PARTIAL"
  stagnation_count: 1
  exact_checker: "artifacts/R13/20260917T1335Z_k5-priorart-obstruction-4e2b_checker.py"
  checker_commit: "dac3e6a91c4749108d0e6041ce6217c5a733724d"
  output: "artifacts/R13/20260917T1335Z_k5-priorart-obstruction-4e2b_output.txt"
  output_commit: "1b55e78c545b3e130234cef46502292df67726ff"
  next_obligation: "globally certify or refute c_5 >= 79/98 - 2*sqrt(142)/49 across every oriented projective cover"
  closure: "NO; C30-C32 are self-checked and finite-n outside audits are absent"
```
