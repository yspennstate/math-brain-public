# T087 round 6 working log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 10:40 Asia/Tbilisi.

## Orientation and scope

Read the startup memory and compute state (`warn`, `cpu_saturated`,
`owner_away_open`). This is a proof task; no sustained computation is
planned. No subagents, git, external posting, or predecessor edits.
All deliverables stay in this directory. The task-specific folder rule
overrides shared mesh, checklist, and memory writes.

An initial `OMP_NUM_THREADS=1 nice -n 15 python3
~/.claude/dreaming/brain.py recall 'percolation T087
crossing component count exponents'` returned unrelated memories and
reported a denied priority adjustment and failed telemetry persistence.
Unlike the predecessor, this command was invoked before noticing its
warning about recall's possible index writes. It will not be repeated;
no shared-state write is needed for this task.

Read REPORT.md, PROOF.md and LOG.md in all four predecessor directories,
and the round 5 AUDIT.md. Used `rg --files`, `cat` and split reads;
file searches found no predecessor computation scripts. Earlier folders:
`codex_op_1114`, `codex_op_1114r3`, `codex_op_1114r4`, and
`codex_op_1114r5`, each under `briefs/T087`.

## Literature status check (closed within five minutes)

Queries included `three dimensional percolation critical exponents proof
2026`, `percolation continuity Z^3 critical 2026`, and `three-dimensional
percolation exponents proved 2026`.

Opened primary sources:

- Tom Hutchcroft, *Dimension dependence of critical phenomena in long-range
  percolation*, published ICM contribution:
  https://epubs.siam.org/doi/full/10.1137/25M180679X .
  Its discussion distinguishes short-range dimensions 3, 4, 5 from the
  long-range results; no solution of T087 is stated there.
- Yan Ru Pei, *No infinite cluster at criticality for long-range percolation
  with fast-decaying interactions*, arXiv:2611.01490:
  https://arxiv.org/abs/2611.01490 . Opened its arXiv page, not merely
  the proxy returned by search. It announces critical nonpercolation,
  not existence or values of the cubic-lattice critical exponents.

Also opened a community index for the September 2026 quasi-transitive
continuity manuscript; that index is not used as a proof source.
The recent continuity claims deserve a separate audit; none is needed
below. No verified complete solution of T087 was found, so no
SOLVED_ELSEWHERE.md is warranted. Further source reading will concern
only the selected mathematical extension.

## Independent predecessor recheck: the main claim holds

For a rectangle let D be the maximum number of edge-disjoint open
crossings and R its crossing probability. The increasing crossing
events have disjoint path witnesses, so BK gives P(D>=k)<=R^k.
Thus E D<=R/(1-R). Assign each component counted by K_n to a signed
outer face. After its last visit to that coordinate at level n, its
path crosses a length-n rectangle of transverse side 4n. Distinct
components supply vertex-disjoint paths. Therefore K_n<=sum of 2d
such D's, recovering both the round 5 tail and its exact expectation
factor 2d. No BK assertion about nonmonotone component counts is used.

Independently reconstruct the shell comparison with q=n/m>=8 and
h=floor(3q/2). The m-grid shell at radius mh has
S=(2h+1)^d-(2h-1)^d centers. The radius-2m boxes are inside B_{2n},
and rounding a path's vertex at radius mh to the grid lands within m/2
of a center. That path must subsequently exit the small box. Different
B_{2n} components cannot use the same small-box component. Consequently
E K_n<=2d S R(m)/(1-R(m)). The disjoint shell partition gives
S<=2d(2h+1)^{d-1}<=2d(4q)^{d-1}, recovering
C_d=4d^2 4^{d-1}, and C_3=576. The exact d=3 count at q=8 is
6*(25^3-23^3)=20748, below 576*64=36864.

For logarithmically dense m_j, choosing the largest m_j<=n/8 yields
log m_j/log n->1. Each logarithmic loss in the expectation bound
then vanishes after division by log n. Thus the latest main claim
holds, including its sparse-scale statement.

Also re-derived the original pair inequality by Cauchy–Schwarz on
(configuration, component) pairs. Rechecked the round 4 recurrence:
buffered inner edges are disjoint from the annulus count's edges,
so the bad-count term factors; the resulting f_{j+1}<=q_j f_j+A r^j
contracts when q_j<=r/2. The round 3 mass-to-tail conversion uses
V F(t)>=E M-t, and its balanced exponents are a/(d-a) and d-2a.
No defect found. These conditional results will be used as inputs.

## Choice, recorded before the extension is proved

Extend the predecessor reductions to the largest free-boundary cluster
in a box, including its moments and its logarithmic size in probability.
This is one finite-volume extension. Under the round 5 crossing-deficit
criterion and either predecessor input exponent, aim to show that its
scale is n^{d-a+o(1)}. The preceding reports give a lower bound on its
expectation at selected scales but do not establish this finite-volume
law or control all moments.

The proposed missing lemma is a deterministic packing of a large
bounded-degree tree into disjoint connected sets of size at least t.
BK applied to volume events at roots of these sets should give, for
maximum degree Delta and box volume V,

    P(M>=Delta*k*t) <= (V*F(t)/t)^k/k!.

If valid, this gives upper tails and moment control. The lower bound
will require a separate finite-volume argument; an expectation lower
bound alone does not imply convergence in probability. This issue must
be resolved or the final claim restricted.

## Packing lemma and completion of the lower-bound route

The packing argument works with Delta=2d. Root an open spanning tree.
A deepest vertex whose descendant subtree has at least t vertices has
at most Delta children, each with at most t-1 descendants including
itself. Its subtree has at most 1+Delta(t-1)<=Delta*t vertices.
Remove this subtree and repeat. A tree of size at least Delta*k*t
therefore contains k vertex-disjoint connected sets, each of size at
least t. Each set supplies at least t choices of a root witnessing a
cluster-volume event, and permuting the sets supplies k! choices.
BK bounds the expected number of ordered root tuples by V^k F(t)^k.
This proves the displayed factorial tail, with no component-count
monotonicity assumption and no independence of full clusters.

Using F(t)=t^{-a/(d-a)+o(1)} from the verified round 3 result, put
D=d-a and t=ceil(n^{D+h}). Then V_n F(t)/t tends to zero. The
factorial tail bounds every fixed positive moment by n^{rD+o(1)}.
The round 3 buffered mass bound at logarithmically dense good scales,
followed by monotonicity, gives E M_n>=n^{D-o(1)} at every scale.
Paley–Zygmund then gives a probability n^{-o(1)} of a cluster of size
n^{D-o(1)} in a box. Packing independent smaller boxes of radius
floor(n^{1-delta}) inside B_n amplifies this to a stretched-exponential
lower-tail bound. This supplies the missing probability step.

Both tail bounds are summable in n for any fixed logarithmic error.
Thus the same extension yields log M_n/log n->D almost surely, and
E M_n^r=n^{rD+o(1)} for every fixed r>0. These are conditional on (P)
and a nondegenerate arm exponent; the round 5 crossing criterion is
a sufficient condition for (P). None is proved at critical Z^3 here.

Opened C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform
Boundedness of Critical Crossing Probabilities Implies Hyperscaling*,
MSR-TR-98-26 (1998),
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .
Its Sections 5–6 already discuss the largest cluster and its moments.
The result here is a continuation for the predecessors' weaker (P)
and logarithmic limits, with an explicit elementary packing bound;
no literature priority is claimed.

## 10:48 — proof saved and independently audited

Saved and reread PROOF.md. Commands:

    OMP_NUM_THREADS=1 nice -n 15 sed -n '1,220p' PROOF.md
    OMP_NUM_THREADS=1 nice -n 15 sed -n '221,440p' PROOF.md

Both printed the complete proof in two parts and exited 0. As earlier,
the sandbox reports `nice: setpriority: Operation not permitted`; no
sustained numerical workload was launched. A short clock read returned
`2026-11-15 10:48:01 +04`. There are no numerical scripts or data.

The theorem proves, under the predecessor (P) and arm law with
0<a<d/2, D=d-a,

    log M_n/log n -> D almost surely,
    E M_n^r=n^{rD+o(1)} for every fixed r>0.

The audited lower tail is

    P(M_n<n^{D-epsilon})
      <=exp[-3^{-d} n^{d*epsilon/(8D)}], 0<epsilon<D,

eventually. The upper tail at n^{D+epsilon} is eventually smaller than
any prescribed n^{-A}. These summable bounds justify the almost sure
statement without independence across n.

Saved AUDIT.md. A second derivation using uniform random root tuples
recovers the k! and t^k factors in the packing lemma. Solving both
V F(t)/t=1 and t^{1+b}=n^d checks the scale D. Expanding the small-box
threshold gives D-epsilon/2+epsilon^2/(16D), and counting successes
gives d*epsilon/(8D), independently checking every lower-tail power.
The audit checks cycles, stars, root ordering, t=1, empty events,
integer floors, nonmonotone counts, exceptional large counts, overlaps,
fractional moments, fixed-ratio arm comparisons, and Borel–Cantelli.

No defect was found. The tempting shortcuts that fail are applying BK
to component counts, replacing an expectation lower bound by a typical
size bound, and invoking Jensen in the lower-bound direction for
fractional moments. The proof uses volume witnesses, a second moment,
and disjoint internal box configurations to avoid these shortcuts.

## Final verification and report saved

Saved REPORT.md with first line
`VERDICT: PARTIAL conditional almost sure largest-cluster exponent and all positive moment exponents`.

Final checks:

    OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
    OMP_NUM_THREADS=1 nice -n 15 cat AUDIT.md
    OMP_NUM_THREADS=1 nice -n 15 rg -n 'VERDICT:|Task:|Delta\*k\*t|k!|epsilon/\(8D\)|almost surely|E M_n\^r|10:4|## ' LOG.md PROOF.md AUDIT.md REPORT.md

All three exited 0 and printed the complete report, complete audit,
and matching hypotheses, constants, exponent formulas and task line.
The same priority-adjustment warning appeared. The proof was reread
after replacing ambiguous bond-percolation wording about vertices
with connected vertex sets. No mathematical claim changed.

The four deliverables are LOG.md, PROOF.md, AUDIT.md and REPORT.md.
The result is conditional: no critical Z^3 exponent or needed geometric
input has been established. The explicit unconditional contribution
within the continuation is the finite bounded-degree packing estimate;
the conditional almost sure and moment laws are its application to
the verified predecessor volume-tail and buffered mass results.
