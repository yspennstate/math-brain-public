# T087 round 5 working log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, about 08:05 Asia/Tbilisi. All new files stay
in this folder. No git, subagents, external posting, or shared-state write.

## Orientation and predecessor reading

Read `~/.claude/brain_startup.md`, the brain navigation
index, and the compute-state file. Compute state: `warn`,
`owner_away_open`, CPU saturation. No numerical workload will be run.
The explicit task restriction to this folder overrides shared mesh,
checklist, and brain writes. Brain recall is omitted because the earlier
log records that it attempts an index refresh outside the permitted scope.

Commands: `rg --files` on this and all three predecessor folders, then
`OMP_NUM_THREADS=1 nice -n 15 cat ...` on each predecessor's REPORT.md,
LOG.md, PROOF.md and AUDIT.md. No predecessor computation scripts exist.
All named proof and audit files were read in full, splitting reads to
avoid truncated output. No predecessor file was edited.

The short text-read commands complete with exit code 0 but print
`nice: setpriority: Operation not permitted`. The requested priority
adjustment cannot be certified in this sandbox; no sustained computation
is launched. Tool clock at orientation: `2026-11-15 04:07:14 UTC`.

## Literature check, closed within five minutes

Search queries:

- `three dimensional percolation critical exponents existence open 2026 2025`
- `percolation uniform boundedness crossing probabilities hyperscaling Borgs Chayes Kesten Spencer 1999`

Opened primary sources:

1. Tom Hutchcroft, *Dimension dependence of critical phenomena in long-range
   percolation*, arXiv:2510.03951:
   https://arxiv.org/abs/2510.03951 and
   https://arxiv.org/html/2510.03951v1 .
2. C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform Boundedness
   of Critical Crossing Probabilities Implies Hyperscaling*,
   MSR-TR-98-26 (1998):
   https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .
   Read the introduction and Lemma 4.2. Its proof explicitly dominates
   component count by disjoint-path count before applying BK.
3. OpenAI, *Critical bond and site percolation on the cubic lattice*,
   September 24, 2026, README:
   https://raw.githubusercontent.com/openai/math/main/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/README.md .
   This is metadata and does not verify the continuity claim or any
   exponent theorem. No arXiv id appears there.

No verified solution of the full T087 problem was found. No
SOLVED_ELSEWHERE.md is warranted. The status search is closed; any further
source reading will concern only the chosen lemma.

## Independent recheck: round 4 result holds

Re-derived the main inequality using normalized core mass. Put
V=|B_{4m}|. If W is the number of core vertices reaching partial B_{16m}
and s_i their masses in distinct crossing box components, then
W=sum s_i and Q=sum s_i^2. Every such box component contains an annulus
crossing component after the last visit to partial B_{8m}; hence their
number R is at most J_m. On G={J_m<=L}, W^2<=LQ. Sampling two uniform
core vertices gives E Q/V^2<=X(8m)/V. Thus

    E[(W/V)1_G] <= sqrt(L X(8m)/V).

On G's complement every successful core vertex first reaches partial
B_{7m}. For a deterministic core vertex this inner event has probability
at most pi(3m), and uses edges disjoint from those defining J_m. Hence

    E[(W/V)1_{G^c}] <= pi(3m) P(J_m>L).

Meanwhile E W/V>=pi(20m). This recovers exactly the round 4 inequality,
including its square root, volume normalization, and direction.

Rechecked the cover: a center in m*partial B_12 has its radius-2m box
between radii 10m and 14m, fully inside the annulus. A chosen crossing
path hits radius 12m and then exits a covering box; distinct annulus
components cannot share a component of that box. Thus (P) passes to J_m.

For X(n)=n^{s+o(1)}, a=(d-s)/2 and L=ceil(m^h), the error is
O(m^{-a+h}). At m=8^j, f_j=pi(3*8^j), r=8^{-(a-h)}, the recurrence is
f_{j+1}<=q_j f_j+A r^j, q_j->0. Unrolling with q_j<=r/2 gives an error
sum bounded by 2A r^{j-1}; therefore f_j=O(r^j). This independently
checks the recurrence and the factor 2A/r. Monotonicity fills all scales.
Conversely, with N=ceil((3n)^{1/t}), t<1,
X(3n)/X(N)=N^{-s(1-t)+o(1)}->0, and separated endpoint arms give
pi(n)^2>=[X(N)-X(3n)]/|B_N|. Letting t increase to one supplies the
opposite exponent. No defect was found in the reverse-transfer theorem.

Also rechecked the round 3 tail argument: telescoping pi(3*8^j) supplies
good scales in every [N,N^{1+zeta}]; buffered loss of core mass at those
scales is negligible. Largest mass m^{d-a-o(1)} sampled with mass/volume
weight gives tail power a/(d-a). The upper bound
F(t)<=pi(n)+X(n)/t balances at t=n^{d-a}; subsequent subtraction at
t=n^{(1-h)(d-a)} recovers X. The original expected-count pair bound
follows by Cauchy–Schwarz on (configuration, component) pairs. All three
predecessor claims survive this recheck.

## Choice, recorded before the new proof

Prove the round 4 report's proposed geometric reduction: a quantitative
rectangular crossing criterion implying (P) for the exact free-boundary
K_n. Use rectangles of length n and transverse side 4n, whose crossing
probability is R(n). Keep distinct box components separate from maximal
edge-disjoint paths. Aim for an explicit exponential tail and expectation
bound in terms of the crossing deficit 1-R(n), allowing that deficit to
decrease with n. This is one geometric extension and remains conditional
at criticality on Z^3.

Reason: every B_n-to-partial B_{2n} component supplies a path in one of
2d face rectangles, and distinct components supply disjoint paths.
The nonmonotone component-count event is never an input to BK. A precise
bound will replace (P) by a scalar finite-volume crossing estimate and
state exactly how much approach to crossing probability one is allowed.

## Quantitative target and refinement, before writing PROOF.md

Write delta(n)=1-R(n), with R(n) the length-n, width-4n crossing
probability. Direct face assignment suggests, for integer u>=1,

    P(K_n>=u) <= 2d R(n)^{ceil(u/(2d))},
    E K_n <= 2d R(n)/delta(n).

Thus delta(n)=n^{-o(1)} is sufficient even for the stronger expected-count
hypothesis. Check a same-piece refinement: if 1<=m<=n/8, cover a shell
of radius m*floor(3n/(2m)) by radius-2m boxes. Their number is
O((n/m)^{d-1}); each lies inside B_{2n}. If this gives

    E K_n <= C_d (n/m)^{d-1}/delta(m),

then the deficit condition need only hold on a sequence m_j with
log(m_{j+1})/log(m_j)->1. This is a scale-selection corollary of the
same geometric reduction, not another exponent theorem. Its geometry
and the factor d-1, rather than d, will be checked independently.

## 08:11 — new proof saved and reread

Saved PROOF.md. The direct bound is

    P(K_n>=u)<=2d R(n)^{ceil(u/(2d))},
    E K_n<=2d R(n)/(1-R(n)).

A component's path is assigned to its outer endpoint's signed face.
Taking its last visit to coordinate n leaves a crossing of the correct
length-n, width-4n rectangle. Distinct components supply vertex-disjoint,
and hence edge-disjoint, witnesses there. BK is applied only to the
increasing disjoint-path event. No independence between rectangles is
asserted.

The scale comparison was also proved. For h=floor(3n/(2m)) and
1<=m<=n/8, the shell cover has exactly
S=(2h+1)^d-(2h-1)^d centers, and its boxes lie at norms strictly above
n and below 2n. An injection gives K_n<=sum_z K_m(z). In particular,

    E K_n <= C_d (n/m)^{d-1}/(1-R(m)),
    C_d=4d^2 4^{d-1}.

This proves (H), and therefore (P), if 1-R(n)=n^{-o(1)}. It also proves
them if the deficit assumption holds only on m_j with
log(m_{j+1})/log(m_j)->1: choose the largest m_j<=n/8, so
log m_j/log n->1 and all losses in the comparison are subpolynomial.

Command: `OMP_NUM_THREADS=1 nice -n 15 sed -n '1,360p' PROOF.md`.
Output: complete saved proof; exit code 0, with the priority-adjustment
warning already recorded. Tool clock: `2026-11-15 04:11:00 UTC`.
No computation script or percolation simulation was needed.

## 08:13 — independent audit and report completed

Saved AUDIT.md and REPORT.md. The audit checked the face extraction
using the signed coordinate of a path as an integer-valued walk, the
ceiling thresholds by contraposition, and the expectation bound by
geometric stochastic domination and memorylessness. A disjoint shell
partition independently gives

    S=2 sum_{i=1}^d (2h-1)^{i-1}(2h+1)^{d-i}
      <=2d(2h+1)^{d-1},

which recovers C_d=4d^2 4^{d-1} without the derivative argument.
In d=3, C_3=576 by two counts. At n=8m, h=12,
S=3458 and N=20748 by both a difference of cubes and a disjoint
face partition; the general bound gives 36864, in the correct direction.

Attempted failures: nonmonotone component counts; component mergers;
paths sharing vertices inside one component; overlapping rectangles;
repeated path returns; corners and ties; boundary cases n=1 and n=8m;
integer ceiling errors; replacing logarithmic density by arbitrary
sparsity; mistaking a finite positive deficit for a subpolynomial one;
and inferring exponent existence from the geometric criterion alone.
No invalid step was found. The criterion is sufficient, not necessary.

Commands:

    OMP_NUM_THREADS=1 nice -n 15 cat AUDIT.md REPORT.md
    OMP_NUM_THREADS=1 nice -n 15 rg -n '^(VERDICT:|## |Task:)|C_d=|C_3=|R\(n\)|log\(m_\{j\+1\}\)' LOG.md PROOF.md AUDIT.md REPORT.md

Output: complete audit and report, followed by matching definitions,
constants, scale conditions, required verdict at REPORT.md line 1,
and task attribution. Both short reads completed with exit code 0 and
the previously recorded priority warning. Tool clock:
`2026-11-15 04:13:34 UTC`. No numerical computation was launched.

The result is PARTIAL: an explicit geometric sufficient condition,
including selected-scale estimates, for the earlier crossing-count
hypotheses. Proving that deficit estimate at critical Z^3 remains open
within this work; even with it, one input exponent must still be proved
to exist. All four deliverables are saved here and no files elsewhere
were edited.
