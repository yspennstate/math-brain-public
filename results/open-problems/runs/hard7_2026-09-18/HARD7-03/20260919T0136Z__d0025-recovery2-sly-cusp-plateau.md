Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-03 metric moves `L <= Delta_2(Q): 0 -> 1/16`; methods B4 / B20 / B25.**

# HARD7-03 — Section-I recovery 2: repair of the adaptive-coupling obstruction and an explicit K=2 binary-disorder plateau

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source Problem 4 remains open in its full generality.** This run began as the mandatory second Section-I recovery after the previous frozen metric remained at zero. The new-method review found that the preceding report's B15 diagnosis was wrong: choosing a crossing time after seeing the disordered weights does **not** destroy the Sly coupling bonus, because the maximizing path is measurable with respect to the disordered field while the auxiliary coupling variables remain conditionally independent. Repairing that point yields a source-valid theorem for the frozen `K=2` binary site-disorder case and moves the fixed metric.

Canonical source: Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4. Active claim: `operations/claims/D0025.md`, owner `HARD7-03`.

Frozen case:
\[
K=2,\qquad Q=\frac12\delta_{1/2}+\frac12\delta_1,
\]
and
\[
\Delta_2(Q)=\sup\{\delta\ge0:\ f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]
The tracked quantity is a rigorous lower bound `L <= Delta_2(Q)`.

## 1. Continuity, ownership, source and current-status refresh

I resumed the newest checkpoint rather than restarting the target. Before the mathematical work I re-read/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/D0025.md`;
- all five preceding HARD7-03 checkpoints, especially
  `runs/hard7_2026-09-18/HARD7-03/20260919T0019Z__d0025-atomic-minimum-central-shape-saturation.md`;
- newest neighboring HARD7-02 and HARD7-04 reports;
- the D-intake record keyed by `disordered_asep_open_1999::problem_4`.

Repository claim search still identifies `D0025` as exclusively owned by HARD7-03. No release, duplicate owner, posted equivalent, or source-closing repository result was found.

The exact source question is still Seppäläinen's question whether the disordered `K`-exclusion flux has a flat segment around `rho=K/2`. The ordinary `K=1` iid site-disorder plateau is known and excluded from new credit.

A bounded current-literature refresh dated 2026-09-19 used the exact source title/Problem 4 together with `K=2 disordered exclusion plateau`, `K-exclusion disorder flat segment flux`, `simple K-exclusion disorder`, and Sly aliases. It recovered the 1999 source, Allan Sly's `K=1` paper `arXiv:1609.06589`, the broad random-environment hydrodynamic literature, and Ayyer--Misra's distinct deformed-rate 2024 model, but no theorem closing the exact `K>=2` source residual. This is negative evidence only, not proof of worldwide novelty or openness.

The primary source and the 1999 Annals hydrodynamics paper were also rechecked for the exact duality and growth-path conventions. In the latter, the `K=2` admissible increments are `(1,0),(0,1),(2,-1)`, the growth shape is homogeneous, and the hydrodynamic flux is
\[
f_{2,Q}(\rho)=\inf_x\{\rho x+g_Q(x)\}.
\tag{1.1}
\]

## 2. Metric movement

Before:
\[
L=0.
\]

After this run:
\[
\boxed{L=\frac1{16}.}
\tag{2.1}
\]

More precisely, the on-page argument below proves the self-checked restricted theorem
\[
\boxed{
 f_{2,Q}(\rho)=f_{2,Q}(1)
 \quad\text{for every}\quad
 \rho\in\left[\frac{15}{16},\frac{17}{16}\right].
}
\tag{2.2}
\]
Therefore
\[
\boxed{\Delta_2(Q)\ge\frac1{16}.}
\tag{2.3}
\]

This is genuine movement on the frozen source metric. It does **not** close Seppäläinen Problem 4 for arbitrary `K` or arbitrary disorder. Under the owner's status rules the track therefore remains **PARTIAL**. No closure, novelty, or audit-completion claim is made.

## 3. Starting point inherited from the preceding checkpoints

The previous Section-I recovery established the exact `K=2` change of coordinates
\[
t=i+j-1,\qquad y=j,
\]
under which all three admissible source increments become unit-time lazy nearest-neighbor increments
\[
\Delta y\in\{-1,0,1\}.
\]

Write the static row rates as `alpha_y` and let `xi_{t,y}` be iid `Exp(1)`, independent of the row environment. The disordered lazy-LPP weights are
\[
W_{t,y}=\frac{\xi_{t,y}}{\alpha_y}.
\tag{3.1}
\]
Conditional on the row environment, these are independent exponentials of rate `alpha_y`.

For a lazy path from row zero to row `m` in `n` steps let
\[
T_Q(n,m)=\max_\pi\sum_{t=1}^n W_{t,\pi_t},
\tag{3.2}
\]
and denote the deterministic point-to-point shape by
\[
G_Q(v)=\lim_{n\to\infty}\frac1nT_Q(n,\lfloor vn\rfloor),
\qquad |v|\le1.
\tag{3.3}
\]

The immediately preceding report proved, with a full rare-region argument, the central saturation identity
\[
\boxed{G_Q(0)=G_r(0),\qquad r=\frac12,}
\tag{3.4}
\]
where `G_r` is the homogeneous lazy-LPP shape with all row rates equal to the minimum rate `r`.

That result is a dependency of the present proof and is not re-derived here.

## 4. B20 — find why the algorithm was said to fail: the previous B15 obstruction is false

The preceding report correctly noticed that the maximizing path chooses its crossing times after seeing the disordered weights. It then made the wrong inference that this adaptive choice destroys the fixed-time mean coupling bonus. The key sigma-field was omitted.

Let
\[
\mathcal F=\sigma\bigl((\alpha_y)_y,(W_{t,y})_{t,y}\bigr).
\tag{4.1}
\]
Choose a maximizing path `pi*` for `T_Q(n,m)` by a deterministic tie rule. Then `pi*` is `F`-measurable.

Use the standard minimum-rate coupling, coordinate by coordinate. Conditional on a row rate `a>=r`, let
\[
Z=W+U,
\tag{4.2}
\]
where
\[
W\sim\operatorname{Exp}(a),
\qquad
U=B E,
\qquad
B\sim\operatorname{Ber}(1-r/a),
\qquad
E\sim\operatorname{Exp}(r),
\tag{4.3}
\]
and `B,E` are independent of `W`. Then
\[
Z\sim\operatorname{Exp}(r)
\tag{4.4}
\]
and
\[
\mathbb E[U\mid\alpha=a]=\frac1r-\frac1a.
\tag{4.5}
\]

For the frozen binary law this is
\[
U=0\quad\text{on a slow row},\qquad
\mathbb E U=1\quad\text{on a fast row}.
\tag{4.6}
\]

The crucial point is that all auxiliary `U_{t,y}` are sampled independently of the entire disordered weight field conditional on the row environment. Hence after conditioning on `F`, an `F`-measurable choice of coordinates still leaves the corresponding `U` variables independent with their original row-dependent laws.

So the offline optimization is not an obstruction. The path may choose the *time* at which it first crosses a row using all the `W` values, but it does not get to inspect the independent `U` bonus before making that choice.

This directly repairs the false route diagnosis in the previous report.

## 5. B25 — count the same forced displacement twice

Assume first `m>0`. Every lazy nearest-neighbor path from `0` to `m` must visit each row
\[
1,2,\ldots,m.
\]
For the disordered maximizing path `pi*`, let `tau_y` be its first hitting time of row `y`. The coordinates
\[
(\tau_y,y),\qquad 1\le y\le m,
\]
are distinct and `F`-measurable.

Evaluate the homogeneous coupled field `Z=W+U` on the *same* path. Since all `U` are nonnegative,
\[
\begin{aligned}
T_r(n,m)
&\ge \sum_{t=1}^n Z_{t,\pi_t^*}\\
&=T_Q(n,m)+\sum_{t=1}^n U_{t,\pi_t^*}\\
&\ge T_Q(n,m)+\sum_{y=1}^m U_{\tau_y,y}.
\end{aligned}
\tag{5.1}
\]

This is the double count: the endpoint displacement forces one first-visit coordinate in every intermediate row, and the independent coupling assigns a bonus to those same forced coordinates.

For the binary law define
\[
N_m=\#\{1\le y\le m:\alpha_y=1\}.
\]
By the spatial law of large numbers,
\[
\frac{N_m}{m}\longrightarrow\frac12
\qquad\text{almost surely}.
\tag{5.2}
\]

Conditional on `F`, the selected bonuses at the `N_m` fast rows are iid copies of
\[
U=B E,\qquad B\sim\operatorname{Ber}(1/2),\quad
E\sim\operatorname{Exp}(1/2),
\tag{5.3}
\]
with mean one. For each fixed `eps>0`, the lower-tail Chernoff bound gives a constant `c_eps>0` such that
\[
\mathbb P\!\left(
 \sum_{\substack{1\le y\le m\\\alpha_y=1}}U_{\tau_y,y}
 \le(1-\varepsilon)N_m
 \,\middle|\,\mathcal F
\right)
\le e^{-c_\varepsilon N_m}.
\tag{5.4}
\]
This bound is valid despite the adaptive first-hit times because those times are `F`-measurable and the selected `U` coordinates are conditionally independent.

Fix `v>0` and set `m_n=floor(vn)`. On the almost-sure row-environment event from (5.2), `N_{m_n}` is linear in `n`; hence the probabilities in (5.4) are summable. Conditional Borel--Cantelli, followed by `eps downarrow 0`, gives
\[
\liminf_{n\to\infty}
\frac1n\sum_{y=1}^{m_n}U_{\tau_y,y}
\ge\frac v2
\qquad\text{almost surely}.
\tag{5.5}
\]

The same argument to the left handles `v<0`. Taking the shape limits in (5.1) yields
\[
\boxed{
G_r(v)\ge G_Q(v)+\frac12|v|,
\qquad |v|\le1.
}
\tag{5.6}
\]

For complete rigor one can first prove (5.6) for rational `v`, intersect the resulting probability-one events, and extend to the whole interval by continuity of the deterministic concave shapes.

### Why the conditional concentration is legitimate

For a fast row, the Laplace transform of the selected `U` is the same at every selected time because the time is chosen from `F`, not from the auxiliary field. In particular, for `theta>0`,
\[
\mathbb E[e^{-\theta U}]
=\frac12+\frac12\frac{1/2}{1/2+\theta},
\tag{5.7}
\]
so the usual exponential lower-tail estimate is uniform over all `F`-measurable coordinate choices. This is the precise point the prior B15 argument missed.

## 6. B4 — prove the frozen source case completely enough to move the metric

The homogeneous lazy-LPP shape `G_r` is even by row reflection and concave by concatenation/superadditivity. Consequently
\[
G_r(v)\le G_r(0).
\tag{6.1}
\]
Combine this with (5.6) and the inherited central saturation (3.4):
\[
G_Q(v)
\le G_r(v)-\frac12|v|
\le G_r(0)-\frac12|v|
=G_Q(0)-\frac12|v|.
\]
Therefore
\[
\boxed{
G_Q(0)-G_Q(v)\ge\frac12|v|.
}
\tag{6.2}
\]

This is exactly the first-order endpoint-tilt cost that the previous two recovery cycles had isolated as the blocker.

## 7. Translate the lazy cusp back to Seppäläinen's source growth function

Let `gamma_Q(x,y)` be the source two-coordinate passage shape. Under
\[
t=i+j-1,\qquad y=j,
\]
macroscopic source coordinates `(x,y)` correspond to lazy time `x+y` and lazy velocity `v=y/(x+y)`. Hence, ignoring the vanishing lattice offset `-1`,
\[
\gamma_Q(x,y)
=(x+y)\,
G_Q\!\left(\frac{y}{x+y}\right).
\tag{7.1}
\]

Seppäläinen's convex source function is the level-one boundary
\[
g_Q(s)=\inf\{x>0:\gamma_Q(x,s)\ge1\}.
\tag{7.2}
\]
Parameterize this boundary by lazy velocity `v`. Put
\[
s(v)=\frac{v}{G_Q(v)}.
\tag{7.3}
\]
Then
\[
\boxed{
g_Q(s(v))=\frac{1-v}{G_Q(v)},
\qquad
g_Q(0)=\frac1{G_Q(0)}.
}
\tag{7.4}
\]

The secant slope from zero is therefore exactly
\[
\frac{g_Q(s(v))-g_Q(0)}{s(v)}
=
\frac{G_Q(0)-G_Q(v)}{G_Q(0)v}-1.
\tag{7.5}
\]

For `v>0`, (6.2) gives
\[
\frac{g_Q(s(v))-g_Q(0)}{s(v)}
\ge -1+\frac{1}{2G_Q(0)}.
\]
For `v<0`,
\[
\frac{g_Q(s(v))-g_Q(0)}{s(v)}
\le -1-\frac{1}{2G_Q(0)}.
\]
Letting `v -> 0+` and `v -> 0-` and using convexity,
\[
g'_{Q,-}(0)
\le -1-\frac{1}{2G_Q(0)},
\qquad
g'_{Q,+}(0)
\ge -1+\frac{1}{2G_Q(0)}.
\tag{7.6}
\]
Thus
\[
\boxed{
\left[
-1-\frac{1}{2G_Q(0)},
-1+\frac{1}{2G_Q(0)}
\right]
\subseteq\partial g_Q(0).
}
\tag{7.7}
\]

Since `g_Q(0)=1/G_Q(0)`, the half-width obtained so far is
\[
\delta_0=\frac12\,g_Q(0).
\tag{7.8}
\]

## 8. An explicit numerical-free lower bound: `delta_0 >= 1/16`

It remains only to give a rigorous positive lower bound on `g_Q(0)`. This can be done self-containedly.

Let `G_1` denote homogeneous unit-rate lazy LPP. There are at most `3^n` lazy paths of length `n`. Along any fixed path the passage sum is Gamma(`n`, rate `1`). With exponential-Chernoff parameter `theta=3/4`,
\[
\mathbb P\{\Gamma(n,1)\ge4n\}
\le e^{-3n}4^n.
\tag{8.1}
\]
Therefore
\[
\mathbb P\{T_1(n,0)\ge4n\}
\le 3^n e^{-3n}4^n
=\left(\frac{12}{e^3}\right)^n.
\tag{8.2}
\]
The series is summable because
\[
e^3>1+3+\frac{3^2}{2!}+\frac{3^3}{3!}=13>12.
\tag{8.3}
\]
Borel--Cantelli gives
\[
G_1(0)\le4.
\tag{8.4}
\]

Homogeneous exponential passage times scale inversely with the rate, so
\[
G_r(0)=\frac1rG_1(0).
\]
With `r=1/2`, central saturation yields
\[
G_Q(0)=G_r(0)\le8,
\qquad
g_Q(0)=\frac1{G_Q(0)}\ge\frac18.
\tag{8.5}
\]
Hence from (7.8),
\[
\boxed{\delta_0\ge\frac1{16}.}
\tag{8.6}
\]

Finally use the source duality (1.1). If `-rho` lies in `partial g_Q(0)`, then `x=0` minimizes `rho x+g_Q(x)`, so
\[
f_{2,Q}(\rho)=g_Q(0).
\tag{8.7}
\]
Equation (7.7) together with (8.6) therefore gives
\[
f_{2,Q}(\rho)=f_{2,Q}(1)
\quad
\text{for every }
\rho\in[15/16,17/16].
\]
This proves (2.2)--(2.3).

## 9. What this does and does not establish

The new result is a full on-page argument for the **frozen `K=2` binary site-disorder case**, subject to independent checking of the source-coordinate identifications and the inherited central-saturation theorem. It is not a finite simulation and does not infer asymptotic behavior from samples.

It does **not** establish:

- the full arbitrary-`K` source problem;
- the exact plateau width or exact plateau current;
- a theorem for disorder without an atom at its minimum;
- publication novelty;
- closure under the fleet protocol.

The mechanism plainly extends at the coupling level to a `K=2` iid row law supported on `[r,infinity)` with an atom at `r`: the forced-row mean bonus becomes
\[
\mu=\frac1r-\mathbb E\frac1\alpha,
\]
and the preceding central-saturation theorem supplies the zero-velocity equality. I do **not** count that broader formulation as an additional closed result in this run; it should be audited and checked against prior art separately before promotion.

The most important correction is methodological: the earlier “offline time selection destroys the bonus” obstruction was spurious. Conditional independence is exactly strong enough to survive an optimizer chosen from the disordered field.

## 10. Exact checker and archived output

The exact finite/symbolic identities used for the explicit constant were executed and archived at

- `artifacts/hard7_2026-09-18/HARD7-03/recovery2_sly_lazy_cusp_algebra.py`;
- `artifacts/hard7_2026-09-18/HARD7-03/recovery2_sly_lazy_cusp_algebra.out`.

The checker verifies:

1. `E[1/alpha]=3/2`, `mu=1/2`;
2. the exact Laplace-transform identity `W+U ~ Exp(1/2)` on a fast row;
3. the level-set/secant algebra (7.5);
4. the Taylor certificate `e^3>13>12` used in the summable union bound;
5. `g_Q(0)>=1/8`, `Delta_2(Q)>=1/16`;
6. the interval endpoints `[15/16,17/16]`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

This checker certifies the algebraic core only. The asymptotic conditional-concentration and convex-duality proof is the written argument above and remains a **self-check** pending independent audit.

## 11. Section-I state and next route

Because the fixed metric moved from zero to `1/16`, the stagnant-run counter resets. This run is not another no-movement recovery and does not trigger rotation away from D0025.

The most useful next research directions are not another checker. A subsequent run should use a new triple, for example:

- **B5**: vary the minimum-atom law and quantify the general `K=2` half-width;
- **B21**: compare the repaired adaptive-coupling mechanism with columnar LPP / queueing results to test prior-art risk and search for a `K>2` analogue;
- **B29**: analyze the boundary where the minimum-rate atom disappears, which is exactly where the central-saturation proof fails.

The owner-required closure standard is unchanged: this restricted theorem remains PARTIAL until source scope, prior art, and the required two independent outside audits are satisfied.

## 12. Capability statement

The scheduler/runtime surface available to this run still does not expose a binding model selector, a reasoning-effort selector, authenticated maximum-reasoning telemetry, or guaranteed execution duration. GPT-6/maximum is therefore only a text request. The actual model exposed here is GPT-5.6 Sol and the reasoning level is UNVERIFIED.

The repository policy records historical native edit failures of the form `You cannot modify this task`, including P26 in one context and later success from another authorized context. For any task that remains non-editable, the compliant route is the authorized owner/account/workspace interface or platform support/ownership correction, not a duplicate schedule or permission bypass. No scheduler was modified in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  frozen_case:
    K: 2
    site_rate_law: "1/2 delta_{1/2} + 1/2 delta_1"
  metric: "rigorous certified lower bound L <= Delta_2(Q)"
  before: 0
  after: 1/16
  movement: true
  methods: [4, 20, 25]
  section_I_state: "recovery 2 found and repaired a false independence obstruction; movement resets stagnation counter"
  new_self_checked_result:
    statement: "For frozen K=2 binary iid site disorder, f_{2,Q} is constant on [15/16,17/16], hence Delta_2(Q)>=1/16."
    key_shape_bound: "G_Q(0)-G_Q(v) >= |v|/2"
    audit_status: "self-check only; no independent closure audit claimed"
  corrected_prior_statement: "Adaptive/offline crossing-time selection does not destroy the Sly coupling bonus when the path is measurable with respect to the disordered field and auxiliary U variables are conditionally independent."
  exact_artifacts:
    - artifacts/hard7_2026-09-18/HARD7-03/recovery2_sly_lazy_cusp_algebra.py
    - artifacts/hard7_2026-09-18/HARD7-03/recovery2_sly_lazy_cusp_algebra.out
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  next_methods: [5, 21, 29]
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```

No public posting, email, Drive write, shared-root mutation, independent audit, or closure claim is made.
