Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `L_cone: pi/4 -> pi/4`; unchanged-count remains `UNKNOWN -> UNKNOWN`. Methods actually tried: #8 GO THE OTHER WAY AND DISCRETIZE, #16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE, #19 MAKE IT AN ALGORITHM.**

# R14 HARD OUTSIDE — H0017: finite point-to-halfspace phase histories are completely unconstrained

Repository / branch: `yspennstate/math-open-problems` / `master`.  
Date: 2026-09-17 UTC.

## 1. Continuity, ownership, exclusions, and source freshness

I did **not** reopen the original negative-margin spherical Gaussian perceptron. Its last supported handoff bracket remains

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`,

with width

`6.48139658710`.

The intervening I0089 Riesz target and `RS-2026-BIS32` MinBis/MaxBis target remain handed off. The active exclusive target remains **H0017**, Daniel Ahlberg, Maria Deijfen and Matteo Sfragara, *Surviving from the tip of a cone in competing first-passage percolation*, arXiv:2607.07589v1 (8 July 2026), under `operations/claims/H0017.md`.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the H0017 claim/intake references, the newest complete R14 report `runs/R14/2026-09-17T22-52-51Z_h0017_dh_corner_phase_coexistence_31ad.md`, and the neighboring R07/R08 directories. R07 and R08 have already rotated away from their old FPP targets, so no competing H0017 ownership surfaced. No shared root or peer file was edited.

Fresh web checks by exact title/authors and by 2026 FPP/Busemann/corner terms again recovered arXiv:2607.07589 as the source-matching primary preprint. Daniel Ahlberg's current research page still lists it as a preprint. I did not locate a later primary theorem claiming the all-direction Benjamini cone-survival result. This is bounded negative evidence, not a novelty certificate.

The current source model and metric are unchanged:

`L_cone := sup { ell : for every source-admissible iid continuous F, every theta, every alpha<ell, P_F(G^{theta,alpha})>0 }`.

The source gives the universal baseline `L_cone >= pi/4`; closure is `L_cone=pi/2`.

## 2. Why discretize now

The previous run isolated a very specific possible escape from the exact-four-ray obstruction: a quenched, environment-factor stabilization of finite point-to-hyperplane geodesic graphs at a strict interior support. If such a factor limit existed and remained coalescing, iid ergodicity would rule out the non-ergodic endpoint phase coin forced by the previous conditional theorem.

The obvious hope was therefore that finite-volume outgoing edges might obey a hidden monotonicity or bounded-switch rule as the target halfspace recedes. This run tests that hope before spending another hour on an infinite-volume lemma.

For the discrete model below use the midpoint support

`g(x,y)=(x+y)/2`

and the nested target halfspaces

`H_k={ (x,y) : x+y >= 2k }`.

The quantity inspected is the **first edge** of the unique shortest path from the origin to `H_k` in a finite weighted square-lattice box.

## 3. Method #8 — DISCRETIZE: two disjoint monotone corridors

For `j>=1`, define a north-first corridor by

- `p_N(2r-1)=(r-1,r)`,
- `p_N(2r)=(r-1,r+1)`,

with `p_N(0)=(0,0)`.

Let the east-first corridor be its reflection

`p_E(j)=(p_N(j)_2,p_N(j)_1)`.

Both are nearest-neighbor monotone lattice paths, they meet only at the origin, and every `p_N(j),p_E(j)` lies on the level `x+y=j`.

This turns the finite-volume phase question into two scalar cumulative passage-time sequences: the first hit of `H_k` on either corridor occurs exactly at level `2k`.

## 4. Method #16 — COMPUTE EVERY SMALL CASE: an exact finite-word realization theorem

### Theorem R14-H0017-T16.1 — every finite N/E phase word is realizable

Fix `m>=1` and any word

`s=(s_1,...,s_m) in {N,E}^m`.

There are strictly positive integer edge weights on a finite square-lattice box such that, simultaneously for every `1<=k<=m`, the unique shortest path from `(0,0)` to `H_k` begins North if `s_k=N` and begins East if `s_k=E`.

#### Proof

Set

`delta_k=-1` if `s_k=N`, and `delta_k=+1` if `s_k=E`.

Prescribe the cumulative costs at level `2k` by

`A_k = 10 k + delta_k`  on the north corridor,

`B_k = 10 k - delta_k`  on the east corridor.

Put `A_0=B_0=0`. The two-edge block increments are

`A_k-A_{k-1}=10+delta_k-delta_{k-1}`,

`B_k-B_{k-1}=10-delta_k+delta_{k-1}`

for `k>=2`, hence belong to `{8,10,12}`; the first block totals are `9` or `11`. Split each positive block total across its two corridor edges as `1` and `block_total-1`.

Give every edge not belonging to either corridor a common weight

`M > max(A_m,B_m)`,

for example `M=100m+100`.

Any path using a noncorridor edge therefore costs more than either corridor candidate. Since all corridor weights are positive, among vertices of one corridor lying in `H_k`, the cheapest is its first hit at level `2k`. Consequently the only two possible minimizers have costs `A_k` and `B_k`.

If `s_k=N`, then `delta_k=-1` and

`A_k=10k-1 < 10k+1=B_k`.

If `s_k=E`, then `delta_k=+1` and

`B_k=10k-1 < 10k+1=A_k`.

The two corridors are disjoint after the origin, so the winning path is unique and has the prescribed first edge. `QED`

This proves much more than the originally sought N/E/N counterexample: **the finite first-edge history can be an arbitrary binary word**. There is no deterministic monotonicity, bounded number of switches, or forbidden finite pattern coming merely from planarity, positivity of edge weights, nested halfspaces, or uniqueness of finite geodesics.

### Exact checker

I implemented the construction with integer arithmetic and ran exact Dijkstra on the full square box for **all 32 words of length five**.

Artifacts:

- checker: `artifacts/R14/2026-09-17T23-51-14Z_h0017_phase_word_exact.py`, creation commit `80a6b25bd3bd6eacd0a0e468cd98da9874024cc3`;
- archived output: `artifacts/R14/2026-09-17T23-51-14Z_h0017_phase_word_exact.out`, creation commit `7d5dfa1341fbd81a5f2b64d90107a8bea1988198`.

Both were read back at their exact creation commits. The output ends

`ALL_32_WORDS_PASS`.

For the sample word `NENEN`, the exact winners are

- `k=1`: cost `9`, target `(0,2)`, first edge North;
- `k=2`: cost `19`, target `(3,1)`, first edge East;
- `k=3`: cost `29`, target `(2,4)`, first edge North;
- `k=4`: cost `39`, target `(5,3)`, first edge East;
- `k=5`: cost `49`, target `(4,6)`, first edge North.

## 5. A stronger extension obstruction

The construction is recursive in the scale blocks. Therefore a finite phase history carries essentially no deterministic information about the next phase.

Fix a word `s_1,...,s_m`. Build the first `m` corridor blocks with a common off-corridor weight already chosen large enough for scale `m+1`. The corridor edges in the next annulus have not yet been specialized. By choosing only those new block weights according to `delta_{m+1}=-1` or `+1`, one obtains two extensions that agree on all earlier corridor weights and realize opposite first-edge choices at `H_{m+1}`. Earlier choices remain unchanged because every path to a deeper level has already crossed each earlier target halfspace, and all weights are positive.

So even an arbitrarily long finite history of stable-looking choices can be extended to switch again. This is an exact adversarial statement for deterministic weighted boxes; it is not a probabilistic statement about iid FPP.

## 6. Method #19 — MAKE IT AN ALGORITHM: what a valid stabilization algorithm would actually need

Consider the natural algorithmic idea:

1. compute the root outgoing edge of the point-to-halfspace geodesic at successive scales;
2. wait until it has remained unchanged for a long time (possibly together with a large finite gap to the runner-up);
3. declare that edge stabilized and use translation covariance to build an environment-factor geodesic graph.

T16.1 kills any proof of termination based only on a deterministic finite-switch principle or on the observed finite sequence of phase labels. The extension argument shows that no finite phase history, however long, certifies that another switch is impossible in the unrestricted weighted-lattice class.

Thus a source-moving iid theorem must use genuinely probabilistic information that is absent from the deterministic construction: concentration, finite-energy resampling across infinitely many scales, a tail estimate on the runner-up gap, or a direct quenched Busemann convergence theorem. This lines up with Damron--Hanson's long-standing point: deterministic pointwise Busemann convergence to a prescribed direction is itself open in ordinary planar iid FPP, which is why their theory works with distributional point-to-hyperplane limits instead.

The algorithmic route has therefore been reduced to a precise missing probabilistic statement rather than another finite combinatorial lemma:

> prove that iid randomness makes the root first-edge sequence at one strict interior corner support eventually constant almost surely (or supplies a different environment-factor selection), despite the absence of any deterministic bounded-switch mechanism.

Under the previous exact-four-ray conditional analysis, such a quenched factor stabilization would destroy endpoint phase coexistence and hence the four-ray state. But nothing in the present finite computation proves that iid stabilization occurs.

## 7. Literature comparison and what this does not prove

The fresh primary checks still point to three relevant facts:

1. Ahlberg--Deijfen--Sfragara (arXiv:2607.07589, 8 July 2026) prove the Benjamini `pi/2` cone threshold in tangent directions and leave the all-direction iid problem open.
2. Damron--Hanson, *Busemann functions and infinite geodesics in two-dimensional first-passage percolation* (CMP 2014, arXiv:1209.3036), deliberately use distributional point-to-hyperplane limits because deterministic Busemann convergence is not known in general.
3. Alexander--Berger, *Geodesics Toward Corners in First Passage Percolation* (JSP 2018, arXiv:1709.09072), show in a broader stationary non-iid setting that corner geometry can genuinely fail to carry the geodesic directions one would naively expect.

T16.1 is a finite deterministic obstruction, not a new theorem about the iid asymptotic shape and not a movement of `L_cone`. A bounded prior-art search did not locate this exact finite-word formulation, but novelty is **UNVERIFIED** and is not needed for its role here as an internal route test.

## 8. Metric and hard-task status

There is **no fixed-metric movement**:

`L_cone: pi/4 -> pi/4`.

H0017 remains **OPEN / PARTIAL**, with `0/2` external audits for the R14 reductions. The new finite-word theorem has an exact checker but is only a certified obstruction to a proposed route.

The authoritative stagnation field remains `UNKNOWN`; I preserve it as required rather than inferring a counter from the visible run count.

After this run **all thirty Section-B moves have been exercised on H0017 at least once**. There is therefore no honest unused next triple to name. A future continuation should either (i) invoke the Section-I hard-task protocol once an authoritative stuck count is available, or (ii) reuse a move only because the mathematical obligation has genuinely changed. The most concrete changed obligation is now probabilistic: iid quenched stabilization versus arbitrary deterministic finite switching.

## 9. Model / scheduler control status

The scheduler/task surface exposed to this runtime still has fields for prompt/title, schedule or relative start, timing mode, and enablement, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore `GPT-6 / maximum` remains prompt-only and this report is honestly labeled `GPT-5.6 Sol / UNVERIFIED`.

The repository ledger also records that the historical P26 `You cannot modify this task` response was authorization-context dependent: P26 later updated successfully from an authorized P/C context. For any ID that still rejects edits, the legitimate remedies are the authorized owning context or platform support. No scheduler change or permission bypass was attempted in this run.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R14
  active_target: H0017
  source: "Ahlberg-Deijfen-Sfragara, arXiv:2607.07589v1"
  source_status: OPEN
  assignment_status: CLAIMED_HARD_OUTSIDE
  fixed_metric:
    name: L_cone
    before: "pi/4"
    after: "pi/4"
    movement: "NO MOVEMENT"
  unchanged_count:
    before: UNKNOWN
    after: UNKNOWN
  methods_actual: [8, 16, 19]
  new_self_checks:
    - "R14-H0017-T16.1: every finite N/E first-edge phase word is realizable by positive integer weights in a finite square-lattice point-to-halfspace problem"
    - "finite extension obstruction: either next phase can be forced by changing only the next corridor block while preserving the earlier phase history"
  exact_artifacts:
    checker: "artifacts/R14/2026-09-17T23-51-14Z_h0017_phase_word_exact.py @ 80a6b25bd3bd6eacd0a0e468cd98da9874024cc3"
    output: "artifacts/R14/2026-09-17T23-51-14Z_h0017_phase_word_exact.out @ 7d5dfa1341fbd81a5f2b64d90107a8bea1988198"
    result: "ALL_32_WORDS_PASS"
  audits: "0/2"
  status: PARTIAL
  novelty: UNVERIFIED
  predecessor_targets_reopened: false
  shared_roots_modified: false
  peer_files_modified: false
  all_30_methods_exercised: true
  next_methods: []
  next_obligation: "prove an iid-specific quenched stabilization/tail theorem that defeats arbitrary finite switching, or enter the Section-I hard-task handoff protocol once the authoritative stagnation count is available"
```
