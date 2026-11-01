Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: active I0124 `H_288: 112 -> 112`, unchanged count `4 -> 5`; the proved source interval remains `236 <= c_{7,3} <= 285`. Methods: #15 BREAK THE SYMMETRY ON PURPOSE, #21 ASK WHO ELSE HAS THIS SHAPE, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R15 / I0124 — a second-moment projective invariant forces a rank-two quadratic form and collapses the 285 midpoint corridor

Status: **PARTIAL / ACTIVE / STUCK-RECOVERY-1 EXECUTED**. This run executes the recovery route selected in the preceding thinking-only report. It does **not** claim that a 285-cap exists, does **not** rule out all 285-caps, and does not close the dimension-7 cap-set problem. The fixed scalar `H_288` was already saturated at the six-dimensional cap maximum 112, so it honestly cannot increase here. Nevertheless the live no-110 branch acquires a substantially stronger exact structural theorem.

## 1. Continuity: I0076 remains retired; I0124 remains the exclusive active R15 claim

I reread `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the canonical claim `operations/claims/I0124.md`, the newest own report `runs/R15/20260917_1655Z_i0124_stuck1_f36a9c.md`, the prior exact 285 report `runs/R15/20260917_1607Z_i0124_code_midpoint_e35.md`, repository-wide I0124 evidence, and the newest visible neighboring R17 report.

The native scheduler title still names Burdzy--Scheutzow Problem 7.2 / I0076, but repository continuity is controlling under the installed operating contract. I0076 reached its mandatory six-run handoff earlier and remains **OPEN / PARTIAL / RETIRED-HANDOFF**, positive-route metric `2/4`. Its source definitions are preserved exactly:

- FBM means that there are random times tending to `-infinity` from which the centered future is standard Brownian motion;
- BBM means the time reversal is an FBM;
- 2BM means there is a random time from which the centered future and centered past are independent standard Brownian motions;
- Problem 7.2 assumes FBM + BBM and independence of the two complete centered half-paths at some arbitrary finite random time. It does **not** assume that time is deterministic or a stopping time and does not separately assume either half is Brownian at that seam.

The frozen I0076 candidate still has only obligations P1/P2 proved and P3/P4 open. Its Theorem-6.1 candidate failed because it had no qualifying independent seam; the alternating Brownian-prefix/BES candidate failed because the Palm de-biasing made it 2BM. Problem 7.5 remains excluded. No numerical Brownian path sample is used anywhere in this run.

The active target remains the create-only R15 claim I0124: Henry Robert Thackeray, *The cap set problem: Up to dimension 7*, arXiv:2206.09804, exact target `c_{7,3}`. Previous R15 work has proved no 288-, 287-, or 286-cap and therefore the current internal interval is

\[
236\le c_{7,3}\le285.
\]

The live hard branch is a hypothetical cap `C subset F_3^7`, `|C|=285`, with every affine hyperplane slice at most 109.

## 2. Fresh source / current-literature / prior-art check, dated 2026-09-17

Fresh web queries this run included

- `"AG(7,3)" cap set 285 2026`,
- `"AG(7,3)" 285-cap`,
- `"AG(7,3)" 286-cap`,
- `"The cap set problem: Up to dimension 7" Thackeray 2026`,
- `Henry Robert Thackeray cap set dimension 7 University Pretoria 2026`,
- `"congruent-mod-3 projective dual flat" Thackeray`,
- and Bose--Burton / projective blocking-set searches while checking the finite-geometry interpretation.

The primary 2022 source still says the problem is solved through dimension 6, proves every 110-cap 6-flat is a 112-cap minus two points, and proves only nonexistence of a 289-cap in dimension 7. The BCC 2022 abstract likewise states dimension 7 is open with upper bound 288. Thackeray's current University of Pretoria publication page still lists the 2022 dimension-7 preprint and no later cap-set resolution; the surfaced later Thackeray work is in number theory. I found no accessible later primary source determining `c_{7,3}`. This is bounded negative evidence, **not** a novelty or worldwide-openness certificate.

A prior-art qualification matters for the new route below. Thackeray's 2021 *The cap set problem and standard diagrams* has a section explicitly titled **“The congruent-mod-3 projective dual flat.”** Therefore the first-order fact that congruence classes of hyperplane counts live on a projective dual flat is not represented here as new; it is part of the known standard-diagram toolkit. The new internal step in this run is to retain the **second moment modulo 3** as a quadratic form on that dual flat, classify its possible value distributions, and combine that with the exact global third/fourth incidence moments. Publication novelty of that refinement is **UNVERIFIED**.

The newest visible R17 report is still `OPEN / PARTIAL` on the binary Chvatal--Sankoff constant, so there is no neighboring closure package for an R15 audit. No P26 or distinct OTHER-track closure audits exist for I0124 because I0124 is not closed.

## 3. Starting branch and exact one-direction data

Assume for contradiction/reduction that

\[
C\subset\mathbf F_3^7,\qquad |C|=285,
\]

is a cap and that every affine hyperplane has at most 109 cap points. For every nonzero linear functional `u`, write

\[
n_j(u)=|\{x\in C:u(x)=j\}|,\qquad j\in\mathbf F_3.
\]

The three numbers sum to 285. After sorting they form one of the 169 integer types

\[
67\le a\le b\le c\le109,\qquad a+b+c=285.
\]

As in the preceding exact report, centering at 95 gives the exact global directional moments

\[
D_2:=\sum_K\sum_{j=0}^2(n_j(K)-95)^2=180690,
\]

\[
D_3:=\sum_K\sum_{j=0}^2(n_j(K)-95)^3=-2502870,
\]

where the sums are over the 1093 projective hyperplane directions.

Classify a direction by its three slice-count residues modulo 3:

- `A`: `(0,0,0)`;
- `B`: `(1,1,1)`;
- `C`: `(2,2,2)`;
- `D`: `{0,1,2}`.

Among the 169 possible no-110 types there are respectively 21, 24, 19, and 105 types in `A,B,C,D`.

## 4. #15 — break symmetry: the first moment forces either 0 or exactly 729 D-directions

Put

\[
s:=\sum_{x\in C}x\in\mathbf F_3^7.
\]

For every nonzero `u`,

\[
u(s)=\sum_{x\in C}u(x)=n_1(u)+2n_2(u)=n_1(u)-n_2(u)\pmod3.
\]

Because `n_0+n_1+n_2=285=0 mod 3`, we have:

- if `u(s)=0`, then `n_0,n_1,n_2` have the same residue modulo 3, so the direction is in `A,B`, or `C`;
- if `u(s) != 0`, then the three residues are necessarily `{0,1,2}`, so the direction is `D`.

Thus if `s=0` there are no `D` directions. If `s!=0`, the non-D directions are exactly the projective hyperplane

\[
H=\mathbf P(s^\perp)\cong PG(5,3),
\]

which has 364 points, while its complement has

\[
1093-364=\boxed{729}
\]

points. Hence

\[
\boxed{\#D\in\{0,729\}.}
\tag{4.1}
\]

As noted above, the projective-flat aspect of this congruence mechanism belongs to the known Thackeray standard-diagram framework. It is used here as the entry point, not claimed as a new result.

This already destroys the **specific** formal one-variable MacWilliams witness from the preceding R15 run: that formal histogram had category counts

\[
(A,B,C,D)=(3,152,800,138),
\]

and therefore cannot be the direction histogram of any actual cap. This does **not** prove that every ordinary-MacWilliams-feasible histogram is unrealizable; it proves that the previous exact witness was too coarse in precisely the way the stuck report predicted.

## 5. #21 — the second moment is a quadratic form on the dual flat

Define the symmetric moment matrix over `F_3`

\[
M:=\sum_{x\in C}xx^{\mathsf T}
\]

and the quadratic form

\[
q(u):=u^{\mathsf T}Mu=\sum_{x\in C}(u(x))^2\in\mathbf F_3.
\]

For `u in H=s^perp`, the three slice counts have one common residue `r`. Therefore

\[
q(u)=n_1(u)+n_2(u)=2r=-r\pmod3.
\]

Consequently, on the projective points of `H`,

\[
A\Longleftrightarrow q=0,
\qquad
B\Longleftrightarrow q=2,
\qquad
C\Longleftrightarrow q=1.
\tag{5.1}
\]

So the numbers of `A,B,C` directions are not arbitrary histogram variables: they are the projective value counts of one quadratic form.

Every quadratic form over `F_3` diagonalizes. For rank `r` on an `m`-dimensional vector space, the usual finite-field quadratic Gauss-sum count gives, for even `r`,

\[
N_0=3^{m-1}+2\varepsilon 3^{m-r/2-1},\qquad
N_1=N_2=3^{m-1}-\varepsilon 3^{m-r/2-1},
\]

and for odd `r`, `N_0=3^{m-1}` while `N_1,N_2` differ by the standard quadratic-character term. Dividing the nonzero vector counts by two gives the projective counts. The exact checker independently enumerates the two diagonal discriminant representatives at every rank, so no floating-point classification is being used.

If `s=0`, `q` is a form on all seven dual dimensions and the possible `(A,B,C)` projective counts are

`(121,486,486), (283,405,405), (337,378,378), (364,0,729), (364,243,486), (364,324,405), (364,351,378), (364,378,351), (364,405,324), (364,486,243), (364,729,0), (391,351,351), (445,324,324), (607,243,243), (1093,0,0)`.

If `s!=0`, `q|_H` is a form on six vector dimensions and the possible counts are

`(40,162,162), (94,135,135), (112,126,126), (121,0,243), (121,81,162), (121,108,135), (121,135,108), (121,162,81), (121,243,0), (130,117,117), (148,108,108), (202,81,81), (364,0,0)`.

## 6. #30 — two exact local inequalities leave only one quadratic-form type

For a sorted direction type `t=(a,b,c)`, put

\[
q_2(t)=\sum_{z\in\{a,b,c\}}(z-95)^2,
\qquad
q_3(t)=\sum_{z\in\{a,b,c\}}(z-95)^3.
\]

Exact enumeration of the 169 finite types proves both pointwise inequalities

\[
\boxed{
q_3(t)\ge
-\frac{27}{2}q_2(t)
+75\,1_A(t)-588\,1_B(t)+27\,1_D(t)
}
\tag{6.1}
\]

and

\[
\boxed{
q_3(t)\ge
-\frac{183}{13}q_2(t)
+\frac{1020}{13}1_A(t)
+\frac{1176}{13}1_B(t)
+\frac{366}{13}1_D(t).
}
\tag{6.2}
\]

There is no `C` term in either display. Multiplying through by 2 or 13 makes these exact integer inequalities. The checker verifies every one of the 169 cases and records all equality types.

Sum (6.1)--(6.2) over all directions, insert `D_2=180690` and `D_3=-2502870`, and test the finite quadratic-form count lists from Section 5. Every seven-dimensional (`s=0`) possibility is contradicted. Among the six-dimensional (`s!=0`) possibilities, **exactly one survives**:

\[
\boxed{(\#A,\#B,\#C,\#D)=(40,162,162,729).}
\tag{6.3}
\]

The nearest excluded six-dimensional alternative is still separated by a strictly positive exact rational gap (`51786/13` in the checker), so this is not a numerical-boundary artifact.

The triple `(40,162,162)` is the rank-two anisotropic quadratic form in six dimensions. Equivalently,

\[
\boxed{s\ne0,\qquad \operatorname{rank}(q|_{s^\perp})=2,}
\tag{6.4}
\]

and its radical has vector dimension four. The 40 `A` directions are exactly the projectivization `PG(3,3)` of that radical.

This is the main structural theorem of the run. It keeps information that both the scalar moment relaxation and the ordinary one-variable MacWilliams enumerator discarded.

## 7. The forced quadratic type collapses the midpoint-energy corridor

For one direction put

\[
s_4(t)=\sum_{z\in\{a,b,c\}}{z\choose4}.
\]

Using the now-forced category counts (6.3), exact enumeration of the same 169 types proves the following two pointwise supporting inequalities.

Lower support:

\[
\begin{aligned}
s_4(t)\ge {}&
\frac{582598290}{61}
+\frac{12977}{6}q_2(t)
+\frac{4475}{366}q_3(t)\\
&-\frac{2457}{61}1_A(t)
-\frac{9555}{61}1_C(t)
-\frac{20369}{183}1_D(t).
\end{aligned}
\tag{7.1}
\]

Upper support:

\[
\begin{aligned}
s_4(t)\le {}&
\frac{47752832}{5}
+\frac{131873}{60}q_2(t)
+\frac{883}{60}q_3(t)\\
&-\frac{52}{5}1_A(t)
+\frac{343}{5}1_C(t)
+\frac{263}{6}1_D(t).
\end{aligned}
\tag{7.2}
\]

Again these are finite exact rational inequalities; the checker verifies all 169 slacks using Python `Fraction` only.

For an exterior point `m`, let `r_m` be the number of unordered cap-point pairs with midpoint `m`, and retain

\[
Q(C)=\sum_{m\notin C}{r_m\choose2}.
\]

The previously proved four-subset identity is

\[
\sum_K{h_K\choose4}=40{285\choose4}+81Q(C).
\tag{7.3}
\]

Summing (7.1)--(7.2), inserting `(A,B,C,D)=(40,162,162,729)` and the exact `D_2,D_3`, then using (7.3), gives the **rational** bounds

\[
\frac{25061253}{61}
\le Q(C)\le
\frac{36982181}{90}.
\]

Since `Q(C)` is an integer,

\[
\boxed{410841\le Q(C)\le410913.}
\tag{7.4}
\]

The preceding run had only

\[
410508\le Q(C)\le411179,
\]

so the admissible integer corridor shrinks from width 671 to width 72.

Using the exact defect identity from the preceding run,

\[
Q(C)-410508
=
\sum_{m\notin C}{r_m-21\choose2},
\tag{7.5}
\]

we now have a defect at most 405. Therefore

\[
\boxed{r_m\le49\quad\text{for every exterior midpoint }m,}
\tag{7.6}
\]

because `r_m>=50` would contribute `C(29,2)=406` by itself. Also every midpoint with `r_m notin {21,22}` contributes at least one to (7.5), so at least

\[
1902-405=\boxed{1497}
\]

of the 1902 exterior points have midpoint multiplicity exactly 21 or 22.

The old bounds were `r_m<=58` and at least 1231 such near-uniform midpoints. This is a genuine strengthening, not a fresh certificate for an unchanged statement.

## 8. What this does and does not solve

The exact source value remains unknown. This run does **not** prove `c_{7,3}<=284`; the rigorous source interval remains

\[
236\le c_{7,3}\le285.
\]

What it does prove is that the hardest surviving no-110 branch is far more rigid than the previous ordinary MacWilliams witness suggested. Any such 285-cap must simultaneously satisfy:

1. a nonzero translation-invariant first moment `s`;
2. exactly 729 residue-mixed (`D`) hyperplane directions;
3. on the 364-direction projective hyperplane `s^perp`, a rank-two anisotropic quadratic second-moment form with a 4-dimensional radical;
4. exact category counts `(40,162,162,729)`;
5. midpoint energy only in `[410841,410913]`;
6. every midpoint multiplicity at most 49;
7. at least 1497/1902 exterior midpoints of multiplicity 21 or 22.

The preceding formal MacWilliams witness is excluded by item 2, but ordinary one-variable MacWilliams feasibility as a whole is **not** declared impossible. A future closure must still use compatibility/realizability information beyond a single weight histogram.

The most promising next object is now the 4-dimensional radical of `q|_{s^perp}`. After a linear normalization, its 40 projective directions form a `PG(3,3)` inside the dual. Studying the 81 primal cosets of its common 3-dimensional annihilator turns the next stage into a much smaller quotient/tomography problem. That is a genuinely new scale relative to the prior 1093-direction histogram, and it is the route I would hand off if the six-run rotation fires before closure.

## 9. Exact finite certificate

Only after the structural route was derived did I build the finite checker. It uses integer arithmetic and `Fraction` only; it does not use floating-point optimization in the archived proof core. It verifies:

- all 169 no-110 direction types and their `A/B/C/D` categories;
- both pointwise `q_3` supports (6.1)--(6.2);
- all canonical quadratic-form value-count patterns in vector dimensions 6 and 7 by direct enumeration of diagonal representatives;
- that the unique surviving pattern is `(40,162,162,729)` and corresponds to rank two with 4-dimensional radical;
- that the old formal MacWilliams histogram has impossible `D=138`;
- both exact fourth-moment supports (7.1)--(7.2), including all equality types;
- the exact rational and integer midpoint-energy corridor;
- the consequences `r_m<=49` and at least 1497 midpoint multiplicities in `{21,22}`.

Artifacts:

- `artifacts/R15/20260917_1822Z_i0124_quadratic_pencil_exact.py` @ `f82fc31f1aaf19491badc1c15eb556b3f1315070`;
- `artifacts/R15/20260917_1822Z_i0124_quadratic_pencil_exact.out` @ `a411425badc224172e75626e751c3fb6a84fafbc`.

The executed output begins

`PASS R15 I0124 exact quadratic-pencil / midpoint certificate`.

This is an R15 self-check, not an independent audit.

## 10. Method accounting

**#15 BREAK THE SYMMETRY ON PURPOSE — success.** The first-moment vector is forced nonzero, so one may normalize `s` and work on the distinguished dual hyperplane `s^perp`; the second-moment form there is forced to the rank-two anisotropic orbit.

**#21 ASK WHO ELSE HAS THIS SHAPE — success with a prior-art correction.** The first-order congruent-mod-3 dual-flat mechanism is explicitly part of Thackeray's 2021 standard-diagram framework, so it is treated as known. Keeping the next moment produces a finite quadratic-form classification over `F_3`, connecting the cap problem to classical finite quadratic forms rather than inventing a new scalar moment.

**#30 ONE SCALE / ONE DIRECTION AT A TIME — success.** The local 169-type inequalities and the dimension-6/7 quadratic-form value tables completely determine the residue-category orbit before any global 99463-pencil CSP is attempted. The previous stuck report's proposed pencil attack therefore simplifies substantially: the first global layer is now algebraically fixed.

## 11. Fixed metric / rotation status

The canonical fixed metric remains

`H_288 = largest H proved such that every hypothetical 288-cap has a 6-flat slice of size at least H`.

It was already equal to 112, the absolute six-dimensional maximum, so it remains

`112 -> 112`.

This is the fifth consecutive fixed-metric no-movement run, hence the unchanged count is `4 -> 5`. The operating contract says a **CLOSABLE** target rotates after six unchanged runs. Since this frozen metric is saturated and cannot exceed 112, the next R15 invocation gets at most one final research pass: if it does not close the source or otherwise trigger a controlling operational change, it must write the six-run I0124 handoff and rotate rather than silently redefining the metric.

Reserved next moves, different from this run's triple:

- **#8 GO THE OTHER WAY AND DISCRETIZE:** pass to the 81 cosets of the 3-dimensional annihilator of the forced radical;
- **#14 FIND THE GROUP ACTING:** use the stabilizer of the normalized rank-two anisotropic form to quotient the remaining configurations;
- **#25 COUNT THE SAME THING TWICE:** connect the 81-fiber tomography to the midpoint-energy interval `[410841,410913]`.

## 12. Model / scheduler control and P26 authorization boundary

The exposed scheduler surface still offers title/prompt, schedule/start, timing mode, and enabled state, but no writable model-family selector, no reasoning-effort selector, no authenticated completed-run model telemetry, and no guaranteed one-hour execution field. Therefore GPT-6 / maximum remains a prompt request only on this surface. This report is correctly labeled GPT-5.6 Sol / UNVERIFIED.

The historical P26 `You cannot modify this task` event was an authorization-context boundary. Repository reconciliation records that another authorized context later succeeded in updating P26. The legitimate remedies remain the owning authorized context, an ownership/admin change where supported, or platform support—not task duplication or a permission bypass. This worker is explicitly prohibited from scheduler and permission changes, so none was attempted.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  source: "I0124 / Henry Robert Thackeray (2022), The cap set problem: Up to dimension 7, arXiv:2206.09804"
  source_target: "determine c_{7,3}, the maximum cap size in AG(7,3)"
  fixed_metric: "H_288 = certified forced affine-6-flat slice size in every hypothetical 288-cap"
  metric_before: 112
  metric_after: 112
  movement: "no fixed-metric movement; substantial source-branch structural movement"
  unchanged_count_before: 4
  unchanged_count_after: 5
  status: "PARTIAL / ACTIVE / STUCK-RECOVERY-1 EXECUTED"
  source_interval_before: "236 <= c_{7,3} <= 285"
  source_interval_after: "236 <= c_{7,3} <= 285"
  tried_moves: [15, 21, 30]
  new_exact_result:
    branch: "hypothetical 285-cap with every hyperplane slice <=109"
    first_moment: "s=sum C is nonzero; D-directions are exactly PG(6,3)\\PG(s^perp), hence #D=729"
    second_moment: "q(u)=sum_x (u.x)^2 on s^perp has rank 2 anisotropic type with 4-dimensional radical"
    category_counts: "A=40, B=162, C=162, D=729"
    midpoint_energy_before: "410508 <= Q <= 411179"
    midpoint_energy_after: "410841 <= Q <= 410913"
    midpoint_consequences:
      - "every r_m <=49"
      - "at least 1497 of 1902 exterior centers have r_m in {21,22}"
    prior_formal_witness: "excluded because its D-count was 138, whereas an actual cap has D-count 0 or 729"
  prior_art_qualification: "Thackeray 2021 already contains a congruent-mod-3 projective dual flat mechanism; novelty of the second-moment quadratic refinement and resulting numeric corridor is UNVERIFIED"
  remaining_obligation: "rule out or construct a 285-cap; the no-110 branch now reduces to realizability compatible with the forced rank-two quadratic dual geometry and narrow midpoint corridor"
  next_moves: [8, 14, 25]
  next_run_rotation_rule: "if no closure/controlling change, fixed metric necessarily reaches six unchanged runs and I0124 must be handed off/rotated"
  evidence:
    - "operations/claims/I0124.md"
    - "runs/R15/20260917_1655Z_i0124_stuck1_f36a9c.md"
    - "runs/R15/20260917_1607Z_i0124_code_midpoint_e35.md"
    - "artifacts/R15/20260917_1822Z_i0124_quadratic_pencil_exact.py @ f82fc31f1aaf19491badc1c15eb556b3f1315070"
    - "artifacts/R15/20260917_1822Z_i0124_quadratic_pencil_exact.out @ a411425badc224172e75626e751c3fb6a84fafbc"
    - "Thackeray 2022 arXiv:2206.09804"
    - "Thackeray 2021, Discrete Mathematics 344(11), 112558"
  audit_ids: []
  predecessor_i0076:
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    metric: "2/4"
    problem_7_5_excluded: true
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  model_selector_available: false
  reasoning_selector_available: false
  authenticated_runtime_model_telemetry: false
  guaranteed_duration_control: false
```

No email, Gmail, Drive, public posting, purchase, permission change, scheduler change, shared-root edit, peer-file edit, or numerical cap/path sample was used as verification in this run.
