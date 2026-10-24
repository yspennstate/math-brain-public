# Derived checkpoint 14: regular finite crossings and logarithmic parity FEI

3 October 2026 UTC.  Parent master
`197a8e32a6c1adb0fa0e9123dc4c8a8ba26079aa`.  Only this campaign's
`CURRENT.md` changes in place; every earlier checkpoint remains immutable.
The full proofs, independent audits, failed routes, exact programs and
reports are in
`proofnet24/P03-fei/continuations/2026-10-03-parity-and-regular-crossings/`.

## 1. Ordinary FEI for balanced regular finite-crossing scores

For fixed `m,B,r0`, let `g=F(sum_i w_i X_i)`, where `F` has `m` genuine
alternating crossings, `max_i|w_i| <= B||w||_2/sqrt(n)`, and both output
labels have probability at least `r0`.  Then `H(g)<=C(m,B,r0)I(g)`.
Crossing locations and spacings are arbitrary, `m` may be even or odd, and
individual weights have no positive lower bound.

The new proof converts output balance, through a whole-score Berry--Esseen
comparison, into two long protected opposite-label intervals inside a
central Gaussian window.  A localized signed-translation identity between
their centers gives pivotal Lebesgue measure at least the selected-block
displacement.  A uniform fixed-size mask has exact mean energy and a uniform
upper bound, yielding the needed lower square-root average without reversing
Jensen.  Remainder Berry--Esseen and resampling then give
`I(g)>=c(m,B,r0)sqrt(n)`.  The established KOS/CKLS noise route gives
`H(g)=O_m(sqrt(n))`; weak logarithmic FEI handles finitely many lower
dimensions.

The actual half-open/closed label sets retain every attained crossing atom
in the discrete balance comparison.  Their open interiors differ only by
Gaussian-null endpoints.  This repairs an ambiguity caught during the
adversarial audit.  The independent analytic audit passes the repaired
proof.  The author checker passes 440 exact local-translation identities
(160 even-crossing) and 35,259 balanced truth-table cases.  A separately
implemented attained-cut suite passes 14,386 families, 28,772 label
inequalities, 2,970 attained-cut occurrences and 41,534 legal endpoint
assignments.  Finite checks supplement
the analytic proof.

The result is not uniform as `r0` tends to zero or regularity `B` diverges.
It does not solve arbitrary irregular-weight finite crossings or full FEI.

## 2. Incomparable arbitrary-bias odd-crossing theorem

The complete input-regular odd-crossing theorem permits arbitrarily biased
output, but assumes all crossing locations are within fixed normalized
distance `lambda` of zero.  It proves `H(g)<=C(m,B,lambda)I(g)` for odd `m`,
arbitrary crossing spacings, and no minimum weight.  Its independent full
analytic audit passes.  Root reran the three suites: 3,339 heat-mask checks,
11,868 author mask/moment checks, and the 240-function constituent suite
with 9,552 exact translations, 7,152 endpoint inclusions, 648 selected
moments and 648 resampling identities
and explicit huge-cutoff comparisons.  This theorem and the balanced theorem
cover different rare-output regimes; neither is counted as a corollary of
the other.

## 3. Logarithmic FEI for character outputs of unate-gate combinations

If `g=F(g_1,...,g_m)`, the outer Boolean function is arbitrary, and every
gate is unate (shared inputs and unrelated orientations allowed), then for
`h=chi_T g`, `q=n-|T|`,

    H(h) <= [log2(4m^2+2q)+3] I(h).

Full output parity has constant `2log2(m)+5`.  More generally `m` may be
replaced by an upper bound on the Euclidean norm of the influence vector.
The proof combines exact parity influence complementation, the unate Chow
norm bound, and an elementary full-spectral-law Gibbs proof of the known
weak `H<=(log2 n+3)I` estimate.  The empty Fourier atom and constant cases
are retained.

The independent analytic audit passes.  Root reran the author suite:
65,814 functions, 1,050,698 character pairs, 440 genuinely shared-input
gate combinations, and 1,053,853 exact isoperimetric comparisons.  The
separate implementation passes 4,366 character pairs, 4,296 direct KL
identities, 12 exact Gibbs normalizations, 96 overlapping combinations and
49,446 real-parameter regime comparisons.  The general weak logarithmic
bound is established prior work and is explicitly credited.  For `T` empty
this remains dimension dependent; no ordinary closure theorem for arbitrary
shared-input compositions is claimed.

The separate bounded-alternation character theorem is also complete:
`H(chi_T g)<=4cot^2(pi/[2(m+q+2)])I(chi_T g)` when `g` has at most `m`
sign changes on every ascending path.  It includes all finite-crossing
scalar scores under nearly full parity.  Full parity of a unate function has
the sharp constant 2.  Its full audit and 1,051,466 rerun function/character
pairs pass.  The older quadratic gate-count theorem is retained and marked
superseded by the logarithmic result.

## 4. Failed unrestricted three-crossing routes

The still-open middle-trace route is reduced exactly to
`4xy<=o^2+2t(x+y+o)`.  A broader common-score trace/Poincare statement has
an explicit family with divergent ratio, and the score-ordered noise kernel
has an exact negative TP2 minor `-3/32`.  Exhaustive positive integer weights
`1,...,8` through dimension eight cover 12,321 families and 47,693,379
triple cuts.  Their largest actual trace ratio is `3/2`; this is evidence,
not an asymptotic proof.

Another exact family retains all three crossings in both largest-coordinate
restrictions while its local entropy-increment/influence ratio diverges.
A signed three-halfspace decomposition can lose an unbounded factor.  These
disprove proposed proof shortcuts, not FEI.  The lacunary derivation is a
known-class consequence and is credited rather than advertised.

Primary KOS, CKLS, Wan--Wright--Wu, regular-LTF and symmetric-FEI sources
were checked.  Recent 2026 plateaued and stopping-tree manuscripts concern
distinct subclasses and continue to state general FEI as a conjecture.  No
bounded search certifies priority.  Historical novelty and external review
remain unverified.  Full Boolean FEI, the full forest/random-cluster
conjecture, unrestricted ML10, and Kaplansky/direct finiteness remain open in
this campaign.
