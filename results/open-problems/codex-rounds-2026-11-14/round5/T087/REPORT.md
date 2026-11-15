VERDICT: PARTIAL scale-dependent rectangular crossing criterion for subpolynomial component counts

The earlier reverse exponent-transfer theorem was independently
re-derived and holds. The new result proves the geometric reduction
suggested in the round 4 report, for its exact free-boundary K_n.

Let R(n) be the probability of a short-direction open crossing of
[0,n] x [-2n,2n]^{d-1}, and let delta(n)=1-R(n). Then

    P(K_n>=u) <= 2d R(n)^{ceil(u/(2d))},
    E K_n <= 2d R(n)/delta(n).

Thus a subpolynomial reciprocal crossing deficit,

    log(1/delta(n))/log n -> 0,

implies the stronger expected-count hypothesis (H), and hence the
probability hypothesis (P) used by rounds 3 and 4. The deficit may
tend to zero; it need not be uniformly positive. For every epsilon>0,
the criterion gives eventually

    P(K_n>n^epsilon) <= 2d exp[-n^{epsilon/2}/(2d)].

Estimates only on logarithmically dense scales suffice. More precisely,
the same conclusions hold if a sequence m_j tends to infinity with

    log(m_{j+1})/log(m_j) -> 1,
    log(1/delta(m_j))/log(m_j) -> 0.

The finite-scale bridge, proved by an explicit shell cover, is

    E K_n <= C_d (n/m)^{d-1}/delta(m),  1<=m<=n/8,
    C_d=4d^2 4^{d-1}.

Distinct components are first dominated by maximal edge-disjoint
rectangle crossings. BK is applied only to those increasing path
events. The component-count events need not be increasing.

Neither crossing-deficit criterion is proved at p_c on Z^3. They
therefore provide conditional inputs to the earlier exponent-transfer
and volume-tail theorems, without establishing exponent existence,
values, pointwise decay, or near-critical matching. The geometric
method is classical; no literature priority is claimed.

## Verification and commands

Read REPORT.md, LOG.md, PROOF.md and AUDIT.md in all three predecessor
folders. File searches found no computation scripts. Rechecked the
original pair inequality, round 3 tail interpolation, and especially
round 4's buffered quadratic estimate and contracting recurrence.
LOG.md records these checks before the new piece was chosen.

This was a proof task, with no numerical program or simulation. Command:

    OMP_NUM_THREADS=1 nice -n 15 sed -n '1,360p' PROOF.md

printed the complete saved proof and completed with exit code 0.
The sandbox reports `nice: setpriority: Operation not permitted`;
no sustained computational workload was launched. AUDIT.md re-derives
the shell bound by a disjoint combinatorial partition, the geometric
expectation by memorylessness, and the sparse-scale limit by a second
logarithmic calculation. All load-bearing constants and thresholds
were checked independently, including the dimension-three bound
C_3=576 and the boundary case n=8m.

The literature status check finished within five minutes. No verified
complete solution of T087 was found. Opened primary sources are listed
in LOG.md. The relevant classical comparison is C. Borgs, J. T. Chayes,
H. Kesten and J. Spencer, *Uniform Boundedness of Critical Crossing
Probabilities Implies Hyperscaling*, MSR-TR-98-26 (1998), Lemma 4.2:
https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf .

All new artifacts are in this folder: LOG.md, PROOF.md, AUDIT.md and
REPORT.md. No git, subagent, external posting or shared-memory write
was used. The predecessor folders were read only.

## What failed or remains uncertain

No mathematical failure was found in the predecessor claims or this
extension. Direct BK on component counts would be invalid. Merely
knowing the finite-scale deficit is positive does not give its needed
asymptotic bound. A fixed polynomial reciprocal deficit gives only a
polynomial count estimate here. An arbitrary sparse sequence leaves a
polynomial covering loss; logarithmic density is used explicitly.

The criterion is sufficient; no converse is claimed. It uses rectangles
with transverse side 4n, and no aspect-ratio conversion from the classical
side 3n is silently assumed. Novelty beyond this local continuation has
not been established.

## Next step

The geometric target is now an explicit scalar estimate: at p_c on Z^3,
find integers m_j with log(m_{j+1})/log(m_j)->1 for which the no-crossing
probability of [0,m_j] x [-2m_j,2m_j]^2 has subpolynomial reciprocal.
Proving this would supply both predecessor count hypotheses. Existence
of either the one-arm or averaged two-point exponent would still be
needed. A weaker polynomial deficit estimate would give a quantitative
count bound through (2)–(4), but would not by itself establish (P).

Task: “take the NEXT checkable step on this problem, building on that
work.” — T087, 15 November 2026, approximately 08:05 Asia/Tbilisi.
