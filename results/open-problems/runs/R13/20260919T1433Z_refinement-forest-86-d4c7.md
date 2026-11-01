Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper metric** `B_R13(86)=728139/100000=7.28139`; **explicit finite obstruction MOVED at the same dimension** `K_86^* >= 225925611947/10^11 = 2.25925611947 -> K_86^* >= 22643/10000 = 2.2643`, exact increase `504388053/10^11 = 0.00504388053`; fixed-upper unchanged count `0 -> 1`. Methods actually used: **#6 DEFORM TO A POINT YOU CAN SOLVE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #25 COUNT THE SAME THING TWICE.**

# R13 — Boolean Komlós: an 86-column refinement-forest obstruction from the exact 11-column cover

Run ID: `20260919T1433Z_refinement-forest-86-d4c7`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity, source status, ownership, and fixed metric

I continued from the newest immutable R13 report

`runs/R13/20260919T1415Z_shell-binomial-5a7c.md`

at creation commit

`24643871078759165c4d1e996982706c25a584b3`,

rather than restarting Komlós or re-deriving the DTV chain. Before new mathematics I reread/reconciled `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the E0042 intake row in `probability_1000_intake_E_20260908/problems.jsonl`, the newest R13 report/checker chain, the exact eleven-column R13 obstruction, and the newest neighboring R16 state. `QUEUE.md` still identifies Boolean Komlós/R13 as an assigned hard target rather than unassigned reserve material. No shared root, peer-track file, ownership claim, workflow, permission, email, Drive, public posting, purchase, or scheduler state is changed here.

Fresh primary-source checks on 19 September 2026 preserve the source separation:

- Guo--Fang--Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189, submitted 10 September 2026, prove the genuine real-Boolean dimension-free bound `3 sqrt(2 pi)`;
- Akbas--Sra, *Boolean Small-Ball Inequalities for Discrepancy Theory*, arXiv:2609.20785, submitted 17 September 2026, recover ordinary Komlós through a small-ball theorem, but their displayed application retains unnamed upstream universal constants and does not presently give an immediately comparable `7.28`-scale finite constant;
- Bansal--Jiang remains the earlier real-Boolean polylogarithmic route;
- Kunisky, SIAM J. Discrete Math. 37 (2023), supplies the unsatisfiable-matrix / support-load lower-bound mechanism and the standard doubling operation.

Thus the **qualitative source status is KNOWN / RESOLVED in current 2026 preprint literature**. R13 is only a finite-dimensional quantitative track. Complex phases, rank-two/vector colorings, and average-case bounds are not substituted for the real Boolean statement.

The immediately preceding exact same-dimension interval was

\[
\frac{225925611947}{10^{11}}
\le K_{86}^*
\le \frac{728139}{100000},
\]

i.e.

\[
2.25925611947\le K_{86}^*\le7.28139.
\]

This run changes only the lower endpoint.

## 2. The complete fixed upper metric is unchanged

The owner-tracked metric remains the complete pointwise upper envelope, not the lower obstruction and not merely the `n=86` headline. Put

\[
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
\]

The oldest DTV branch is retained exactly:

\[
D_0(n)=\left\lceil\frac{10^6n^2}{7507^2}\right\rceil,
\qquad
p_D=\frac{2e^{-1/(18D)}}{81\sqrt{2\pi}D^{3/2}},
\]
\[
\delta_D=2[1-(1-p_D)^D],
\qquad
G_0(n)=\max\left\{\frac{7507}{1000},
3\sqrt{2\pi}(1-\delta_{D_0(n)})\right\}.
\]

The retained one-threshold branch is

\[
D_*(n)=
\left\lceil\frac{400000000n^2}{22114366681}\right\rceil-1,
\]
\[
\alpha_D=\frac{2-1/D}{3\sqrt{2\pi}\sqrt D},
\qquad
\beta_D=\frac{\alpha_D}{2(1+\alpha_D)},
\]
\[
H(n)=\max\left\{\frac{148709}{20000},
3\sqrt{2\pi}(1-\beta_{D_*(n)})\right\}.
\]

For the retained three-threshold occupancy polynomial, with the exact predecessor coefficients `c_{ell,D}^{(3)}` and their unchanged threshold/failure conventions,

\[
\beta_D^{\uparrow,3}
=\frac12\sum_{\ell=1}^D c_{\ell,D}^{(3)}
\left[\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}\right],
\]
\[
D_9(n)=
\left\lceil\frac{10^{10}n^2}{547864952041}\right\rceil-1,
\]
\[
J(n)=\max\left\{\frac{740179}{100000},
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D_9(n)}^{\uparrow,3})\right\}.
\]

For integer `D>=135`, all exact inherited conditional-tail definitions and failed-threshold zero conventions remain unchanged:

\[
C_D^-=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\qquad
L_-(n)=\inf_{D\in\mathbb Z,\,D\ge135}
\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\},
\]

and, for `r=2,3,4`,

\[
C_D^{(r)}=
\frac{27\sqrt{10\pi}}{20}
(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,r}),
\qquad
L_r(n)=\inf_{D\in\mathbb Z,\,D\ge135}
\max\left\{C_D^{(r)},\frac n{\sqrt{D+1}}\right\}.
\]

The exact definitions of `beta_D^{downarrow,-}` and `beta_D^{downarrow,r}`, including every truncation threshold, conditional moment, and failed-threshold zero convention, are inherited verbatim from the immutable predecessor chain; this run neither changes nor relaxes them.

The five-threshold branch remains

\[
A_{k,D}=\frac{5}{7(4437/5000)}
\left(1-\frac{2k}{5D}\right)
\left(\frac{2k}{5}\right)^{7/5}D^{-2/5},
\quad k=1,\ldots,5,
\]
with
\[
a_k=A_{k,D}/D,\quad a_0=0,\quad d_k=a_k-a_{k-1},
\]
\[
F_{1,0}=1,
\qquad
F_{k,r}=\sum_{s=0}^rF_{k-1,r-s}\frac{d_k^s}{s!},
\]
\[
C_{D,5}(x)=
\sum_{r=0}^4\frac{D!}{(D-r)!}F_{5,r}x^r(1-a_5x)^{D-r}.
\]
Writing
\[
1-C_{D,5}(x)=\sum_{\ell=1}^Dc_{\ell,D}^{(5)}x^\ell,
\]
\[
\beta_{D,5}^{\uparrow}
=\frac12\sum_{\ell=1}^Dc_{\ell,D}^{(5)}
\left[\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}\right],
\]
and retaining exactly the predecessor's truncated `U=157/20`, four-shell Cantelli functional `beta_{D,5}^{downarrow}`,
\[
L_5(n)=
\inf_{D\in\mathbb Z,\,D\ge135}
\max\left\{
\frac{27\sqrt{10\pi}}{20}
(1-\beta_{D,5}^{\uparrow}-\beta_{D,5}^{\downarrow}),
\frac n{\sqrt{D+1}}
\right\}.
\]

The older transform branch is

\[
L_{\rm LT}(n)=
\max\left\{\frac{739097}{100000},\frac n{\sqrt{136}}\right\},
\]

and the current shell-recovery branch remains

\[
L_{33/20}^{\rm shell}(n)=
\max\left\{\frac{728139}{100000},\frac n{\sqrt{140}}\right\}.
\]

Therefore the complete fixed metric after this run is still

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},
G_0,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&5\le n\le85,\\
\min\{G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&n\ge86.
\end{cases}}
\]

In particular

\[
\boxed{B_{R13}(86)=7.28139}
\]

is unchanged, so the fixed-upper unchanged count is now `1`.

## 3. #23 DO WHAT THE PROPOSER DID NOT EXPECT — use the exact 11-column obstruction as the base gadget

The preceding 86-column lower constructions started from complete or balanced binary-tree clause systems. I instead used the strongest exact small-dimensional support already present in R13 as the **base gadget**: the eleven-column matrix from

`runs/R13/20260918T1437Z_n11-explicit-near2-8c4d.md`.

Its eleven signed row templates form a projective cylinder partition of the eleven-cube, and its exact discrepancy floor is

\[
K_{11}^*\ge1.99488049.
\]

For the lower construction only the **signed support templates** are needed; the old decimal/rational magnitudes are discarded. This is the unexpected step: refine a strong non-tree finite cover rather than starting again from singleton clauses or a complete tree.

A support-load optimization was used only for discovery. Its numerical optimum for the best refinement pattern below is approximately `2.26433884`; no floating-point optimizer output is used in the theorem. I rounded to a much safer rational target

\[
\boxed{q=\frac{22643}{10000}=2.2643}
\]

and certify that value from scratch with exact arithmetic.

**Outcome #23: success.** The small exact obstruction can be transplanted into a much larger refinement forest and beats the preceding same-dimension balanced-tree obstruction.

## 4. #6 DEFORM TO A POINT YOU CAN SOLVE — 75 exact cylinder splits, not a complete doubling

A cylinder split takes one signed row template `T`, adjoins one new Boolean coordinate `z`, and replaces `T` by two children `T_+` and `T_-` carrying the same old signs and respectively `+1` and `-1` on `z`. The two child cylinders partition the old cylinder after the new coordinate is introduced. Every split increases both row count and column count by one.

Starting from the 11-row / 11-column exact cover:

1. split all 11 rows once: `11 -> 22`, columns `11 -> 22`;
2. split all 22 rows once: `22 -> 44`, columns `22 -> 44`;
3. among those 44 parents, leave parents numbered `12` and `29` unsplit and split the other 42: `44 -> 86`, columns `44 -> 86`.

Thus the deformation uses exactly

\[
11+22+42=75
\]

splits and ends with an `86 x 86` signed support system. The final support-size distribution is

\[
\boxed{42\text{ rows of support size }7,
\qquad44\text{ rows of support size }8.}
\]

This is not the earlier balanced-tree support: its cylinders inherit the non-tree eleven-column base relations.

The rational column weights used for the exact load certificate are

```text
424464,237673,425791,424463,240036,414396,240036,162804,160136,162803,
257027,175629,176389,114214,116017,176387,113232,113232,116017,114214,
181745,181745,124189,124189,124726,124726,80762,80762,82881,81184,
124725,124725,80067,80067,80067,80067,82881,81183,80761,80762,
128514,128514,128514,128514,87814,87814,87814,87814,88194,88194,
88194,88194,57107,57107,57107,57107,57786,57406,57406,88194,
88194,88194,88194,56617,56616,56616,56616,56616,56616,56616,
56616,57785,57405,57405,57107,57107,57107,57107,90873,90873,
90873,90873,90873,90873,90873,90873
```

They are positive integers and sum exactly to `10^7`.

If final row `i` has support `S_i`, define

\[
x_{ij}:=
\frac{W_j^{-1}}{\sum_{k\in S_i}W_k^{-1}}
\qquad(j\in S_i),
\]

and put

\[
A_{ij}:=q\,\sigma_{ij}x_{ij},
\]

where `sigma_ij` is the signed cylinder template; entries outside `S_i` are zero. Then, identically for every row,

\[
\sum_j|A_{ij}|=q.
\]

The exact checker computes the 86 normalized squared column loads

\[
\Lambda_j:=\sum_i x_{ij}^2
\]

using `Fraction`. The worst column is column 32, with diagnostic value

\[
\max_j\Lambda_j
=0.19503917687654113\ldots.
\]

More importantly, exact rational arithmetic verifies

\[
q^2\Lambda_j<1
\qquad\text{for all }j,
\]

with worst scaled squared column norm

\[
0.9999764875307743\ldots<1
\]

and exact positive slack. Therefore every column of `A` has Euclidean norm strictly below one.

**Outcome #6: success.** The partial third-level deformation creates room to equalize the inherited strong eleven-column cover at a common row mass above `2.2643`.

## 5. #25 COUNT THE SAME THING TWICE — pairwise incompatibility plus Kraft mass proves the full Boolean cover

The remaining issue is global Boolean coverage. Enumerating `2^86` signings is neither necessary nor useful.

For a signed row template supported on `s` coordinates, its matching cylinder in the **projective** Boolean cube has mass

\[
2^{-(s-1)}.
\]

The exact checker compares every pair of the 86 final templates. Two projective cylinders would intersect exactly when their signs agree up to one global sign on every common support coordinate. It finds

\[
\boxed{0\text{ compatible pairs}.}
\]

Hence all 86 cylinders are pairwise disjoint. Their total projective mass is

\[
42\cdot2^{-6}+44\cdot2^{-7}
=\frac{84+44}{128}
=1.
\]

Thus the pairwise-disjoint cylinders partition the entire projective Boolean cube.

Consequently every `epsilon in {+-1}^{86}` aligns, up to global sign, with exactly one row `i`. On that row every nonzero summand has the same sign, so

\[
|(A\varepsilon)_i|
=\sum_j|A_{ij}|
=q.
\]

Therefore

\[
\boxed{K_{86}^*\ge\frac{22643}{10000}=2.2643.}
\tag{5.1}
\]

This is a genuine deterministic real-Boolean finite obstruction. No complex phases, vector/rank-two coloring, average-case statement, or numerical optimizer is part of the proof.

**Outcome #25: success.** Coverage is proved by an exact finite incompatibility calculation plus one exact Kraft identity rather than an infeasible signing enumeration.

## 6. Exact movement and propagated lower branch

The preceding strongest R13 obstruction at the same dimension was

\[
\frac{225925611947}{10^{11}}=2.25925611947.
\]

The new exact improvement is

\[
\frac{22643}{10000}
-
\frac{225925611947}{10^{11}}
=
\boxed{\frac{504388053}{10^{11}}}
=
0.00504388053.
\]

Hence the current same-dimension rigorous interval is

\[
\boxed{2.2643\le K_{86}^*\le7.28139.}
\]

Kunisky's doubling construction also propagates the stronger lower endpoint. If

\[
q_0=\frac{22643}{10000},
\qquad
q_{r+1}=\frac{1+q_r}{\sqrt2},
\]
then

\[
K_{86\cdot2^r}^*\ge q_r
\qquad(r\ge0),
\]
with zero-padding giving the same floor for every larger column count. The first diagnostic values are

\[
2.2643,\quad2.3082086658\ldots,\quad
2.3392567812\ldots,\quad2.3612111141\ldots.
\]

This propagated branch is secondary history; it does not replace the owner-tracked upper metric `B_R13(n)`.

## 7. Exact checker, execution, and readback

The self-checker is

`artifacts/R13/20260919T1433Z_refinement-forest-86-d4c7_checker.py`

created at commit

`139e22c4281c4cb781e93a714a0533433d994c4c`.

It was read back at that exact commit. It reconstructs the signed 11-column base templates, executes all 75 support splits, checks the final `86 x 86` dimensions, verifies the `42/44` support-size distribution, checks all projective-pair incompatibilities, verifies the Kraft identity, constructs the rational magnitudes from the 86 integer weights, checks every exact column-load inequality, and verifies the exact improvement over the predecessor lower endpoint.

The executed output is

`artifacts/R13/20260919T1433Z_refinement-forest-86-d4c7.out`

created at commit

`6ba68bc0453d00cca3c4486ac78647ef6ece8445`.

It was read back at that exact commit and ends

`R13_REFINEMENT_FOREST_86_EXACT_PASS`.

This is a **self-check**, not an independent outside audit.

## 8. Prior art and novelty discipline

The broad ingredients are not claimed as new: Kunisky already introduced unsatisfiable matrices, convex support-load optimization, clause/tree refinements, and the doubling lower-bound mechanism. The new claim here is only the specific finite 86-column refinement forest, its rational weight certificate, and the resulting numerical lower endpoint.

Bounded searches on 19 September 2026 included the exact decimal `2.2643` with Komlós/discrepancy terms, `86 Komlos discrepancy lower bound unsatisfiable matrix`, `refinement unsatisfiable matrix Komlos 86 columns`, and the exact R13 eleven-column value combined with doubling/refinement terminology. No matching finite-86 certificate surfaced. This is only bounded negative evidence; **novelty remains UNVERIFIED** and no priority claim is made.

Outside audits of this new sharpening: **0/2**. Closure is not claimed.

## 9. Two structural routes deliberately not turned into certificate churn

Two other genuinely different upper routes were checked and abandoned early rather than padded with unchanged certificates.

First, the Akbas--Sra September 17 small-ball application still carries unnamed universal constants (`q_1`, ultimately upstream curvature/reverse-Hölder constants) in the displayed ordinary-Komlós corollary. Without a new quantitative constant chase through those predecessors, it does not yet yield a rigorous finite number competitive with `7.28139`.

Second, permutation-symmetrized mixed cosine exponents reduce rigorously to a balanced-direction mixed inverse-gamma law, but exploratory two-exponent scouting near the homogeneous `p=33/20` optimum did not improve the homogeneous finite-`D` value. Those numerical scouts are discovery-only and support no theorem, so no artifact was manufactured for them.

The successful route was therefore the lower-obstruction deformation above, which changes the actual R13 continuation quantity rather than adding another auxiliary lemma to an unchanged upper proof.

## 10. Next research obligation

The fixed upper metric has one unchanged run, not three, because the predecessor moved it. R13 is not in the Section-I stuck state. The hard-assignment continuation condition is independently satisfied because the explicit finite obstruction moved substantially at the owner-relevant dimension.

The next useful lower attack is **not** another rational retuning of these same 86 supports. The support-load optimizer indicates the present refinement pattern has additional decimal headroom, but spending a run merely closing that tiny gap would violate the new-method priority. The higher-value lower question is whether a different selection of unsplit parents or a different small exact base gadget changes the support combinatorics enough to produce a visibly larger obstruction. On the upper side, the high-value targets remain an intersection-aware six-column theorem below about `7.28139/sqrt(15)`, a genuinely nonproduct DTV density, or an explicit constant extraction from a different small-ball mechanism.

## 11. Model / scheduler-control status

The limitation remains the same on the exposed task-control surface: it provides task title/prompt, schedule/timing, enablement, and update controls, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort telemetry**. GPT-6/maximum is therefore still a prompt request rather than an enforceable runtime setting on this surface.

The current repository reconciliation is more precise than the old one-line failure: P26/P01/P03 modifications were denied in one native context with `You cannot modify this task`, while `RESULTS.md` records that P26 later updated successfully from a different authorized context. The legitimate remedy for an inaccessible task is therefore its owning/authorized product or workspace context, an owner/admin surface that actually exposes the needed controls where supported, or platform support. A duplicate task, repository edit, or permission bypass is not a scheduler repair.

## Status

**SOURCE QUALITATIVE STATUS KNOWN / R13 QUANTITATIVE STATUS PARTIAL / FIXED UPPER METRIC NO MOVEMENT / FIXED-UPPER UNCHANGED COUNT 1 / EXPLICIT FINITE OBSTRUCTION MOVED / full written proof / exact self-check PASS / outside audits 0/2 / novelty UNVERIFIED.**

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Boolean Komlos vector balancing; current qualitative resolution Guo-Fang-Lu arXiv:2609.11189; finite quantitative continuation"
  target: "Every real unit-column matrix admits Boolean signs; track complete certified upper B_R13(n) and permitted explicit finite obstructions"
  fixed_metric: "complete pointwise upper envelope B_R13(n) with all inherited constants/domains"
  upper_before: "B_R13(86)=728139/100000=7.28139"
  upper_after: "B_R13(86)=728139/100000=7.28139"
  upper_movement: "none"
  fixed_upper_unchanged_count: 1
  finite_obstruction_before: "K_86^* >= 225925611947/10^11 = 2.25925611947"
  finite_obstruction_after: "K_86^* >= 22643/10000 = 2.2643"
  finite_obstruction_exact_gain: "504388053/10^11 = 0.00504388053"
  methods: [6, 23, 25]
  status: "PARTIAL"
  source_status: "KNOWN / resolved qualitatively in 2026 preprint literature"
  checker: "artifacts/R13/20260919T1433Z_refinement-forest-86-d4c7_checker.py @ 139e22c4281c4cb781e93a714a0533433d994c4c"
  output: "artifacts/R13/20260919T1433Z_refinement-forest-86-d4c7.out @ 6ba68bc0453d00cca3c4486ac78647ef6ece8445"
  audits: "0/2 for this sharpening"
  novelty: "UNVERIFIED"
```
