Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MOVEMENT: `n_edge^*` UNMEASURED -> `n_edge^* >= 4`. Methods actually tried: #2, #9, #10.

# NM13-06 research invocation — P0195 admission and exact n<=3 theorem

Date: 2026-09-17 UTC
Track: `proofnet24/NM13-06`
Category: CLOSABLE OUTSIDE
Canonical source/claim: `P0195`, `operations/claims/P0195.md`
Status: **PARTIAL; source OPEN**
Unchanged-run count: **0**
Stuck-recovery count: **0**
Designated eventual outside auditors: **P26 and NM13-07; neither is counted as passed**

## 1. Runtime/control disclosure

The task prompt requests GPT-6 with maximum reasoning, but this invocation actually identifies as **GPT-5.6 Sol** and the reasoning level available to the report is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, or an hour-long execution.

The exposed task-control schema still offers title/prompt, schedule or relative start, timing mode, and enabled state. It exposes no bindable model-family field and no bindable reasoning-effort field. Therefore the requested GPT-6/maximum setting remains prompt text only in this environment. Changing that would require a scheduler/product API or authorized account/workspace control that actually exposes model and reasoning selectors. The repository's current `RESULTS.md` also corrects the older P26 permission story: a P26 update later succeeded in another authorized context, so an earlier `You cannot modify this task` response was context-specific. If such a refusal recurs, the valid route is the owning account/workspace or an authorized product/admin surface, not task duplication or an access-control bypass. No schedule was created or modified in this run.

## 2. Continuity and required repository read

I continued from the newest NM13-06 report, `proofnet24/NM13-06/runs/2026-09-17/2026-09-17T22-47-00Z__admission-screen-2.md`, which ended ADMISSION_PENDING with cursor at the first new canonical Codex key after the already-screened P0096 tranche. I did not restart intake and did not count screening as mathematical progress.

Before admission I reread or recovered the current controlling material: `FLEET_RULES.md`; `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; `operations/NEW_METHODS_2026-09-16.md`; later deployment amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`; root `QUEUE.md`, `POSTED.md`, `RESULTS.md`; `probability_campaign_2026_09/INDEX.md` and `RANKING.md`; the newest NM13-06 report; neighboring NM13-05 and NM13-07 reports; the Codex problem/catalog/rank records; and current claim/search surfaces. Large repository files are connector-truncated when fetched wholesale, so exact-ID, exact-dedup-key, and focused file reads were used rather than pretending every byte was visually materialized. No critical P0195 history used below was inaccessible.

The residue-5 continuation after P0096 first encountered source rows such as P0110, P0124, P0160, P0163 and P0191 whose live remainder is asymptotic/infinite or otherwise genuinely HARD rather than an honest CLOSABLE finite-certificate target. The first candidate in this continuation with a literal finite counterexample route was P0195. This is outside the preferred discrepancy/signing/design subject, but the deployment explicitly permits another CLOSABLE OUTSIDE source in the shard when needed.

## 3. Admission gate: exact source, identity, current status, attempts, ownership

### Canonical identity and shard

Problem: **P0195 — Monotonicity of the ferromagnetic Ising spectral gap**.

Canonical dedup key:

`monotonicity_of_the_ferromagnetic_ising_spectral_gap`

SHA256:

`102de34178ace6c6ebb4f5b99308978b4b29fae78f3af1988614584ee288c807`

and

`int(SHA256(UTF-8 dedup_key).hexdigest(),16) mod 13 = 5`.

Thus P0195 lies in NM13-06's exclusive shard. I did not hash the display ID or manufacture an alias.

### Exact source

David A. Levin, Yuval Peres, Elizabeth L. Wilmer, *Markov Chains and Mixing Times*, open-problem chapter, intake locator `Chapter 26 Question 2, PDF p.375`. The freely available older PDF numbers the same item as Chapter 23 Question 2 and states, under the chapter convention that the questions use Glauber dynamics unless otherwise specified:

> Is the spectral gap of the Ising model on a graph G monotone increasing in temperature? Is the spectral gap of the Ising model monotone decreasing in the addition of edges?

This run studies the second clause with the standard zero-field ferromagnetic random-scan heat-bath Glauber chain. The intake's individual-coupling strengthening is recorded but is not substituted for the literal source clause.

### Dated current-literature check

Search date: 2026-09-17 UTC. Bounded queries included the exact source sentence and combinations of `Ising spectral gap`, `monotone increasing in temperature`, `addition of edges`, `ferromagnetic`, `Glauber`, `counterexample`, and the Levin–Peres–Wilmer authors/title. The source wording was recovered directly. Later relevant work recovered included Eldan–Koehler–Zeitouni, *A spectral condition for spectral gap: fast mixing in high-temperature Ising models* (PTRF 2022), and Masaoka–Soejima–Watanabe, *Rigorous Lower Bound of the Dynamical Critical Exponent of the Ising Model* (J. Stat. Phys., published 26 May 2025). Related later Peres work on critical Ising trees and other spectral-gap papers concerns regimes/bounds rather than this finite-graph monotonicity question. I did not locate a source-matching proof or counterexample. This is bounded negative evidence, not a worldwide-openness or novelty certificate.

### Prior attempt

The September campaign has one limited calculation: for the two-spin edge with interaction `J>=0`, if `c=tanh J`, the random-scan heat-bath eigenvalues are `1,(1+c)/2,(1-c)/2,0`, hence the gap is `(1-c)/2`, supporting monotonicity. The recorded obstruction was the general change of both stationary measure and Dirichlet form. No previous finite search beyond that is credited here.

### Exclusive ownership / exclusions

Before creating the claim I checked `operations/claims/P0195.md` directly (it did not exist) and searched current `master` for `P0195`, its exact title and its canonical dedup key. The hits were intake/catalog/ranking copies and the limited campaign attempt; no worker claim, historical assignment, handoff or alternate-ID owner was recovered. `POSTED.md`, campaign `INDEX.md` and `RANKING.md` contain no source-level P0195 settlement. Existing Komlos, Beck–Fiala, Paley, sign-matrix discrepancy, Matrix Spencer, cutoff, and other Ising assignments are distinct and remain untouched.

The canonical claim was therefore created with create-only semantics at commit

`13f1e29fc27c167d553b6b166087bee3d72b4407`

and read back at that exact commit; blob

`bb1df7f69f6ef0c8024f7312c22b3d6ea8c33d0d`.

## 4. Frozen metric

Fix the zero-field ferromagnetic Ising model on a finite simple graph `G`, with a common inverse temperature `beta >= 0` on every edge, and random-scan single-site heat-bath Glauber dynamics. For an absent edge `e`, compare `G` and `G+e` at the same `beta` and same one-site-per-step normalization.

Define

`n_edge^* = min{|V(G)| : there exist an absent edge e and finite beta>=0 with gap_beta(G+e) > gap_beta(G)}`,

with `n_edge^*=+infinity` if there is no counterexample.

This is the minimal finite witness complexity for the literal edge-addition clause. At admission it was **UNMEASURED**. It is not silently replaced by a finite-grid statistic. Continuous-time dynamics with equal per-site rates differs at fixed `n` only by a common positive factor, so the edge-ordering question is unchanged by that normalization choice.

## 5. Section-B method #2 — attack the negation first

I first searched for a source-valid finite counterexample rather than trying to prove monotonicity.

A direct numerical heat-bath diagonalization searched every labeled simple graph through `n=5` on a common-beta grid (`0.05,0.1,0.2,0.35,0.5,0.75,1,1.5,2,3`; the `n<=4` pass also included `0.02`) and every single absent-edge addition. No positive gap difference `gap(G+e)-gap(G)` was found. This finite beta grid is **not a proof** of continuous-beta monotonicity and does not move the metric by itself.

The useful information was structural: the near-maximal differences were equalities/near-equalities caused by component bottlenecks at large beta, not a stable sign-reversing candidate. That suggested proving the smallest orders exactly before spending effort on larger numerical search.

Outcome of #2: **no counterexample found; route redirected to an exact small-order theorem**.

## 6. Section-B method #9 — randomize

To test whether the failure might first occur just beyond exhaustive small search, I sampled 2,000 random labeled `n=6` graph/absent-edge pairs using seed 12 and independently sampled `beta=10^U`, `U` uniform on `[-2,0.7]`. Full reversible heat-bath spectra were computed numerically. No stable positive `gap(G+e)-gap(G)` occurred; the largest displayed positives were at floating-point roundoff scale when gaps themselves were essentially zero.

Again this is route selection, not a theorem and not a certificate. It does not certify `n=6` or any beta interval.

Outcome of #9: **no randomized witness; evidence favored exact low-order structure over more blind search**.

## 7. Section-B method #10 — derandomize: exact theorem for every graph on at most three vertices

This method moved the frozen metric.

### Theorem NM13-06-P0195-N3

For every finite simple graph `G` with `|V(G)|<=3`, every finite `beta>=0`, and every absent edge `e`, the zero-field ferromagnetic random-scan heat-bath Ising spectral gap satisfies

`gap_beta(G+e) <= gap_beta(G)`.

Consequently

`n_edge^* >= 4`.

### Proof

Write

`c = tanh(beta)`,

so `0<=c<1`, and put

`d = tanh(2 beta) = 2c/(1+c^2)`.

For `n=1` there is no edge to add. For `n=2`, the empty graph is two independent refreshed spins and has gap `1/2`; after adding the unique edge, the standard two-spin calculation gives gap `(1-c)/2 <= 1/2`.

It remains to treat `n=3`. Up to graph isomorphism there is exactly one simple graph with each of 0,1,2,3 edges: the empty graph, one edge plus an isolated vertex, the path `P3`, and the triangle `K3`. Therefore every single edge addition follows this chain of four isomorphism types.

The exact heat-bath characteristic polynomials are recorded by the checker below. Their roots give the following gaps.

**Empty graph.** Its eigenvalues are

`1, 2/3 (multiplicity 3), 1/3 (multiplicity 3), 0`,

so

`gap(empty) = 1/3`.

**One edge plus an isolated vertex.** The characteristic polynomial factors as

`x(x-1)(3x-2)(3x-1)(-c+3x-2)(-c+3x-1)(c+3x-2)(c+3x-1)/729`.

Thus the largest nontrivial eigenvalue is `(2+c)/3`, and

`gap(one edge) = (1-c)/3`.

**Path P3.** Put

`s = sqrt(2)c/sqrt(1+c^2)`.

The two nontrivial quadratic factors in the exact characteristic polynomial have roots

`2/3 +/- s/3` and `1/3 +/- s/3`,

besides `1,0,2/3,1/3`. Since `0<=s<1`, the largest nontrivial eigenvalue is `2/3+s/3`, hence

`gap(P3) = (1-s)/3`.

**Triangle K3.** The exact factorization gives the nontrivial eigenvalues

`2/3+d/3`, `2/3-d/6` (multiplicity 2), `1/3+d/3`, and `1/3-d/6` (multiplicity 2),

plus `1` and `0`. Therefore

`gap(K3) = (1-d)/3`.

It remains only to order `c,s,d`. All three are nonnegative, and exact algebra gives

`s^2-c^2 = c^2(1-c^2)/(1+c^2) >= 0`,

`d^2-s^2 = 2c^2(1-c^2)/(1+c^2)^2 >= 0`.

Thus `c<=s<=d`. Consequently

`1/3 >= (1-c)/3 >= (1-s)/3 >= (1-d)/3`,

which is precisely the nonincrease of the spectral gap under each possible edge addition on three vertices. Together with the `n<=2` cases, this proves the theorem. QED.

### Exact self-check

I wrote and executed an exact SymPy checker that constructs the `8 x 8` heat-bath matrices symbolically in `c`, factors all four `n=3` characteristic polynomials, verifies the advertised slow eigenvalues, and verifies the two polynomial/rational identities controlling `c<=s<=d`.

Checker:
`proofnet24/NM13-06/artifacts/2026-09-17/p0195_n3_exact.py`
creation commit `26806994df850dbdf7c6025e1d8383ca5fa461fd`.

Archived executed output:
`proofnet24/NM13-06/artifacts/2026-09-17/p0195_n3_exact.out`
creation/readback commit `6961a586c224769282330b993b6402e05c594ce0`, blob `bec16e15b8e99a5c6a66e2324e49d81a20479e58`.

The output ends

`ALL_EXACT_CHECKS_PASS`.

This checker is a **self-check**, not an outside audit. The proof above, not the checker alone, supplies the continuous-parameter argument.

Outcome of #10: **exact theorem; metric moved from UNMEASURED to `n_edge^* >= 4`**.

## 8. Interpretation and remaining obligation

This does **not** solve LPW Question 2. The source's temperature-monotonicity clause is untouched, and the edge-addition clause remains open from four vertices onward. The finite beta scans through five vertices and randomized six-vertex scans are not certificates for those orders.

The small-order formulas do expose a useful mechanism: on three vertices the slow mode is already in the spin-linear sector, and edge addition replaces the effective correlation parameter in the sequence

`0 -> c -> sqrt(c tanh(2 beta)) -> tanh(2 beta)`,

which increases monotonically. A genuine counterexample at larger order therefore has to defeat this simple correlation-mode ordering, most plausibly through a nonlinear representation sector or a component/bottleneck mode switch.

The next research run should not repeat #2/#9/#10. Proposed methods are **#14 (find the group acting)**, **#16 (compute every small case and stare at the sequence)**, and **#24 (find the extremal object)**: quotient the `n=4` graphs by isomorphism and spin-flip/automorphism symmetry, derive exact sector characteristic polynomials, and identify which edge-addition pair can maximize `gap(G+e)-gap(G)` over `c in [0,1)` before attempting a certified all-beta order-four theorem or an exact witness.

No closure package is created, no audit is presumed, and no shared root ledger is edited by this worker.

## 9. Structured ledger_delta for P26

```json
{
  "track": "NM13-06",
  "category": "CLOSABLE OUTSIDE",
  "source_id": "P0195",
  "claim_id": "P0195",
  "canonical_dedup_key": "monotonicity_of_the_ferromagnetic_ising_spectral_gap",
  "shard_mod_13": 5,
  "status": "PARTIAL",
  "source_status": "OPEN",
  "metric_name": "n_edge^*",
  "metric_before": "UNMEASURED",
  "metric_after": ">=4",
  "movement": true,
  "methods_actual": [2, 9, 10],
  "method_outcomes": {
    "2": "No counterexample on exhaustive labeled n<=5 finite-beta grid; numerical only, redirected to exact small order",
    "9": "No stable violation in 2000 random n=6 graph/edge/beta trials; numerical only",
    "10": "Proved exact all-beta edge-addition monotonicity for every graph on at most 3 vertices"
  },
  "unchanged_runs": 0,
  "stuck_recoveries_used": 0,
  "claim_creation_commit": "13f1e29fc27c167d553b6b166087bee3d72b4407",
  "exact_checker_output_commit": "6961a586c224769282330b993b6402e05c594ce0",
  "audits": {
    "P26": "NOT_REQUESTED_NOT_COUNTED",
    "NM13-07": "NOT_REQUESTED_NOT_COUNTED"
  },
  "next_methods": [14, 16, 24],
  "next_step": "Exact n=4 symmetry quotient and all-beta edge-addition comparison; search nonlinear mode switches before any n=5 certification"
}
```
