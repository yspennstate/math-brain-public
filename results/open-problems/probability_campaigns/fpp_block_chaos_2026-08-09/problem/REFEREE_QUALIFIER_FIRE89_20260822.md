# The doubling note's equivalence argument does not hold as printed, and its conclusion needs a
# scope line: doubling buys beta = O(1) at the blocks the geodesic actually meets, not everywhere.
# 2026-08-22, lane P8_record, from lane P3's referee pass.
# STATUS: correction companion. It corrects a mechanism and a corollary; it moves nothing.
# chi = 1/3 UNMOVED.

## 0. What this file is and what it does not do

DOUBLING_IS_NOT_A_SIDE_DOOR_20260812.md (fire 89) went into the record unrefereed and stayed
there for ten days, and its closing summary is the text that downstream surfaces have been
serving. Lane P3 refereed it on 2026-08-22. Its verdict on the note's third section is GAP AS
PRINTED; the note's conclusion survives, but through a different argument and at a narrower
scope than the note claims.

The original file is not edited. Provenance in this campaign is immutable, and the note is
cited by SHA elsewhere in the chain, so the correction travels beside it:

    DOUBLING_IS_NOT_A_SIDE_DOOR_20260812.md   sha256 e2f0198eb3cb6126e37030c7244c4aebbcf3bd7e566f551bc12db08ce4c4f2e3  (2899 bytes)
    P3_VERDICTS_20260822.md                   sha256 a98486c60e3e41e7bf01d1bd6e974b3bf080dfa488749ad2eb6a8bcd9651b4b7  (36935 bytes)
    MONOTONICITY_HAS_NO_CONSUMER_20260815.md  sha256 40b8db498297bb11e38a4c595b7700d950d3792b6391e47fe1a168916209cd92  (8467 bytes)
    CONTINUITY_BOOTSTRAP_20260815.md          sha256 830c9419bf27652c44c90a01288cab18ac647199f34ad7949d838b82bc324acc  (26767 bytes)

Authority for everything below: P3's verdict document, entry 89.3, at
P3_VERDICTS_20260822.md
(one-line summary in VERDICT_INDEX.md in the same directory).

## 1. What still stands, unchanged

Route 1. Efron-Stein with the bounded-weight influence bound and the linear geodesic length
certifies Var(X_2n) <= C n, hence A(n) ~ n / log n against the Newman-Piza log lower bound.
CONFIRMED by P3, who re-derived the display constant (1/2)(b-a)^2 E|gamma| under the note's own
"geodesic of the smaller configuration" reading and checked the NP95 consumption: the
transcription's atom conditions (2.12)/(2.13) are inherited, and for weight laws that violate
them the certified ratio only worsens (n/const in place of n/log n), so the route degrades
adversarially and survives.

Route 2. Subadditivity gives no variance content, because pointwise domination compares no
variances. CONFIRMED.

The practical corollary. Constant-A doubling is a reformulation of the main obstruction and not
low-hanging fruit; an attack on "just doubling" is an attack on the wall with fewer tools. That
is the claim everything downstream actually uses, and it STANDS.

## 2. The defect in the printed mechanism

The note's third section certifies beta_cert = U_raw(j+1)/L(j) <= A K = O(1) from a maintained
window R(j) = U(j)/L(j) <= K. Two problems, either of which is enough.

(a) The window is not maintained by the engine's own output. The halving returns
U(j+1) = (M/2) U(j) while the only unconditional lower bound grows like log n, so
R(j+1) ~ (M/2) R(j) and beta_cert = A R(j) leaves O(1) after a single step. This is exactly the
consumer-3 computation in MONOTONICITY_HAS_NO_CONSUMER_20260815.md, written three days after
fire 89 and never connected back to it.

(b) The step is written at doubling granularity, M = 2, where the engine cannot run at all: a
(1/2)M halving at M = 2 concludes non-increasing variance, which contradicts NP95 under its atom
conditions, so package H is unsatisfiable there. The operative statement lives at the engine's
large M with doubling iterated, A_M = A^{log2 M}.

## 3. What repairs it, and the scope the repair carries

The repair is fire 3's clarification (CONTINUITY_BOOTSTRAP_20260815.md, 4bis): CRUX 9.8's beta is
O of the TRUE variance ratio, and doubling bounds the true ratio, so beta = O(1) follows directly
with no window and no induction to start. That is correct and it is what saves the conclusion.

It does not save it everywhere. 9.8 delivers (L1') from the ratio only at blocks the geodesic
meets with probability of order one - its own hedge is that it "explains (L1') where the sums live
and assumes it where they do not". Through m2_L <= 4 Var(X_Mn)/p_L, a block with p_L ~ M^{-3/4} on
the O(M^{7/4}) near band gets beta_L ~ M^{3/4} A, not O(1).

So the proved statement is: doubling delivers the wall's variance-ratio core at the sum-carrying
blocks. Conversely, (L1') together with (L3) and Efron-Stein delivers the M-fold constant ratio,
not the 2-fold ratio - descending from Mn to 2n needs a regularity nobody has. "Wall-equivalent"
as an exact biconditional is unproved in both directions at the edges.

    Read fire 89's equivalence as: constant-A doubling gives beta = O(1) on typical blocks,
    which is the wall's core; it is not a two-way equivalence, and it says nothing about the
    small-p blocks on the near band.

## 4. The corollary's monotonicity clause is stale for a second, unrelated reason

Fire 89 closes by naming variance monotonicity "a genuinely separate, plausibly softer target".
That reading was withdrawn on 2026-08-15 by fire 4, which found monotonicity has no consumer in
this program: it gives R_n >= 1 where every consumer needs the upper bound, it yields only a
constant floor where a log floor is already unconditional, and in the maintain-up window it makes
the window diverge. Its one non-trivial consequence, a density of good dyadic scales, is Kesten
repackaged. Monotonicity came off the target list then and has not been put back. P3 confirmed
both the payoff audit and the density derivation.

Fire 93's FKG obstruction still stands, and monotonicity remains open even for the mean
(arXiv 1202.2665). Off the target list is a statement about what it would buy this campaign, not
about whether it is interesting mathematics.

## 5. Where this correction had to be carried

The fire-89 summary was in circulation, not just on disk: the math-brain prompt hook injected the
row verbatim on the evening of 2026-08-22, carrying both the unqualified wall-equivalence and the
withdrawn monotonicity clause. The store row (claim_925a5f66e641446fa12df62c9b4b5b34, filed
2026-08-12) has been superseded in place by a corrected row that restates sections 1 to 4 of this
file, so a retrieval hit now carries the qualifier. The original row is retained and hidden, not
deleted; the store is append-only and nothing in it was edited.
