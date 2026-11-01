Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-01 admission screen — C0133 one-dimensional resolution and P0177 closure ambiguity

## Snapshot and scope

Repository / branch: private `yspennstate/math-open-problems` / existing `master`.

Start-of-run captured master SHA:

`d6a7f46c0c2c5eae754d326a91b908639cc70c47`.

Fresh master before this artifact:

`d694cda7c5ef4b45d4620143bfedcc755b61a5f7`.

Native identity recovered from `operations/research7_2026-09-17/REGISTRY.md`:

- slot `R7-01 Counterexamples and Constants`;
- native ID `6aabe777361481919c9e614646464772`;
- shard gate `sum(ord(c) for c in canonical_id) % 7 == 0`;
- preferred class `CLOSABLE OUTSIDE`.

Newest prior own report:

`research7_2026-09-17/R7-01/runs/2026-09-18/2026-09-18T201023Z__report.md`, creation commit `5abbeb4d349dcc6ceb8053b6a55eefa1de1c3e16`.

That report left the slot at `PENDING_ADMISSION` after rejecting I0071 as a HARD/BROAD full-source programme. The predecessor P0087 remains under its terminal HARD handoff and is not reopened.

This screen advances two exact shard-0 candidates that had not yet been source-reconciled in the current R7-01 successor phase. It does not treat absence of a canonical claim as proof of release.

## Candidate 1: C0133

### Shard and repository record

`C0133`: `67+48+49+51+51 = 266 = 38*7`, so the ID is in shard 0.

Canonical intake:

- title: `Zero velocity on the non-transient event for excited random walks`;
- source ID: `kosygina_zerner_erw_2012`;
- locator: Problem 4.7, p. 19 of the source PDF;
- intake statement: for excited random walk on `Z^d` under iid elliptic cookie environment and direction `ell`, ask whether `X_n·ell/n -> 0` almost surely on the complement of `{|X_n| -> infinity}`.

A fresh direct fetch of `operations/claims/C0133.md` returned 404. Repository search recovered historical intake/catalog work but no current canonical C0133 claim.

The prior attempt `C0133-A001` was also recovered. Its useful content was: Theorem 4.8 does not by itself settle the question; on the non-transient event the walk returns to bounded regions along a subsequence, giving a zero liminf along such times, but that does not exclude linear-size excursions between returns. The recorded obstruction was a missing uniform excursion estimate without bounded-stack control. This is prior work, not new work of this screen.

### Exact outside source

Authors: **Elena Kosygina and Martin P. W. Zerner**.

Title: **Excited random walks: results, methods, open problems**.

Preprint: arXiv:1204.1895 (2012), https://arxiv.org/abs/1204.1895 .

Published version: *Bulletin of the Institute of Mathematics, Academia Sinica (New Series)* 8 (2013), 105–157.

Exact locator: **Problem 4.7**, printed p. 19 of the article/PDF.

The literal source quantifiers are: `d >= 1`; assumptions `(IID)` and `(EL)`; nonzero direction `ell in R^d`; ask whether

`X_n · ell / n -> 0` almost surely on `{ |X_n| -> infinity }^c`.

The source explicitly says this would generalize Zerner's one-dimensional theorem and then states Theorem 4.8 with an extra directional-total-transience hypothesis because Problem 4.7 is not available in full generality.

### Material current-status correction: the d=1 slice is already known

A later paper is directly relevant:

Gideon Amir, Noam Berger, Tal Orenshtein, **Zero-one law for directional transience of one dimensional excited random walks**, *Annales de l'Institut Henri Poincare, Probabilites et Statistiques* 52(1) (2016), 47–57, DOI 10.1214/14-AIHP615.

The paper's abstract states that for a one-dimensional stationary ergodic elliptic cookie environment, directional transience is a zero-one event and, as an application, a law of large numbers holds. It explicitly describes this as solving a problem posed by Kosygina and Zerner. The source assumptions `(IID)+(EL)` are a subclass of stationary-ergodic plus elliptic.

There is a short exact deduction from that LLN to the `d=1` instance of Problem 4.7. Let

`X_n/n -> v` almost surely.

On the event `A = {|X_n| not -> infinity}`, suppose `v != 0`. Then for sufficiently large `n`, `|X_n|/n >= |v|/2`, hence `|X_n| >= (|v|/2)n -> infinity`, contradicting `A`. Therefore `v=0` on `A`, and hence `X_n/n -> 0` on `A`. For either nonzero one-dimensional direction `ell`, this gives `X_n ell/n -> 0`.

Thus the literal `d=1` clause of C0133 is **KNOWN / RESOLVED_IN_LITERATURE** by the 2016 zero-one-law/LLN result. The canonical intake's undifferentiated `d >= 1` open-looking label is too coarse.

### What remains and admission verdict

A bounded current search dated 2026-09-18/19 recovered no later theorem settling the full `d >= 2` Problem 4.7 under exactly `(IID)+(EL)`. This is negative evidence only, not an openness or novelty certificate.

The unresolved remainder is a genuinely multidimensional excited-random-walk theorem. The previous attempted route already identifies the hard phenomenon: non-escape does not automatically preclude arbitrarily large linear excursions followed by returns. There is no source-fixed finite certificate, sharp scalar constant, or short finite classification that would close the remaining `d >= 2` source statement.

**C0133 disposition for this slot: HARD / NOT GENUINELY CLOSABLE.**

No canonical claim is created. The useful result of this screen is the status correction `d=1 KNOWN; only d>=2 remains open-looking`.

## Candidate 2: P0177

### Shard and ownership

`P0177`: `80+48+49+55+55 = 287 = 41*7`, so the ID is in shard 0.

A fresh direct fetch of `operations/claims/P0177.md` returned 404. Search recovered campaign/catalog history but no current canonical P0177 claim.

The campaign tier file ranks P0177 as tier 2 with the note `Brownian mode location at large time; partial asymptotics`, making it a natural closable-looking candidate to inspect before rejecting the shard as empty.

### Exact outside source and source question

Authors: **Takahiro Hasebe and Yuki Ueda**.

Title: **Large time unimodality for classical and free Brownian motions with initial distributions**.

Published in *ALEA, Latin American Journal of Probability and Mathematical Statistics* 15 (2018), 353–374, DOI 10.30757/ALEA.v15-15; preprint arXiv:1710.08240.

Exact locator: **Problem 4.6**, near the end of Section 4.

The source assumes an exponential-square moment condition: for some `epsilon>0`,

`alpha = integral exp(epsilon x^2) dmu(x) < infinity`.

After proving eventual classical unimodality and locating the unique mode in `[-sqrt(t)/2, sqrt(t)/2]` for a sufficient large-time threshold, the authors ask to **estimate the position of the mode** for classical Brownian motion under that assumption and then ask the corresponding question for free Brownian motion.

### Prior repository work recovered

The existing campaign has already done useful partial mathematics on this row. For compactly supported initial laws it records asymptotic expansions of the classical and free modes, with both displacements of order `1/t` and a source-specific relation between the leading free and classical displacements. This is prior work and is not re-claimed here.

### Why P0177 cannot be honestly admitted under the current full-source protocol

The literal source endpoint is not a theorem with fixed quantifiers such as `prove m_t -> m`, `prove |m_t-mu| <= C/t`, or `find the sharp constant C`. It says **estimate the position** and then `How about free Brownian motion?` There is no unique source-specified accuracy, asymptotic order, number of expansion terms, sharp constant, or universality class whose completion constitutes source-level closure.

The existing compact-support `O(1/t)` asymptotics show why this matters: they are mathematically strong, but there is no source-internal rule saying that this estimate, rather than an all-orders expansion, a sharp nonasymptotic bound, or the full exponential-tail class, is the closure endpoint. Admitting a narrower statement of our own choosing would manufacture a new conjecture/subproblem and could not later be labeled full Problem 4.6 resolution.

**P0177 disposition for this slot: PROGRAMMATIC / SOURCE-CLOSURE-CRITERION NOT FIXED, therefore NOT ADMITTED.**

This is not a claim that the underlying mathematics is uninteresting or impossible; it is an operational admission verdict under the owner's requirement that a target have a complete source-valid closure criterion.

## Consequence for R7-01

Neither screened shard-0 candidate yields a lawful `CLOSABLE OUTSIDE` admission:

- `C0133`: one-dimensional clause is already KNOWN; the remaining multidimensional theorem is HARD;
- `P0177`: mathematically tractable-looking, but the literal source request is programmatic and does not define a unique full-source closure endpoint.

The slot therefore remains `PENDING_ADMISSION`. The successor metric remains `UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`; successor stagnation is `NOT_STARTED`; the initial research methods B2/B24/B11 remain unspent because no source passed admission.

No `operations/claims/*.md` file, shared queue/result/posting ledger, peer report, or historical file was changed.

## Next bounded admission action

On the next run, first delta-check fresh `master`, claims, and queue. Do not re-screen C0133 or P0177 absent a real source/literature/ownership change. Advance to the next unscreened exact shard-0 canonical candidate with a source-fixed finite/counterexample/constant/short-theorem endpoint. In particular, absence of a canonical claim for old campaign rows with candidate-full proofs (for example P0267) is not a release and must not be treated as inventory.
