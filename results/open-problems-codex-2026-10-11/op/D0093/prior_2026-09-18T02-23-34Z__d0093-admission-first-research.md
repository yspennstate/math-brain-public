Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but no authenticated runtime model-family selector or reasoning-effort selector is exposed, so this was not a verified GPT-6/maximum run and I do not claim otherwise. **NO SOURCE-METRIC MOVEMENT: `beta_fast = 2 -> 2`; D0093 no-movement count `0 -> 1`; methods actually tried: B26 HUNT THE SPORADIC CASE, B18 SAY IT IN ANOTHER LANGUAGE, B25 COUNT THE SAME THING TWICE.**

# P13 — D0093 admission and first substantive research: multiscale repair route for the fast ARW cycle

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Own root: `proofnet24/P13-outside-successor`.  
Canonical claim: `operations/claims/D0093.md`.  
Source: Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), arXiv:1906.05037v2, Section 6.2, open problem immediately after Theorem 6.1 / estimate (6.3).  
Status after this run: **OPEN / PARTIAL**.

## 1. Continuity, exclusions, ownership, and why this is a new source rather than a renamed old one

The former P13 target I0051 (Aldous--Janson Open Problem 9, clade covariances) remains **RETIRED** and was not reopened. The later P13 successor P0082 (finite-WARM forest threshold) remains handed off after its six unchanged source-metric runs; none of its endpoint work was restarted.

The controlling preceding P13 report is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T01-03-25Z__successor-admission-delta-screen.md`.

That report left P13 in `CLOSABLE OUTSIDE / ADMISSION_PENDING` with no active source and successor metric `UNMEASURED`. This run advanced the intake cursor rather than recycling the previously screened Bradley/Virág cluster.

Before claiming D0093 I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the controlling owner/new-method directives, the newest P13 report, the newest relevant P14 report, the current canonical-claim surface, and the D-intake problem/attempt records. A direct fetch of `operations/claims/D0093.md` returned 404. Repository-wide exact-ID searches found the intake/catalog/prior attempt but no canonical owner or current D0093 research report.

I therefore created the claim **create-only**, as required:

`operations/claims/D0093.md`

creation commit

`f34fd075a3a4ae57a610152b79d5130b8d35a058`,

read-back blob

`d4cd8b1caaa1dd9e90e56b55b9702cba5b204176`.

The claim assigns D0093 exclusively to native P13 slot `6aa7b253b37c8191b693d8dc79298d37`. No peer claim was overwritten.

## 2. Exact source target and frozen metric

The source considers activated random walk on the cycle `Z_n`, started from i.i.d. Poisson(`zeta`) active particles, with symmetric nearest-neighbor jumps and sleep rate `lambda`. Theorem 6.1 proves two regimes. In the fast regime, for suitable source parameters (the proof chooses

\[
\zeta<\zeta'<\frac{\lambda}{1+\lambda}),
\]

there are constants `kappa,delta>0` such that, for all large `n`, the total number `T` of topplings satisfies

\[
\mathbb P\bigl(T\le \kappa n\log^2 n\bigr)\ge 1-n^{-\delta}.
\]

The open problem immediately following the theorem asks to improve this estimate **to one without the `log^2 n` term**.

The source-faithful frozen metric is therefore

\[
\boxed{
\beta_{\rm fast}:=
\inf\left\{\beta\ge0:
\exists\kappa<\infty,\delta>0,
\ \mathbb P\!\left(T\le \kappa n(\log n)^\beta\right)
\ge1-n^{-\delta}
\text{ for all large }n
\right\},
}
\]

with **the source's Poisson initial law and fast-regime domain frozen**. The source proves `beta_fast <= 2`; for campaign bookkeeping the certified frontier is recorded as

`beta_fast = 2`,

and the source asks for `beta_fast = 0`. A Bernoulli initial law, an open interval, an infinite-line odometer theorem, or a narrower parameter subcase does not move this metric unless it is upgraded back to the exact finite-cycle Poisson source statement.

This first research run does not achieve that upgrade, so

\[
\boxed{\beta_{\rm fast}:2\to2.}
\]

## 3. Current literature check, dated 18 September 2026

I checked the original Rolla survey statement, the original Basu--Ganguly--Hoffman--Richey cycle paper behind Theorem 6.1, later ARW papers surfaced by exact-title/keyword searches, and especially the new 2025 paper

Sam Johnson and Leonardo T. Rolla/Richey [repository search metadata should be read with the paper itself], *The odometer in subcritical activated random walk*, arXiv:2510.05514v2 (2025).

The material point is this: the old D0093 intake attempt said that no useful odometer tail bound was known in the fast/subcritical regime. The 2025 paper changes that route. It proves a stretched-exponential upper tail of order `exp(-c sqrt(t))` for the site odometer on `Z` under subcritical i.i.d. Bernoulli initial data, hence finite mean; its discussion says the proof should extend nearly verbatim to other i.i.d. light-tailed initial laws, while heavy tails can destroy finite expectation.

That is **not** a source-matching solution of D0093. The source has a periodic finite cycle and i.i.d. Poisson data. Passing from the infinite line to a cycle is not monotone in the useful direction because periodic wrapping removes an escape boundary, and the Poisson extension is suggested rather than stated as the theorem checked here.

Fresh bounded web queries included variants of:

- `Rolla activated random walk log^2 n open problem cycle total topplings`;
- `activated random walk cycle total topplings linear O(n) fast phase`;
- `subcritical activated random walk odometer tail 2025 2026`;
- `Johnson Richey odometer subcritical activated random walk`.

They recovered the source, the original cycle theorem, the 2025 infinite-line odometer-tail result, and newer ARW work on other regimes, but no later primary theorem giving the exact Poisson finite-cycle `O(n)` high-probability bound requested by D0093. This is **bounded negative evidence only**, not proof of worldwide openness or a novelty certificate.

## 4. B26 — attack the negation first: do Poisson sporadic piles force a logarithmic loss?

The first research question was whether the source's hoped-for `O(n)` statement could actually be false because rare Poisson piles force superlinear work. The most obvious candidate is the maximum initial pile, which is unbounded with `n`.

That mechanism does **not** by itself force any logarithmic factor in the aggregate.

### Lemma P13-D0093-POISSON-POLYNOMIAL-BUDGET-01

Let `X_1,...,X_n` be i.i.d. Poisson(`zeta`) with fixed `zeta>0`. For every fixed `q>0` and every `delta>0`, there is `C=C(q,delta,zeta)<infinity` such that

\[
\boxed{
\mathbb P\left(
\sum_{i=1}^n(1+X_i)^q>Cn
\right)
\le n^{-\delta}
}
\]

for all sufficiently large `n`.

#### Proof

Put `Y_i=(1+X_i)^q`. A Poisson random variable has moments of every positive order, so `Y_i` also has moments of every order. Choose an integer `p>=2` with `p/2>delta`. Set `mu=E Y_1` and `W_i=Y_i-mu`.

Rosenthal's inequality gives a constant `C_p` such that

\[
\mathbb E\left|\sum_{i=1}^nW_i\right|^p
\le
C_p\left(
\sum_{i=1}^n\mathbb E|W_i|^p
+\left(\sum_{i=1}^n\mathbb E W_i^2\right)^{p/2}
\right)
=O(n^{p/2}).
\]

Take `C=2mu+1`. If `sum_i Y_i>Cn`, then for all large `n`,

\[
\left|\sum_{i=1}^nW_i\right|>(C-\mu)n\ge c n
\]

for a fixed `c>0`. Markov's inequality therefore yields

\[
\mathbb P\left(\sum_iY_i>Cn\right)
\le
\frac{O(n^{p/2})}{(cn)^p}
=O(n^{-p/2})
\le n^{-\delta}
\]

for all sufficiently large `n`. `square`

### What this rules out

Any prospective lower-bound obstruction whose extra stabilization cost at site `i` is bounded by a fixed polynomial in the initial Poisson pile cannot force a superlinear total cost with polynomially high probability. In particular, even a quadratic local cost budget remains `O(n)` with arbitrarily high polynomial probability after summing over the cycle.

The analogous empty-gap obstruction also fails at the most naive level: the occupied-site indicators are i.i.d. Bernoulli with parameter `1-e^{-zeta}`, so the longest initially empty run is only logarithmic, and one isolated diffusive `O(log n)` gap costs only `O(log^2 n)=o(n)`. I did not promote this heuristic into a source theorem because repeated interactions among gaps are exactly what the dynamics must control.

**Counterexample-search verdict:** no exact source-valid counterexample candidate survived this first pass. Therefore no finite counterexample checker was warranted; I did not manufacture a checker merely to show that the run occurred.

## 5. B18 — say the source proof in another language: the `log^2 n` is a max-block penalty

The source's proof makes the logarithm unusually transparent. It chooses a block radius

\[
r=K\log n.
\]

There are two exponentially small bad events at scale `r`:

1. in Stage 1, a designated source receives too many particles; the Poisson large-deviation cost is `exp(-c r)`;
2. in Stage 2, Proposition 6.5 says that at most `2 zeta' r` particles placed at one source can be stabilized without exiting an interval of radius `r` except with probability `exp(-c r)`.

The proof asks **all** order-`n/r` blocks to succeed simultaneously. A union bound therefore requires `exp(-cr)` to beat a factor of order `n`, which forces `r` to be order `log n`. The diffusive stabilization cost inside a radius-`r` block is order `r^2` per particle, giving the total source bound `O(nr^2)=O(n log^2 n)`.

This suggests a genuinely different route: do not force every constant-size block to succeed. Start with a large **constant** base scale `L_0`; keep successful blocks frozen; merge only neighboring failed blocks; retry those rare merged regions on scales

\[
L_j=2^jL_0.
\]

Exponential rarity can then beat the polynomial repair cost in **sum**, rather than through a maximum-block union bound.

### Lemma P13-D0093-MULTISCALE-ACCOUNTING-02

Fix `L_j=2^jL_0`. Suppose a legal repair construction for the cycle has, on an event `G_n`, total length `U_j` of regions repaired at scale `j` satisfying

\[
U_0\le n,
\qquad
U_j\le C_0 n e^{-cL_{j-1}}
\quad(j\ge1),
\]

and suppose the total number of topplings used to repair a collection of scale-`j` regions of total length `U_j` is at most

\[
C_1 U_jL_j^2.
\]

Then on `G_n`,

\[
\boxed{T\le Cn}
\]

for a constant `C` depending only on `L_0,c,C_0,C_1`, not on `n`.

#### Proof

Summing the scale costs gives

\[
T\le C_1nL_0^2
+C_0C_1n\sum_{j\ge1}e^{-cL_{j-1}}L_j^2.
\]

Because `L_j=2^jL_0`, the series

\[
\sum_{j\ge1}4^jL_0^2e^{-c2^{j-1}L_0}
\]

converges. Absorb its finite value and the scale-zero term into `C`. `square`

This lemma is deliberately an **accounting reduction**, not a claim that the ARW dynamics already satisfy the hypotheses. It identifies what the source's one-scale proof is paying for and exactly how an adaptive repair scheme could remove that payment.

## 6. B25 — count the same topplings twice: cubic block cost, not the largest block, is the natural quantity

Let `m(x)` be the stabilization odometer. By definition,

\[
\boxed{T=\sum_{x\in\mathbb Z_n}m(x).}
\]

Now recount the same topplings by source blocks. A source block of linear size `L` contains `O(L)` particles on the desired density event. A confined one-dimensional random-walk stabilization costs `O(L^2)` topplings per particle at the scale of exit-time estimates. Thus the crude total cost of one repaired block is

\[
O(L^3).
\]

If all blocks have common size `r`, there are `O(n/r)` blocks and the count is

\[
O\left(\frac nr r^3\right)=O(nr^2),
\]

which is exactly the source `n log^2 n` mechanism when `r=K log n`.

But an adaptive partition with block lengths `L_1,L_2,...` should be charged by

\[
\boxed{\sum_iL_i^3,}
\]

not by `n(max_iL_i)^2`. Consequently, an exponential tail for terminal repair lengths has finite cubic moment and is fully compatible with a linear total budget. This is the same mechanism as the multiscale lemma, expressed directly in the quantity the source is counting.

### Why the argument does not yet close

The missing point is **not** the summation. It is a local ARW theorem strong enough to feed the summation.

Proposition 6.5 of the source begins with at most `2 zeta' r` particles concentrated at a **single source** and produces an exponentially reliable confinement inside a radius-`r` interval. After one or more failed constant-scale repairs, however, an adaptive merged region contains a **distributed, history-dependent configuration**. It is not a fresh centered pile. Simply merging two failed regions and invoking Proposition 6.5 again would therefore be an invalid use of the theorem.

The precise missing source-faithful ingredient is a distributed repair lemma of the following shape:

\[
\boxed{
\begin{minipage}{0.82\linewidth}
For an interval `I` of length `L`, a subcritical configuration in `I` with total mass below `(zeta'+margin)L`, arising after earlier local exploration but with fresh unused instruction-stack tails, can be legally stabilized inside a controlled enlargement of `I` with failure probability at most `e^{-cL}` and toppling cost at most `CL^3`.
\end{minipage}}
\]

The statement above is an **obligation**, not a theorem proved here.

## 7. New way into the blocker: finite-interval trap capacity rather than a centered-pile restart

The source's Section 4 trap-setting construction is now the most promising route. It settles particles one at a time and produces geometric trap spacings with success parameter

\[
\frac{\lambda}{1+\lambda}.
\]

The exact fast-regime inequality

\[
\zeta'<\frac{\lambda}{1+\lambda}
\]

is therefore a negative-drift / excess-trap-capacity condition. Proposition 6.5 is already a two-sided finite-interval trap argument for a centered pile.

The natural strengthening is to start from both boundaries and match traps to a **distributed** list of particles. If the source density slack can be converted into an exponential large-deviation bound for the associated trap-capacity queue, then the missing distributed repair lemma should follow; the multiscale accounting theorem above would then convert it into the desired global `O(n)` high-probability bound.

This is meaningfully different from repeating the source's fixed-block proof: the proposed proof pays for failed blocks by their random cluster sizes rather than choosing one logarithmic scale large enough to make every block good.

A second route remains available from the 2025 infinite-line odometer-tail theorem: extend its Bernoulli proof to Poisson, then prove a local-to-periodic gluing lemma that prevents wrap-around from destroying the tail. I did not claim that gluing lemma here.

## 8. Honest status and next run

The source metric does not move:

\[
\boxed{\beta_{\rm fast}=2\to2.}
\]

But the run is not bookkeeping-only. It did three things that change the mathematical route:

1. it eliminated the simplest Poisson sporadic-pile obstruction by a complete high-probability polynomial-budget lemma;
2. it identified the source `log^2 n` as a **maximum-block union-bound penalty** and replaced it with an explicit multiscale accounting target;
3. it isolated the exact new local theorem required for closure: exponentially reliable **distributed** trap repair with cubic local cost.

The source remains **OPEN / PARTIAL**. No closure, no novelty claim, and no audit vote is asserted. Independent closure would still require a full source-matching proof, a prior-art review with stated limitations, a P26 end-to-end audit, and a second distinct OTHER-track end-to-end audit.

The next three untried-on-D0093 section-B moves are:

- **B3 PROVE SOMETHING STRONGER:** prove a distributed repair lemma with buffer/slack strong enough to survive conditioning on earlier failures;
- **B12 FIND WHAT IS CONSERVED:** track particle mass and unused-stack/trap capacity through merges, seeking a queueing invariant under legal topplings;
- **B30 ONE SCALE AT A TIME:** first prove the two-block merge estimate, then dyadic induction, before attempting the full cycle.

No P14 audit was repeated merely to create activity. The latest P14 state read in this run did not present a new theorem-sized item requiring a fresh P13 component audit, and earlier completed P13->P14 audits remain preserved.

## 9. Structured ledger_delta for P26/coordinator reconciliation

```yaml
ledger_delta:
  worker: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  allocation: CLOSABLE_OUTSIDE
  repository: yspennstate/math-open-problems
  branch: master
  retired_preserved:
    - I0051_Aldous_Janson_OP9
    - P0082_WARM_after_six_run_handoff
  successor:
    problem_id: D0093
    source: Rolla_2020_Activated_Random_Walks_on_Zd
    locator: Section_6_2_open_problem_after_Theorem_6_1_estimate_6_3
    target: remove_log_squared_n_from_fast_phase_total_toppling_bound_on_cycle
    source_initial_law: iid_Poisson_zeta_all_active
    claim_path: operations/claims/D0093.md
    claim_creation_commit: f34fd075a3a4ae57a610152b79d5130b8d35a058
    claim_blob: d4cd8b1caaa1dd9e90e56b55b9702cba5b204176
    ownership: EXCLUSIVE_P13
  metric:
    name: beta_fast
    exact_form: P(T<=kappa*n*(log n)^beta)>=1-n^(-delta)_under_source_fast_domain
    before: 2
    after: 2
    target: 0
    movement: none
    no_movement_count: 1
  methods_actually_tried: [26,18,25]
  mathematical_outputs:
    - P13-D0093-POISSON-POLYNOMIAL-BUDGET-01
    - P13-D0093-MULTISCALE-ACCOUNTING-02
    - fixed_block_cost_recount_sum_L_cubed
  remaining_obligation: >-
    Prove an exponentially reliable finite-interval distributed repair lemma
    under the source density slack zeta'<lambda/(1+lambda), with fresh-stack
    conditioning handled correctly and O(L^3) local toppling cost; then feed
    it into dyadic multiscale repair without replacing the finite-cycle
    Poisson source domain.
  next_methods: [3,12,30]
  source_status: OPEN_PARTIAL
  closure_claim: false
  independent_audits: 0_of_2
```

No shared root ledger, historical report, peer file, scheduler setting, email/Gmail item, Drive object, public post, paid compute, permission, or workflow was modified in this run.
