Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime model/effort telemetry or binding selector is exposed.

# R7-02 Tier-3 shard-1 focused admission screen — P0358

Date: 2026-09-19 UTC  
Repository: private `yspennstate/math-open-problems`  
Branch: existing `master`  
Own root: `research7_2026-09-17/R7-02/`  
Native task id: `6aabe797a39081919acc889f29f4c556`  
Run-start captured master: `6aed2b0eaeb1c4fa29856e0af5be78b7ca54fe78`  
Pre-write master recheck: `092d5bb885ff31b83c3329a683bb63576f865ede`

## Purpose

P0169 has already reached its mandatory six-unchanged-run CLOSABLE handoff. The preceding R7-02 screen exhausted the already-ranked Tier-1/Tier-2 shard-1 frontier and left a durable instruction to inspect Tier-3 only when the literal source shape resembles an exact finite construction/counterexample/certificate or similarly sharply bounded target. This screen therefore does **not** repeat the old queue inventory. It advances one focused Tier-3 candidate, `P0358`, because its literal source asks for one exact positive constant.

No source is admitted in this screen unless every source/status/ownership/classification gate is satisfied.

## Exact shard check

Canonical candidate ID: `P0358`.

Character-code sum:

- `P = 80`;
- `0 = 48`;
- `3 = 51`;
- `5 = 53`;
- `8 = 56`.

Thus

`sum(ord(c) for c in "P0358") = 288`,

and

`288 mod 7 = 1`.

So `P0358` is genuinely in R7-02's exact case-sensitive shard.

## Recovered original source and literal target

Repository source metadata identifies the primary source as Aïdékon–Hu–Shi, *Boundedness of discounted tree sums* (2024), arXiv `2409.01048`, archived source URL `https://arxiv.org/pdf/2409.01048`.

The canonical Codex locator is:

- **Open question 2**;
- **Theorem 1.2** supplies the hypotheses/existence theorem referenced by the question;
- repository catalog locator: **PDF pp. 2–5**.

The source-matching statement preserved in the repository is:

> identify the positive finite constant `a1` in
> `inf_ray limsup_n V(ray_n)/sqrt(n log n) = a1`
> under the full hypotheses of Theorem 1.2.

The campaign ledger explicitly warns that the objective is the **value of the constant**, not merely reproving its existence, and that the full tilted-tail/logarithmic-moment assumptions are retained by reference.

## Prior work recovered

The 2026-09-07 campaign attempt did not identify `a1`. Its useful observation was a scaling check: multiplying every displacement by `c>0` preserves the theorem class with the corresponding scale parameter transformed, so any proposed closed form for `a1` must obey the same homogeneity. The attempt records that the upper and lower constructions are controlled by rare negative drops and reproduction, and that their sharp matching coefficient was not extracted.

This is a real prior attempt and prevents treating P0358 as an untouched one-line constant problem.

## Current-source / later-work screen, bounded to the private repository

The owner requires GitHub-only operation, so this run did not contact arXiv, authors, search engines, or any third party. Within the private repository, the following evidence was recovered and checked on 2026-09-19:

1. the campaign catalog still labels P0358 `unsolved` but expressly says its 2026-09-07 current-literature check was **unverified** and did not establish a full current-openness certificate;
2. the repository later-source inventory contains Zhang, *Boundedness of discounted branching random walks via generic chaining* (2026), arXiv `2602.18919`, as related later literature;
3. focused repository searches on P0358, the exact ray-height expression, the Aïdékon–Hu–Shi source, and the Zhang title found no repository record claiming that Open question 2's constant `a1` has been identified;
4. a search miss is **not** promoted to proof of worldwide openness, novelty, or priority.

Therefore the honest current-status label from the permitted evidence is:

`SOURCE_POSED_OPEN / REPOSITORY_BOUNDED_NO_RESOLUTION_FOUND / WORLD_CURRENT_STATUS_UNVERIFIED`.

## Ownership screen

At the run-start captured master, direct read of `operations/claims/P0358.md` returned `404 Not Found`. Focused repository search found no canonical P0358 ownership claim.

This means no ownership collision was evidenced, but absence of a claim does not cure the other admission failures below.

## CLOSABLE classification gate

P0358 initially looks attractive because it asks for one scalar constant. On inspection it is **not** an honest R7-02 CLOSABLE finite-certificate target under the current owner rules:

1. the quantity is an almost-sure/infinite-ray asymptotic extremum, not a fixed finite witness or exact finite certificate;
2. the proof obligation is theorem-sized and depends on the full Theorem 1.2 hypothesis package, including tilted-tail and logarithmic-moment assumptions;
3. the private GitHub corpus preserves those assumptions only **by reference** in the canonical P0358 record; the third-party primary PDF bytes/text are not archived in the repository surface used here, so the complete source quantifiers/hypotheses cannot be reconstructed source-faithfully in this GitHub-only run;
4. existing work supplies only a scaling consistency check and a qualitative description of the unmatched upper/lower mechanisms, not a finite reduction whose remaining search space can be certified;
5. the related 2026 Zhang source is recorded but not accompanied by a source-matching resolution audit of Open question 2.

The exact-constant wording therefore does not justify relabeling a deep asymptotic branching-random-walk problem as CLOSABLE merely to fill the slot.

Disposition:

`P0358 = SHARD_PASS / OWNERSHIP_LOOKS_FREE / SOURCE_SCOPE_RECOVERED_PARTIALLY / CURRENT_OPENNESS_UNVERIFIED / CLASSIFICATION_FAIL_FOR_CLOSABLE`.

**No claim is created. No metric is frozen. No Section-B method is charged.**

## Adjacent Tier-3 triage without reopening broad programs

The current Tier-3 metadata shows that the nearby shard-1 rows are predominantly broad asymptotic/structural programs rather than finite endpoints: P0349 asks for a detailed asymptotic analysis of complex clade-size powers; P0351 asks for stronger structural connections between CTCS(infinity) and the beta(2,1) coalescent; P0360 asks an unrestricted uniqueness implication for frozen percolation; later shard-1 rows include universal-limit, statistical-efficiency, scheduling-characterization, and exceptional-ray questions. P0423 and P0448 are repository-recorded literature-resolved/known exclusions, while P0457 has an active canonical claim.

Those title/status facts are used only as a filter against wasteful bulk reopening. They are **not** asserted as full source screens. P0358 was the only candidate in this tranche promoted to a source-level gate because its literal target had the requisite exact-scalar shape.

## Result and durable cursor

No genuinely CLOSABLE OUTSIDE successor crossed all gates.

Successor state remains:

- target: `PENDING_ADMISSION`;
- source-native metric: `UNKNOWN/UNMEASURED`;
- stagnation: `NOT_STARTED`;
- reserved first-successor methods: `B2 / B16 / B19`, still **NOT_TRIED**.

Durable cursor after this screen:

`POST_P0169_TIER3_SHARD1_EXACT_SHAPE_P0358_SCREENED_REJECTED`.

Do not rescreen P0358 on a later run unless there is a material source/status/ownership change, a repository copy of the full primary assumptions becomes available, or an exact finite reduction is independently deposited. The next admission work should continue forward to a genuinely sharp finite/certificate-shaped shard-1 source rather than cycling through broad Tier-3 asymptotic programs.