# T179 log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 01:38 Asia/Tbilisi.

## Orientation and literature check

Read the earlier REPORT.md, LOG.md, PROOF.md and check_heat.py in
~/codex_op_1114/briefs/T179, without editing them.
Read the startup memory index, brain navigation index and compute state.
The compute state says warn/owner_away_open, with CPU saturation; only tiny
single-thread calculations are planned. All writes remain in this folder.
The task-specific restriction excludes writes to the external mesh,
checklist and brain logs. No git, subagents or external messages.

Web search queries included “2611.07310 stochastic heat”, “Yi Han stochastic
heat nondegenerate continuous coefficient uniqueness November 2026”, and
“2611.07310 L2 uniqueness”. Opened the official abstract and full HTML at
https://arxiv.org/abs/2611.07310 and
https://arxiv.org/html/2611.07310v1, and the original full HTML at
https://arxiv.org/html/2608.01279v1.
The abstract still lists only v1, submitted 5 November 2026. Theorem 1.1,
Theorem 1.2(ii), Proposition 8.1 and the paragraph after Theorem 1.2 still
have the exact scope recorded by the earlier worker. No later resolution
was found in the short search. The residual case remains unbounded g and
general L2 initial data. Literature status check ended within five minutes.

## Independent re-check of the earlier result

The conditional reduction holds. Independently, for any bounded Lipschitz f,
condition at delta and compare both laws with the deterministic bounded state
S_delta u0. On the event ||U_delta||<=R and
||U_delta-S_delta u0||<=r the error is the stated modulus; its complement
costs at most 2[C sqrt(delta)/r^2+M/R^2] for each solution.
Adding gives precisely the earlier (5). Taking delta->0, then r->0, then
R->infinity proves equality of one-time laws, and bounded-start restart
identifies the positive-time finite-dimensional laws.

The stochastic-error estimate also checks: the squared Hilbert-Schmidt norm
is p_(2r)(0)||g(U)||_2^2, whose leading heat-trace term is
(8 pi r)^(-1/2). Integration gives sqrt(delta)/sqrt(2 pi).
The positive-time boundedness parameters independently require
2 eta+(1+beta)/2<1 and eta>3/(2p), which are compatible for beta<1.
No error was found in the earlier main claim.

## Choice of one extension, before starting its proof

Prove an L1 contraction for the unique bounded-start laws by taking smooth
coefficient approximations and an ordered coupling. For two initial states,
couple four approximating solutions from their minimum, the two states,
and their maximum. Comparison bounds their L1 distance by the nonnegative
upper-minus-lower solution; its expected spatial integral is preserved.
This would give a modulus independent of both initial spatial suprema.

The reason for choosing this route is that scalar order is available even
when the limiting equation has no pathwise uniqueness: only the approximating
equations need synchronous comparison, and uniqueness in law identifies the
limiting marginals. L1 Lipschitz observables may already suffice to identify
H-valued laws. The proof must check tightness, uniform integrability,
comparison for the approximants, and the measurable-state-space issue.

## 01:44 +04: contraction proof saved

Wrote PROOF.md. The key estimate for each smooth approximation is
E||X_n^v(t)-X_n^w(t)||_1 <= ||v-w||_1. The enclosing ordered solutions
start from v min w and v max w. Their difference is nonnegative, so its
L1 norm is its spatial mass, whose expectation is constant. This bound
does not contain the approximating Lipschitz constant. Tightness and the
cylinder martingale problem identify each bounded-start marginal limit
using Han's Proposition 8.1.

Combining the L1 bound with ||D||_2^2<=||D||_1||D||_infinity and the
uniform positive-time supremum moment gives the missing (UC) with exponent
1/2. Its constant depends on the initial L2 ball and time interval but
not on initial spatial suprema. Applying the earlier reduction then gives
uniqueness from every deterministic L2 state, conditional on the cited
bounded-start theorem.

An independent closure uses bounded L1-Lipschitz tests directly, yielding
an initial-restart error O(delta^(1/4)) without an H cutoff. Fourier
characteristic functions are such tests and determine H-valued laws.
This avoids confusing L1 convergence with H convergence.

For a second check of the L1 mechanism, opened Nicolas Fournier and
Jacques Printems, arXiv:1007.0896v1, official abstract and PDF.
Proposition 6 gives a related L1 martingale inequality for Lipschitz
coefficients with Neumann boundary conditions. The present periodic proof
uses comparison and mass conservation, not a claimed extension of their
theorem to Hölder coefficients. Initial attempts to open the author's
PDF and the Utah lecture-book mirror timed out; the official arXiv PDF
opened. Also opened Lenya Ryzhik's Spring 2016 SPDE notes and read their
comparison theorem as a consistency check; no theorem from those notes
is needed or cited as a research result in PROOF.md.

Proof audit now focuses on the approximation limit and the order
comparison argument. Neither a common-noise limiting uniqueness theorem
nor a uniform bound on g_n' is assumed.

## 03:31 +04: resumed audit of the saved argument

Read the complete earlier proof and scalar-arithmetic script again, and
read the current draft through its two closure arguments. The earlier
conditional reduction still checks independently. Opened the official
Han abstract and HTML again: v1 and Proposition 8.1 retain the bounded-
initial-data restriction. The short search returned no later resolution.
Opened the Fournier--Printems abstract and full PDF; both authors and the
Lipschitz/Neumann scope agree with the draft's citation.

The extension remains the single chosen piece: supply the missing uniform
continuity through comparison of smooth approximations. Audited the
colored-noise comparison, its white-noise limit, the tightness operator,
and the two different test classes used to close the initial-time gap.
Small clarifications to make before final reporting: restrict the displayed
H modulus to bounded Lipschitz tests, justify uniformity in the noise
smoothing parameter, and give the martingale-measure and Borel-kernel
arguments more explicitly. These do not change the contraction estimate.

All mutations stay here. The current compute state remains warn with CPU
saturation; no simulation is needed. A tiny standard-library diagnostic
will independently check the analytic exponents and the enclosing-mass
identity. This will be supporting arithmetic, not a numerical proof of
an SPDE assertion.

## Exact-arithmetic diagnostic and proof clarifications

Expanded the martingale representation and obtained Borel state-law kernels
as pointwise limits of the measurable Lipschitz-approximation kernels.
This removes the draft's unnecessary abstract Borel-graph assertion.
Made the noise-smoothing moment bound explicitly uniform in its smoothing
parameter. Restricted the H modulus statement to bounded Lipschitz tests,
which is exactly the class needed by (UC).

One edit attempt failed context matching before changing any file; the
corrected patch applied. No mathematical calculation failed.

Created check_estimates.py and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_estimates.py
```

Output:

```text
nice: setpriority: Operation not permitted
beta=1/100; eta=99/800; p=14; inner=301/400; outer_gap=93/5600
beta=1/2; eta=1/16; p=26; inner=7/8; outer_gap=1/208
beta=2/3; eta=1/24; p=38; inner=11/12; outer_gap=1/456
beta=3/4; eta=1/32; p=50; inner=15/16; outer_gap=1/800
beta=99/100; eta=1/800; p=1202; inner=399/400; outer_gap=1/480800
beta=999/1000; eta=1/8000; p=12002; inner=3999/4000; outer_gap=1/48008000
three crossing/signed envelope-mass identities: exact
three unit-L2 spike identities with growing supremum: exact
restart exponents: H modulus 1/8; L1 tests 1/4
nice=20; peak RSS=13.67 MiB
```

Exit code 0. Like the earlier worker's run, the launcher inherited nice 20;
the script checked that value before calculating. Its rational-arithmetic
calculations used one thread and completed immediately. The warning was
not a computation failure. No data were written outside this directory.

The exact exponent checks are supplementary: the inequalities for all
0<beta<1, and both restart rates, are proved symbolically in PROOF.md.
The signed example checks a potential error: |integral(v-w)| cannot replace
integral|v-w|. The spike example checks the uniformity as the bounded
initial functions' spatial suprema diverge. Neither diagnostic approximates
the stochastic equation or claims to test uniqueness numerically.

## Final mathematical audit and report

The load-bearing constant one in the L1 estimate was checked two ways:
the nonnegative enclosing-gap mass martingale gives the upper bound, and
constant diffusion with a constant initial displacement attains it.
The L2 exponent 1/2 follows from the deterministic L1/Linfinity
interpolation and Cauchy--Schwarz in probability; it needs no independence
of those norms. The two independent restart arguments give powers 1/8
and 1/4 from the same squared stochastic error delta^(1/2).

Rechecked the inner heat exponent by the L^(1/(1-beta)) norm of p_r^2,
and the outer exponent by direct L^(p/(p-1)) integrability. Both are
compatible for every beta<1. The diagnostic verifies the rational
algebra at six exponents, including beta=2/3 and beta=999/1000.
The old constant-noise variance coefficient also re-derives from the
zero Gaussian image and independently from the Fourier Riemann integral:
2 sqrt(pi*a)/a with a=8*pi^2 equals 1/sqrt(2*pi).

Checked the potential contradiction with known nonelliptic examples:
the limit of smooth approximations is identified with arbitrary
bounded-start solutions only by input (B). That step is unavailable in
those examples. No limiting pathwise comparison theorem was smuggled in.

Wrote REPORT.md with verdict PROVED for the bounded-start-to-L2 extension
and uniform modulus, expressly retaining Han's Proposition 8.1 as the
external uniqueness input. The proof does not independently certify the
entire new preprint. No post-report complete solution was found, so there
is no new SOLVED_ELSEWHERE.md. All written files are inside this folder.

Final read-only verification at approximately 03:37 Asia/Tbilisi:
REPORT.md starts with the required verdict, PROOF.md states the bounded-
Lipschitz scope and external input explicitly, and the diagnostic and full
output are saved here. Existing runner files were left untouched.
