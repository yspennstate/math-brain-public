# R7-04 shard-3 extended successor-admission screen — 2026-09-18

Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum; no authenticated runtime model/effort telemetry or binding selector is exposed.

## Snapshot and continuity

- repository: `yspennstate/math-open-problems`
- branch: `master`
- captured start SHA: `742f9ab21d7e73d8a5dcb5d388b6ec86249b8320`
- slot: `R7-04`
- native ID recovered from `operations/research7_2026-09-17/REGISTRY.md`: `6aabe7ea6e1881919a65503f8445a813`
- own root: `research7_2026-09-17/R7-04/`
- previous report: `research7_2026-09-17/R7-04/runs/2026-09-18/2026-09-18T112814Z__report.md`, creation commit `20fbfb396f42586b007400d53ef766be7aeecfdd`
- previous target `F0106` is terminally handed off/retired after six ordinary unchanged runs; this screen does not reopen it or inherit its metric.
- successor state entering this screen: `PENDING_ADMISSION`; successor metric `UNKNOWN/UNMEASURED`.

The controlling owner directive, visible fleet, `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, current claims, registry, newest own report/handoff, and relevant intake records were re-read at the captured snapshot. Exact shard rule remains `sum(ord(c) for c in canonical_id) % 7 == 3`.

## Extended residue-3 census

This pass extends the prior top-of-queue screen down older intake rows instead of re-counting the same pending rows.

Already excluded by live ownership, retirement, known resolution, or source shape include:

- `D0009`: already canonically owned elsewhere.
- `D0011`: canonically owned by R12; HARD outside.
- `D0018`: remaining Brownian-sheet simultaneous-slice statement is theorem-scale/HARD; previous source reconciliation settles only a dimension-specific part.
- `D0020`: broad hyperbolic-SPDE slice theory, not a short finite-certificate target.
- `D0027`: former R7-04 route with its own six-run terminal handoff; RETIRED for this slot.
- `D0036`: previously claimed HARD route with terminal handoff/retirement history.
- `D0045`: fresh fleet source review found a broad, later-literature-rich question rather than a crisp unresolved predicate; NOT CLEAN CLOSABLE.
- `D0054`: high-dimensional log-correlated random metric programme; HARD-shaped.
- `D0063`: fleet literature reconciliation records it as resolved in later GMC literature.
- `D0072`: canonically claimed by P20 and already has independent audit artifacts.
- `D0079`, `D0081`, `D0088`, `D0090`, `D0097`: asymptotic LQG/planar-map/ARW theorem programmes, not honest CLOSABLE finite-certificate targets for this slot.
- `D0002`: source Open Problem 2 asks for a *generic proof method* unifying several complete-mixability theorems. The repository already has a partial orbit construction, but the source is methodological and open-ended rather than a single source-level yes/no theorem, so it is not a clean CLOSABLE successor.

The earlier shard-3 census also remains binding for the I/E/F/G/H candidates already screened: claimed/reserved rows stay unavailable; resolved rows stay excluded; broad famous conjectures stay HARD rather than being relabeled CLOSABLE. No stale claim status or disabled schedule was treated as release.

## Deep source check: `D0101`

### Exact outside source

Leonardo T. Rolla, **“Activated Random Walks on $\mathbb Z^d$”**, *Probability Surveys* 17 (2020), 478–544, DOI `10.1214/19-PS339`, arXiv `1906.05037v2` (28 September 2020).

Primary source URL: https://arxiv.org/abs/1906.05037

The source page itself was inspected at printed page **517** (PDF page index 39). The exact fourth open problem in Section 8 is:

> **Open Problem. When does $\mathbb P(m(0)\ge 1)=1$ imply $\mathbb P(m(0)=\infty)=1$?**

This corrects two intake-level ambiguities:

1. the authoritative printed locator is page 517 (the repository intake labels it “PDF p. 40” because of PDF/page-index conventions);
2. the exact source sign is **`>= 1`**, not `> 1` (one text extraction garbles the glyph, while the page image is unambiguous).

The surrounding model permits `0 < lambda <= infinity`, and Section 8 is formulated for the standard infinite-volume site-wise odometer under translation-ergodic initial states.

### Counterexample-first obstruction to a universal reading

There is an elementary source-valid obstruction showing that `D0101` is not secretly the universal implication “positive odometer implies infinite odometer” over the whole stated parameter range.

**Lemma (infinite-sleep-rate obstruction).** Let `lambda = infinity` and take the deterministic translation-ergodic initial state having exactly one active particle at every site of `Z^d`. Then

`m(x)=1` for every site `x` almost surely.

**Proof.** At `lambda = infinity`, whenever a lone active particle topples, its first legal action is to sleep with probability one. Initially every site contains exactly one active particle and is unstable. In any finite stabilization volume, topple each site once. No jump is produced; each active singleton becomes one sleeper, hence every site in the volume is stable after exactly one toppling. By the abelian property this is the finite-volume stabilizing odometer. Passing through the standard increasing-volume definition gives `m(x)=1` at every fixed site. Therefore `P(m(0)>=1)=1` while `P(m(0)=infinity)=0`. QED.

So any honest theorem answering the source must specify *conditions* that exclude this and other possible finite-odometer regimes. That is exactly why the author phrases the item as “When does …?”, rather than as a binary conjecture.

### Dated later-literature check — 2026-09-18

A bounded current search was performed around the exact odometer dichotomy, Rolla’s survey, later author work, and citing ARW literature.

- Tobias Johnson and Jacob Richey, **“The odometer in subcritical activated random walk”**, arXiv:2510.05514 (7 October 2025), proves stretched-exponential odometer tails and finite mean below criticality on `Z` for i.i.d. Bernoulli initial data. Its introduction explicitly describes this as progress on Rolla’s *preceding* expected-odometer question (page 517), not as a solution of the `P(m(0)>=1)` versus `P(m(0)=infinity)` classification.
- Nicolas Forien, Christopher Hoffman, Tobias Johnson, Josh Meisel, Jacob Richey, and Leonardo T. Rolla, **“Explosivity in 1-d Activated Random Walk”**, arXiv:2601.03411 (2026), proves a different nearby Rolla conjecture: supercritical ergodic sleeping states in one dimension can trigger an infinite avalanche after activating a particle. This advances the *second* Section-8 open problem on page 517, not the fourth odometer dichotomy.
- Balazs Rath, Jacob Richey, and Miklos Salanki, **“Law of large numbers for activated random walk on villages”**, arXiv:2605.06887 (7 May 2026), studies a dissipative finite-village model and does not supply the requested infinite-volume classification.

No exact resolution of the fourth page-517 open problem surfaced in this bounded search. This is negative evidence only; worldwide current openness and novelty remain UNVERIFIED.

### Ownership / alias check

- `operations/claims/D0101.md` does not exist at the captured master snapshot.
- repository search for the exact title/ID found intake/campaign references but no canonical competing claim or demonstrated alias owner.
- `D0101` is distinct from the already-owned canonical ID `I0101`; exact case-sensitive canonical IDs are not interchangeable.

Ownership therefore looks clear, but ownership alone is insufficient for admission.

## Admission decision

**DO NOT CLAIM `D0101` in this run.** Classification for this slot: **SOURCE OPEN-LOOKING / BROAD CLASSIFICATION QUESTION / NOT CLEAN CLOSABLE**.

Reason: the source does not specify one fixed class of initial states or one necessary-and-sufficient criterion to prove. Its literal closure criterion is a characterization of the conditions under which the implication holds. The exact `lambda=infinity` example above already defeats a universal interpretation. Admitting it as CLOSABLE would silently narrow the quantifiers and violate source scope.

No alternative unclaimed shard-3 candidate in the bounded extended census simultaneously passed (i) exact current source scope, (ii) current-open check, (iii) ownership/release check, (iv) CLOSABLE classification, and (v) a plausible finite construction/coupling/short-theorem closure route.

Accordingly R7-04 remains **PENDING_ADMISSION**. No canonical claim was created, no predecessor metric was inherited, and no Section-B research triple is charged to a fictitious target.

## Successor metric

`UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`.

This is intentionally not replaced by a count of screened rows: screening throughput is not a mathematical source metric.

## Next admission action

Continue the residue-3 cursor with newly appearing or previously under-specified exact canonical candidates, prioritizing sources whose literal statement is a finite construction, explicit counterexample request, fixed coupling, or short theorem. Recheck fresh master before any future create-only claim.