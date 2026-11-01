Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper metric** `B_R13(86)=728139/100000=7.28139`; **explicit finite obstruction MOVED** `K_86^* >= 22643/10000 = 2.2643 -> K_86^* >= 452931/200000 = 2.264655`, exact gain `71/200000 = 0.000355`; fixed-upper unchanged count `1 -> 2`. Methods actually used: **#15 BREAK THE SYMMETRY ON PURPOSE, #24 FIND THE EXTREMAL OBJECT, #26 HUNT THE SPORADIC CASE.**

# R13 — Boolean Komlos: nonuniform refinement depths improve the 86-column obstruction

Run ID: `20260919T1550Z_nonuniform-refinement-86-a6f2`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity, required reads, source status, and ownership

I continued from the newest immutable R13 report

`runs/R13/20260919T1433Z_refinement-forest-86-d4c7.md`

rather than restarting. Before new mathematics I reconciled `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the R13/E0042 history and exact checker chain, the newest R02 Komlos-adjacent current-literature report, and the newest relevant hard-lane state. `QUEUE.md` still does not make E0042 an unassigned reserve target; this run remains inside R13's existing hard assignment. I changed no shared root, peer-track file, ownership claim, workflow, permission, email, Drive, public posting, purchase, or scheduler state.

Fresh primary/current-source checks on 19 September 2026 preserve the source separation:

- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189 (10 Sep 2026), state the genuine real-Boolean Komlos bound `3 sqrt(2 pi)`.
- Akbas--Sra, *Boolean Small-Ball Inequalities for Discrepancy Theory*, arXiv:2609.20785 (17 Sep 2026), recover Komlos as a corollary but do not expose in the abstract/application an immediately comparable finite-`n` constant below R13's `7.28139` branch.
- Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), give an elementary real-sign proof with constant `36` and explicitly describe it as simplifying the Guo--Fang--Lu proof.
- Bansal--Jiang, arXiv:2508.03961v2, remains the earlier real-Boolean polylogarithmic route.
- Kunisky, arXiv:2111.02974 / SIAM J. Discrete Math. 37 (2023), is the published source for unsatisfiable-matrix/support-load lower constructions approaching `1+sqrt(2)`.

Thus the **qualitative source status is KNOWN in current 2026 preprint/technical-report literature**. R13 is only a quantitative finite-dimensional track. Complex phases, vector/rank-two colorings, and average-case bounds are not substituted for the real Boolean statement.

A bounded prior-art search for the exact decimal `2.264655`, the phrase `refinement forest` together with Komlos discrepancy, and an `11 -> 86` finite refinement construction did not find a matching published certificate. This is bounded negative evidence only. The broad unsatisfiable-matrix, convex scaling, and refinement ideas are not claimed as new. **Novelty remains UNVERIFIED.**

## 2. Fixed metric before/after: no upper movement

The owner-tracked metric is still the complete rigorously certified pointwise upper envelope `B_R13(n)`, not the lower obstruction. Put

\[
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\]

The oldest retained DTV branch remains

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\qquad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]
\[
\delta_D=2[1-(1-p_D)^D],
\qquad
G_0(n)=\max\left\{\frac{7507}{1000},3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\]

The retained one-threshold branch remains

\[
D_*(n)=\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]
\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]
\[
H(n)=\max\left\{\frac{148709}{20000},3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\]

For the retained three-threshold occupancy polynomial, with the exact predecessor coefficients `c_{ell,D}^{(3)}` and their unchanged threshold/failure conventions,

\[
\beta_D^{\uparrow,3}=\frac12\sum_{\ell=1}^D c_{\ell,D}^{(3)}
\left[\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}\right],
\]
\[
D_9(n)=\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]
\[
J(n)=\max\left\{\frac{740179}{100000},\frac{27\sqrt{10\pi}}{20}(1-\beta_{D_9(n)}^{\uparrow,3})\right\}.
\]

For every integer `D>=135`, the inherited conditional-tail branches remain exactly

\[
C_D^-=\frac{27\sqrt{10\pi}}{20}(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\qquad
L_-(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\},
\]

and, for `r=2,3,4`,

\[
C_D^{(r)}=\frac{27\sqrt{10\pi}}{20}(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,r}),
\qquad
L_r(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{C_D^{(r)},\frac n{\sqrt{D+1}}\right\}.
\]

Their exact conditional moments, truncation thresholds, and failed-threshold zero conventions are unchanged from the immutable predecessor chain; this run neither changes nor relaxes any of them.

The five-threshold branch remains

\[
A_{k,D}=\frac{5}{7(4437/5000)}\left(1-\frac{2k}{5D}\right)\left(\frac{2k}{5}\right)^{7/5}D^{-2/5},\qquad k=1,\ldots,5,
\]
with
\[
a_k=A_{k,D}/D,\quad a_0=0,\quad d_k=a_k-a_{k-1},
\]
\[
F_{1,0}=1,\qquad F_{k,r}=\sum_{s=0}^rF_{k-1,r-s}\frac{d_k^s}{s!},
\]
\[
C_{D,5}(x)=\sum_{r=0}^4\frac{D!}{(D-r)!}F_{5,r}x^r(1-a_5x)^{D-r}.
\]
Writing
\[
1-C_{D,5}(x)=\sum_{\ell=1}^Dc_{\ell,D}^{(5)}x^\ell,
\]
\[
\beta_{D,5}^{\uparrow}=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(5)}
\left[\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}\right],
\]
and retaining exactly the predecessor's truncated `U=157/20`, four-shell Cantelli functional `beta_{D,5}^{downarrow}`,
\[
L_5(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{
\frac{27\sqrt{10\pi}}{20}(1-\beta_{D,5}^{\uparrow}-\beta_{D,5}^{\downarrow}),
\frac n{\sqrt{D+1}}\right\}.
\]

The transform branches remain

\[
L_{\rm LT}(n)=\max\left\{\frac{739097}{100000},\frac n{\sqrt{136}}\right\},
\]
\[
L_{33/20}^{\rm shell}(n)=\max\left\{\frac{728139}{100000},\frac n{\sqrt{140}}\right\}.
\]

Therefore the complete fixed metric is unchanged:

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&5\le n\le85,\\
\min\{G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&n\ge86.
\end{cases}}
\]

In particular,

\[
\boxed{B_{R13}(86)=\frac{728139}{100000}=7.28139}
\]

before and after this run. The fixed-upper unchanged count is therefore `1 -> 2`. This does not yet trigger the three-run stuck protocol; the explicit finite obstruction also moved, so the hard-assignment continuation condition is satisfied.

## 3. #15 BREAK THE SYMMETRY ON PURPOSE — do not refine all eleven base cylinders equally

The preceding lower construction used an almost level-symmetric forest: ten of the eleven base cylinders produced eight final leaves and two bases were reduced to seven leaves through two unsplit depth-two parents. That was natural, but it implicitly treated base cylinders with support size four and support size five almost the same.

The exact eleven-row base has five support-four cylinders and six support-five cylinders. A refinement adds one support coordinate. Therefore a support-four base needs, roughly, one extra refinement level to place its descendants on the same final support-size scale as descendants of a support-five base.

I broke the level symmetry and allocated the 86 final leaves as

\[
\boxed{(11,11,6,5,11,5,5,5,5,11,11)}.
\]

For each base template, I repeatedly split the currently shallowest descendant, using a fresh Boolean coordinate for each split. Since the counts sum to 86, the process performs exactly `86-11=75` refinements and ends with 86 rows and 86 columns.

The resulting depth distribution relative to the eleven-column base is

\[
\boxed{17\text{ leaves at depth }2,\quad39\text{ at depth }3,\quad30\text{ at depth }4.}
\]

Despite the asymmetric depth allocation, the final support-size distribution is still exactly

\[
\boxed{42\text{ supports of size }7,\qquad44\text{ supports of size }8.}
\]

This is a structural change from the preceding support incidence pattern, not a retuning of its rational weights.

**Outcome #15: success.** Nonuniform refinement depth gives a support system with strictly better certifiable load than the preceding almost-level forest.

## 4. #24 FIND THE EXTREMAL OBJECT — optimize the fixed support system, then throw away the floating-point optimum

For a fixed final support family `S_i`, normalize each row by nonnegative magnitudes `x_ij` satisfying

\[
\sum_{j\in S_i}x_{ij}=1.
\]

The fixed-support load problem is the convex minimax problem

\[
t(S)=\min_x\max_j\sum_{i:j\in S_i}x_{ij}^2.
\]

Any feasible point gives a Komlos obstruction scale `q<1/sqrt(t)` after common row scaling. The KKT form motivates positive column weights `W_j` and

\[
x_{ij}=\frac{W_j^{-1}}{\sum_{k\in S_i}W_k^{-1}}.
\]

I used numerical optimization only as a **discovery tool** across asymmetric refinement allocations. No optimizer output, no claimed optimum, and no floating-point inequality enters the theorem. Once a better support pattern was found, I discarded the numerical certificate and rounded to the integer weight vector embedded in the exact checker.

The final theorem uses the safe rational target

\[
\boxed{q=\frac{2264655}{10^6}=2.264655}.
\]

The checker verifies every load from the integer weights with `Fraction` arithmetic. The worst normalized squared load is at column 41, diagnostically

\[
0.19498253885337843\ldots,
\]

and exact arithmetic proves

\[
q^2\max_j\sum_i x_{ij}^2<1.
\]

The corresponding displayed worst squared column norm is

\[
0.999999590136023\ldots<1,
\]

with exact positive slack. Thus every column of the scaled 86-by-86 real matrix has Euclidean norm strictly below one.

**Outcome #24: success.** The support-load optimization identifies the extremal pressure point, while the published claim is certified independently by rational arithmetic.

## 5. #26 HUNT THE SPORADIC CASE — depth four is useful, and the 12-column base is not

I deliberately searched outside the almost-complete third refinement level rather than merely changing which two depth-two parents were left unsplit.

Two exploratory outcomes mattered:

1. Replacing the eleven-column base by the exact twelve-column R13 cover and refining it to 86 columns was numerically inferior in the tested asymmetric patterns; its best tested discovery value stayed below the preceding `2.2643` certificate. I therefore did not manufacture a checker for that failed route.
2. Allowing a small number of depth-four descendants while leaving more support-five descendants at depth two produced the successful 11-base allocation above. This is the sporadic geometry the level-symmetric construction misses.

The discovery search was deliberately not promoted into an exhaustive-optimality theorem. The only finite claim archived is the explicit rational witness below.

**Outcome #26: success on the 11-base deformation; failed on the tested 12-base deformation.**

## 6. Exact projective-cover proof and the new lower obstruction

A cylinder split replaces a signed template `T` by its two children carrying the same old signs and opposite signs on one new coordinate. Therefore repeated splits preserve a projective partition. The checker nevertheless verifies the final finite core directly.

Two final cylinders can meet projectively only if their signs agree up to one global sign on every coordinate in their support intersection. Over all

\[
\binom{86}{2}=3655
\]

pairs, exact combinatorial checking finds

\[
\boxed{0\text{ projectively compatible pairs}.}
\]

A signed support of size `s` occupies projective mass `2^{-(s-1)}`. The total final mass is exactly

\[
42\cdot2^{-6}+44\cdot2^{-7}=1.
\]

Hence the 86 pairwise-disjoint cylinders partition the entire projective Boolean cube. Every `epsilon in {+-1}^{86}` fully aligns, up to global sign, with exactly one row.

For each row `i` with support `S_i`, the exact checker sets

\[
x_{ij}=\frac{W_j^{-1}}{\sum_{k\in S_i}W_k^{-1}},
\qquad
A_{ij}=q\,\sigma_{ij}x_{ij}.
\]

Every row has exact `l1` mass `q`, and all columns have Euclidean norm strictly below one by the exact load calculation above. Therefore every Boolean signing has some row with signed magnitude exactly `q`, proving

\[
\boxed{K_{86}^*\ge\frac{452931}{200000}=2.264655.}
\]

The preceding certified lower endpoint was

\[
\frac{22643}{10000}=2.2643,
\]

so the exact movement is

\[
\boxed{\frac{452931}{200000}-\frac{22643}{10000}
=\frac{71}{200000}=0.000355.}
\]

The current same-dimension certified interval is therefore

\[
\boxed{2.264655\le K_{86}^*\le7.28139.}
\]

Zero-padding preserves the lower bound for every `n>=86`; Kunisky's standard doubling construction can also propagate it to an infinite subsequence, but that propagation is secondary history rather than the fixed metric.

## 7. Exact checker and archive

The theorem-sized finite core is checked by

`artifacts/R13/20260919T1550Z_nonuniform-refinement-86-a6f2_checker.py`

created at commit

`b63176ca9c015c285e9769e58faf225538c1c2a0`

and read back from that exact commit. The independently executed matching output is

`artifacts/R13/20260919T1550Z_nonuniform-refinement-86-a6f2.out`

created at commit

`6d0f308233b700660373d25c1b00161a67975b93`

and read back from that exact commit. The output terminates

`R13_NONUNIFORM_REFINEMENT_86_EXACT_PASS`.

This is a **self-check**, not an outside audit. Outside audits of this sharpening remain `0/2`; closure is not claimed.

## 8. What the new route says about the next move

The improvement is large enough relative to the preceding weight-only residual to show that **refinement topology matters**. The next lower-bound run should not spend itself squeezing the integer weights of this one forest. A genuinely new lower attack would change the base cover or solve a combinatorial allocation problem over refinement trees, ideally with a dual certificate that bounds an entire topology class.

The upper side remains more valuable scientifically. A universal six-column theorem below about

\[
7.28139/\sqrt{15}\approx1.88005
\]

would move the existing block compiler immediately. A different DTV density or a finite-constant extraction from Boolean small-ball also remains worthwhile. If the fixed upper metric fails to move on the next run, its unchanged count would reach three and the owner-prescribed stuck protocol must be used.

## 9. Model / scheduler-control truth

The exposed task-control surface still provides prompt/title, schedule/timing, enablement, and task-update controls but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. GPT-6/maximum therefore remains prompt-only here; I cannot truthfully attest that it ran.

Repository reconciliation also shows that the historical P26 `You cannot modify this task` result is authorization-context dependent: later P26 edits succeeded from another authorized context. The lawful workaround is the task-owning/otherwise-authorized product or workspace surface, or platform support for that same task — not duplication, permission bypass, or pretending a repository edit changed scheduler model settings.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  source_id: E0042
  source_target: real Boolean Komlos signing
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  quantitative_track_status: PARTIAL
  fixed_metric:
    name: complete rigorously certified pointwise upper envelope B_R13(n)
    anchor_n86_before: 728139/100000
    anchor_n86_after: 728139/100000
    moved: false
    unchanged_count_before: 1
    unchanged_count_after: 2
  explicit_finite_obstruction:
    dimension: 86
    before: 22643/10000
    after: 452931/200000
    exact_gain: 71/200000
    moved: true
  methods_this_run: [15, 24, 26]
  exact_self_check: PASS
  outside_audits_of_this_sharpening: 0/2
  novelty: UNVERIFIED
  checker: artifacts/R13/20260919T1550Z_nonuniform-refinement-86-a6f2_checker.py
  checker_commit: b63176ca9c015c285e9769e58faf225538c1c2a0
  output: artifacts/R13/20260919T1550Z_nonuniform-refinement-86-a6f2.out
  output_commit: 6d0f308233b700660373d25c1b00161a67975b93
  next_if_upper_no_movement: owner_section_I_stuck_protocol
```
