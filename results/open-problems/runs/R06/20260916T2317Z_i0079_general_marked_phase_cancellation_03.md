Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED** by runtime metadata — GPT-6 maximum was requested, but the exposed scheduler/runtime surface has no authenticated model-family selector or reasoning-effort selector, so I do not claim GPT-6 maximum. **NO MOVEMENT: active I0079 metric `R_unique = +infinity -> +infinity`; Section-B moves tried: #1 CHANGE THE CATEGORY, #20 FIND WHY THE ALGORITHM FAILS, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

Problem/source: Héctor Jardón-Sánchez, Sam Mellick, Antoine Poulin, Konrad Wróbel, *Exactness and the topology of the space of invariant random equivalence relations*, Question 2 (accepted 2026 version): “In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?” Intake I0079. **Status: PARTIAL; the full source question is not claimed closed.**

# R06 CLOSABLE OUTSIDE — I0079 run 3: general marked-lattice phase cancellation and a graph criterion for unique refined IBVTs

Run date: 2026-09-17 Asia/Jerusalem / 2026-09-16 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Repository continuity — I0056 remains rotated

The native task title/prompt still names Lyons--Peres Question 6.20 / I0056, but current repository state is later than that assignment. R06 already reached the six-unchanged-run rotation threshold on I0056 and preserved the handoff in

`runs/R06/20260916T2020Z_i0056_rotation_i0079.md`.

The canonical active claim is

`operations/claims/I0079.md`,

and the newest own report before this run is

`runs/R06/20260916T2218Z_i0079_global_unfolding_priorart_02.md`.

Therefore this run continues I0079 rather than silently restarting a rotated source. I0056 remains preserved as PARTIAL / audit-gated, including its exact frozen `H_{5,5}` value and all mixed-face handoff material.

Before new mathematics I reread/rechecked current `master` through the connector:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md` and `DEPLOYMENT.md`;
- canonical `operations/claims/I0079.md`;
- newest own R06 report;
- newest neighboring package `runs/R07/20260916T2226Z_i0077_log_periodic_pulses_06.md`;
- exact repository searches for I0079, R06-I0079 audits, P26 audit records, and the current model/deployment record;
- targeted intake/source/ownership hits in `probability_1000_intake_I_20260914/problems.jsonl`.

The large intake JSONL mirrors cannot be rendered row-by-row in one connector response; the active source row, ownership, duplicate attempts and exclusions were checked by exact/targeted queries. No other track's file was edited.

## 2. Fixed metric and audit state

Frozen group from the canonical claim:

\[
\Gamma=F_2\times F_2,
\]

with its standard product word metric, equivalently `T_4 x T_4` with the `l^1` graph metric.

Frozen refinement: every Bernoulli nucleus gets an iid continuous `Unif[0,1]` label and any distance tie is won by the nucleus with smallest label. This is an equivariant genuine-partition refinement permitted by the source. It is also exactly the tie convention used in the product-tree convergence paper.

Metric:

\[
R_{\rm unique}
=\sup\{R\ge1:\text{all subsequential refined BVT limits agree on every IRE cylinder supported in }B_R(e)\}.
\]

The first I0079 run proved `R_unique=+infinity`; run 2 kept it there. Hence

\[
\boxed{+\infty\longrightarrow+\infty.}
\]

This is the second consecutive unchanged I0079 run, so `unchanged_count = 2`. If the next I0079 run also has no metric movement, the installed three-run stuck protocol applies.

A fresh repository audit search found one independent OTHER-track audit that the preceding R06 report had not yet incorporated:

`R05-AUDIT-R06-I0079-PHASE-CANCELLATION-01-20260916T221717Z: PASS_CORE_MATH / SOURCE-HANDOFF_SCOPED / NOVELTY_UNVERIFIED`.

That audit covers the frozen phase-cancellation core, not the stronger general theorem proved below. No `P26-AUDIT-R06-I0079` record was found. Thus even the frozen subclass remains closure-gated by P26; the new general criterion needs its own independent audit before any closure/package claim.

## 3. Source statement and tie-refinement scope rechecked

Primary source rechecked on 2026-09-17:

`https://antoinegpoulin.github.io/pdf/exac.pdf`

Section 6 fixes a left-invariant proper metric on the countable group, defines the Bernoulli Voronoi tessellation from iid Bernoulli nuclei, notes explicitly that ordinary Voronoi cells can overlap on distance ties, and says the cells may be refined equivariantly to a genuine partition; random tie choice is given as an example, and other boundary-resolution methods are allowed. Subsequential weak limits as the Bernoulli intensity tends to zero are called ideal Bernoulli Voronoi tessellations.

The source still asks Question 2:

> In what generality can one say that there is a unique ideal Bernoulli Voronoi tessellation on a group?

It records Bhupatiraju's regular-tree uniqueness as the discrete benchmark. Therefore a theorem for a broad graph class or for products of trees is a source-valid PARTIAL answer, not closure of the open-ended full question.

## 4. Current primary literature — the exact general graph phase family

The decisive input is Matteo D'Achille and Ali Khezeli, *Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv:2606.30517 (June 2026, current v2 surfaced in the dated search).

Their Theorem 1.3 says, for a vertex-measured graph, that after choosing the natural integer radial shift, subsequential low-intensity Poisson nuclei converge precisely when:

1. the integer volume function is log-regularly-varying with a positive index `b`;
2. normalized ball measure converges weakly to a boundary probability `nu_0`;
3. the residual intensity phase converges, say `lambda_n F(n) -> exp(b xi)`.

Writing `p=exp(b)>1`, the limiting boundary signatures are iid `nu_0`, while the independent integer delays form a Poisson point process on `Z` with intensity

\[
\boxed{\beta^{(\xi)}(m)=(p-1)p^{m-1+\xi}.}
\tag{4.1}
\]

Their Remark 4.8 emphasizes that the **unrefined** vertex-measured IPVT generally can depend on the fractional phase `xi`; this dependence is known for regular trees. Their Lemma 4.9 proves asymptotic equivalence of Poisson and Bernoulli nuclei on the same vertex measure under its growth/square-mass condition; for counting measure the square-mass condition is automatic once the stated graph growth hypotheses hold.

This is exactly the shape needed for a general source-level tie-refined statement.

There is important close prior art. The same D'Achille--Khezeli paper proves phase independence for **edge-measured** graph IPVTs under additional hypotheses, via a continuous within-edge coordinate and a “magic telescopic sum.” Also D'Achille--Curien--Enriquez--Lyons--Ünel record Bhupatiraju's theorem that on a regular tree the restriction to vertices / Bernoulli model with iid continuous nucleus labels has a unique low-intensity limit, even though the corresponding unrefined graph IPVTs differ by phase. Thus the cancellation mechanism is not claimed new in spirit. The exact general iid-nucleus-label theorem below was not located in the checked literature; that is bounded negative evidence only, so publication novelty remains UNVERIFIED.

## 5. Move #1 — CHANGE THE CATEGORY: from graph delays to measure transport

The graph problem has a discrete nuisance: integer delays carry a fractional radial phase. The source-allowed iid tie labels supply exactly one continuous coordinate. Treat delay plus label not as two graph decorations, but as a single positive Poisson coordinate.

Let `H` be any measurable family of integer-valued normalized graph horofunctions / score functions

\[
h:V(G)\to\mathbb Z,
\]

let `nu_0` be a sigma-finite measure on `H`, fix `p>1`, and for `xi in R` consider a marked Poisson point process

\[
\Xi_\xi\subset H\times\mathbb Z\times[0,1)
\]

with intensity

\[
\nu_0(dh)\,(p-1)p^{m-1+\xi}\,du.
\tag{5.1}
\]

At a graph vertex `v`, rank an atom `(h,m,u)` lexicographically by

\[
(m+h(v),u).
\tag{5.2}
\]

This is exactly “distance/horofunction first, iid nucleus label second.”

Define

\[
\boxed{
T=T_\xi(m,u)
:=p^{m-1+\xi}\bigl(1+(p-1)u\bigr).
}
\tag{5.3}
\]

For fixed integer `m`, as `u` ranges over `[0,1)`, `T` ranges bijectively over

\[
I_m(\xi)=[p^{m-1+\xi},p^{m+\xi}),
\]

and

\[
dT=(p-1)p^{m-1+\xi}\,du.
\tag{5.4}
\]

The half-open intervals `I_m(xi)`, `m in Z`, partition `(0,infinity)`. Hence the Poisson mapping theorem turns (5.1) **exactly** into the phase-free intensity

\[
\boxed{\nu_0(dh)\,dT.}
\tag{5.5}
\]

No asymptotics or averaging are involved in this cancellation.

## 6. I0079-R06-T3 — general marked geometric-lattice phase cancellation

**STATUS: PROVED / AUDIT_PENDING / NOVELTY_UNVERIFIED.**

### Statement

Under the setup of Section 5, assume the winner at every graph vertex exists and only finitely many atoms attain the minimum unmarked score (the standard finite-competitor property in the graph IPVT limits under discussion). Then the entire iid-label-refined winner field, and therefore the induced partition / IRE, has the same law for every phase `xi`.

More strongly, every phase has a coupling through one common Poisson process

\[
\Pi\sim\operatorname{PPP}(\nu_0\otimes\operatorname{Leb}_{(0,\infty)})
\]

for which

\[
\boxed{
W(v)=\arg\min_{(h,T)\in\Pi} T p^{h(v)}.
}
\tag{T3.1}
\]

### Proof

Section 5 already proves that `(h,m,u) -> (h,T)` maps the marked phase-`xi` process to the same phase-free PPP `Pi` for every `xi`.

Fix `v`. Since `h(v)` is an integer,

\[
T p^{h(v)}
\in
[p^{m+h(v)-1+\xi},p^{m+h(v)+\xi}).
\tag{T3.2}
\]

For two atoms, if their first lexicographic coordinates `m+h(v)` differ, the two quantities in (T3.2) lie in disjoint ordered adjacent `p`-adic intervals, so their numerical order agrees with the integer-score order. If their first coordinates agree, multiplication by the common positive factor leaves the order of

\[
1+(p-1)u
\]

and hence the order of the tie marks `u` unchanged. Therefore

\[
(m_1+h_1(v),u_1)<_{\rm lex}(m_2+h_2(v),u_2)
\]

if and only if

\[
T_1p^{h_1(v)}<T_2p^{h_2(v)},
\]

apart from the null endpoint/mark-tie events. The finite-competitor hypothesis makes the minimum well-defined and the continuous marks make it unique almost surely. Thus (T3.1) gives exactly the refined winner at every vertex.

The same `Pi` is used simultaneously for all vertices, so equality is for the entire winner field, not only one finite cylinder. The right-hand side of (T3.1) contains no `xi`; hence the winner field and induced equivalence relation are phase-independent. `QED`

## 7. Move #20 — FIND WHY THE ALGORITHM FAILS: why unrefined phase dependence survives but refined dependence does not

D'Achille--Khezeli Remark 4.8 is the correct adversarial test: without the iid labels, the integer delay measure is

\[
\beta^{(\xi)}(m)=(p-1)p^{m-1+\xi},
\]

and different fractional `xi` are not related by an integer shift. The unrefined graph IPVT can therefore remember `xi`; regular trees really do.

The failure mechanism is now exact. If one tries to map only the integer delay `m` to a positive multiplicative coordinate, one gets a geometric lattice with gaps. The within-tie mark `u` fills precisely the missing interval

\[
[p^{m-1+\xi},p^{m+\xi}),
\]

and its Jacobian is exactly the mass `(p-1)p^{m-1+xi}`. Thus the label is not a cosmetic tie breaker: it is the continuous coordinate that removes the fractional lattice phase.

This also explains the close edge-measured prior art. In the edge-measured model, position inside an edge supplies a continuous within-layer coordinate; in the source's refined Bernoulli model, the iid tie label supplies the analogous coordinate. The exact models are different, but the cancellation geometry is closely related and must be cited as such.

## 8. Move #23 — DO WHAT THE PROPOSER DID NOT EXPECT: a broad sufficient criterion for unique refined IBVTs

The source asks “in what generality,” so a criterion is more valuable than another single graph.

### I0079-R06-T4 — graph criterion

**STATUS: PROVED conditional on the published convergence hypotheses; AUDIT_PENDING / NOVELTY_UNVERIFIED.**

Let `G` be a Cayley graph with counting measure. Assume:

1. the hypotheses of D'Achille--Khezeli Theorem 1.3 hold, so every phase subsequence of low-intensity vertex nuclei has boundary law `nu_0` independent of the fractional phase and integer delay intensity (4.1);
2. the hypotheses of their Poisson-versus-Bernoulli Lemma 4.9 hold (for counting measure its additional square-mass ratio is automatic under their graph-growth assumptions);
3. the source-allowed refinement is iid continuous labels on nuclei, with the smallest label winning a distance tie.

Then the refined Bernoulli Voronoi tessellations converge as the Bernoulli intensity tends to zero to a **unique** ideal Bernoulli Voronoi IRE.

### Proof

Take an arbitrary intensity sequence tending to zero. The radial normalization in Theorem 1.3 places the residual factor `lambda F(n)` in a compact multiplicative interval asymptotic to `[1,p]`; hence every subsequence has a further subsequence with a limiting phase `xi`.

For the corresponding Poisson nuclei, Theorem 1.3 gives the phase-`xi` boundary/delay process. Independently mark every nucleus by `Unif[0,1]`. Standard independent marking gives the marked limit (5.1). At a fixed finite vertex set, the set of candidates at or below the first nonwinning score is almost surely finite (the geometric tail of `beta^(xi)` gives finite mass below each integer cutoff), and continuous marks are almost surely distinct. Therefore the finite refined winner map is an almost-sure continuity functional of the marked point process; equivalently, one can use the finite-competitor argument already written in the preceding R06 report.

T3 now says that the limiting refined partition law is independent of `xi`.

Finally, D'Achille--Khezeli Lemma 4.9 couples Poisson and Bernoulli nuclei so that, on every fixed finite ball, the relevant nuclei agree with probability tending to one. Give matched nuclei the same independent labels. On that coupling event the refined partitions agree as well. Thus the Bernoulli model has the same phase-independent finite-cylinder limit.

Because every subsequence has a further subsequence converging to the same finite-cylinder law, the whole refined BVT family converges. Compatibility of the finite cylinders gives one limiting IRE. `QED`

### Scope warning

T4 is a **sufficient criterion**, not a characterization of all groups with unique ideal BVT. It does not answer the full open-ended source question. It also depends on the chosen source-admissible iid-nucleus-label refinement; no refinement-independent uniqueness theorem is claimed.

## 9. Concrete corollary beyond the frozen pair: all equal regular-tree products

D'Achille--Grebik--Khezeli--Recke--Wilkens, *Vanishing uniqueness thresholds in Voronoi percolation on products*, arXiv:2511.23317, provides an especially clean direct application.

For

\[
G=(T_d)^k,\qquad d\ge3,\ k\ge2,
\]

its Theorem 20 proves every subsequential boundary intensity has the form

\[
\beta_d^k\otimes\theta,
\qquad
\theta(m)=\theta(0)(d-1)^m.
\]

Theorem 25 then identifies every subsequential Bernoulli Voronoi **partition** limit with the ideal marked Poisson partition built from that intensity; crucially, their construction gives the nuclei iid `Unif[0,1]` labels and uses the minimum label to resolve equal score.

Writing `q=d-1`, T3 applies verbatim (the arbitrary multiplicative constant `theta(0)>0` is the same phase scale). Therefore:

\[
\boxed{
\text{For every }d\ge3,\ k\ge2,
\text{ the iid-nucleus-label refined BVT on }(T_d)^k
\text{ has a unique low-intensity partition/IRE limit.}
}
\tag{9.1}
\]

These graphs are Cayley graphs: for example `T_d` is the Cayley graph of the free product of `d` copies of `Z/2Z` with the involution generators, and products give the Cartesian product graph; for even `d`, the standard free-group realization is also available. Hence (9.1) gives an explicit infinite family of source-admissible groups. The frozen `F_2 x F_2` case is `d=4,k=2`.

This appears to move substantially beyond the regular-tree benchmark quoted by the source. I did not find a paper explicitly stating (9.1). However, the mechanism overlaps strongly with D'Achille--Khezeli 2026 and regular-tree phase cancellation is already known, so **novelty remains UNVERIFIED** pending a focused expert/prior-art audit.

## 10. Dated prior-art/search log — 2026-09-17 Asia/Jerusalem

Fresh searches/rechecks included:

- exact source phrase `"unique ideal Bernoulli Voronoi tessellation"`;
- `regular tree Bernoulli Voronoi tie breaker unique ideal`;
- `random labels ideal Bernoulli Voronoi tree`;
- D'Achille--Khezeli `Theorem 1.3 vertex-measured graphs phase xi`;
- D'Achille--Khezeli `beta^(xi)` / `Lemma 4.9 Poisson VS Bernoulli` / `Remark 4.8`;
- D'Achille--Grebik--Khezeli--Recke--Wilkens `Theorem 20`, `Theorem 25`, `same law`, and phase-parameter queries;
- later-author/current pages for Jardón-Sánchez, Mellick and Poulin.

What is known from the checked sources:

- Bhupatiraju: unique low-intensity iid-label Bernoulli Voronoi limit on a regular tree.
- D'Achille--Curien--Enriquez--Lyons--Ünel: unrefined regular-tree graph IPVTs are phase-dependent, but their restriction/tie-refined Bernoulli counterpart is phase-independent; they explicitly say it was unclear whether there were Cayley graphs other than trees with a unique low-intensity Bernoulli Voronoi limit (apart from trivial limits).
- D'Achille--Khezeli 2026: general vertex-measured phase family; unrefined phase dependence; Bernoulli/Poisson equivalence; separate edge-measured phase-independence theorem with a telescopic cancellation mechanism.
- Product-tree 2025: subsequential intensity classification and marked partition convergence for all equal regular-tree products.

No checked source states T3/T4 or the all-`(T_d)^k` refined partition uniqueness corollary. This is bounded negative evidence, not proof of novelty.

## 11. Exact-certificate decision

No new finite combinatorial claim was introduced in T3/T4. Their core is an exact change-of-variables theorem with a complete proof on the page. Creating another finite checker would not test the new infinite-volume implication and would violate the 90/10 instruction.

The pre-existing frozen finite certificate remains:

`artifacts/R06/20260916T2121Z_i0079_phase_cancellation_exact.py`

with its archived output; it checks the phase cancellation on finite `T_4 x T_4` cylinders but is explicitly not a substitute for the infinite convergence proof.

No new artifact was created this run.

## 12. Independent audit of newest R07 package

Newest neighboring package read:

`runs/R07/20260916T2226Z_i0077_log_periodic_pulses_06.md`.

Claim audited: `I0077-R07-T7`, the universal nonconfinement theorem for continuous 1-periodic log-pulsed parabolic-scale tubes satisfying the explicit duty-cycle spectral inequality.

Audit ID:

`R06-AUDIT-R07-I0077-T7-20260916T2317Z: PASS_SCOPED / NOVELTY_UNVERIFIED`.

### Audit details

I independently checked the following chain.

1. **Lamperti transform.** `Y_r=e^{-r/2}B_{e^r}` is stationary OU, and the moving Brownian tube becomes a period-one killed-OU domain in logarithmic time.

2. **Static spectral lower bound.** On `(-b,b)`, the weighted Rayleigh quotient plus the ordinary Dirichlet Poincare constant gives
\[
\lambda_b\ge \pi^2 e^{-b^2/2}/(8b^2).
\]
The factor `1/2` from the OU generator and the interval eigenvalue are consistent.

3. **Period contraction.** During every narrow subinterval of length at least `tau`, the moving killed kernel is dominated by the static kernel on `(-b,b)`; all remaining OU/killing factors are `L^2(gamma)` contractions. Thus every complete log-period loses at least `exp(-lambda_b tau)`, giving the claimed power survival estimate with exponent `kappa>1`.

4. **Continuum terminal times.** The modulus-of-continuity reduction is valid: for `t in [n,n+1]` and `s in [R_n,n]`, both shifted time pairs differ by at most one and lie in the blocks controlled by `M_n`. The reflection/Gaussian estimate gives a summable bound for `M_n`, while `R_n=O(log n)` converts the OU estimate to `n^{-kappa}(log n)^kappa`, summable exactly because `kappa>1`.

5. **FBM witness contradiction.** The proof needs no independence between the eventual-confinement event and the FBM witness time. Since `S_j -> -infinity` a.s., one deterministic witness index can be chosen with high probability past the fixed cutoff. Its forward increment process is standard Brownian motion by the FBM definition, so the terminal-time probability bound applies and contradicts the positive mass of the confinement event.

I found no mathematical gap in T7 at this scope. I did **not** audit the entire R07 Problem 7.8 program, its novelty, or a sharp Floquet classification. Therefore the verdict is PASS_SCOPED, not source closure.

## 13. Model / reasoning control and permission escalation

The limitation remains unresolved and is confirmed by the current deployment manifest. The exposed native task-control schema permits title/prompt, schedule, `timing_mode`, and enabled-state changes. It exposes **no model-family selector, no reasoning-effort selector, no authenticated runtime-model telemetry, and no guaranteed full-hour execution field**.

Thus `GPT-6 / maximum` can be requested in prompt text but cannot be authenticated or forced by this worker. A real fix requires either product/API support for task-level model and reasoning fields plus runtime telemetry, or an authorized owner/admin/platform-support context that can set those properties.

The historical P26 `You cannot modify this task` response is an ownership/context permission boundary, not a mathematical or prompt problem. Repository history records that P26 was later modified successfully from another authorized context. The legitimate workaround is therefore the owning authorized task-control context or platform support; duplicating the task or bypassing its permission boundary is not authorized. This run made no scheduler change.

## 14. Closure status

Frozen `F_2 x F_2` marked theorem:

- mathematics: PROVED in R06 reports;
- finite exact certificate: existing;
- independent OTHER-track audit: R05 PASS_CORE_MATH / SOURCE-HANDOFF_SCOPED;
- P26 audit: **NOT FOUND / PENDING**;
- novelty: UNVERIFIED with substantial close prior art.

New T3/T4 and the all-equal-tree-product corollary:

- mathematics: PROVED on the page conditional on the stated published convergence hypotheses;
- P26 audit: none;
- second independent audit: none specifically of the strengthened scope;
- novelty: UNVERIFIED / close overlapping prior art.

Therefore no source/subclass is declared closure-certified this run and no `paper_*` folder is created. The full source Question 2 remains PARTIAL.

## 15. Structured ledger delta

```yaml
ledger_delta:
  worker: R06
  source:
    authors: [Hector Jardon-Sanchez, Sam Mellick, Antoine Poulin, Konrad Wrobel]
    year: 2026
    title: Exactness and the topology of the space of invariant random equivalence relations
    locator: Question 2
    intake: I0079
  frozen_target: "iid-nucleus-label refined ideal BVT on F_2 x F_2 with the standard product word metric"
  metric: "R_unique: largest radius on which every subsequential refined BVT limit agrees on all IRE cylinders"
  before: +infinity
  after: +infinity
  movement: false
  unchanged_count: 2
  status: PARTIAL
  tried_moves: [1, 20, 23]
  new_claims:
    - id: I0079-R06-T3
      status: "PROVED / AUDIT_PENDING / NOVELTY_UNVERIFIED"
      statement: "For any integer-valued graph boundary phase family with marked PPP intensity nu_0(dh)(p-1)p^(m-1+xi)du, iid continuous tie labels admit an exact phase-free PPP coupling and the entire refined winner field is independent of xi."
    - id: I0079-R06-T4
      status: "PROVED conditional on published convergence hypotheses / AUDIT_PENDING / NOVELTY_UNVERIFIED"
      statement: "A Cayley graph satisfying D'Achille--Khezeli Theorem 1.3 and Bernoulli-equivalence hypotheses has a unique iid-nucleus-label refined ideal Bernoulli Voronoi IRE."
    - id: I0079-R06-COR-TREE-PRODUCTS
      status: "PROVED from T3 plus published Theorems 20/25 / AUDIT_PENDING / NOVELTY_UNVERIFIED"
      statement: "For every d>=3 and k>=2, the iid-nucleus-label refined Bernoulli Voronoi tessellation on (T_d)^k has a unique low-intensity partition/IRE limit."
  exact_evidence:
    - "complete change-of-variables and winner-order proof in Sections 5-9 of this immutable report"
    - "existing finite checker artifacts/R06/20260916T2121Z_i0079_phase_cancellation_exact.py and archived output for frozen T_4 x T_4"
    - "D'Achille--Khezeli arXiv:2606.30517 Theorem 1.3, Remark 4.8, Lemma 4.9"
    - "D'Achille--Grebik--Khezeli--Recke--Wilkens arXiv:2511.23317 Theorems 20 and 25"
  audit_ids:
    - "R05-AUDIT-R06-I0079-PHASE-CANCELLATION-01-20260916T221717Z: PASS_CORE_MATH / SOURCE-HANDOFF_SCOPED / NOVELTY_UNVERIFIED"
    - "R06-AUDIT-R07-I0077-T7-20260916T2317Z: PASS_SCOPED / NOVELTY_UNVERIFIED"
  remaining_obligation: "Obtain P26 audit for the frozen I0079 theorem; independently audit strengthened T3/T4 scope; resolve novelty against D'Achille--Khezeli 2026 and Bhupatiraju/regular-tree literature; full source Question 2 remains open-ended. If next R06 metric is unchanged, invoke the formal three-run stuck protocol."
  closure: false
```

## 16. Next attack if I0079 continues

Because `R_unique` is already infinite, another theorem that merely restates phase cancellation does not move the frozen metric. If the next run cannot create a genuine closure event (most naturally, a returned P26 audit plus source-scope/novelty resolution), it reaches the three-run unchanged trigger and must be a formal stuck/thinking run rather than another lemma.

Unused-method candidates for that next run, if needed:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** move from equal tree products to an unequal-growth product and identify exactly where the single-base geometric ladder breaks;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** allow boundary law or growth base to depend on an orbit/type and test whether one scalar mark still unfolds all phases;
- **#26 HUNT THE SPORADIC CASE:** search for a source-valid Cayley graph satisfying Theorem 1.3 but with multiple exponential lattice bases, where iid-label phase cancellation can fail.

Those attacks target the actual boundary of T4, not another re-proof of the already infinite frozen metric.