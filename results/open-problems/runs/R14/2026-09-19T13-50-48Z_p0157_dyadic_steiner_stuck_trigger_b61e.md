Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on P0157: `Q_m -> 0` before and after; this is R14's third consecutive unchanged P0157 run after reassignment, so the next invocation must be STUCK-RECOVERY-1/2 and thinking-only. Methods actually used: #13 FIND WHAT ONLY INCREASES, #21 ASK WHO ELSE HAS THIS SHAPE, #28 REPLACE “FOR ALL” WITH “FOR TYPICAL”.**

# R14 HARD OUTSIDE — P0157 dyadic top-band rank-one reduction

Run date: 2026-09-19 UTC. Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN.** The negative-margin spherical perceptron and H0008 remain terminally handed off and were not reopened. R14 continues the exclusive P0157 assignment recorded in `operations/claims/P0157.md`.

## 1. Continuity, source, and ownership

I continued from the newest own report

`runs/R14/2026-09-19T13-02-27Z_p0157_matched_tail_pair_7b4d.md`

rather than restarting the source. Before the new argument I reread/recovered the controlling campaign/index state, including:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical `operations/claims/P0157.md`;
- the newest R14 P0157 report and the indexed neighboring P0157/R17 admission history;
- the HARD7-04 P0157 chain containing the finite-population maximal-root LLN, absorbing hub kernel, multi-hub obstruction, and four-hub core count;
- indexed intake/problem-list history for van der Hofstad's historical Open Problem 4.13 and current source wording.

The repository-wide intake collections are too large to render literally through the connector in one response; I used their indexed source/alias searches plus the canonical claim rather than claiming a byte-for-byte dump. No competing owner, release, posting exclusion, or source closure surfaced. P0157 remains exclusively R14-owned.

## 2. Fresh primary-source and literature check

I reopened Remco van der Hofstad, *Stochastic processes on random graphs*, current preliminary monograph dated **4 August 2026**, and inspected printed p. 245 / PDF page index 254. In the Notes on Section 8.3 the author still explicitly calls the finite-third-moment subcritical configuration-model behavior an **interesting open problem**. The text recalls the strictly subcritical high-degree law

\[
L_1\asymp \frac{d_{\max}}{1-\nu},
\]

contrasts it with the Erdős--Rényi barely-subcritical scale

\[
\delta_n^{-2}\log(n\delta_n^3),
\qquad \delta_n=1-\nu_n>0,
\]

and says this suggests a phase transition within the subcritical regime.

Fresh bounded searches dated 2026-09-19 again recovered:

1. Matthew Coulson and Guillem Perarnau, *Largest component of subcritical random graphs with given degree sequence*, arXiv:2111.11780 / EJP 28 (2023), which gives strong configuration-model upper bounds in the (barely) subcritical regime and asymptotic tightness for certain degree sequences, but not the complete finite-third-moment crossover requested here.
2. Matthias Lienau and Matthias Schulte, *Large components in the subcritical Norros--Reittu model*, arXiv:2311.17606, whose rank-one independent-edge model is methodologically close to the marked-tail object below but is not the deterministic-degree configuration model.

I did not locate a later source-matching theorem closing P0157 in this bounded search. This is negative bounded evidence only, not a worldwide novelty certificate.

## 3. Frozen metric — no movement and Section-I trigger

The frozen P0157 quantity remains

\[
Q_n
=\frac{\operatorname{Var}(T_n)}{(d_{\max}/\delta_n)^2}
=\frac{\sigma_n^2}{d_{\max}\delta_n}.
\]

On the inherited explicit stress/staircase families,

\[
Q_m\sim m^{-1}\to0.
\]

The new general theorem below does not alter this scalar. Therefore

\[
\boxed{Q_m:0\text{ in the limit}\longrightarrow0\text{ in the limit}.}
\]

This is **R14's third consecutive unchanged P0157 run after reassignment**. Under Section I, the next R14 invocation is therefore mandatory **STUCK-RECOVERY-1/2, thinking-only, with no new theorem claims**. This run remains a research run because the third unchanged count is reached only at its end.

## 4. New theorem-sized result: dyadic top-band Steiner penalty

The complete proof is in

`artifacts/R14/p0157_dyadic_steiner_penalty.md`

created at commit

`2262b4e60815c6447fead05b07d15cc8b3fb9116`.

The result moves the candidate marked-tail graph from a pairwise heuristic to a general upper approximation on a dyadic high-degree band.

Assume

\[
\ell\ge cn,
\qquad
\sum_i d_i^3\le Cn,
\qquad
\delta=1-\frac{\sum_i d_i(d_i-1)}\ell>0.
\]

For a threshold `a`, let

\[
H_a=\{i:d_i\ge a\},
\qquad
\delta_a
=1-\frac1\ell\sum_{v\notin H_a}d_v(d_v-1)\ge\delta.
\]

Fix a prescribed set `A subset H_a` of `r>=2` vertices all in one dyadic degree band,

\[
a\le d_i<2a\qquad(i\in A),
\]

and write `S_A=sum_{i in A} d_i`. Choose `omega>=2` and

\[
R=\left\lfloor\frac{\ell\delta}{4\omega}\right\rfloor,
\qquad
\Delta_a=\delta_a-\frac\delta{2\omega},
\qquad
g=(\ell\Delta_a)^{-1}.
\]

A **tail-exact** connecting tree for `A` is a tree connecting the vertices of `A` whose other vertices all have degree `<a`; thus no unlisted `H_a` vertex is used as an internal Steiner vertex.

Let `C_0=C/c` and

\[
\eta=\frac{2e^2C_0r}{a\Delta_a}.
\]

The proof gives the explicit upper bound

\[
\boxed{
\Pr(\text{a short tail-exact tree connects }A)
\le
\frac1{1-\eta}
\,g^{r-1}
\Big(\prod_{i\in A}d_i\Big)S_A^{r-2}
}
\tag{4.1}
\]

whenever `eta<1`.

The leading term is **exactly** the weighted tree sum of the rank-one kernel:

\[
\boxed{
 g^{r-1}\Big(\prod_{i\in A}d_i\Big)S_A^{r-2}
=
\sum_{T\in\mathcal T(A)}
\prod_{\{i,j\}\in E(T)}
\frac{d_i d_j}{\ell\Delta_a}.
}
\tag{4.2}
\]

Under

\[
\frac r{a\delta_a}\to0,
\qquad
\frac r\omega\to0,
\]

this becomes

\[
\Pr(\text{short tail-exact connection of }A)
\le(1+o(1))
\frac{(\prod_{i\in A}d_i)S_A^{r-2}}
{(\ell\delta_a)^{r-1}}.
\tag{4.3}
\]

The long-exploration error is separately bounded by

\[
\boxed{
\Pr(\exists h\in A:\tau_h>R)
\le\frac{8\omega S_A}{\ell\delta^2}.
}
\tag{4.4}
\]

Thus for top bands also satisfying `omega S_A/(ell delta^2)->0`, the only missing step for a two-sided rank-one approximation is a matching lower bound / overlap-Poissonization theorem. No independence claim is made here.

## 5. Method #13 — find what only increases: the Steiner defect

Take a minimal tree connecting the prescribed top-band vertices and suppress every unmarked bulk vertex of tree-degree two. The remaining core contains the `r` marked vertices and `t` unmarked bulk branch vertices, where

\[
0\le t\le r-2.
\]

The integer `t` is the useful monovariant/defect. Summing all degree-two bulk chains gives one Green factor

\[
\frac1{\ell\Delta_a}
\]

per core edge. If an unmarked branch vertex has core degree `s>=3`, then the finite-third-moment hypothesis gives

\[
\sum_{v\notin H_a}(d_v)_s
\le \frac Cc\,\ell a^{s-3}.
\]

A weighted Cayley sum over all labeled core trees then gives, for the total contribution `W_t` of cores with `t` unmarked branch vertices,

\[
\boxed{
\frac{W_t}{W_0}
\le
\left[
\frac{2e^2(C/c)r}{a\Delta_a}
\right]^t.
}
\tag{5.1}
\]

So every extra unmarked Steiner branch pays another factor of order `r/(a delta_a)`. Once `a delta_a >> r`, higher-order bulk branching is geometrically suppressed.

**Outcome #13: successful.** The obstruction to pairwise rank-one behavior is no longer an amorphous collection of bulk topologies; it is quantitatively indexed by `t`, with an explicit geometric penalty.

## 6. Method #21 — ask who else has this shape: the surviving object is rank one

The `t=0` contribution has no genuine unmarked branch point. Weighted Cayley gives exactly

\[
\frac{(\prod_i d_i)S_A^{r-2}}{(\ell\delta_a)^{r-1}},
\]

which is the tree weight of a rank-one inhomogeneous graph with pair scale

\[
\kappa_{ij}^{(a)}=\frac{d_i d_j}{\ell\delta_a}.
\]

This is the same structural language used by Norros--Reittu / rank-one models. The fresh Lienau--Schulte paper confirms that largest subcritical components in that independent-edge setting are naturally tied to large weights/degrees, but I do **not** transfer their theorem to the dependent configuration-model tail graph.

**Outcome #21: successful as a category match.** The rank-one graph is now derived as the leading **tree-count upper object** rather than guessed from a two-hub marginal. The remaining difficulty is dependence/overlap, not identification of the first-order kernel.

## 7. Method #28 — replace “for all” with “for typical”: localize by top degree scale

The source's full finite-third-moment class allows complicated upper tails, and the previous matched-pair theorem showed that no fixed scalar summary can work globally. The natural way to avoid demanding one uniform coupling across all degrees is to condition on the component's top degree scale and use dyadic bands.

For a component whose relevant top vertices lie in `[a,2a)`, the theorem above applies to its prescribed top-band marked set. On bands satisfying

\[
r=o(a\delta_a),
\qquad
\omega S_A=o(\ell\delta^2),
\]

the dangerous unmarked Steiner cores and long-exploration witnesses are negligible, leaving the rank-one marked tree sum as the leading upper object.

**Outcome #28: successful as a localization reduction.** It identifies a broad class of typical/top-band components where the general CM dependence is reduced to a rank-one overlap problem. It does not yet prove that every extremal component falls into such a band with the required quantitative bounds.

## 8. Exact proof mechanism

For completeness, the two short calculations that drive the theorem are:

### Bulk chains

If `D=ell-2R`, then

\[
\sum_{v\notin H_a}d_v(d_v-1)=\ell(1-\delta_a),
\]

so a core edge expanded through any number of degree-two-in-tree bulk vertices contributes at most

\[
\sum_{k\ge0}D^{-1}
\left(\frac{\ell(1-\delta_a)}D\right)^k
=\frac1{D-\ell(1-\delta_a)}
\le\frac1{\ell\Delta_a}.
\]

### Core branches

After labeling the `t` unmarked branch vertices (an overcount), weighted Cayley gives

\[
\sum_T
\prod_{i\in A}d_i^{\deg_T(i)}
\prod_{u=1}^t a^{\deg_T(u)}
=
\Big(\prod_{i\in A}d_i\Big)a^t(S_A+ta)^{r+t-2}.
\]

Combining this with the branch-moment bound and the chain Green factors yields (5.1), then summing the geometric series yields (4.1).

The proof is theorem-sized and written on the page. No finite claim required an exact-arithmetic checker, so no checker-only artifact was manufactured.

## 9. What remains / exact blocker for the mandatory stuck recovery

The marked-tail route is now narrowed to a precise two-sided dependence problem. The strongest missing statement is of the form

\[
\boxed{
\Pr(A\text{ is tail-exact connected})
\sim
\sum_{T\in\mathcal T(A)}
\prod_{\{i,j\}\in E(T)}
\frac{d_i d_j}{\ell\delta_a}
}
\tag{9.1}
\]

uniformly in the growing top-band ranges needed for the extreme component, together with the bulk-mass transfer

\[
|C|\approx\delta^{-1}\sum_{i\in C\cap H_a}d_i.
\tag{9.2}
\]

The current theorem proves only the upper/tree-dominance half of (9.1), not the matching lower bound or an independent-edge coupling. That is the exact obstruction the next thinking-only recovery must address.

Because the frozen metric has now been unchanged for three consecutive R14 P0157 runs, **the next invocation must not add another lemma.** It must write the full Section-I five-part stuck report and choose exactly one recovery action. The fresh method triple reserved for that recovery is:

- **#11 DUALIZE** — seek a switching / Radon--Nikodym formulation comparing the CM pairing law to the rank-one tail graph;
- **#25 COUNT THE SAME THING TWICE** — derive the same prescribed-tree event by witness counting and by sequential exploration to expose the missing lower correction;
- **#30 ONE SCALE AT A TIME** — first solve a single dyadic band with `r=o(a delta_a)` before trying to glue scales.

## 10. Model / scheduler capability truth

The model-control limitation remains exactly as recorded by the deployment policy. The exposed task-control schema permits title/prompt, schedule or relative start, timing mode, enablement, and notifications, but exposes **no binding model-family selector and no reasoning-effort selector**. GPT-6/maximum is therefore prompt text only in this surface; it cannot be truthfully claimed as the applied runtime here.

The historical P26 `You cannot modify this task` error was an authorization-context boundary, and repository records say P26 was later editable from another authorized context. The legitimate remedy for any presently protected task is the owning/admin-authorized account/workspace/context or platform support. No permission bypass, duplicate scheduler, or scheduler mutation was attempted here.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  category: HARD_OUTSIDE
  target: P0157
  source_status: OPEN
  worker_status: PARTIAL
  runtime_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  requested_model: GPT-6
  requested_reasoning: maximum

  frozen_quantity: Q_n = sigma_n^2/(d_max*delta_n)
  before: Q_m ~ m^-1 -> 0
  after: Q_m ~ m^-1 -> 0
  movement: none
  r14_p0157_unchanged_streak: 3
  next_lifecycle_state: STUCK_RECOVERY_1_OF_2_THINKING_ONLY

  methods: [13, 21, 28]
  substantive_result: "dyadic top-band tail-exact connection upper bound with geometric Steiner penalty"
  leading_kernel: "kappa_ij^(a) = d_i*d_j/(ell*delta_a)"
  steiner_penalty: "W_t/W_0 <= [2 e^2 (C/c) r/(a Delta_a)]^t"
  long_error: "P(exists h in A: tau_h>R) <= 8 omega S_A/(ell delta^2)"
  exact_blocker: "uniform matching lower bound / overlap-Poissonization for the rank-one tail tree law, plus bulk-mass transfer"

  artifact: artifacts/R14/p0157_dyadic_steiner_penalty.md
  artifact_commit: 2262b4e60815c6447fead05b07d15cc8b3fb9116
  checker_created: false
  independent_audits: 0

  next_methods: [11, 25, 30]
  next_run_rule: "Section-I STUCK-RECOVERY-1/2; thinking-only; no new theorem claims"

  shared_roots_edited: false
  peer_files_edited: false
  scheduler_changed: false
  email_or_drive_used: false
  public_posting_used: false
```

**Net result:** no frozen-metric movement, but a general structural reduction: on a dyadic high-degree band, the configuration-model tail connectivity has a rank-one weighted-tree upper term and every extra unmarked bulk Steiner branch vertex pays an explicit factor `O(r/(a delta_a))`. The next run is nevertheless forced into the Section-I thinking-only recovery because the fixed metric has now been unchanged three consecutive times.