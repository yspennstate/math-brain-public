Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED**—not verified GPT-6 maximum. **METRIC MOVED:** `B_R13(5): sqrt(15)/2 -> sqrt(2)+1/2`, and the propagated certified envelope improves strictly at 22 dimensions `n<=75`. Methods actually used: **#3 PROVE SOMETHING STRONGER, #20 FIND WHY THE ALGORITHM FAILS, #24 FIND THE EXTREMAL OBJECT**.

# R13 — Boolean Komlós: exact weighted four-vector constant and a sharper five-column bound

Run ID: `20260917T1323Z_n5-weighted-sharp-7d3c`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, fixed metric, repository state

The target remains the **real Boolean** Komlós signing problem. For a deterministic real `m x n` matrix `A` with every column of Euclidean norm at most one, choose `epsilon in {-1,+1}^n` minimizing `||A epsilon||_infinity`. Complex phases, rank-two/vector colorings and average-case statements are not substitutes.

The frozen metric is the complete certified pointwise upper-envelope function `B_R13(n)`, with constants and ranges stated. I continued from the newest complete R13 report

`runs/R13/20260917T1134Z_weighted-lift-product-obstructions-4c91.md`

at commit

`1f12a0f38af901bb1c965f12dbab4ce2a8622e77`.

Its retained envelope was

`B_R13(1)=1`,

`B_R13(2)=sqrt(2)`,

`B_R13(3)=(sqrt(11)+sqrt(2))/3`,

`B_R13(n)<=sqrt(3n/4)` for `4<=n<=75`,

and the Guo--Fang--Lu universal entry `B_R13(n)<3 sqrt(2 pi)` for `n>=76`.

The previous run was unchanged and had supported stagnation count `1`. This run moves the metric, so the supported unchanged count resets to `0`.

Before new research I recovered/read the required current surfaces: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current `E0042` Komlós intake record, the newest R13 report and artifacts, the existing R12/P26 Komlós audit records, and current neighboring R-series state. The newest R16 report is now on the unrelated I0036/SLE self-avoiding-walk target, so there is no duplicate neighboring Komlós ownership to merge. No shared root or peer file was edited.

All thirty section-B labels have already appeared somewhere in the long R13 history, so a literally never-used label is no longer available. This run does not repeat the immediately preceding triple `#5,#11,#17`, and the mathematical route is different from the preceding GFL-lift obstruction work.

## 2. Fresh source and prior-art check — 17 September 2026

Current primary-source navigation remains:

1. Bansal--Jiang, `arXiv:2508.03961v2`, full **Boolean** Komlós with the earlier `\widetilde O((log n)^(1/4))` scale; their 2026 exposition is `arXiv:2608.28452v1`.
2. Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, `arXiv:2609.11189v1`, submitted 10 September 2026: the unrestricted deterministic **real Boolean** theorem `||sum epsilon_j v_j||_infinity < 3 sqrt(2 pi)` for Euclidean-unit vectors.
3. Guillen--Kobzar, `arXiv:2609.15071v1`, submitted 14 September 2026: unit-modulus complex phases / rank-two vector discrepancy on real vectors, not Boolean signing.

A fresh bounded search found no correction, withdrawal or later version of Guo--Fang--Lu v1. The universal existence part of the old Komlós conjecture is therefore now a current external theorem claim, and the fleet already has two distinct end-to-end PASS audits of that package: `R12-AUDIT-R13-KOMLOS-01` and `P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11`. Those audits do **not** cover R13's later finite-`n` quantitative refinements.

I also searched the exact phrases `sqrt(2)+1/2` / `1/2+sqrt(2)` together with Komlós/vector balancing/discrepancy, plus weighted four-vector Komlós variants. I found no source matching C27/C28 below. This negative search is not a novelty certificate. The finite witness-cover mechanism is elementary/computer-assisted enough that publication novelty remains **UNVERIFIED**.

## 3. Method #20 — find why the previous algorithm failed

The preceding symbolic balanced-four report made a **too-strong interpretation** of its checker output. It correctly proved

`B_R13(n)<=sqrt(3n/4)`

but then noted that the checker printed `min_chosen_margin = 0` in each residue and described `3n/4` as sitting on the boundary of the certificate.

That tightness interpretation is **corrected here**.

The checker stopped searching the 455 diagonal weights as soon as it found the **first** weight with nonnegative margin. A selected margin of zero therefore showed only that one early certificate was tight; it did **not** show that the best dual certificate for that witness configuration had zero margin.

Optimizing the same finite dual idea instead of stopping at the first success immediately moved the residue-1 case. A first exact-rational search over the old denominator-16 dictionary gave squared threshold

`329/89 = 3.696629... < 15/4`.

The extremal configurations then exposed a clean continuous weight ratio and the algebraic constant below. Thus the old theorem C25/C26 remains valid, but its claimed certificate-tightness interpretation for the `r=1` case is retracted.

## 4. Method #3 — prove a stronger weighted theorem

The useful object is not initially the five-column problem but an exact weighted four-vector problem.

Let `u_1,u_2,u_3,u_4` be arbitrary real vectors in a common Euclidean space satisfying

`||u_1||_2^2 <= 2`,

`||u_2||_2^2, ||u_3||_2^2, ||u_4||_2^2 <= 1`.

Set

`K_*=sqrt(2)+1/2`,

`T_*=K_*^2=9/4+sqrt(2)`.

### R13-C27 — exact weighted four-vector theorem

For every such four vectors there exist Boolean signs `sigma_j` with

`||sigma_1 u_1+sigma_2 u_2+sigma_3 u_3+sigma_4 u_4||_infinity <= K_*`.

Moreover the constant is sharp for this weighted problem.

### Upper-bound proof: finite witness cover

Modulo global negation there are eight Boolean sign classes. Use representatives

`S={(1,x_2,x_3,x_4): x_j in {-1,+1}}`.

Assume for contradiction that every class has discrepancy strictly larger than `K_*`. For each class choose one coordinate row witnessing the violation, orient the class so that the selected row has positive dot product, and group classes selecting the same row into blocks. Divide each selected row by `K_*`. For every oriented sign vector `t_s` in block `B`, the normalized row `r_B` satisfies

`r_B . t_s > 1`.                                           (4.1)

Put

`E_j=sum_B r_{B,j}^2`.

The selected rows are a subset of the ambient coordinate rows, hence

`E_1 <= 2/T_*`,

`E_j <= 1/T_*` for `j=2,3,4`.                              (4.2)

There are finitely many strict inequalities in (4.1). Multiplying every selected row by one common `eta<1`, sufficiently close to one, preserves the non-strict constraints `r_B.t_s>=1` while making every inequality in (4.2) strict.

Now choose a positive diagonal weight

`Lambda=diag(lambda_1,...,lambda_4)`, `sum lambda_j=1`.

For any nonempty subset `U` of a block set

`v_U=sum_{s in U} t_s`.

If `v_U=0`, that block is infeasible because summing its constraints gives `0>=|U|`. Otherwise weighted Cauchy gives

`r_B^T Lambda r_B >= |U|^2/(v_U^T Lambda^{-1} v_U)`.

Define

`L_B(lambda)=max_{empty != U subseteq B} |U|^2/(v_U^T Lambda^{-1}v_U)`.

Therefore

`sum_j lambda_j E_j >= sum_B L_B(lambda)`.                 (4.3)

On the other hand the strict budget bounds give

`sum_j lambda_j E_j < (2 lambda_1+lambda_2+lambda_3+lambda_4)/T_*`.
                                                                    (4.4)

The finite certificate exhausts all `75,905` genuine oriented witness configurations and verifies that each either contains an immediate zero-sum infeasible block or admits one exact weight from a 22-element dictionary satisfying

`sum_B L_B(lambda) >= (2 lambda_1+lambda_2+lambda_3+lambda_4)/T_*`.  (4.5)

The dictionary contains exact rational weights and four algebraic weights in `Q(sqrt(2))`. The latter have one coordinate

`y=sqrt(2)/(3+sqrt(2))=(-2+3sqrt(2))/7`

and the remaining three coordinates

`x=1/(3+sqrt(2))=(3-sqrt(2))/7`.

Every acceptance comparison is exact in `Q(sqrt(2))`; there is no floating-point acceptance test. Equations (4.3)--(4.5) contradict each other and prove the upper bound.

## 5. Method #24 — find the extremal object: C27 is sharp

The clean constant was not guessed from a decimal. It comes with a matching explicit weighted four-vector witness.

Let `a=1/sqrt(2)=sqrt(2)/2` and take the four columns in `R^4`

`u_1=(a,a,a,a)`,

`u_2=(-1/2,-1/2,1/2,1/2)`,

`u_3=(-a,a,0,0)`,

`u_4=(0,0,-a,a)`.

Their squared norms are exactly

`(2,1,1,1)`.

For signs `sigma_j`, rows 1--2 have the form

`a sigma_1 - (1/2)sigma_2 +/- a sigma_3`,

so their maximum absolute value is

`|a sigma_1-(1/2)sigma_2|+a`.

Rows 3--4 similarly give

`|a sigma_1+(1/2)sigma_2|+a`.

For `sigma_1,sigma_2 in {+/-1}`, one of the two inner absolute values is `a+1/2`. Hence every signing has

`||sum_j sigma_j u_j||_infinity = 2a+1/2 = sqrt(2)+1/2`.

Thus the weighted theorem C27 is **exact**:

`K_weighted(2,1,1,1)=sqrt(2)+1/2`.                         (5.1)

This sharpness is for the weighted four-vector problem. It is **not** a lower bound proving that the five-column Komlós constant itself equals the same value.

## 6. R13-C28 — five-column Komlós improvement

Let `v_1,...,v_5` be arbitrary Euclidean-unit columns. For the first pair, choose internal signs `delta_1,delta_2`. Averaging over the four choices gives

`E ||delta_1 v_1+delta_2 v_2||_2^2 = ||v_1||_2^2+||v_2||_2^2 <= 2`.

Hence some deterministic internal pair signing produces

`u_1=delta_1v_1+delta_2v_2`

with `||u_1||_2^2<=2`. Let

`u_2=v_3, u_3=v_4, u_4=v_5`.

Apply C27 and absorb the four outer signs into the original five signs. Therefore

`boxed: B_R13(5) <= sqrt(2)+1/2 = 1.914213562...`.

The previous certificate was

`sqrt(15)/2 = 1.936491673...`,

and the improvement is strict because

`(sqrt(2)+1/2)^2=9/4+sqrt(2)<15/4`

using `sqrt(2)<3/2`.

Again: this is an **upper certificate** for the true five-column constant, not an exact-value claim.

## 7. R13-C29 — propagation to 22 finite dimensions

The already-proved equal-block compiler says that if `B(k)<=K`, then

`B(n)<=sqrt(ceil(n/k)) K`.

Applying it with `k=5` and C28 gives

`B_R13(n) <= (sqrt(2)+1/2) sqrt(ceil(n/5))`.                (7.1)

Compare (7.1) with the preceding balanced-four envelope `sqrt(3n/4)`. Exact arithmetic shows strict improvements at exactly

`n = 5,10,15,20,25,30,35,40,44,45,49,50,54,55,59,60,64,65,69,70,74,75`.

That is **22 pointwise metric movements** this run.

At `n=76`, the five-block squared bound is

`16(9/4+sqrt(2)) > 57`,

while the Guo--Fang--Lu squared universal constant obeys

`18 pi < 18*(22/7) < 57`.

The five-block staircase is nondecreasing thereafter, so it does not move the universal crossover beyond 75.

The complete retained certified envelope is now

`B_R13(1)=1`,

`B_R13(2)=sqrt(2)`,

`B_R13(3)=(sqrt(11)+sqrt(2))/3`,

`B_R13(4)=sqrt(3)`,

and for `5<=n<=75`,

`boxed: B_R13(n) <= min{ sqrt(3n/4), (sqrt(2)+1/2)sqrt(ceil(n/5)) }`,

while for `n>=76`,

`boxed: B_R13(n) < 3 sqrt(2 pi)`

from Guo--Fang--Lu.

The first four finite values retain their earlier exact-value status. C27 is exact in its separate weighted problem. The finite entries from `n>=5` above are upper certificates unless separately proved exact.

## 8. Exact certificate and execution

Checker:

`artifacts/R13/20260917T1323Z_n5-weighted-sharp-7d3c_checker.py`

creation/readback commit:

`cafcbaba23aa11328e4490c0b4340ffc55b5f2a7`

Git blob:

`9195e3a8b5fff8df5e9d5d07a486f4d9d909b1bc`.

Archived executed output:

`artifacts/R13/20260917T1323Z_n5-weighted-sharp-7d3c_output.txt`

creation/readback commit:

`a14a9eb660f5dd16056c0e5b4720a8399c8408de`

Git blob:

`835283da116665d100fd6ccd6a0ad5f4b6cdba27`.

The local exact execution used the same finite enumeration and algebraic acceptance logic and ended

`ALL_EXACT_CHECKS_PASS`.

It verified:

- all `75,905` oriented witness configurations;
- 22 exact certificate weights;
- exact `Q(sqrt(2))` arithmetic for every algebraic comparison;
- the sharp weighted witness with squared column norms `(2,1,1,1)`;
- `B(5)^2: 15/4 -> 9/4+sqrt(2)`;
- the 22 propagated strict-improvement dimensions listed above;
- the `n=76` failure of the five-block staircase to beat the universal entry.

The checker is a **self-check**, not an independent OTHER-track audit.

## 9. What worked, what failed, and next route

- **#20 succeeded decisively:** the old `min_chosen_margin=0` was an algorithmic early-stop artifact, not a true dual optimum. Correcting that interpretation unlocked the new constant.
- **#3 succeeded:** strengthening from “improve `B(5)`” to an exact weighted `(2,1,1,1)` four-vector theorem made the finite geometry transparent and reusable.
- **#24 succeeded:** the exact extremal weighted matrix forced the clean constant `sqrt(2)+1/2`, replacing a decimal/rational search result by a sharp algebraic theorem.

The immediate next high-value route is **not** another denominator refinement of the same 22-weight dictionary. C27 is already sharp as a weighted theorem. Further `B(5)` progress must exploit that the length-`sqrt(2)` aggregate in C27 came specifically from **two original unit columns**, not from an arbitrary norm-`sqrt(2)` vector. The weighted extremizer need not decompose into two unit columns in a way that preserves its hard sign geometry for both pair sum and pair difference. That additional decomposition structure is exactly the information discarded by C28 and is the next plausible source of a strict five-column improvement.

A second useful direction is a genuinely weighted five-block theorem for balanced budgets `(q+1,...,q)`. The equal-block C29 staircase cannot beat the universal constant at `n=76`; a residue-sensitive five-vector theorem would be required to move that crossover.

Because the fixed metric moved, this is not a stuck run and the unchanged count is reset to zero.

## 10. Audit and closure status

The universal Guo--Fang--Lu theorem package retains its two distinct PASS audits, but they do not cover C27--C29. No new finite-dimensional outside audit was fabricated or requested in another track from this worker.

Status of this run:

**PARTIAL QUANTITATIVE REFINEMENT / METRIC MOVED / EXACT FINITE SELF-CHECK PASS / OUTSIDE AUDITS PENDING.**

No closure or paper-folder claim is made for C27--C29.

## 11. Model / scheduler control status

The runtime did **not** authenticate GPT-6 maximum. The exposed task/scheduler schema still offers prompt/title/schedule/enabled/timing controls but no model-family field, no reasoning-effort field and no authenticated applied-effort telemetry. Therefore `GPT-6 / maximum` remains a request in prompt text only from this interface.

The repository's current deployment record also distinguishes contexts: the historical `You cannot modify this task` response for P26 was context/ownership-dependent, and a later authorized P/C context successfully updated P26, while another exposed context denied R-series edits. The legitimate remedy for a denied native task remains the authorized task/workspace-owner context or platform support exposing the necessary native controls. No duplication, permission bypass or scheduler modification was attempted in this run.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Boolean Komlos; E0042/Bandeira Open Problem 0.1; current Boolean source navigation Bansal-Jiang arXiv:2508.03961v2 and Guo-Fang-Lu arXiv:2609.11189v1; Guillen-Kobzar arXiv:2609.15071v1 is complex/rank-two only"
  target: "Every deterministic real m-by-n unit-column matrix admits Boolean signs with uniformly bounded l_infinity discrepancy; quantitative pointwise B(n) refinement"
  metric: "complete rigorously certified pointwise upper-envelope B_R13(n), with constants and ranges"
  before: "B1=1; B2=sqrt2; B3=(sqrt11+sqrt2)/3; B(n)<=sqrt(3n/4) for 4<=n<=75; B(n)<3sqrt(2pi) for n>=76"
  after: "B1=1; B2=sqrt2; B3=(sqrt11+sqrt2)/3; B4=sqrt3; for 5<=n<=75, B(n)<=min(sqrt(3n/4),(sqrt2+1/2)*sqrt(ceil(n/5))); B(n)<3sqrt(2pi) for n>=76"
  movement: "YES: B5 sqrt(15)/2 -> sqrt2+1/2; 22 finite dimensions strictly improved by propagation"
  strict_improvement_dimensions: [5,10,15,20,25,30,35,40,44,45,49,50,54,55,59,60,64,65,69,70,74,75]
  unchanged_count: 0
  status: "PARTIAL_QUANTITATIVE / exact self-check PASS / outside finite-claim audits pending; universal GFL package separately has 2/2 audits"
  methods: [3,20,24]
  corrections:
    - "Prior C25/C26 proof remains valid, but its selected zero-margin output did not establish certificate optimality because the checker stopped at the first passing dual weight."
  new_claims:
    - "R13-C27 PROVED (computer-assisted finite upper core + explicit lower witness): exact weighted four-vector constant for squared norm budgets (2,1,1,1) is sqrt(2)+1/2."
    - "R13-C28 PROVED: B_R13(5)<=sqrt(2)+1/2."
    - "R13-C29 PROVED: B_R13(n)<=(sqrt(2)+1/2)sqrt(ceil(n/5)); combined envelope improves 22 dimensions through n=75."
  exact_evidence:
    checker_path: "artifacts/R13/20260917T1323Z_n5-weighted-sharp-7d3c_checker.py"
    checker_commit: "cafcbaba23aa11328e4490c0b4340ffc55b5f2a7"
    checker_blob: "9195e3a8b5fff8df5e9d5d07a486f4d9d909b1bc"
    output_path: "artifacts/R13/20260917T1323Z_n5-weighted-sharp-7d3c_output.txt"
    output_commit: "a14a9eb660f5dd16056c0e5b4720a8399c8408de"
    output_blob: "835283da116665d100fd6ccd6a0ad5f4b6cdba27"
    oriented_configurations: 75905
    certificate_weights: 22
    result: "ALL_EXACT_CHECKS_PASS"
  audits:
    gfl_universal: "R12 PASS + P26 PASS; does not cover C27-C29"
    finite_new_claims: "PENDING"
  model_runtime: "GPT-5.6 Sol; reasoning UNVERIFIED; no exposed scheduler model/reasoning selector"
```
