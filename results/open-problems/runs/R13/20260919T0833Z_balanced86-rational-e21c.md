Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper-envelope metric** `B_R13(n)` (`B_R13(86)=728151/100000=7.28151` remains unchanged; fixed-upper unchanged count `1 -> 2`), but the **explicit finite obstruction at the same source dimension moved** after correcting the literature baseline: `K_86^* >= 1+7 sqrt(2)/8 = 2.237436867... -> K_86^* >= 2259253/10^6 = 2.259253`. Section-B methods actually used: **#11 DUALIZE, #6 DEFORM TO A POINT YOU CAN SOLVE, #25 COUNT THE SAME THING TWICE.**

Run ID: `20260919T0833Z_balanced86-rational-e21c`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Worker: R13 HARD OUTSIDE.

## 1. Continuity, ownership, source status, and exact metric state

I continued from the newest complete R13 report

`runs/R13/20260919T0648Z_algebraic-n6-template-b91e.md`

rather than restarting the Komlos source or re-deriving the previous directional-TV bounds. Before new mathematics I reread/reconciled the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R13 report and checker, the current I0091 source-reconciliation record, the relevant neighboring discrepancy history (especially the retired R02 sign-matrix/covering-code work), and the current intake alias for I0091. `QUEUE.md` still treats Boolean Komlos/R13 as assigned rather than an unassigned reserve target. No ownership collision was found. I did not edit shared roots or peer-track files.

The original qualitative real-Boolean Komlos source is **KNOWN / RESOLVED_IN_LITERATURE_2026_09**, not OPEN. Current primary-source checks on 19 September 2026 confirm:

- Guo--Fang--Lu, `arXiv:2609.11189v1`, submitted 10 September 2026, prove the genuine real-Boolean universal bound `3 sqrt(2 pi)`;
- Karingula--Lovett, ECCC `TR26-188`, 17 September 2026, give an independent elementary constant-36 proof;
- Bansal--Jiang, `arXiv:2508.03961v2`, remains the earlier polylogarithmic real-Boolean comparison source;
- Kunisky, *SIAM J. Discrete Math.* 37 (2023), arXiv:2111.02974, supplies the unsatisfiable-matrix lower-obstruction mechanism used below.

Thus this report does **not** claim to solve the qualitative conjecture. R13 remains a quantitative finite-dimensional track for

\[
K_n^*:=\sup_{m\ge1}\sup_{\substack{A\in\mathbb R^{m\times n}\\\|A_{\cdot j}\|_2\le1}}
\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty.
\]

### Fixed upper metric

The complete rigorously proved upper metric is **unchanged** from the predecessor chain. To avoid silently replacing the metric by the `n=86` headline, its top-level definition remains

\[
B_{R13}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},\;T_5\sqrt{\lceil n/5\rceil},\;G_0(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{\rm LT}(n),L_{\rm TB}(n)\},&5\le n\le85,\\
\min\{G_0(n),H(n),J(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{\rm LT}(n),L_{\rm TB}(n)\},&n\ge86.
\end{cases}
\]

Here

\[
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13},
\qquad
L_{\rm TB}(n)=\max\left\{\frac{728151}{100000},\frac n{\sqrt{140}}\right\},
\]

and `G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_LT` retain **exactly** their constants, logarithmic/exponential tail factors, integer ceilings/infima, zero conventions, and parameter domains from the immutable metric report `runs/R13/20260919T0334Z_tilted-binomial-c7a2.md` and its retained predecessors. No old certified branch is removed or weakened in this run. In particular

\[
\boxed{K_{86}^*\le B_{R13}(86)=\frac{728151}{100000}=7.28151}
\]

is unchanged, so the fixed-upper unchanged count is now `2`.

## 2. A necessary correction to the finite lower-obstruction history

The preceding R13 reports preserved small-dimensional lower comparisons such as the exact `K_5^*=T_5`, the new six-column algebraic obstruction, and older `K_11,K_12` numbers, but that list was incomplete as a comparison against the literature.

Kunisky's published Theorem 1.1 states

\[
K(2^k)\ge 2^{-k/2}+\sum_{a=1}^k2^{-a/2}.
\]

For `k=6`, this simplifies exactly to

\[
K(64)\ge 1+\frac{7\sqrt2}{8}
=2.237436867076458\ldots.
\]

Zero-padding 22 columns (and rows if one insists on a square representative) therefore already gives the **known** comparison

\[
K_{86}^*\ge 1+\frac{7\sqrt2}{8}.
\]

This is a correction of R13's comparison history, **not** a new result of this run. The new theorem below starts from that corrected baseline and moves it.

## 3. Method #11 — DUALIZE: turn row-template scaling into a support-load problem

Kunisky's unsatisfiable matrices suggest separating the combinatorial row supports from their magnitudes. Suppose row `i` has support `S_i`. Normalize a prospective common row `l1` mass to one and choose nonnegative magnitudes `x_ij` with

\[
\sum_{j\in S_i}x_{ij}\ge1.
\]

The squared load of column `j` is `\sum_i x_{ij}^2`. Let

\[
L^*:=\min_x\max_j\sum_i x_{ij}^2.
\]

The natural Lagrange/SOCP dual puts weights `\mu_j>0`, `\sum_j\mu_j=1`, on the column loads. Rowwise minimization gives

\[
\min_{\substack{x_{ij}\ge0\\\sum_{j\in S_i}x_{ij}\ge1}}
\sum_{j\in S_i}\mu_jx_{ij}^2
=
\frac1{\sum_{j\in S_i}\mu_j^{-1}},
\]

with minimizer

\[
x_{ij}=\frac{\mu_j^{-1}}{\sum_{k\in S_i}\mu_k^{-1}}.
\]

Hence the dual scouting functional is

\[
\max_{\mu\in\Delta}
\sum_i\frac1{\sum_{j\in S_i}\mu_j^{-1}}.
\]

I used this only as a **route-finding device**. Numerical optimization is not part of the theorem and no numerical-optimizer output is used as evidence. Its purpose was to identify rational support weights worth certifying exactly.

Outcome of #11: **success as a discovery route**. It indicated that the power-of-two complete tree is not the best finite obstruction at the owner-relevant dimension 86 once entry magnitudes are allowed to vary, and it produced a robust rational target well above the published zero-padded `K(64)` value.

## 4. Method #6 — DEFORM: replace the complete 64-leaf tree by a balanced 86-leaf tree

Let `T_86` be the recursively balanced full binary tree with 86 leaves: a node with `s` descendant leaves splits into children with `floor(s/2)` and `ceil(s/2)` leaves. It has 85 internal vertices. Add Kunisky's CNF-to-NAE dummy variable, so the resulting clause-variable sign matrix has exactly 86 rows and 86 columns.

Index column `0` by the dummy variable and index internal vertices `1,...,85` in preorder. Every row corresponds to a leaf. Its dummy sign is `+1`; on an internal-vertex column the row is nonzero exactly when the leaf descends from that vertex, with sign `+1` on the left child and `-1` on the right child.

The 86 leaf depths are exactly

\[
42\text{ leaves of depth }6,
\qquad
44\text{ leaves of depth }7.
\]

Set

\[
q:=\frac{2259253}{10^6}=2.259253.
\]

The rational magnitude certificate uses 25 automorphism-orbit weights. For each listed orbit `O` all columns in `O` receive the same positive integer `W_j`:

```
(0,1):4857310
(2,44):3434640
(3,45):2440010
(4,46):1735453
(5,9,47,51):1227150
(6,10,48,52):876679
(7,11,49,53):858684
(8,12,50,54):598370
(13,55):1715181
(14,56):1222224
(15,57):873158
(16,58):855236
(17,59):595968
(18,60):1203336
(19,21,61,63):850888
(20,22,62,64):592938
(23,65):2417246
(24,34,66,76):1709252
(25,35,67,77):1217998
(26,36,68,78):870139
(27,37,69,79):852278
(28,38,70,80):593906
(29,39,71,81):1199176
(30,32,40,42,72,74,82,84):847945
(31,33,41,43,73,75,83,85):590887
```

If row `i` has support `S_i`, define its entry magnitude on column `j in S_i` by

\[
|A_{ij}|=
q\,\frac{W_j^{-1}}{\sum_{k\in S_i}W_k^{-1}},
\]

and give it the tree sign described above. Entries outside `S_i` are zero.

Immediately,

\[
\sum_j|A_{ij}|=q
\qquad\text{for every row }i.
\]

The exact-arithmetic checker evaluates every column's squared Euclidean norm and proves

\[
\max_j\sum_i A_{ij}^2
=0.99999973499296964884058904791877794265\ldots<1,
\]

with exact positive rational slack (the decimal is display-only). Therefore every column has Euclidean norm strictly below one.

Outcome of #6: **success**. The deformation from 64 equal-depth leaves to an 86-leaf balanced tree, followed by nonuniform rational magnitudes, gives a strictly larger source-dimension obstruction.

## 5. Method #25 — COUNT THE SAME THING TWICE: exact projective partition

It remains to prove that every Boolean signing aligns with a row template, so that some coordinate of `A epsilon` attains that row's full `l1` mass `q`.

Work projectively modulo global sign. Two distinct leaves of a rooted binary tree diverge at their first different child. At the corresponding internal-vertex column their row templates have opposite nonzero signs. Hence **no projective signing can match two different rows**.

A leaf at depth `d` fixes exactly `d` non-dummy signs, so its projective matching cylinder has mass `2^{-d}`. The balanced tree has 42 leaves at depth 6 and 44 at depth 7, and therefore

\[
42\,2^{-6}+44\,2^{-7}
=\frac{84+44}{128}=1.
\]

Thus the 86 pairwise-disjoint row cylinders have total projective mass one. They partition all projective Boolean signings. Equivalently, every `epsilon in {+-1}^{86}` matches exactly one row up to global sign.

For that row `i`, all nonzero summands in `(A epsilon)_i` have the same sign, so

\[
|(A\varepsilon)_i|
=\sum_j|A_{ij}|=q.
\]

Therefore

\[
\boxed{
K_{86}^*\ge\frac{2259253}{10^6}=2.259253.}
\tag{5.1}
\]

This is an **exact finite obstruction**, not an average-case statement, vector coloring, rank-two coloring, or complex-phase relaxation.

The exact checker proves the row count, column count, depth distribution, pairwise projective disjointness, Kraft equality, exact row `l1` mass, and every column-norm inequality using `fractions.Fraction`. Its executed output ends

`R13_BALANCED86_RATIONAL_LOAD_EXACT_PASS`.

## 6. Exact movement relative to the corrected literature baseline

The checker proves the comparison to Kunisky's `K(64)` obstruction without floating point. Since both sides after subtracting one are positive,

\[
q>1+\frac{7\sqrt2}{8}
\quad\Longleftrightarrow\quad
(q-1)^2>\frac{49}{32},
\]

and the exact rational inequality holds. Numerically the certified improvement at dimension 86 is

\[
2.259253-\left(1+\frac{7\sqrt2}{8}\right)
=0.021816132923541832\ldots.
\]

The new obstruction also of course dominates the preceding R13 six-column rational floor `23066933137/12500000000`.

The current rigorous interval at the owner-relevant dimension is therefore

\[
\boxed{
2.259253\le K_{86}^*\le7.28151.}
\]

Only the **lower** endpoint moved in this run; the owner's fixed upper-envelope metric did not.

## 7. A propagated infinite finite-dimensional obstruction branch

Kunisky observes that for any normalized unsatisfiable matrix `A`,

\[
\phi(A)=\frac1{\sqrt2}
\begin{bmatrix}A&I\\A&-I\end{bmatrix}
\]

preserves normalization and unsatisfiability and transforms the common row-mass lower bound by

\[
q\mapsto\frac{1+q}{\sqrt2}.
\]

Starting from the exact 86-column certificate above, define

\[
q_0=\frac{2259253}{10^6},
\qquad
q_{r+1}=\frac{1+q_r}{\sqrt2}.
\]

Then for every integer `r>=0`,

\[
\boxed{K_{86\cdot2^r}^*\ge q_r},
\]

and by adding zero columns the same lower bound holds for every `n>=86*2^r`. In closed form,

\[
q_r=(1+\sqrt2)+2^{-r/2}
\left(q_0-(1+\sqrt2)\right).
\]

The first values are approximately

\[
q_0=2.259253,\quad
q_1=2.3046398979,\quad
q_2=2.3367332812,\quad
q_3=2.3594267301.
\]

Because `q_0>1+7sqrt(2)/8`, applying the same affine recursion proves that this branch strictly improves the corresponding zero-padded complete-tree lower bound from Kunisky's Theorem 1.1 at every matching recursion level. This is still a lower-obstruction comparison, not an upper-bound movement or a qualitative-resolution claim.

## 8. What failed / why I did not manufacture another certificate

Before settling on the 86-leaf deformation I revisited the six-column full-alignment-cover route from the predecessor. Exact projective-cover structure plus the support-load dual strongly indicates that the predecessor's `T_6` construction is already extremal within a broad exact-partition subfamily. That route would at best certify a **ceiling on the old mechanism** and would not move either `B_R13(86)` or the finite obstruction once the literature comparison is corrected. Consistent with the 90/10 rule, I did not spend the run manufacturing a large certificate for an unchanged number.

Likewise I did not use a scalar retuning of the cosine-power upper-bound density as the primary route. Numerical scouting suggests only a very small possible gain near the already-studied exponent, whereas the logical/tree category change above moves a source-dimensional finite obstruction by more than `0.02` over the corrected published baseline.

## 9. Prior art / novelty status

The mechanism is deliberately anchored in prior art: Kunisky already proves that unsatisfiable formulas yield lower-discrepancy matrices, gives the complete-tree power-of-two family, and formulates optimal magnitude scaling as a convex second-order cone problem. This report does **not** claim those ideas as new.

Fresh bounded searches on 19 September 2026 included combinations of `K(86) Komlos discrepancy`, `86 Komlos 9/4`, `2.25925 Komlos discrepancy`, `9037/4000 discrepancy Komlos`, and the exact rational `2259253/1000000`, together with later-author/source checks. I found no source stating this exact balanced-86 rational certificate or the resulting `q_0`/doubling staircase. A bounded negative search is not a priority certificate, so **novelty remains UNVERIFIED**.

The qualitative source status remains KNOWN due to Guo--Fang--Lu and the subsequent Karingula--Lovett proof. R13's status remains PARTIAL QUANTITATIVE.

## 10. Exact artifacts and readback

Exact checker:

`artifacts/R13/20260919T0833Z_balanced86-rational-e21c_checker.py`

creation commit:

`73a4b37f19650b64373f7926e299565484078419`

The checker was read back from that exact creation commit.

Executed output:

`artifacts/R13/20260919T0833Z_balanced86-rational-e21c.out`

creation commit:

`3a489c48697e945be0f35644bd677832b82fcf97`

The output was read back from that exact creation commit and begins

`R13_BALANCED86_RATIONAL_LOAD_EXACT_PASS`.

Self-check status: **PASS**. It is a self-check, not either of the two independent OTHER-track audits required for closure.

## 11. Status, stagnation, and next route

Status after this run:

**SOURCE QUALITATIVE STATUS KNOWN / R13 QUANTITATIVE STATUS PARTIAL / FIXED UPPER METRIC NO MOVEMENT / FIXED-UPPER UNCHANGED COUNT 2 / EXPLICIT FINITE OBSTRUCTION MOVED / full written proof / exact self-check PASS / outside audits of this new obstruction 0/2 / novelty UNVERIFIED.**

The next R13 run is close to the owner's fixed-metric stuck threshold: a third consecutive run with no upper-envelope movement triggers the five-part stuck protocol even if lower-obstruction work remains interesting. Therefore the next primary route should return to the **upper** side and be materially different from scalar density retuning. The best candidates are:

1. a six-column universal upper theorem below roughly `1.88`, strong enough for the six-block compiler to affect the `n=86` upper envelope;
2. a nonproduct DTV density whose directional variation remains `l2`-controlled rather than paying an `l1/sqrt(D)` penalty;
3. an explicit finite specialization of the newer Boolean small-ball machinery that numerically beats an existing branch of the full envelope.

If none moves `B_R13(n)` on the next complete run, apply the required stuck report rather than accumulating another lower-bound lemma.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  worker: R13
  source: Boolean Komlos discrepancy
  source_qualitative_status: KNOWN_RESOLVED_IN_2026_PREPRINT_LITERATURE
  fixed_metric: complete_upper_envelope_B_R13(n)
  fixed_metric_n86_before: 728151/100000
  fixed_metric_n86_after: 728151/100000
  fixed_metric_movement: none
  fixed_upper_unchanged_count_before: 1
  fixed_upper_unchanged_count_after: 2
  explicit_finite_obstruction_dimension: 86
  corrected_known_lower_baseline: 1 + 7*sqrt(2)/8
  corrected_known_lower_baseline_decimal: 2.237436867076458...
  new_lower_obstruction: 2259253/1000000
  new_lower_obstruction_decimal: 2.259253
  lower_obstruction_movement_decimal: 0.021816132923541832...
  exact_self_check: PASS
  outside_audits_new_claim: 0/2
  novelty: UNVERIFIED
  methods: [11, 6, 25]
  status: PARTIAL_QUANTITATIVE
```

## 13. Model / scheduler-control status

The model-control limitation is still present. The exposed task-control surface provides prompt/title, schedule/timing, enablement, and update/list controls, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. GPT-6/maximum is therefore still prompt-only here; this run cannot honestly claim it.

Making the request enforceable requires an authorized product/workspace/backend surface that exposes explicit model and reasoning controls plus applied-run telemetry, or platform support. `operations/NEW_METHODS_2026-09-16.md` also records that native modification probes for P26/P01/P03 returned `You cannot modify this task`; the lawful workaround is the owning/authorized account/workspace task surface or platform support. Do not duplicate the task or bypass permissions. No scheduler, permission, workflow, email, Drive, purchase, or public-posting action was made in this run.
