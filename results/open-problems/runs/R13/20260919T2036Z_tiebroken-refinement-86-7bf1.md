Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper metric** `B_R13(n)` (`B_R13(86)=728139/100000=7.28139` remains unchanged; fixed-upper unchanged count `0 -> 1`), but the **explicit finite obstruction MOVED** `K_86^*: 452931/200000 = 2.264655 -> 2830911/1250000 = 2.2647288`, exact gain `369/5000000 = 0.0000738`. Methods actually used: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #13 FIND WHAT ONLY INCREASES, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R13 — Boolean Komlós: tie-broken shallow refinement of the 11-cylinder cover

Run ID: `20260919T2036Z_tiebroken-refinement-86-7bf1`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity and required state

I continued from the newest complete R13 report

`runs/R13/20260919T1935Z_k6-le2-recovery2-4c7a.md`

rather than restarting. That report resolved STUCK1 recovery 2 by proving the genuine arbitrary-row theorem

\[
K_6^*\le 2,
\]

and added the exact universal branch

\[
U_6(n)=2\sqrt{\lceil n/6\rceil}
\]

to the complete pointwise upper envelope. Since that moved the owner-fixed function `B_R13(n)`, the fixed-metric unchanged count reset to zero.

Before new mathematics I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and `operations/NEW_METHODS_2026-09-16.md`;
- the current Boolean-Komlós intake alias/reconciliation around canonical row `I0091`;
- the newest complete R13 report and its finite-dimensional predecessor chain;
- the exact previous `n=86` refinement checker;
- the newest neighboring discrepancy report visible in R02.

No shared root, peer track, scheduler, workflow, email, Drive, permission, purchase, or public-posting state was changed.

## 2. Current source/literature status, checked 19 September 2026

The qualitative real-Boolean Komlós conjecture is **KNOWN / RESOLVED in current 2026 preprint literature**, not open:

1. Shengtao Guo, Ethan X. Fang, and Junwei Lu, *Vector Balancing via Directional Total Variation*, arXiv:2609.11189, submitted 10 September 2026, prove the real-sign dimension-free bound `3 sqrt(2 pi)`.
2. Emrullah Akbas and Suvrit Sra, *Boolean Small-Ball Inequalities for Discrepancy Theory*, arXiv:2609.20785, submitted 17 September 2026, recover Komlós among their applications.
3. Sankeerth Rao Karingula and Shachar Lovett, ECCC TR26-188, 17 September 2026, give an elementary real-sign proof with constant `36`.
4. Nikhil Bansal and Haotian Jiang, arXiv:2508.03961v2, remain the earlier real-Boolean `~O((log n)^(1/4))` benchmark through which R13 originally navigated.

Kunisky's published unsatisfiable-matrix construction remains relevant lower-bound prior art and approaches `1+sqrt(2)`. R13 is therefore a **finite-dimensional quantitative** track only. Complex phases, vector/rank-two colorings, and average-case bounds are not substituted for the Boolean statement.

A bounded search for `2.2647288`, `86-column Komlos`, and refinement-tree/cylinder variants found no matching finite certificate. This is only bounded negative evidence. The refinement/unsatisfiable-matrix mechanism has prior art, so **novelty is UNVERIFIED and no priority claim is made**.

## 3. Fixed upper metric before and after — unchanged this run

The tracked quantity remains

\[
K_n^*:=\sup_{m\ge1}\sup_{A:\,\|A_{\cdot j}\|_2\le1}
\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty,
\]

and the owner-fixed metric is the complete rigorously certified pointwise upper function `B_R13(n)`.

Put

\[
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13},
\qquad
U_6(n)=2\sqrt{\left\lceil\frac n6\right\rceil}.
\]

The retained oldest DTV branch is

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

The one-threshold branch remains

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

For the retained three-threshold occupancy coefficients `c_{ell,D}^{(3)}`,

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

For every integer `D>=135`, the exact inherited conditional-tail branches remain

\[
C_D^-=\frac{27\sqrt{10\pi}}{20}(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\quad
L_-(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\},
\]

and for `r=2,3,4`,

\[
C_D^{(r)}=\frac{27\sqrt{10\pi}}{20}(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,r}),
\quad
L_r(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{C_D^{(r)},\frac n{\sqrt{D+1}}\right\}.
\]

The exact predecessor definitions of the conditional moments, thresholds, truncations, and failed-threshold zero conventions are inherited **unchanged** from `runs/R13/20260919T1935Z_k6-le2-recovery2-4c7a.md`; no parameter or admissible domain is changed here.

The retained five-threshold branch uses

\[
A_{k,D}=\frac{5}{7(4437/5000)}\left(1-\frac{2k}{5D}\right)
\left(\frac{2k}{5}\right)^{7/5}D^{-2/5},\qquad k=1,\ldots,5,
\]
with `a_k=A_{k,D}/D`, `a_0=0`, `d_k=a_k-a_{k-1}`,

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

and retaining exactly the predecessor's truncated `U=157/20`, four-shell Cantelli functional `beta_{D,5}^{downarrow}` and its zero conventions,

\[
L_5(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{
\frac{27\sqrt{10\pi}}{20}(1-\beta_{D,5}^{\uparrow}-\beta_{D,5}^{\downarrow}),
\frac n{\sqrt{D+1}}\right\}.
\]

The explicit transform branches remain

\[
L_{\rm LT}(n)=\max\left\{\frac{739097}{100000},\frac n{\sqrt{136}}\right\},
\]
\[
L_{33/20}^{\rm shell}(n)=\max\left\{\frac{728139}{100000},\frac n{\sqrt{140}}\right\}.
\]

Therefore the complete current upper envelope remains

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\
\sqrt2,&n=2,\\
(\sqrt{11}+\sqrt2)/3,&n=3,\\
\sqrt3,&n=4,\\
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},U_6,G_0,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&5\le n\le85,\\
\min\{U_6,G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_{\rm LT},L_{33/20}^{\rm shell}\}(n),&n\ge86.
\end{cases}}
\]

In particular,

\[
\boxed{B_{R13}(86)=\frac{728139}{100000}=7.28139}
\]

before and after this run. The fixed-upper unchanged count is `0 -> 1`, not a stuck trigger.

## 4. Methods #5, #13, #30 — change the topology, not another coefficient

The immediately preceding R13 triple was `#18/#11/#4`. This run deliberately changes mechanism.

### #5 ADD A PARAMETER AND DIFFERENTIATE IN IT

The predecessor's `n=86` obstruction was built by refining the exact eleven-cylinder base cover with leaf-count vector

\[
(11,11,6,5,11,5,5,5,5,11,11).
\]

I treated the refinement **topology** as the new parameter. First I varied the leaf-count allocation by single transfers and random local walks; those searches did not beat the predecessor support family. I then held the leaf counts fixed and varied the tie-breaking order among leaves of equal minimum depth. This changes support incidence without changing the depth or support-size histograms.

Numerical convex optimization was used only as a scout. No theorem below depends on floating-point optimization.

### #13 FIND WHAT ONLY INCREASES

For a fixed support family `S=(S_i)`, the normalized load problem is

\[
t(S)=\min_{x_{ij}\ge0,\ \sum_{j\in S_i}x_{ij}=1}
\max_j\sum_{i:j\in S_i}x_{ij}^2.
\]

A feasible family at scale `q` gives a Komlós obstruction whenever `q^2 t(S)<1`. The dual/scout parameterization uses positive column prices and the corresponding reciprocal-weight row solution; during topology search I retained a candidate only when the scout value of `1/sqrt(t(S))` strictly increased. This monotone acceptance exposed a better support incidence pattern rather than another scalar magnitude tweak.

### #30 DO ONE SCALE / ONE DIRECTION AT A TIME

I localized the topology change severely: every split still acts on a **currently shallowest** leaf and introduces exactly one new coordinate. Only the tie-breaking among equally shallow leaves changes. Consequently the new forest keeps exactly

\[
17\text{ leaves at depth }2,\qquad39\text{ at depth }3,\qquad30\text{ at depth }4,
\]

and exactly

\[
42\text{ supports of size }7,\qquad44\text{ supports of size }8.
\]

For the small bases with five or six leaves I also exhaustively screened their shallow tie sequences while holding the other bases fixed and found no further improvement of the scout objective. That is **search evidence only**, not an optimality theorem for the full topology class.

The successful deterministic split-choice lists are archived in the exact checker. Their scout optimum was around `2.26473`; the actual theorem uses the independent rational certificate below.

## 5. Exact new finite obstruction

The exact base remains the eleven-column signed cylinder cover from R13 history. Apply the same leaf-count vector as above, but use the new deterministic shallow tie-break choices in the checker. This produces exactly 86 signed cylinders on 86 coordinates.

Let `S_i` denote the final support of row `i`. The checker proves exactly:

1. the 86 projective cylinders have **zero compatible pairs**;
2. their projective Kraft mass is

\[
42\,2^{-6}+44\,2^{-7}=1.
\]

Therefore they partition the entire projective Boolean cube.

Now use the explicit positive integer weights `W_j` archived in the checker and define

\[
x_{ij}=\frac{W_j^{-1}}{\sum_{k\in S_i}W_k^{-1}}
\qquad(j\in S_i).
\]

Then every normalized row has exact `l1` mass one. Put

\[
q=\frac{2830911}{1250000}=2.2647288
\]

and give row `i` its archived cylinder signs `sigma_{ij}` with magnitudes

\[
A_{ij}=q\,\sigma_{ij}x_{ij}.
\]

Every row has exact absolute mass `q`.

Because the cylinders form a projective partition, for every Boolean signing `epsilon in {+-1}^{86}` there is exactly one row whose sign template agrees with `epsilon` up to global sign. On that row,

\[
|(A\varepsilon)_i|=\sum_j|A_{ij}|=q.
\]

It remains only to verify the column norm constraint. The exact `Fraction` checker computes all 86 normalized loads

\[
\ell_j=\sum_i x_{ij}^2
\]

and proves

\[
q^2\ell_j<1\qquad(j=1,\ldots,86).
\]

The worst diagnostic value is at column 2 (zero-based checker index):

\[
\max_j q^2\ell_j
=0.9999999388761972\ldots<1,
\]

with exact positive rational slack. Therefore every column has Euclidean norm strictly below one.

Hence

\[
\boxed{K_{86}^*\ge\frac{2830911}{1250000}=2.2647288.}
\]

The predecessor certified

\[
K_{86}^*\ge\frac{452931}{200000}=2.264655,
\]

so the exact movement is

\[
\boxed{
\frac{2830911}{1250000}-\frac{452931}{200000}
=\frac{369}{5000000}
=0.0000738.}
\]

The current same-dimension certified interval is therefore

\[
\boxed{2.2647288\le K_{86}^*\le7.28139.}
\]

Zero-padding preserves the new lower obstruction for every `n>=86`; this is secondary lower-bound history and does not change the owner-fixed upper metric.

## 6. Exact artifacts

Idea written before the checker:

- `artifacts/R13/20260919T2036Z_tiebroken-refinement-86-7bf1_idea.md`
- creation commit `7f7d682254694d13a1d373876819d19a5be41e8d`.

Exact checker:

- `artifacts/R13/20260919T2036Z_tiebroken-refinement-86-7bf1_checker.py`
- creation/readback commit `5470cf68cc56045418e57ac846f65a781abdcc5b`.

Archived executed output:

- `artifacts/R13/20260919T2036Z_tiebroken-refinement-86-7bf1.out`
- creation/readback commit `18271a8b951be27e46ca43e08425303c34e6d610`.

The archived output records:

- 86 rows and 86 columns;
- leaf counts `(11,11,6,5,11,5,5,5,5,11,11)`;
- refinement depths `{2:17,3:39,4:30}`;
- support sizes `{7:42,8:44}`;
- projectively compatible pairs `0`;
- Kraft mass `1`;
- worst normalized load `0.19496989938581294...`;
- worst scaled column norm squared `0.9999999388761972...`;
- exact positive slack;
- new lower bound `2830911/1250000`;
- exact improvement `369/5000000`;
- terminal `R13_TIEBROKEN_SHALLOW_86_EXACT_PASS`.

This is a **self-check**, not an independent audit.

## 7. What this run learned / what not to do next

This movement comes from support **incidence**, not another decimal tightening of the previous magnitude vector. The same leaf counts and the same support-size/depth histograms can support a strictly stronger obstruction solely because equal-depth split tie-breaking changes how rows share columns.

The next lower-bound run should therefore **not** spend its research budget retuning these 86 rational weights. A structurally useful continuation would either:

- quotient shallow tie-break trees by the automorphism group of the eleven-base cover and optimize topology classes rather than individual sequences;
- prove a topology-class upper/dual bound showing this shallow-refinement family is near saturation; or
- change the base exact cover rather than its descendant weights.

On the upper side, `K_6^*<=2` is now exact certified progress but is still too weak to improve the `n=86` headline through the six-block compiler. A genuinely new small-column theorem below about `1.88005` would beat the current `7.28139` branch at `n=86`.

Suggested next genuinely different Section-B triple: **#3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #21 ASK WHO ELSE HAS THIS SHAPE**. Do not simply repeat the present topology search.

## 8. Model / scheduler-control truth

The prompt requests GPT-6 with maximum reasoning, but this invocation identifies as **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The available scheduler/task-control surface exposes prompt/title, schedule/timing, enabled state and ordinary update fields, but **no binding model-family selector, no reasoning-effort selector, no guaranteed-duration field, and no authenticated completed-run model/effort receipt**. GPT-6/maximum therefore remains prompt-only from this surface. A binding change requires an owner-authorized product/workspace/admin/API scheduler that actually persists those routing fields and attests the values executed.

The historical P26 `You cannot modify this task` response is authorization-context dependent; later repository evidence records successful P26 reconciliation from an authorized context. The compliant workaround is the task's owning/authorized workspace/interface or platform support, not duplication or permission bypass.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R13
  lane: HARD_OUTSIDE
  target: Boolean_Komlos_quantitative_finite_dimension
  qualitative_source_status: KNOWN_RESOLVED_2026_PREPRINT_LITERATURE
  quantitative_status: PARTIAL
  fixed_metric_name: complete_rigorously_certified_B_R13(n)
  fixed_metric_before: unchanged_current_envelope_with_U6_and_DTV_branches
  fixed_metric_after: unchanged_current_envelope_with_U6_and_DTV_branches
  B_R13_86_before: 728139/100000
  B_R13_86_after: 728139/100000
  fixed_metric_movement: false
  fixed_upper_unchanged_count_before: 0
  fixed_upper_unchanged_count_after: 1
  permitted_finite_obstruction_name: K_86_star_lower_bound
  finite_obstruction_before: 452931/200000
  finite_obstruction_after: 2830911/1250000
  finite_obstruction_exact_gain: 369/5000000
  finite_obstruction_movement: true
  methods: [5, 13, 30]
  exact_self_check: PASS
  outside_audits: 0/2
  novelty: UNVERIFIED
  lifecycle: CONTINUE_HARD
  continuation_reason: explicit_finite_obstruction_moved
  next_methods: [3, 14, 21]
```

**Status: SOURCE QUALITATIVE STATUS KNOWN / R13 QUANTITATIVE STATUS PARTIAL / FIXED UPPER METRIC NO MOVEMENT / FIXED-UPPER UNCHANGED COUNT 1 / EXPLICIT FINITE OBSTRUCTION MOVED / exact self-check PASS / outside audits 0/2 / novelty UNVERIFIED.**
