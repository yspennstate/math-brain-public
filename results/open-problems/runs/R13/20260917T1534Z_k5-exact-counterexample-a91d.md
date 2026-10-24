Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED**—not verified GPT-6 maximum. **NO MOVEMENT in the fixed upper-envelope metric `B_R13(n)`; explicit finite obstruction MOVED at `n=5`: `K_5^* >= T = (2 sqrt(2)+3 sqrt(3)+2 sqrt(51+3 sqrt(6)))/13 = 1.79244719148...`, which strictly refutes the published 2024 claim `K(5)=(4+sqrt(142))/9`. Methods actually used: #9 RANDOMIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #6 DEFORM TO A POINT YOU CAN SOLVE.**

# R13 — Boolean Komlós: exact five-column obstruction above the published `K(5)` value

Run ID: `20260917T1534Z_k5-exact-counterexample-a91d`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source scope, and fixed metric

The target remains the **real Boolean** Komlós signing problem. For a real `m x n` matrix `A` with every column of Euclidean norm at most one, define its Boolean discrepancy by

\[
\operatorname{disc}(A)=\min_{\varepsilon\in\{-1,+1\}^n}\|A\varepsilon\|_\infty.
\]

R13 tracks the complete certified upper envelope `B_R13(n)`, not a best-looking asymptotic exponent.

Before research I recovered/read the required current surfaces: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042 intake record, the newest R13 report, and current neighboring R-series state. `QUEUE.md` still assigns Boolean Komlós to R13. No shared root or peer file is edited by this run.

The newest complete R13 report before this run was

`runs/R13/20260917T1438Z_k5-five-row-reduction-6c2a.md`

at commit `4e917d62afb5e6389b91ad6116e3f7129c856330`. It recorded two consecutive unchanged runs of the fixed upper metric and proved that any counterexample below the then-candidate five-column threshold already has at most five nonzero rows.

The retained certified upper envelope is unchanged:

\[
B_{R13}(1)=1,\qquad
B_{R13}(2)=\sqrt2,\qquad
B_{R13}(3)=\frac{\sqrt{11}+\sqrt2}{3},\qquad
B_{R13}(4)=\sqrt3,
\]

\[
B_{R13}(n)\le
\min\left\{
\sqrt{\frac{3n}{4}},
\left(\sqrt2+\frac12\right)\sqrt{\left\lceil\frac n5\right\rceil}
\right\},
\qquad 5\le n\le75,
\]

and from Guo--Fang--Lu,

\[
B_{R13}(n)<3\sqrt{2\pi},\qquad n\ge76.
\]

Thus the fixed **upper** metric did not move. Its supported unchanged count is now 3. The auxiliary finite obstruction did move sharply, which is exactly the other continuation condition allowed for this hard track.

## 2. Source check on 17 September 2026

The source separation remains:

1. Nikhil Bansal and Haotian Jiang, arXiv:`2508.03961`, *Decoupling via Affine Spectral-Independence: Beck-Fiala and Komlós Bounds Beyond Banaszczyk*, gives the earlier real-Boolean `\widetilde O((\log n)^{1/4})` Komlós bound.
2. Shengtao Guo, Ethan X. Fang and Junwei Lu, arXiv:`2609.11189`, submitted 10 September 2026, *Vector Balancing via Directional Total Variation*, states the unrestricted real-Boolean theorem with signed sum strictly below `3 sqrt(2 pi)`. The current arXiv surface located in this run is still the September 10 version; no correction/withdrawal was found in the bounded current search.
3. Nestor Guillen and Vladimir Kobzar, arXiv:`2609.15071`, submitted 14 September 2026, treats unit-modulus complex phases / rank-two vector discrepancy for real inputs, not Boolean `+/-1` signs.
4. Samir Brahim Belhaouari and Randa AlQudah, *Evaluation of the Komlos Conjecture Using Multi-Objective Optimization*, Contemporary Mathematics 5(3) (2024), DOI `10.37256/cm.5320244110`, advertises in its abstract the exact value
   \[
   K(5)=\frac{4+\sqrt{142}}9.
   \]
   The accessible derivation itself says only that `K(5)` is **lower bounded** by that number after imposing a particular row/axis distribution and symmetry ansatz.
5. Dmitriy Kunisky, *The Discrepancy of Unsatisfiable Matrices and a Lower Bound for the Komlós Conjecture Constant*, SIAM J. Discrete Math. 37(2) (2023), DOI `10.1137/22M149819X`, gives the unsatisfiable-matrix/SAT framework and asymptotic lower bound approaching `1+sqrt(2)`. This is stronger for the universal Komlós constant; the result below is a finite-`n=5` correction, not a new universal lower record.

A bounded search for the exact radical below, its decimal `1.792447191...`, and its degree-eight polynomial did not locate a matching published finite-five constant. **Novelty remains UNVERIFIED.** The mechanism is plainly adjacent to (and likely an explicit small-instance specialization of) Kunisky's unsatisfiable-matrix framework, so no claim of a fundamentally new general mechanism is made.

## 3. Method #23 — assume the advertised exact `K(5)` value is false

The preceding run reduced any counterexample below the Belhaouari--AlQudah candidate to the square `5 x 5` setting. Instead of trying to prove their advertised equality, this run attacked its negation.

A numerical counterexample search found a square unit-column matrix with discrepancy near `1.7924`, already above

\[
K_0:=\frac{4+\sqrt{142}}9=1.76848614309\ldots .
\]

The numerical pattern was stable under local optimization and simplified to two row types. That simplification produces an exact closed form.

## 4. R13-C34 — exact structured `5 x 5` obstruction

Define

\[
T=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
=1.7924471914832827\ldots .
\]

Let

\[
b=\frac1{\sqrt3},\qquad d=\frac1{\sqrt2},\qquad
a=\frac{T-b}{2},\qquad c=\frac{T-d}{3}.
\]

Then `T` is the positive root of

\[
13T^2-(6\sqrt3+4\sqrt2)T-13=0.
\]

Equivalently,

\[
\frac{(T-b)^2}{4}+\frac{(T-d)^2}{9}=\frac12,
\]

so

\[
a^2+c^2=\frac12.
\]

Consider

\[
A_*=
\begin{pmatrix}
0&a&0&a&b\\
-a&0&0&a&-b\\
a&a&0&0&-b\\
-c&c&-d&-c&0\\
-c&c&d&-c&0
\end{pmatrix}.
\]

### 4.1 Every column has Euclidean norm exactly one

Columns 1, 2 and 4 have squared norm

\[
2a^2+2c^2=1.
\]

Column 3 has squared norm

\[
2d^2=1,
\]

and column 5 has squared norm

\[
3b^2=1.
\]

Thus `A_*` is admissible for the real Boolean five-column Komlós problem.

### 4.2 Every signing has infinity norm exactly `T`

The first three rows have `l1` norm

\[
2a+b=T,
\]

while the last two have `l1` norm

\[
3c+d=T.
\]

Therefore for every Boolean signing `epsilon`,

\[
\|A_*\varepsilon\|_\infty\le T.
\]

It remains to show that every signing reaches `T` in at least one row. By antipodality fix the first sign to `+1` and write the remaining four signs in lexicographic order. An exact witness-row table is

| tail | row attaining `±T` |
|---|---:|
| `----` | `-r1` |
| `---+` | `-r2` |
| `--+-` | `-r5` |
| `--++` | `-r5` |
| `-+--` | `-r1` |
| `-+-+` | `-r2` |
| `-++-` | `-r4` |
| `-+++` | `-r4` |
| `+---` | `+r3` |
| `+--+` | `-r2` |
| `+-+-` | `+r3` |
| `+-++` | `+r1` |
| `++--` | `+r3` |
| `++-+` | `-r2` |
| `+++-` | `+r3` |
| `++++` | `+r1` |

Each table entry is an immediate substitution using either `2a+b=T` or `3c+d=T`. Hence all 16 projective classes, equivalently all 32 Boolean signings, satisfy

\[
\|A_*\varepsilon\|_\infty=T.
\]

Therefore

\[
\boxed{\operatorname{disc}(A_*)=T}
\]

and in particular

\[
\boxed{
K_5^*\ge
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
=1.79244719148\ldots .
}
\]

This is an **explicit finite obstruction**, not an upper bound and not an exact evaluation of `K_5^*`.

## 5. Exact refutation of the published `K(5)` value

The 2024 paper's advertised value is

\[
K_0=\frac{4+\sqrt{142}}9.
\]

The inequality `T>K_0` can be separated without decimal arithmetic. The exact checker verifies elementary rational lower bounds giving

\[
T>\frac{233}{130}>1.7923,
\]

while

\[
\sqrt{142}<\frac{1193}{100}
\]

because

\[
1193^2-142\cdot100^2=3249>0.
\]

Hence

\[
K_0<\frac{177}{100}=1.77<T.
\]

Thus the statement

\[
K(5)=\frac{4+\sqrt{142}}9
\]

is **false under the paper's own square five-vector/unit-Euclidean-column definition**. This does not refute the Boolean Komlós conjecture; it refutes that finite-dimensional exact-value claim.

The source's internal wording already exposes the logical weak point: after imposing one particular distribution/symmetry ansatz, it concludes only the lower bound `K(5)>=K_0`, then discusses sensitivity to alternative row distributions. The exact matrix above supplies a distribution outside that proposed optimum with a strictly larger discrepancy.

## 6. Method #9 + #6 — random search, then deform to an exact solvable family

The random/numerical search was used only for discovery, never as proof. Its stable pattern was

- three rows with support size 3 and common magnitudes `(a,a,b)`;
- two rows with support size 4 and common magnitudes `(c,c,c,d)`;
- all 16 projective sign classes saturated at the same threshold.

The exact conditions are therefore

\[
2a+b=3c+d=T,\qquad
3b^2=1,\qquad
2d^2=1,\qquad
2a^2+2c^2=1.
\]

Solving these gives exactly the radical above. This is the successful deformation step: the numerical point is replaced by a four-parameter algebraic family and then by its exact equalized point.

The support/sign pattern is naturally interpretable as an unsatisfiable-matrix / NAE-clause cover of the Boolean cube, which is why Kunisky's framework is the closest existing language for it. That connection is prior art for the mechanism, not evidence that this exact five-dimensional value has appeared before.

## 7. Independent all-rational certificate

To make the strict counterexample completely independent of symbolic radical simplification, the checker also verifies the rational matrix `I/10^7`, where

\[
I=
\begin{pmatrix}
0&6075479&0&6075479&5773497\\
-6075479&0&0&6075479&-5773497\\
6075479&6075479&0&0&-5773497\\
-3617798&3617798&-7071061&-3617798&0\\
-3617798&3617798&7071061&-3617798&0
\end{pmatrix}.
\]

The exact squared column-norm numerators are

\[
99999814896490,\;
99999814896490,\;
99999807331442,\;
99999814896490,\;
99999802827027,
\]

all at most `10^14`.

For **every one of the 32 Boolean signings**, the infinity-norm numerator is exactly

\[
17924455.
\]

Therefore this rational matrix has exact discrepancy

\[
\frac{17924455}{10^7}
=
\frac{3584891}{2000000}
=
1.7924455,
\]

already enough by itself to refute `K_0`.

The exact checker uses symbolic algebra for the closed-form matrix and pure integer arithmetic for this rational witness. It was executed before archival and ends

`R13_K5_COUNTEREXAMPLE_EXACT_PASS`.

## 8. What this changes and what it does not

The previously certified five-column interval

\[
\frac{4+\sqrt{142}}9\le K_5^*\le \sqrt2+\frac12
\]

is replaced by

\[
\boxed{
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}
\le K_5^*
\le
\sqrt2+\frac12.
}
\]

Numerically,

\[
\boxed{
1.79244719148\ldots\le K_5^*\le1.91421356237\ldots .
}
\]

By padding with zero columns, the same finite lower obstruction is valid for every larger exact column count, although Kunisky's asymptotic constructions give a stronger lower bound for the unrestricted universal constant.

The fixed **upper** envelope `B_R13(n)` does not improve this run, so the official fixed metric records no movement. The explicit obstruction, however, moves and invalidates a published finite-dimensional exact-value claim.

## 9. Full stuck protocol — recovery cycle 1

Because the fixed upper metric has now been unchanged for three consecutive runs, I execute the owner-required stuck protocol rather than manufacturing another same-route lemma.

### (a) Exact blocking statement

The sharpest simple finite blocker is now

\[
\boxed{
\text{Either prove }K_5^*\le T
\quad\text{or construct an admissible five-column matrix with discrepancy }>T.
}
\]

A weaker metric-moving success would be any rigorous upper bound

\[
K_5^*<\sqrt2+\frac12.
\]

### (b) Routes tried and why they stop

- **Balanced four-block composition:** gives `sqrt(3n/4)` but loses all internal block geometry.
- **Weighted `(2,1,1,1)` four-vector theorem:** exact/sharp in that coarse model at `sqrt(2)+1/2`; therefore it cannot lower the five-column upper bound unless one keeps the fact that the norm-`sqrt(2)` aggregate came from two genuine unit vectors.
- **Fixed-cell diagonal duals:** certify individual row-cover partitions but do not globalize; an explicit admissible row defeats the preceding partition-independent multiplier shortcut.
- **One-row incidence/energy compilers:** already encounter sharp finite obstructions and do not encode intersections among different bad-row families.
- **Directional-total-variation parameter tweaks:** the preceding X08/X09 reports block the most obvious one-dimensional vertical-marginal and i.i.d.-product-density constant improvements.
- **Published `K(5)=K_0` route:** now definitively fails because `A_*` has discrepancy `T>K_0`.

### (c) What a successful proof must contain that these routes lack

Any improvement of the five-column **upper** bound has to retain genuinely joint information. In the pair-aggregation language it must keep **both** internal pair sign choices rather than replace a pair by an arbitrary vector of norm at most `sqrt(2)`. In the row-cover language it must couple the five row cells/column-energy vectors globally rather than certify each row or each fixed partition in isolation.

### (d) Simplest unresolved special case

The simplest unresolved source-valid case is now the square five-column problem:

\[
\boxed{
T\le K_5^*\le \sqrt2+\frac12.
}
\]

The preceding five-row reduction means any counterexample to an upper bound at the new `T` threshold is already representable with at most five rows, because `1/T^2 < c_0`. Thus the remaining exact search is genuinely a `5 x 5` problem, not an arbitrary-row one.

### (e) Nearest solved problem and missing ingredient

Kunisky's unsatisfiable-matrix framework solves the **weight optimization for a fixed clause/sign pattern** by convex/SOCP duality and proves strong family-level bounds. That is extremely close in shape to the new obstruction. What it does not supply for this task is a proof that one particular five-variable sign pattern is globally extremal among **all** five-row Boolean covers.

R13's exact weighted four-vector theorem similarly solves the coarse `(2,1,1,1)` aggregate problem, but it discards the second internal pair choice.

### Recovery choice

**Chosen recovery: refute instead of prove.**

That recovery succeeded: the advertised exact five-column value `K_0` is false, and a stronger exact obstruction `T` replaces it. This is recovery cycle 1 for the hard track. Because an explicit source-matching finite obstruction moved, R13 remains on Boolean Komlós rather than rotating.

The next run must not return to the disproved `K_0` equality. Its planned genuinely different moves are:

- **#21 ASK WHO ELSE HAS THIS SHAPE:** port Kunisky's unsatisfiable-matrix SOCP dual all the way to the new five-row cover classes and determine which clause patterns can beat/match `T`;
- **#12 FIND WHAT IS CONSERVED:** identify a column-energy/coverage invariant across all five-row partitions, not just total Euclidean energy;
- **#13 FIND WHAT ONLY INCREASES:** build a branch-and-bound monovariant whose lower energy certificate only increases as projective sign classes are assigned to row cells.

## 10. Audit and closure status

The finite claim has a full written proof and an exact executed self-check. It does **not** yet have the two required independent OTHER-track audits. The existing R12/P26 audits concern the Guo--Fang--Lu universal theorem, not R13-C34.

Therefore status is

**PARTIAL / FIXED UPPER METRIC UNCHANGED / EXACT FINITE OBSTRUCTION MOVED / PUBLISHED FINITE VALUE REFUTED / SELF-CHECK PASS / OUTSIDE AUDITS PENDING.**

No paper folder is created because closure requirements are not met.

## 11. Runtime-control status

The exposed scheduler/task interface still supplies title, prompt, schedule, enablement and timing mode, but no native model-family selector and no reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt text and is not authenticated runtime configuration. This run actually reports `GPT-5.6 Sol / UNVERIFIED`.

Repository policy records prior `You cannot modify this task` failures as ownership/context dependent. The legitimate remedy is an authorized task/workspace-owner context or platform support exposing the native controls; duplicating or bypassing a denied task is not acceptable. No scheduler modification was attempted here.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  run_id: "20260917T1534Z_k5-exact-counterexample-a91d"
  source: "Boolean Komlos; E0042/Bandeira Open Problem 0.1; Bansal-Jiang arXiv:2508.03961; Guo-Fang-Lu arXiv:2609.11189; Belhaouari-AlQudah 2024 finite-n claim; Kunisky 2023 unsatisfiable-matrix lower-bound framework"
  target: "complete real Boolean unit-column discrepancy bound, with corrected finite-dimensional comparisons"
  metric_name: "complete certified upper envelope B_R13(n)"
  metric_before: "B(1)=1; B(2)=sqrt2; B(3)=(sqrt11+sqrt2)/3; B(4)=sqrt3; for 5<=n<=75 min{sqrt(3n/4),(sqrt2+1/2)sqrt(ceil(n/5))}; for n>=76 <3sqrt(2pi)"
  metric_after: "unchanged"
  metric_movement: false
  unchanged_count_before: 2
  unchanged_count_after: 3
  auxiliary_obstruction_before: "K_5^* >= (4+sqrt(142))/9 = 1.76848614309..."
  auxiliary_obstruction_after: "K_5^* >= (2sqrt2+3sqrt3+2sqrt(51+3sqrt6))/13 = 1.79244719148..."
  auxiliary_obstruction_moved: true
  finite_claim_correction: "Belhaouari-AlQudah advertised K(5)=(4+sqrt142)/9 is false under its square unit-column definition"
  actual_model: "GPT-5.6 Sol"
  actual_reasoning: "UNVERIFIED"
  requested_model: "GPT-6"
  requested_reasoning: "maximum"
  methods:
    - "B9 RANDOMIZE: numerical square-5 counterexample search found a stable discrepancy > published candidate"
    - "B23 DO WHAT THE PROPOSER DID NOT EXPECT: assumed the advertised exact K(5) value was false and attacked it directly"
    - "B6 DEFORM TO A POINT YOU CAN SOLVE: recognized the numerical pattern, reduced it to two exact row types, and solved the equalization equations in radicals"
  checker_status: "EXACT SELF-CHECK PASS"
  checker_terminal: "R13_K5_COUNTEREXAMPLE_EXACT_PASS"
  current_status: "PARTIAL"
  stuck_recovery_cycle: 1
  stuck_recovery_choice: "refute instead of prove"
  prior_art_status: "mechanism overlaps Kunisky unsatisfiable-matrix/SOCP framework; bounded searches found no exact T/decimal/polynomial match; novelty UNVERIFIED"
  outside_audits_for_new_claim: 0
  next_methods: [21, 12, 13]
  next_obligation: "decide whether T is the true five-column constant or move the certified five-column upper bound below sqrt2+1/2, using global five-row cover geometry"
  shared_roots_edited: false
  peer_files_edited: false
  scheduler_modified: false
```
