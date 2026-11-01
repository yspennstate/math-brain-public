Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **no movement in the frozen metric `L <= Delta_2(Q)`: `0 -> 0`; methods B3, B15, B28.** GPT-6/maximum was requested in prompt text, but this runtime does not expose authenticated GPT-6/maximum reasoning telemetry, so I do not claim otherwise.

# HARD7-03 — recovery-route theorem: atomic-minimum central-shape saturation, and the logarithmic fast-run barrier

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source residual remains OPEN_BY_BOUNDED_SEARCH.** This execution carries out the optimizer-pinning / endpoint-cost route chosen in Section-I recovery 1. It proves a source-relevant zero-tilt theorem for the exact lazy-LPP representation and then attacks the missing linear endpoint-cost statement from the positive-velocity side. It does **not** prove a positive plateau width and does not close Seppäläinen Problem 4.

Canonical target: `D0025`, Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4. Exclusive claim: `operations/claims/D0025.md`, owner `HARD7-03`.

Frozen case:
\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]
with hydrodynamic flux `f_{2,Q}` and
\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]
The fixed metric is a rigorous lower bound `L <= Delta_2(Q)`.

## 1. Continuity, repository state, ownership, and source refresh

I resumed the admitted target and the newest checkpoint rather than restarting admission. Before mathematical work I read/recovered:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/D0025.md`;
- newest own checkpoint `runs/hard7_2026-09-18/HARD7-03/20260918T2323Z__d0025-stuck-lazy-lpp-pinning-route.md` and the three preceding HARD7-03 reports;
- newest neighboring HARD7-02 report `runs/hard7_2026-09-18/HARD7-02/2026-09-18T23-12-00Z__rank-marked-pwit-full-local-limit.md`;
- newest neighboring HARD7-04 report `runs/hard7_2026-09-18/HARD7-04/2026-09-18T23-37Z__p0157_finite_population_hub_lln.md`;
- the D-intake/source records for `disordered_asep_open_1999::problem_4`, including prior attempt `D0025-A001`.

Repository-wide search still identifies `D0025` as exclusively owned by HARD7-03. I found no release, duplicate canonical owner, posted equivalent, or source-closing repository result.

The source question remains Seppäläinen's explicit Problem 4 question whether the disordered `K`-exclusion flux has a flat segment around `rho=K/2`. The `K=1` iid site-disorder plateau is known and excluded from new credit; the frozen `K=2` binary site-rate case remains the active residual.

### Bounded current-literature check, 2026-09-19 UTC

I refreshed the exact source/current-status queries rather than treating the prior negative search as permanent. Sources checked included:

1. T. Seppäläinen, 1999, arXiv `math/9906194`, Problem 4;
2. A. Sly, *Note on the flux for TASEP with general disorder*, arXiv `1609.06589`, the known `K=1` plateau baseline;
3. Bahadoran--Guiol--Ravishankar--Saada, *Euler hydrodynamics for attractive particle systems in random environment*, AIHP 50 (2014), broad hydrodynamics but not an explicit general-`K` plateau theorem;
4. Bakhtin--Khanin--Mészáros--Voltz, *Last passage percolation in a product-type random environment*, arXiv `2310.08379` (revised 2025), a nearby lazy-walk pinning/corner model with materially different separable bounded product disorder.

Dated searches used the source title/Problem 4 aliases together with `disordered K-exclusion plateau`, `site disorder K-exclusion flux`, `general K TASEP site disorder plateau`, and `columnar lazy last passage percolation exponential row disorder`. I found no theorem closing the exact `K>=2` source residual. This is a bounded negative search, **not** a proof of worldwide openness or novelty.

The Bakhtin--Khanin--Mészáros--Voltz proof was read specifically for its failure/success mechanism. Their corner proof decomposes lazy paths into loops and exploits discrepancy in a product-type potential. Our weights are conditionally independent exponentials whose *rate* is the static row variable; the temporal randomness is not a bounded separable sign factor, so their discrepancy estimate cannot simply be quoted. The transferable idea is the loop/essential-displacement decomposition, not their theorem.

## 2. Frozen metric and recovery state

Before this run,
\[
L=0.
\]
After this run,
\[
\boxed{L:0\longrightarrow0.}
\]
**No movement.** The source-level blocker remains
\[
\exists\delta>0:\qquad [-1-\delta,-1+\delta]\subseteq\partial g_{2,Q}(0),
\tag{2.1}
\]
equivalently a positive-width flat interval of `f_{2,Q}` around density one.

The previous execution was Section-I recovery 1 and chose the optimizer-pinning / linear endpoint-tilt-cost route, with next methods B3/B15/B28. This run executes that route. Because the frozen metric remains unchanged, the **next** HARD7-03 invocation must be Section-I stuck recovery 2 (thinking protocol), not another incremental lemma/checker run.

## 3. Exact lazy-LPP notation inherited from the previous checkpoint

The prior report established the exact coordinate change from Seppäläinen's `K=2` admissible paths to lazy nearest-neighbor paths. I restate only the object needed here.

Let the static row rates `(alpha_y)_{y in Z}` be iid with law `Q`. Let `(xi_{t,y})` be iid `Exp(1)`, independent of the row environment, and set
\[
W_{t,y}=\frac{\xi_{t,y}}{\alpha_y}.
\tag{3.1}
\]
Conditional on `(alpha_y)`, these are independent exponentials of rate `alpha_y`. For a lazy path `pi=(y_0,...,y_n)` with
\[
y_0=0,\qquad y_{t+1}-y_t\in\{-1,0,1\},
\]
define its passage value using the convention
\[
A_Q(\pi)=\sum_{t=1}^n W_{t,y_t}.
\]
Let
\[
T_Q(n,z)=\max\{A_Q(\pi): y_n=z\}.
\tag{3.2}
\]
The zero-velocity shape is
\[
G_Q(0)=\lim_{n\to\infty}\frac{T_Q(n,0)}n
\tag{3.3}
\]
whenever the limit exists. The source shape theorem supplies existence in the admitted model; the argument below in fact pins the limit directly in the atomic-minimum case.

For homogeneous rate `r`, write `T_r`, `G_r(0)`.

No finite sampled path is being used as proof of a continuous/asymptotic statement here.

## 4. B3 — prove something stronger: atomic-minimum central-shape saturation

The previous pinning route suggested looking for a favorable slow row or cluster. For the **central value**, one can do substantially more than a heuristic localization statement.

### Theorem 4.1 (self-checked route theorem; not source closure)

Let `Q` be any iid row-rate law supported on `[r,infinity)` with
\[
r>0,\qquad p:=Q(\{r\})>0.
\]
For the lazy LPP (3.1)--(3.3),
\[
\boxed{G_Q(0)=G_r(0).}
\tag{4.1}
\]
In words: an atom at the minimal rate makes the quenched **zero-velocity** growth rate saturate the completely homogeneous all-slowest-row value, even if most rows are faster.

In particular, for the frozen binary law,
\[
\boxed{G_{\frac12\delta_{1/2}+\frac12\delta_1}(0)=G_{1/2}(0).}
\tag{4.2}
\]

This theorem fixes the central value but does not supply any nonzero one-sided slope and therefore does not move `L`.

### Proof

#### Step 1: monotone coupling gives the upper bound

Use the same iid `xi_{t,y}~Exp(1)` for the disordered and homogeneous fields and define
\[
W_{t,y}=\frac{\xi_{t,y}}{\alpha_y},\qquad Z_{t,y}=\frac{\xi_{t,y}}r.
\]
Since `alpha_y>=r` almost surely,
\[
W_{t,y}\le Z_{t,y}\qquad\text{for every }(t,y)
\tag{4.3}
\]
under this coupling. Therefore every path has no larger disordered passage value than homogeneous rate-`r` passage value, so pathwise
\[
T_Q(n,0)\le T_r(n,0).
\]
Hence
\[
\limsup_{n\to\infty}\frac{T_Q(n,0)}n\le G_r(0).
\tag{4.4}
\]

#### Step 2: finite homogeneous strips and their shape constants

For `M>=0`, let `T_r^{(M)}(n,0)` be the homogeneous rate-`r` maximum restricted to paths contained in the strip `[-M,M]` and ending at zero. Concatenation at zero gives the stationary superadditive process
\[
T_r^{(M)}(m+n,0)\ge T_r^{(M)}(m,0)+T_{r,\,m}^{(M)}(n,0),
\tag{4.5}
\]
where the second term uses the time-shifted iid environment. Standard superadditive ergodic theory therefore gives an almost-sure and `L^1` limit
\[
\lambda_M:=\lim_{n\to\infty}\frac{T_r^{(M)}(n,0)}n
=\sup_{n\ge1}\frac{\mathbb E T_r^{(M)}(n,0)}n.
\tag{4.6}
\]
Integrability is elementary: there are at most `3^n` lazy paths and every fixed-path sum is Gamma(`n`, rate `r`), so an exponential Chernoff bound plus a union bound gives a finite linear upper tail for the maximum.

The strip constants increase with `M` and exhaust the full homogeneous central shape:
\[
\lambda_M\uparrow G_r(0).
\tag{4.7}
\]
Indeed, every `n`-step lazy path from zero stays inside `[-n,n]`, so
\[
T_r^{(M)}(n,0)=T_r(n,0)\qquad(M\ge n).
\tag{4.8}
\]
Consequently for every fixed `n` and every `M>=n`,
\[
\lambda_M\ge \frac{\mathbb E T_r(n,0)}n.
\]
Taking first `M->infinity` and then the supremum over `n`, and applying the same superadditive formula to the full-space point-to-point process, gives
\[
\sup_M\lambda_M\ge \sup_n\frac{\mathbb E T_r(n,0)}n=G_r(0).
\]
The reverse inequality is immediate from strip restriction, proving (4.7).

#### Step 3: the iid row environment contains every fixed all-slow strip

Fix `M`. Partition the integer line into disjoint blocks of length `2M+1`. Each block consists entirely of minimum-rate rows with probability
\[
p^{2M+1}>0,
\]
and these block events are independent. Hence almost surely infinitely many such blocks occur. Choose one and denote its center by `a_M`; for each fixed `M`, `|a_M|<infinity` almost surely.

On the block `[a_M-M,a_M+M]`, the field `(W_{t,y})` is exactly iid `Exp(r)` in time and space.

#### Step 4: travel to a slow strip, spend macroscopic time there, return

For `n>2|a_M|`, consider the admissible path that

1. moves from row `0` to row `a_M` in `|a_M|` steps;
2. during the next `n-2|a_M|` steps uses an optimal path from `a_M` to `a_M` constrained to the all-slow strip `[a_M-M,a_M+M]`;
3. returns from `a_M` to `0` in `|a_M|` steps.

All passage weights are nonnegative, so discarding the travel contribution yields
\[
T_Q(n,0)\ge \widetilde T_{r,M}\bigl(n-2|a_M|\bigr),
\tag{4.9}
\]
where the right side is the strip point-to-point last-passage value in a fixed time translate of an iid homogeneous rate-`r` strip. Time-stationarity and ergodicity imply
\[
\lim_{n\to\infty}\frac{\widetilde T_{r,M}(n-2|a_M|)}n=\lambda_M
\qquad\text{almost surely}.
\tag{4.10}
\]
Therefore
\[
\liminf_{n\to\infty}\frac{T_Q(n,0)}n\ge \lambda_M.
\tag{4.11}
\]
This holds simultaneously for every integer `M` on a probability-one event. Letting `M->infinity` and using (4.7),
\[
\liminf_{n\to\infty}\frac{T_Q(n,0)}n\ge G_r(0).
\tag{4.12}
\]
Together with (4.4), this proves (4.1). `□`

### Why this is useful and why it is not enough

The theorem rigorously confirms a genuine rare-region pinning mechanism at **exactly zero tilt**: the optimizer can exploit an arbitrarily wide minimum-rate island at only sublinear asymptotic travel cost, because the island's location is fixed once its width is fixed and the `n->infinity` limit comes first.

But (4.1) is only a value statement. A plateau requires first-order separation away from zero, for example a bound of the form
\[
G_Q(0)-G_Q(v)\ge c|v|+o(|v|),\qquad c>0.
\tag{4.13}
\]
The theorem does not imply (4.13). This is why the frozen source metric remains `L=0`.

I have not found this exact atomic-minimum saturation statement in the bounded prior-art search. The mechanism is a natural rare-region/columnar-pinning argument and may be folklore; **no novelty claim is made without a dedicated prior-art audit.**

## 5. B15 — break the symmetry: positive endpoint velocity exposes a false linear-toll proof

Now force an endpoint `m>0`, so a path must eventually cross each intermediate row. This is the most tempting place to convert the density of fast rows into a linear cost.

Use the Sly-style monotone coupling from the previous checkpoint, with homogeneous minimum rate `r=1/2`. On a fast row (`alpha=1`), one can realize
\[
Z=W+U,
\]
with
\[
W\sim\operatorname{Exp}(1),\qquad
U=B E,
\qquad B\sim\operatorname{Ber}(1/2),\qquad E\sim\operatorname{Exp}(1/2),
\tag{5.1}
\]
independently in the standard representation. Hence
\[
\mathbb P(U=0)=\frac12,
\qquad \mathbb E U=1.
\tag{5.2}
\]

A **fixed-time** crossing of a fast row has positive mean homogeneous-slow bonus, but the last-passage optimizer is offline and chooses the crossing time after seeing the field. For one required fast row and `h` candidate crossing times,
\[
\mathbb P(\text{at least one zero-bonus candidate})=1-2^{-h}.
\tag{5.3}
\]
Therefore the argument
\[
\text{“about }m/2\text{ fast rows”}+\text{“mean bonus }1\text{ per fast row”}
\]
cannot be applied to the optimizing path. Selection destroys the fixed-time expectation. Any proof of (4.13) must control **opportunity cost** or the number/geometry of candidate crossing times, not merely count fast rows.

This is a precise counterexample to a tempting strengthening of the Sly coupling route. I am not claiming that the optimizer pays zero total cost, only that a deterministic or naive mean positive toll per required fast row is unavailable.

## 6. B28 — replace “all paths” by “typical environment”: the logarithmic fast-run scale is exactly critical

The binary row environment gives a second exact diagnostic. Let
\[
F_y=\mathbf 1\{\alpha_y=1\},
\]
so `(F_y)` are iid Bernoulli(`1/2`). Let `R_m` be the longest consecutive run of fast rows among `1,...,m`.

### Lemma 6.1
For every `eps>0`,
\[
\frac{R_m}{\log_2 m}\xrightarrow[m\to\infty]{\mathbb P}1.
\tag{6.1}
\]

### Proof
For `k_+=(1+eps)log_2 m`, a union bound over possible starting points gives
\[
\mathbb P(R_m\ge k_+)\le m2^{-k_+}\le m^{-\varepsilon}.
\]
For `k_-=(1-eps)log_2 m`, partition `[1,m]` into disjoint blocks of length `ceil(k_-)`. The probability a given block is all fast is at least a constant multiple of `m^{-(1-eps)}`, while the number of disjoint blocks is of order `m/log m`. Hence the probability none is all fast is at most
\[
\exp\{-c m^{\varepsilon}/\log m\}\to0.
\]
This proves (6.1). `□`

Now combine this environment scale with the exact zero-bonus probability (5.2). If a fast run has length `k`, then a **straight monotone traversal** over `k` consecutive time steps has zero coupling bonus at every visited fast site with probability
\[
2^{-k}.
\tag{6.2}
\]
Among `h` disjoint candidate start times, the probability that none of these straight zero-bonus windows occurs is
\[
(1-2^{-k})^h.
\tag{6.3}
\]
At the typical extremal run scale `k≈log_2 m`, and on a time horizon `h` of order `n` with `m≈vn`,
\[
h2^{-k}\asymp \frac{n}{m}\asymp \frac1v.
\tag{6.4}
\]
Thus the longest environmental fast runs are **exactly at the critical scale** where perfect zero-bonus monotone crossing windows occur with neither overwhelming nor vanishing first-moment frequency. A shorter run has many such windows; a substantially longer run would suppress them, but such longer runs are themselves atypical.

This rules out another superficially plausible proof strategy: “the longest fast run is a hard barrier, so it automatically forces a linear tilt cost.” At its natural logarithmic length, the zero-bonus availability and environment rarity balance one another.

The conclusion is constructive rather than nihilistic. A successful endpoint-cost proof must use more than the indicator `U=0`. It must combine at least one of:

1. the **magnitude** of positive bonuses when a perfect zero window is unavailable;
2. the **opportunity cost** of waiting for a favorable crossing time, measured against the central strip growth rate from Theorem 4.1;
3. a loop/essential-displacement decomposition that forces every net row advance to consume time that cannot simultaneously be used in the pinned slow strip;
4. a multi-row passage estimate controlling adaptive, nonmonotone attempts rather than only straight windows.

This is the closest source-valid analogue I found to the loop-discrepancy step in Bakhtin--Khanin--Mészáros--Voltz.

## 7. What changed mathematically in this run

Before this run, the pinning route was only a proposed qualitative mechanism: prove that a zero-velocity optimizer localizes on favorable slow rows and that tilt causes linear loss.

After this run:

- the **zero-tilt value** is rigorously identified for every iid row law with an atom at its minimum rate: `G_Q(0)=G_r(0)`;
- the result is obtained by a genuine rare-region argument, not simulation and not a finite-size inference;
- two tempting ways to turn this into a corner are sharply excluded:
  - summing the positive mean coupling bonus over required fast rows is invalid under optimizer time selection;
  - the longest fast run alone sits at a critical `log_2 m` scale where zero-bonus crossing-window frequency balances run rarity;
- the missing proof obligation is now narrower: quantify the **opportunity cost / loop mass lost per net displacement** in the exponential row-rate model.

The source metric nevertheless remains unchanged because no positive one-sided slope has been proved.

## 8. Next mandatory Section-I recovery

Because `L` is still zero after execution of recovery route 1, the next invocation is **Section-I stuck recovery 2**. It must be a thinking run and must not simply append another capacity or local-stationarity lemma.

The exact blocker remains
\[
\boxed{\exists c>0,\ v_0>0:\quad G_Q(0)-G_Q(v)\ge c|v|+o(|v|)\quad(0<|v|<v_0),}
\tag{8.1}
\]
translated back through the source convex duality to positive width in `partial g(0)`.

The recovery-2 comparison target should be a loop/essential-displacement decomposition rather than a direct row toll. The next Section-B triple is reserved as
\[
\boxed{\text{B4 / B20 / B25}.}
\]
Interpretation:

- **B4**: prove a weaker but complete finite-strip / one-fast-block passage-cost theorem;
- **B20**: identify exactly why the natural max-plus crossing algorithm loses control under offline time selection;
- **B25**: count passage time two ways, as loop mass plus essential net-displacement mass, to isolate a candidate deterministic linear deficit.

If recovery 2 also leaves the same source obligation unchanged, the hard-track rotation limit is close: a third stuck episode requires a handoff and a fresh admissible external target rather than indefinite work on D0025.

## 9. Verification / artifacts / capability honesty

No finite exhaustive claim was made in this run, so I did not manufacture an exact-arithmetic checker merely to produce a receipt. The substantive new claim is theorem-sized and its full proof is on this page. Lemma 6.1 is also proved on the page. Both remain **self-checks** pending independent review; neither counts as a closure audit.

The scheduler capability statement is unchanged and was checked against the controlling policy: the exposed automation surface offers scheduling/prompt/enablement controls but no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed run duration. GPT-6 maximum is therefore only a text request. A real change requires a platform/API surface that exposes and authenticates model/reasoning selection; a repository edit cannot supply it.

The policy also records historical native modification denials (`You cannot modify this task`) for some IDs, including P26 in one context, with later success for P26 from another authorized context. The lawful workaround for any still-denied task is the authorized owner/workspace interface or platform support, not cloning, bypassing, or creating a replacement schedule. I modified no other task or schedule in this run.

## 10. Ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  status: PARTIAL
  metric: "rigorous lower bound L <= Delta_2(Q)"
  before: 0
  after: 0
  movement: false
  methods: [3, 15, 28]
  source_status: OPEN_BY_BOUNDED_SEARCH
  new_self_checked_results:
    - "Atomic-minimum central-shape saturation: for iid row rates supported on [r,infinity) with Q({r})>0, the K=2 lazy-LPP zero-velocity shape satisfies G_Q(0)=G_r(0)."
    - "For frozen binary disorder, the longest consecutive fast-row run R_m satisfies R_m/log_2(m) -> 1 in probability; at this scale the perfect zero-bonus straight-crossing opportunity count is critical rather than exponentially absent."
  exact_blocker: "prove a strictly positive first-order endpoint-tilt cost, hence positive subgradient width at zero"
  section_I_state: "recovery route 1 executed; next run must be stuck recovery 2"
  next_methods: [4, 20, 25]
  artifacts_added: none
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```

No closure, proof audit, public posting, email, Drive write, scheduler mutation, or shared-ledger mutation is claimed.
