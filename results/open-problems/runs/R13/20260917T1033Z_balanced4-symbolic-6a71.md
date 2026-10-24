Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED**—not verified GPT-6 maximum. **Metric moved on 38 dimensions: the certified envelope improves strictly at `n = 5,10,11,13,15,17,19,22,23,25,26,29,31,33,34,37,38,39,41,43,46,47,50,51,53,55,57,58,59,61,62,65,67,69,71,73,74,75`; the full finite envelope collapses to `B_R13(n) <= sqrt(3n/4)` for every `4 <= n <= 75`. Methods used: #16 COMPUTE EVERY SMALL CASE, #24 FIND THE EXTREMAL OBJECT, #27 SWAP THE QUANTIFIERS.**

# R13 — Boolean Komlos: symbolic balanced four-block theorem

Run ID: `20260917T1033Z_balanced4-symbolic-6a71`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and fixed metric

The target remains the **real Boolean** Komlos signing problem: for every deterministic real `m x n` matrix `A` with column Euclidean norms at most one, choose `epsilon in {-1,+1}^n` so that `||A epsilon||_infinity` is small. Complex phases, rank-two/vector colorings and average-case bounds do not replace this target.

The frozen metric remains the complete pointwise certified upper-bound function `B_R13(n)`. I use `B_R13` only for the retained **certified upper envelope**; it is not a claim that every displayed value is the exact optimal finite-`n` Komlos constant.

I continued from the newest complete R13 report

`runs/R13/20260917T094249Z_weighted-boundary-73-74-5d7c.md`,

which had

- the exact values/certificates retained at `n=1,2,3,4`;
- the small-dimensional certificates through `n=9`;
- the block-composition envelope through `n=72`;
- weighted four-vector improvements `B_R13(73)<=sqrt(55)` and `B_R13(74)<=sqrt(56)`;
- the Guo--Fang--Lu universal entry `3 sqrt(2 pi)` from `n=75` onward.

Before research I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current `E0042` Komlos intake statement, the newest R13 report and artifacts, the existing R12 and P26 Komlos audit records, and current neighboring R-series state. R12 and R16 have both rotated to different source problems, so neither currently duplicates this R13 target. I did not edit shared roots or peer files.

All section-B labels have appeared somewhere in the long R13 history, so a literally unused label no longer exists. This run does **not** repeat the preceding triple `#3,#18,#30`, and the mathematical route is new relative to that run.

## 2. Current source status — fresh check, 17 September 2026

The source navigation remains:

1. Bansal--Jiang, *Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlos Bounds Beyond Banaszczyk*, arXiv:2508.03961v2: full Boolean signing, with `\widetilde O((log n)^(1/4))` Komlos discrepancy.
2. Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189v1, submitted 10 September 2026: claims the unrestricted deterministic **real Boolean** theorem with
   `||sum epsilon_j v_j||_infinity < 3 sqrt(2 pi)`
   for every finite family of Euclidean-unit vectors.
3. Guillen--Kobzar, *The Komlos conjecture for complex discrepancy*, arXiv:2609.15071v1, submitted 14 September 2026: allows unit-modulus complex phases; on real vectors this is rank-two/vector discrepancy, not Boolean signing.

Fresh bounded searches on 17 September found no primary correction or withdrawal of Guo--Fang--Lu v1. A targeted search for `sqrt(3n/4)`, `3n/4 Komlos discrepancy`, weighted four-vector discrepancy, and exact finite-`n` Komlos constants did not surface the theorem below. This is **not** a novelty certificate. The weighted mechanism is elementary enough that it may be folklore; novelty remains **UNVERIFIED**.

The universal Guo--Fang--Lu package already has the two distinct internal audits `R12-AUDIT-R13-KOMLOS-01=PASS` and `P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11=PASS`. Those audits do not cover this new finite-dimensional strengthening.

## 3. New-method work

### #16 — COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE

The preceding weighted-boundary run checked only the two budget vectors `(19,18,18,18)` and `(19,19,18,18)`. I tested the next balanced case `(19,19,19,18)` and found that squared threshold `56` fails in the same finite dual dictionary, but `225/4 = 56.25` passes exactly. That number is not accidental:

`225/4 = 3*75/4`.

Testing the smaller balanced patterns showed the same formula. The right object is therefore not a list of boundary dimensions but a four-residue symbolic theorem.

### #24 — FIND THE EXTREMAL OBJECT

The exact finite search reports zero dual margin for explicit witness configurations in every residue class. Thus the value `3n/4` sits on the boundary of the present exact witness-cover certificate rather than being a loose decimal fit. I use this only as a **certificate-tightness observation**; it is not asserted as a lower bound on the true finite-`n` Komlos constant.

### #27 — SWAP THE QUANTIFIERS

Instead of checking one `q` after another, I changed the finite statement from

`for every q >= 1 and every witness pattern, find a dual weight`

to

`for every witness pattern, find one dual weight controlling both q=1 and q=infinity`.

Because the required ratio is a fractional-linear function of `q`, those two endpoints control every integer `q>=1`. This removes the infinite parameter from the finite computation.

## 4. The finite four-vector witness reduction

Let `u_1,...,u_4` be arbitrary real vectors in a common Euclidean space and suppose

`||u_j||_2^2 <= C_j`.

There are eight Boolean sign classes modulo global negation. Use the canonical representatives

`S = {(1,x_2,x_3,x_4): x_i in {-1,+1}}`.

Fix a squared discrepancy threshold `T`. Suppose, toward contradiction, that every antipodal sign class has discrepancy strictly larger than `sqrt(T)`. For every class choose one coordinate row witnessing the violation, orient the class so that the selected row has positive dot product, and group sign classes that selected the same row into a block. Divide each distinct selected row by `sqrt(T)`. If `B` is one block, its normalized witness row `r_B` satisfies

`r_B . t_s > 1` for every oriented sign vector `t_s` in `B`.

Let

`E_j = sum_B r_{B,j}^2`.

The selected rows are a subset of the ambient coordinate rows of the four vectors, hence

`E_j <= C_j/T`.

Because there are finitely many strict inequalities, multiply all selected rows by one common factor `eta<1` sufficiently close to one. The constraints remain `>=1`, while all energy bounds become strict:

`E_j < C_j/T`.

Now choose a positive diagonal weight

`Lambda = diag(lambda_1,...,lambda_4)`, `sum lambda_j = 1`.

For every nonempty subset `U` of a block `B`, put

`v_U = sum_{s in U} t_s`.

If `v_U=0`, the constraints of that block are immediately infeasible because summing them gives `0 >= |U|`. Otherwise weighted Cauchy gives

`(r_B^T Lambda r_B)(v_U^T Lambda^{-1} v_U) >= |U|^2`.

Therefore define the exact block lower bound

`L_B(lambda) = max_{empty != U subseteq B} |U|^2 / (v_U^T Lambda^{-1} v_U)`.

Summing over blocks yields

`sum_j lambda_j E_j >= sum_B L_B(lambda)`.

Thus the witness configuration is impossible whenever one can choose `lambda` with

`sum_B L_B(lambda) >= (sum_j lambda_j C_j)/T`.      (4.1)

This is the same arbitrary-ambient-dimension reduction used in the prior exact four-vector work; the new step is to make the budget parameter symbolic rather than instantiate it separately.

## 5. R13-C25 — symbolic balanced four-vector theorem

Write

`n = 4q + r`, with `q>=1` and `r in {0,1,2,3}`.

After relabeling the four vectors, set the balanced squared-norm budgets

`C_j(q,r) = q+1` for `1 <= j <= r`,

and

`C_j(q,r) = q` for `r < j <= 4`.

Set

`T(q,r) = 3(4q+r)/4 = 3n/4`.      (5.1)

### Theorem C25

For every `q>=1`, every `r in {0,1,2,3}`, and every four real vectors satisfying those coordinatewise squared-norm budgets, there are Boolean signs `sigma_1,...,sigma_4` such that

`||sum_{j=1}^4 sigma_j u_j||_infinity^2 <= 3(4q+r)/4`.      (5.2)

Equivalently,

`||sum sigma_j u_j||_infinity <= sqrt(3n/4)`.

### Symbolic reduction of the infinite q-quantifier

Restrict the dual search to the same exact dictionary used in the previous four-vector certificates:

`lambda_j = a_j/16`,

where `a_j` are positive integers with `a_1+...+a_4=16`. There are exactly `455` such weights.

For a fixed witness configuration and a fixed `lambda`, let

`L(lambda)=sum_B L_B(lambda)`

and

`s = sum_{j=1}^r lambda_j`.

Then the right side of (4.1) is

`R_q(lambda) = (q+s)/(3q+3r/4)`.      (5.3)

The key identity is

`R_q(lambda) - 1/3 = (s-r/4)/(3q+3r/4)`.      (5.4)

Hence, for every integer `q>=1`, `R_q(lambda)` lies between `R_1(lambda)` and `1/3`. Consequently it is enough, for every finite witness configuration, to find one rational `lambda` satisfying

`L(lambda) >= max(1/3, R_1(lambda))`.      (5.5)

That one weight then proves (4.1) **simultaneously for every q>=1** in the given residue class.

## 6. Exact finite certificate

The checker exhausts the complete finite witness universe:

- `4140` set partitions of the eight antipodal sign classes;
- `75,905` genuine oriented partition configurations after fixing one orientation per block;
- all `455` positive diagonal weights with denominator `16`.

For each residue `r=0,1,2,3`, every one of the `75,905` configurations either contains an immediately infeasible zero-sum subset or receives a rational weight satisfying (5.5) exactly.

The executed output is:

- `PASS residue 0 configs 75905`
- `PASS residue 1 configs 75905`
- `PASS residue 2 configs 75905`
- `PASS residue 3 configs 75905`
- `ALL_EXACT_CHECKS_PASS`.

The minimum chosen margin is exactly zero in every residue, which is the certificate-tightness observation mentioned under method #24.

Checker:

`artifacts/R13/20260917T1033Z_balanced4_symbolic_checker.py`

creation commit:

`b7473354d0ab4204e978ec54d44c1eac65916f51`

executed-source SHA-256:

`aa9a42fde90e08d526a9d3ea7abeaa039cedcea23f9f283e591acfba3b8c1842`

Archived stdout:

`artifacts/R13/20260917T1033Z_balanced4_symbolic_output.txt`

creation commit:

`f018480313f2a0b64da21260780eacdf45ded63a`

output SHA-256:

`b439674c3471698b952df1812f267164d113b9649e07c8c1fe3b13a320fe8743`

Both files were read back at their actual creation commits. This is a **self-check**, not an outside audit.

## 7. R13-C26 — balanced four-block Komlos compiler

Let `A` have `n>=4` columns `v_1,...,v_n`, each with Euclidean norm at most one. Write `n=4q+r` with `q>=1` and `0<=r<=3`. Partition the columns into four blocks: `r` blocks of size `q+1`, and `4-r` blocks of size `q`.

For one block `G`, choose independent internal signs `delta_j`. Then

`E ||sum_{j in G} delta_j v_j||_2^2 = sum_{j in G} ||v_j||_2^2 <= |G|`.

Therefore some deterministic internal signing gives an aggregate

`u_G = sum_{j in G} delta_j v_j`

with

`||u_G||_2^2 <= |G|`.

Do this independently for the four blocks. Their squared-norm budgets are exactly the balanced vector `C(q,r)` in C25. Apply C25 to obtain outer signs `sigma_G` with

`||sum_G sigma_G u_G||_infinity^2 <= 3n/4`.

Absorb each outer sign into the corresponding internal block signs. The result is one Boolean signing of all original columns. Thus

`boxed: B_R13(n) <= sqrt(3n/4) for every n>=4.`      (7.1)

This is uniform in the row dimension and uses no random-input assumption; randomness is only an averaging device to prove existence of the internal block signings.

## 8. Complete retained pointwise envelope

The preceding finite table is now dominated by a much simpler expression. The exact checker compares (7.1) with every entry of the immediately preceding R13 envelope and finds **38 strict improvements**:

`n = 5,10,11,13,15,17,19,22,23,25,26,29,31,33,34,37,38,39,41,43,46,47,50,51,53,55,57,58,59,61,62,65,67,69,71,73,74,75`.

There are 34 equality dimensions in `4<=n<=74`; no preceding finite entry is better.

The most visible changes are

- `B_R13(5): 2 -> sqrt(15)/2`;
- `B_R13(10): 2 sqrt(2) -> sqrt(15/2)`;
- `B_R13(73): sqrt(55) -> sqrt(219)/2`;
- `B_R13(74): sqrt(56) -> sqrt(111/2)`;
- `B_R13(75): 3 sqrt(2 pi) -> 15/2`.

For the crossover, the finite squared bound is `3n/4` and the Guo--Fang--Lu squared constant is `18 pi`.

At `n=75`, using `pi > 223/71`,

`225/4 < 18*(223/71) < 18 pi`,

so `15/2 < 3 sqrt(2 pi)`.

At `n=76`, using `pi < 22/7`,

`18 pi < 18*(22/7) = 396/7 < 57 = 3*76/4`.

Therefore the complete retained certified envelope is

`B_R13(n) = 1` for `n=1`,

`B_R13(n) = sqrt(2)` for `n=2`,

`B_R13(n) = (sqrt(11)+sqrt(2))/3` for `n=3`,

`B_R13(n) = sqrt(3n/4)` for `4 <= n <= 75`,

`B_R13(n) = 3 sqrt(2 pi)` for `n >= 76`,

where equality signs here define the **chosen certified envelope**, not the unknown optimal finite constants. The `n=1,2,3,4` entries retain their earlier exact-value status; the later finite entries are upper certificates unless separately proved exact.

## 9. What this does and does not solve

Guo--Fang--Lu already claim the full universal Boolean Komlos conjecture with constant `3 sqrt(2 pi)`. This run does not improve their universal constant as `n -> infinity`; it strengthens the certified finite-`n` envelope through `n=75`.

The symbolic four-block compiler itself grows like `sqrt(n)`, so from `n=76` onward the universal theorem is better. The exact zero-margin witness configurations show that the current 455-weight finite dual dictionary is already on its boundary. A further finite improvement should therefore not be another denominator-16 re-run of the same certificate. The next useful routes are intersection-aware multi-block certificates, a stronger four-vector block lower bound, or a construction showing that the certificate-tight configurations are genuine primal extremizers.

This is **PARTIAL / METRIC MOVED / exact self-check PASS / independent audits pending**, not closed under the fleet closure rule.

## 10. Runtime/model control and scheduler permissions

The exposed task interface still provides prompt/title/schedule/enabled/timing controls but no native model-family or reasoning-effort field. Therefore `GPT-6 / maximum` remains prompt-only; this run cannot authenticate that setting and does not claim it.

The repository record also shows that a historical `You cannot modify this task` response for P26 was context/ownership dependent: P26 was later editable from an authorized P/C context, while R-series edits were denied from another exposed context. The legitimate fix is an authorized task/workspace-owner context or platform support that exposes the native controls. I did not attempt a scheduler modification, duplicate task, permission bypass, email, Drive write, public post, workflow execution or paid-compute action.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Boolean Komlos; E0042/Bandeira Open Problem 0.1; current Boolean source navigation Bansal-Jiang arXiv:2508.03961v2 and Guo-Fang-Lu arXiv:2609.11189v1; Guillen-Kobzar arXiv:2609.15071v1 is complex/rank-two only"
  target: "complete rigorously certified pointwise real-Boolean discrepancy upper envelope B_R13(n)"
  status: "PARTIAL"
  metric_before: "previous piecewise envelope with weighted n=73,74 entries and universal 3sqrt(2pi) from n=75"
  metric_after: "B_R13(1)=1; B_R13(2)=sqrt2; B_R13(3)=(sqrt11+sqrt2)/3; B_R13(n)=sqrt(3n/4) for 4<=n<=75; B_R13(n)=3sqrt(2pi) for n>=76"
  movement: "38 strict finite-dimensional improvements; 34 equal retained dimensions in 4..74; no regression"
  methods: [16,24,27]
  theorem_ids: ["R13-C25", "R13-C26"]
  exact_checker: "artifacts/R13/20260917T1033Z_balanced4_symbolic_checker.py @ b7473354d0ab4204e978ec54d44c1eac65916f51"
  exact_output: "artifacts/R13/20260917T1033Z_balanced4_symbolic_output.txt @ f018480313f2a0b64da21260780eacdf45ded63a"
  exact_output_status: "ALL_EXACT_CHECKS_PASS"
  audits:
    universal_GFL_R12: "R12-AUDIT-R13-KOMLOS-01=PASS"
    universal_GFL_P26: "P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11=PASS"
    new_balanced4_P26: "PENDING"
    new_balanced4_other: "PENDING"
  prior_art: "fresh bounded search 2026-09-17; no exact matching finite theorem located; novelty UNVERIFIED"
  stagnation_count: 0
  next_obligation: "use a genuinely stronger certificate than the denominator-16 balanced four-block dual if attempting finite improvement beyond this boundary"
```
