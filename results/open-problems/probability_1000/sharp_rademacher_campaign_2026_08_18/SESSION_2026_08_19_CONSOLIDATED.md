# The 2026-08-19 session, consolidated

One document for a reader who was not here. Written 2026-08-20 from `STATE.md` (top block, 22:1x),
`problem/WHAT_STANDS.md`, `problem/why_ceil_k_over_two.md` (through §23),
`problem/linked_pair_characterisation.md`, `problem/rooted_target_in_the_pairsum_frame.md`,
`problem/hub_count_formula.md`, the `mathbrain/` store, and the reports of the four agents that
closed the session.

**The sharp Rademacher singularity conjecture is OPEN.** `Pr(det B_n = 0) = (1+o(1))·2n²·2⁻ⁿ` has
not moved. Every object this campaign has computed is a known non-member of the residual class the
proof needs, and no member of that class has ever been exhibited — not here, and not in the 200-page
dossier. Nothing below should be read otherwise.

---

## 1. What the session set out to do

The owner's ask on 08-18 at 23:09 was to keep working on the math brain and on the probability open
problem he had been working on, using the dossier he had just downloaded, for twenty hours, firing
every ten minutes. The dossier is a 200-page research packet whose own verdict is "open program,
substantial audited progress", and whose named gap is a connector-compatible linear
entropy–rigidity theorem for dense, singleton-layer cyclic blocks: a rooted estimate
`dim((R+R_<)/R_<) ≤ C·L_{Q|W}` together with an absorption clause `R ∩ span W ⊆ R_<`.

That statement is about a quantity called the selector distance `d_cb`. Nobody in the packet
computes `d_cb` on more than a handful of objects, and the constants in the target are asserted
rather than derived from anything small. So the session's working decision was to build a
laboratory: compute `d_cb` exactly on the smallest family where the definitions bite — NAE triangle
systems — and see what the quantity actually does before arguing about what it ought to do.

That decision is the reason the session produced both real theorems and a long list of dead
formulas. The laboratory works. What kept dying was the closed forms fitted on top of its output.

---

## 2. What is proved now that was not before

All of these are unconditional, with a written argument, and all were established in this session.

**The star family.** `d_cb(k-arm NAE star) = k − 1` for every `k ≥ 2`. Before this it was verified
only to `k ≤ 3` and carried as an upper bound above that. The upper direction is a construction; the
lower direction is a leftover-structure plus derangement argument with a raw-part parallelism step
(`star_family_proved.md` §§2, 6).

**The disjoint family, and where the constant comes from.** `d_cb(m disjoint NAE triples) = m` with
`ℓ = mβ`, so tightness `d_cb·β/ℓ` is exactly 1 at every `m`. Together with the star (whose tightness
`(k−1)/k` approaches 1 without attaining it), this proves that `1/β = 2.409420` is exactly optimal
for the unrooted bridge `d_cb ≤ C·ℓ`: it cannot be lowered, and it is attained with equality along
an infinite family (`the_constant_is_attained.md` §§3–4). The campaign had been carrying `1/β` as a
floor forced by products of NAE three-circuits. A floor says the constant cannot be smaller. This
says why that number and not another.

**Why β, mechanically.** `β` is the absorption threshold. Absorbability has a closed form needing no
rank minimisation — with `π` restricting a form to the coordinates outside the window, a
configuration is absorbable exactly when some basis of `D` meets every `±`-class of `π(D)` — and
absorbable implies the rooted target's left-hand side is 0 outright. Claim B, that `L_{Q|W} < β`
forces absorbability, survived exhaustive enumeration at `r = 4, 5, 6` (192 / 16,222 / 393,212
configurations, of which 42 / 832 / 17,587 sit below `β`, with zero counterexamples and controls
firing in both directions in the same pass). And `β` is attained: the minimal non-absorbable
configuration is two disjoint NAE triples with `W` equal to one of them, giving
`L = 3 − log₂6 = 2 − log₂3 = β` exactly (`beta_is_the_absorption_threshold.md`).

**Additivity.** `ℓ` and `d_cb` add over coordinate-disjoint blocks, and tightness is the
`ℓ`-weighted average of component tightnesses. Proved, and it predicted six values to four decimals
before they were measured. This lemma does real work later: it kills one of the session's own
formulas without any measurement at all.

**The explicit dual, and the Rado condition as a blocking condition.** For a linear system of `k`
triangles on `r` coordinates, `D` is exactly the `r` coordinate forms plus one form per triangle, so
`|D| = r + k`. From that, `ker Φ = span{ρ_t}` with dimension exactly `k`, and the transversal/Rado
condition becomes a blocking condition: the missed set must kill every nonzero combination of the
`k` triangle relations. Checked against the independent `valid_R` implementation on about 29,000
subspaces with zero disagreements. One caveat that should travel with these two: the "no other dual
forms exist" half of `|D| = r + k` is exhaustively verified, not proved, and the store's own object
says so.

**`E_c ≤ d`**, because signed incidence vectors of a forest are independent.

**`excess ≤ 2` at `d = 1` for linear systems**, by a four-case argument, with equality exactly on
the `3k` pair-sums whose pair lies inside a triangle. This one earns its place twice, because the
same argument proves *why linearity is the hypothesis and not treeness*: every failing case runs
through `f_t − f_s` collapsing to support 2, which happens exactly when two triangles share an edge.
Book `p=3` is that in one line — its triangles all share the pair `{0,1}`, so `e_0+e_1` buys four
merges where a linear system permits two. Read this as a statement about `d = 1` only. Linearity is
the right hypothesis there and it is *not* sufficient at higher `d`, which is what §3 is about.

**The excess formula, derived (§23).** For `R` spanned by pair-sum lines, one per triangle,
`excess = E + (V′ − comp)` and `dim R = V′ − b`, where `E` is the edges of the pair-sum graph in
`R`, `V′` the coordinates it touches, `comp` its components and `b` its bipartite components.
Verified 618 of 618 on subspaces of dimension `≤ 3` across six objects, zero mismatches. Substituting
gives the whole story of the refutations below in one line: `excess ≤ 2d` holds exactly when the
pair-sum graph in `R` is a forest, and can fail the moment it carries a cycle.

**The rooted condition, made combinatorial.** `R ∩ span W = 0` iff the chosen vectors stay
independent after deleting the window coordinates; and `rooted d ≤ r − |W|` as a hard counting
ceiling. Both proved. This is what opened the named gap to computation at all.

**Smaller items that stand.** Claim Q — the largest level set of a non-coordinate linear form on
`{±1}^n` is exactly `(3/4)·2^n` — proved here, and it turns out to be the dossier's own tag (13),
rediscovered. Every minimal Rado violation has deficiency exactly 1. The Fano plane has `|A| = 0`.
The rank identities R1/R2/R7 from the rank lane are proved but unrefereed, and the clause-tension
result rests on R2.

---

## 3. What was refuted, and by what

This is the session's real content. Five closed-form formulas of ours died, plus one lemma the
counting bound was reduced to, plus four readings of the rooted data, plus a conjecture and a
published verdict. Each has a named witness, and every one of the five formulas died on a check that
had been registered before it ran.

### The five formulas

| dead claim | killed by |
|---|---|
| `d_cb = max(2, largest attachment group)` | chain `k=5` is 3. Profile `(1,1,1,1)`, largest group 1, formula says 2 |
| `d_cb = max(largest attachment group, ⌈k/2⌉)` | `(3,2)` at `k=6` is 4 against a **registered** prediction of 3 — 2871s exhausting the `d=3` search. It had fitted eleven exact values and hit nine registered predictions in a row |
| `d_cb = max(⌈k/2⌉, k−h)` globally | the campaign's own proved additivity lemma: chain3 ⊔ chain3 is `2+2 = 4`, the global expression says 3. Every pair of odd chains breaks it. No measurement required |
| the same formula per connected component | `(3,1,1)` at `k=6` is 4 against 3 — by hand first, then exhaustive search (5289s), then confirmed by a separate `d ≤ 3` exhaustion (2962s). `(2,1,1,1)` has the same `k` and the same `h` and comes out 3, so no expression in `k` and `h` alone can be right |
| `excess ≤ 2d` for linear systems | tri-cycle `k=4`, `R = span{e₀+e₂, e₂+e₄, e₄+e₆}`, `dim 3`, **excess 7**. Tri-cycle `k=6` reaches 11 at `d=5`. These are linear systems, so linearity is not sufficient |

And the repair died too: `excess ≤ 2d+1`, fitted to the cycle mechanism, was killed one experiment
later by two coordinate-disjoint tri-cycle `k=4` blocks reaching **excess 14** at `dim 6`. That
prediction was stated in advance from additivity, which is the one satisfying thing about it.

The consequence is blunt. `d_cb ≥ ⌈k/2⌉` — the campaign's principal quantitative conjecture — is
true on every object ever measured and **has no derivation left at any `k`**. It is a conjecture
supported by measurement, not a bound with an argument behind it. The `d = 1` case survives, proved.

### `E_t ≤ d` is false, which the session had listed as its one remaining open link

The counting bound had been reduced to a single unproved lemma, `E_t ≤ d`, and `STATE.md`'s top
block still carries it under "still open". It is not open, it is false, and the witness is already
in hand: `excess = E_c + E_t` with `E_c ≤ d` proved, and the tri-cycle `k=4` witness has excess 7 at
`d = 3`, forcing `E_t ≥ 4 > d`. The math-objects agent did not leave that as an inference — it
reimplemented the merge and class machinery from the definitions and recomputed the certificate,
reproducing `|D| = 12`, `d = 3`, five classes with sizes `[4,2,2,2,2]` and excess 7 exactly, then
split them `E_c = 3, E_t = 4`. Two further witnesses agree (tri-cycle `k=6` at `E_c=5, E_t=6`; two
blocks at `E_c=6, E_t=8`), the tri-cycle `k=8` negative control gives excess exactly `2d` with
`E_c = E_t = 3`, and both small controls fire correctly.

So the counting bound does not have one missing lemma. It has no derivation.

### Four readings of the rooted data

| dead claim | killed by |
|---|---|
| "rooting is free or fatal, almost never expensive" | chain `k=6` at `\|W\|=5`: worst rooted 4 against unrooted 3. One window in 1,287 |
| "tri-cycles never block" | tri-cycle `k=6` blocks at `\|W\| = 7`, 6 windows of 792. The earlier sweep stopped at 5 |
| "the raising window is the hub set" | the hub set is free on chains `k = 4, 5, 6` — including chain `k=6`, which has a raiser at exactly the hub set's size, so the coincidence was a coincidence |
| "covering whole triangles is what raises `d`" | chain `k=4`'s window `{0,1,2}` covers a whole triangle and does not raise; chain `k=5` has no raiser at any size |

All four were read off the smallest object on which the phenomenon appears, which is the worst place
to read a mechanism. On fan `k=3` the hub set, the middle triangle and the needed pair-sum are the
same three coordinates, so one observation fits three different stories. The guard that caught two
of them was cheap and is now the standing rule: run the proposed mechanism where it predicts nothing
should happen, not only where something did.

### Everything else that died

Conjecture R (`d_cb ≤ (1/β)·L_{Q|W}` for every NAE fibre and rooting) is refuted by the book rooted
at its shared pair — exact ratios 2.5, 3.0, 4.25, 6.6 at `p = 2..5`, growing without bound, because
the boundary explains away the constraints and drives `L → 0` with the dual untouched. The "`μ` is
not `O(L)`" verdict, which had a whole document titled after it, is withdrawn: its `μ` values came
from a greedy that minimised `d_cb` first and read `μ` afterwards, so they are upper bounds and
every row points in the worthless direction; the exact minimisation gives `μ_min = 0` almost
everywhere. Every quantitative claim in `gluing_is_a_cliff.md` is retracted except its additivity
lemma — each was a maximum over a bounded enumeration read as a property of the objects. The 4.26
star floor was the worst of 10,976 boundary-preserving certificates, realised by four of them; the
honest floors are 1.42 and 2.84. And the natural selection rule for the construction — pick
independent triangles — is not merely insufficient but fatal: on `(2,1,1,1)` at `k=6` all 135
independent choices are invalid while 108 valid ones exist.

### What replaced the formulas

Not a sixth formula. The statement that survives is in the machinery's own terms:

> `d_cb` is the least `d` such that `d` linked pairs `(1_{S_j}, e_t)`, `j ∈ t`, span `Q^k`.

The two constraints a dimension supplies are *linked* — both come from the same triangle. It matches
34 of 34 objects with five advance predictions and five hits, it reproduces both proved theorems
rather than being fitted to them, and it makes the discrimination no `(k,h)` formula can:
`(3,1,1)` and `(2,2,1)` share `k = 6` and `h = 3` and come out 4 and 3. Its scope is measured rather
than assumed — it fails on 5 of 7 non-linear objects, uniformly by overestimating, which is the sign
the mechanism requires.

It is a description, not a theorem. Its lower direction rested on `excess ≤ 2d` and is therefore
worse off now than when it was written; its upper direction — that a spanning selection is always
realisable as an actual subspace — has never been argued.

---

## 4. The dossier connection, which is the strongest external validation the campaign has

The families this campaign built as *non-linear controls* — objects meant to fail the counting bound
so the detector could be shown to be alive — turned out to be the objects the dossier has already
solved.

The dossier's rooted NAE cycle `A_n` is our wheel: triples `(0, i, i+1)` around a cycle, all sharing
coordinate 0. Its rooted NAE path is our fan, the same triples taken non-cyclically. That is an
identification by unfolding definitions, not an analogy. The dossier proves
`d_cb(A_n) = d_geo(A_n) = ⌈n/3⌉` for `n ≥ 4` (tag 35), `⌈(N−1)/3⌉` for the path (tag 38f), and a
rooted version of the path result (tag 38g).

Measured here by the exact `fast_dcb` search, with no knowledge of those theorems:

| | measured | dossier |
|---|---|---|
| wheel `n = 3, 4, 5, 6, 7` | 1, 2, 2, 2, 3 | `⌈n/3⌉` = 1, 2, 2, 2, 3 |
| fan `k = 3, 4, 5` | 1, 2, 2 | `⌈k/3⌉` = 1, 2, 2 |
| rooted fan `k = 3, 4, 5` | 1, 2, 2 | tag 38g, same values |

Also: the crosspolytope at `r = 4` gives `d_cb = 1`, matching the dossier's tag (31) — a third
independent implementation of that value. And Claim Q, proved here from scratch, is the dossier's
own tag (13).

Two things follow, and both matter more than the arithmetic.

The machinery is calibrated against an external proved standard rather than only against itself.
Nine or ten independent agreements against two separately proved theorems is the only external check
this campaign has ever had, and it is a real one. (Nine versus ten is discussed in §7 below; nothing
rests on it.)

And the boundary between what is settled and what is open runs exactly along linearity, from both
directions. The wheel violates our counting bound by precisely the gap between `⌈n/2⌉` demanded and
`⌈n/3⌉` true — and it violates it because it is non-linear, consecutive triples sharing the edge
`{0, i+1}`. So the families that break the linear theory are the families the document has solved,
and the families the linear theory handles are the ones the document does not discuss. That is a
clean division of labour, and it was not designed.

Conjecture RC lines up the same way. The dossier's tag 38d proves `d ≤ ℓ/log₂(4/3)` for cycles,
which is `d_cb ≤ ℓ/β` — exactly this campaign's tightness `≤ 1`. Added here: `d_cb ≤ k` by a
construction with no search (take one pair-sum per triangle, missing `f_t`, which supplies the unit
`e_t`; the `k` units span `Q^k`), which with `ℓ = kβ` gives the same bound for triangle-trees and
disjoint unions. RC now holds on three families for two different reasons — proved with equality on
disjoint unions, proved by the dossier for cycles, and conditional for trees on the one unargued
step in the construction (the chosen pairs' incidence vectors must be independent, a no-even-cycle
condition that holds in all 35 objects checked and is free on trees but is not argued in general).

Where that argument does *not* close is worth recording, because it is the shape of every honest
limit in this document: off the tree and disjoint families `ℓ ≠ kβ`. Tri-cycle `k=4` has
`ℓ/β = 3.957`, so `d_cb ≤ k` permits tightness 1.0108 and proves nothing there. The measured value
is fine at 0.5054, but that is a measurement.

---

## 5. Where the named gap stands

The gap is the rooted statement, and this session is the first time the campaign has computed
anything about it rather than talking about it.

The condition became combinatorial and then computable: `R ∩ span W = 0` iff the chosen vectors stay
independent after deleting the window coordinates, plus the hard ceiling `rooted d ≤ r − |W|`. Both
proved. Run against the dossier's own proved rooted path theorem on fans `k = 3, 4, 5`, it agrees
three for three, computed from the combinatorial reading with no knowledge of the construction the
dossier uses.

What the exhaustive sweep found, across roughly 5,000 windows enumerated by size on objects up to
`r = 13`:

Raises are rare but real, and exactly two are known. Fan `k=3` at `W = {0,2,3}` — its middle
triangle — and chain `k=6` at `W = {4,5,6,7,8}` — two adjacent triangles. Both are unions of whole
triangles, and that is emphatically not sufficient: chain `k=4`'s whole-triangle window does not
raise, and chain `k=5` has no raiser at any size. For chain `k=6` alone the empirical rule is clean —
every raising window, at any size, covers triangles 2 and 3 wholly, with the remaining coordinates
free — and what changes at `k=6` that does not change at `k=4` or `k=5` is not established.

Blocking is real and structural, not an arithmetic artefact. Tri-cycle `k=6` blocks at `|W| = 7` (6
windows of 792) and not below, with `r − |W| = 5` still above the unrooted value of 3. And blocking
was verified against the full line set of the dual rather than only pair-sums — two blocking windows
plus one raiser plus five controls — so the restricted search did not manufacture the result.

No wheel window has raised the dimension. That is stated as the bound of a sweep, not a property of
wheels, because exactly that conflation has already failed twice in this line of work.

Four mechanism guesses for what distinguishes a raising window have died. A fifth is not being
offered.

The honest limit is this. Everything measured is small, and the windows are either inherited from
the dossier's path setup or adversarially chosen but still small. The regime the named gap actually
asks about is dense, singleton-layer cyclic blocks with larger windows, where the connector condition
is expected to bite hard. What has been shown is that the machinery reproduces the known case and
that the rooted condition has real content in both directions — it can raise and it can block. The
block-internal certificate Layer II needs has not moved in the entire campaign.

---

## 6. What the four closing agents added

**math-objects** extended the typed-object store with `mathbrain/campaign_objects_v2.jsonl` (44
objects) and `mathbrain/campaign_edges_v2.jsonl` (128 edges), covering everything the session
established after the original 13 objects were filed. Validation passed on every check: all lines
parse, all 44 carry the eight required keys non-empty, statuses are in vocabulary (7 proved, 15
exact-certificate, 2 conditional, 11 disproved, 6 heuristic, 3 open), 44 unique names with zero
collisions against the 325 dossier and 13 campaign names, 78 dependency names all resolving, 128
edges with every endpoint resolving and no self-loops or duplicates. Reach matters as much as count:
27 edges point into dossier objects and 39 into the existing campaign layer, so the older objects
gain the new proofs and refutations without being edited, and all six named dossier anchors are edge
targets. Every dead formula is now a `disproved` object naming its killing witness, and a banner
object records that every object studied is a known non-member of the class. Beyond transcription it
produced one real finding — the `E_t ≤ d` refutation described in §3, re-derived from the
definitions rather than inferred. It flagged two things upstream: `mathbrain/README.md` still
describes the campaign layer as the original thirteen objects and never mentions the v2 files, and
`STATE.md`'s top block should stop listing `E_t ≤ d` as still open.

**method-memories** wrote the session's six durable method lessons as standalone brain memories,
each with its concrete instance and real numbers:
`a_fitted_pattern_dies_on_the_prediction_you_register_2026_08_19.md`,
`ask_what_your_generator_cannot_produce_2026_08_19.md`,
`run_the_mechanism_where_it_predicts_nothing_2026_08_19.md`,
`read_the_checker_when_it_contradicts_the_impossible_2026_08_19.md`,
`derived_machinery_survives_the_formulas_fitted_on_top_2026_08_19.md`,
`a_broken_lemma_is_not_a_broken_conclusion_2026_08_19.md` (all under
`~\.claude\projects\<project>\memory\`). Four of the natural slugs were already
taken by the automatic end-of-turn filer, which names turn records after each turn's lesson line;
those are turn-scoped work logs owned by another process, so the agent wrote distinct standalone
nodes and cited each job record as the session record it distils. Its own audit pass caught an
overreach in its draft — it had stated `excess = 2d + c` as the true shape when that is fitted plus
an incidence argument — and corrected it in place.

**claims-audit** wrote `problem/WHAT_STANDS.md`, the campaign's authoritative status document, after
reading all 35 files in `problem/` plus `STATE.md`, `LOG.md`, `STATE_OF_THE_PROOF.md`,
`ITERATION2_SYNTHESIS.md` and the store. It separates 18 proved items from 21 exhaustive
certificates, the partially-measured readings, 11 conjectures and 22 refutations each with its
witness; lists every exact `d_cb` value the campaign holds split by how it was earned (proved
theorem / full search over every line / forced by additivity / squeeze / pair-sum only); names 12
sections that still assert refuted claims; and names 7 contradictions between documents. It made two
corrections of its own accounting, both flagged as its own, discussed in §7.

Four of the twelve misleading sections it named have since been fixed with correction banners:
`why_ceil_k_over_two.md`, `hub_count_formula.md`, `k6_predictions.md` and `mu_on_dense_stars.md` all
now open with a "read this first" block. Four that I checked and that remain unmarked:
`gluing_is_a_cliff.md` still carries its retracted title and six retracted numbers before the
retraction at the end, `rooted_target_in_the_pairsum_frame.md` still has four passages reading as
live, `linked_pair_characterisation.md` still calls `excess ≤ 2d` "unproved" when it is false, and
`STATE.md`'s rank-lane block still heads itself "the cheapest unexplored hypothesis is FALSE". The
remaining four on the audit's list I did not re-check, so treat its list as the live one.

**push-prep** was the one agent that did no mathematics. It verified read-only that nothing in the
outgoing set of four repositories contains a real credential: the secret gate's five findings across
the 57 outgoing commits are all the low-precision "2FA code" rule firing on the literal prose "mode
code 100644" — a git file mode quoted inside three documents that exist to explain this exact false
positive — and no high-precision rule fired anywhere. An independent localizer reproduced the gate's
census exactly. It identified the live blocker as the second gate: the nightly dream runs a
range scan after committing, the offending blobs are already committed, and editing the three files
will not clear it. The fix is to tighten the 2FA rule or push by another route. It also flagged a
pre-existing file already at `origin/main` and not part of this push,
`01_ai_consciousness/historical_memories/singles/TADPOLE_ACCESS_HANDOFF_2026-06-10.md`, which holds
a real credential dossier; all four repositories are private, pushing changes its exposure by
nothing, and rotation is the owner's call. Nothing was pushed, committed or staged.

---

## 7. Where the agents disagree, unsmoothed

**On the status of `excess = 2d + c`.** math-objects filed it `heuristic` with the reason stated as
"fitted to two counterexamples plus a counting sketch". claims-audit read it as derived only for `R`
spanned by pair-sum lines. Both were right when written, and the store is now stale by one section:
§23 of `why_ceil_k_over_two.md`, written after math-objects read the file, gives the derivation
(`excess = E + (V′ − comp)`, `dim R = V′ − b`) and verifies it 618 of 618. The honest current
reading is claims-audit's: derived and verified for pair-sum-spanned `R`, silent about non-pair-sum
directions, and therefore **not** an upper bound on excess for arbitrary `R` of dimension `d`. No
general upper bound on excess is currently held. The store's `heuristic` status understates the
derivation and its stated reason is now wrong; the object should be re-filed against §23.

**On how much of the 34-object table is independent evidence.** math-objects transcribed the
campaign's own figure, "about 21 of the 34 could have diverged". claims-audit recounted it at 25,
on the grounds that the disconnected values are forced by the *proved* additivity lemma plus exact
component values rather than measured by the pair-sum search, and that the stars at the top of the
range are covered by a proved theorem. The recount is right, and `hub_count_formula.md` says so
itself when it uses chain3 ⊔ chain3 to kill the global formula: "the refutation does not actually
rest on the measurement". `linked_pair_characterisation.md` under-counts its own independent
evidence. The corrected split is 25 fully independent, four more carrying an independent lower
bound, and five genuinely pair-sum-only.

**On the dossier agreement count.** `STATE.md` and math-objects say ten; claims-audit says nine is
the defensible number, because the dossier states its cycle theorem for `n ≥ 4` and the wheel `n=3`
row therefore agrees with an extrapolation rather than with the theorem. That reasoning is correct.
*Mine, and neither agent said it:* the arithmetic recovers the tenth from a different row. The four
wheels in the campaign's count are `n = 3,4,5,6`, taken from the comparison table in
`linked_pair_characterisation.md`, but wheel `n=7` was also measured exactly — at 3, by the full
search over every line, per `star_vs_wheel_dichotomy.md` and `WHAT_STANDS.md` §6b — and `⌈7/3⌉ = 3`,
so it sits inside the theorem's stated range and was never counted. Drop `n=3`, add `n=7`, and there
are four in-range wheels, three fans and three rooted fans: ten. Nothing rests on nine versus ten and
the campaign should stop arguing about it; what matters is that the agreements are independent and
against externally proved theorems.

**Not a disagreement but a gap between store and documents.** The original thirteen campaign objects
still carry statuses the session overturned — `excess_at_most_two_per_dimension` is `audited-pass`
and refuted, `hub_count_formula` is `heuristic` and refuted twice — and the `README.md` summary
repeats them. The v2 layer records the refutations correctly but does not edit the older objects, by
design. A reader querying the store without the v2 file gets the dead formulas and none of the
session's theorems.

---

## 8. What to pick up first next session

In this order.

**Fix the four stale records, which takes minutes and prevents a re-derivation of dead work.** Update
`STATE.md`'s top block to move `E_t ≤ d` from still-open to refuted. Re-file
`excess_equals_two_d_plus_cycle_rank` against §23 with the correct reason. Update
`mathbrain/README.md` to describe the v2 layer. Add correction banners to `gluing_is_a_cliff.md`,
`rooted_target_in_the_pairsum_frame.md` and `linked_pair_characterisation.md`, and move the proved
additivity lemma out of `gluing_is_a_cliff.md` — it currently sits inside a document whose closing
line says to disregard the file, while forcing five exact `d_cb` values and underwriting the whole
component-wise reading.

**Then the one experiment that could settle the counting bound.** `d_cb ≥ ⌈k/2⌉` has no derivation.
The threat is that `excess = 2d + c = d + E` lets a *dense* linear system make `E` quadratic in `d`,
pushing the counting argument down to roughly `√(2k)`. The Fano plane suggests that threat may be
self-limiting — it is the densest linear system on 7 points and its fibre is empty, because packing
triples tightly is exactly what forces a monochromatic line — but that is a reason to expect the
bound to survive, not a proof. The test is a deliberately dense linear configuration, sparser than
Fano so it is 2-colourable, checked for whether its excess really reaches `k` at `d` well below
`k/2` and whether the resulting `R` passes `valid_R`. Partial Steiner systems are the place to look.

**Then the check the current evidence cannot supply.** Run the full `fast_dcb` search over every
line on one `k=7` shape where only the pair-sum search has spoken. The pair-sum search and the
linked-pair model share the assumption that pair-sums are the directions that matter, so their
agreement is one anchor measured twice; this is the honest test of the shared half. Expensive at
`r = 15`, and the campaign has named it as the outstanding check more than once without running it.

**On the named gap itself, the next move is to leave the small objects.** The rooted sweep has
exhausted what small tree-like and small cyclic objects can tell us — four mechanism guesses died
there. What the gap asks about is dense, singleton-layer cyclic blocks with large windows. Either
build one and compute the rooted quantity on it, or accept that the laboratory cannot reach the
regime and say so. That decision is worth making explicitly rather than by drift.

**And one thing not to do.** Do not write a sixth formula in `k` and `h`. Five have died, each on a
registered prediction, and the reason is structural: `(3,1,1)` and `(2,2,1)` share every parameter
such a formula can see and have different answers. What survived every round in this session was the
derived machinery, never the closed forms fitted on top of it.

---

A last statement of position, because it should be in the same breath as everything above. The
conjecture has not moved. What the campaign has is a small sharp theory of a finite object — the
selector distance of linear triangle systems — with two theorems in it (the star at `k−1`, disjoint
triples at `m`) and the exact optimality of `1/β` that follows from them, a proved additivity lemma,
a proved reformulation of the Rado condition, a proved account of why linearity is the hypothesis,
and a mechanism explaining where the constant `1/β` comes from that ties the rooted target's constant
to the dossier's own anticoncentration cap. It has nine or ten independent agreements with two
externally proved theorems, which is the only calibration the machinery has ever had. Against that,
its principal quantitative conjecture has no derivation, its best description of `d_cb` is a
description rather than a theorem, and every number in this document is a measurement on something
known not to be in the class the proof needs. The campaign has built a working laboratory and
calibrated it against outside results. It has not yet used it on the case that matters.
