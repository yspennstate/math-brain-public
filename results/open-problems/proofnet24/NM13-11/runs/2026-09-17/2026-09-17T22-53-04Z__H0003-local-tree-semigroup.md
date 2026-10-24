Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MOVEMENT in the frozen `A_echo` metric: on bounded-degree Benjamini–Schramm-to-tree, strictly subcritical source instances the global coefficient `Lambda_*` can be replaced by the local-tree coefficient `a_Delta = 2*sqrt(Delta_max-1)` without a uniform global spectral-gap hypothesis; in particular on connected `d`-regular approximants the certified coefficient moves `d -> 2*sqrt(d-1)`. Methods actually tried this run: #5 ADD A PARAMETER AND DIFFERENTIATE, #18 SAY IT IN ANOTHER LANGUAGE, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# NM13-11 third run — H0003 local-tree semigroup bound beyond global spectral contraction

Date: 2026-09-17 UTC  
Track: NM13-11 / HARD OUTSIDE  
Repository: `yspennstate/math-open-problems`, branch `master`  
Canonical source/claim: H0003 / `operations/claims/H0003.md`  
Canonical dedup identity: `arxiv_2608_15987::conjecture_11.8`, residue 10 mod 13  
Overall source status: **OPEN**  
Local status after this run: **PARTIAL; new strong-coupling subcritical slice proved**

## 1. Runtime honesty and control-plane status

The requested header asks for GPT-6 with maximum reasoning. That is not what I can verify ran. The actual model exposed to this invocation is **GPT-5.6 Sol**. The reasoning-effort level is not authenticated by runtime telemetry or a binding selector and is therefore **UNVERIFIED**.

The exposed automation/task-control schema still has task text/title, timing/schedule, enabled state and timing-mode controls, but **no model-family selector and no reasoning/thinking selector**. Thus `GPT-6 / maximum` remains prompt text rather than a binding scheduler setting in this interface. Making it binding would require a platform/task surface that actually exposes model and reasoning fields, used from an authorized owner context. The repository also records an older `You cannot modify this task` response for one P26 context and a later successful P26 update from another authorized context; I therefore do not treat the older denial as a permanent global state. If such a denial occurs for a particular task, the lawful remedy is the owning account/workspace or an authorized product/admin surface, not a duplicate job or an ACL bypass. I changed no schedule in this invocation.

## 2. Continuity recovered before new mathematics

This is not a new admission. I continued the live, exclusive H0003 claim owned by NM13-11. Before working I reread or targeted-search-recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and the later NM13 deployment record;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the H-intake row in `probability_1000_intake_H_20260914/problems.jsonl`;
- `operations/claims/H0003.md`;
- both earlier NM13-11 immutable reports, newest first: `2026-09-17T21-48-00Z__H0003-pf-coboundary-critical-stability.md` and `2026-09-17T20-49-43Z__H0003-spectral-echo-first-attack.md`;
- newest neighboring NM13-10 and NM13-12 reports;
- targeted searches for H0003, its exact arXiv identity, claims, attempts, handoffs, retirement/POSTED state, and neighboring percolation/interacting-particle ownership.

No release, handoff, retirement, posted result, new owner, or outside audit for H0003 was recovered. The canonical claim remains NM13-11-owned. The H intake still identifies Conjecture 11.8 as the exact source statement. Repository/code searches are bounded default-branch searches and large ledgers can be connector-truncated; I do not represent this as an omniscient byte-for-byte history census. The source-specific continuity required for this run was accessible.

## 3. Fresh source and literature check

Dated bounded check: **2026-09-17 UTC** (crossing into 2026-09-18 local time does not change the UTC report date).

Exact source: Achyut Kumar, *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1, 17 August 2026, Conjecture 11.8 / Section 11.5:

`https://arxiv.org/abs/2608.15987`

The source still says the strong-coupling regime `kappa>=1` is open. Its Proposition 11.2 gives cellwise `O(epsilon(delta))` control, Lemma 11.3 gives first-passage stability under bounded drift perturbation, Lemma 11.4 / Theorem 11.5 prove front decoupling when

`kappa = gamma_max L_sigma Delta_max / alpha_min < 1`,

and Conjecture 11.8 asks for the full saturated regime, including strong coupling and critical-window uniformity.

Fresh exact-title/author searches again recovered only v1 of the source and the Kumar--Duddala companion arXiv:2608.21125 (21 August 2026). The companion treats front propagation / Bramson correction and the continuous-type limit, not a proof of Conjecture 11.8. No source-matching later resolution was recovered. This is bounded negative evidence, not proof of worldwide openness or novelty.

For the graph input below I searched `spectral radius finite tree maximum degree 2 sqrt(D-1)` and nearby formulations. The inequality

`rho(A_T) <= 2 sqrt(Delta-1)`

for a tree of maximum degree `Delta` is standard graph-spectral folklore; Dvorak--Mohar (arXiv:0907.1591) explicitly describes it as well known. I therefore make **no novelty claim for that spectral lemma**. I did not recover a source applying the finite-time/local-tree semigroup truncation below to Kumar's echo problem. Novelty of that synthesis remains **UNVERIFIED**.

## 4. Frozen metric and previous state

The metric remains exactly the admission metric:

`A_echo` = a graph-amplification coefficient in a rigorously proved sufficient linear echo-stability condition

`gamma_max * L_sigma * A_echo < alpha_min`

that is actually carried through to a source-relevant front-decoupling theorem.

Source baseline: `A_echo = Delta_max` in the row-sum criterion of Theorem 11.5.

First NM13-11 run: on the additional uniform-global-spectral subclass,

`A_echo = Lambda_* := sup_n ||A(G_n)||_(2->2)`.

Second run: no change to this metric; `Lambda_* -> Lambda_*`.

This run proves a different, genuinely local coefficient for the source's bounded-degree locally-tree-like setting:

`a_Delta := 2 sqrt(Delta_max-1)`.

On the overlap with the old global-spectral subclass the best certified coefficient is now

`A_echo = min{Lambda_*, a_Delta}`.

More importantly, the `a_Delta` theorem below does **not** assume a uniform global spectral gap at all. For any connected finite `d`-regular approximant, `Lambda_*=d`, so the concrete certified movement is

`d -> 2 sqrt(d-1)`,

strict for every `d>=3`. Hence the interval

`2 gamma_max L_sigma sqrt(d-1) < alpha_min <= gamma_max L_sigma d`

is a nonempty source-classified **strong-coupling** (`kappa>=1`) slice now covered in the strictly subcritical regime.

---

# 5. Method #5 — ADD A PARAMETER AND DIFFERENTIATE

The previous run proposed differentiating the full one-cell SDE law. I tried that literally first. A direct interpolation between the true and directed stopped SDEs creates a nuisance: one must prove the saturation/stopping geometry uniformly for every interpolated path before differentiating its stopped law. I did **not** assume that missing fact.

Instead I parameterised the rigorous comparison equation that the source itself derives before any `kappa<1` weighted-norm step.

Put

`c := gamma_max L_sigma`, `alpha := alpha_min`, and let `A=A(G_n)`.

From the synchronous coupling, with `x_v(t)=|D_v(t)|`, the source's line-by-line argument gives up to the stopped exploration

`D^+ x(t) <= (-alpha I + c A) x(t) + g(t)`                         (5.1)

coordinatewise, with `g_v(t) <= gamma_max epsilon(delta) 1{v~S_t}`.

Introduce an echo-strength parameter `z in [0,1]` in the dominating semigroup,

`P_z(t) := exp[t(-alpha I + z c A)]`.

Because `I` and `A` commute, differentiation is exact:

`(d^j/dz^j) P_z(t)|_(z=0) = e^(-alpha t) (c t)^j A^j`.             (5.2)

Thus the `j`th derivative in echo strength is exactly the contribution of graph walks of length `j`. This is the parameter calculation I needed: it says that the obstruction is not best organised by global eigenmodes first, but by **echo order / walk length**.

Outcome of method #5: the literal stopped-cell-law derivative remains unresolved, but differentiating the already-rigorous echo comparison exposes an exact walk-length expansion and produces a new route. No unproved interpolation hypothesis is used below.

---

# 6. Method #18 — SAY IT IN ANOTHER LANGUAGE: killed walk counts

Equation (5.2) rewrites the echo as a killed-walk Green kernel. Variation of constants and positivity of the Metzler comparison matrix give

`x(t) <= int_0^t exp[(-alpha I+cA)(t-s)] g(s) ds`                  (6.1)

coordinatewise. Expanding the semigroup,

`exp[(-alpha I+cA)u] = e^(-alpha u) sum_(j>=0) (cu)^j A^j/j!`.    (6.2)

So a perturbation travels along a length-`j` graph walk, pays `(cu)^j/j!`, and is killed in time at rate `alpha`. The source's coefficient `Delta_max` bounds all walk growth by `Delta_max^j`. On a tree neighbourhood, that is wasteful: the relevant `l2` growth is at most `a_Delta^j` with

`a_Delta=2 sqrt(Delta-1)`.

## Lemma 6.1 — exact finite-tree spectral bound

Let `T` be any finite tree of maximum degree at most `Delta>=2`. Then

`||A_T||_(2->2) <= 2 sqrt(Delta-1)`.                               (6.3)

### Proof

Root the tree arbitrarily and orient every edge parent-to-child. For any real vector `f`, put `q=sqrt(Delta-1)` and use

`2 |f_p f_c| <= q^(-1) f_p^2 + q f_c^2`                           (6.4)

on every oriented edge `p->c`.

A nonroot vertex receives coefficient at most `q` from its parent edge and at most `(Delta-1)/q=q` from its child edges, hence at most `2q`. The root receives at most `Delta/q <= 2q` (the last inequality is exactly `Delta<=2(Delta-1)`). Therefore

`|f^T A_T f| <= 2q ||f||_2^2`.

Since `A_T` is symmetric, (6.3) follows. ∎

This lemma is standard; the proof is included only so the present theorem has no hidden graph-spectral dependency.

The key point is local: even when a finite `d`-regular graph has the global Perron eigenvalue `d`, every fixed tree ball has adjacency norm at most `2 sqrt(d-1)`. Benjamini--Schramm convergence lets us use that local norm for every **bounded echo order**, while the factorial tail in (6.2) controls the discarded long echo orders over a bounded physical time window.

Outcome of method #18: the global instability is translated into a walk-length tail. That makes the locally-tree-like geometry usable even when the global constant mode destroys the first run's `Lambda_*<Delta` improvement.

---

# 7. Method #30 — ONE SCALE / ONE DIRECTION AT A TIME

I now localise three quantities separately rather than trying to control the infinite cascade in one estimate:

- at most `K` failed vertices;
- at most time `T` for each active transmission decision;
- at most `R-1` echo steps before charging the factorial walk tail.

The result is a complete restricted theorem.

## Theorem NM13-11-H0003-LOCAL-TREE-ECHO-03

Let `(G_n,o_n)` be finite connected graphs with maximum degree at most `Delta>=2`, rooted uniformly, and suppose

`(G_n,o_n) ->^BS (T,o)`

where `T` is a tree (in particular the source's `UGW(g)` case). Assume the source's saturated regime and finite type set, and assume the ideal multitype Galton--Watson law is strictly subcritical:

`rho(M)<1`.

Set

`c = gamma_max L_sigma`,
`a_Delta = 2 sqrt(Delta-1)`,
`g_tree = alpha_min - c a_Delta`.

If

`g_tree>0`,                                                        (7.1)

then in the iterated limit `n->infinity` followed by `delta->infinity`, the failed-cluster law converges in total variation to the source's ideal multitype Galton--Watson law. In particular the source reduction is unconditional on this strictly subcritical slice, even if

`kappa = c Delta / alpha_min >= 1`.

A quantitative stopped estimate is as follows. Let `epsilon=epsilon(delta)`. Let

`eta_(n,L) = P(B_(G_n)(o_n,L) is not a tree)`.

For integers `K,R>=1` and `T>0`, put `H=K T` and

`Q_R(x)=sum_(j>=R) x^j/j!`.

There are source-parameter constants `C,C_0,c_0,C_exit,lambda_exit>0`, independent of `n,K,R,T,delta`, such that the mismatch probability of breadth-first explorations stopped at `K` failed vertices obeys

`delta_(n,K) <= eta_(n,K+R+2)
               + C epsilon K
               + C epsilon K^(3/2) [ g_tree^(-1) + H Q_R(c Delta H) ]
               + C_exit K exp(-lambda_exit T)`,                    (7.2)

and the full cluster laws obey

`d_TV(L(S_n),L(S_GW)) <= 2 delta_(n,K) + 2 C_0 exp(-c_0 K)`.        (7.3)

Consequently one may choose `K,T,R` as functions of `epsilon` after the `n->infinity` limit so that the right side tends to zero as `epsilon->0`.

### Proof

#### Step 1. Stop before the geometry can grow

Couple the true and directed systems synchronously as in the source and telescope their breadth-first transmission decisions exactly as in Theorem 11.5. Stop when either a mismatch occurs or `K` failed vertices have been discovered.

Before this stopping time the failed set is connected to the root and has at most `K` vertices, hence it lies in `B(o,K-1)`. The source term in (5.1) is supported on neighbours of the failed set, hence in `B(o,K)`, and by the source's bound `g_v<=gamma_max epsilon 1{v~S_t}`,

`||g(t)||_2 <= C_g epsilon sqrt(K)`                                (7.4)

for a constant depending only on the fixed degree/type/coupling bounds.

#### Step 2. Uniform active-cell exit-time tail

While a child is awaiting its transmission decision, its state lies between the safe and failure barriers, a fixed bounded interval. On this interval the total drift of either the true or directed cell is bounded in absolute value by a constant `B`: the OU part is bounded there, the graph degree is at most `Delta`, all couplings are bounded, and `0<=sigma<=1`. Its diffusion coefficient is one of finitely many `b_d` and satisfies `b_d^2>=mu_0>0`.

Fix `t_0>0`. If, during an interval of length `t_0`, the Brownian increment at the endpoint exceeds

`A_0 := (L+B t_0)/b_min`,

where `L` is the safe-to-failure interval width and `b_min=min_d b_d>0`, then a trajectory that had remained inside the interval would have endpoint displacement greater than `L`, a contradiction. Thus, conditionally on every past history, the probability of exiting one of the two barriers within `t_0` is at least

`p_0=P(N(0,t_0)>=A_0)>0`.

Applying the strong Markov property at multiples of `t_0`, uniformly over types and histories,

`P(tau_exit>T | past) <= C_exit exp(-lambda_exit T)`.               (7.5)

The same bound holds for both coupled cells. At most `Delta K` transmission decisions are tested before the `K`-vertex stop, so the event that any tested cell remains unresolved more than `T` after activation has probability at most the last term of (7.2), after changing `C_exit`.

On the complementary event every causal chain leading to a tested decision has physical duration at most

`H=KT`.                                                             (7.6)

#### Step 3. Tree-local semigroup estimate up to echo order `R-1`

Work on the event that `B(o,K+R+2)` is a tree. Let `v` be a currently tested child or one of its neighbours. For every `j<R`, any length-`j` graph walk from the support of `g` to `v` stays inside that tree ball. Therefore the `j`th term of (6.2), when evaluated at `v`, is exactly a term in the adjacency power of a finite tree of maximum degree `Delta`.

By Lemma 6.1,

`|(A^j g)_v| <= a_Delta^j ||g||_2`, `j<R`.                          (7.7)

For `j>=R` use only the global degree bound,

`|(A^j g)_v| <= Delta^j ||g||_2`.                                   (7.8)

Insert (7.7)--(7.8) into (6.1)--(6.2), use (7.4), and restrict to `t<=H`. The short-walk contribution is bounded by

`C_g epsilon sqrt(K) int_0^infinity exp[-g_tree u] du
 = C_g epsilon sqrt(K)/g_tree`.                                      (7.9)

The long-walk contribution is bounded by

`C_g epsilon sqrt(K) H Q_R(c Delta H)`.                              (7.10)

Thus every state coordinate relevant to the next transmission test, and by the same estimate each of its at most `Delta` neighbouring coordinates, differs between the true and directed systems by at most

`C epsilon sqrt(K) [g_tree^(-1)+H Q_R(c Delta H)]`.                  (7.11)

The corresponding drift discrepancy in the one-cell equation is bounded by the same expression after multiplying by the fixed factor `c Delta` and adding the direct `O(epsilon)` saturated-cell residual.

#### Step 4. Convert to a transmission-probability error

Apply the source's Lemma 11.3 to the one-cell first-passage problem. On the event that the decision resolves by time `T`, the barrier-sandwich proof of that lemma only needs the uniform drift/state bound up to the exit time, which is provided by (7.11). If a decision lasts longer than `T`, charge it to (7.5).

Hence each tested edge has conditional mismatch probability at most

`C epsilon
 + C epsilon sqrt(K)[g_tree^(-1)+H Q_R(c Delta H)]`

plus its exit-tail charge. Before `K` failures there are at most `Delta K` tested outward edges. Maximal coupling one edge at a time and summing the conditional mismatch probabilities gives exactly (7.2), with the non-tree-ball event charged to `eta_(n,K+R+2)`.

#### Step 5. Remove the `K` cutoff

The previous NM13-11 spectral-echo report already proved, from the finite-type bounded-offspring generating-function equation, that strict subcriticality `rho(M)<1` gives an exponential ideal total-progeny tail

`P(|S_GW|>=K) <= C_0 exp(-c_0 K)`.                                  (7.12)

No new assumption is introduced here. If the stopped explorations agree and the ideal tree dies before `K`, the true exploration has made the same transmission decisions and also dies before `K`. Thus the same cutoff-removal coupling used in that report yields (7.3).

#### Step 6. Choose the three scales

For each fixed `epsilon>0`, choose for example

`K = ceil(A log(1/epsilon))`,
`T = ceil(B log(1/epsilon))`,
`H=KT`,

with `A,B` large enough that the last term of (7.2) and (7.12) vanish as positive powers of `epsilon`.

Now choose

`R >= 2 e c Delta H`.

For `x=c Delta H` and every `j>=R`, Stirling's elementary bound `j! >= (j/e)^j` gives

`x^j/j! <= (e x/j)^j <= 2^(-j)`,

hence

`Q_R(c Delta H) <= 2^(1-R)`.                                       (7.13)

So the long-walk term in (7.2) is negligible, while the short-walk contribution is

`O(epsilon K^(3/2)/g_tree)=o(1)`.                                   (7.14)

For fixed `epsilon`, the chosen `K,T,R` are finite. Benjamini--Schramm convergence to a tree therefore gives

`eta_(n,K+R+2) -> 0`

as `n->infinity`. Taking that limit first and then `epsilon(delta)->0` proves the theorem. ∎

### What the theorem does and does not say

1. It **does** remove the source's row-sum contraction condition `c Delta<alpha` on a real source-valid subcritical slice, replacing it by

   `2 c sqrt(Delta-1)<alpha`.

   For `Delta>=3` these conditions differ on a nonempty interval.

2. It **does** avoid the first run's global spectral hypothesis. A finite `d`-regular graph has global adjacency norm `d`, but its bounded-radius tree neighbourhoods obey the `2 sqrt(d-1)` coefficient; factorial suppression of long walk orders prevents distant cycles/global constant modes from contaminating a bounded cascade experiment before the BS limit is taken.

3. It is **not** Conjecture 11.8. The theorem is strictly subcritical, has a polylogarithmic loss if one extracts an explicit `epsilon` rate from the displayed scale choice, and does not supply the conjectured uniform `C(epsilon+eta_n)` critical-window estimate.

4. It does not treat unbounded degrees.

5. The tree spectral inequality is standard/folklore; the source-specific semigroup/locality synthesis has only a bounded prior-art search and carries no certified novelty label.

6. No finite computation is used to infer an asymptotic theorem. No checker artifact is warranted: the claims are analytic and their proofs are written above.

---

# 8. Metric movement and strong-coupling witness

The frozen quantity moves this run.

Before:

`A_echo = Lambda_*` on the additional uniform-global-spectral subclass.

After:

`A_echo = a_Delta = 2 sqrt(Delta_max-1)` on the bounded-degree BS-to-tree, strictly subcritical class, with `min{Lambda_*,a_Delta}` available on the overlap.

Concrete source-valid witness: connected `d`-regular finite graph sequences with local weak limit the `d`-regular tree. For every finite connected `d`-regular graph,

`Lambda_*=d`,

while the new local coefficient is

`2 sqrt(d-1)<d` for `d>=3`.

For `d=3`, this is

`3 -> 2 sqrt(2)`.

Thus parameters satisfying

`2 sqrt(2) gamma_max L_sigma < alpha_min <= 3 gamma_max L_sigma`

are classified as `kappa>=1` by the source but are covered by Theorem LOCAL-TREE-ECHO-03 when `rho(M)<1` and the saturation assumptions hold.

Because the metric moved, the consecutive unchanged-run counter resets from 1 to **0**. Hard stuck-recovery count remains **0**.

## 9. Relation to the previous critical Perron-coboundary route

The second run's theorem `NM13-11-H0003-PF-COBOUNDARY-TV-02` remains useful and is not superseded. The two routes now attack orthogonal obstructions:

- **LOCAL-TREE-ECHO-03** controls spatial echo amplification past `kappa=1` in the strictly subcritical regime;
- **PF-COBOUNDARY-TV-02** shows how a very special first-order offspring-law score can avoid `epsilon * volume` accumulation at criticality.

The natural next problem is to join them without assuming the missing bridge: derive a source-valid front score after the local-tree semigroup reduction and determine whether its first-order critical component is a Perron coboundary. I do not claim that it is.

## 10. Next methods

Do not repeat `5,18,30` next run. If H0003 remains active, use a genuinely different triple:

- **#11 DUALIZE:** derive the first-order critical cell-score as a linear functional and identify the annihilator of finite-tree flow constraints; this should decide exactly which score components telescope.
- **#15 BREAK THE SYMMETRY ON PURPOSE:** test a two-type asymmetric parent/child system, where a false coboundary guess cannot hide behind regular-tree symmetry.
- **#22 READ THE FAILURES, NOT THE SUCCESSES:** inspect the source's failed Girsanov route and the closest multitype perturbation literature specifically for the non-telescoping score component, rather than collecting more positive analogies.

No audit is requested or counted yet. The source remains OPEN/PARTIAL and this run is not a closure package.

---

```yaml
ledger_delta:
  track: NM13-11
  source_id: H0003
  canonical_dedup_key: arxiv_2608_15987::conjecture_11.8
  claim_path: operations/claims/H0003.md
  category: HARD_OUTSIDE
  exact_source_status: OPEN
  mathematical_status: PARTIAL
  metric:
    name: A_echo
    before: Lambda_star_on_uniform_global_spectral_subclass
    after: 2_sqrt_Delta_minus_1_on_bounded_degree_BS_tree_subcritical_class
    overlap_best: min_Lambda_star_and_2_sqrt_Delta_minus_1
    concrete_d_regular_before: d
    concrete_d_regular_after: 2_sqrt_d_minus_1
    movement: true
    meaning: sufficient graph-amplification coefficient in gamma_max*L_sigma*A_echo < alpha_min carried through to front decoupling
  new_internal_theorem:
    id: NM13-11-H0003-LOCAL-TREE-ECHO-03
    statement: bounded-degree BS-to-tree saturated cascades with rho(M)<1 satisfy front decoupling whenever alpha_min > 2*gamma_max*L_sigma*sqrt(Delta_max-1), without a uniform global adjacency-spectral-gap assumption
    source_level_scope: PARTIAL_STRONG_COUPLING_SUBCRITICAL_SLICE
  methods_tried: [5, 18, 30]
  method_outcomes:
    5: exact echo-strength derivative of the comparison semigroup identifies echo order with graph-walk length; literal stopped-cell-law differentiation was not assumed
    18: killed-walk/semigroup language isolates the local tree spectral coefficient 2*sqrt(Delta-1) and a factorial long-walk tail
    30: K-vertex, T-time, R-walk truncation yields a complete BS-transfer proof and a genuine strong-coupling subcritical extension
  unchanged_runs: 0
  stuck_recoveries: 0
  audits:
    p26: MISSING
    nm13_12: MISSING
  closure: false
  next_obligation: combine the local-tree spatial control with a source-derived first-order critical offspring score, then decide whether the score lies in the Perron/tree-coboundary subspace
  next_methods: [11, 15, 22]
  literature_status: bounded_search_no_source_matching_resolution_found
  novelty_status: UNVERIFIED
  shared_root_edit_requested: false
  artifacts_created: []
```

**End of complete run report.**