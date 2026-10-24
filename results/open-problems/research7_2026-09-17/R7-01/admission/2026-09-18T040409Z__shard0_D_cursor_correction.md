# R7-01 shard-0 D-cursor correction and live-queue exclusion pass

Date: 2026-09-18 UTC
Repository: `yspennstate/math-open-problems`
Branch: `master`
Native slot: `R7-01 Counterexamples and Constants`
Native ID: `6aabe777361481919c9e614646464772`
Start snapshot: `010c07b98cfd31da7fee523ce0c4d62bf6850c86`
Fresh pre-delivery master observed during this run: `b722de57ba8e3c24a683d8c9249dee7707051b13`
Selection rule: `sum(ord(c) for c in canonical_id) % 7 == 0`, exact case-sensitive canonical ID.

This is cumulative admission work, not a source admission. No target passes the full shard/current-source/ownership/CLOSABLE gate below, so no `operations/claims/<ID>.md` is created and no research Section-B triple is charged.

## 1. Correction to the previous cursor

The previous R7-01 report suggested continuing with `D0060`, `D0067`, and `D0075`. The last ID is not in shard 0:

- `D0075`: `68+48+48+55+53 = 272`, hence `272 mod 7 = 6`.
- `D0076`: `68+48+48+55+54 = 273`, hence `273 mod 7 = 0`.

Therefore `D0075` belongs to R7-07's shard, not R7-01's shard. R7-01 must not screen, claim, or attack it merely because it appeared in the previous cursor prose. The correct next D candidate is `D0076`.

For the canonical D intake `D0001` through `D0102`, the exact shard-0 IDs are:

`D0006, D0015, D0024, D0033, D0042, D0049, D0051, D0058, D0060, D0067, D0076, D0085, D0094`.

The earlier R7-01 reports already disposed of `D0015`, `D0024`, `D0033`, `D0042`, and `D0051`. This run closes the remaining D-cursor cases without inventing an assignment.

## 2. D0006 — owned/retired route, not free inventory

Canonical `operations/claims/D0006.md` exists and records an exclusive HARD OUTSIDE assignment. The source is Ruodu Wang, *Current Open Questions in Complete Mixability* (2015), Open Problem 6. The owning track subsequently exhausted its permitted HARD recovery sequence and rotated, but the canonical claim/handoff remains preserved; there is no explicit release to R7-01.

Disposition: `EXCLUDE_OWNED_OR_RETIRED_ROUTE`.

## 3. D0049 — gamma-LQG Hausdorff dimension is HARD, not CLOSABLE

The intake/catalog identifies `D0049` as the problem of determining the Hausdorff dimension `d_gamma` of a `gamma`-LQG metric space (equivalently the relation between the metric exponent parameters) beyond the special solved case. This is a global LQG exponent problem, not a finite certificate, exact finite construction, sharp one-parameter boundary theorem with a short route, or one-witness counterexample.

Disposition: `OPEN_OR_UNVERIFIED_BUT_HARD_NOT_CLOSABLE`.

No current-source claim is made here beyond the operational fact that it is not suitable for this CLOSABLE slot.

## 4. D0058 — critical Derrida-Retaux moment asymptotics is HARD

The intake identifies `D0058` as Conjecture 3 in the critical Derrida-Retaux recursion package: moment asymptotics in the critical regime. Current neighboring admission work already classifies it as part of the hard critical asymptotic package. It requires asymptotic control of the recursion rather than an isolated finite certificate or short exact counterexample.

Disposition: `HARD_ASYMPTOTIC_NOT_CLOSABLE`.

## 5. D0060 — one-ended nonamenable percolation conjecture is a famous HARD problem

Outside source recovered: Russell Lyons, *Phase Transitions on Nonamenable Graphs*, Journal of Mathematical Physics 41 (2000), arXiv `math/9908177`, Conjecture 3.6. The source question is the one-ended transitive nonamenable percolation conjecture asserting `p_u(G) < 1` under the stated transitivity/nonamenability/one-end hypotheses.

Fresh bounded literature check dated 2026-09-18 recovered the primary Lyons survey and later strong partial results in important subclasses, including hyperbolic/quasi-transitive regimes and modern nonamenable percolation work, but no general theorem matching the full source quantifiers. A search miss is not proof of openness; the relevant admission conclusion is narrower: this remains a famous theorem-scale percolation problem and is not honestly CLOSABLE for R7-01.

Primary source URL: `https://arxiv.org/abs/math/9908177`.

Disposition: `HARD_FAMOUS_NOT_CLOSABLE`.

## 6. D0067 — actively claimed elsewhere

`D0067` is Grimmett-Li's self-avoiding-walk successive-ratio problem. A canonical `operations/claims/D0067.md` exists for native `6aa7b53b0858819196d923203522c996` and classifies the target as HARD OUTSIDE. The claim is current repository ownership evidence; R7-01 may not duplicate it.

Disposition: `EXCLUDE_CANONICAL_CLAIM`.

## 7. D0076 — correct shard-0 locality question, but broad/HARD

Outside source recovered: Geoffrey R. Grimmett and Zhongyang Li, *Self-avoiding walks and connective constants* (2017), arXiv `1704.05884`, Question 7.1, Section 7.1, PDF p. 22. The source asks under what conditions local convergence of quasi-transitive graphs (`K(G,G_n) -> infinity`) forces convergence of connective constants `mu(G_n) -> mu(G)`.

The source itself describes only a partial answer based on unimodular graph height functions. The dedicated Grimmett-Li locality paper proves locality under an additional height-function-type condition; later height-function work expands the class but does not turn the survey's broad “under what conditions” request into a single short endpoint.

Fresh bounded check dated 2026-09-18:

- source: `https://arxiv.org/abs/1704.05884`;
- locality theorem: `https://arxiv.org/abs/1412.0150`;
- repository/primary abstracts still describe the result as a locality theorem subject to an additional unimodular graph-height-function condition.

This is therefore a genuine broad locality programme, not a clean CLOSABLE source statement for this slot. The previous cursor's `D0075` was a shard error; `D0076` is the correct ID and is rejected on classification, not ownership.

Disposition: `HARD_BROAD_NOT_CLOSABLE`.

## 8. D0085 — random planar-map no-macroscopic-faces problem is HARD

The intake and independent admission screens identify `D0085` as Gwynne-Holden-Sun's random-planar-map embedding problem asking for a no-macroscopic-faces/scaling-limit statement. Its source-level endpoint is an asymptotic embedding theorem, not a finite witness or short exact theorem.

Disposition: `HARD_ASYMPTOTIC_NOT_CLOSABLE`.

## 9. D0094 — fast-phase ARW odometer tightness remains hard-shaped

Outside source recovered: Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), 478-544, Third Open Problem after Theorem 6.1, Section 6, PDF p. 30. The source asks for tightness of the single-site odometer on finite cycles in the fast phase.

Primary source record: `https://doi.org/10.1214/19-PS339`.

Fresh bounded 2026-09-18 searching recovered the 2020 survey and later 2026 ARW progress on different questions (for example explosivity above criticality in one dimension), but no source-matching theorem settling this finite-cycle odometer-tightness endpoint. That is negative evidence only. The repository's prior exact attempt identifies a genuine structural obstruction: finite-box/domain monotonicity does not pass to the conservative quotient cycle, and the available total-toppling bound does not directly yield uniform one-site tightness.

Disposition: `OPEN_LOOKING_BUT_HARD_NOT_CLOSABLE`.

## 10. Live QUEUE shard-0 inventory is also exhausted by ownership/scope

Applying the exact character-sum rule to the current visible `QUEUE.md` rows gives the relevant shard-0 queue IDs:

- `I0035`: canonical claim/reservation owned by C31;
- `I0087`: no safe fresh-open source scope; prior current-status work says it is not a lawful fresh-open successor;
- `I0001`: canonical HARD claim exists;
- `I0008`: canonical HARD claim exists;
- `I0062`: canonical P11 claim and source-level refutation package/history exist;
- `I0078`: canonical C27 successor claim exists.

Thus no current high-priority queue row in R7-01's shard is simultaneously CLOSABLE, current-scope-safe, and unclaimed.

The current queue's dated historical READY labels do not override these later claims/status corrections.

## 11. Admission result and next cursor

No candidate in this corrected D pass or the current visible queue satisfies all of:

1. exact shard 0;
2. outside source with frozen source-level quantifiers;
3. genuinely CLOSABLE under the owner's current policy;
4. current literature not already resolving/absorbing the endpoint;
5. no canonical claim/reservation/hold/retirement;
6. enough source evidence to justify a create-only ownership claim.

Accordingly:

- active target remains `PENDING_ADMISSION`;
- no claim is created;
- no source mathematical metric is started;
- successor metric remains `UNKNOWN/UNMEASURED`;
- successor stagnation count remains `NOT_STARTED`;
- no Section-B research triple is charged.

The next cumulative pass should not repeat the D family or the visible queue rows above absent a material status/ownership change. It should enumerate the next still-unscreened shard-0 canonical intake rows outside the already-covered D/E/F/G/H material, with exact ID arithmetic first and source/current-literature/ownership checks second. A new target begins mathematical work only after admission.
