# T097 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First local clock reading: 15 November 2026, 01:24:34 +04 (Asia/Tbilisi).

## Orientation and earlier files

Read the startup MEMORY.md and compute_state.json, then the earlier folder's
REPORT.md, LOG.md, PROOF.md, AUDIT.md and LITERATURE.md. Its directory listing
contains no mathematical scripts or numerical data to rerun. The present
folder initially contains PROMPT.md, codex.log and run.pid.

The task-specific rule forbids writes outside this folder. Accordingly no
external brain, mesh or checklist updates are made; the earlier folder is
read only. No subagents or git operations are used. Commands are prefixed
with OMP_NUM_THREADS=1 nice -n 15. The sandbox reports
`nice: setpriority: Operation not permitted`; no numerical workload is run.
The compute state is warn / owner_away_open with CPU saturation.

Read commands (all under the prefix above):

    /bin/cat ~/codex_op_1114/briefs/T097/{REPORT,LOG,PROOF,AUDIT,LITERATURE}.md
    /bin/ls -la ~/codex_op_1114/briefs/T097
    /bin/date '+%Y-%m-%d %H:%M:%S %z'

Output that matters: the earlier proof uses SRW Green covariance,
cap(B_R) <= (28R-1/R)/3, and Gaussian quantile comparison. Its claimed
consequences are beta >= 2 rho, p_R(h_*) >= R^(-2-epsilon), and
L_rel(t) >= c t^(-2)/log(1/t).

## Brief literature check

Used the web search tool for:

- `"Gaussian free field" "lattice" "critical exponents" 2026 percolation`
- `"2611.05357"`
- `"Gaussian free field" "critical" "November" "2026" percolation`

Opened arXiv:2611.05357, arXiv:2610.03703, and the full HTML of
arXiv:2206.10724v2. The two 2026 abstracts concern metric-graph clusters;
they do not resolve critical lattice excursions at h_* > 0. No subsequent
lattice solution has been found. Muirhead's Theorems 1.2 and 1.10 are being
checked directly as inputs to the independent verification below.

The literature check ends here, before five minutes of work. A final
targeted query for lattice critical exponents in November 2026 found no
resolution. No SOLVED_ELSEWHERE.md is warranted. Only the arXiv sources
actually opened will be cited.

## Independent verification of the earlier result

Re-derived the comparison by whitening the finite Gaussian vector: the
translation has Euclidean length t sqrt(1^T G_K^(-1)1), and the likelihood
ratio is decreasing in its standard normal coordinate. Moving any event's
mass to the upper tail minimizes its translated probability. Integrating
that tail gives exactly Phi(Phi^(-1)(p)-t sqrt(cap(K))). A one-site check
gives equality and fixes the sign. Last-exit decomposition gives
G_K e_K=1 and hence the asserted capacity normalization.

Independently checked the shell count: there are 6(2k+1)^2 edges between
sup-norm shells k and k+1, each with energy weight 1/6. Summing the squared
tent increments gives (28R-1/R)/3; R=1 gives 9 and R=2 gives 37/2.

For the exponent check, a bounded quantile displacement changes
log(1/p) by O(sqrt(log(1/p))+1). With t=R^(-1/2), the density exponent
beta therefore becomes beta/2 for the arm bound. Muirhead Theorem 1.2(2)
has gamma<1/4 in d=3; Theorem 1.10 applies it to the same SRW Green
normalization. Thus theta(h_*-t)>=c_q t^q for every q>4, exactly as used
earlier. This gives limsup[-log p_R(h_*)]/log R<=2. Inserting R of order
t^(-2)/log(1/t) in the relative-tail comparison gives a bounded loss, and
the subcritical theorem gives finiteness of L_rel. The earlier main claims
hold. No critical nonpercolation assumption is needed.

## Chosen extension, before its proof

Choose the sharper-constant option in the task: optimize the capacity test
function over all functions constant on sup-norm shells. The earlier tent
is not the optimizer. The shell problem is a series-resistance problem,
with proposed optimal energy

    [sum_{k=R}^infinity (2k+1)^(-2)]^(-1) = 4R + O(1).

Prove this variational formula, its optimality within this restricted class,
and its consequence for the same L_rel: the target quantitative improvement
is liminf t^2 log(1/t) L_rel(t) >= (log 2)^2/32, replacing an unspecified
small constant. This is one refinement of the earlier capacity method;
it does not claim a new exponent or a connection-specific score estimate.
As an adversarial check, use increasing Gaussian half-spaces to test whether
the normal-tail logarithmic loss can be removed by an event-independent
comparison.

## Proof completed

Created PROOF.md. The shell optimization is exact for each finite annulus:
the minimizing increments are proportional to (2k+1)^(-2), and the minimum
energy is the reciprocal of their sum. Taking the outer radius to infinity
gives A_R. A rational telescoping inequality improves the provisional
4R+O(1) target to

    cap(B_R) <= A_R <= 4R+1/(3R),
    A_R = 4R+1/(3R)+O(R^(-3)).

The identity that proves the explicit bound is

    1/(2k+1)^2 - [3k/(12k^2+1)-3(k+1)/(12(k+1)^2+1)]
      = 16/[(2k+1)^2(12k^2+1)(12(k+1)^2+1)].

Substitution in the earlier Gaussian comparison, together with its verified
critical arm limsup bound 2, proves

    liminf_{t->0} t^2 log(1/t) L_rel(t) >= (log 2)^2/32.

The proof checks all smaller radii, treats finitely many small radii by
continuity, and separately proves that L_rel is finite. Exact numerical
commands and numerical output: none; this is a proof-only extension.

## Adversarial audit completed

Created AUDIT.md. Re-derived the finite-annulus minimizer by Lagrange
multipliers, independently of Cauchy-Schwarz. Verified the telescoping
numerator 16 by substituting v=k(k+1). Summing the difference between
the midpoint sum and the integral confirms the leading coefficients
4 and 1/3 by another route. An optimized Holder inequality gives the
stronger relative comparison

    q/p >= exp[-s sqrt(2 log(1/p))-s^2/2],

and reproduces the denominator 32 in the crossover coefficient.

The proposed event-independent removal of the logarithm fails: increasing
half-spaces with critical probabilities R^(-2) have ratio tending to
exp(-delta) under shifts t_R=delta/(b_R sqrt(cap(B_R))), where
b_R^2=4 log R+O(log log R). Thus a half-ratio occurs even though
t_R^2 cap(B_R)->0. This is an obstruction for arbitrary increasing events,
not a counterexample about lattice connection events.

Checked finite radii, floor errors, normalization, the absence of any
assumption of critical nonpercolation, and the non-monotonicity issue for
the defining probability ratio. Created LITERATURE.md and REPORT.md.
Verdict PARTIAL: the sharper constant is proved, while the original
exponent problem remains open.

## Final file verification

Ran (with OMP_NUM_THREADS=1 nice -n 15):

    /bin/zsh -c 'for f in LOG.md PROOF.md AUDIT.md LITERATURE.md REPORT.md; do if [[ -s "$f" ]]; then print -r -- "$f: present"; else print -r -- "$f: MISSING"; fi; done'
    /usr/bin/head -1 REPORT.md
    /bin/date '+%Y-%m-%d %H:%M:%S %z'

Output:

    LOG.md: present
    PROOF.md: present
    AUDIT.md: present
    LITERATURE.md: present
    REPORT.md: present
    VERDICT: PARTIAL an optimized shell capacity bound and an explicit relative crossover coefficient
    2026-11-15 01:31:23 +0400

An attempted /usr/bin/rg was unavailable at that absolute path; rerunning
`rg` through PATH succeeded. Final consistency command:

    OMP_NUM_THREADS=1 nice -n 15 rg -n 'VERDICT|cap\(B_R\)|liminf|32|1/3|1/\(3R\)|Next worker|Task:' REPORT.md PROOF.md AUDIT.md

Output confirms the same capacity bound and crossover coefficient in the
proof, audit and report, and the required verdict and next-worker guidance.
All these calls remained lightweight read-only checks; nice continued to
report the sandbox priority restriction. No numerical workload followed.
