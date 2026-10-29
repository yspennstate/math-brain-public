gates any mention of Theorem A; a fresh-eyes pass and the arXiv May-August 2026 sweep are owed
before anything print-bound. Human-voice rules apply throughout. NO funding section and NO
acknowledgments are to be added to this note by any agent, ever: funding blocks are current-facts
listed). If this draft is ever expanded toward submission, that block stays absent until he adds it.

---

A block-resampling variance inequality for planar first-passage percolation

We record an elementary deterministic bound on the occupation of rectangles by geodesics in
first-passage percolation on Z^2, and an unconditional variance inequality of Efron-Stein type in
which the resampling unit is a rectangular block of edges and the fluctuation sensitivity enters
through a block-level chaos quantity. The inequality transplants, with a sharper constant, the
variance-reduction engine used by Basu, Sidoravicius and Sly in their recent work on rotationally
invariant models, where it is one step of an unconditional theorem; on the lattice it isolates
exactly what a chaos estimate must provide to improve the Benjamini-Kalai-Schramm variance bound.
The reduction follows the superconcentration-chaos equivalence of Chatterjee, transplanted to
first-passage percolation with i.i.d. weights by Ahlberg, Deijfen and Sfragara, who posed
improving variance bounds via a chaos estimate as an open direction; Basu, Sidoravicius and Sly
proved a quantitative version, via block resampling, for a class of rotationally invariant
continuum models. We prove the analogous unconditional inequality for the standard lattice model
with i.i.d. bounded weights.

1. The occupation lemma

Lemma 1. Let 0 < a <= b < infinity, let each edge of Z^2 carry a weight in [a, b], and let gamma
be a geodesic between any two vertices. For every axis-aligned box B whose lattice diameter in the
l^1 metric is d(B) (an n x W box has d(B) = n + W), the number of edges of gamma inside B is at
most (b/a) d(B).

Proof. Suppose gamma meets the closed box; let x be the first vertex of gamma in B and y the last
(if an endpoint of gamma lies in B, take it). Then x, y in B, so there is a lattice path from x to
y of at most d(B) edges, of total weight at most b d(B). The segment gamma[x -> y] is a geodesic
between x and y by subpath optimality, so its weight is at most b d(B); since every edge costs at
least a, the segment has at most (b/a) d(B) edges, and every edge of gamma inside B lies on it.

The constant is sharp: with all weights equal, a corner-to-corner staircase geodesic of an n x n
box uses exactly 2n = d(B) edges.

[Referee record, campaign-internal: confirmed 2026-08-09 by hostile referee with independent
adversarial search; two defects of an earlier draft (a false O(1) claim and a one-sided
consequence) were caught and repaired; the two-sided consequence below is the corrected form.]

2. Consequences for block resampling

Fix endpoints at l^1 distance L and tile the edges of Z^2 by n x W boxes. Resample the weights of
one block Lambda from an independent copy; write X for the passage time, X^Lambda for the
resampled passage time, N_Lambda and N'_Lambda for the occupation of Lambda by the original and
the resampled geodesics. Comparing each optimum against the other's geodesic,

  (X^Lambda - X)^+ <= (b - a) N_Lambda,   (X - X^Lambda)^+ <= (b - a) N'_Lambda,

and Lemma 1 applies to both geodesics, so with Sum_Lambda N_Lambda <= (b/a) L + O(1):

  Sum_Lambda E[(X^Lambda - X)^2] <= 2 (b-a)^2 (b/a)^2 (n + W) L + O(1),

with the analogous fourth-moment bound carrying (n+W)^3. [Full display and constants: campaign
document CRUX, section 5, refereed form.]

3. The engine inequality

Theorem. Consider bond first-passage percolation on Z^2 with i.i.d. edge weights of law mu
supported in [a, b], 0 < a <= b < infinity, atoms allowed; fix endpoints and write X for their
passage time. Tile the edges by finite blocks; give each block an independent same-law reservoir
and an independent uniform label; let X^Lambda denote the passage time after resampling block
Lambda from its reservoir, gamma_can the canonical (alpha-minimal) geodesic of X - a fixed
measurable selection requiring no uniqueness - and U_Lambda the event that gamma_can uses an edge
of Lambda. With F_t the filtration revealing, for each block of label at most t, its label
together with the pair (weights, reservoir), set

  A2 := Sum_Lambda E[ 1(U_Lambda) (X^Lambda - X)^2 ],
  A4 := Sum_Lambda E[ 1(U_Lambda) ((X^Lambda - X)^+)^4 ],
  Pbar(kappa) := Sum_Lambda E[ P(U_Lambda | F_{1-kappa})^2 ].

Then for every kappa in (0, 1),

  Var(X) <= kappa A2 + sqrt( A4 Pbar(kappa) ).

The proof uses only the exchangeability of the resampled pair, the off-geodesic monotonicity
X^Lambda <= X outside U_Lambda, an order-averaged martingale decomposition of the variance, and a
sharp per-block inequality E[H^2] <= E[G^2] obtained by retaining a cross term that the
corresponding continuum argument discards; neither the FKG inequality nor any isotropy of the
model enters, and planarity is consumed only in constructing the canonical selection. [Full proof:
campaign document MG2B, sections 1-8, referee-verified; a standalone version would inline it at
about six pages. Whether this note carries the full proof or cites the companion document is the
outstanding scope decision.]

4. The weak reduction

Combining sections 2 and 3. Tile by n x W blocks and let the endpoint distance be N = Mn. The
occupation lemma gives A2 <= 2C'(b-a)^2 M n (n+W) and A4 <= 2C''(b-a)^4 M n (n+W)^3
unconditionally, so if the block-chaos quantity satisfies Pbar(kappa) <= eps M then

  Var(X_N) <= 2C'(b-a)^2 kappa M n (n+W) + (b-a)^2 M (n+W)^{3/2} sqrt(2 C'' eps n),

that is, Var(X_N) = o(N (n+W)) as kappa and eps tend to zero. The bound is unconditional but
weaker than the Benjamini-Kalai-Schramm bound unless the chaos strength decays with the scale, and
we record it as a price list rather than an improvement: the strong form of the reduction needs
block moment bounds at the fluctuation scale rather than the deterministic worst case, and those
remain open. (Both displayed terms carry the factor M; an earlier draft of this paragraph dropped
it. The controlling computation is the companion document's iteration arithmetic, section 5.) [Wall arithmetic: CRUX section 2; conditional
theorem under the full hypothesis package: campaign document MG2A, referee pending.]

5. Two errata on arXiv:2604.01214

[Import the two-paragraph erratum note already drafted (bss_errata_note_draft.md), stated once,

---
Assembly status: sections 1-2 complete in refereed form; section 3 statement fixed, proof import
pending scope decision; section 4 complete; section 5 pointer. Next: MG2-A referee verdict, then
