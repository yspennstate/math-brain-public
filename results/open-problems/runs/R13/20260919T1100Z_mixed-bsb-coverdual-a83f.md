Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED** — this was not authenticated GPT-6 maximum. **FIXED METRIC MOVED:** `B_R13(86): 45509/6250 = 7.28144 -> 728143/100000 = 7.28143`, exact decrease `1/100000`; methods actually used: **#23 DO WHAT THE PROPOSER DID NOT EXPECT, #22 READ THE FAILURES, NOT THE SUCCESSES, #26 HUNT THE SPORADIC CASE.**

# R13 — Boolean Komlós: mixed-density / small-ball / projective-cover probes, then an exact prefactor tightening

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: R13  
Lane: **HARD OUTSIDE**

## 1. Continuity and source status

I continued from the newest immutable R13 report

`runs/R13/20260919T1001Z_p165-tilted-4f2d.md`

at creation commit

`d1f30c3e8f3f865bcfdb59d9a3e196b005f2a534`.

Before doing new research I re-read the required repository state: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md` and `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R13 report, and current neighboring discrepancy work including the R02 pair-lift obstruction. The Boolean Komlós target remains assigned to R13; no posted/exclusion/lifecycle change supersedes it.

Fresh dated source checks also confirm the qualitative source status remains **KNOWN in current 2026 preprint literature**, not OPEN:

- Guo--Fang--Lu, arXiv:2609.11189, submitted 2026-09-10, prove the genuine real-sign dimension-free bound `3 sqrt(2 pi)` by directional total variation;
- Karingula--Lovett, ECCC TR26-188, 2026-09-17, give an independent elementary real-sign bound `36`;
- Akbas--Sra, arXiv:2609.20785, submitted 2026-09-17, prove Boolean small-ball inequalities and recover Komlós;
- Bansal--Jiang, arXiv:2508.03961v2, remains the earlier `~O((log n)^(1/4))` comparison source.

Thus R13 is only a **finite-dimensional quantitative sharpening track**. I make no claim to solving the already-resolved qualitative conjecture.

The tracked quantity entering this run was the complete universal envelope `B_R13(n)`, with

`B_R13(86)=45509/6250=7.28144`,

and same-dimension lower obstruction

`K_86^* >= 2259253/1000000 = 2.259253`.

The immediately preceding Section-B triple was `#7/#15/#30`; this run does not repeat it.

## 2. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: try to beat the homogeneous density by heterogeneity

The preceding report proved a rigorous reduction for permutation-symmetrized mixed cosine-power densities. If the coordinate exponents are `p_1,...,p_D>1`, permutation symmetrization gives the directional-TV upper bound

\[
V_u(\bar\rho)
\le
\frac{\sqrt{\pi/2}}{C}\,
\frac1{D!}\sum_\sigma
\mathbb E\sqrt{\sum_i u_i^2\frac{p_{\sigma(i)}^2}{S_{\sigma(i)}}},
\qquad S_j\sim\chi^2_{p_j+1}.
\]

The right side is symmetric and concave in the weights `u_i^2`, so its worst direction is the balanced one. This converts the heterogeneous problem to a scalar mixed inverse-gamma transform:

\[
C_{\rm mix}
=
3\sqrt{\frac\pi2}
\,\mathbb E\sqrt{\frac1D\sum_{j=1}^D\frac{p_j^2}{S_j}}.
\tag{2.1}
\]

Instead of assuming the best density should be homogeneous, I explicitly tried the opposite: split the coordinates between nearby exponents around the finite-`D` homogeneous optimum and ask whether the increased Jensen defect can outweigh the mean-score penalty.

Exploratory numerical scouting of two-exponent mixtures at `D=139` did **not** locate a mixture beating the homogeneous neighborhood near `p=1.65`; small mean-preserving exponent perturbations moved the numerical objective in the wrong direction. This scouting is intentionally **not** promoted to a theorem, finite claim, or metric update: there is no exact certificate for the heterogeneous search and no artifact was manufactured merely to certify a negative numerical screen.

The useful conclusion is structural. Heterogeneity has now been reduced to a clean one-dimensional transform question; the directional obstacle is gone. A future successful mixed-density route would need a genuine nonlocal exponent distribution, not another small perturbation of the homogeneous optimum.

**Outcome #23:** substantive failure; no metric claim.

## 3. Method #22 — READ THE FAILURES: why the new Boolean-small-ball theorem does not yet yield a numerical finite-`n` branch

I read the constant dependencies in Akbas--Sra's new Boolean small-ball paper rather than treating the words “recovers Komlós” as an explicit finite constant.

Their Theorem 1.1 is stated with universal constants `nu_0`, `q_1`, and `C_1`. In their warm-up variance--Frobenius criterion, the explicit displayed choices are still in terms of earlier universal constants `eta` and `C_R`; the full theorem then introduces `a_*` and `b_*` from Proposition 3.8. Corollary 4.1 obtains Komlós by choosing a universal `K` large enough in terms of these constants, but the paper as presently posted does not instantiate those inputs numerically at a level that can be compared directly with `7.28144`.

This pinpoints the exact failure of the obvious transfer: the result is quantitatively explicit **up to upstream universal constants**, not yet an off-the-shelf decimal theorem for this R13 metric. To turn it into a source-matching branch one would have to chase `eta,C_R,a_*,b_*` through the Gaussian reciprocal estimate and the DTV ingredient, or replace those ingredients by independently explicit constants. Until that is done, inserting an arbitrary numerical `K` would be false precision.

**Outcome #22:** no metric movement; the missing obligation is an explicit upstream constant chain, not another application lemma.

## 4. Method #26 — HUNT THE SPORADIC CASE: projective full-alignment covers and an exact minimax reduction

The six-column lower construction suggested searching for a different sporadic projective cover rather than optimizing its existing support pattern. There is a useful exact reduction here.

Fix supports `S_1,...,S_R subset [6]`. A full-alignment row on support `S_r` with common target row mass `q` can be written

\[
|a_{rj}|=q\alpha_{rj},\qquad
\alpha_{rj}\ge0,\qquad
\sum_{j\in S_r}\alpha_{rj}=1.
\]

For a selected family of projective alignment cylinders that covers all Boolean sign classes, the only remaining feasibility issue is the column-energy load

\[
L_j=\sum_{r:j\in S_r}\alpha_{rj}^2.
\]

Define

\[
z(S_1,\ldots,S_R)
:=
\inf_{\alpha}
\max_{1\le j\le6} L_j.
\tag{4.1}
\]

Then the best common row mass permitted by this fixed support family is

\[
q_{\max}=z(S_1,\ldots,S_R)^{-1/2}.
\tag{4.2}
\]

### Exact minimax identity

The continuous weight optimization has the dual formula

\[
\boxed{
z(S_1,\ldots,S_R)
=
\max_{\lambda\in\Delta_6}
\sum_{r=1}^R
\left(\sum_{j\in S_r}\frac1{\lambda_j}\right)^{-1}}
\tag{4.3}
\]

with the natural limiting convention on the boundary of the simplex.

Proof. Introduce an epigraph variable `z` and multipliers `lambda_j>=0` for the six constraints `L_j<=z`. Minimization in `z` forces `sum_j lambda_j=1`. For a fixed row support `S`, the remaining rowwise problem is

\[
\inf_{\alpha_j\ge0,\;\sum_{j\in S}\alpha_j=1}
\sum_{j\in S}\lambda_j\alpha_j^2.
\]

By Cauchy--Schwarz,

\[
1
=\left(\sum_{j\in S}\alpha_j\right)^2
\le
\left(\sum_{j\in S}\lambda_j\alpha_j^2\right)
\left(\sum_{j\in S}\lambda_j^{-1}\right),
\]

and equality is attained by `alpha_j proportional to 1/lambda_j` whenever the relevant `lambda_j` are positive. Summing the rowwise minima gives the right side of (4.3). The primal is a finite convex program with a strict epigraph feasible point, so strong duality applies; boundary cases follow by continuity. QED.

This is the useful new route reduction: instead of jointly optimizing all row amplitudes for every candidate projective cover, one only needs a finite cylinder-selection search plus a five-dimensional concave dual problem.

I used this reduction to scout exact-partition and covering patterns in the 32 projective sign classes. The search repeatedly returned the already-known six-row mixed support type as the strongest pattern encountered near the current `K_6` obstruction. I did **not** complete an exact global dual certificate over all candidate covers in this run, so I do **not** claim optimality of that pattern and I do not report an uncertified enumeration count as a theorem. This is precisely where the sporadic-cover route stops.

**Outcome #26:** a rigorous minimax reduction, but no new finite obstruction and no source-metric movement from the cover search itself.

## 5. The final 10 percent: exact arithmetic tightening of the existing `p=33/20`, `D=139` theorem

Only after the three new-method attacks above failed to move the metric did I spend the bookkeeping portion of the run on the already-certified `p=33/20` theorem.

The predecessor exact checker and report prove

\[
\delta
:=1-\mathbb E\sqrt{X_{139}}
>0.05374576758247757\ldots .
\]

I import only the weaker rational consequence

\[
\delta>\frac{53745767}{10^9}.
\tag{5.1}
\]

For `p=33/20`, the deterministic prefactor satisfies

\[
B_p^2
=
\left(\frac{3p\sqrt{\pi/2}}{\sqrt{p-1}}\right)^2
=rac{9801\pi}{520}.
\]

The predecessor used the coarse rational upper bound `B_p<7.695`. Reusing the same classical inequality

\[
\pi<\frac{355}{113},
\]

exact rational arithmetic gives the sharper bound

\[
\boxed{B_p<\frac{7694998}{10^6}=7.694998},
\]

because

\[
\left(\frac{7694998}{10^6}\right)^2
>
\frac{9801}{520}\frac{355}{113}.
\]

Combining this with (5.1),

\[
C_{33/20,139}
<
\frac{7694998}{10^6}
\left(1-\frac{53745767}{10^9}\right)
=
7.281424430426534\ldots
<
\boxed{\frac{728143}{100000}=7.28143}.
\tag{5.2}
\]

This is a genuine exact improvement, but it is deliberately classified as the final arithmetic/checking portion of the run rather than the research route.

## 6. Row pruning and the moved source metric

Set

\[
h=\frac{728143}{100000}=7.28143.
\]

For an arbitrary real `m x 86` matrix with unit-Euclidean columns, call row `r_i` active when

\[
\|r_i\|_2>\frac{h}{\sqrt{86}}.
\]

Since `sum_i ||r_i||_2^2<=86` and the exact checker proves

\[
139<\frac{86^2}{h^2}<140,
\]

there are at most `139` active rows. Apply (5.2) on those active coordinates; every inactive row is at most `h` by Cauchy--Schwarz. Therefore

\[
\boxed{K_{86}^*\le\frac{728143}{100000}=7.28143}.
\tag{6.1}
\]

The fixed tracked value moves by

\[
\frac{45509}{6250}-\frac{728143}{100000}
=oxed{\frac1{100000}}.
\]

## 7. Complete fixed upper envelope

Define the sharpened all-`n` branch

\[
\boxed{
L_{33/20}^{\rm tight}(n)
:=
\max\left\{
\frac{728143}{100000},\frac{n}{\sqrt{140}}
\right\}.}
\tag{7.1}
\]

It pointwise dominates the immediately preceding branch

\[
L_{33/20}(n)=
\max\left\{
\frac{45509}{6250},\frac n{\sqrt{140}}
\right\}.
\]

No other certified branch is changed or discarded. Let `G_0,H,J,L_-,L_2,L_3,L_4,L_5,L_LT` have **exactly** the definitions, constants, logarithmic/exponential factors, ceilings/infima, zero conventions and parameter restrictions pinned in the immutable predecessor metric chain culminating at

`runs/R13/20260919T0334Z_tilted-binomial-c7a2.md`

and inherited unchanged by the 08:33 and 10:01 reports. With

\[
T_5=
\frac{2\sqrt2+3\sqrt3+2\sqrt{51+3\sqrt6}}{13},
\]

the complete current envelope is

\[
\boxed{
B_{R13}(n)=
\begin{cases}
1,&n=1,\\[1mm]
\sqrt2,&n=2,\\[1mm]
(\sqrt{11}+\sqrt2)/3,&n=3,\\[1mm]
\sqrt3,&n=4,\\[1mm]
\min\{\sqrt{3n/4},T_5\sqrt{\lceil n/5\rceil},G_0(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{\rm LT}(n),L_{33/20}^{\rm tight}(n)\},&5\le n\le85,\\[2mm]
\min\{G_0(n),H(n),J(n),L_-(n),L_2(n),L_3(n),L_4(n),L_5(n),L_{\rm LT}(n),L_{33/20}^{\rm tight}(n)\},&n\ge86.
\end{cases}}
\tag{7.2}
\]

Equivalently, exactly and without asymptotic shorthand,

\[
B_{R13}^{\rm new}(n)
=
\min\{B_{R13}^{1001}(n),L_{33/20}^{\rm tight}(n)\},
\]

where `B_R13^1001` is the complete function in the predecessor report at commit `d1f30c3e8f3f865bcfdb59d9a3e196b005f2a534`. Thus every historical dimension/domain restriction remains in force.

## 8. Lower obstruction and current same-dimension interval

No lower obstruction moved in this run. In particular the retained balanced-tree certificate remains

\[
\boxed{K_{86}^*\ge\frac{2259253}{10^6}=2.259253}.
\]

Hence the current certified same-dimension interval is

\[
\boxed{2.259253\le K_{86}^*\le7.28143}.
\tag{8.1}
\]

The exact `K_5`, algebraic `K_6`, older `K_11,K_12` floors, Kunisky comparison, and the propagated balanced-tree lower staircase are unchanged.

## 9. Exact checker and archived execution

The new exact arithmetic checker is

`artifacts/R13/20260919T1100Z_constant-tightening-a83f_checker.py`

creation commit

`b1b2cd842e5e4d7e54fe928813c239146f344fcf`,

read back at that exact commit.

The executed output is

`artifacts/R13/20260919T1100Z_constant-tightening-a83f.out`

creation commit

`8ee36fe7b64bb1fb5a0cc1d5ad63ee672377081b`,

also read back at creation. It records

```text
R13_CONSTANT_TIGHTENING_EXACT_PASS
delta_floor = 0.053745767
base_up = 7.694998
C_upper = 7.281424430426534
h = 7.28143
row_ratio = 139.49657507496704
improvement = 1e-05
```

The imported defect floor is not a new unverified decimal: the immediately preceding exact checker/output and written proof certify the stronger value `delta>0.05374576758247757...`; this run deliberately weakens it to the rational `53745767/10^9` before doing the new arithmetic.

## 10. What failed, exactly, and what should be tried next

The three research attacks did not themselves move the metric:

1. heterogeneous mixed exponents: directional reduction succeeds, but local heterogeneous scouting did not beat the homogeneous finite-`D` transform;
2. Boolean small-ball: the current theorem's universal constants are not numerically instantiated through the upstream constant chain, so no honest `7.28...` comparison is available yet;
3. sporadic six-column covers: the weight optimization is now exactly dualized by (4.3), but a global exact finite cover certificate has not been completed.

The next primary route should therefore **not** be another decimal retuning of `p`. The highest-value continuation is the projective-cover minimax program (4.3), because it separates the discrete cover choice from the continuous weights and gives a clean exact target. A second route is to chase the Akbas--Sra upstream constants all the way to a numerical value. The mixed-density route should be revisited only with a genuinely nonlocal exponent law rather than a two-point perturbation around `p=1.65`.

Because the fixed metric moved, the stuck counter resets to `0`.

## 11. Model-control / P26 truth

The scheduler/runtime surface still exposes no binding model-family selector, no reasoning-effort selector, and no authenticated completed-run model/effort receipt. Therefore `GPT-6 / maximum` remains prompt-only on this surface; this run is correctly labeled **GPT-5.6 Sol / UNVERIFIED**. Making the request enforceable would require an owner-authorized product/workspace/API/admin surface that persists model/reasoning fields into execution routing and returns authenticated per-run telemetry, or platform support.

The historical P26 `You cannot modify this task` result remains an authorization-context issue; repository state records a later successful P26 update from an authorized context. The lawful workaround is the owning/authorized surface or platform support, not duplication or permission bypass.

No scheduler, permission, workflow, email, Drive, purchase, or public-posting action was made.

## 12. Status and structured `ledger_delta`

Status: **SOURCE QUALITATIVE STATUS KNOWN / R13 QUANTITATIVE STATUS PARTIAL / FIXED UPPER METRIC MOVED / full written arithmetic proof / exact self-check PASS / outside audits 0/2 / novelty UNVERIFIED / fixed-upper stagnation count reset to 0**.

```yaml
ledger_delta:
  worker: R13
  lane: HARD_OUTSIDE
  canonical_intake_alias: I0091
  source_target: real Boolean Komlos signing
  source_qualitative_status: KNOWN_IN_2026_PREPRINT_LITERATURE
  quantitative_track_status: PARTIAL
  fixed_metric: complete universal upper envelope B_R13(n)
  tracked_dimension: 86
  fixed_metric_before: 45509/6250
  fixed_metric_after: 728143/100000
  exact_decrease: 1/100000
  fixed_upper_unchanged_count_before: 0
  fixed_upper_unchanged_count_after: 0
  new_branch: L_33_20_tight(n)=max(728143/100000,n/sqrt(140))
  finite_lower_obstruction_K86: 2259253/1000000
  current_K86_interval: [2259253/1000000,728143/100000]
  methods: [23,22,26]
  method_23: SUBSTANTIVE_FAILURE_NO_METRIC_CLAIM
  method_22: UPSTREAM_CONSTANT_CHAIN_BLOCKER_IDENTIFIED
  method_26: EXACT_MINIMAX_REDUCTION_NO_GLOBAL_FINITE_CERTIFICATE
  imported_exact_predecessor_delta_floor: 53745767/1000000000
  self_check: PASS
  outside_audits: 0/2
  novelty: UNVERIFIED
  stuck_protocol: NOT_TRIGGERED_METRIC_MOVED
```
