# T179 log

Task received: 14 November 2026, approximately 21:19 Asia/Tbilisi (17:19 UTC).
Ask: “push this problem forward by one checkable piece.”

## 17:19–17:22 UTC: orientation and literature check

Read the startup memory index and compute governor state. The latter reported
`status=warn`, `mode=owner_away_open`; no substantial computation is planned.
All writes stay in this folder. The task-specific restriction rules out the
usual external checklist, mesh, and brain-log writes. No git or subagents.

Read-only commands: `pwd`; `rg --files .`; `head -85` on the startup memory
index; `cat` on the compute state; a targeted `rg` in the brain navigation views.
No relevant prior mathematical result was found in those views.

Web queries: `"2608.01279"` and
`"stochastic heat" "uniqueness" "Hölder" "2/3" Han`.
Opened https://arxiv.org/abs/2608.01279,
https://arxiv.org/abs/2611.07310, and the full PDF mirror
https://arxiv.cnoctave.top/pdf/2611.07310.

The official arXiv page identifies a later paper by Yi Han, submitted
5 November 2026, claiming the full positive Hölder range. The theorem statements
distinguish bounded from unbounded coefficients and distinguish initial-data
classes. Next: read the official full text and audit those restrictions before
deciding whether the stopping condition applies.

## 17:20 UTC: scope audit and choice of piece

Opened the official new PDF and HTML, including page 3 and Section 8.1, and
the original paper's HTML. The original Theorem 1.1 allows every deterministic
L2 initial state and does not impose an upper bound on g. The newer result
explicitly leaves the combination “unbounded g, general L2 initial state” for
future work. Thus the whole source-level formulation is not settled; stopping
at the new abstract would miss an initial-data restriction.

Choice: prove a precise reduction of this residual case to a uniform continuity
estimate for the already unique transition laws from bounded initial states.
The reduction will quantify the initial stochastic error as O(t^(1/4)) in
mean-square root. This isolates one semigroup estimate that would extend the
new theorem to all L2 initial data, without claiming that estimate is known.
It is a manageable piece because the stochastic error uses only heat-kernel
scaling and sublinear growth, and conditional restart is available after any
positive time.

Additional web search: `"2611.07310" correction OR withdrawn OR gap` and
`"Weak uniqueness for the stochastic heat equation" "Han" "2026"`.
No correction was found in the returned results. This is not a proof audit of
the entire new preprint. Literature search ended within the ten-minute limit.

## Reduction design

The candidate missing estimate is uniform L2 continuity of the known bounded-
initial-state transition operators, on L2 balls and on time intervals bounded
away from zero. Conditional restart then compares two arbitrary rough-start
solutions to the same deterministic state S_delta u0. The error from each
solution to S_delta u0 is O(delta^(1/4)) in L2 mean-square root.

Audit issue identified: convergence U_delta -> u0 alone does not imply equality
of later laws. The transition operators need a continuity estimate uniform as
the bounded approximations' spatial suprema diverge. The proof must state this
as an additional, unproved hypothesis. Positive-time boundedness must also be
established rather than silently assumed. A heat-factorization argument gives
it for every beta<1 from L2 initial data.

## Proof completed; audit in progress

Wrote PROOF.md with the precise conditional theorem and its error bounds.
The proof includes stopped-integrand moment estimates, positive-time spatial
boundedness from L2 initial data, and the passage from single-time laws to
state-path laws. The limits are explicitly ordered: delta to zero, continuity
radius to zero, then the H-norm cutoff to infinity.

Independent checks prepared: Fourier and periodized heat-kernel derivations
of the small-time variance constant 1/sqrt(2 pi); a constant-coefficient check
of the continuity hypothesis; and an L2 singular initial function for which
every fixed spatial exit time is zero. Added a small scalar-arithmetic script
to compare the two covariance formulas. Its output will be recorded below.

First run command:
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 check_heat.py`.
It stopped before computing: macOS rejected a proposed RLIMIT_DATA reduction
with `ValueError: current limit exceeds maximum limit`. The `nice` launcher
also printed `setpriority: Operation not permitted`. A separate tiny Python
read confirmed the inherited priority is already 20, so no priority increase
is needed. `ps` is disallowed by the sandbox. Read the matching existing
macOS priority memory. Removed the rejected memory-limit setter; the script
uses a generator and five small rows, reports peak RSS, and refuses to compute
unless its actual nice value is at least 15. No mathematical calculation ran
during the failed attempt.

Successful rerun, same exact command:

```text
nice: setpriority: Operation not permitted
N=100000; images=8; five Fourier/image comparisons passed
predicted small-time constant = 0.398942280401
t=0.1  variance/sqrt(t)=0.447959509639  image-Fourier=2.533017e-07
t=0.01  variance/sqrt(t)=0.398942387325  image-Fourier=2.533017e-07
t=0.001  variance/sqrt(t)=0.398942280401  image-Fourier=2.533017e-07
t=0.0001  variance/sqrt(t)=0.398942280401  image-Fourier=2.533017e-07
t=1e-05  variance/sqrt(t)=0.398942280401  image-Fourier=2.533017e-07
Fourier tail bound = 2.533030e-07
data: heat_check.csv
nice=20; peak RSS=13.89 MiB
```

The warning concerns an attempted relative priority change on an already
nice-20 process. The script verified nice=20 before calculating. The run took
less than a second, used one thread and about 14 MiB peak RSS, and wrote only
heat_check.csv in this folder. These floating-point checks support the two
analytic derivations; they are not used as a proof of uniqueness.

## Self-audit

* Recomputed the stochastic-error exponent both by integrating the heat trace
  and by exact constant-noise Fourier variances. Its squared-norm constant is
  1/sqrt(2 pi), not 1/sqrt(4 pi); the generator is Delta, not Delta/2.
* Recomputed the spatial heat exponent as
  -1+(1-beta)/2 = -(1+beta)/2. Inner-time integrability requires
  eta<(1-beta)/4. Outer-time Holder integrability independently gives
  eta>3/(2p). Both can hold for every beta<1, with finite p.
* Checked all factors of two in (5)-(6) by first bounding one solution against
  the deterministic comparison state and then adding the second bound.
* Used stopped-integrand convolutions, rather than claiming that the stopped
  state U_(t wedge tau) obeys the same mild equation.
* Changed conditional restart to conditioning on the canonical state history,
  so no regular conditional law of an arbitrary ambient filtration is needed.
* A fixed spatial cutoff genuinely fails for u0(x)=dist(x,0)^(-a) near zero,
  0<a<1/2: its heat evolution diverges like at least t^(-a/2). The continuous
  stochastic remainder cannot cancel this. Every corresponding fixed cutoff
  has exit-time infimum zero.
* For constant g, synchronous coupling verifies (UC) with modulus at most r.
  No proof of (UC) for general g has been obtained. Assuming it automatically
  from smoothing would be the missing argument, not a valid shortcut.

## Final deliverables

Wrote REPORT.md with verdict PARTIAL. The completed piece is the conditional
continuity reduction, not a proof of its remaining semigroup hypothesis.
SOLVED_ELSEWHERE.md records the newer theorem without overstating its
initial-data scope. PROOF.md contains all mathematical steps; check_heat.py
and heat_check.csv contain the independent covariance diagnostic. The final
scope check excludes an unnecessary claim about the beta>2/3 rough-data case,
which the original paper already settles.
