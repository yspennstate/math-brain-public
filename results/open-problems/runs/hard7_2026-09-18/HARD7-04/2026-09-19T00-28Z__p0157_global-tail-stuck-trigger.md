Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-04 frozen metric no movement, `Q_n=sigma_n^2/(d_max delta_n) -> sigma_n^2/(d_max delta_n)`; methods B15 / B20 / B22.**

# HARD7-04 bounded research iteration — P0157 global-tail barrier and Section-I trigger

Date: **2026-09-19 UTC**. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source residual remains OPEN by the current primary source plus bounded current-literature review.** This is the third consecutive P0157 run with no movement in the frozen admission metric. Therefore the Section-I stagnation trigger is now reached: the **next** HARD7-04 invocation must be a STUCK1 thinking/recovery run rather than another incremental lemma/checker run. This report does not relabel source-route progress as movement of the frozen metric.

## 1. Continuity, ownership, repository state

I resumed the exact admitted claim `operations/claims/P0157.md`, owned exclusively by HARD7-04. I did not restart admission, take I0049, or change the source statement.

Before the mathematical work I read/recovered the governing files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the newest own checkpoint `runs/hard7_2026-09-18/HARD7-04/2026-09-18T23-37Z__p0157_finite_population_hub_lln.md` and the earlier P0157 checkpoints;
- the newest neighboring HARD7-03 report `runs/hard7_2026-09-18/HARD7-03/20260919T0019Z__d0025-atomic-minimum-central-shape-saturation.md`;
- the newest neighboring HARD7-05 report `runs/hard7_2026-09-18/HARD7-05/2026-09-18T2341Z_theta_third_exact.md`;
- the P0157 intake/ranking records and a fresh repository-wide collision search.

The claim search still returns `operations/claims/P0157.md` with owner HARD7-04; other tracks explicitly recognize this ownership. I found no release, duplicate owner, posted equivalent, or canonical-claim collision.

The previous checkpoint proved, at graph level, that for a maximal-degree vertex `v_max`,

\[
\frac{|C(v_{\max})|}{d_{\max}/\delta_n}\xrightarrow{\mathbb P}1
\qquad\text{if }d_{\max}\delta_n\to\infty,
\tag{1.1}
\]

under the finite-third-moment barely-subcritical assumptions used by this track. Thus in the strong hub-dominant regime it already gives the source-relevant lower bound

\[
L_1\ge (1-o_{\mathbb P}(1))H_n,
\qquad H_n:=\frac{d_{\max}}{\delta_n}.
\tag{1.2}
\]

The remaining hub-side obligation is global: exclude a different component that is substantially larger.

## 2. Primary source and current-status refresh

I re-read the primary source itself:

Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF page index 254:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`.

The page calls this an “interesting open problem” for subcritical configuration models with finite third-moment degrees. It recalls Janson's strictly subcritical law `d_max/(1-nu)(1+o_P(1))`, contrasts it with the Erdos--Renyi barely-subcritical order `epsilon_n^{-2} log(n epsilon_n^3)`, and says this suggests a phase transition inside the subcritical regime. I visually checked this PDF page in this run. As before, I use the positive convention

\[
\delta_n:=1-\nu_n>0
\]

rather than the source prose's negative `epsilon_n=nu_n-1`.

I also re-read the closest solved configuration-model upper-bound paper:

Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, Electronic Journal of Probability 28 (2023), DOI `10.1214/23-EJP921`, arXiv `2111.11780`.

Their Theorem 1.3 assumes, in their notation,

\[
Q=\frac1m\sum_i d_i(d_i-2)<0,\qquad
R=\frac1m\sum_i d_i(d_i-2)^2,
\]

plus Assumption 1.1 and `Delta |Q|=o(R)`, and proves the Erdos--Renyi-type upper scale

\[
\frac{2R}{Q^2}\log\!\frac{|Q|^3n}{R^2}.
\]

Their more general Theorem 1.5 uses the moment generating function of the size-biased exploration increment and assumes `Delta<=n^(1/6)` in addition to Assumption 1.1. Assumption 1.1(v) is a fourth-moment restriction, and Remark 1.2 explicitly calls it the most restrictive assumption and asks how much fourth-moment control is really needed. These hypotheses are not the full finite-third-moment source regime.

Fresh dated searches for the exact barely-subcritical finite-third-moment configuration-model crossover recovered Coulson--Perarnau and adjacent models but no theorem closing the exact 4 August 2026 source residual. This is bounded negative evidence only, **not** a proof of worldwide openness or novelty.

## 3. Frozen metric — before/after

The admission metric remains

\[
Q_n^{\mathrm{hub}}
:=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

Before:

\[
Q_n^{\mathrm{hub}}=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

After:

\[
Q_n^{\mathrm{hub}}=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

**No movement.** This is consecutive no-movement count **3** after the exact determination of the metric. I do not replace it by an easier quantity. The rest of this report records genuine route work and why the remaining global argument is different from the rooted law already proved.

For compact notation in the route analysis put

\[
N_n:=n\delta_n^3\to\infty,
\qquad
b_n:=d_{\max}\delta_n,
\qquad
\frac{H_n}{E_n}=\frac{b_n}{\log N_n},
\tag{3.1}
\]

where `E_n=delta_n^{-2} log N_n`. The strong hub side is `b_n/log N_n -> infinity`.

## 4. B15 — break the symmetry: hostile multiplicity of near-maximal hubs

The most obvious way for the local theorem (1.1) to fail globally is to put many vertices near `d_max`: perhaps two or more large hubs coalesce, or the maximum over many nominally `H_n`-scale rooted components acquires an extreme-value boost.

Instead of assuming a unique hub, I deliberately allowed the worst multiplicity compatible with the source third-moment budget. Let

\[
M_{3,n}:=\frac1n\sum_{v=1}^n d_v^3=O(1)
\]

and for `x>0` define the degree shell tail

\[
S_n(x):=\{v:d_v\delta_n\ge x\}.
\]

Two deterministic Markov bounds are

\[
|S_n(x)|
\le \frac{\delta_n^3}{x^3}\sum_vd_v^3
\le C\frac{N_n}{x^3},
\tag{4.1}
\]

and

\[
\sum_{v\in S_n(x)}d_v
\le \frac{\delta_n^2}{x^2}\sum_vd_v^3
\le C\frac{n\delta_n^2}{x^2}.
\tag{4.2}
\]

Since the total half-edge count is asymptotic to a positive constant times `n`, the half-edge mass fraction of `S_n(x)` is `O(delta_n^2/x^2)`.

Now take `x=eta b_n` for fixed `eta>0`. Then

\[
|S_n(\eta b_n)|\le C\frac{N_n}{b_n^3},
\qquad
\frac{\sum_{v\in S_n(\eta b_n)}d_v}{\ell_n}
=O\!\left(\frac{1}{d_{\max}^2}\right).
\tag{4.3}
\]

On an exploration lasting `O(H_n)=O(b_n/delta_n^2)` pairings, the crude expected number of partners landing in another comparable-hub half-edge set is therefore only

\[
O\!\left(\frac{b_n}{\delta_n^2}\right)
O\!\left(\frac{\delta_n^2}{b_n^2}\right)
=O(b_n^{-1}).
\tag{4.4}
\]

The previous rooted tightness theorem makes this calculation relevant for the already-controlled maximal-root exploration. Moreover,

\[
\log\bigl(2+|S_n(\eta b_n)|\bigr)
\le \log N_n+O(1)=o(b_n)
\tag{4.5}
\]

on the strong hub side.

**Outcome of B15:** the naive counterexample “there are so many comparable hubs that they merge or their maximum automatically beats the maximal-root scale” does not survive the source third-moment budget in the strong hub regime. The entropy of comparable hubs is at most `log N_n`, while the natural rooted deviation parameter is `b_n >> log N_n`; direct comparable-hub collisions have `O(1/b_n)` scale along an `O(H_n)` exploration.

This is **not** yet a global upper theorem. Equations (4.1)--(4.5) do not control components initiated by the enormous population of low- and medium-degree vertices, and they do not supply the sharp `t^{-3/2}`/moderate-deviation prefactor responsible for replacing `log n` by `log(n delta_n^3)`.

## 5. B20 — find why the obvious global algorithm fails

The natural algorithm is: dominate every component exploration by one iid negative-drift walk, obtain an exponential survival tail, and union-bound over roots. Coulson--Perarnau make precisely this architecture sharp in their regime. Reading their proof identifies two separate failure points for the present source-wide hub regime.

### 5.1 The low-hub theorem points in the opposite direction

Here `Q=-delta_n` and, under finite-third-moment convergence, `R` stays on constant order under the usual nondegeneracy. Their Theorem 1.3 requires

\[
\Delta|Q|=d_{\max}\delta_n=o(R),
\]

so it is designed for `b_n=o(1)`, essentially the opposite side from

\[
b_n/\log N_n\to\infty.
\]

Its Taylor step uses `theta_0~|Q|/R` together with `theta_0 Delta=o(1)`, which is exactly what fails when hubs are source-relevant.

### 5.2 The general exponential tilt is contaminated by the hubs

For a root of degree `d_v`, their tilted hitting-time estimate carries the factor

\[
d_v e^{\theta_0 d_v}.
\tag{5.1}
\]

Their component-counting argument sums these factors and normalizes by

\[
\mathbb E[D_ne^{\theta_0D_n}].
\tag{5.2}
\]

This is elegant when the same tilt describes the entire degree sequence. But on the hub side `theta_0 d_max` need not be small, so (5.2) is itself exponentially sensitive to the rare vertices whose effect we are trying to separate. The one global tilt mixes two mechanisms instead of comparing them: ordinary bulk large deviations and deterministic high-degree initial mass.

The failure is therefore informative rather than merely technical. **The proof should not ask one exponential tilt to treat the bulk and the hubs symmetrically.** The source phase transition is exactly where that symmetry becomes wrong.

**Outcome of B20:** a direct transplantation of the best nearby global-tail algorithm fails at the root-weight/MGF step. This isolates a concrete repair: peel the high-degree vertices before applying the Cramer/local-limit machinery to the bulk, then reinsert the peeled roots with degree-dependent estimates.

## 6. B22 — read the failures: what the nearest solved proof has that the source does not

Coulson--Perarnau's Assumption 1.1(v) imposes the fourth-moment restriction

\[
\mathbb E[D_n^4]\le \Delta_n^{1/2},
\tag{6.1}
\]

as printed in the paper; their Remark 1.2 calls this the most restrictive condition and explicitly asks how far a fourth-moment condition is needed. In their local-limit step, the tilted increment's third absolute moment is bounded using this assumption, producing `gamma=O(Delta^{1/2})`, and the error is then killed using `Delta=o(T)`. Their Theorem 1.5 also assumes `Delta<=n^(1/6)`; the proof later notes that this degree cap is needed in Lemma 3.1 in the complementary `R=O(Delta|Q|)` case.

The source question here asks for the finite-third-moment degree setting. That gives exactly the second-moment control of the size-biased offspring needed for diffusive exploration fluctuations, but it does **not** give the uniform tilted third moment used in the Coulson--Perarnau local-limit estimate. Riordan's sharp bounded-degree result avoids this because its increments are bounded; Janson's high-degree law is strictly subcritical and does not supply the required uniform barely-subcritical global tail.

So the nearest solved proof possesses two ingredients absent in the exact source scope:

1. a single MGF that can be used before separating hubs; and
2. enough higher-moment/bounded-jump control for a quantitative tilted local limit.

**Outcome of B22:** the shortest plausible port is now specific. Use finite-third-moment uniform integrability to **truncate first, tilt second**, and account for the removed degrees separately. Merely weakening constants in the existing proof will not address the mechanism.

## 7. New route exposed by the three attacks: hub peeling + truncated tilt

I am not claiming the following programme is proved in this run. It is the concrete new route produced by B15/B20/B22.

Choose a deterministic `rho_n downarrow 0` slowly enough that

\[
y_n:=\rho_n/\delta_n\to\infty
\]

and the empirical third-moment tail above `y_n` tends to zero. Such a diagonal choice is compatible with the source's third-moment convergence. Then:

1. **Peel** vertices with `d_v>y_n`. Removing positive high-degree contributions can only make the residual exploration more subcritical.
2. On the residual sequence, a bulk tilt of size `theta=O(delta_n)` has
   \[
   \theta y_n=O(\rho_n)=o(1),
   \]
   restoring a uniform Taylor regime without asking for an exponential moment of the original degree sequence.
3. Prove a truncated local/moderate-deviation estimate at times `t~delta_n^{-2}log N_n`. The target entropy is `N_n=n delta_n^3`, not `n`.
4. Reinsert the peeled vertices by dyadic `x=d_v delta_n` shells. Equation (4.1) gives shell cardinality `O(N_n/x^3)`, exactly the counting scale that can potentially be paid for by a root-dependent survival exponent.
5. In the strong hub regime, show every shell stays below `(1+epsilon)H_n`; in the low-hub regime, let the bulk extreme scale survive. At order-one `b_n/log N_n`, optimize the two costs rather than guess a sharp switch.

The key reason this is not just another version of the previous rooted argument is that it contains a mechanism for the **global entropy factor** `N_n`, which is the missing ingredient in (1.1).

## 8. Section-I trigger record

Because the frozen metric has now failed to move for three consecutive P0157 runs, the next invocation must use the five-part Section-I thinking protocol. To prevent accidental restart, here is the exact state it must inherit.

### Blocking statement

The nearest source-matching hub-side statement not yet proved is

\[
\boxed{
\forall\varepsilon>0:\quad
\mathbb P\!\left(
L_1(\mathrm{CM}_n(\mathbf d))>(1+\varepsilon)\frac{d_{\max}}{\delta_n}
\right)\to0
}
\tag{8.1}
\]

under the finite-third-moment barely-subcritical assumptions together with

\[
\frac{d_{\max}\delta_n}{\log(n\delta_n^3)}\to\infty.
\tag{8.2}
\]

The matching lower bound is already available from (1.1).

### Routes tried and their precise obstruction

- Independent branching surrogate: gives exact mean/variance and rooted concentration, but no finite-population/global maximum control.
- Active-queue cycle analysis: removes the false birthday-collision obstruction, but only for a chosen root.
- Exact finite-population drift/Doob analysis: proves the maximal-root graph LLN, but its polynomial martingale control is far too weak to union over all possible components.
- Single global exponential tilt: nearby literature makes it sharp when `d_max delta=o(1)`, but in the hub regime the factors `e^{theta d}` are dominated by the very hubs that must be separated.
- Comparable-hub multiplicity attack from this run: third-moment counting defeats the simplest merger counterexample, but does not control the low-degree bulk extreme.

### What a successful proof must add

It must simultaneously contain:

1. a root-degree-sensitive component tail with the correct `n delta_n^3` effective entropy;
2. separation of rare high-degree jumps before exponential tilting;
3. a local/moderate-deviation estimate that uses only source-level finite third moment, not an unassumed fourth moment or exponential moment; and
4. a summation over degree shells strong enough to rule out every competitor component, not only the component of `v_max`.

### Simplest still-unproved special case

Take a bounded limiting bulk degree law and **one** exceptional vertex of degree `d_max`, with `d_max^3/n -> 0`, tune the bulk so `delta_n->0`, `n delta_n^3->infinity`, and assume (8.2). The maximal-root LLN is already proved here, but even this one-hub model still needs a self-contained global proof that the bounded-degree bulk produces no component of order `H_n`. This is the cleanest test case for the peel-then-tilt route because after removing one hub the residual increments are genuinely bounded.

### Nearest solved problem and missing ingredient

Coulson--Perarnau Theorems 1.3/1.5 are nearest. Their proof uses stochastic domination, exponential tilting, a quantitative lattice local limit, and root-weight summation. What the source-wide problem lacks is their fourth-moment/degree control and the small-`theta Delta` regime; on the hub side the MGF is contaminated by rare high degrees.

The recommended Section-I recovery choice for the next run is **port the technique from the nearest solved problem**, but only after hub peeling. A clean first test is the one-exceptional-hub special case above.

Next unused section-B moves reserved for that recovery: **B8 (discretize into degree shells), B13 (use the decreasing third-moment tail as a monovariant), B25 (count large components once by roots and once by components).**

## 9. Capability honesty

The scheduler limitation remains unchanged. The exposed automation controls provide title, prompt, schedule, timing mode and enabled state, but **no model selector, no reasoning-effort selector, no authenticated reasoning telemetry and no guaranteed run duration**. GPT-6/maximum is therefore only a prompt request. This run actually identifies as GPT-5.6 Sol; the reasoning level is UNVERIFIED. Changing the model/reasoning guarantee would require a platform/API surface exposing native selector controls or authenticated runtime metadata; a GitHub edit cannot do it.

The repository policy records historical `You cannot modify this task` responses for some scheduler IDs (including P26/P01/P03 in one context), while later authorized contexts have succeeded on some of them. The lawful workaround for any still-denied task is the correct owner/workspace context or platform support, not a duplicate schedule, permission bypass, or repository-only imitation. I did not modify, create, reactivate, or disable any schedule.

No email or Drive action was taken. No finite exhaustive claim was made, so I did not manufacture an exact checker merely to create activity.

## ledger_delta

```yaml
track: HARD7-04
canonical_claim: P0157
owner: HARD7-04
allocation: HARD_OUTSIDE
status_before: PARTIAL_OPEN
status_after: PARTIAL_OPEN_SECTION_I_TRIGGERED
metric: Q_n_normalized_hub_branching_variance
metric_before: "sigma_n^2/(d_max delta_n)"
metric_after: "sigma_n^2/(d_max delta_n)"
movement: no_movement
consecutive_no_movement_after: 3
source_scales:
  H_n: "d_max/delta_n"
  E_n: "delta_n^-2 log(n delta_n^3)"
  b_n: "d_max delta_n"
  N_n: "n delta_n^3"
method_moves: [15, 20, 22]
new_route:
  - "peel vertices above y_n=rho_n/delta_n"
  - "apply Cramer/local-limit machinery only to truncated bulk"
  - "reinsert peeled roots by dyadic x=d delta shells using |S_x|=O(N_n/x^3)"
blocking_statement: "global upper L1 <= (1+eps)d_max/delta_n whp when b_n/log N_n -> infinity"
simplest_unproved_case: "bounded bulk plus one exceptional hub"
next_run_required: "SECTION_I_STUCK1_THINKING_RECOVERY"
recommended_recovery: "port Coulson-Perarnau tail method after hub peeling"
next_methods: [8, 13, 25]
closure: false
independent_audits: []
```
