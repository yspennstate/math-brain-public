Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-02 — post-C0134 shard-1 low-tier admission screen

Date: 2026-09-19 UTC  
Repository: `yspennstate/math-open-problems`  
Branch: `master`  
Native slot identity: `6aabe797a39081919acc889f29f4c556`  
Category: `CLOSABLE OUTSIDE`  
State entering screen: `PENDING_ADMISSION` after the immutable C0134 six-run handoff.

## 1. Snapshot and continuity

Run-start master was captured as

`da28736a5b97a8bb69b97e68e033ca9808435a71`.

The previous own report is

`research7_2026-09-17/R7-02/runs/2026-09-19/2026-09-19T012400Z__report.md`

with creation commit

`590ca571f7a82889f59f020261c653177042a323`.

That report terminally retired/handed off `C0134` after six ordinary unchanged runs and returned this slot to `PENDING_ADMISSION`; its successor metric is `UNKNOWN/UNMEASURED` and there is no inherited successor stagnation count.

Before this screen I reread the owner directive, visible-fleet state, root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md` and `RANKING.md`, the R7 registry, the latest own report, the prior R7-02 successor screens, relevant intake records, canonical claim locations, and useful neighboring admission screens. The older R7-02 screen had already exhausted the residue-1 D/E/F/G/H/I frontier. This invocation therefore did not repeat that work; it advanced into the low-ranked C/Claude and Codex P frontier.

## 2. Exact shard rule and bounded frontier examined

Eligibility is the owner's literal rule

`sum(ord(c) for c in ID) % 7 == 1`

using the exact case-sensitive canonical candidate ID.

I used the campaign's ranked low-tier list because the slot must be genuinely CLOSABLE and should prefer exact constructions/counterexamples/certificates over broad asymptotic programs. Within the current Tier 1 and Tier 2 inventory, the complete shard-1 frontier is:

### Tier 1

- `P0342` — transferring a stationary fringe-process CLT to finite critical beta-splitting trees.

### Tier 2

- `C0035` — determinantal trigonometric-polynomial symbols as block factors;
- `C0062` — finite-n maximal-dimension Young diagrams;
- `C0100` — sandpile height-fraction/identity scaling limits;
- `C0134` — the retired R7-02 positive-cookie ballisticity target;
- `P0088` — matching local limits of Bernoulli and Poisson-outdegree attachment;
- `P0090` — multistate pivot-tree interpretation criterion;
- `P0234` — simultaneous protection of an extended initial color seed;
- `P0439` — server provisioning for a response-time quantile SLO;
- `P0441` — deterministic DelayedOff waiting/power tradeoff.

This is a new bounded screening tranche for R7-02: no Tier-1/2 shard-1 C/P candidate was silently skipped.

## 3. Candidate-by-candidate disposition

### P0342 — closest apparent counterexample target, but not admissible

Source record: Aldous–Janson beta-splitting overview, Open Problem 12, PDF pp.44–45. The intake asks whether a CLT for a functional along the stationary infinite fringe process necessarily transfers to the corresponding sum over the leaves of `DTCS(n)`.

The repository already contains an explicit bounded continuous functional

`probability_campaign_2026_09/codex_20h_20260906/proofs/P0342_beta_tree_fringe_transfer_scope_counterexample.md`.

For the stationary infinite fringe tree its normalized sums are identically zero, hence have a degenerate Gaussian limit, while for the finite tree the normalized sums equal

`n^(1/4) (B_n-p_n)`

with `p_n -> 1/2`, and are therefore not tight. This is a genuine obstruction to an unrestricted transfer theorem.

It is not safe to freeze that as full source closure. The existing packet itself records the unresolved interpretation: if “CLT” is intended to mean strictly positive limiting variance, or if the functional is implicitly required to depend on a fixed/local fringe neighborhood, this construction does not settle the intended question. The current ledger consequently records `candidate_partial_counterexample`, not a full source-level refutation. Admitting it by choosing the degenerate-Gaussian reading would silently narrow/resolve an ambiguity instead of preserving full source scope.

There is no canonical `operations/claims/P0342.md` at the final pre-write master, and a bounded repository ownership search found no active claim/reservation. That removes an ownership obstacle but not the source-scope obstacle. A neighboring 2026-09-17 CLOSABLE admission screen independently classified P0342 as an infinite CLT/scaling problem rather than a short finite-certificate target.

**Disposition:** not admitted; `SOURCE_SCOPE_AMBIGUOUS_AND_RESIDUAL_THEOREM_NOT_CLOSABLE`.

### C0062 — finite/combinatorial flavor, but source package is not a finite certificate

Source: Dan Romik, *The Surprising Mathematics of Longest Increasing Subsequences*, manuscript dated 20 August 2014, Section 1.18, p.64 of the book / PDF p.74. The source asks for three things: a precise finite-n description or efficient algorithm for the maximal-dimension partition, uniqueness, and improved asymptotic bounds.

The repository's 2026-09-09 exact campaign is substantial rather than a blank finite search. It exhaustively recomputed maxima through `n<=90`, cross-checked dimensions against OEIS data, tested several one-box structural rules, and retained an unproved stronger single-box-move conjecture. It also recovered prior exhaustive literature tables through `n<=130` and OEIS values through `n<=153`; a 2023 paper reports structural experiments up to `10^6` boxes without proving the general structural conjecture.

There is also a scope issue: `dim(lambda)=dim(lambda')` by the hook-length formula, so literal uniqueness can only mean uniqueness up to conjugation unless the maximizer is self-conjugate. The source is therefore a universal all-n structural/algorithmic/asymptotic research package, not a bounded finite certificate whose exhaustive verification would close the source statement.

No canonical `operations/claims/C0062.md` exists at the final pre-write master, but absence of a claim is not sufficient for admission. A neighboring CLOSABLE screen on 2026-09-17 reached the same classification after a bounded current literature check: still a research program, with substantial prior campaign history.

**Disposition:** not admitted; `BROAD_ALL_N_STRUCTURAL_PROGRAM_WITH_SUBSTANTIAL_PRIOR_ATTEMPT`.

### C0035

Source question: for every trigonometric polynomial `f:T->[0,1]` of degree `m`, is the stationary `m`-dependent determinantal process `P_f` an `(m+1)`-block factor of iid? The source records only `m=1` as known. This is a universal representation theorem over arbitrary degree and coefficients, not one finite instance/certificate.

**Disposition:** `HARD_STRUCTURAL_UNIVERSAL`, not CLOSABLE.

### C0100

The source asks for convergence of local sandpile height fractions under lattice scaling and also the scaling limit of the identity element. Both are asymptotic scaling-limit statements on growing lattices.

**Disposition:** `HARD_ASYMPTOTIC_SCALING`, not CLOSABLE.

### C0134

This is the immediately preceding R7-02 target. It reached candidate source-level mathematical completion but was terminally retired/handed off after the sixth ordinary unchanged run, with audits/prior-art/package synchronization still outstanding. The owner rule explicitly forbids treating retirement or a disabled schedule as release.

**Disposition:** `RETIRED_OWN_ROUTE_DO_NOT_REOPEN`.

### P0088

The source asks to identify/match local weak limits of two preferential-attachment model families. Even though the matching parameter problem is concrete, closure is an asymptotic local-limit theorem over a model family.

**Disposition:** `ASYMPTOTIC_MODEL_FAMILY`, not CLOSABLE.

### P0090

The source asks for a multistate extension of the pivot-tree interpretation criterion for arbitrary finite color sets (including critical/supercritical cases without positive regularity). This is a general structural classification theorem, not a finite instance.

**Disposition:** `GENERAL_CRITERION_PROGRAM`, not CLOSABLE.

### P0234

The source asks whether a limiting random blue region avoids an entire initial red segment/ball. The known pointwise protection mechanism does not give the required simultaneous continuum statement. Closure requires a uniform stochastic-geometric theorem, not a finite certificate.

**Disposition:** `CONTINUUM_UNIFORMITY_THEOREM`, not CLOSABLE.

### P0439

The source asks for the minimum server count and a scheduling policy meeting a response-time quantile under a specified stochastic workload, with general service laws and policy choice part of the target. This is a parameterized stochastic-control/optimization program rather than one frozen finite proposition.

**Disposition:** `BROAD_QUEUEING_OPTIMIZATION`, not CLOSABLE.

### P0441

The source asks to analyze waiting and power for deterministic setup under a DelayedOff grace interval. It does not freeze one exact claimed formula/constant whose certification would close the question; it is a policy-performance analysis program.

**Disposition:** `EXPLORATORY_POLICY_ANALYSIS`, not CLOSABLE.

## 4. Source-current gate

The task requires a current primary-source/later-literature check before any admission. This run is GitHub-only by owner instruction. The repository contains dated source/literature checks through 2026-09-17 for several of the closest rows, and the C0062 exact memo records literature through the 2023 Duzhin–Smirnov-Maltsev paper plus later repository screening. It does not contain a new 2026-09-19 primary-source/citation update establishing worldwide current openness for P0342 or C0062.

Therefore even the two closest candidates would retain `CURRENT_OPEN=UNVERIFIED` under this run's permitted information boundary. A repository search miss is not treated as proof of novelty or current openness.

## 5. Final-master recheck

Before writing this screen I re-read `master`. It had advanced from the run-start SHA to

`759e99c3e471e6d34f9ec94a6be93e3bc1ff945e`.

The new tip is an unrelated P0063 audit-gate report under `proofnet24/HARD10-01/...`; the commit adds no root ledger, intake, R7-02, or canonical claim file and does not alter any candidate disposition above. No collision/release event was inferred from that unrelated change.

## 6. Admission decision and metric

**Decision: remain `PENDING_ADMISSION`. No canonical claim is created.**

No current shard-1 Tier-1/2 candidate simultaneously satisfies:

1. genuinely outside source;
2. exact residue-1 identity;
3. source-current status sufficiently evidenced under the GitHub-only boundary;
4. no controlling ownership/retirement conflict;
5. honest `CLOSABLE OUTSIDE` shape with a source-matching finite/exact endpoint.

The successor metric remains unfrozen:

- before: `UNKNOWN/UNMEASURED`;
- after: `UNKNOWN/UNMEASURED`;
- mathematical movement: none, because no source is admitted;
- successor stagnation count: `NOT_STARTED`;
- stuck-recovery count: `0`.

No Section-B research method is charged in this admission-only screen. In particular, screening or reclassifying a source is not counted as mathematical progress on an admitted target.

## 7. Durable next cursor

Do not repeat the already exhausted D/E/F/G/H/I shard-1 screen or this Tier-1/Tier-2 C/P screen absent a source/status/ownership change.

Next lawful work should be one of:

1. inspect newly added/changed shard-1 intake rows after this snapshot;
2. among shard-1 Tier-3 rows, inspect only entries whose literal source form is an explicit finite construction/counterexample/exact certificate despite their rank, rather than bulk-screening broad asymptotic programs;
3. if a source-current update makes P0342's intended CLT scope explicit, re-evaluate it from that exact source wording rather than silently choosing the degenerate-normal interpretation;
4. if no candidate passes all gates, remain `PENDING_ADMISSION` and advance the bounded cursor without inventing a surrogate target.

This screen is continuity evidence only and pre-authorizes no future claim.
