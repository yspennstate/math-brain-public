VERDICT: PARTIAL reverse exponent-existence transfer under crossing-count control in probability

The earlier conditional volume-tail theorem was independently re-derived
and holds. The new result resolves the reverse-transfer question left
open in the round 3 report.

Let K_n count open components of the induced free-boundary graph on
B_{2n} meeting B_n and partial B_{2n}, and let
X(n)=sum_{x in B_n} P(0<->x), with unrestricted connections. Assume

    for every epsilon>0, P(K_n>n^epsilon)->0.         (P)

PROOF.md proves

    X(n)=n^{s+o(1)}, 0<s<d
      => pi(n)=n^{-(d-s)/2+o(1)}.

Together with the verified predecessor theorem, (P) therefore makes
existence of a nondegenerate one-arm exponent equivalent to existence
of a nondegenerate averaged two-point growth exponent. Starting from
X alone now also gives

    P(|C(0)|>=t)=t^{-(d-s)/(d+s)+o(1)},
    delta=(d+s)/(d-s).

All limits are logarithmic. No arm-ratio regularity or expected-count
bound is assumed. The input hypotheses remain unproved at p_c on Z^3;
this does not solve T087 or establish any numerical exponent value.

The new finite-scale estimate is

    pi(20m) <= pi(3m) P(J_m>L)
                   + sqrt(L X(8m)/V_{4m}),

where J_m counts crossing components in the induced annulus of radii
8m and 16m, V_{4m}=(8m+1)^d, and L>=1. A deterministic covering
transfers (P) to J_m. Squared core-component masses give the square-root
error; independent inner edges control the bad-count contribution.
On scales m=8^j, this becomes a contracting recurrence with an error of
the desired power. It avoids needing a one-arm exponent in order to
select good arm-ratio scales.

## Verification and commands

Read REPORT.md, LOG.md, PROOF.md and AUDIT.md from both earlier folders.
The file search found no predecessor computation scripts. Independently
checked the earlier covering, largest-cluster estimate, logarithmically
dense good scales, volume-tail interpolation and recovery of X.
LOG.md records the verification before the new piece was chosen.

This was a proof task, with no simulation or numerical program. The
complete saved proof was reread using

    OMP_NUM_THREADS=1 nice -n 15 sed -n '1,360p' PROOF.md

The read completed with exit code 0. The sandbox denied the priority
adjustment (`nice: setpriority: Operation not permitted`), so no sustained
computational workload was launched. AUDIT.md independently re-derives
the quadratic bound by uniform pair sampling and the recurrence by
explicit geometric summation. It checks constants, exponent signs,
boundary conventions, component mergers, independence and all scales.

The status search finished within five minutes. No verified complete
solution of T087 was found. Opened primary sources and exact URLs are
recorded in LOG.md. The classical comparison is C. Borgs, J. T. Chayes,
H. Kesten and J. Spencer, *Uniform Boundedness of Critical Crossing
Probabilities Implies Hyperscaling*, MSR-TR-98-26. No priority claim is
made over classical conditional hyperscaling results.

All new artifacts are in this folder: LOG.md, PROOF.md, AUDIT.md and
REPORT.md. No git, subagent, external posting or shared-memory write
was used, and the predecessor folders were not edited.

## What failed or remains uncertain

Neither (P) nor exponent existence on critical Z^3 is proved. No
pointwise two-point lower bound, near-critical matching or exact exponent
value follows. Literature priority of this formulation is not established.
No mathematical failure was found in either the rechecked predecessor
theorem or the new reverse proof.

A fixed-ratio comparison of X cannot justify the needed subtraction
under logarithmic exponent existence alone. The proof uses distinct
power scales. Replacing bad-count probabilities by expectations, or
treating the core mass and annulus count as independent, would also be
unjustified; neither shortcut is used.

## Next step

The reverse-transfer gap is closed. The geometric target is still (P)
for the exact free-boundary K_n at criticality on Z^3. A concrete next
lemma is to derive an explicit sufficient condition on rectangular
crossing probabilities that implies (P), allowing scale-dependent
crossing deficits. Keep distinct-component counts separate from maximum
numbers of disjoint paths, and do not apply BK directly to count events.
Such a reduction would identify a more accessible geometric estimate;
proving it in dimension three remains separate work.

Task: “take the NEXT checkable step on this problem, building on that
work.” — T087, 15 November 2026, approximately 04:46 Asia/Tbilisi.
