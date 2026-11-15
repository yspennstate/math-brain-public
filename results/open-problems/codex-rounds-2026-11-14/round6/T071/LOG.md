# T071 round 6 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 10:24 Asia/Tbilisi (UTC+4).

## 1. Orientation and literature check

Read the startup instructions at ~/.claude/brain_startup.md, the brain
navigation index and the compute governor state. The latter reports warn,
cpu_saturated, owner_away_open. The task's later folder-only rule supersedes
the global shared mesh/checklist/brain writers. None was invoked. No git,
subagents, external messages, background jobs or predecessor edits.

Listed all four predecessor directories with rg --files and ls. They contain
no mathematical scripts. Read their REPORT.md, LOG.md and PROOF.md; also
read the round-5 AUDIT.md. Reads use

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat <files>'

The sandbox reports `nice: setpriority: Operation not permitted`. No
numerical workload will be launched with that priority unverified; this
session's verification is analytic. Small text reads complete normally.

The opening web check ran between the shell readbacks at 10:24:25 and
10:26:17, within five minutes.
Queries included `"N-BBM" "genealogy" "2026"`, `"branching Brownian motion"
"selection" "Bolthausen" genealogy 2026 2025`, `"N-BBM" genealogy coalescent
2026 theorem`, and `"Berestycki" "N-BBM" 2026`.

Opened primary sources:

- Pascal Maillard, *Speed and fluctuations of N-particle branching Brownian
  motion with spatial selection*, https://arxiv.org/html/1304.0562v4.
- Alexandre Legrand and Pascal Maillard, *Time-inhomogeneous N-particle
  Branching Brownian Motion and the continuous random energy model*,
  https://arxiv.org/abs/2402.04917: still v4, 9 April 2026, displacement.
- Julien Berestycki and Oliver Tough, *Selection principle for the N-BBM*,
  https://arxiv.org/abs/2407.05792: stationary empirical measure.
- Jacob Mercer, *Branching Brownian motion with rank-based selection and
  reaction-diffusion equations*, https://arxiv.org/abs/2605.04860:
  hydrodynamics and velocity.

No qualifying genealogy solution found; this is a bounded search, not a
certificate of absence. No SOLVED_ELSEWHERE.md is warranted. No further
literature search is planned.

## 2. Independent recheck of round 5

The main claim holds. Count ordered terminal quadruples by their four
distinct younger colors. The older filter ensures that the two pairs use
disjoint colors, so the numerator is a nonnegative multilinear homogeneous
degree-four polynomial F. For a branch of color a followed by deletion of
color b, its change is

    partial_a F(x) - partial_b F(x+e_a).

Summing the first term over the N possible parents gives 4F by Euler's
identity; the second gives exactly the stated nonnegative R. Thus
generator F=4F-R, including a=b. Independently pruning four independent
unselected Yule families bounds every distinct-color product by exp(4L).
This rederives the propagation bound without any selected-family
independence. The three possible pairings are disjoint, so their sampled
probability is 3F/(N)_4. The short-window constant is
3*N*(N-1)*[2exp(ell)(exp(ell)-1)]^2/(N)_4, hence twelve as reported.

Checked the sharpness calculation separately: F=8x1*x2*x3*x4,
E[PZ]/E[P]=8exp(L)-4, and exp(4log(N/16))=(N/16)^4.
The retained fraction 1/2 yields 3*8/(2*16^4)=3/16384.
The spatial crossing error is superpolynomially small at this L. No error
was found. These conditional examples do not establish their frequency in
the all-zero late-time observation regime.

## 3. Chosen extension, recorded before the proof

Derive an exact spatial representation of the distinct-color descendant
kernel using k distinguished particles (ultimately k=4). In a killed
auxiliary N-particle process, ordinary particles branch at rate one,
distinguished particles at rate two, and a distinguished particle chooses
one daughter uniformly. Leftmost selection is unchanged. Kill the whole
auxiliary process when any distinguished line is deleted. Prove that the
original descendant product equals exp(kL) times its survival probability.

Then compute its killing rate and remove killing events to obtain a
conservative process and an occupation-time exponential. This is one
extension: an explicit representation of the selection correction, with
the older filter retained by summing over the frozen admissible quadruples.
It will identify an averaged spatial estimate needed on the log-cubed
clock; it will not claim that estimate. In particular, the auxiliary
spatial law must not be silently replaced by ordinary N-BBM.

## 4. Proof saved

Created PROOF.md with the exact simplification

    generator F = kF-(N+k-1)partial_b F,

where b is the current minimum's color. For k=4 the previously unsimplified
loss is (N+3)partial_b F. Euler's identity applied to partial_b F proves
the coefficient. A separate marked-history density calculation gives

    E product_j W_(a_j)(L) = exp(kL) P^dagger(zeta>L).

The distinguished paths branch at rate two, not one. Removing killing
transitions gives a conservative process which suppresses births while
the minimum is distinguished. If A_L is its marked-minimum occupation,

    P^dagger(zeta>L) = E^circ exp(-(N+k-1)A_L).

Summing over the frozen admissible quadruples yields the exact filtered
formula (7) in PROOF.md. Formula (13) retains the actual random younger
configuration and ancestral restrictions in the proposed observation regime.

A load-bearing coefficient was checked before saving: at a marked minimum,
the ordinary parents contribute N-k, the other marked parents 2(k-1),
and the minimum's own branch contributes one. The killing rate is N+k-1,
not N; forgetting the doubled rate of the other marked parents would give
the wrong constant. The polynomial calculation independently confirms it.

The arithmetic-geometric mean bound gives the occupation lower-tail
constraint (11). It does not imply the needed small-window estimate;
after restoring exp(kL), it returns the elementary product bound.

Read back with

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat PROOF.md; date "+%Y-%m-%d %H:%M:%S %Z"'

The command returned the saved proof and the same priority warning. No
simulation, mathematical script or numerical evidence is claimed.

## 5. Independent audit and attempted failures

Created AUDIT.md and read it back, alongside the round-5 audit, with

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat <round-5>/AUDIT.md; cat AUDIT.md; date "+%Y-%m-%d %H:%M:%S %Z"'

The output matched both files and gave 2026-11-15 10:32:35 +04, with
the same rejected priority change. Also read the remaining round-3 proof
sections and round-4 log sections separately to avoid combined-output
truncation. No predecessor files were changed.

The second derivation of (N+k-1) expands one monomial directly and sums
the included-color and excluded-color parent contributions. A separate
generator intertwining checks the marked-history density proof and the
factor exp(kL). For k=N, direct extinction at hazard N-1 gives
E product W=exp(-(N-1)L), while the conservative process has A_L=L and
gives exp(NL-(2N-1)L), the same answer. Thus N=k=4 gives exp(-3L),
exposing both a missing rate-two term and a spurious extra death rate.

For a uniformly chosen single root, mass conservation gives exactly
E^circ exp(-N A_L)=exp(-L), independently of starting positions. The
polynomial F=sum x_v gives the same normalization. This does not extend
to uniform marked-rank probabilities for the filtered four-root mixture.

Checked empty C, L=0, extinct colors, multiple copies of a root color,
Brownian crossings, tied daughters and arbitrary initial ties. Specified
that the selection tie rule must not consult the auxiliary mark choice.
The occupation lower-tail inequality has the correct direction; Jensen
separately gives the consistent mean-occupation lower bound recorded in
AUDIT.md. No failure was found in the saved finite-N representation.

Failed routes: replacing the marked law by ordinary N-BBM changes the
generator; replacing the filtered tuple law by uniform marks discards
ancestral/spatial correlation; bounding only mean occupation has the wrong
Jensen direction for an upper bound on the required exponential moment.
The universal lower-tail estimate merely translates the elementary
product bound. None gives the needed averaged short-window estimate.

## 6. Final report and readback

Created REPORT.md with first line

    VERDICT: PARTIAL exact rank-occupation formula for the filtered descendant kernel

Final readback command:

    env OMP_NUM_THREADS=1 nice -n 15 sh -c 'cat AUDIT.md REPORT.md; wc -l LOG.md PROOF.md AUDIT.md REPORT.md; date "+%Y-%m-%d %H:%M:%S %Z"'

It returned the saved audit and report, then 166, 295, 184 and 104 lines
respectively, before this append, and 2026-11-15 10:33:30 +04. The only
warning was the rejected priority change. Checked the required verdict,
the exact N+3 coefficient, the conservative law's suppression rule, the
retained older filter, and the explicit unresolved averaged estimate.
Deliverables are LOG.md, PROOF.md, AUDIT.md and REPORT.md, all in this
folder. No numerical results or solution of the original conjecture are
claimed. All writes remained inside this folder.
