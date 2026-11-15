# T097 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
15 November 2026, Asia/Tbilisi. First retained local clock reading:
08:14:56 +0400.

## Orientation and literature check

Read REPORT.md, LOG.md and PROOF.md in all three predecessor folders,
and the round 4 AUDIT.md. `rg --files` found no mathematical scripts in
those folders. Earlier folders remain read only. The task-specific rule
forbids external writes, so no brain, mesh or external checklist mutations
are made. No git or subagents are used.

Read the brain navigation index and compute_state.json. The latter said
status ok, mode owner_away_open. Shell reads use
`OMP_NUM_THREADS=1 nice -n 15`; the sandbox reports
`nice: setpriority: Operation not permitted`. No numerical workload is
launched. This session will use analytic proofs and lightweight file checks.

Web-search queries:

- `Gaussian free field lattice critical exponents 2026 percolation h star`
- `Gaussian free field percolation lattice critical continuity one arm 2025 2026 Muirhead`

Opened arXiv:2610.03703, arXiv:2611.05357, arXiv:2002.07735 and the full
HTML of arXiv:2206.10724v2. The two 2026 papers concern cable systems.
No later solution of the lattice problem was found. The check is complete
within five minutes; no SOLVED_ELSEWHERE.md is warranted. Muirhead's
Theorems 1.2 and 1.10 again give theta(h_*-t)>=c_q t^q for each q>4,
not the endpoint q=4. The source uses the same SRW Green covariance.

Read commands:

    OMP_NUM_THREADS=1 nice -n 15 rg --files <three predecessor folders> .
    OMP_NUM_THREADS=1 nice -n 15 cat <predecessor REPORT.md LOG.md PROOF.md>
    OMP_NUM_THREADS=1 nice -n 15 cat <round 4 AUDIT.md>

## Independent recheck of the round 4 result

The unit-cell transfer holds: Cauchy-Schwarz in the line displacement and
cell variable, followed by tiling at each fixed displacement, bounds the
sum of squared lattice differences by integral |grad F|^2. With the SRW
factor 1/6 and the half-cell enlargement, this gives the stated capacity
bound. Independently differentiate the parallel volume

    8a^3+24a^2 s+6 pi a s^2+(4 pi/3)s^3

to recover S_a(s)=24a^2+12 pi a s+4 pi s^2. Completing the square with
w=2s/a+3 gives

    integral_0^infinity ds/S_a(s)
      = log((3+delta)/(3-delta))/(4 pi delta a),
    delta^2=9-24/pi.

The minimum profile energy is the reciprocal integral, so division by 6
gives exactly C_cube a, where a=R+1/2. The finite-cutoff profiles are
admissible before the cutoff tends to infinity. This main capacity claim
holds.

An independent Gaussian-tail check gives a ratio loss at most
s sqrt(2 log(1/p))+O(s+s^2), s=t sqrt(cap(B_R)). With
log(1/p_R(h_*))<=(2+epsilon)log R and R=c/(t^2 log(1/t)), the leading
loss is sqrt(8 C_cube c) as epsilon tends to zero. Equating it with
log 2 recovers (log 2)^2/(8 C_cube). Small radii require continuity,
as the predecessor correctly checked. The earlier result survives.

No critical nonpercolation or identification of L_rel with a conventional
correlation length is inferred from this calculation.

## Chosen extension, recorded before proof

Choose one capacity extension: establish the matching reverse transfer
from lattice functions to continuum functions, using piecewise trilinear
interpolation. Together with the predecessor's cell-averaging transfer,
this should identify the actual leading coefficient rather than another
restricted trial-family coefficient.

Define kappa as one sixth of the infimum of integral |grad F|^2 over
compactly supported Lipschitz continuum functions equal to one on [-1,1]^3.
The target is the exact finite-radius sandwich

    kappa R <= cap(B_R) <= kappa (R+1/2),  R>=1.

This would prove cap(B_R)=kappa R+O(1), with error between zero and
kappa/2, and identify the best leading coefficient in the capacity method.
The reverse transfer is elementary enough to check directly without any
external continuum-limit theorem. Check also whether a variation on a face
strictly lowers the previous distance-profile energy, so that the limiting
coefficient is strictly less than C_cube. Any such variation is part of
the same capacity problem, not a claim about a new percolation exponent.

Reason: round 4 leaves the true leading cube-capacity coefficient
unidentified. The two transfers address that precise gap. They will not
remove the logarithm from L_rel, and no connection-specific score estimate
is assumed. All work is analytic; no numerical script is required.

## Proof completed

Created PROOF.md. The reverse transfer works exactly: on one unit cube,
the integral of a squared coordinate derivative of the trilinear
interpolant is at most one fourth of the sum of the four corresponding
squared edge differences. Each edge belongs to four cubes, so the factors
cancel. The interpolant equals one on the whole solid Q_R when the lattice
function equals one on B_R. Taking infima proves the lower bound
kappa R<=cap(B_R). The earlier unit-cell transfer proves the upper bound
cap(B_R)<=kappa(R+1/2). Consequently the actual capacity coefficient is
kappa, with an error in [0,kappa/2], uniformly in integer R>=1.

The distance profile is strictly suboptimal: its Laplacian is positive in
each open face region. Six disjoint separable tent variations have total
gradient energy 16 and a negative energy cross term bounded in magnitude
below by 36 pi/[J(24+16 pi)^2], where J=1/(6 C_cube). Optimizing the
quadratic perturbation proves

    kappa <= C_1 := C_cube
                     -486 pi^2 C_cube^2/(24+16 pi)^4 < C_cube.

The same Gaussian comparison now yields the bound

    liminf t^2 log(1/t) L_rel(t) >= (log 2)^2/(8 kappa)
                              >= (log 2)^2/(8 C_1).

This is a deterministic capacity extension and its existing-method
consequence. It does not improve a critical exponent or eliminate the
logarithmic loss. The leading capacity coefficient is identified
variationally, not evaluated in closed form. Novelty is not established.

Commands after proof construction:

    OMP_NUM_THREADS=1 nice -n 15 tail -n 110 <first predecessor>/PROOF.md
    OMP_NUM_THREADS=1 nice -n 15 rg -n 'L_rel|486|kappa|is finite|C_1' PROOF.md
    OMP_NUM_THREADS=1 nice -n 15 date '+%Y-%m-%d %H:%M:%S %z'

The last clock reading was 08:21:26 +0400. These were read-only checks;
the priority warning persists. The text search caught a missing newline
in the finiteness paragraph; it was corrected. No computation was run.
One multi-file patch was rejected for a log-context mismatch; it made no
changes. Reapplying with the exact context succeeded.

## Adversarial checks completed

Created AUDIT.md. Independently re-derived the interpolation factor from
the eigenvalues 1/2 and 1/6 of the one-dimensional linear-basis Gram
matrix. Its tensor square has largest eigenvalue 1/4, which cancels
the four cubes incident to each edge. A single-site trial function gives
lattice energy 1 and interpolated continuum energy 4/9, checking the
direction and the factor 1/6 separately.

Re-derived the perturbation energy through one-dimensional rescaling,
then checked 486 by inserting a fixed trial amplitude instead of
optimizing a quadratic. The normalized base, cross and square terms are
C_cube, -972*pi^2*C_cube^2/D^4, and +486*pi^2*C_cube^2/D^4,
where D=24+16*pi. This again gives exactly the stated decrement.
The elementary bound decrement/C_cube<1/400 is a separate magnitude
check, not a numerical computation. The old C_cube remains valid; its
restricted optimality never implied harmonic optimality.

Checked finite support before limits, nonnegative versus arbitrary real
trial functions, all cube boundaries, null support intersections, R=1,
the half-cell enlargement and integer-radius restriction. Gaussian tails
independently reproduce the new relative-radius coefficient. The
logarithmic loss persists, and no relation to a conventional correlation
length was found. Created LITERATURE.md listing only opened papers.

## Final report and file verification

Created REPORT.md with verdict PARTIAL. The completed extension is the
two-sided capacity sandwich with a uniform bounded error, together with
the strict face-variation improvement. The requested exact lattice
exponent problem remains unresolved. No claim of novelty is made.

Ran:

```sh
OMP_NUM_THREADS=1 nice -n 15 sh -c 'for f in LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md; do if test -s "$f"; then echo "$f: present"; else echo "$f: MISSING"; fi; done; head -n 1 REPORT.md; wc -l LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md; date "+%Y-%m-%d %H:%M:%S %z"'
```

Output:

```text
nice: setpriority: Operation not permitted
LOG.md: present
PROOF.md: present
AUDIT.md: present
LITERATURE.md: present
REPORT.md: present
VERDICT: PARTIAL the actual cube-capacity coefficient with a bounded error and a strict improvement of the previous trial constant
164 LOG.md
384 PROOF.md
177 AUDIT.md
31 LITERATURE.md
74 REPORT.md
830 total
2026-11-15 08:24:39 +0400
```

The LOG.md line count precedes this final append. Also ran:

```sh
OMP_NUM_THREADS=1 nice -n 15 rg -n '486|972|kappa R|kappa/2|8 kappa|VERDICT|Next worker|Task:' REPORT.md PROOF.md AUDIT.md LOG.md
```

Output confirms consistent factors 486 and 972, the error kappa/2,
the coefficient (log 2)^2/(8 kappa), the required verdict, next-worker
guidance and task attribution. All authored artifacts are confined to
this folder; no mathematical script, numerical workload or external
mutation was used. The final proof checks justify no further test runs.
