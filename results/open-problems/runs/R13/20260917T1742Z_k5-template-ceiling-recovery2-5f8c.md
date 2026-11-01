Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this is not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper-envelope metric `B_R13(n)`; auxiliary finite-route obstruction MOVED: the complete at-most-five-row NAE/full-alignment clause-template lower-bound mechanism has exact ceiling `T=(2sqrt2+3sqrt3+2sqrt(51+3sqrt6))/13`, attained by the preceding `A_*`; every other canonical support pattern has a certified ceiling `<177/100<T`. Methods actually used: #21 ASK WHO ELSE HAS THIS SHAPE, #12 FIND WHAT IS CONSERVED, #13 FIND WHAT ONLY INCREASES.**

# R13 — Boolean Komlós: exact ceiling for every five-row full-alignment clause template

Run ID: `20260917T1742Z_k5-template-ceiling-recovery2-5f8c`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source scope, and fixed metric

The target remains the real Boolean Komlós quantitative problem. For a real matrix `A` whose `n` columns have Euclidean norm at most one, write

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{-1,+1\}^n}\|A\varepsilon\|_\infty,
\qquad
K_n^*=\sup_A \operatorname{disc}(A).
\]

R13's fixed metric is the **complete certified upper envelope** `B_R13(n)` for `K_n^*`, retaining every constant, finite-dimensional restriction, logarithm and parameter condition rather than reporting only an exponent.

Before research I recovered/read the controlling repository state required by the owner: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042/Komlós intake navigation, the newest complete R13 report, the newer R13 artifact-only commits, and current neighboring discrepancy/recovery state. The neighbor registry has moved historical R16 away from Beck--Fiala to a different source, so I did not import its present metric into this track. No shared root or peer file is edited here.

The newest **complete** R13 report before this run is

`runs/R13/20260917T1534Z_k5-exact-counterexample-a91d.md`

at commit `ea33d21fa2ae398a2e92b04e456fbc5230892b57`. It proved the exact five-column lower obstruction

\[
T=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
=1.79244719148328\ldots
\]

and exhibited an admissible `5 x 5` matrix `A_*` with discrepancy exactly `T`, thereby refuting the published/advertised finite claim

\[
K(5)=\frac{4+\sqrt{142}}9.
\]

That report was the first hard-target stuck recovery. It explicitly selected the next methods `#21,#12,#13`; I follow that instruction here.

The retained upper envelope is unchanged:

\[
B_{R13}(1)=1,
\quad B_{R13}(2)=\sqrt2,
\quad B_{R13}(3)=\frac{\sqrt{11}+\sqrt2}{3},
\quad B_{R13}(4)=\sqrt3,
\]

\[
B_{R13}(n)\le
\min\left\{
\sqrt{\frac{3n}{4}},
\left(\sqrt2+\frac12\right)
\sqrt{\left\lceil\frac n5\right\rceil}
\right\},
\qquad 5\le n\le75,
\]

and the current Guo--Fang--Lu theorem gives the dimension-free real-Boolean guarantee

\[
B_{R13}(n)<3\sqrt{2\pi},\qquad n\ge76.
\]

The fixed upper metric has therefore now been unchanged for four consecutive complete R13 runs. This run is **STUCK_RECOVERY_2**, the second and final same-problem recovery permitted by the hard-target policy. Unlike a receipt-only run, however, it closes an entire candidate lower-bound mechanism by an exact finite certificate.

## 2. Current source and prior-art check, 17 September 2026

The source picture was checked afresh before interpreting the new finite result.

1. Nikhil Bansal and Haotian Jiang, arXiv:`2508.03961`, *Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk*, is the earlier real-Boolean advance and gives the `\widetilde O((\log n)^{1/4})` Komlós bound.
2. Shengtao Guo, Ethan X. Fang and Junwei Lu, arXiv:`2609.11189`, submitted 10 September 2026, *Vector Balancing via Directional Total Variation*, currently presents the unrestricted **real Boolean** theorem with universal constant `3sqrt(2pi)`. A bounded current search again found the September 10 `v1` surface and no correction or withdrawal. Thus the historical existence conjecture itself is no longer treated here as an unsolved source statement; R13 is a quantitative finite-constant/refinement track.
3. Nestor Guillen and Vladimir Kobzar, arXiv:`2609.15071`, submitted 14 September 2026, allows unit-modulus complex phases, equivalently rank-two/vector discrepancy for real input vectors. It is not a Boolean-sign replacement.
4. Dmitriy Kunisky, *The Discrepancy of Unsatisfiable Matrices and a Lower Bound for the Komlós Conjecture Constant*, SIAM J. Discrete Math. 37 (2023), 586--603, is the closest prior language to the present route. It builds lower-bound matrices from unsatisfiable formula/clause-variable templates, optimizes scalings by SOCP, and gives dual certificates for a broad read-once-resolution family.
5. The Belhaouari--AlQudah 2019/2024 line advertises the now-refuted finite value `(4+sqrt(142))/9`; the preceding R13 report contains the exact counterexample and source-scope correction.

A bounded search did not locate the exact five-variable template ceiling proved below. This is **not** a novelty certificate. The mechanism is explicitly adjacent to Kunisky's unsatisfiable-matrix framework, and the safe claim is an exact finite classification/certificate inside that mechanism.

## 3. Method #21 — port the unsatisfiable-matrix shape, not just one formula

The preceding `A_*` is not an isolated numerical curiosity. Its five rows have supports of sizes `3,3,3,4,4`, and every projective Boolean signing is fully aligned or anti-aligned with at least one row at the attained threshold `T`. This is exactly the finite geometry behind a clause-variable/NAE-style lower-bound construction.

For five variables, fix the sixteen projective sign classes

\[
\mathcal S_5=\{(1,s_2,s_3,s_4,s_5):s_j\in\{\pm1\}\}.
\]

For a nonzero row `r`, write its support as `S(r) subset [5]` and its literal orientation as the signs of its nonzero coefficients. A projective sign vector is **fully aligned** with this row if, after possibly negating the whole projective sign vector, every coordinate in `S(r)` agrees with the row orientation. In that event

\[
|r\cdot s|=\|r\|_1.
\]

A support/orientation family is a **full-alignment clause cover** if every class in `\mathcal S_5` is fully aligned with at least one row. Such a cover certifies the usual formula-template discrepancy lower bound

\[
d_{\rm FA}:=\min_i\|r_i\|_1,
\]

because each Boolean signing saturates at least one row at magnitude at least `d_FA`.

The question attacked in this recovery is therefore not one hand-picked formula but the full finite class:

> How large can the certified lower-bound parameter `d_FA` be among **all** full-alignment clause covers on five variables with at most five rows and with every column having Euclidean norm at most one?

The answer is exactly `T`.

This is deliberately narrower than the true `K_5^*`: a general threshold row can witness a signing by **partial** rather than full alignment. The theorem below closes the clause-template mechanism; it does not silently promote that mechanism to all Boolean discrepancy matrices.

## 4. Method #12 — the conserved quantity is weighted column energy

Let the active rows be `r_1,...,r_q`, with `q<=5`, supports `S_i`, and column energies

\[
E_j:=\sum_{i=1}^q r_{ij}^2\le1,
\qquad j=1,...,5.
\]

Let

\[
d:=\min_i\|r_i\|_1.
\]

For any weights `alpha_i>=0` with `sum_i alpha_i=1`,

\[
\begin{aligned}
d
&\le \sum_i\alpha_i\|r_i\|_1\\
&=\sum_{j=1}^5\sum_{i:j\in S_i}\alpha_i|r_{ij}|\\
&\le\sum_{j=1}^5
\sqrt{\sum_{i:j\in S_i}\alpha_i^2}
\sqrt{\sum_i r_{ij}^2}\\
&\le
\boxed{
F_H(\alpha):=
\sum_{j=1}^5
\sqrt{\sum_{i:j\in S_i}\alpha_i^2}
},
\end{aligned}
\tag{4.1}
\]

where `H=(S_1,...,S_q)` is the support multiset. Equation (4.1) is the route's global invariant: it couples all rows through the **same five column-energy budgets**. It is stronger than summing rowwise Euclidean lower bounds and is exactly the type of cross-row information missing from the earlier total-energy arguments.

Thus to upper-bound the best clause-template lower certificate for a fixed support pattern, it suffices to find a single exact weight vector `alpha` giving a small value of `F_H(alpha)`.

Two trivial cases can be removed before enumeration. A one-row cover cannot produce a lower certificate above `1` under a unit column budget, and any support-one row has `\|r_i\|_1=|r_{ij}|<=1`. Since the target `T>1.79`, only `2<=q<=5` and supports of size at least two can matter.

## 5. Method #13 — exhaustive support-pattern monovariant

The finite core now has no continuous search left except the explicit function `F_H`.

The exact checker enumerates every multiset of `2,3,4,5` nontrivial supports `S subset [5]`, `|S|>=2`, modulo all `5!` coordinate permutations. It then asks whether some literal orientation for each support fully aligns with all sixteen projective sign classes. Repeated supports are treated conservatively: the coverability DP even permits reusing an orientation, so every genuine distinct-row clause template is included. False-positive support patterns only make the certification task harder and therefore cannot invalidate the upper conclusion.

The exact counts are

\[
\boxed{2537\text{ canonical support patterns}},
\]

of which

\[
\boxed{1505\text{ are coverable}},
\]

split by row count as

\[
\boxed{1,12,125,1367\quad\text{for }q=2,3,4,5.}
\]

There is one distinguished canonical pattern

\[
H_*= (7,11,13,30,30),
\]

where masks are the five-bit support indicators. Up to a coordinate permutation, this is exactly the support family of the preceding matrix `A_*`; it has support sizes `3,3,3,4,4`.

For **each of the other 1504 coverable canonical patterns**, the artifact stores an exact rational weight vector

\[
\alpha_i=\frac{w_i}{100},
\qquad w_i\in\mathbb Z_{\ge0},
\qquad \sum_i w_i=100.
\]

For each square root in (4.1), the checker replaces the irrational value by an explicitly verified rational **upper** bound obtained by integer ceiling at scale `10^6`. Hence the comparison is one-sided in the rigorous direction and uses no floating-point acceptance criterion.

The result is

\[
\boxed{F_H(\alpha)<\frac{177}{100}}
\qquad\text{for every coverable }H\ne H_*.
\tag{5.1}
\]

The largest stored rational upper certificate occurs at support pattern

\[
(7,7,11,27,27)
\]

and is only

\[
\frac{176932763}{100000000}=1.76932763.
\]

Thus there is a strict, exact gap between the exceptional pattern and every other support template.

## 6. The exceptional pattern has exact ceiling `T`

Write the preceding extremal matrix parameters as

\[
b=\frac1{\sqrt3},\qquad
d_0=\frac1{\sqrt2},\qquad
a=\frac{T-b}{2},\qquad c=\frac{T-d_0}{3}.
\]

They satisfy

\[
a^2+c^2=\frac12.
\]

Set

\[
D=3a+2c,
\qquad
x=\frac aD,
\qquad
y=\frac cD,
\]

so that

\[
3x+2y=1.
\]

For the support incidence pattern `H_*`, substituting the row weights `(x,x,x,y,y)` into (4.1) gives exactly

\[
F_{H_*}(x,x,x,y,y)
=
\sqrt3\,x
+3\sqrt{2x^2+2y^2}
+\sqrt2\,y
=
\boxed{T}.
\tag{6.1}
\]

This is checked symbolically in the exact artifact.

Conversely the matrix

\[
A_*=
\begin{pmatrix}
0&a&0&a&b\\
-a&0&0&a&-b\\
a&a&0&0&-b\\
-c&c&-d_0&-c&0\\
-c&c&d_0&-c&0
\end{pmatrix}
\]

has every column norm exactly one, every row `l1` norm exactly `T`, canonical support pattern `H_*`, and every one of the sixteen projective sign classes fully aligns or anti-aligns with at least one row. Therefore its full-alignment lower certificate equals `T`.

Combining (5.1) and (6.1) proves the exact restricted theorem.

### R13-C35 — exact five-variable clause-template ceiling

Among all at-most-five-row full-alignment/NAE clause-cover constructions on five Boolean variables, with arbitrary real row magnitudes but column Euclidean energies at most one, the largest certified lower-bound parameter

\[
\min_i\|r_i\|_1
\]

is exactly

\[
\boxed{
T=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
}
\]

The exceptional support pattern is `H_*=(7,11,13,30,30)` up to coordinate permutation; every other coverable canonical pattern is separated by the exact bound `<177/100<T`.

The executed exact self-check terminates with

`R13_K5_TEMPLATE_CEILING_EXACT_PASS`.

Artifacts:

- `artifacts/R13/20260917T1701Z_k5-template-ceiling-5f8c_checker.py`, creation commit `41f0fe61ac9df98c45941a470a1268f51c9e1226`;
- `artifacts/R13/20260917T1701Z_k5-template-ceiling-5f8c_output.txt`, archival commit `88bb507bbd89f610a6bee890ceaf44a1620fb0c7`.

The output records the exact counts, the exceptional pattern, the `1504` certificate count, the worst nonexceptional rational upper bound, the exact symbolic value `T`, and the terminal PASS marker.

## 7. What this rules out — and the exact point where it stops

This theorem is useful because it kills the most natural way to try to beat the new finite obstruction.

The preceding five-row reduction says that any hypothetical five-column discrepancy obstruction above `T` can already be witnessed using at most five rows. R13-C35 now says that, among such five-row witnesses, **no lower construction whose Boolean coverage is certified solely by full row alignment / unsatisfied-clause cells can beat `T`.**

Therefore any stronger five-column obstruction must contain a genuinely different feature:

\[
\boxed{
\text{some projective sign class must be witnessed at threshold }>T
\text{ by a row that is only partially aligned with that sign class.}
}
\tag{7.1}
\]

Equivalently, a stronger obstruction cannot be obtained merely by choosing a new five-variable unsatisfiable clause support pattern and rescaling its rows. The obstruction has to use a **weighted threshold row**, where several coordinates oppose the row orientation but the remaining aligned weight is still large enough to cross the threshold.

This is exactly the failure mode that the formula-template language does not encode.

I stress the scope: R13-C35 is **not** a proof that `K_5^*=T`. The true Boolean discrepancy of a matrix may be driven by partial-alignment row values; (4.1) bounds the standard full-alignment minimum-row-`l1` certificate. Claiming that the checker settles all `5 x 5` matrices would be false.

The current rigorously certified five-column interval therefore remains

\[
\boxed{
T\le K_5^*\le\sqrt2+\frac12.
}
\]

The fixed upper metric `B_R13(5)=sqrt2+1/2` does not move this run.

## 8. Stuck protocol — recovery cycle 2

Because the fixed upper metric was already unchanged for three runs, this is the second and final permitted hard-target recovery on this blocker.

### (a) Exact blocking statement

After closing the full-alignment mechanism, the remaining statement is

\[
\boxed{
\text{Either prove }K_5^*\le T,
\text{ or produce an admissible five-column matrix of discrepancy }>T,
}
\]

and any counterexample to the first alternative must use the partial-alignment phenomenon (7.1).

A weaker but still fixed-metric-moving success would be any proof

\[
K_5^*<\sqrt2+\frac12.
\]

### (b) Routes tried and their precise failures

- **Balanced block composition:** loses internal block geometry and stops at `sqrt(3n/4)`.
- **Weighted `(2,1,1,1)` four-vector theorem:** is itself sharp at `sqrt2+1/2`; it cannot improve `B(5)` after the pair is compressed to an arbitrary vector of norm `sqrt2`.
- **Diagonal fixed-cell duals:** strong enough to certify individual support/partition cells but do not automatically globalize over all threshold-cell geometries.
- **Directional-total-variation parameter changes:** the earlier R13 lift/product obstructions show that changing only the vertical marginal or only the regular i.i.d. product factor does not improve the relevant `1/3` / `sqrt(2pi)` ingredients.
- **Published finite `K(5)` ansatz:** explicitly refuted by `A_*`.
- **Full-alignment/NAE clause templates:** **now exhausted completely** at five rows; R13-C35 proves their exact ceiling is `T`.

### (c) What a successful proof must contain that no previous route contains

It must encode **partial-alignment threshold cells**. For a row with absolute coefficient vector `p`, a signing can be witnessed even after some coordinates oppose the row orientation, provided the total flipped weight is at most `(||p||_1-d)/2`. The next proof must couple those weighted Hamming balls/downsets across the five rows while simultaneously enforcing all five column-energy constraints.

A total-energy count alone is insufficient. The previous exact `M_k` table shows that the minimum total row energy for a five-block projective cover can sit below the candidate columnwise threshold. The missing information is how the energy is distributed by coordinate and how the partial-alignment cells intersect.

### (d) Simplest unresolved special case

The simplest unresolved special case is the **square five-column / at-most-five-witness-row threshold-cover problem with at least one non-clause row**:

\[
T\le K_5^*\le\sqrt2+\frac12.
\]

Full-alignment covers are now completely removed from the search.

### (e) Nearest solved problem and what it has that this one lacks

Kunisky's framework solves the scaling optimization for a fixed Boolean-formula incidence pattern by convex SOCP duality. R13-C35 pushes that finite-formula route all the way through every five-variable support pattern. What remains is outside pure clause incidence: **weighted threshold functions with zero/partial-alignment regions**. The nearest standard language is threshold logic / weighted voting, not ordinary unsatisfiable CNF/NAE incidence.

### Recovery choice

Chosen recovery: **reduce the obstruction to a finite computation and run it.**

This recovery succeeds at its stated scope: the complete five-row full-alignment clause-template family has been exhausted, and the exact exceptional template identified. It does not move the fixed upper metric. Under the owner's two-recovery rule, another run that reaches the same blocker without moving either the source-matching quantitative bound or an explicit finite obstruction must leave a handoff and rotate to an eligible outside target rather than manufacture another template lemma.

If the track continues because the blocker moves, the next genuinely different methods are:

- **#15 BREAK THE SYMMETRY ON PURPOSE:** classify a first non-clause row by the strict ordering of its five absolute coefficients instead of averaging it back to a symmetric clause template;
- **#27 SWAP THE QUANTIFIERS:** for a fixed diagonal energy multiplier, enumerate all threshold-cell types that can beat `T`, then ask whether any five of those cells can cover the projective cube;
- **#30 ONE DIRECTION AT A TIME:** localize to one partial-alignment flip set, derive the exact quadratic cost for that cell, and glue only after the single-cell catalogue is complete.

## 9. Audit and closure status

R13-C35 has a full written proof and an executed exact self-check. It does **not** yet have the two required independent OTHER-track audits, and the checker addresses a restricted lower-bound mechanism rather than the full five-column Komlós upper problem.

Status:

**PARTIAL / FIXED UPPER METRIC UNCHANGED / RECOVERY 2 / EXACT CLAUSE-TEMPLATE CEILING PROVED BY SELF-CHECK / TRUE FIVE-COLUMN CONSTANT STILL OPEN IN THIS TRACK / OUTSIDE AUDITS PENDING.**

No paper folder is created.

## 10. Runtime-control status

The scheduler interface exposed to this environment still has title, prompt, schedule, enablement and timing controls, but **no model-family field and no reasoning-effort field**. Therefore `GPT-6 / maximum` remains a prompt request rather than authenticated runtime configuration. This run actually reports `GPT-5.6 Sol / UNVERIFIED`.

The repository's current deployment ledger also records that an earlier `You cannot modify this task` failure for P26 was context/ownership dependent and that P26 was subsequently editable from an authorized P/C context. The legitimate remedy for a denied task is therefore the authorized task/workspace-owner context, or a platform change/support path that exposes native model/reasoning controls. Duplicating a denied task or bypassing permissions is not an acceptable workaround. No scheduler modification was attempted here.

## 11. Structured ledger delta

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  run_id: "20260917T1742Z_k5-template-ceiling-recovery2-5f8c"
  source: "Boolean Komlos quantitative refinement; Bansal-Jiang arXiv:2508.03961; Guo-Fang-Lu arXiv:2609.11189; Kunisky 2023 unsatisfiable matrices; Belhaouari-AlQudah finite-n claim"
  target: "complete rigorously certified real-Boolean unit-column discrepancy envelope B_R13(n), retaining corrected finite comparisons"
  metric_name: "complete certified upper envelope B_R13(n)"
  metric_before: "B1=1; B2=sqrt2; B3=(sqrt11+sqrt2)/3; B4=sqrt3; 5<=n<=75 min{sqrt(3n/4),(sqrt2+1/2)sqrt(ceil(n/5))}; n>=76 <3sqrt(2pi)"
  metric_after: "unchanged"
  metric_movement: false
  unchanged_count_before: 3
  unchanged_count_after: 4
  auxiliary_before: "K_5^* >= T from explicit exact A_*; published old finite K(5) value refuted"
  auxiliary_after: "full at-most-five-row full-alignment/NAE clause-template lower-bound mechanism has exact ceiling T; 1504 nonexceptional canonical support patterns have exact rational certificates <177/100; unique exceptional canonical support H_*=(7,11,13,30,30) is attained by A_*"
  auxiliary_movement: true
  actual_model: "GPT-5.6 Sol"
  actual_reasoning: "UNVERIFIED"
  requested_model: "GPT-6"
  requested_reasoning: "maximum"
  methods:
    - "B21 ASK WHO ELSE HAS THIS SHAPE: ported the five-variable obstruction into Kunisky's unsatisfiable-matrix/clause-template language and attacked the entire support-pattern family"
    - "B12 FIND WHAT IS CONSERVED: used the common five column-energy budgets to derive the weighted functional F_H(alpha) controlling every row scaling of a fixed support family"
    - "B13 FIND WHAT ONLY INCREASES: quotient/enumerate support patterns, certify each nonexceptional branch by an exact rational dual weight, leaving one exact exceptional branch"
  finite_core:
    canonical_support_patterns: 2537
    coverable_patterns: 1505
    coverable_by_row_count: "{2:1,3:12,4:125,5:1367}"
    nonexceptional_exact_certificates: 1504
    worst_nonexceptional_rational_upper: "176932763/100000000"
    exceptional_pattern: "(7,11,13,30,30)"
    exceptional_ceiling: "T=(2sqrt2+3sqrt3+2sqrt(51+3sqrt6))/13"
  checker_status: "EXACT SELF-CHECK PASS"
  checker_terminal: "R13_K5_TEMPLATE_CEILING_EXACT_PASS"
  checker_path: "artifacts/R13/20260917T1701Z_k5-template-ceiling-5f8c_checker.py"
  output_path: "artifacts/R13/20260917T1701Z_k5-template-ceiling-5f8c_output.txt"
  current_status: "PARTIAL"
  source_existence_status: "current Guo-Fang-Lu preprint claims complete real-Boolean dimension-free theorem; R13 is quantitative refinement, not a new source-solution claim"
  stuck_recovery_cycle: 2
  stuck_recovery_choice: "reduce obstruction to a finite computation and run it"
  outside_audits_for_new_claim: 0
  next_methods: [15, 27, 30]
  next_obligation: "classify/certify genuinely partial-alignment five-row threshold cells; move B_R13(5) below sqrt2+1/2 or produce a stronger exact five-column obstruction; otherwise hand off/rotate under the hard two-recovery limit"
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_modified: false
```
