Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: I0076 remains OPEN / PARTIAL / RETIRED-HANDOFF at the historical carried 2/4, with no surviving frozen counterexample candidate; admission `E_ready: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, every `k=2` weak-dual witness supported on pair-atoms whose support graph is a forest is impossible at the universal two-coordinate constant from Talagrand Theorem 10.6; in particular, for `n=3`, any two-atom witness with both atoms supported on at most two coordinates is eliminated. Methods #1 CHANGE THE CATEGORY, #11 DUALIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

# R15 successor screen — forest obstruction for `k=2` Talagrand dual witnesses

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All new mathematical statements below are **SELF_CHECK_ONLY** unless explicitly identified as source material. The proofs are written on the page. No independent fleet audit is claimed, and no novelty claim is made.

## 1. Continuity: I0076 remains retired, source-exact, and unreopened

I reread the campaign roots `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the owner directive `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, and the current implementation manifest `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`. I also recovered the newest R15 report

`runs/R15/20260918_1354Z_successor_screen_f0111_moment_ratio_c1_m59j.md`

and the last neighboring R20 F0111 handoff

`runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`.

The exact original source was rechecked at arXiv v4:

- Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4.
- Definition 2.1: FBM means Brownian future paths from random origins tending to `-infinity`; BBM is the time-reversed analogue; 2BM means that at one random origin the two centered half-paths are independent **standard Brownian motions**.
- Problem 7.2: if `X` is FBM and BBM and there exists a random time `T` such that the complete centered forward and backward half-paths at `T` are independent, must `X` be 2BM?

The source does **not** assume that `T` is a stopping time and does **not** separately assume that either seam half is Brownian. I have not substituted deterministic-time independence, a stopping-time hypothesis, or Problem 7.5.

The six-run I0076 handoff remains controlling. The Theorem-6.1-derived candidate was eliminated because no source-valid independent seam survived. The later Brownian-prefix/Bessel candidate satisfied the first three intended features but was then proved actually 2BM, so it was eliminated as a counterexample. There is presently **no surviving frozen candidate**. The copied-continuous-Brownian-cell construction remains an architecture only. Therefore the historical track value `2/4` is carried only as the retired handoff value; it is not a claim that an active frozen candidate currently has two certified obligations.

Fresh exact-problem searches dated 2026-09-18 recovered the original paper and mirrors/citation pages, but I found no accessible later primary source explicitly claiming to settle exact Problem 7.2. This is bounded negative search evidence only, not a worldwide openness certificate.

The queue and compact ledger still expose no newly certified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successor available to R15. I therefore make no claim file and do not promote any PENDING item to READY. Admission remains

`E_ready = 0 -> 0`.

---

## 2. Retained screen: exact Talagrand source and what is already known

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9 (`F0111`). For an up-class `A` on a finite set `S`, hazard coordinates `t=(t_i)` correspond to independent inclusion probabilities

`P_t(i in X) = 1-exp(-t_i)`, 

and

`F_A(t) = -log(1-zeta_t(A)).`

Talagrand calls a function a polynomial when

`P(t)=sum_{I subset S} beta_I t_I`, `beta_I>=0`, `beta_emptyset=0`.

Definition 10.1 says that `A in C_gamma` if for every base point `q>=0` there is such a positive multilinear polynomial with

`F_A(t) <= P(t)` for all `t>=0`,

and

`P(gamma q) <= gamma F_A(q)`.

Problem 10.9 asks whether one universal `gamma>0` works for every cardinality threshold

`A_{n,k}={X subset [n]: |X|>=k}`.

Two source facts matter below.

1. Proposition 10.2 gives the nonempty-set endpoint in `C_1`.
2. Theorem 10.6 proves that there exists a universal `gamma_0>0` for which the all-elements class `A={S}` belongs to `C_{gamma_0}` for every finite `S`. Theorem 10.7 reduces this endpoint to the two-variable function

`Phi(u,v)=-log(exp(-u)+exp(-v)-exp(-u-v))`.

Talagrand explicitly says it would be interesting to know whether the endpoint theorem holds with `gamma=1`; his proof only supplies some universal positive constant. I do not strengthen that source theorem.

The latest R15 work proved, self-check only, an exact `C_1` certificate for the special homogeneous `n=3,k=2` base points. That does not cover heterogeneous bases and does not settle Problem 10.9.

A fresh literature check dated 2026-09-18 recovered Talagrand's primary PDF, DeMarco--Kahn (2015), Frankston--Kahn--Park (2022), and Warnke (2024). Frankston--Kahn--Park explicitly concerns a different Talagrand threshold formulation (weakly `p`-small versus `p`-small, with a pair-supported test case), not the exact Definition-10.1 positive-polynomial `C_gamma` statement above. I found no accessible later theorem explicitly resolving Problem 10.9 as stated. Again, this is bounded negative evidence rather than an exhaustive novelty/open-status certificate.

---

## 3. Method #1 — CHANGE THE CATEGORY: a forest inequality for the `k=2` hazard

For `k=2`, write

`F_{n,2}(q) = -log P_q(N<=1)`,

where `N` is the number of included coordinates. For a pair `{i,j}`, the trace threshold is the two-coordinate all-elements class and its hazard is

`Phi(q_i,q_j) = -log(exp(-q_i)+exp(-q_j)-exp(-(q_i+q_j))).`

The new observation is that pair hazards are controlled by **forest combinatorics**.

### Theorem R15-F0111-FOREST1 — forest pair-hazard domination

Let `G=([n],E)` be any forest and let `q in R_+^n`. Then

`sum_{ij in E} Phi(q_i,q_j) <= F_{n,2}(q)`.                 (3.1)

Equivalently,

`P_q(N<=1) <= product_{ij in E} P_q(not both i and j are included)`.   (3.2)

#### Proof

Set

`a_i = exp(-q_i) in (0,1]`,

and introduce the odds

`r_i = (1-a_i)/a_i = exp(q_i)-1 >=0`.

Let

`B = product_i a_i`.

The event `N<=1` consists of the empty configuration and the `n` singleton configurations, hence

`P_q(N<=1) = B (1 + sum_i r_i)`.                            (3.3)

For an edge `ij`,

`P_q(not both i and j are included)`
` = a_i+a_j-a_i a_j`
` = a_i a_j (1+r_i+r_j)`.                                  (3.4)

If `d_i` is the degree of vertex `i` in `G`, multiplying (3.4) over the edges and dividing by (3.3) shows that (3.2) is equivalent to

`R_G(r) := [product_{ij in E}(1+r_i+r_j)] [product_i (1+r_i)^(1-d_i)]`
`          >= 1 + sum_i r_i`.                              (3.5)

We prove (3.5) by induction on the number of edges.

If `G` has no edges, then

`R_G(r)=product_i(1+r_i) >= 1+sum_i r_i`,

because all omitted expansion terms are nonnegative.

Now suppose `G` has an edge. Since `G` is a forest, choose a leaf `ell` with unique neighbor `v`, and let `G'=G-ell`. Directly from (3.5), the degree change at `v` gives

`R_G(r) = R_{G'}(r) * (1+r_ell+r_v)/(1+r_v)`
`       = R_{G'}(r) * (1 + r_ell/(1+r_v)).`                 (3.6)

Put `S'=sum_{i != ell} r_i`. By induction,

`R_{G'}(r) >= 1+S'`.

Therefore

`R_G(r) >= (1+S') (1+r_ell/(1+r_v)).`

The difference between the right side and `1+S'+r_ell` is

`r_ell * [(1+S')/(1+r_v)-1]`
` = r_ell (S'-r_v)/(1+r_v) >=0`,

because `S'` contains `r_v` and all other terms are nonnegative. Hence

`R_G(r) >= 1+S'+r_ell = 1+sum_i r_i`.

This completes the induction and proves (3.5), hence (3.2). Taking `-log` gives (3.1). QED.

### Why this is the right category change

The previous R15 overlap theorem separated disjoint support from overlapping support. The correct next invariant for pair-supported `k=2` dual measures is not merely “overlap versus no overlap”; it is the **cycle structure of the support graph**. Forests still admit a one-dimensional leaf elimination, while a cycle is the first place the induction has no leaf with which to discharge the duplicated coordinate resource.

This theorem contains both the old disjoint-edge no-go and the two-edge star/path calculation as special cases.

---

## 4. Method #11 — DUALIZE: all forest-supported pair witnesses are impossible

I use the same weak-dual necessary condition carried from the earlier R15 F0111 reports. If a positive finite measure `mu` on `R_+^n` satisfies the monomial budgets

`int t_I dmu(t) <= (gamma q)_I` for every nonempty `I subset [n]`,   (4.1)

then any `C_gamma` certificate at base `q` implies

`int F_{n,k}(t) dmu(t) <= gamma F_{n,k}(q)`.                (4.2)

Thus a strict reverse inequality in (4.2) is a weak-dual refutation certificate.

The source endpoint theorem plus (3.1) rules out an entire class of such certificates.

### Theorem R15-F0111-FOREST2 — forest-supported pair dual measures cannot refute `k=2`

Let `gamma_0>0` be any universal constant supplied by Talagrand Theorem 10.6 for the all-elements classes, and fix

`0 < gamma <= min(1,gamma_0)`.

Let `mu` be a positive finite measure satisfying the full `k=2` weak-dual budgets (4.1) at a base point `q>=0`. Assume that every point in the support of `mu` has coordinate support of size at most two, and that the graph `G` formed by the distinct two-coordinate supports carrying positive `mu`-mass is a forest. Then

`int F_{n,2}(t) dmu(t) <= gamma F_{n,2}(q)`.                (4.3)

Hence such a measure cannot be a weak-dual refutation of Talagrand's `k=2` threshold statement at this universal `gamma`.

#### Proof

Atoms supported on zero or one coordinate contribute zero to `F_{n,2}` and may be discarded from the objective.

For every edge `e={i,j}` of `G`, let `mu_e` be the restriction of `mu` to points whose nonzero coordinate support is exactly `{i,j}`. On this two-coordinate plane,

`F_{n,2}(t) = Phi(t_i,t_j)`.

Because `mu_e <= mu` as positive measures, the global moment budgets (4.1) imply the local budgets

`int t_i dmu_e <= gamma q_i`,

`int t_j dmu_e <= gamma q_j`,

`int t_i t_j dmu_e <= gamma^2 q_i q_j`.                    (4.4)

Talagrand Theorem 10.6 says that the two-coordinate all-elements class belongs to `C_{gamma_0}`, and Definition 10.1 notes that `C_gamma` increases as `gamma` decreases. Therefore it belongs to `C_gamma`. Apply its source-valid positive polynomial certificate at the local base `(q_i,q_j)`. Integrating that certificate against `mu_e` and using (4.4) gives

`int Phi(t_i,t_j) dmu_e(t) <= gamma Phi(q_i,q_j)`.          (4.5)

Summing (4.5) over all edges,

`int F_{n,2}(t)dmu(t)`
` <= gamma sum_{ij in E(G)} Phi(q_i,q_j)`
` <= gamma F_{n,2}(q)`,

where the final inequality is Theorem R15-F0111-FOREST1. This proves (4.3). QED.

### Exact reduction obtained

For any `gamma` no larger than the universal endpoint constant from Talagrand Theorem 10.6, a `k=2` weak-dual counterexample must satisfy at least one of the following:

1. some support point has at least **three** nonzero coordinates; or
2. if every support point has size at most two, the graph of pair supports contains a **cycle**.

For the smallest non-endpoint case `n=3,k=2`, this is especially sharp:

- any two-atom witness whose two atoms each have support size at most two is impossible, because at most two distinct pair supports form a forest;
- therefore any unresolved two-atom witness must contain a **full-support atom**;
- a pair-only witness must use all three pair supports `{1,2}`, `{2,3}`, `{1,3}` (at least one positive-mass group on each), so the first unresolved pair-only topology is the triangle.

This strictly narrows the “overlap-connected two-atom” obstruction from the previous R15 report.

---

## 5. Method #23 — DO WHAT THE PROPOSER DID NOT EXPECT: the cycle boundary is real

The forest hypothesis in (3.1) cannot simply be replaced by an arbitrary graph. For the triangle `K_3` and the homogeneous ray `q=c(1,1,1)`,

`Phi(c,c) = 2c-log(2 exp(c)-1) = c-log 2+o(1)`,

while

`F_{3,2}(c,c,c) = 3c-log(3 exp(c)-2) = 2c-log 3+o(1)`.

Hence

`3 Phi(c,c)-F_{3,2}(c,c,c)`
` = c + log 3 - 3 log 2 + o(1) -> +infinity`.               (5.1)

So the pair-hazard domination theorem is genuinely **acyclic**. A cycle creates enough repeated pair hazard that the leaf-elimination budget breaks at first order. This does not itself produce a feasible weak-dual counterexample—the mixed monomial constraints may still forbid the required mass—but it shows that “cycle versus forest” is not an artifact of the proof.

The next negative search should therefore focus on exactly two minimal configurations rather than another generic coefficient scan:

- `n=3,k=2`: one full-support atom plus one lower-support atom;
- `n=3,k=2`: a triangle of pair-supported mass groups, with the three pair moment budgets coupled exactly.

Those are now the first unresolved finite topologies on the dual side.

---

## 6. Prior-art and current-literature log

Queries/access checks performed on 2026-09-18:

- direct arXiv v4 read of `arXiv:1302.6958`, Definition 2.1 and Problem 7.2;
- exact phrase / title searches for `Forward Brownian Motion`, `Problem 7.2`, Burdzy, Scheutzow;
- direct Talagrand primary PDF read of Definition 10.1, Theorem 10.6 / Theorem 10.7, and Problem 10.9;
- exact searches for `Problem 10.9`, `C_gamma`, cardinality thresholds, and Talagrand's title;
- later related literature checks including DeMarco--Kahn, Frankston--Kahn--Park, and Warnke;
- prior-art searches for the forest identity using variants of `at most one Bernoulli`, `forest`, `product (1-p_i p_j)`, and the odds-form expression involving `1+r_i+r_j`.

The forest searches did not return a source stating exactly (3.1)/(3.5). That is **not** enough to claim novelty. The leaf-induction mechanism is elementary and may well be folklore or implicit in reliability/graphical-model literature. Publication novelty is therefore `UNVERIFIED`.

Access limits: web search is not a complete citation database; some publisher results expose abstracts rather than full texts. No claim of exhaustive global open status or novelty is made.

---

## 7. Validation allocation

No checker was created. The new claims are analytic theorem-sized statements with full proofs above, not finite enumerations. A ceremonial numerical grid or sampled-path check would not strengthen them and would violate the 90/10 research-first directive.

No audits were requested in this run because F0111 remains a retained screening problem, not a closure claim. No source problem is labeled PROVED or REFUTED.

---

## 8. Structured ledger delta

```yaml
ledger_delta:
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2, intake I0076"
  metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  metric_before: "historical carried 2/4; retired handoff; no surviving frozen candidate"
  metric_after: "historical carried 2/4; retired handoff; no surviving frozen candidate"
  status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  unchanged_count: "6, frozen at retirement"
  tried_moves: [1, 11, 23]
  remaining_obligation: "No active candidate. Any future reassignment must first freeze a new source-valid candidate, then prove FBM, BBM, exact arbitrary-random-time half-path independence, and failure of 2BM without strengthening the source hypotheses."
  evidence:
    - "arXiv:1302.6958v4 Definition 2.1 and Problem 7.2 rechecked 2026-09-18"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_1354Z_successor_screen_f0111_moment_ratio_c1_m59j.md"
  audit_ids: []
  admission:
    E_ready_before: 0
    E_ready_after: 0
  retained_screen:
    source: "Talagrand, Are Many Small Sets Explicitly Small?, Problem 10.9, F0111"
    status: "OPEN-looking / PARTIAL screening / NOT CLAIMED / novelty UNVERIFIED"
    new_result: "For k=2 and gamma no larger than Talagrand's universal all-elements endpoint constant, any weak-dual measure supported on pair-atoms whose pair-support graph is a forest obeys the target dual inequality. For n=3, every two-atom witness with both supports of size <=2 is eliminated; a pair-only witness must contain the triangle cycle."
    evidence_level: "SELF_CHECK_ONLY, full analytic proof in this report"
```

---

## 9. Model / scheduler control status

The scheduler limitation remains unchanged in the exposed interface. The available task surface exposes prompt/title, schedule or relative start, timing mode, and enabled state, but no binding model-family selector, no reasoning-effort selector, no authenticated per-run applied-model/effort receipt, and no guaranteed hour-long execution field. Therefore `GPT-6 / maximum` remains a prompt request rather than an enforceable setting from this surface, and this report truthfully records the actual visible model as GPT-5.6 Sol with reasoning level UNVERIFIED.

The implementation manifest still records the historical P26 scheduler ID `6aa7b43682948191b697d72fec69d539` returning `You cannot modify this task` in one authorization context. The legitimate workaround is an owning/admin-authorized product or backend context (or platform support) that exposes permission plus model/reasoning controls. Duplication, permission bypass, or pretending the selector was set is not a valid workaround. No scheduler changes were attempted in this run.

## 10. Next fresh methods

The F0111 screen has now used all thirty owner-method labels at least once across the R15 sequence. The next run should therefore begin a new cycle but must not repeat this run's triple. The mathematically clean next target is the **minimal cycle/full-support obstruction** above, preferably with a fresh combination such as #4 PROVE SOMETHING WEAKER COMPLETELY, #16 COMPUTE EVERY SMALL CASE (exact symbolic/algebraic, only after the analytic setup), and #27 SWAP THE QUANTIFIERS.
