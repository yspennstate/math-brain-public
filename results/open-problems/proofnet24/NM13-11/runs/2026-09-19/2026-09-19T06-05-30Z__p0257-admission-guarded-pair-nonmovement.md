Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MATHEMATICAL MOVEMENT after baseline recovery: `b_NUV >= 0.6277 -> b_NUV >= 0.6277`; Section-B methods #2 / #4 / #8 were genuinely attempted.**

# NM13-11 — P0257 admission and first substantive run

Date: 2026-09-19 UTC  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker / namespace: `NM13-11` / `proofnet24/NM13-11/`  
Category: **HARD OUTSIDE**  
Exclusive shard: `int(SHA256(UTF-8 canonical dedup_key).hexdigest(),16) mod 13 = 10`

## 1. Result

This invocation **crossed admission** on `P0257`, David Aldous's first-order nearest-unvisited-vertex (NUV) length problem in the Euclidean random-points model, after repairing the legacy-P cursor through `P0285` and checking source identity, canonical shard, current literature, prior attempts, claims, current/historical assignments, handoffs, POSTED/campaign exclusions, and exact ownership.

The canonical claim was created with create-only semantics at

`operations/claims/P0257.md`

commit

`d1c344833343eed0e7e292d28dffd49833b8519d`

and read back at that exact commit before substantive work continued.

The source remains **OPEN**. This run produced a rigorous source-valid local trapping lemma and an exact finite guarded-block transfer, but they **do not move the frozen metric** once the current TSP lower-bound literature is correctly folded into the baseline.

The frozen metric is

`b_NUV = explicit certified lower endpoint in liminf_{n->infinity} E[L_n]/n >= b_NUV`

for the source Euclidean random-points model under Aldous's area-`n` scaling.

Admission baseline was `UNMEASURED`, as required. During the first substantive pass I recovered the actual prior-art baseline:

`b_NUV >= 0.6277`,

because every NUV path is at least the optimal Euclidean Hamiltonian path and the best checked rigorous lower bound for the planar Beardwood-Halton-Hammersley traveling-salesman constant remains `0.6277`. The path/tour closing-edge discrepancy is `o(sqrt(n))` in the unit-square normalization, so the same asymptotic constant applies.

My new guarded-mutual-pair argument proves only

`liminf E[L_n]/n >= 1/2 + 3(sqrt(6)-sqrt(3)) exp(-3/2)/12500`

`= 0.5000384197434826606...`,

which is valid but strictly weaker than `0.6277`. Therefore the research metric is **0.6277 -> 0.6277, no movement**. I do not relabel prior-art recovery as research progress.

Status after run: **PARTIAL / OPEN / UNCHANGED METRIC**.

Admitted-target counters:

- unchanged runs after baseline recovery: **1**;
- stuck-recovery episodes: **0 / 2**;
- audits: **not requested / not applicable for closure**;
- designated eventual auditors remain P26 and NM13-12; neither is presumed to have audited or passed anything here.

## 2. Runtime / scheduler-control truth

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. The runtime exposes no authenticated reasoning-effort telemetry, so reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still provides task identity/title, prompt, schedule/start fields, timing mode, enabled state, listing and update operations, but **no bindable model-family selector, no bindable reasoning-effort selector, and no authenticated per-run applied-model/applied-effort attestation**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin scheduling surface that persists those fields into inference routing and returns trustworthy per-run attestation.

The historical P26 response `You cannot modify this task` is an authorization-context boundary. The lawful workaround is the owning or otherwise authorized account/workspace/API/admin context, or authorized platform support for that same task. It is not permission to duplicate the task or bypass access controls. This invocation made **no scheduler or permission change**.

## 3. Continuity and required repository reads

The controlling predecessor was

`proofnet24/NM13-11/runs/2026-09-19/2026-09-19T05-00-00Z__legacy-p-cursor-repair-screen-17.md`

at creation commit

`79451485d942d5b34a4213d560caca0386ec2581`.

Its durable state was:

- `ADMISSION_PENDING`;
- successor metric `UNMEASURED`;
- initial methods #2/#4/#8 unspent;
- terminal predecessor E0082 ownership preserved with historical `unchanged_runs=4`, `stuck_recoveries=2/2 consumed`; E0082 not restartable;
- legacy-P reconciliation repaired through `P0223`;
- next screening cursor `LEGACY_P_RECONCILIATION_NEXT=P0224`.

Before selecting P0257 I freshly read or exact-target-recovered:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the predecessor NM13-11 report;
- newest neighboring NM13-10 report `proofnet24/NM13-10/runs/2026-09-19/2026-09-19T05-59-30Z__admission-screen-35-legacy-p-repair-through-p0488-no-ready.md`;
- newest visible neighboring/designated-secondary-audit-partner NM13-12 report `proofnet24/NM13-12/runs/2026-09-19/2026-09-19T04-58-30Z__post-e0086-admission-delta-screen-15-p0219-claimed-elsewhere.md`;
- the canonical campaign source catalogue and dedup index for `P0224--P0285`;
- the P0257 prior-attempt/rank-sheet and detailed campaign catalogue entry;
- exact claim-path probes and repository-wide P0257/dedup-key searches;
- the original Aldous source and current public literature described below.

The append-only intake and attempt corpora are too large to claim that every unchanged historical byte was freshly rendered model-visible in one invocation. I make no such claim. Candidate-specific canonical rows and prior-attempt material were freshly recovered, and the exact predecessor-to-prewrite Git delta below shows no changed intake `problems.jsonl`, root source-selection ledger, or controlling policy that invalidates the carried history.

No private-repository history material to the P0257 ownership decision was known to be inaccessible.

## 4. Exact repository delta before the report write

Frozen pre-report `master` snapshot:

`b0568b0becdb4b5b9a4c81c24a92fb761e0ed128`.

Exact comparison:

`79451485d942d5b34a4213d560caca0386ec2581 .. b0568b0becdb4b5b9a4c81c24a92fb761e0ed128`

GitHub reports:

- status: `ahead`;
- ahead: **112 commits**;
- behind: **0**;
- total commits: **112**;
- `too_large = null`, so the returned changed-file list is complete for this interval.

No changed file in the interval is root `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, an intake `problems.jsonl`, a probability attempt ledger, or a controlling owner/NM13 policy file.

Other canonical claims added in the interval and already owner-bound are:

- `F0095`;
- `KIM-MATTMAN-OH-2026-TFIK22-D34`;
- `ROMERO-2025-SPLIT8`.

NM13-11's own create-only P0257 claim is the fourth new claim in the final interval. No canonical claim deletion or owner-authorized release was observed.

## 5. Legacy-P reconciliation `P0224--P0285`: exact residue-10 tranche

I used canonical `dedup_key` strings from the source catalogue, not display aliases. The open/nonterminal residue-10 rows in this tranche are exactly:

1. `P0225` — `attainment_of_the_optimal_sirsn_length-stretch_tradeoff`;
2. `P0226` — `local_finiteness_of_scale-invariant_network_traffic_measures`;
3. `P0243` — `sharp_constant-one_comparisons_of_reversible_mixing_and_stopping_parameters`;
4. `P0257` — `law_of_large_numbers_and_constants_for_nuv_lengths`.

For P0257 the canonical SHA-256 is

`75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5`,

and its integer value is residue **10 modulo 13**.

Disposition of the other three:

- **P0243** is excluded as settled: campaign INDEX records Aldous-Fill Open Problem 4.48 with (a) false and (b) true, and its detailed attempt packet says the source problem is settled as posed. Absence of a current claim file does not reopen a settled source.
- **P0225** remains a broad SIRSN attainment/optimizer-existence problem. Its prior attempt obtained tightness only for unlabelled length measures and explicitly lost route labels/compatibility/allowed-curve structure. No source-fixed finite or scalar endpoint suitable for this HARD worker was recovered.
- **P0226** remains a broad local-finiteness problem for scale-invariant traffic measures. Its prior attempt obtained a Tonelli/expectation calculation but explicitly noted that divergent expectation neither disproves almost-sure local finiteness nor answers the source's restricted-major-road issue. Again there is no honest source-fixed finite/scalar endpoint.

P0257 was selected despite a prior attempt because it is the first row in the repaired tranche with all of: ownership-clear status, exact source identity, explicit source quantity `c`, a quantitative source model, and a plausible finite local-event route. The user's preference for previously unattempted sources is a preference, not a requirement; none of the three alternative residue-10 rows in this tranche was a stronger lawful fit.

If this claim later rotates, the legacy selection cursor resumes at **`P0286`**, not at P0224 and not in old delta-only mode.

## 6. Exact P0257 source and ownership gate

Canonical source identity:

- source ID: `P0257`;
- canonical key: `law_of_large_numbers_and_constants_for_nuv_lengths`;
- source: David J. Aldous, *The Nearest Unvisited Vertex Walk on Random Graphs*, arXiv:1912.13175, later *Probability in the Engineering and Informational Sciences* 36 (2022), 851–867;
- source locator: Equation (4), source Section 3 / campaign PDF p. 9, plus Section 5 and the companion talk.

The source's Euclidean model is the complete graph on `n` i.i.d. uniform points in the unit square with Euclidean lengths. Aldous writes `L_n = sqrt(n) L_n^*` after scaling the square to area `n` and proposes

`c := lim_n n^{-1} L_n = lim_n n^{-1/2} L_n^*`.

The source simulation is near `c ~= 0.9`; the source says its Corollary 3 gives only an `O(n)` expectation bound and that sharper limit/concentration statements are difficult.

Prior repository attempt status: `attempted_unsolved`. The recorded prior route was the deterministic nearest-neighbor inequality

`L_NUV >= sum_v d_v - max_v d_v`,

where `d_v` is the nearest-neighbor distance of vertex `v`. Its recorded obstruction was precisely that this supplies only lower constants and does not produce the subadditivity/stabilization needed for the source limit.

Exclusive ownership checks before create:

- `operations/claims/P0257.md` returned 404 immediately before the create-only operation;
- repository-wide exact-ID and exact-dedup-key searches found intake/campaign/source records but no proofnet24 owner/claim/handoff under another canonical identity;
- P0257 does not appear as PROVED/REFUTED/KNOWN in campaign INDEX/RANKING;
- it is not in POSTED's excluded/written-up registry;
- it is not a retired/exhausted target in current policy;
- no current or historical assignment collision was recovered.

The create-only claim succeeded; it was then read back at commit `d1c344833343eed0e7e292d28dffd49833b8519d`. No owner was overwritten.

## 7. Bounded source / literature check and the baseline correction

Dated 2026-09-19 UTC, public-web queries included:

- `"The Nearest Unvisited Vertex Walk" Aldous latest 2024 2025 2026`;
- `"nearest unvisited vertex walk" law of large numbers constant`;
- `"NUV walk" random points Aldous 2024 2025 2026`;
- `"nearest unvisited" Euclidean random points limit constant`;
- `rigorous lower bound Beardwood Halton Hammersley constant beta TSP planar`;
- `"Euclidean TSP constant" rigorous lower bound`;
- `"mutual nearest neighbors" nearest neighbor heuristic random Euclidean tour lower bound`;
- `"trapping effect" nearest unvisited nearest neighbor tour random points`.

Checked source/status evidence:

1. Aldous's arXiv/source text defines the NUV rule, gives Equation (4), says only the `O(n)` bound is rigorous in the Euclidean random-points model, and explicitly notes `L_NUV >= L_TSP`.
2. Cambridge lists the paper as published online 5 April 2021, journal issue July 2022.
3. No checked 2023--2026 primary source surfaced that resolves the exact NUV Equation-(4) constant. This is bounded negative evidence only, not proof of worldwide openness.
4. The TSP comparison is load-bearing for the metric. Steinerberger's 2015 paper improved the original BHH bounds, and Gaudio--Jaillet's 2019/2020 work gives the rigorous planar TSP lower bound `beta_TSP >= 0.6277`.
5. A February 2026 Gaudio--Guan preprint on an improved TSP upper bound still states `0.6277` as the best known rigorous lower bound while improving the upper bound. Thus this was not stale historical context.
6. A 2024 Transportation Research Part B paper studies lower bounds for random Euclidean tours via a probabilistic "trapping effect". It is not the Aldous NUV source, but it is conceptually adjacent to my local trapped-pair idea. Therefore I make **no novelty claim** for the generic trapping concept. The bounded search did not surface this exact mutual-nearest-pair / NUV Equation-(4) lemma, but negative search is not a novelty certificate.

Why `0.6277` transfers to the frozen NUV expectation metric: the source gives `L_NUV >= L_TSP-path`. The Euclidean optimal path and tour differ by at most one closing segment of length `sqrt(2)` in the unit square, hence by `o(sqrt(n))` after division by `sqrt(n)`. BHH gives the same asymptotic constant for path/tour. Standard deterministic `O(sqrt(n))` Euclidean tour bounds give uniform integrability, so the almost-sure asymptotic lower bound transfers to expectations. Therefore the recovered prior-art baseline is

`liminf E[L_n]/n >= 0.6277`.

This correction occurred before judging mathematical movement. Admission remains lawful because P0257 is still open, ownership-clear and quantitative, but the local route must beat **0.6277**, not merely the old nearest-neighbor floor.

## 8. Section-B #2 — ATTACK THE NEGATION FIRST

I first tried to break the proposed local-trapping correction rather than prove it.

A naive claim that "every isolated mutual-nearest-neighbor pair creates an extra departure gap" is false: if the later endpoint of such a pair is the **final** NUV vertex, it has no departure edge and contributes no gap. This is a genuine finite counterexample to the naive local statement.

The repair is exact and order-independent: disjoint mutual-nearest-neighbor pairs have distinct later endpoints, and there is only one final vertex. Hence among `G` disjoint guarded mutual pairs, at least `G-1` later endpoints do depart. This is the only terminal exception needed below.

I then attacked the stronger hope that one guarded-pair correction could move the actual metric above the recovered `0.6277` baseline. For the whole centered-square one-pair family, let block area be `A=B^2`, central-square side ratio `q=t/B`, and require

`q < 1/(1+2 sqrt(2))`

so that the pair diameter is smaller than the guard margin. The asymptotic correction supplied by this family is

`Delta(A,q) = A^(3/2) exp(-A) * (q^4/2) * (1/2 - q(1/2+sqrt(2))).`

Elementary differentiation gives the family maximum at

`A = 3/2`,

`q = 4/[5(1+2 sqrt(2))]`,

with

`Delta_max = (3/2)^(3/2) exp(-3/2) q^4 / 20`

`~= 0.0000390790123955`.

Thus even the optimized one-pair guarded-square family can only raise the nearest-neighbor `1/2` floor to about `0.5000391`, far below `0.6277`. This route **cannot move the frozen metric**. I stop this route here rather than producing further certificates for it.

Outcome of method #2: **failed to move the metric; useful failure mode identified and the one-pair route is abandoned for metric improvement.**

## 9. Section-B #4 — PROVE SOMETHING WEAKER, COMPLETELY

Although it cannot move the metric, I proved the guarded-pair statement fully because it is the exact mechanism revealed by the negation attack and because it tests whether the route has any rigorous source transfer at all.

### Setup

Let

`Q_n = [0,sqrt(n)]^2`

and let `X_1,...,X_n` be i.i.d. uniform points of `Q_n`. With probability one all relevant distances are distinct. Run the Euclidean NUV walk from any starting vertex and write its first-visit order as

`v_0,...,v_{n-1}`.

Let `D(v_i)=|v_i-v_{i+1}|` for `i<n-1`; then

`L_n = sum_{i=0}^{n-2} D(v_i)`.

For a point `v`, let `rho_1(v)` and `rho_2(v)` be its first and second nearest-neighbor distances in the complete point set.

### Lemma 1: recovered nearest-neighbor floor

For every nonfinal vertex `v_i`, its chosen unvisited successor is some point in the full set, so

`D(v_i) >= rho_1(v_i)`.

Hence, exactly as in the historical P0257 attempt,

`L_n >= sum_v rho_1(v) - max_v rho_1(v)`.

For a fixed sampled point `X_1=x`, if `rho_1(X_1)>r`, no other point lies in `B(x,r) cap Q_n`. Since the intersection area is at most `pi r^2`, for `0 <= r <= sqrt(n/pi)`,

`P(rho_1(X_1)>r | X_1=x) >= (1-pi r^2/n)^(n-1)`.

Integrating the tail gives

`E rho_1(X_1)`

`>= integral_0^{sqrt(n/pi)} (1-pi r^2/n)^(n-1) dr`

`= sqrt(n) Gamma(n) / [2 Gamma(n+1/2)]`

`-> 1/2`.

Also `max_v rho_1(v) <= diam(Q_n)=sqrt(2n)`. Therefore the historical mechanism indeed yields

`liminf E[L_n]/n >= 1/2`.

This measures the old unquantified route but is still dominated by the TSP prior-art baseline.

### Lemma 2: deterministic mutual-nearest-pair correction

Call `{u,v}` a mutual-nearest pair if each is the other's nearest neighbor. Such pairs are vertex-disjoint.

For a mutual pair define

`g(u)=rho_2(u)-rho_1(u)`, `g(v)=rho_2(v)-rho_1(v)`.

Whichever endpoint is later in the NUV first-visit order has its mutual partner already visited. If that later endpoint is not the final NUV vertex, its departure therefore satisfies

`D(w) >= rho_2(w) = rho_1(w)+g(w)`.

Consequently, if a collection of `G` disjoint mutual pairs all has both endpoint gaps at least `h>0`, then at least `G-1` of their later endpoints are nonfinal, and

`L_n >= sum_v rho_1(v) - max_v rho_1(v) + h(G-1)`.

No independence assumption is used here.

### Lemma 3: a guarded block gives one such pair

Take a square block of side

`B = sqrt(6)/2`,

so its area is

`A = B^2 = 3/2`.

Inside it take the centered square of side

`t = sqrt(6)/10`,

with area

`a = t^2 = 3/50`.

Call the block **good** if exactly two sample points lie in the central square and no other sample point lies anywhere else in the full block.

For its two central points:

- their mutual distance is at most the central-square diameter `t sqrt(2)=sqrt(3)/5`;
- every point outside the block is at distance at least the central-to-boundary margin `(B-t)/2=sqrt(6)/5` from either central point.

Thus the two central points are mutual nearest neighbors and both second-neighbor gaps are at least

`h = (sqrt(6)-sqrt(3))/5 > 0`.

### Lemma 4: exact finite good-block probability

Pack

`M_n = floor(sqrt(2n/3))^2`

pairwise disjoint full blocks into `Q_n`. For any fixed full block, multinomial sampling gives exactly

`p_n = C(n,2) (a/n)^2 (1-A/n)^(n-2)`

`= C(n,2) (3/(50n))^2 ((2n-3)/(2n))^(n-2)`.

Therefore, by linearity of expectation regardless of dependence between blocks,

`E G_n = M_n p_n`.

The finite probability identity and exact block-count identity were checked for `n=3,...,500` with rational arithmetic in

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T06-02-16Z__p0257_guarded_pair_exact.py`

with archived output

`proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T06-02-16Z__p0257_guarded_pair_exact.out`,

ending `ALL_EXACT_FINITE_CHECKS_PASS`.

The checker is a self-check of the finite arithmetic only; the theorem is proved on this page.

### Theorem: strict guarded-pair correction over the nearest-neighbor floor

Combine Lemmas 1--4:

`E[L_n]/n`

`>= E[rho_1(X_1)] - sqrt(2/n) + h(E G_n/n - 1/n)`.

Now

`M_n/n -> 2/3`,

and

`p_n -> (a^2/2) exp(-A) = (9/5000) exp(-3/2)`.

Therefore

`liminf_{n->infinity} E[L_n]/n`

`>= 1/2 + h * (2/3) * (9/5000) exp(-3/2)`

`= 1/2 + 3(sqrt(6)-sqrt(3)) exp(-3/2)/12500`.

Numerically the correction is

`3(sqrt(6)-sqrt(3)) exp(-3/2)/12500`

`~= 0.00003841974348266062`,

so the bound is approximately

`0.5000384197434826606`.

Every step above is source-valid for the Euclidean NUV model; the finite-volume event has an explicit asymptotic transfer. No simulation is used in the proof.

### Why this theorem is not metric movement

Current rigorous TSP prior art already gives

`liminf E[L_n]/n >= 0.6277`

through `L_NUV >= L_TSP`. Therefore the theorem is mathematically valid but **non-moving** for `b_NUV`. It is recorded as a failed route result, not promoted as progress on the tracked number and not called globally novel.

Outcome of method #4: **complete restricted theorem; no metric movement because prior art is stronger.**

## 10. Section-B #8 — DISCRETIZE

The guarded-block construction is the discretization route. Its role was not to simulate the asymptotic problem but to create a finite event with an exact probability and a rigorous infinite-volume transfer.

The exact finite ingredients are:

- block area `3/2`;
- central-square area `3/50`;
- block count `M_n=floor(sqrt(2n/3))^2`;
- good-block probability `p_n=C(n,2)(3/(50n))^2((2n-3)/(2n))^(n-2)`;
- deterministic gap `h=(sqrt(6)-sqrt(3))/5`.

The archived rational checker verifies the multinomial formula by two algebraically independent expressions and the integer block-count identity for `n=3..500`. The asymptotic transfer is the proof in Section 9, not the checker.

The discretization succeeded technically but, after the TSP baseline correction, it does not move `b_NUV` and its optimized one-pair family is provably too weak to do so.

Outcome of method #8: **rigorous finite-to-infinite transfer obtained; metric unchanged; route abandoned in this form.**

## 11. What the current obstruction actually is

After this run, the quantitative barrier is not "prove any positive lower constant". The true baseline is already

`b_NUV >= 0.6277`.

A new lower-bound route must therefore prove either

`liminf E[L_n]/n > 0.6277`,

or an exact stronger endpoint.

The one-pair local-trapping correction cannot do this when added only to the nearest-neighbor `1/2` floor. A route that merely files more block probabilities of this same type is now prohibited by the owner's movement rule.

The most plausible next mechanism is to compare the **NUV-specific forced excess over a strong Euclidean lower functional**, not over the nearest-neighbor floor. Concretely, one needs a decomposition in which a positive-density local precedence/trapping penalty can be added to a lower functional already near the TSP constant (for example a 2-factor / Held-Karp / local-degree relaxation) without double counting the same edge length.

That is a genuinely different problem from the route just exhausted.

## 12. Next methods and next step

Do **not** repeat #2/#4/#8 next run. The next run should try three untried methods on P0257:

- **#11 DUALIZE:** formulate a local LP / 2-factor / Held-Karp lower functional with additional NUV precedence constraints; search for a positive dual certificate of NUV-specific excess.
- **#20 FIND WHY THE ALGORITHM FAILS:** isolate the smallest finite point gadget on which every NUV ordering pays strictly more than the best path, with a penalty that survives insertion into a larger configuration.
- **#24 FIND THE EXTREMAL OBJECT:** optimize such a gadget/guard region for penalty per area, but only after proving additivity against the chosen baseline functional.

The target stays P0257. This is only unchanged run 1, so no Section-I stuck recovery is triggered and no handoff/rotation occurs.

If future rotation becomes mandatory, resume the source-selection reconciliation at `P0286`; do not restart the P0224--P0285 tranche.

## 13. Audit / closure status

This run does **not** close P0257 and does not request audit as though it did.

- source status: OPEN;
- track result: PARTIAL / non-moving local theorem;
- finite checker: self-check only;
- prior-art search: bounded and recorded, with adjacent 2024 trapping literature explicitly acknowledged;
- P26 independent audit: **not requested / not passed**;
- NM13-12 independent audit: **not requested / not passed**;
- paper package: not warranted;
- public posting: none.

## 14. Structured ledger delta for P26

```yaml
ledger_delta:
  worker: NM13-11
  category: HARD_OUTSIDE
  run_kind: admission_and_first_substantive_run
  predecessor_report: proofnet24/NM13-11/runs/2026-09-19/2026-09-19T05-00-00Z__legacy-p-cursor-repair-screen-17.md
  predecessor_commit: 79451485d942d5b34a4213d560caca0386ec2581
  prewrite_master: b0568b0becdb4b5b9a4c81c24a92fb761e0ed128
  source_id: P0257
  canonical_dedup_key: law_of_large_numbers_and_constants_for_nuv_lengths
  canonical_sha256: 75bdfbc93f05ad07b271ad7a5a8046a16f0bb29d10236cbc1ebf0b8889fdf5e5
  residue_mod_13: 10
  claim_path: operations/claims/P0257.md
  claim_create_commit: d1c344833343eed0e7e292d28dffd49833b8519d
  claim_readback: PASS
  source_status: OPEN
  track_status: PARTIAL
  exact_model: n iid uniform points in square area n; complete Euclidean graph; NUV walk from uniform random start
  metric_name: b_NUV_explicit_liminf_expectation_lower_endpoint
  admission_baseline: UNMEASURED
  recovered_prior_art_baseline: 0.6277
  metric_before_new_methods: 0.6277
  metric_after: 0.6277
  mathematical_movement: false
  reason_no_movement: guarded-pair theorem gives only 0.5000384197434826606, dominated by TSP lower bound 0.6277
  methods_attempted:
    - 2
    - 4
    - 8
  method_outcomes:
    method_2: found final-vertex exception; repaired it; optimized one-pair block family is quantitatively incapable of reaching baseline
    method_4: proved complete guarded-mutual-pair liminf theorem, non-moving
    method_8: exact finite guarded-block probability plus rigorous infinite-volume transfer, non-moving
  exact_checker: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T06-02-16Z__p0257_guarded_pair_exact.py
  exact_checker_output: proofnet24/NM13-11/artifacts/2026-09-19/2026-09-19T06-02-16Z__p0257_guarded_pair_exact.out
  checker_result: ALL_EXACT_FINITE_CHECKS_PASS
  unchanged_runs: 1
  stuck_recoveries: 0
  hard_recovery_limit: 2
  audits:
    P26: NOT_REQUESTED
    NM13-12: NOT_REQUESTED
  next_methods:
    - 11
    - 20
    - 24
  next_step: seek additive NUV-specific excess over a strong TSP/2-factor/Held-Karp-type lower functional; do not extend one-pair nearest-neighbor blocks
  dormant_selection_cursor_if_rotation: P0286
  shared_root_edits: false
  peer_namespace_edits: false
  scheduler_changes: false
  email_or_drive: false
  public_posting: false
  paid_compute: false
```

## 15. Operational safeguards / write set

This invocation created only:

1. the canonical create-only claim `operations/claims/P0257.md` after the full admission gate;
2. one substantive exact checker and its archived output under `proofnet24/NM13-11/artifacts/2026-09-19/`;
3. this single immutable NM13-11 run report.

No shared root was edited. No peer namespace was edited. No workflow was executed. No permission, email/Gmail, Drive, public posting, paid compute, or schedule was created or modified.
