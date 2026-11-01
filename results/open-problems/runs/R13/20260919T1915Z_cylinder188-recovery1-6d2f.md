Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **NO MOVEMENT in the fixed upper metric** `B_R13(86)=728139/100000=7.28139`; fixed-upper unchanged count `3 -> 4`. The retained finite lower obstruction also has no movement and remains `K_86^* >= 452931/200000 = 2.264655`. This is **STUCK1 recovery 1**. Methods actually used: **#16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #20 FIND WHY THE ALGORITHM FAILS, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.** The recovery did not prove `K_6^* <= 47/25`, but it rigorously eliminates the entire six-column **full-alignment/projective-cylinder** obstruction mechanism at that threshold.

# R13 — Boolean Komlós STUCK1 recovery 1: exact no-go for every six-column full-alignment cover at 47/25

Run ID: `20260919T1915Z_cylinder188-recovery1-6d2f`  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity, source status, mandatory state recovery

I continued from the newest complete R13 report

`runs/R13/20260919T1732Z_stuck1-k6-threshold-c1e8.md`

rather than restarting. That report triggered the owner's first stuck episode after three consecutive unchanged fixed-upper runs and selected exactly one recovery:

\[
\boxed{K_6^*\le 47/25=1.88.}
\]

It also prescribed methods `#16,#20,#30`, which are the methods used below.

At run start I reread/reconciled `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R13 report, the R13 exact `n=5` and `n=6` finite history, the newest neighboring R02 Boolean-small-ball reconciliation, and current R16 ownership state. `QUEUE.md` continues to treat Boolean Komlós as R13's hard assignment, not a free reserve item. I edited no shared root and no peer-track file.

Current literature was refreshed on 19 September 2026. Guo--Fang--Lu, arXiv:2609.11189 (submitted 10 September 2026), prove the genuine real-Boolean dimension-free bound `3 sqrt(2 pi)`. Akbas--Sra, arXiv:2609.20785 (submitted 17 September), recover Komlós using their Boolean small-ball machinery together with the Guo--Fang--Lu signing input. Karingula--Lovett, ECCC TR26-188 (17 September), give an elementary real-sign proof with constant `36`. Bansal--Jiang, arXiv:2508.03961, remains the earlier real-Boolean `~O(log^(1/4)n)` route. Therefore the qualitative source is **KNOWN in current 2026 preprint/technical-report literature**; R13 is only a finite-dimensional quantitative track.

Kunisky's 2023 SIAM J. Discrete Math. paper already develops unsatisfiable/clause-variable matrix lower bounds, convex scaling, and dual certificates, with asymptotic lower constant approaching `1+sqrt(2)`. The full-alignment/cylinder mechanism below is therefore closely related to published prior art. A bounded fresh search for the exact `47/25` six-column no-go, the particular 27-support classification, and the rational endpoint below found no matching source, but that is only negative search evidence. **Novelty remains UNVERIFIED.**

## 2. Fixed metric before / after — no movement

The tracked quantity remains

\[
K_n^*:=\sup_{m\ge1}\sup_{A:\,\|A_{\cdot j}\|_2\le1}
\min_{\varepsilon\in\{\pm1\}^n}\|A\varepsilon\|_\infty,
\]

with the complete certified upper envelope `K_n^* <= B_R13(n)`.

Put

\[
T_5=\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13}.
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

The one-threshold branch is

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

For every integer `D>=135`, the inherited conditional-tail branches remain

\[
C_D^-=\frac{27\sqrt{10\pi}}{20}(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,-}),
\quad
L_-(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{C_D^-,\frac n{\sqrt{D+1}}\right\},
\]

and, for `r=2,3,4`,

\[
C_D^{(r)}=\frac{27\sqrt{10\pi}}{20}(1-\beta_D^{\uparrow,3}-\beta_D^{\downarrow,r}),
\quad
L_r(n)=\inf_{D\in\mathbb Z,\,D\ge135}\max\left\{C_D^{(r)},\frac n{\sqrt{D+1}}\right\}.
\]

Their exact conditional moments, thresholds, truncation definitions and failed-threshold zero conventions are inherited unchanged from the immutable predecessor chain.

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
Writing `1-C_{D,5}(x)=sum_{ell=1}^D c_{ell,D}^{(5)}x^ell`,

\[
\beta_{D,5}^{\uparrow}=\frac12\sum_{\ell=1}^D c_{\ell,D}^{(5)}
\left[\frac1{7\ell/5-1}-\frac1{7\ell/5-1/2}\right],
\]

and retaining exactly the predecessor's truncated `U=157/20`, four-shell Cantelli functional `beta_{D,5}^{downarrow}`,

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
\boxed{B_{R13}(86)=728139/100000=7.28139}
\]

before and after the run. The fixed-upper unchanged count is `3 -> 4`. The retained lower endpoint at the same dimension is

\[
\boxed{K_{86}^*\ge452931/200000=2.264655.}
\]

The recovery target is valuable because

\[
\frac{47}{25}\sqrt{15}=7.281208690\ldots<7.28139,
\]

so a proof of `K_6^*<=47/25` would immediately move the fixed metric. This run does **not** prove it.

## 3. Method #30 — localize completely to one scale and one lower-obstruction mechanism

Work only at

\[
n=6,\qquad t=47/25,\qquad c=t^{-2}=625/2209.
\]

There are 32 antipodal/projective Boolean sign classes.

A signed support `(S,sigma)` with `S subset [6]` defines its **full-alignment cylinder**: the projective classes whose signs agree with `sigma` on all coordinates in `S`, up to global negation. If `|S|=s`, the cylinder contains exactly

\[
2^{6-s}
\]

projective classes.

This is precisely the Boolean-formula / unsatisfiable-matrix style mechanism in which every signing is forced because it fully aligns with at least one row. I deliberately separated this category from arbitrary rows, whose threshold-bad families may be strictly larger than their full-alignment cylinders.

Width `s=1` cannot participate at threshold `t>1`: a one-coordinate row with `ell_1` norm exceeding `t` would contain an entry exceeding one in magnitude and hence violate that column's Euclidean norm bound. Thus only widths `2,...,6` matter.

## 4. Analytic normalization: every feasible cylinder obstruction has integer cost at most 101

Suppose rows indexed by `i` have full-alignment cylinders covering all 32 projective classes and each row has `ell_1` mass

\[
L_i>t.
\]

Write its positive normalized absolute coefficients as

\[
x_{ij}=\frac{|a_{ij}|}{L_i},\qquad
\sum_{j\in S_i}x_{ij}=1.
\]

For each coordinate `j`, the column condition gives

\[
1\ge\sum_i a_{ij}^2
=\sum_i L_i^2x_{ij}^2
>t^2\sum_i x_{ij}^2,
\]

hence

\[
\sum_i x_{ij}^2<c=\frac{625}{2209}.
\tag{4.1}
\]

For a row supported on `s_i` coordinates, Cauchy gives

\[
\sum_{j\in S_i}x_{ij}^2\ge\frac1{s_i}.
\]

Summing over rows and then columns,

\[
\sum_i\frac1{s_i}
\le\sum_{i,j}x_{ij}^2
<6c=\frac{3750}{2209}.
\tag{4.2}
\]

Use cost units `60/s_i`, which are integers for `s_i=2,...,6`. Equation (4.2) implies

\[
\sum_i\frac{60}{s_i}
<360c
=\frac{225000}{2209}
=101.856\ldots.
\]

Therefore every candidate full-alignment obstruction at `47/25` has exact integer cost

\[
\boxed{\sum_i60/s_i\le101.}
\tag{4.3}
\]

This is the finite entry point for method #16.

## 5. Method #16 — exhaustive exact cover classification

Modulo global negation there are exactly **358** distinct signed projective cylinders with widths `2,...,6`. The checker enumerates all cylinder covers of the 32 projective classes with cost at most 101, using first-uncovered branching and exact 32-bit masks.

The complete search visits

\[
\boxed{1,249,005,886}
\]

search nodes and reaches

\[
\boxed{2,318,559}
\]

terminal covers.

A first exact dual prune is applied for every nonempty coordinate subset `J`: take coordinate prices uniform on `J`. This leaves 257,222 terminal covers. Redundant cylinders are then deleted—deleting a redundant row can only improve load feasibility—and the support multisets are quotiented by all `6!=720` coordinate permutations.

Exactly

\[
\boxed{27}
\]

canonical support multisets remain.

The search is exhaustive within the stated cylinder category: every width-2-through-6 signed cylinder is generated; every possible cost-`<=101` cover is reached by the first-uncovered branching; the cost lower bound for remaining uncovered points is valid because a width-two cylinder has the best new-points-per-cost ratio; and canonicalization occurs only after terminal coverage is established.

## 6. Exact load dual kills every one of the 27 survivors

For a fixed support family `S_1,...,S_q`, define the normalized-load optimum

\[
t_*(S)=
\min_{\substack{x_{ij}\ge0\\\sum_{j\in S_i}x_{ij}=1}}
\max_{1\le j\le6}\sum_{i:j\in S_i}x_{ij}^2.
\tag{6.1}
\]

For any positive coordinate weights `lambda_j` summing to one,

\[
\max_j\sum_i x_{ij}^2
\ge
\sum_j\lambda_j\sum_i x_{ij}^2
=
\sum_i\sum_{j\in S_i}\lambda_jx_{ij}^2.
\]

Weighted Cauchy minimizes the `i`th term subject to `sum_{j in S_i}x_{ij}=1`, giving

\[
\sum_{j\in S_i}\lambda_jx_{ij}^2
\ge
\left(\sum_{j\in S_i}\lambda_j^{-1}\right)^{-1}.
\]

Therefore

\[
\boxed{
t_*(S)\ge D_S(\lambda):=
\sum_i\left(\sum_{j\in S_i}\lambda_j^{-1}\right)^{-1}.}
\tag{6.2}
\]

For each of the 27 canonical support families, the checker embeds a positive integer vector `W=(W_1,...,W_6)` and uses the exact rational choice

\[
\lambda_j=\frac{W_j}{\sum_kW_k}.
\]

Every one of the 27 exact dual values satisfies

\[
D_S(\lambda)>\frac{625}{2209}.
\tag{6.3}
\]

The weakest embedded certificate is canonical survivor 26, with support masks

`[7,11,29,29,46,46]`

and weights

`[203,203,192,192,105,105]`.

Its exact dual value is

\[
\boxed{
D=\frac{52208352}{177787625}
=0.293655714226454\ldots
>
\frac{625}{2209}
=0.282933454051607\ldots.}
\]

Indeed the exact positive gap is

\[
D-\frac{625}{2209}
=\frac{4210983943}{392732863625}>0.
\]

Since (4.1) would require every coordinate normalized load to be **strictly below** `625/2209`, (6.3) rules out all 27 survivors.

### Theorem R13-CYL188

There is **no** six-column real Komlós obstruction at threshold `47/25` whose proof of badness for every Boolean signing comes solely from a cover of the 32 projective sign classes by rows' full-alignment cylinders.

Equivalently: among six-column constructions of the unsatisfiable/full-alignment cylinder type, no admissible unit-column matrix can have every Boolean signing forced above `47/25` by full alignment with one of its rows.

This is a genuine finite theorem with a complete exact certificate. It is **not** the unrestricted statement `K_6^*<=47/25`.

## 7. Method #20 — exact failure of the natural algorithm

The result identifies the missing mechanism sharply.

The known six-row lower obstruction from R13 has a projective-cylinder partition, and its support family appears here (up to coordinate permutation) as the weakest of the 27 surviving combinatorial patterns before the final load dual. Its optimized load is already well above the `625/2209` load required to reach `1.88`. Thus simply changing the SAT/cylinder support pattern cannot bridge the remaining gap at six columns within the entire cost-feasible full-alignment category.

But an arbitrary row at threshold `1.88` may be bad on sign classes that are **not fully aligned** with all of its nonzero coefficients. Those threshold halfspace families can overlap in ways that cylinders cannot. This is why the present theorem does not imply the desired `K_6^*<=1.88`.

A second diagnostic reinforces the point: if one drops actual projective-cover compatibility and reasons only from abstract support incidences/load counts, artificial support patterns can pass the coarse energy tests. So neither support load alone nor cylinder combinatorics alone is enough. The unrestricted proof has to combine the exact threshold-halfspace type with the six coordinate-energy constraints.

That is the precise failure of the natural algorithm: **full alignment is too rigid; arbitrary threshold-bad sign families are the remaining obstruction.**

## 8. Exact artifact and execution

Exact checker:

`artifacts/R13/20260919T1915Z_cylinder188-recovery1-6d2f_checker.cpp`

creation/readback commit `811fa975251ef66cf19dcad9d210615bea1dd88c`.

Archived executed output:

`artifacts/R13/20260919T1915Z_cylinder188-recovery1-6d2f.out`

creation/readback commit `a0d3ee5333955ce654b3b1a2c9b6e120b7d42fd0`.

The executed output records:

```text
R13_CYLINDER_188_EXACT_PASS
projective_classes=32 cylinders_width_2_to_6=358
target_t=47/25 target_c=625/2209
aggregate_cost_cutoff_units_60=101 because 225000/2209=101.856...
search_nodes=1249005886 terminal_covers=2318559 cheap_dual_survivors=257222
canonical_support_survivors=27
minimum_embedded_dual_index=26 numerator=52208352 denominator=177787625
minimum_embedded_dual_decimal~0.293655714226454 > 625/2209~0.282933454051607
all_27_exact_rational_dual_certificates_pass=1
```

All acceptance decisions use exact integer bitmasks and exact `boost::multiprecision::cpp_int` rational comparisons. Decimal values are diagnostics only. This is a **self-check**, not an independent outside audit.

## 9. What remains, and recovery accounting

The exact blocker remains the unrestricted six-column theorem

\[
\boxed{K_6^*\le47/25.}
\]

The simplest surviving object is now more specific than in STUCK1: classify and couple the possible **non-cylinder threshold bad families**

\[
\mathcal B_t(r)=\{[\varepsilon]:|r\cdot\varepsilon|>t\}
\]

at `t=47/25` under the six separate column-energy budgets.

Preliminary discovery work suggests this may still admit a finite reduction: after fixing a positive sorted row, its oriented bad family is a shifted downset, and the diameter constraints at `t=1.88` make the list of combinatorial types small enough to attack. That observation is scouting only and is not promoted to a theorem in this report.

This run is **STUCK1 recovery 1 of at most 2**. It made no fixed-metric movement and no lower-obstruction movement, but it completely eliminates one major source-matching mechanism rather than adding an auxiliary estimate to it. The next and final recovery on this target will use a genuinely different route: enumerate arbitrary realizable threshold-family types rather than cylinders, formulate their exact multirow energy dual, and attempt the `47/25` theorem directly. Planned Section-B methods are **#18 SAY IT IN ANOTHER LANGUAGE, #11 DUALIZE, #4 PROVE SOMETHING WEAKER COMPLETELY**. If that recovery returns to the same missing multirow step without moving the fixed metric or a source-matching finite obstruction, R13 must leave a handoff and rotate under the two-recovery rule.

## 10. Model / scheduler control

The available task-control surface still exposes prompt/title, schedule/timing, enabled state, and update/list operations, but **no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort receipt**. GPT-6 maximum therefore remains prompt-only on this surface; this run actually executed as GPT-5.6 Sol with reasoning level UNVERIFIED.

The repository's current reconciliation records the earlier P26 `You cannot modify this task` result as authorization-context dependent and a later successful P26 update from another authorized context. The lawful workaround is therefore the task-owning/authorized product or workspace surface, or platform support—not duplication or permission bypass. No scheduler, permission, workflow, email, Drive, purchase, or public-posting action was made.

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  canonical_intake_alias: I0091
  source_target: real Boolean Komlos signing
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  quantitative_track_status: PARTIAL
  fixed_metric_name: complete rigorously certified upper envelope B_R13(n)
  fixed_metric_before: B_R13(86)=728139/100000
  fixed_metric_after: B_R13(86)=728139/100000
  fixed_metric_movement: NONE
  fixed_metric_unchanged_count: 4
  retained_lower_n86: 452931/200000
  stuck_episode: STUCK1
  recovery_number: 1
  recovery_target: K_6^* <= 47/25
  recovery_result: restricted full-alignment/projective-cylinder mechanism eliminated at 47/25; unrestricted target unresolved
  new_claim: R13-CYL188
  exact_search_nodes: 1249005886
  exact_terminal_covers: 2318559
  canonical_support_survivors_before_final_dual: 27
  weakest_exact_dual: 52208352/177787625
  target_normalized_load: 625/2209
  exact_self_check: PASS
  outside_audits_new_claim: 0/2
  novelty: UNVERIFIED
  methods: [16,20,30]
  next_methods: [18,11,4]
  next_route: arbitrary realizable non-cylinder threshold-family classification plus exact multirow energy dual
```
