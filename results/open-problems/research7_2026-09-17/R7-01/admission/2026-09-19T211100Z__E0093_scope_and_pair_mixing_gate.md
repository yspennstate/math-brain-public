Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum.** No authenticated runtime model/effort telemetry or binding GPT-6/maximum selector is exposed here.

# R7-01 admission screen — E0093 / Diaconis random-random-walk Question 2

## Decision

**Candidate E0093 is `HARD/BROAD OUTSIDE / SOURCE-PROGRAMME WITH A PRECISE EMBEDDED A_n CONJECTURE / NOT_ADMITTED`.**

R7-01 remains `PENDING_ADMISSION`. No canonical claim is created, no successor metric is started, and B2/B24/B11 are not charged. The source-matching successor metric remains `UNKNOWN/UNMEASURED` because the source has not crossed admission.

## Repository snapshot and shard

- Repository: private `yspennstate/math-open-problems`, existing branch `master`.
- Worker: `R7-01 Counterexamples and Constants`.
- Native ID: `6aabe777361481919c9e614646464772`.
- Own root: `research7_2026-09-17/R7-01/`.
- Fresh pre-artifact master: `924375ccf6e3613339b702be02f5dd97f7c55bac`.
- Previous own report creation commit: `ce5b1ddfcb3bb09dae20f2d07d94b9024e992911`.
- Previous state: `PENDING_ADMISSION`, metric `UNKNOWN/UNMEASURED`, stagnation `NOT_STARTED`, B2/B24/B11 unused.

Exact shard arithmetic:

`sum(ord(c) for c in "E0093") = 273`, hence `273 mod 7 = 0`.

So E0093 belongs to R7-01's residue-zero admission partition. This is a partition fact, not an ownership claim.

## Exact outside source

Persi Diaconis, **“Some things we've learned (about Markov chain Monte Carlo)”**, *Bernoulli* **19**(4) (2013), 1294–1305, DOI `10.3150/12-BEJSP09`, arXiv:`1309.7754v1`, Section 5, **Question 2**, printed page 9.

Primary source URLs:

- `https://arxiv.org/abs/1309.7754`
- `https://arxiv.org/pdf/1309.7754`

The source asks, for an arbitrary finite group `G`, what the typical convergence rate is when a generating set `S` is chosen at random. It identifies this as the “random random walks” problem and points to Hildebrand's survey and diameter bounds for random Cayley graphs.

The same paragraph contains a much sharper embedded conjecture for the alternating group. For `A_n`, Diaconis notes that a random pair generates with probability tending to one and conjectures that a walk based on **any** generating pair “gets random in at most `n^3 log n` steps.”

The intake row E0093 preserves the broad arbitrary-group Question 2 but omits this embedded alternating-group conjecture. That omission matters for admission: the broad question is a research programme rather than a single fully quantified theorem, while the embedded conjecture is mathematically sharp but appears far too hard for R7-01's preferred CLOSABLE lane.

## Source-scope ambiguities that block broad admission

The literal broad question does not itself freeze all of the following:

1. the cardinality `|S|` as a function of `|G|`;
2. whether random generators are sampled with or without replacement;
3. whether the Cayley walk is directed on `S`, symmetric on `S union S^{-1}`, or made lazy;
4. the asymptotic family of groups across which “typical” is taken;
5. a numerical mixing threshold for “rate of convergence.”

These choices change the answer. It would therefore be improper to install a single scalar metric for the whole broad Question 2 without narrowing the canonical source. The embedded `A_n` conjecture gives a legitimate sharp subproblem, but silently replacing E0093 by that subproblem would alter the current canonical intake statement.

## New exact derivation 1 — support size converts mixing into diameter

This run supplies a deterministic reduction that applies to any finite-group walk and makes the hardness of the embedded `A_n` conjecture explicit.

Let `G` be a finite group, let `mu` be any probability measure on `G`, and let

`nu_t = mu^{*t}`

be the law after `t` steps from the identity. Let `U` be the uniform law on `G`, and define

`A_t = supp(nu_t)`.

### Lemma

If

`||nu_t-U||_TV <= epsilon`,

then

`|A_t| >= (1-epsilon)|G|`.

If additionally `epsilon < 1/2`, then

`A_t A_t^{-1} = G`.

Consequently, if `mu` is supported on a generating set `S`, then

`diam Cay(G, S union S^{-1}) <= 2t`.

### Proof

Because `nu_t(G\A_t)=0`, total variation gives

`||nu_t-U||_TV >= U(G\A_t)-nu_t(G\A_t) = 1-|A_t|/|G|`.

Therefore `|A_t| >= (1-epsilon)|G|`.

When `epsilon<1/2`, `|A_t|>|G|/2`. For any `g in G`, both `A_t` and `g A_t` have more than half of the group, so they intersect. Choose `a_1,a_2 in A_t` with `a_1=g a_2`. Then

`g=a_1 a_2^{-1}`.

Every element of `A_t` is represented by a word of length `t` in `S`; its inverse is represented by a word of length `t` in `S^{-1}`. Hence every `g` is a word of length at most `2t` in `S union S^{-1}`, proving the diameter bound. QED.

### Consequence for Diaconis's embedded conjecture

Any universal `O(n^3 log n)` total-variation mixing upper bound for every generating pair of `A_n` would imply an `O(n^3 log n)` diameter upper bound for every such two-generator Cayley graph.

Thus the conjecture is not merely a routine mixing estimate. It would force a strong polynomial-diameter theorem for all two-generator presentations of `A_n`.

## New exact derivation 2 — entropy/support lower bound for every two-point walk

Suppose `mu` is supported on two generators. Then there are at most `2^t` positive words of length `t`, so

`|A_t| <= 2^t`.

Combining with the preceding lemma, any time satisfying `||nu_t-U||_TV <= epsilon` must obey

`2^t >= (1-epsilon)|G|`,

or equivalently

`t >= log_2((1-epsilon)|G|)`.

For `G=A_n`, `|A_n|=n!/2`. At the standard threshold `epsilon=1/4`,

`t_mix(1/4) >= log_2(3 n!/8)`.

By Stirling's formula,

`t_mix(1/4) >= n log_2 n - (log_2 e)n + O(log n)`.

So every generating-pair walk has an information-theoretic lower bound of order `n log n`; Diaconis's proposed `n^3 log n` upper bound leaves an `n^2`-scale structural gap that cannot be closed by support counting alone.

This is a source-relevant exact bound, but it does not decide the conjecture.

## Current literature check — dated 2026-09-20 local / 2026-09-19 UTC

The check used the original/current source, exact-phrase searches for the `A_n` pair conjecture, and bounded searches on random Cayley mixing and permutation-group diameter.

### Original/current source

The arXiv record has a single 2013 version and gives the Bernoulli publication and DOI above. The printed Question 2 on page 9 contains both the broad arbitrary-group question and the explicit `A_n` generating-pair conjecture.

### Arbitrary generating sets on `Sym(n)` and `Alt(n)`

Helfgott and Seress, **“On the diameter of permutation groups,”** *Annals of Mathematics* 179 (2014), prove

`diam = exp(O((log n)^4 log log n))`

uniformly over arbitrary generating sets of `Sym(n)` and `Alt(n)`. Their abstract explicitly describes polynomial diameter as a longstanding conjecture. This is much weaker than the polynomial consequence derived above from Diaconis's `n^3 log n` mixing conjecture and is strong evidence that the embedded target is theorem-sized.

### Random pairs

Babai and Hetyei, **“On the Diameter of Random Cayley Graphs of the Symmetric Group,”** prove for a uniformly random pair that, with high probability, the generated `S_n`/`A_n` Cayley graph has diameter at most

`exp((1/2+o(1))(log n)^2)`.

This is a random-pair diameter result, not Diaconis's universal “any generating pair” mixing bound.

### Abelian and nilpotent progress

Jonathan Hermon and Sam Olesker-Taylor, **“Cutoff for almost all random walks on Abelian groups,”** *JEMS* 28 (2026), 1913–1977, DOI `10.4171/JEMS/1743`, prove cutoff for broad random-generator regimes on all finite Abelian groups and obtain nilpotent comparisons/partial Wilson-type consequences.

Jonathan Hermon and Xiangying Huang, **“Cutoff for random Cayley graphs of nilpotent groups,”** arXiv:`2403.12355` (2024), prove high-probability cutoff for bounded-rank/bounded-class nilpotent groups in growing-generator regimes and comparison results for some general generating sets.

Xiangying Huang and Renyu Rao, **“Cutoff for random walks on dihedral groups,”** arXiv:`2510.19942` (2025), treat a virtually Abelian family in a growing-generator regime.

These results materially advance “random random walks,” but none recovered in this bounded check resolves the source's arbitrary finite-group programme or the worst-case two-generator `A_n` conjecture.

A negative search is not proof of openness or novelty. The admission decision below relies on the positive fact that the closest current theorems are structurally restricted and on the exact hardness reduction above, not on search failure alone.

## Prior repository work and ownership

- Intake attempt `E0093-A001` (2026-09-08) separated growing-generator and fixed-generator regimes and identified representation theory as the obstruction. It did not prove or refute the source.
- Earlier R7-01 admission history already labeled E0093 broad/HARD and warned not to admit it merely because it was the next residue-zero ID.
- Direct current fetch of `operations/claims/E0093.md` returned 404. This is repository ownership evidence only, not evidence of global novelty or openness.
- The exact repository comparison from the preceding R7-01 report commit `ce5b1ddfcb3bb09dae20f2d07d94b9024e992911` to fresh master `924375ccf6e3613339b702be02f5dd97f7c55bac` is `ahead 140 / behind 0`. Its admission-relevant canonical claim additions are occupied by other workers; there is no explicit free residue-zero CLOSABLE release for R7-01.

## Classification and metric gate

### Broad E0093

`HARD/BROAD OUTSIDE / UNDER-SPECIFIED PROGRAMME / NOT_ADMITTED`.

There is no honest single source-matching scalar for the entire broad question until the group family, generator-count regime and walk convention are fixed.

### Embedded alternating-group conjecture

If this were ever split into its own canonical source target, a natural frozen quantity would be

`T_pair(n) = sup t_mix^{a,b}(1/4)`

over generating pairs `(a,b)` of `A_n` under an explicitly frozen increment convention. Diaconis's conjecture asks for

`T_pair(n) = O(n^3 log n)`.

For admission purposes its baseline remains **UNKNOWN/UNMEASURED**. The support argument above proves only the universal lower bound

`T_pair(n) >= log_2(3 n!/8)`

under a two-point increment law; that bound is not promoted into a successor metric because E0093 is not admitted.

## Admission verdict

Do **not** create `operations/claims/E0093.md`.

Reasons:

1. the canonical E0093 row is a broad source programme, not a single fully frozen theorem;
2. the precise embedded `A_n` conjecture is a strong theorem-sized target whose mixing bound implies a polynomial diameter bound for every two-generator Cayley graph of `A_n`;
3. the best general arbitrary-generator diameter theorem recovered is still quasipolynomial rather than polynomial;
4. the recent 2024–2026 cutoff literature resolves important Abelian/nilpotent/dihedral regimes, not this universal pair target;
5. R7-01 is explicitly to prefer genuinely CLOSABLE outside endpoints, and no finite certificate, sharp finite constant, or short complete-theorem route was recovered here.

Therefore R7-01 remains `PENDING_ADMISSION`, successor metric `UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED`, stagnation `NOT_STARTED`, and B2/B24/B11 remain reserved for a future admitted target.

## Reusable handoff

If a HARD worker later takes the embedded `A_n` conjecture, reuse the two exact support lemmas above before attempting spectral or representation-theoretic bounds. The key obstruction is now explicit:

`TV mixing < 1/2  =>  support > |G|/2  =>  A_t A_t^{-1}=G  =>  symmetric Cayley diameter <= 2t`.

Any proof of Diaconis's universal `n^3 log n` mixing bound must therefore contain, directly or indirectly, enough group-growth control to imply polynomial two-generator diameter.
