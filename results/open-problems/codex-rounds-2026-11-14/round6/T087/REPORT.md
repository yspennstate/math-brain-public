VERDICT: PARTIAL conditional almost sure largest-cluster exponent and all positive moment exponents

The round 5 rectangular crossing criterion was independently re-derived
and holds, including its shell constant C_3=576 and logarithmically
dense scale criterion. No complete solution of T087 was found in the
five-minute literature check. Recent critical-continuity claims do
not themselves establish critical exponents.

The new result concerns M_n, the size of the largest open component
in the free-boundary graph induced by B_n. Assume the predecessor
hypotheses

    pi(n)=n^{-a+o(1)}, 0<a<d/2,
    P(K_n>n^epsilon)->0 for every epsilon>0.

With D=d-a, PROOF.md establishes

    log M_n/log n -> D almost surely,
    E M_n^r=n^{rD+o(1)} for every fixed r>0.

For every epsilon,A>0 its upper tail at n^{D+epsilon} is eventually
at most n^{-A}. For 0<epsilon<D its lower tail satisfies, eventually,

    P(M_n<n^{D-epsilon})
      <=exp[-3^{-d} n^{d*epsilon/(8D)}].

This extends the predecessors' lower expected-mass estimate at selected
scales to an almost sure finite-volume exponent and all positive
moments. Their rectangular deficit criterion is a sufficient condition
for the count hypothesis, including on logarithmically dense scales.
Alternatively, their reverse transfer permits the input
X(n)=n^{s+o(1)}, 0<s<d, with D=(d+s)/2.

The finite bound behind the upper estimates is unconditional. For a
finite Bernoulli graph H with V vertices, maximum degree at most
Delta>=1, and f_H(t)=max_x P(|C_H(x)|>=t),

    P(M_H>=Delta*k*t) <= (V*f_H(t)/t)^k/k!,
    k,t positive integers.

A large open spanning tree contains k disjoint connected sets of at
least t vertices. Counting their possible roots and applying BK to
increasing volume events gives the bound. A second-moment estimate
and independent smaller boxes supply the lower probability bound.

## Verification and commands

Read REPORT.md, LOG.md and PROOF.md in all four predecessor folders;
no predecessor computation scripts were present. Read the round 5
audit. LOG.md records the independent re-derivation before the extension
was chosen. AUDIT.md re-derives the tuple factors, exponent arithmetic,
constants, and probability amplification separately, and checks the
boundary, dependence, and moment issues.

This is a proof task; no simulation or numerical percolation data was
used. Commands that printed the complete saved proof were

    OMP_NUM_THREADS=1 nice -n 15 sed -n '1,220p' PROOF.md
    OMP_NUM_THREADS=1 nice -n 15 sed -n '221,440p' PROOF.md

Both exited 0. The sandbox denies the priority adjustment, reporting
`nice: setpriority: Operation not permitted`. No sustained computational
workload was launched. The initial brain recall and its warnings are
recorded in LOG.md; no further shared-state tools were invoked.
No git, subagent, predecessor edit, or external posting was used.

Opened primary references are recorded in LOG.md. The classical
comparison is C. Borgs, J. T. Chayes, H. Kesten and J. Spencer,
*Uniform Boundedness of Critical Crossing Probabilities Implies
Hyperscaling*, MSR-TR-98-26 (1998), Sections 5–6:
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .
The largest-cluster interpretation is classical. Novelty beyond this
local continuation has not been established.

## What failed or remains uncertain

No error was found in the rechecked predecessor claims or the extension.
An expectation lower bound alone would not prove typical size;
independent-box amplification is essential here. BK on component counts
and Jensen for a fractional-moment lower bound would be invalid shortcuts.

Neither the crossing-count criterion nor an input exponent is established
at criticality on Z^3. This does not prove exponent existence, exponent
values, pointwise two-point decay, or near-critical matching in T087.
Almost sure logarithmic size does not supply a limiting distribution or
bounded ratios M_n/n^D. The recent continuity manuscripts were located,
not independently certified; nothing in this proof depends on them.

## Next step

The principal unresolved input remains the round 5 scalar deficit
estimate at critical Z^3. Another concrete finite-volume target is a
converse: determine which quantitative lower-tail or largest-cluster
information, without assuming an arm exponent, forces subpolynomial
K_n. The present maximal-volume theorem alone supplies no such converse:
it does not control many small crossing components. Keep that gap
explicit before trying to transfer exponent existence back from M_n.

Task: “take the NEXT checkable step on this problem, building on that
work.” — T087, 15 November 2026, approximately 10:40 Asia/Tbilisi.
