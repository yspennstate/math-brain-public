Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `m_cert = 5 -> 8`. Section-B methods actually tried: #14 FIND THE GROUP ACTING, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #25 COUNT THE SAME THING TWICE. Status: PARTIAL.**

# NM13-05 / C0146 — Bernstein-layer transport and the exact eight-edge theorem

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Source: Gábor Pete, *Probability and Geometry on Groups*, Question 13.2, printed p. 185 / current PDF p. 184  
Canonical problem / claim: **C0146**  
Canonical dedup key: `fk_q_less_than_1_monotone_coupling`  
SHA-256: `dd817e3ec8169668456ed767e35982573675498dec1367239155a22daa3f4ec6`  
Selection residue: `4` modulo 13  
Frozen metric: `m_cert` from `operations/claims/C0146.md`  
Metric before / after: **5 -> 8**  
Unchanged-run counter after this invocation: **0**  
Stuck recoveries: **0**  
Required eventual auditors for a completed source claim: **P26 and NM13-06; neither is presumed to pass**

## 1. Runtime and control-plane disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The task-control interface exposed in this context still has prompt/title, schedule or relative-start fields, timing mode, enabled-state and identifiers, but **no bindable model-family selector and no bindable reasoning-effort selector**. Therefore the requested GPT-6/maximum setting remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface that exposes persistent model and reasoning fields and authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` event remains an authorization-context boundary, not evidence that ownership was released; current `RESULTS.md` records that P26 was later updated successfully from another authorized context. The lawful workaround to a future refusal is to use the owning/authorized context or platform/admin support, never clone the task or bypass access controls.

## 2. Continuity and required repository read

This run continued the already admitted exclusive C0146 claim from the newest NM13-05 report:

`proofnet24/NM13-05/runs/2026-09-18/2026-09-18T08-22-00Z__c0146-m5-monotone-coupling.md`.

That report moved the frozen metric from `UNMEASURED` to `5`, proved a cactus-class theorem and an exact diamond `K4-e` transport, and set the next route to six-edge 2-connected blocks via exact parametric/Bernstein transport. It used methods #2/#8/#11, so this invocation deliberately used a different triple.

Before new mathematics I reread or targeted-recovered current `master` state for:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/C0146.md`;
- C0146 intake row, canonical dedup alias and historical attempt `C0146-A001`;
- newest visible neighboring NM13-04 state (`2026-09-18T08-18-00Z__p0457-closure-critical-audit.md`);
- newest visible neighboring NM13-06 state (`2026-09-18T07-30-30Z__p0195-stuck-recovery-1.md`);
- current exact-ID / canonical-key / audit searches for C0146.

No claim release, handoff, retirement, POSTED settlement, campaign closure, P26 PASS, or NM13-06 PASS for C0146 was found. C0146 therefore remains the lawful current target; intake was not reopened.

The current source PDF was rechecked on 2026-09-18. Its title page says April 3, 2024, and p. 184 still states literally:

> Question 13.2. Is there a monotone coupling `(omega_p)_{p in [0,1]}` of the `FK(p,q)` measures for any `q in [0,1)`?

The immediately following Exercise 13.8 still asks for an explicit UST-to-UST+1 monotone coupling on the six-vertex seven-edge digital-figure-8 graph. This finite layer-to-layer transport remains source-native evidence for the route used below.

## 3. Frozen source quantity is unchanged in definition

The source question is not replaced. The frozen finite progress quantity remains:

`m_cert` = the largest integer `m` for which NM13-05 has a rigorous certificate that for **every finite simple graph with at most `m` edges**, every `q in (0,1)`, and all `0 <= p1 <= p2 <= 1`,

`FK_G(p1,q) <=_st FK_G(p2,q)`

under edge inclusion.

The previous certified value was `5`. This run proves `m_cert >= 8`, so under the frozen convention the after-value is **8**. I do not extend the metric to the source's `q=0` endpoint: the source includes that endpoint under its own convention, while the present proof normalizes fixed-size layers for `q>0`. Thus the source remains OPEN and the result below is PARTIAL.

## 4. Recalled exact fixed-size reduction

Let `H=(V,E)` be a finite graph, `m=|E|`, and `q>0`. For `A subseteq E`, let `k(A)` be the component count. At fixed size `|A|=r`, the FK conditional law is independent of `p`:

`nu_r(A) = q^{k(A)} / sum_{|C|=r} q^{k(C)}`.

Writing

`c(A) := |A| - |V| + k(A)`

for the cycle nullity, one has on layer `r`

`q^{k(A)} = q^{|V|-r} q^{c(A)}`,

so the common factor cancels and

`nu_r(A) = q^{c(A)} / W_r(q)`,

where

`W_r(q) := sum_{|C|=r} q^{c(C)}`.

As in the previous report, if every adjacent pair `nu_r, nu_{r+1}` has an inclusion coupling, composing their Markov kernels gives a nested chain

`X_0 subseteq X_1 subseteq ... subseteq X_m`,  `X_r ~ nu_r`.

The FK size distribution at parameter `p` has mass proportional to

`W'_r(q) p^r(1-p)^{m-r}`,

where `W'_r(q)=sum_{|A|=r}q^{k(A)}`. For `p1<p2`, the likelihood ratio of the two size laws is a positive constant times

`[p2(1-p1)/(p1(1-p2))]^r`,

hence increases in `r`. A single uniform quantile variable therefore gives a grand nondecreasing size process `R_p`. Taking the size process independently of the nested chain and setting

`omega_p := X_{R_p}`

gives a monotone grand coupling with exact FK marginals. Thus the finite problem reduces to exact inclusion transports between adjacent fixed-size layers.

## 5. Method #14 — find the group acting

I first examined automorphism groups of the new six-edge 2-connected blocks rather than immediately enumerating all transport variables. Up to isomorphism, there are four such blocks: `K4`, the low-symmetry house/theta block, `K_{2,3}`, and `C6`. The exact checker records their automorphism-group orders as

`[24, 2, 12, 12]`.

This was useful but also exposed why a pure orbit proof is the wrong universal route: the house block has automorphism group of order only `2`, so its layer incidence graph does not collapse enough to a tiny symmetric LP. Symmetry was retained for isomorphism classification, but I abandoned symmetry as the main positivity mechanism instead of forcing another orbit lemma.

Outcome of #14: **use symmetry to quotient graph types and verify representatives, not as the transport proof itself**.

## 6. Method #16 — exact census through eight edges

I next enumerated the genuinely new finite frontier exactly. For 2-connected simple graphs, the unlabeled type counts by exact edge number `m=3,...,8` are

`1, 1, 2, 4, 7, 16`.

Thus only **31** 2-connected block types occur through eight edges. The exact checker independently verifies completeness of the hard-coded representative list: for the cases `|V|<|E|` it exhausts all labeled simple graphs, tests 2-connectivity, computes a degree-preserving canonical code and checks membership in the representative list. The numbers of labeled 2-connected graphs actually encountered in those exhaustive `|V|<|E|` scans are

`0, 0, 6, 71, 820, 10050`.

For the omitted `|V|=|E|` branch no search assumption is used: 2-connectivity implies minimum degree at least two, while the degree sum is exactly `2|E|=2|V|`, so every degree is exactly two; connectedness then forces the unique cycle `C_m`.

A floating or heuristic census is not used in the theorem. The archived checker uses only Python's standard library and exact integer/rational arithmetic.

Outcome of #16: **the universal simple-graph problem through eight edges reduces to 218 adjacent-layer transports across 31 exact 2-connected representatives**.

## 7. Method #25 — count the same mass twice, coefficient by coefficient

The key new idea is a Bernstein-basis transport lemma that removes the need to guess one rational formula for an entire `q` interval.

Fix one block `H` and adjacent layers `r,r+1`. An inclusion flow `F_q(A,B)` from `r`-sets to `(r+1)`-sets gives a coupling of `nu_r` and `nu_{r+1}` if its unnormalized margins are

`row_A(q) = q^{c(A)} W_{r+1}(q)`,

`col_B(q) = q^{c(B)} W_r(q)`.

The total mass is the same from either side by the literal double count

`sum_A row_A(q) = W_r(q) W_{r+1}(q) = sum_B col_B(q)`.

For a degree `N`, write the Bernstein basis on `[0,1]` as

`B_{j,N}(q) = binom(N,j) q^j (1-q)^{N-j}`.

The exact identity

`q^k = sum_{j=k}^N [binom(j,k)/binom(N,k)] B_{j,N}(q)`

shows that every polynomial with nonnegative monomial coefficients has nonnegative Bernstein coefficients. The row and column margin polynomials above have precisely that form.

### Bernstein transport lemma

Suppose all row/column margin polynomials have degree at most `N`. Expand

`row_A(q) = sum_j a_{A,j} B_{j,N}(q)`,

`col_B(q) = sum_j b_{B,j} B_{j,N}(q)`.

If, for every `j`, there is a nonnegative inclusion flow `F^{(j)}(A,B)` with row sums `a_{A,j}` and column sums `b_{B,j}`, then

`F_q(A,B) := sum_j B_{j,N}(q) F^{(j)}(A,B)`

is nonnegative for every `q in [0,1]` and has exactly the desired polynomial row and column margins. For `q>0`, dividing by `W_r(q)W_{r+1}(q)` gives an exact inclusion coupling `nu_r <=_st nu_{r+1}`.

This is the point where the two counts genuinely meet: each coefficient layer has equal source and target mass, and the only remaining question is a finite rational max-flow feasibility problem on the inclusion bipartite graph.

For every one of the 31 block representatives through eight edges, **degree `N=7` suffices simultaneously for every adjacent layer**. The checker expands every margin exactly into degree-7 Bernstein coefficients and solves each coefficient transport with integer max-flow after clearing denominators. It then independently re-sums the realized edge flow and asserts every row and column margin. There are

- `218` adjacent-layer transport pairs;
- `8` Bernstein coefficient indices each;
- hence `1744` exact coefficient-flow instances.

Every one is feasible.

Outcome of #25: **an analytic nonnegative transport for the full continuum `0<=q<=1` at every finite block/layer instance certified by the coefficient flows; no interpolation grid is used**.

## 8. The finite eight-edge theorem

**Theorem (source-valid restricted result).** Let `G` be any finite simple graph with at most eight edges and let `q in (0,1)`. Then the family `{FK_G(p,q): 0<=p<=1}` admits a monotone grand coupling in `p`. In particular,

`FK_G(p1,q) <=_st FK_G(p2,q)` whenever `p1<=p2`.

### Proof

First consider a 2-connected block `H` with at least three edges. Since `|E(H)|<=8`, Section 6 and the exact census place `H` in one of the 31 certified isomorphism classes. By the Bernstein transport lemma and the exact coefficient flows, every adjacent fixed-size pair satisfies

`nu_r <=_st nu_{r+1}`

by an inclusion coupling. Compose these adjacent coupling kernels to obtain a single nested chain `X_0 subseteq ... subseteq X_m` with the correct fixed-size marginals. Couple the stochastically increasing FK size distributions by one common quantile variable `R_p` and put `omega_p=X_{R_p}`. Section 4 verifies that the marginal of `omega_p` is exactly `FK_H(p,q)` and that `p -> omega_p` is nondecreasing.

A one-edge bridge block is even simpler: its open probability is

`p / [p+q(1-p)]`,

which is increasing in `p`, so one uniform label grand-couples it.

Now decompose a connected simple graph into its block tree. Under a one-vertex sum `G=G1 vee G2`, if `A=A1 union A2`, then

`k_G(A) = k_{G1}(A1) + k_{G2}(A2) - 1`.

The `-1` is independent of the configuration, so the random-cluster weight factorizes into the product of the two block weights up to a global normalizing constant. Iterating over the block tree shows that the FK law is a product of its block laws; disconnected graph components factor in the same way, and isolated vertices only contribute another constant factor. Take the block grand couplings independently and unite their open-edge sets. The product coupling is monotone and has the exact FK marginal on `G` for every `p`.

This proves the theorem. `QED`

The theorem is stronger than the frozen metric's pairwise stochastic-order requirement, but it does **not** settle Pete's unrestricted all-finite-graphs question and does not certify the `q=0` endpoint.

## 9. Exact self-check and archived evidence

The mathematical route above was written before treating a checker as evidence. The finite core was then executed exactly with no floating point and no external package. It is a **self-check, not an independent audit**.

Artifacts:

- `proofnet24/NM13-05/artifacts/2026-09-18/c0146_m8_bernstein_checker.py`
  - creation commit `e765cc0a5eda7888b1aac28c7ecacf8603ebf848`;
- `proofnet24/NM13-05/artifacts/2026-09-18/c0146_m8_bernstein_checker.out`
  - creation commit `bef55161ba1b27108d1477c4d0e7028baf31fa3f`;
  - read-back blob `e4538154f4916d8b735c608f54bb45eef3e91a27`.

Archived output:

```text
m6_automorphism_group_orders [24, 2, 12, 12]
unlabeled_2connected_type_counts_m3_to_m8 [1, 1, 2, 4, 7, 16]
labeled_2connected_enumerated_n_lt_m [0, 0, 6, 71, 820, 10050]
representatives_total 31
adjacent_layer_transport_pairs 218
bernstein_degree 7
bernstein_coefficient_flow_instances 1744
ALL_EXACT_CHECKS_PASS
```

The checker separately verifies representative 2-connectivity, classification completeness, nonnegative exact Bernstein coefficients, equal coefficientwise total masses, max-flow saturation and re-summed exact row/column margins.

## 10. Bounded current literature check — 2026-09-18

This is a bounded search, not a worldwide openness or novelty certificate.

1. **Original source.** Pete's current public PDF, dated April 3, 2024, still contains Question 13.2 verbatim on current PDF p. 184 and the adjacent finite UST/UST+1 exercise. Source URL checked: `https://math.bme.hu/~gabor/PGG.pdf`.

2. **Park, 2026.** Heehyun Park, *The q<1 Random-Cluster Model on Wired Trees: Uniqueness and Negative Dependence*, arXiv:2608.08565, submitted 2026-08-09, proves wired-tree uniqueness and branch negative-dependence results. Its abstract says even pairwise negative correlation remains open on general graphs. It does not give the unrestricted monotone-in-`p` coupling asked by Pete.

3. **Tang–Zhang, 2026.** Pengfei Tang and Zibo Zhang, *Negative correlation for the random-cluster model below one on high-degree regular graphs*, arXiv:2609.11578, submitted 2026-09-10, proves pairwise negative correlation in broad high-degree regular families under an isoperimetric hypothesis. Again this is not a general monotone coupling theorem.

4. **Lorentzian/Tutte literature.** Brändén–Huh, *Lorentzian polynomials*, Annals of Mathematics 192 (2020), proves the homogenized multivariate Tutte polynomial is Lorentzian for `0<q<=1` and derives negative-dependence consequences. That does not automatically supply the layer-covering couplings needed here: Cryan–Guo–Mousa, *Modified log-Sobolev inequalities for strongly log-concave distributions*, Annals of Probability 49 (2021), Appendix A, explicitly shows strong log-concavity and the stochastic covering property are incomparable. Thus I did not treat Lorentzianity as a source closure.

The dated searches also used phrases `monotone coupling FK(p,q) q<1`, `random-cluster q<1 monotonicity in p`, `stochastic covering random cluster q<1`, and combinations with `Lorentzian`, `Tutte`, and `fixed edge number`. I found no primary source matching either Pete's unrestricted coupling or this exact `<=8` finite theorem. **Publication novelty of the eight-edge theorem and Bernstein construction remains UNVERIFIED.**

## 11. Status, counters, audits, and next route

Source verdict in this report: **OPEN**.  
NM13-05 result status: **PARTIAL**.  
Frozen metric: **`m_cert = 5 -> 8`**.  
Unchanged runs after this invocation: **0**.  
Stuck recoveries: **0**.

Outside audits:

- P26: **NOT PASSED**;
- NM13-06: **NOT PASSED**.

No audit is inferred from the self-check, neighboring work, or literature search.

The next high-value question is structural, not another blind edge-count increment: determine whether the Bernstein coefficient-flow criterion follows from a recognizable matroid / Rayleigh / exchange property for all graphic random-cluster layer measures, or identify the first block where a coefficient Hall inequality fails. Fresh proposed Section-B methods for the next invocation are **#1 CHANGE THE CATEGORY** (graphic matroid / Tutte), **#13 FIND WHAT ONLY INCREASES** (coefficient Hall slack under edge addition), and **#20 FIND WHY THE ALGORITHM FAILS** (search for the first minimal coefficient cut obstruction before extending the census). These are proposals only and are not credited as attempted in this run.

## 12. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  source_id: C0146
  claim_id: C0146
  canonical_dedup_key: fk_q_less_than_1_monotone_coupling
  category: CLOSABLE_OUTSIDE
  status: PARTIAL
  source_status: OPEN
  metric_name: m_cert
  metric_definition: "largest m rigorously certified for all finite simple graphs with <=m edges, q in (0,1), and all p1<=p2, under FK stochastic order"
  metric_before: 5
  metric_after: 8
  movement: true
  methods_actual:
    - 14
    - 16
    - 25
  method_outcomes:
    14: "automorphism quotient useful for type reduction but house block has group order 2, so symmetry alone abandoned"
    16: "exact 2-connected census through eight edges: type counts 1,1,2,4,7,16; 31 representatives"
    25: "Bernstein coefficientwise double-count transport gives exact inclusion flows for all q in [0,1] on every adjacent layer of every representative"
  finite_core:
    checker: proofnet24/NM13-05/artifacts/2026-09-18/c0146_m8_bernstein_checker.py
    output: proofnet24/NM13-05/artifacts/2026-09-18/c0146_m8_bernstein_checker.out
    exact: true
    self_check_only: true
    result: ALL_EXACT_CHECKS_PASS
  theorem: "Every finite simple graph with at most 8 edges and q in (0,1) admits a monotone grand coupling of FK(p,q) over p in [0,1]."
  q_zero_endpoint_certified: false
  unrestricted_source_closed: false
  unchanged_runs: 0
  stuck_recoveries: 0
  audits:
    P26: NOT_PASSED
    NM13-06: NOT_PASSED
  literature_check_date: 2026-09-18
  literature_status: "source still states Q13.2; Park 2608.08565 and Tang-Zhang 2609.11578 do not settle it; Lorentzian/Tutte prior art does not automatically imply stochastic covering; novelty UNVERIFIED"
  next_step: "seek structural graphic-matroid explanation of Bernstein coefficient transports or first exact coefficient Hall obstruction before extending edge census"
```

No shared root, peer namespace, workflow, permission, public surface, email/Drive resource, paid compute, or schedule was modified in this invocation. The only writes were the two warranted C0146 exact artifacts and this single immutable NM13-05 run report.
