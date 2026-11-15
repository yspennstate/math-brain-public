# T071 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 01:09 Asia/Tbilisi (UTC+4).

## 1. Orientation and opening literature check, 01:09–01:12

Read the earlier REPORT.md, LOG.md, PROOF.md and AUDIT.md in
`~/codex_op_1114/briefs/T071`, without changing them.
The directory contains no mathematical scripts to rerun. Read the startup
memory index, brain navigation index and compute governor state. The latter
reported `warn`, `owner_away_open`, CPU saturation. The explicit folder-only
rule overrides the general instructions to write shared mesh/checklist/brain
state; none of those writers was invoked. No subagents or git.

Shell reads after the initial file listing use
`env OMP_NUM_THREADS=1 nice -n 15 sh -c '...'`. The sandbox prints
`nice: setpriority: Operation not permitted` but executes the read. No
numerical workload will be run when the requested priority cannot be set.
This session's deliverable is analytic.

Web searches (opening check only):

- `"N-BBM" genealogy "2026"`
- `"branching Brownian motion" "selection" "genealogy" "2025" "coalescent"`
- `"N-particle" "Brownian" "genealogy" "2026" coalescent`
- `"N-BBM" "genealogy" theorem`

Opened the arXiv abstract pages for 1304.0562, 2402.04917, 2605.04860,
1001.2337, and the full HTML of 1304.0562v4 and 1001.2337v3.
Legrand–Maillard's page still lists v4, 9 April 2026; its abstract concerns
displacement. Mercer's page lists v1, 6 May 2026; its abstract concerns
hydrodynamics and velocity. No later fixed-size N-BBM genealogy theorem was
located. This bounded check does not certify absence from the literature.
The literature check ended within five minutes; no further search is planned.

## 2. Independent recheck of the earlier result

The earlier main claim holds under its stated hypotheses. Derive the
three-block rates directly from the beta integral:
each pair has rate 1/2 and the triple has rate 1/2. First-step discounting gives

    (s+2) F_3(s,r) = 1/2 + (3/2)/(r+1),
    F_3(s,r) = (r+4)/(2(s+2)(r+1)).

Independently, the density on H>0 is (3/2)exp(-2S-H), while the measure on
H=0 is (1/2)exp(-2S)dS. Integration gives masses 3/4 and 1/4 and the same
transform. First-event time and holding time are independent. At T=log 2,
direct triples have probability (1/4)(1-1/4)=3/16. A binary path necessarily
visits a two-block state on an interval; no time bijection can erase that
state in the discrete-state J1 metric. The stated obstruction follows.

Checked the earlier equivalence independently using the vector of pairwise
MRCA times: joint CDF events are finite intersections of partition membership
events, and partitions at deterministic times are recovered by thresholding
these times. All target pair times have continuous marginals. This verifies
the hitting-time argument without assuming finite-N Markov dynamics.

## 3. Chosen extension (recorded before writing the proof)

Extend the exact criterion to four labels. Three times alone lose the shape
of the two-block partition: 3+1 versus 2+2. Retain this shape through a
Laplace statistic weighted to vanish when the two-block holding time vanishes.
Prove a necessary and sufficient four-label criterion, then extract an exact
disjoint-pair burst diagnostic. Construct a counterexample with correct
three-label restrictions to show why the extra shape information matters.

This is the smallest sample size that can distinguish simultaneous disjoint
mergers. It adds a specific estimate an N-BBM proof must address. It supplies
no N-BBM asymptotic estimate or time constant. Details and an independent
analytic audit will be saved in PROOF.md.

## 4. Proof saved; first attempt at breaking it

Created PROOF.md with a necessary and sufficient four-label criterion:
the joint Laplace transform of S,H,G plus the transform of the 2+2 shape
weighted by 1-exp(-qG). A raw mark transform was rejected because its value
at G=0 records invisible choices of binary resolution; it is not necessary
for finite-dimensional convergence. The weighting fixes that issue.

The balanced-shape target subdensity is exp(-3S-2H-G) on S,H,G>0.
Consequently the disjoint-pair burst statistic with S<=T,H<=h,G>=epsilon
has target (1-exp(-3T))(1-exp(-2h))exp(-epsilon)/6, tending to zero as h
tends to zero after the large-population limit. Keeping G>=epsilon avoids
incorrectly ruling out genuine quadruple bursts.

Constructed a stronger counterexample than a four-state rate table alone:
superpose Kingman pair mergers at rate 1/3 per pair, a star event at rate 1/3,
and a fair two-color partition event at rate 2/3. The rules are consistent
under restriction. Every three-label law is exactly B_3, but disjoint-pair
events on four labels have total rate 1/4. The first four-label event still
has rate 3. Strictly binary delayed refinements retain these limiting facts.
Also constructed a separate example showing the unmarked four-label time
transform alone does not determine the genealogy.

Read the saved proof using:

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'

The priority request was denied again; this was only a small text read.
No simulations or numerical scripts have been run.

## 5. Independent analytic audit saved

Created AUDIT.md. Re-derived both transforms from a five-state generator
with states 4,3,31,22,1, independently of the proof's route mixture.
Solved the forward equations and checked the absorption-time density:

    f_V(t)=(11/6)exp(-t)-2exp(-2t)+(1/2)exp(-3t).

Its transform at s=1 is 3/8, agreeing with F(1,1,1). Its mean is 25/18,
also obtained as E S+E H+E G=1/3+1/3+13/18. The balanced-shape visit
probability is 1/6 by both incoming flux and the marked transform.
The later holding times are dependent: Cov(H,G)=1/108. Assuming independent
holding times would therefore break the proposed extension.

Exhaustively counted the sixteen fair-coin assignments analytically (no
program): 2 quadruple, 8 triple/singleton, 6 two-pair. This reproduces the
counterexample's rates. Independently solved its 22 forward equation. At
t=log 2 the target 22 probability is 1/16 and the counterexample's is 7/64;
the gap 3/64 agrees with the separate direct-entry convolution.
The burst atom agrees from density integration and from first-event type
probability 1/12. Added this single-time separation to PROOF.md.

Checked collapsed holding times, conditional label orbits, order-statistic
multiplicity, restriction consistency, finite histories, and ordering across
successive delayed binary resolutions. No failure found. The proof now
explicitly verifies that its label reconstruction also realizes the target
law when initial triple or final multiple mergers collapse intermediate
states. No N-BBM estimate is claimed.

## 6. Final report and readback

Created REPORT.md with the required first line:

    VERDICT: PARTIAL exact four-lineage criterion and disjoint-merger exclusion diagnostic

Ran the recorded final readback command:

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'wc -l LOG.md PROOF.md AUDIT.md REPORT.md; cat AUDIT.md REPORT.md'

Before this append it reported 130, 366, 204 and 107 lines, respectively.
The output matched the saved statements. Clarified in the audit that the
marked-payoff backward equations have zero payoff for direct absorption
from four or three blocks. All final numerical claims were checked by the
second derivations recorded there. The result is the four-label auxiliary
criterion and counterexamples; actual N-BBM estimates remain the next task.
