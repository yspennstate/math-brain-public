# T071 round 4 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 04:34 Asia/Tbilisi.

## 1. Orientation and bounded literature check

All writes are confined to this folder. The task's explicit folder-only order
supersedes the global requests to mutate the shared mesh, checklist and brain;
none of those shared commands was run. No git or subagents. Read the startup
memory at ~/.claude/brain_startup.md and the compute governor state. The latter
reported warn/cpu_saturated, owner_away_open. No simulation is planned.

All shell reads after the initial pwd use `env OMP_NUM_THREADS=1 nice -n 15`.
The sandbox reports `nice: setpriority: Operation not permitted`; reads still
finish. No numerical workload will be launched with an unverified priority.

Used rg --files on both predecessor folders. They contain no mathematical
scripts: PROOF.md, AUDIT.md, LOG.md and REPORT.md are the substantive work.
Reading these files, with no edits to either predecessor directory.

The opening web check (under five minutes) searched:

- `"N-BBM" "genealogy" "2026"`
- `"branching Brownian motion" "selection" "Bolthausen" genealogy conjecture`
- `"N-BBM" genealogy 2025 2026 coalescent proof`
- `"branching Brownian" "selection" "genealogies" 2026 2025`

Opened these primary sources:

- Pascal Maillard, *Speed and fluctuations of N-particle branching Brownian
  motion with spatial selection*, https://arxiv.org/html/1304.0562v4.
  Section 1.4 explicitly says the spatial comparison deforms genealogy.
- Alexandre Legrand and Pascal Maillard, *Time-inhomogeneous N-particle
  Branching Brownian Motion and the continuous random energy model*,
  https://arxiv.org/abs/2402.04917, latest version v4, 9 April 2026.
- Jacob Mercer, *Branching Brownian motion with rank-based selection and
  reaction-diffusion equations*, https://arxiv.org/abs/2605.04860.
- Julien Berestycki and Oliver Tough, *Selection principle for the N-BBM*,
  https://arxiv.org/abs/2407.05792: stationary empirical measure.
- Jacob Mercer, *Critical Drift for Brownian Bees and a Reflected Brownian
  Motion Invariance Principle*, https://arxiv.org/abs/2412.04527:
  includes a rigorous proof concerning the N-BBM speed, not genealogy.

No later solution of the stated genealogy problem was found. This is a
bounded negative search, not an exhaustive bibliographic conclusion. The
speed attribution in the brief needs care: Maillard distinguishes his
log-cubed finite-time theorem from the fixed-N long-time speed. This session
does not attempt to settle the speed bibliography.

## 2. Independent verification of the preceding main claim

Read both predecessors' REPORT.md, LOG.md, PROOF.md and AUDIT.md in full.
Neither folder has a mathematical script. The round-3 criterion holds under
its hypotheses. Here is a new check using pair-time multiplicities rather
than its route probabilities or five-state backward equations.

At four labels let A_ij be pair MRCA times. S is their minimum, U their
second order statistic counting repetitions, V their maximum. For a binary
chain ending in 2+2 their sorted multiplicities are (S,U,V,V,V,V); for a
chain ending in 3+1 they are (S,U,U,V,V,V). Thus the times and balanced mark,
with the mark ignored at G=V-U=0, encode every visible orbit of chains.
When H=U-S=0<G a balanced chain would create a simultaneous disjoint event;
the target marked measure assigns zero mass to this case. When G=0 both
marks have the same visible partitions. This confirms the collapsed cases
needed in the sufficiency argument.

Independently calculate the balanced-route subdensity: there are three
unordered pairings, two possible orders for each, a first specified-pair
rate 1/3, a subsequent complementary-pair rate 1/2, and final holding density
exp(-g). Thus its coefficient is 3*2*(1/3)*(1/2)=1 and its density is
exp(-3s-2h-g). Its marked transform is
q/[(s+3)(r+2)(q+1)], exactly the preceding report. Four-to-one and
four-to-two direct jumps have total rates 1/3 and 2/3; from three blocks
the absorption and pair-jump rates are 1/2 and 3/2. Combining these rates
gives the preceding unmarked transform as well. The marked mass is 1/6.

Explicitly, the four unmarked route contributions are

    1/[3(s+3)],
    2/[3(s+3)(q+1)],
    1/[(s+3)(r+2)],
    3/[(s+3)(r+2)(q+1)].

Their sum is exactly the round-3 F(s,r,q). At zero exponents they give
1/9, 2/9, 1/6, 1/2 and sum to one.

The counterexample check is independent via restricted partitions: on four
labels the extra rate of each two-pair split is 1/12. The three-label
specified pair rate is a+b+d=1/3+1/12+1/12=1/2, and triple rate is
b+c=1/12+5/12=1/2. The excess incoming 22 flux is exp(-3t)/4; convolution
with exp(-t) survival gives (exp(-t)-exp(-3t))/8, hence 3/64 at log 2.
No error found in the earlier auxiliary theorem. No N-BBM claim is hidden
in this verification.

## 3. Chosen extension, recorded before writing the proof

Convert the disjoint-burst event to a fourth factorial moment of actual
N-BBM descendant families at deterministic times. The weight of an ancestor
must be its number of descendants at the sampling time, not its number of
children at the end of the short interval. This distinction is where
selection-induced sampling bias enters.

The piece will give an exact finite-N identity with an additional older-time
filter preserving the two separate families, followed by a sliding-window
bound for the round-3 statistic. A uniform O(h^2) estimate on this population
observable would imply the requested iterated zero limit. As a directly
proved N-BBM estimate, use independent Yule-family domination to bound the
same statistic when the younger endpoint is the sampling time. This controls
physical windows shorter than (1/2)log N, but does not reach fixed rescaled
h(log N)^3 windows. The proof will state that limitation explicitly.

This is one extension: a population-family moment method for the previous
disjoint-pair obstruction. It is not a claim to prove the N-BBM genealogy
conjecture or the full required burst bound.

## 4. Proof saved

Created PROOF.md. It uses the explicit regime: N particles initially at 0,
sample uniformly at tau_N=(log N)^4, backward clock a_N=(log N)^3. All
finite-N identities are uniform over starting configurations.

For younger-ancestor terminal weights w_v and middle-ancestor terminal
weights d_i, the collision increment is c_i=(d_i)_2-sum_(v from i)(w_v)_2.
Aggregate c_i by an additional older ancestor z to get zeta_z. The population
statistic Q=sum_(z!=z')zeta_z*zeta_z'/(N)_4 has three times its expectation
equal to the probability of four distinct younger ancestors becoming 2+2
and persisting as two separate families to the older time.

A sliding window of length 2h gives an exact equivalent criterion, rather
than only a sufficient one: if A is the endpoint probability plus 1/h times
the integrated window probability, then

    P(B(T,h,epsilon)) <= A <= 3 P(B(T+2h,2h,epsilon/2)).

The endpoint term handles first mergers near time zero without any assumed
pair-time or first-merger-time convergence. Uniform O(delta^2) expected Q
is sufficient; the equivalent criterion needs only an averaged estimate.

For the actual N-BBM a direct Yule domination gives

    P(2+2 at physical lag ell)
       <= min(1,12*exp(2ell)*(exp(ell)-1)^2/((N-2)*(N-3))).

This is at most (12+o(1))*N^(-4eta) for ell<=(1/2-eta)log N. It controls
the sampling-endpoint term on a prescribed microscopic window, not the
full averaged criterion at fixed rescaled h. No numerical computation.

## 5. Independent audit and attempted failures

Created AUDIT.md. An unordered-sample derivation independently gives the
factor three and (N)_4 denominator. A hand-counted N=8 forest with unequal
terminal weights gives probability 2/35 both by direct enumeration of four
subsets among 70 and by the moment numerator 32. Merging the two families'
older ancestors changes this probability to zero, correctly reflected by
the older filter. Setting terminal weights to one gives the wrong answer.

Re-derived the sliding-window interval directly from S,U,V. This checks
the endpoint term, persistence margin and the factor three in the two-sided
bound. Strengthened the finite-history condition to log N>T+2epsilon so
both enlarged burst tests are decided inside the recorded history.

For normalized B_4, independently by route integration and forward ODEs,

    P(E(s,delta,e)) = exp(-3s-delta-e)*(1-exp(-delta))^2/2.

Its expected Q has leading coefficient exp(-3s-e)/6 times delta^2. The
old counterexample instead has a linear term exp(-3s-e)*delta/12, so the
normalized integrated moment detects it. This checks that the proposed
population criterion retains the obstruction it was intended to measure.

Re-derived the Yule factorial moment from the geometric law, independently
of the proof's generator ODE. Re-derived the constant twelve by unordered
family pairs and unordered four-element sampling. Re-derived the exponent
-4eta by taking logarithms. All central constants agree.

The Yule approach fails at ell=h(log N)^3 because its bound grows like
exp(4ell)/N^2; the probability minimum then gives only one. Extending it
from s=0 also fails without controlling the terminal descendant weights.
These are unresolved estimates, not small technical errors in the proof.

## 6. Readback and report

Read the saved proof with

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'

The output matched the proof; timestamp 2026-11-15 04:44:05 +04. The same
priority warning appeared. Added the explicit distinction between a target
coalescent window probability and the finite-population observable Q: no
population realization of the abstract counterexample is presumed.

Created REPORT.md with verdict PARTIAL. Deliverables are LOG.md, PROOF.md,
AUDIT.md and REPORT.md. No scripts or numerical results, no
SOLVED_ELSEWHERE.md, and no edits outside this folder. The proved estimate
is on physical log-N windows; the desired fixed rescaled-window moment
estimate remains open.

Final readback command:

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'wc -l LOG.md PROOF.md AUDIT.md REPORT.md; cat AUDIT.md REPORT.md'

Before this last log update it returned 188, 327, 247 and 112 lines. The
saved audit and report matched the stated results and scope. The only
shell warning was the rejected priority adjustment; no computational data
are claimed. Final check: REPORT.md starts with the required VERDICT line,
each new proposition has a full proof, all load-bearing constants have a
second derivation, and the unresolved log-cubed estimate is stated explicitly.

