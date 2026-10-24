Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. HARD7-03 frozen metric has no movement, `L <= Delta_2(Q): 500000/6578563 -> 500000/6578563`; methods B1 / B19 / B27. Source-scope movement: the self-checked plateau mechanism extends from `K=2` to every fixed `K>=1` for iid site disorder with positive essential infimum.**

# HARD7-03 — source-coordinate recovery and a general-`K` site-disorder plateau candidate

Date: 2026-09-19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source Problem 4 remains OPEN as a whole.** This run gives a theorem-sized self-check that answers the **flat-segment clause** of Seppäläinen's Problem 4 for every fixed capacity `K>=1` in the iid **site-disorder** model covered below, assuming the source growth-model/duality framework exactly as printed. It does not settle the broader phase-transition question, particle disorder, finer-scale behavior, or any formulation outside this source model. No closure is claimed: prior-art search is bounded and the result has not received the two required independent audits.

Canonical target: `D0025`, Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4. Active owner claim: `operations/claims/D0025.md`, owner `HARD7-03`.

The exact source model is the one-dimensional totally asymmetric `K`-exclusion process with site rate `alpha_x`: a particle jumps from `x` to `x+1` at rate `alpha_x` when the source is nonempty and the target contains fewer than `K` particles. The source asks whether there is a phase transition analogous to the disordered zero-range process and, concretely, whether the hydrodynamic flux has a flat segment around density `K/2`.

## 1. Continuity, repository state, source check, and literature refresh

I resumed the newest HARD7-03 checkpoint rather than restarting admission:

`runs/hard7_2026-09-18/HARD7-03/20260919T0221Z__d0025-general-k2-no-atom-plateau.md`.

Before the new mathematics I re-read/recovered the required current state:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/D0025.md` and the D0025 intake/source records;
- the full current HARD7-03 checkpoint chain;
- the newest visible neighboring HARD7-02 and HARD7-04 reports.

Repository collision search still has D0025 exclusively owned by HARD7-03; no release, posted equivalent, or competing canonical claim was found.

### Primary-source geometry rechecked rather than inferred from the `K=2` rewrite

The source open problem was rechecked in arXiv `math/9906194` / DOI `10.11606/resimeusp.v4i1.74889`. For the growth model and exact `K`-dependent path geometry I also rechecked Seppäläinen, *Existence of hydrodynamics for the totally asymmetric simple K-exclusion process*, Ann. Probab. 27 (1999), 361–415, DOI `10.1214/aop/1022677266`.

The latter source defines `K`-admissible lattice paths with exactly three step types

`(1,0), (0,1), (K,-1)`,                                      (1.1)

and attaches to site `(i,j)` the passage time

`tau_{i,j}=lambda_{i,j}/alpha_j`,                             (1.2)

where the `lambda_{i,j}` are iid unit exponentials. Thus the disorder is columnar/rowwise in the second coordinate. Proposition 5.1 gives the deterministic concave passage shape `gamma_K(x,y)` on the wedge `x>0, y>-x/K`; the level-one boundary is

`g_K(y)=inf{x>0: gamma_K(x,y)>=1}`,                           (1.3)

and the hydrodynamic flux is exactly

`f_K(rho)=inf_x {rho x + g_K(x)}, 0<=rho<=K`.                 (1.4)

Crucially, Lemma 9.1(ii) states for a reversible rate environment (in particular iid rates)

`g_K(-y)=g_K(y)+K y`.                                         (1.5)

This is the source identity that centers the relevant subgradient at `-K/2`.

### Bounded current-literature refresh, 2026-09-19

Fresh searches used combinations of `disordered K-exclusion`, `site disorder K-exclusion flux`, `partial exclusion random rates plateau`, `flat segment K-exclusion`, and the exact Seppäläinen source/problem. They again recovered:

- Allan Sly, *Note on the flux for TASEP with general disorder*, arXiv:1609.06589, proving a plateau for ordinary `K=1` iid site-disordered TASEP;
- Bahadoran–Bodineau's `K=1` site-disorder plateau/quantitative work;
- Floreani–Redig–Sau, *Hydrodynamics for the partial exclusion process in random environment*, whose environment randomizes site capacities rather than Seppäläinen's totally asymmetric site jump rates;
- Gonçalves–Hayashi–Sasada, arXiv:2405.15142, a different asymmetric partial-exclusion class tied to gradient/product-measure structure;
- Ayyer–Misra's exactly solvable deformed-rate `K`-exclusion, not the source process.

No located source closed the exact `K>=2` iid site-rate plateau question. This is **bounded negative evidence only**, not a worldwide novelty certificate. The argument below should therefore be treated as a self-checked candidate extension of the Sly-type comparison mechanism, pending citation-graph review and independent audits.

## 2. Frozen metric: no movement, but a genuine source-scope advance

The canonical frozen quantity remains

`Delta_2(Q)=sup{delta>=0: f_{2,Q} is constant on [1-delta,1+delta]}`

for

`Q=(1/2) delta_{1/2}+(1/2) delta_1`,

with tracked rigorous certificate `L<=Delta_2(Q)`.

Before:

`L = 500000/6578563`.

After:

`L = 500000/6578563`.

So there is **no movement on the frozen numerical metric** this run. The substantive advance is orthogonal to that scalar: the preceding theorem covered `K=2`; the argument below removes the `K=2` path-length accident and yields the same qualitative plateau mechanism for **every fixed `K`**.

This is not counted as numerical movement and does not reset the metric definition.

## 3. B1 — change category: first kill the false `K=2` coordinate generalization

The preceding proof used, for `K=2`, the change of coordinates

`t=i+j-1,  y=j`,

under which all three admissible steps become one-unit-time lazy nearest-neighbor steps. That representation does **not** generalize to `K>=3`.

Let a `K`-admissible path from `(1,0)` have `R,U,D` right/up/stretched-down steps. Its endpoint `(i,j)` satisfies

`i-1 = R+K D,    j=U-D`.                                      (3.1)

Hence its number of steps is exactly

`N=R+U+D=i-1+j-(K-2)D`.                                      (3.2)

For fixed endpoint, `N` is independent of the path only when `K=2`. Equivalently, if a linear coordinate `t=a i+b j` is required to increase by one on both `(1,0)` and `(0,1)`, then `a=b=1`; on `(K,-1)` its increment is `K-1`, which equals one iff `K=2`.

Thus the lazy-LPP clock was a `K=2` accident. Trying to generalize the theorem by pretending every admissible step consumes one common time unit is invalid.

The repair is to return to Seppäläinen's **original source coordinates** `(i,j)`, where the vertical increment of every admissible step is still in `{-1,0,1}`. The coupling needs only that row-crossing fact; it does not need endpoint-invariant path length.

**B1 outcome:** the naïve generalization is refuted exactly, and the obstruction identifies the correct category: source-coordinate last-passage shape rather than a unit-clock lazy walk.

## 4. General-`K` central saturation at zero vertical slope

Fix `K>=1`. Let the iid rates have nondegenerate law `Q` supported in `[r,1]`, where

`r=ess inf Q>0`.                                               (4.1)

Write `gamma_{K,Q}` for the source passage shape. Let `gamma_{K,r}` denote the homogeneous shape when every site rate is exactly `r`.

### Lemma 4.1 — central saturation for all fixed `K`

For every `x>0`,

`gamma_{K,Q}(x,0)=gamma_{K,r}(x,0)`.                           (4.2)

#### Upper bound

Couple both models with the same unit exponentials `lambda_{i,j}`. Since `alpha_j>=r`,

`lambda_{i,j}/alpha_j <= lambda_{i,j}/r`,

so every path has no larger disordered passage time than homogeneous rate `r`. Hence

`gamma_{K,Q}(x,0)<=gamma_{K,r}(x,0)`.                          (4.3)

#### Lower bound: near-minimum strips, with no atom at `r`

It is enough by homogeneity to work at `x=1`. Fix `epsilon>0` and strip half-width `M`. Since `r` is the essential infimum,

`q_epsilon=Q([r,r+epsilon])>0`.                               (4.4)

Disjoint row blocks of width `2M+1` are independent, and each is entirely in `[r,r+epsilon]` with probability `q_epsilon^(2M+1)>0`. Almost surely infinitely many such blocks occur. Fix one such block and call its center `a`.

For homogeneous rate `c`, let `H_{K,c}^{(M)}(n)` be the maximal passage time from `(1,0)` to `(n,0)` among `K`-admissible paths constrained to `|j|<=M`. Horizontal superadditivity and stationarity give a deterministic strip shape

`h_{K,c}^{(M)}=lim_{n->infty} H_{K,c}^{(M)}(n)/n`.             (4.5)

Moreover

`h_{K,c}^{(M)} up gamma_{K,c}(1,0)` as `M->infty`.             (4.6)

For completeness, (4.6) does not require an unproved localization assertion. A path from `(1,0)` to `(n,0)` has equal numbers `U=D` of up and stretched-down steps, while `n-1=R+K D`; hence `D<=floor((n-1)/K)`. Every finite endpoint path is therefore contained in a finite strip. For any fixed `n`, choosing `M>=floor((n-1)/K)` makes the constrained and unconstrained passage times identical. Superadditivity/Fekete plus the source moment bounds then let `n->infty`, giving (4.6).

Translate the constrained strip to the near-slow block centered at `a`. A finite connector reaches that block and another finite connector returns to row zero; the total horizontal overhead is at most `K|a|+O(M+1)` and is independent of the macroscopic endpoint. Inside the block,

`lambda_{i,j}/alpha_j >= lambda_{i,j}/(r+epsilon)`.            (4.7)

Because the exponentials are independent of the environment, the horizontally repeated constrained model on the selected random block has the same rate-`r+epsilon` strip shape. Consequently, after dividing by the total horizontal scale and sending it to infinity,

`gamma_{K,Q}(1,0)>=h_{K,r+epsilon}^{(M)}`.                     (4.8)

First `M->infty`, then `epsilon downarrow0`. Homogeneous exponential scaling gives

`gamma_{K,r+epsilon}(1,0)=gamma_{K,1}(1,0)/(r+epsilon)`,

so

`gamma_{K,Q}(1,0)>=gamma_{K,r}(1,0)`.                          (4.9)

Together with (4.3), this proves (4.2). `QED`

The key point is that exact minimum-rate rows are unnecessary for every `K`, not just `K=2`.

## 5. B19 — make the forced-crossing comparison algorithmic

Define

`mu_Q = E[1/r - 1/alpha_0]`.                                  (5.1)

For nondegenerate `Q`, `mu_Q>0`.

At a site on a row of rate `a>=r`, let

`W~Exp(a)`,
`B~Ber(1-r/a)`,
`E~Exp(r)`,

independently conditional on `a`, and set

`U=B E,    Z=W+U`.                                             (5.2)

Then

`Z~Exp(r)`, and `E[U|a]=1/r-1/a`.                             (5.3)

Indeed, for `s>=0`,

`E[e^{-sZ}|a] = a/(a+s) * [r/a + (1-r/a) r/(r+s)] = r/(r+s)`. (5.4)

Apply this independently at every lattice site conditional on the row environment. Because the conditional law of every `Z` is the same `Exp(r)` and does not depend on `a`, the whole `Z` field is iid homogeneous rate `r`.

Now take a maximizing disordered `K`-admissible path from `(1,0)` to a macroscopic endpoint `(floor(nx),floor(ny))`, chosen by a deterministic tie rule from the `W` field. The source step set (1.1) changes the row coordinate only by `-1,0,+1`. Therefore:

- if `y>0`, the path must visit every row `1,...,floor(ny)`;
- if `y<0`, it must visit every row `-1,...,floor(ny)`.

Select the **first visited site in each compulsory row**. These selected sites are distinct and are measurable with respect to the environment and `W`; their bonus variables `U` are conditionally independent.

Exactly as in the preceding `K=2` checkpoint, if

`d_j=1/r-1/alpha_j`,

then for any `eta>0` the centered selected bonuses satisfy the uniform conditional Chernoff bound

`P{sum(U_j-d_j)<=-eta m | environment,W}
 <= exp[-eta^2 r^2 m/4]`.                                     (5.5)

The spatial strong law gives the average of `d_j` over the compulsory rows converging to `mu_Q`, and (5.5) is summable. Evaluating the homogeneous `Z` field on the same disordered maximizing path therefore yields, for all source-shape points `(x,y)`,

`gamma_{K,r}(x,y) >= gamma_{K,Q}(x,y) + mu_Q |y|`.             (5.6)

The proof first holds on rational shape points and extends by the source continuity of `gamma_K`.

This is the crucial observation: **the comparison bonus counts net distinct rows, not the number of path steps.** Therefore the `K>=3` variable path length from (3.2) is irrelevant to the cusp mechanism.

**B19 outcome:** the general-`K` crossing decomposition is explicit and survives the exact source path geometry.

## 6. Convert the source-coordinate cusp into a flux plateau

Define ray shapes

`G_Q(v)=gamma_{K,Q}(1,v)`,
`G_r(v)=gamma_{K,r}(1,v)`,                                    (6.1)

for `v>-1/K`, and let

`G_0=G_Q(0)=G_r(0)`                                           (6.2)

by Lemma 4.1.

### 6.1 The homogeneous tangent is centered at `-K/2`

For iid rates, the environment is reversible. Source Lemma 9.1(ii) gives

`g_{K,r}(-s)=g_{K,r}(s)+K s`.                                 (6.3)

Thus

`h(s)=g_{K,r}(s)+(K/2)s`

is convex and even. Hence zero is a minimizer and

`-K/2 in partial g_{K,r}(0)`.                                 (6.4)

For a ray `v`, homogeneity puts the level-one boundary point at

`s_r(v)=v/G_r(v),    g_{K,r}(s_r(v))=1/G_r(v)`.               (6.5)

The supporting-line inequality from (6.4) gives

`1/G_r(v) >= 1/G_0 - (K/2) v/G_r(v)`,

or equivalently

`G_r(v) <= G_0(1+K v/2)`.                                    (6.6)

### 6.2 Disorder subtracts a two-sided linear cusp

Equation (5.6) at `(1,v)` and (6.6) give

`G_Q(v) <= G_0(1+K v/2) - mu_Q |v|`.                          (6.7)

For the disordered level-one boundary,

`s_Q(v)=v/G_Q(v),    g_{K,Q}(s_Q(v))=1/G_Q(v)`.               (6.8)

The exact secant identity is

`[g_{K,Q}(s_Q(v))-g_{K,Q}(0)]/s_Q(v)
 = [G_0-G_Q(v)]/(G_0 v)`.                                    (6.9)

For `v>0`, (6.7) and (6.9) imply

`secant >= -K/2 + mu_Q/G_0`.                                  (6.10)

For `v<0`, division by the negative `v` reverses the inequality and gives

`secant <= -K/2 - mu_Q/G_0`.                                  (6.11)

Convexity of `g_{K,Q}` now implies

`[-K/2-mu_Q/G_0, -K/2+mu_Q/G_0]
 subseteq partial g_{K,Q}(0)`.                                (6.12)

This is the exact general-`K` source-coordinate replacement for the special `K=2` lazy-walk cusp.

## 7. Main theorem candidate — every fixed `K` has an iid site-disorder plateau

### Theorem 7.1 (self-checked general-`K` plateau candidate)

Fix an integer `K>=1`. Let the source site rates be iid with a nondegenerate law `Q` supported in `[r,1]`, where `r=ess inf Q>0`. Define

`mu_Q=E[1/r-1/alpha_0] > 0`,

and

`delta_{K,Q}=mu_Q/gamma_{K,r}(1,0)
             =(1-r E[1/alpha_0])/gamma_{K,1}(1,0) > 0`.        (7.1)

Then the hydrodynamic flux satisfies

`f_{K,Q}(rho)=f_{K,Q}(K/2)`                                   (7.2)

for every density in

`[K/2-delta_{K,Q}, K/2+delta_{K,Q}] cap [0,K]`.                (7.3)

Equivalently, taking the safe symmetric half-width

`delta'_{K,Q}=min{K/2,delta_{K,Q}}`,                           (7.4)

the source flux has a nontrivial flat segment of radius `delta'_{K,Q}` around `K/2`.

#### Proof

The source duality is

`f_{K,Q}(rho)=inf_s {rho s+g_{K,Q}(s)}`.                       (7.5)

For every `rho` with

`|rho-K/2|<=delta_{K,Q}`

and `0<=rho<=K`, equation (6.12) gives `-rho in partial g_{K,Q}(0)`. Therefore `s=0` is a minimizer in (7.5), so

`f_{K,Q}(rho)=g_{K,Q}(0)`,

independent of `rho`. This proves (7.2)–(7.4). `QED`

### Scope accounting

- `K=1` is literature-known and earns no new fleet credit.
- `K=2` recovers and generalizes the preceding HARD7-03 theorem.
- The genuinely new fleet content of this run is the source-coordinate proof for **all fixed `K>=3`**.
- The exact binary `K=2` numerical certificate is unchanged, so the frozen metric correctly records no movement.

If independent audit and a stronger prior-art search confirm the argument, this would answer the flat-segment clause of Seppäläinen Problem 4 for iid site disorder under the source's positive lower-endpoint hypothesis. It would still not by itself close every clause of Problem 4.

## 8. B27 — swap the quantifiers: why the proof is uniform in the choice of fixed `K`

The failed instinct was to seek one `K`-independent unit-time path representation. B27 changes the quantifiers:

1. fix an arbitrary integer `K`;
2. use the exact source `K`-admissible geometry;
3. prove central saturation and the forced-row bonus for that `K`;
4. observe that neither argument requires a `K=2` path clock;
5. only then quantify over all fixed integers `K>=1`.

The only `K`-dependence that survives in the plateau radius is the homogeneous central shape constant `gamma_{K,1}(1,0)` and the symmetry center `K/2`. No step in the row-bonus estimate deteriorates merely because `K` is large.

This is stronger and safer than asserting a single simultaneous-in-`K` stochastic process statement. It proves a theorem for each fixed capacity and then quantifies over the integer parameter.

**B27 outcome:** succeeded; the exact fixed-`K` theorem glues across all integer capacities without changing the disorder coupling.

## 9. Counterexample-oriented stress tests

This run tried to break the argument at the three places most likely to hide a `K=2` assumption.

### 9.1 Variable path length

Refuted the false endpoint-invariant-length claim by (3.2). The general proof no longer uses path length.

### 9.2 Stretched steps skipping rows

They do not: `(K,-1)` changes the row coordinate by exactly `-1`. Thus a path with macroscopic vertical displacement must still visit every intermediate integer row. The coupling selects first visits and is unaffected by the horizontal stretch `K`.

### 9.3 Absence of a minimum-rate atom

The central-saturation proof uses finite **near-minimum** strips, not exact minimum rows. Essential infimum plus iid rows gives such strips at every fixed tolerance and width, and the limits are taken in the safe order: macroscopic horizontal length first, then strip width, then tolerance.

### 9.4 Randomly selected slow block

The block center depends only on the row environment. The exponential field is independent. For each fixed center the horizontal strip shape holds on a probability-one event; intersecting over countably many centers makes the statement valid for the environment-selected block as well.

### 9.5 Density-center sign

The source's exact reversible-environment identity (1.5), not an inferred particle-hole slogan, yields the `-K/2` supporting slope. Thus the dual flat segment is centered at `+K/2` exactly.

No counterexample to Theorem 7.1 survived these checks. This remains a self-check, not an independent audit.

## 10. Exact checker and archived output

Supporting finite/symbolic identities were checked exactly in:

- `artifacts/hard7_2026-09-18/HARD7-03/general_k_plateau_geometry_20260919T0325Z.py`;
- `artifacts/hard7_2026-09-18/HARD7-03/general_k_plateau_geometry_20260919T0325Z.out`.

The checker verifies:

1. the endpoint/path-length identity (3.2);
2. `K=2` is the unique capacity for which one linear coordinate gives unit increment on all three source step types after normalizing right/up increments;
3. the level-boundary secant identity (6.9);
4. the algebra converting the `-K/2` support line to (6.6);
5. the frozen binary certificate remains `500000/6578563` and exceeds `1/16` by exactly `1421437/105257008`.

The executed output ends

`ALL_EXACT_CHECKS_PASS = True`.

The checker certifies only these finite algebraic identities. Lemma 4.1, the conditional concentration/shape comparison, and Theorem 7.1 are theorem-sized mathematical arguments written on the page and still require independent audit.

## 11. Section-I state and next route

The frozen metric moved in the preceding run and is unchanged in this one. Therefore the current unchanged streak on the frozen metric is **one**, not three; Section I is not triggered.

This run changes the remaining obligation materially. The next run should **not** derive another `K=2` lemma. It should try to falsify or audit the new all-`K` theorem from a fresh angle before building on it. A different unused/recently nonrepeated triple should be selected, for example:

- **B6** deform from homogeneous/no-disorder to weak disorder and test whether the predicted positive cusp is compatible with perturbative current response;
- **B15** break spatial reversibility on purpose to isolate exactly which part of the center `K/2` argument fails outside iid/reversible environments;
- **B22** read failed/general-`K` attempts and citation chains around Sly/Bahadoran–Bodineau/Seppäläinen to determine whether the row-crossing comparison is known folklore or genuinely absent.

If the same substantive obligation remains unchanged for three runs, follow the normal Section-I stuck protocol rather than producing another certificate.

## 12. Capability statement

The actual model in this invocation is **GPT-5.6 Sol**. The reasoning-effort level is **UNVERIFIED**. The exposed scheduler/runtime surface still has no binding model selector, no reasoning-effort selector, no authenticated maximum-reasoning telemetry, and no guaranteed execution duration. GPT-6/maximum is therefore prompt-requested only; I do not claim it ran.

The repository records historical native task-edit failures of the form `You cannot modify this task`, including a P26 context, and also records that P26 later succeeded from another authorized context. A denied task requires an authorized owner/account/workspace context or platform support/ownership correction. Repository edits cannot repair scheduler ownership, and creating a duplicate task would violate policy. No schedule was created, modified, disabled, or re-enabled in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  canonical_target: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  frozen_metric: "rigorous certified lower bound L <= Delta_2(Q) for Q=1/2 delta_{1/2}+1/2 delta_1"
  before: 500000/6578563
  after: 500000/6578563
  movement: false
  unchanged_streak: 1
  methods: [1, 19, 27]
  source_scope_advance:
    prior: "self-checked iid site-disorder plateau theorem for K=2"
    after: "self-checked iid site-disorder plateau theorem for every fixed integer K>=1"
    new_credit_scope: "K>=3; K=1 known, K=2 prior HARD7-03"
  theorem_candidate:
    assumptions: "fixed K>=1; iid nondegenerate site rates Q subset [r,1], r=ess inf Q>0"
    central_saturation: "gamma_{K,Q}(x,0)=gamma_{K,r}(x,0)"
    crossing_comparison: "gamma_{K,r}(x,y)>=gamma_{K,Q}(x,y)+mu_Q |y|"
    mu_Q: "E[1/r-1/alpha_0]"
    subgradient: "[-K/2-mu_Q/G0,-K/2+mu_Q/G0] subset partial g_{K,Q}(0)"
    plateau_radius: "min(K/2,(1-r E[1/alpha_0])/gamma_{K,1}(1,0))"
    audit_status: "self-check only; no closure claim"
  exact_artifacts:
    - artifacts/hard7_2026-09-18/HARD7-03/general_k_plateau_geometry_20260919T0325Z.py
    - artifacts/hard7_2026-09-18/HARD7-03/general_k_plateau_geometry_20260919T0325Z.out
  exact_output_status: "ALL_EXACT_CHECKS_PASS = True"
  section_I_state: "not triggered; one unchanged metric run after prior movement"
  next_methods: [6, 15, 22]
  posted_changed: false
  results_changed: false
  queue_changed: false
  claim_changed: false
```

No shared-root ledger, public posting, email, Drive object, independent audit, closure state, or scheduler configuration was modified by HARD7-03 in this run.
