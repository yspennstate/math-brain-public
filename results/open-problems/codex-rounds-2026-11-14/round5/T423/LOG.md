# T423 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 15 November 2026, 09:16 Asia/Tbilisi (05:16 UTC).

## 1. Scope, reading, and bounded literature check

All writes remain in this folder. No git, subagents, external posting,
global checklist, mesh registration, or brain updates. The last three
would mutate files outside this folder and conflict with the task-specific
restriction. Read the brain startup file and compute state. Compute state
is ok/owner_away_open; no substantial computation is planned.

Read REPORT.md, LOG.md, PROOF.md in the original, round 3, and round 4
folders, plus both audit.py scripts. The original has no standalone
research script. These folders are read-only throughout this session.
Initial read-only orientation commands lacked the requested priority
prefix; subsequent shell commands use OMP_NUM_THREADS=1 and nice -n 15.
As in the earlier sessions the wrapper warns that setpriority is not
permitted: the inherited nice value is 20, already below nice 15.

The web search and page check finished within five minutes. Queries:

- `"super-Brownian" "pathwise uniqueness" 2026`
- `"stochastic heat equation" "nonnegative" "uniqueness" 2026 square root`
- `"1612.06055"`

Primary arXiv pages actually opened:

- Hao Wang, https://arxiv.org/abs/1612.06055: withdrawn, with a gap in
  the main proof stated on the record.
- Leonid Mytnik and Johanna Weinberger,
  https://arxiv.org/abs/2509.10984: weak existence and uniqueness.
- Yi Han, https://arxiv.org/abs/2611.07310: weak uniqueness on the
  torus with uniformly nondegenerate diffusion.
- Beom-Seok Han, Kunwoo Kim, and Jaeyun Yi,
  https://arxiv.org/abs/2407.06827: its abstract gives uniqueness in
  the strict-positivity regime, distinct from the compact-support regime
  relevant to the square-root equation.
- Yu-Ting Chen, https://arxiv.org/abs/1308.5141: nonuniqueness with
  immigration.

No verified resolution was found. This bounded search does not prove
that no resolution exists. No SOLVED_ELSEWHERE.md is warranted.

## 2. Independent recheck of the previous main claim

The mass bracket identity holds: direct noise isometry gives
E D_t^2=E integral A, and expansion of the two variances and covariance
gives the same 2mt-2 E integral C. Equality of terminal masses almost
surely therefore implies equality of the fields on the preceding interval.

For round 4, set N_s=exp(-b_s U_s)-exp(-b_s V_s), with
b_s=theta/[1+(T-s)theta/2]. The backward ODE b'=b^2/2 makes N a
square-integrable martingale. Independently of min/max differentiation,
write N=-H D, where H=b integral_0^1 exp(-b(V+rD)) dr>0. Comparing
Tanaka for HD with the product formula for H|D| gives
dL^0(N)=H dL^0(D). On D=0 this is b exp(-bU)dL. Thus
E|N_T|=E integral b exp(-bU)dL, including factor one.

For theta=lambda/T, T*b<=lambda and T*b exp(-bU) tends pointwise
to 2lambda/(lambda+2). The measure E dL has total mass ell<=2m,
so bounded convergence gives the previous finite-parameter limit.
The marginal Laplace exponent gap is exactly 4m/[T(lambda+2)];
the two-marginal triangle bound gives uniform error 8m/(lambda+2)
after multiplying by T. Sending T and then lambda to infinity gives
lim T*delta_T=2ell. The earlier main claim holds. No singular
extinction-kernel domination or unbounded-time optional stopping is needed.

## 3. Chosen extension, before proof development

Prove a uniform budget for local time after either population first becomes
small. Put M=min(U,V) and tau_a=inf{t:M_t<=a}. The target is

    E[L_infinity-L_{tau_a}] <= 2 min(m,a).

In particular local time created at common masses U=V<=a should have
expectation at most 2a, over the whole lifetime. Then translate this into
a quantitative localization of the original spatial occupation criterion:
the small-total-mass region should contribute at most 2a to its normalized
limsup, so uniqueness can be tested with M bounded away from zero.

Reason: the minimum has martingale bracket M dt and downward drift
-dL/2. Its remaining value at the first small-mass entrance pays for all
future local time. This uses absorption and the actual coupled mass
semimartingales, and would remove the simultaneous-extinction boundary
from the unresolved estimate. It does not assume spatial profiles are
controlled by their total masses.

Audits planned: derive the factor 2 a second way with a bounded concave
test of M; handle unbounded tau_a by bounded optional sampling only;
prove the weighted occupation limit rather than assume it; test zero
mass, a>=m, and local-time creation after one mass is zero. No claim
that this budget alone forces ell=0 is intended.

## 4. Extension derived

Tanaka gives M=m+N-L/2, where N is a square-integrable martingale
on every finite interval and d<N>_s=M_s ds. For sigma=T wedge tau_a,
bounded optional sampling, also multiplied by {tau_a<=T}, gives exactly

    E[L_T-L_sigma]
      =2b P(tau_a<=T)-2 E[M_T 1_{tau_a<=T}] <=2b,
    b=min(m,a).

The left side increases to E[L_infinity-L_{tau_a}], so the planned
bound holds without optional sampling at an unbounded time.

There is a finite-width spatial consequence, stronger than the proposed
limsup bound. Let Q_epsilon(T) be the original normalized occupation
integral. Generalized Ito at a bounded stopping time rho gives

    E Q_epsilon(rho)=E L_rho-e_rho,  0<=e_rho<=epsilon/2.

Before tau_a, M>a. Hence for every finite T,

    (1/(2epsilon)) E integral_0^T
      1_{|D|<epsilon, M<=a} A ds <=2b+epsilon/2.

Equivalently the unnormalized integral is at most 4b*epsilon+epsilon^2.
This bound is uniform in T and therefore also holds over [0,infinity).
In particular the region M<=epsilon has occupation at most 5epsilon^2.
It cannot carry the missing linear-order occupation coefficient.

An independent concave-test calculation checks the coefficient 2:
choose f'=1 up to a, taper linearly to zero on [a,a+eta], and f'=0
afterward. Ito for f(M) has both drift terms nonpositive and gives
E integral 1_{M<=a}dL<=2 min(m,a+eta/2). Let eta decrease to zero.
No weighted occupation convergence theorem is needed: positivity bounds
the low-mass occupation directly by the occupation after tau_a.

Next: write the full proof, check endpoint/stopping-time details, and
create a small independent exact-algebra audit. No spatial uniqueness
estimate above a positive mass floor has been obtained.

## 5. Proof, independent checks, and first audit

Saved PROOF.md, REPORT.md and audit.py. Read PROOF.md and REPORT.md back
in full. The proof includes the exact stopped balance, lifetime budget,
finite-width low-mass estimate, equivalent remaining condition above a
positive mass floor, and approximation of the previous tail coefficient
within 4a by local time before tau_a.

Checks:

- The event {tau_a<=T} really belongs to F_{T wedge tau_a}; thus the
  event-weighted optional-sampling identity is valid. Every stopping
  time used for optional sampling is bounded by a deterministic horizon.
- The lifetime limit uses monotone convergence of L_T-L_{T wedge tau_a}
  and then of the nonnegative occupation integral. No unbounded
  optional-sampling theorem is invoked.
- A bounded concave cutoff of M rederives the 2a bound on low-mass
  local time without the entrance-time argument.
- Independent scalar Feller masses started at a give E L_infinity=2a,
  checking factor 2 and attaining the budget in the broader scalar class.
  The identical scalar coupling instead gives zero; the terminal
  expectation in the exact stopped balance cannot be discarded.
- The finite-width error is checked by integrating Tanaka over levels,
  not by repeating the generalized-Ito differentiation.
- Additional edge case: after one mass becomes zero there is no more
  local time, but finite-width occupation can still increase. A separate
  Feller potential g(x)=2epsilon*x-x^2 below epsilon and epsilon^2 above
  solves (x/2)g''=-x*1_{0<x<epsilon}. It gives exact occupation epsilon^2
  for initial surviving mass at least epsilon. This checks why the
  epsilon^2 remainder cannot simply be dropped on extinction grounds.
- Mass zero, a>=m, ties, time endpoints, and the distinction between
  positive total mass and positive density at each spatial point are
  explicitly treated. No spatial comparison estimate has been assumed.

Initial command:

    OMP_NUM_THREADS=1 nice -n 15 python3 audit.py

Exit code 0, under one second. Output before adding the separate
after-extinction potential check:

    nice: setpriority: Operation not permitted
    OMP_NUM_THREADS=1; inherited nice= 20
    Occupation normalization and epsilon/2 error: 243 exact cases
    Mass covariance and min-bracket algebra: 81 exact cases
    Minimum compensator: factor 2 checked independently
    Independent concave cutoff and signs: 366 exact cases
    Post-entrance finite-width constant: 81 exact cases
    Independent scalar T=10: E L_T in [1.947001958, 2.500000000]
    Independent scalar T=1000: E L_T in [2.493757806, 2.500000000]
    Independent scalar T=1e+06: E L_T in [2.499993750, 2.500000000]
    Scalar budget target: 2a=2.5; attained in the broader mass class
    Identical scalar: E L_T=0 and E M_T=a for every finite T
    Documents: balanced delimiters, unique labels 1..22, partial verdict
    All checks passed; the stochastic proof is in PROOF.md.

The script uses exact rational arithmetic apart from the scalar
large-time exponential checks. The latter are sandwich bounds, not an
SPDE simulation. A subsequent audit run is required for the newly added
potential check. No heavy computation or third-party library is used.

## 6. Final audit and handoff

Reran the command after adding the independent extinction-boundary check:

    OMP_NUM_THREADS=1 nice -n 15 python3 audit.py

Exit code 0, under one second. The output is the same as above, with
this additional successful line after the finite-width constant check:

    After-extinction Feller occupation potential: 183 exact cases

It again ends:

    Documents: balanced delimiters, unique labels 1..22, partial verdict
    All checks passed; the stochastic proof is in PROOF.md.

Final analytic readback found no gap in the stated partial result.
Load-bearing constants have separate checks: 2 from the concave
minimum test and independent scalar masses, epsilon/2 from averaged
Tanaka, epsilon^2 from the explicit Feller occupation potential, and
5epsilon^2 by exact substitution a=epsilon. The stopping identity,
rather than an assumed weighted occupation limit, handles the random
mass cutoff.

Deliverables: PROOF.md, REPORT.md, LOG.md, audit.py. The verdict is
PARTIAL. The earlier result holds; the new piece removes low total
masses from the remaining spatial occupation estimate with a uniform
quantitative error. Pathwise uniqueness itself remains unresolved.
The next worker should use spatial information to prove the stopped
estimate before tau_a, or the estimate on min(U,V)>a, at each positive
mass floor. Total-mass positivity does not remove spatial zeros.

Task completed for this session: “take the NEXT checkable step on this
problem, building on that work.” — 15 November 2026, 09:16 Asia/Tbilisi
session start.
