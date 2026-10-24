Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated applied-reasoning telemetry, so I do not claim GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: explicit certified bracket width `W=4.4898-3.52=0.9698 -> 0.9698`. Methods actually used: B20 FIND WHY THE ALGORITHM FAILS, B30 ONE SCALE AT A TIME, B18 SAY IT IN ANOTHER LANGUAGE.**

# PROB10-04 run 1 — a universal clause-local second-moment barrier and the full-component quotient route

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **source OPEN / PROB10-04 PARTIAL**.

The source problem is the classical independent-clause random 3-SAT model fixed by the owner: `n` Boolean variables, `m=floor(alpha n)` clauses, each clause selecting three distinct variables uniformly and then independent uniform signs. The target is the asymptotic satisfiability transition. This report distinguishes (i) a sharp window around an `n`-dependent center from (ii) convergence/identification of a fixed limiting threshold.

The main mathematical outcome of this run is not an endpoint improvement. It is a rigorous route theorem: **ordinary Paley--Zygmund second moments based on any fixed clause-local multiplicative weight depending only on the number of true literals are exponentially obstructed already below the known `3.52` lower bound. Moreover, dividing by any solution-graph ball of radius `R=o(n/log n)` cannot remove that obstruction.** This forces the weighted-count route to use genuinely nonlocal cluster information. I then give an exact full-component quotient that cancels every same-cluster pair, together with the precise remaining lemma needed for source progress.

## 1. Continuity, handoff, ownership, and nonduplication

The owner-directed `operations/PROB10_2026-09-20.md`, current root `POSTED.md`, current owner directive, canonical claims, and newest neighboring 3-SAT reports were recovered before research.

### HARD7-06 handoff

Before switching targets I wrote the required immutable handoff

`runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`

at commit `0c0de277ee50043bf3d4470a841d613f73a8ff12`.

It preserves the actual latest HARD7-06 target `F0095` (ordinary sparse Erdos--Renyi 3-colourability threshold-location), the frozen metric `W_3<=0.6565076260769`, and the exact binary-cascade theorem `5.03<beta_bin<5.04` with divergent negative moments above `beta_bin`. None of that work is relabelled as random 3-SAT progress.

### Historical parent ownership

`operations/claims/F0097.md` is the historical canonical parent claim owned by R03. R03's terminal report

`runs/R03/20260918T0318Z_49_third_stuck_handoff_rotation_hold_7a31.md`

records the third stuck episode and hands F0097 off. I retained all of its failures rather than restarting them. In particular, I do not retry: one-variable cavity iteration; fractional solution-count martingales; randomized booster replacement; loose-hypertree transfer; positive-temperature/free-energy compactification; or bounded-excess minimal-UNSAT enumeration below the pure-literal threshold. The last of these collides with Scott--Sorkin and ceases to control the extensive core above the pure-literal threshold.

The scoped PROB10-04 route was reserved create-only at

`operations/claims/PROB10-04.md`

commit `b45d6cc82ca768263ff3dc5275e9006b0080d335`.

### Neighboring active T04 route

The newest related report

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T02-26-40__t04_four_parameter_branching_index.md`

pursues a **constructive** Hajiaghayi--Sorkin refinement. It derives a four-parameter local degree state and branching-corrected polarity index. This run does not duplicate that route. PROB10-04 is scoped to **cluster-aware weighted counting / overlap variational control**.

## 2. Source status and frozen metric

The 2025 ESA paper of Caragiannis--Gravin--Jiang explicitly distinguishes its `k`-wise-independent clause model from the classical mutually independent model. Its introduction states for the classical model that the small-`j` threshold remains open, with `r_3>=3.52` and `r_3<4.49`; its `~4.26` figure is identified as numerical/physics evidence rather than a proof. Source:

- https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103

The original explicit endpoint sources retained here are:

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, https://arxiv.org/abs/math/0310193;
- Diaz--Kirousis--Mitsche--Perez-Gimenez, *A new upper bound for 3-SAT*, DOI `10.4230/LIPIcs.FSTTCS.2008.1750`, proving UNSAT w.h.p. at density at least `4.4898`.

A 2026 current-status check also finds no small-`k=3` threshold identification in Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited* (published online 27 March 2026, DOI `10.1017/S0963548326100406`). Carenini, ECCC TR26-145, published 16 August 2026, proves an `O(n/log n)` **scaling-window width** for every fixed `k>=3`; that does not imply that the window centers converge.

I therefore freeze the explicit source-normalized numerical metric

`alpha_L=3.52`, `alpha_U=4.4898`,

and

`W := alpha_U-alpha_L = 0.9698`.

This run gives

`W: 0.9698 -> 0.9698`.

No physics decimal, finite instance, or auxiliary route theorem is substituted for endpoint movement.

## 3. B20 — test the simplest weighted second moment and classify exactly why it fails

The cluster-aware priority suggests first asking whether a simpler clause-local weight can already suppress the dangerous high-overlap pairs. The class below contains the standard true-literal-count tilts used in weighted second-moment work, but I do **not** claim the category itself is new; Achlioptas--Peres and subsequent second-moment frameworks are prior art for weighted satisfying-assignment counts.

Fix constants

`u=w_1>0`, `v=w_2>0`, `w=w_3>0`, `w_0=0`.

For a formula `F` and assignment `sigma`, let `N_C(sigma)` be the number of literals of clause `C` made true by `sigma`, and define

`W_F(sigma)=prod_{C in F} w_{N_C(sigma)}`,

`X_w(F)=sum_sigma W_F(sigma)`.

Because `w_0=0` and all three satisfying weights are positive,

`X_w(F)>0` iff `F` is satisfiable.

### 3.1 First moment

For any fixed assignment the three literal truth values in a random proper clause are independent fair bits because the clause signs are independent. Hence exactly

`A := E[w_{N_C(sigma)}] = (3u+3v+w)/8`,

and

`E X_w = 2^n A^m`.

### 3.2 Pair-overlap exponent

Take two assignments with agreement fraction `q`. In the with-replacement asymptotic one-clause model, a single literal has truth pair

`(1,1)` with probability `q/2`,
`(0,0)` with probability `q/2`,
`(1,0)` and `(0,1)` each with probability `(1-q)/2`.

Let

`g(q)=E[w_{N_C(sigma)}w_{N_C(tau)}]`.

For the exact proper-clause model, choosing three distinct variables rather than three with replacement changes this bounded one-clause expectation by `O(1/n)` uniformly in the overlap count: couple the two samplers until the with-replacement sample has a repeated variable, an event of probability at most `3/n`. Since `m=Theta(n)`, this is only an `O(1)` correction to the logarithm of a pair contribution and does not alter the exponential rate below.

There are `2^n binom(n,qn)` ordered pairs with overlap `qn`, so the normalized second-moment exponential rate is

`Phi_alpha(q)=H(q)-log 2 + alpha log(g(q)/A^2)`,

where `H(q)=-q log q-(1-q)log(1-q)`.

At independent overlap `q=1/2`, exact symbolic expansion gives

`g(1/2)=A^2`,

and, crucially,

`g'(1/2)=3(u-v-w)^2/32`.                                      (3.1)

Thus

`Phi_alpha(1/2)=0`,

`Phi_alpha'(1/2)=alpha*g'(1/2)/A^2 >=0`.

If `u != v+w`, the derivative is strictly positive. Therefore for every fixed `alpha>0` there is a `q>1/2` sufficiently close to `1/2` with

`Phi_alpha(q)>0`.

So the normalized second moment grows exponentially and the ordinary Paley--Zygmund route fails.

**Necessary stationarity condition:** the only remaining fixed clause-local weights satisfy

`u=v+w`.                                                       (3.2)

### 3.3 The identical-pair obstruction after stationarity

At `q=1`, the two assignments are identical and

`g(1)=(3u^2+3v^2+w^2)/8`.

Impose (3.2) and put `t=v/w>0`; the overall scale of weights cancels. Then

`R_1(t):=g(1)/A^2 = 4(3t^2+3t+2)/(3t+2)^2`.                   (3.3)

Differentiate:

`R_1'(t)=12(t-2)/(3t+2)^3`.                                    (3.4)

Hence the unique minimum occurs at `t=2`, i.e. at the weight ratio

`u:v:w = 3:2:1`,

and

`min_{t>0} R_1(t)=5/4`.                                        (3.5)

The identical-pair contribution alone has normalized exponential rate

`Phi_alpha(1)=-log 2 + alpha log R_1(t)`.

Consequently a necessary condition for a bounded/subexponential normalized second moment in this entire fixed-weight class is

`alpha <= log(2)/log(5/4) = 3.1062837195...`.                  (3.6)

At the already-rigorous source lower endpoint `alpha=3.52`, even the optimally tuned stationary weight has diagonal exponent

`-log 2 + 3.52 log(5/4) = 0.0923181200... >0`.                 (3.7)

### Auxiliary theorem 3.1 — clause-local barrier

For the classical proper random 3-SAT model, no **fixed positive clause-local multiplicative weight depending only on the number `1,2,3` of true literals** can yield a bounded or subexponential normalized ordinary second moment at density `3.52`. If it fails (3.2), an off-diagonal overlap immediately has positive exponent; if it satisfies (3.2), the identical-pair contribution has positive exponent by (3.5)--(3.7).

This is a theorem about this proof mechanism, **not** a theorem about the satisfiability threshold. The weighted-second-moment category is established prior art; a bounded search did not locate this exact optimized `5/4` route identity, but I make no novelty or priority claim from that negative search.

## 4. B30 — local cluster normalization cannot repair an exponential overlap defect

A natural reaction to Theorem 3.1 is to divide each assignment weight by the size of a local piece of its solution cluster. This run tests that idea at all submesoscopic radii simultaneously.

Let `G_F` be the graph whose vertices are satisfying assignments of `F`, with edges between Hamming-distance-one assignments. Let

`B_R^F(sigma)`

be the graph-distance-`R` ball around `sigma` in `G_F`. Define the locally normalized count

`X_{w,R}(F)=sum_sigma W_F(sigma)/|B_R^F(sigma)|`.

Any radius-`R` solution-graph ball lies inside the ambient Hamming ball, hence

`1 <= |B_R^F(sigma)| <= b_R(n):=sum_{j=0}^R binom(n,j)`.

Pointwise in `F`,

`X_w(F)/b_R(n) <= X_{w,R}(F) <= X_w(F)`.                       (4.1)

Therefore

`E[X_{w,R}^2]/E[X_{w,R}]^2 >= b_R(n)^(-2) * E[X_w^2]/E[X_w]^2`. (4.2)

If

`R=o(n/log n)`,

then

`log b_R(n)=o(n)`

(for example from the standard Hamming-ball bound `b_R(n) <= (R+1)(en/R)^R` when `R<=n/2`). Thus a positive exponential second-moment rate for `X_w` survives unchanged at exponential scale after the local normalization.

Combining this with Theorem 3.1 gives:

### Auxiliary theorem 4.1 — submesoscopic cluster-ball no-go

At density `alpha=3.52`, for every fixed positive clause-local weight triple `(u,v,w)` and every `R=o(n/log n)`, the locally cluster-normalized count `X_{w,R}` still has exponentially diverging normalized second moment.

This is stronger than a failure of radius one or any fixed radius. It says that a cluster correction with only `exp(o(n))` dynamic range cannot pay an `exp(cn)` overlap defect. In particular, the weighted route must access genuinely mesoscopic/macroscopic cluster size or a different global statistic.

Carenini's 2026 `O(n/log n)` scaling-window theorem is logically different and does not prove anything about solution-graph radius. The coincident `n/log n` scale in the crude Hamming-ball estimate above is recorded only as a scale comparison, not as an identification of the two phenomena.

## 5. B18 — rewrite the count in the correct category: one unit per full solution component

The previous theorem says that approximating cluster size by a small Hamming ball is structurally insufficient. The natural exact object is therefore the whole connected component.

For each satisfying assignment `sigma`, let `K_F(sigma)` be its full connected component in `G_F`, and define

`Q(F):=sum_{sigma in Sol(F)} 1/|K_F(sigma)|`.

Then exactly

`Q(F)=# {connected components of G_F}`.                          (5.1)

Hence

`Q(F)>0` iff `F` is satisfiable.

This count has an exact cancellation absent from assignment counting. Expand

`Q(F)^2 = sum_{sigma,tau in Sol(F)} 1/(|K_F(sigma)||K_F(tau)|)`.

The contribution from pairs lying in the same component is

`sum_K sum_{sigma,tau in K} 1/|K|^2 = sum_K 1 = Q(F)`.          (5.2)

Thus **every same-cluster pair, including the entire diagonal/high-overlap multiplicity that produced (3.6), collapses to one unit per component.** Only cross-component pairs remain in the genuinely quadratic part.

There is also an exact random-representative representation. Give every truth assignment an independent continuous mark. In every nonempty solution component select the solution with the smallest mark. Each component contributes exactly one representative, and conditional on `F`,

`P(sigma is its component representative | F, sigma in Sol(F)) = 1/|K_F(sigma)|`.

Equivalently,

`1/|K| = integral_0^1 t^{|K|-1} dt`,                            (5.3)

which turns the reciprocal component size into a one-parameter generating function. These identities suggest two possible analytic entrances: component exploration with a random minimum mark, or a generating-function interpolation in the component size.

### Why this is genuinely different from the killed R03 routes

The R03 cavity/martingale attempts weighted or compared **assignments/formulas** while paying a local or mesoscopic correlation cost. The new quotient changes the counted object from assignments to connected components and cancels same-component multiplicity exactly before any overlap estimate. It also does not duplicate NM13-06's constructive degree-selection algorithm.

### Exact missing lemma

To turn (5.1)--(5.3) into a source lower-bound improvement, one needs a global theorem for some explicit `alpha>3.52`, for example:

1. a lower bound on `E Q(F)` of the correct exponential or nonvanishing scale; and
2. a cross-component estimate strong enough that

`E[Q(F)^2] <= C (E Q(F))^2`                                    (5.4)

with `C` independent of `n` (or another quantitative form sufficient for a positive SAT probability).

Then Paley--Zygmund would give `P(F SAT)>=1/C`; combined with the classical sharp-threshold theorem, this could transfer to w.h.p. satisfiability at a slightly smaller fixed density and move `alpha_L`. I do **not** claim (5.4).

The key remaining obstruction is now sharply localized: distinct components can still contain high-overlap assignments. A proof must show that their weighted cross-component contribution is small, or that distinct components are sufficiently separated in the typical random formula. Mere local-ball control cannot do this by Theorem 4.1.

A useful deterministic first observation for the next run is the following. If two satisfying assignments differ on a set `S` and **no clause contains two variables from `S`**, then the entire coordinate subcube between them is satisfying: a clause containing no changed variable is constant along the subcube, while a clause containing exactly one changed variable is satisfied at both endpoint values, so one of its fixed literals must cover the endpoint where the changed literal is false. Therefore the two assignments lie in the same component. Hence two distinct components at Hamming difference set `S` require at least one clause meeting `S` in at least two variables. This is far too weak by itself, but it identifies the next object: the dependency hypergraph of multi-hit clauses on `S`; a genuine separation proof should force a cyclic/locked substructure rather than just one multi-hit clause.

## 6. Negation tests / three-route comparison

The run deliberately tried three materially different attacks rather than producing another unchanged threshold checker.

### Route A — fixed clause-local weights

**Test:** optimize every positive weight triple, not a sampled family.

**Outcome:** exact no-go. Either `u!=v+w` and the independent-overlap point has positive outgoing derivative, or `u=v+w` and the identical-pair ratio is at least `5/4`. This caps the ordinary second-moment mechanism at `3.1062837...`, below `3.52`.

### Route B — local cluster-size division

**Test:** allow any solution-graph radius `R=o(n/log n)` instead of just radius one.

**Outcome:** exact no-go at exponential scale. The correction changes the normalized second moment by at most `exp(o(n))`, while Route A's obstruction is `exp(cn)`.

### Route C — full-component quotient

**Test:** quotient by the exact connected component instead of approximating it locally.

**Outcome:** survives the two no-go results. Equation (5.2) deletes the whole same-cluster pair multiplicity exactly. The unpaid obligation is now cross-component geometry / expectation of reciprocal component sizes. No source endpoint is claimed moved.

This is the useful research delta of the run: the search space has been reduced from generic weighted second moments to genuinely nonlocal cluster quotients or equivalent exponential-range statistics.

## 7. Prior-art boundary

The following literature is relevant and prevents overclaiming:

- Achlioptas--Peres (JAMS 2004), *The threshold for random k-SAT is 2^k log 2 - O(k)*, already develops weighted second moments for random k-SAT. Thus “weight assignments by satisfied-literal statistics” is not new.
- Maneva--Sinclair, *On the Satisfiability Threshold and Clustering of Solutions of Random 3-SAT Formulas* (TCS 2008; arXiv:0710.0805), proves that for density at least `4.453` random 3-SAT has no nontrivial core assignments. This is an explicit warning that a whitening/core label is not automatically the correct cluster quotient for `k=3`.
- Achlioptas--Ricci-Tersenghi and later solution-space geometry work establish clustering phenomena in other regimes / larger `k`; those results do not supply (5.4) for classical `k=3`.
- Carenini 2026 controls the **density scaling window**, not the solution-component second moment or convergence of its center.

A bounded search did not find a source that states the exact `5/4` optimization (3.5) or the radius transfer (4.2) in this form. That absence is **not** a novelty certificate. Both are recorded as auxiliary route theorems pending independent review, not as paper-ready claims.

## 8. Exact checker and actual test

The idea was written before code at

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-19T23-54-00Z__clause_local_weight_barrier_idea.md`

commit `3d79855fe76ed72fc2d50bde34b816261bebaf9d`.

Exact symbolic checker:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-19T23-57-00Z__clause_local_weight_barrier_exact.py`

commit `3dfe6749edc9f7ccf7f006a1e98faa97203f9952`.

Archived output:

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-19T23-57-00Z__clause_local_weight_barrier_exact.out`

commit `9c6dd5e9280fa1845c99447c000b3b3e09f0802c`.

The checker verifies symbolically, with exact rational algebra,

- `g(1/2)=A^2`;
- `g'(1/2)=3(u-v-w)^2/32`;
- the stationary reduction (3.3);
- derivative (3.4);
- exact minimum `R_1=5/4`;
- and the strict numerical comparison `log(2)/log(5/4)<3.52`.

The archived run ends

`ALL_EXACT_CHECKS_PASS = True`.

The decimal logarithms are orientation only; the algebraic identities and rational minimization are exact. This is a self-check, not an independent audit.

## 9. Source metric and auxiliary delta

### Source-level metric

- before: `[3.52,4.4898]`, width `0.9698`;
- after: `[3.52,4.4898]`, width `0.9698`;
- source movement: **NONE**;
- source status: **OPEN**.

### Auxiliary mechanism progress

- fixed clause-local weighted second moments: **unclassified -> exact universal obstruction at alpha>log2/log(5/4)=3.1062837...** within the stated fixed-weight class;
- local cluster correction: **radius-one idea -> all `R=o(n/log n)` ruled out at exponential scale**;
- nonlocal route: **generic “cluster-aware count” -> exact full-component quotient (5.1), exact same-component cancellation (5.2), and explicit missing cross-component lemma (5.4)**.

These auxiliary changes are not converted into a fake threshold improvement.

## 10. Next bounded mathematical obligation

The next run should stay on PROB10-04 and attack one of two genuinely nonlocal subproblems, not return to clause-local weighting:

1. **Component separation via the difference-set dependency hypergraph.** For a pair of satisfying assignments with difference set `S`, identify the minimal cyclic/locked multi-hit-clause structure necessary for different Hamming-one components and perform a first-moment bound on such structures for `|S|` up to a mesoscopic scale.
2. **Representative interpolation.** Use (5.3) or iid minimum marks to derive a tractable annealed pair functional for component representatives, retaining a rigorous finite-to-infinite error. The target is a cross-component overlap exponent, not another unweighted assignment-pair exponent.

A success must improve the explicit source bracket or prove a source-relevant convergence statement. Another conditional cluster lemma with the same unpaid global cross-component error is not enough.

## ledger_delta

```yaml
ledger_delta:
  worker: PROB10-04
  native_history: HARD7-06
  target: classical_random_3sat_threshold
  model: "m=floor(alpha n), iid proper 3-clauses, 3 distinct variables, independent uniform signs"
  source_status: OPEN
  worker_status: PARTIAL
  source_metric:
    name: explicit_certified_threshold_bracket_width
    before: "[3.52,4.4898], W=0.9698"
    after: "[3.52,4.4898], W=0.9698"
    movement: NO_SOURCE_METRIC_MOVEMENT
  methods:
    - B20_clause_local_weight_failure
    - B30_submesoscopic_cluster_radius_failure
    - B18_full_component_quotient
  auxiliary_results:
    clause_local_barrier: "alpha <= log(2)/log(5/4)=3.1062837195... necessary for ordinary second moment in fixed positive true-count weight class"
    cluster_radius_barrier: "R=o(n/log n) local-ball normalization cannot remove exponential second-moment failure"
    component_identity: "Q=sum_sigma 1/|K(sigma)|=#components; same-component pair contribution to Q^2 equals Q"
  exact_checker: "artifacts/prob10_2026-09-20/PROB10-04/2026-09-19T23-57-00Z__clause_local_weight_barrier_exact.py"
  exact_output: "ALL_EXACT_CHECKS_PASS = True"
  remaining_obligation: "control E[Q] and cross-component representative overlap strongly enough to move alpha_L above 3.52 or otherwise narrow the exact-source threshold problem"
  closure: false
```
