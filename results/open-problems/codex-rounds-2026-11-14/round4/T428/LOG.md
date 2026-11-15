# T428 work log

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, approximately 06:41 +04 (Asia/Tbilisi; first local clock).

## Orientation and bounded literature check

Read REPORT.md, LOG.md, PROOF.md and verify.py in both prior folders:
~/codex_op_1114/briefs/T428 and
~/codex_op_1114r3/briefs/T428. Neither folder was edited.
Inspection used pwd, rg --files, cat and wc -l. Read startup MEMORY.md
and compute_state.json: warn, owner_away_open, CPU saturated, 65% free RAM.
The current folder-only rule overrides external brain/checklist/mesh writes;
no such writes, git, subagents or external messages are used.

Web-tool check, under five minutes, opened the abstract and v1 HTML of
Hindy Drillick, Jonathan Hou and Shalin Parekh, *A universality result for
the critical 2d stochastic heat flow*, https://arxiv.org/abs/2609.15832
and https://arxiv.org/html/2609.15832v1. The current abstract still lists
only v1; the HTML explicitly retains Conjecture 1.17. Queries were
`"2609.15832" "conjecture" signed`,
`"Drillick" "Hou" "Parekh" "exponentially"`,
`"Conjecture 1.17" "heat" signed resolution`, and
`"2609.15832" signed kernels proof November 2026`.
No later resolution was found. This is a bounded search, not an exhaustive
claim about the literature. Only the opened primary paper is cited.

## Independent re-derivation of the earlier result

The previous operator transform theorem holds on re-derivation. Write
mu=m/(4 pi), ell(h)=integral v h, P=u tensor v/m, and K for the weighted
logarithmic kernel. The heat integral has expansion
J_N(z)=L mu P+K+mu(-gamma-log z)P+O_K(N^-1/2).
The sharp eigenvalue is Lambda_N=mu+I_f/(m L)+O(L^-2).
Since P K P=(I_f/m)P, expanding alpha_N using the given tuning yields
B_N=P+L^-1[K/mu+(theta+epsilon_N-I_f/(m mu)-gamma-log z)P]+O(L^-2).
Relative to range(P) plus ker(P), the scalar Schur complement of I-B_N
is (log z+gamma-theta-epsilon_N)/L+O(L^-2): each off-diagonal block is
O(L^-1), so its product contributes only O(L^-2). The inverse divided
by L therefore converges to P/(log z+gamma-theta). This directly checks
the earlier spectral-projection calculation, keeping the nonorthogonal P.

Independently check the actual transform domain: H_N=Delta+alpha_N f is
self-adjoint. For q=b/N, b>exp(theta-gamma), the nonzero spectrum of
alpha_N(q-Delta)^(-1/2) f (q-Delta)^(-1/2) equals that of B_N(b).
Its top is 1-(log b+gamma-theta)/L+o(L^-1)<1. The quadratic-form
factorization of q-H_N then gives sup spectrum(N H_N)<b for large N.
Duhamel's series gives R_N(t)=alpha_N M_u exp(t H_N) M_v.
Thus its Laplace transform is the resolvent asserted by the previous
worker, with exactly N/L after rescaling time. No error found.

## Chosen extension, before writing the proof

Prove locally uniform operator-norm convergence of N R_N(Nt)/L for t>0
in the same fixed real Brownian-profile, positive-mass case, with unchanged
sharp-time Lambda_N. This is one time-resolved pair theorem, stronger
than the previous compact-set Laplace convergence.

Reason: choose the unitary sign multiplier J equal to sgn(f) on f!=0
and 1 on f=0. The signed operator F_N(t)=N R_N(Nt)/L satisfies
F_N(t)J=(N alpha_N/L) M_u exp(t N H_N) M_u, a positive operator.
For b>exp(theta-gamma), e^-bt F_N(t)J decreases in operator order.
Weighted Laplace convergence can first give norm convergence against
continuous time tests by polynomial approximation. Monotonicity can
then squeeze each positive time between neighboring time averages.
This mechanism uses Hilbert-space positivity after removing the endpoint
sign, not nonnegativity of f. It does not require a vertical-line bound.
The candidate scalar density is
g_theta(t)=integral_0^infinity exp((theta-gamma)s) t^(s-1)/Gamma(s) ds.
Its Laplace transform is exactly 1/(log z+gamma-theta).

Planned audit: prove the time-test approximation and order squeeze in full;
derive g_theta independently from the pole and logarithmic branch cut;
check both scalar formulas numerically, including nonzero theta and small
positive times. All computations will be scalar, one thread, nice>=15,
under 1 GB and a short CPU cap.

## Time-resolved proof written

Wrote PROOF.md with a full re-derivation of the prior real-axis transform
input, then the new argument. Set S_N=F_N J and A=PJ=u tensor u/m.
For any fixed b>z_*, exp(-bt)S_N(t) is positive and decreasing in
operator order, by sup spectrum(NH_N)<b. The weighted total masses
converge in norm at z=b, and polynomial tests in exp(-t) converge by
the transform at b+k. Positivity bounds the uniform test approximation
error by the norm of the total mass; it does NOT assert a bound on
the integral of operator norms. Polynomial approximation therefore
gives convergence for continuous time tests.

For a fixed positive time, use continuous nonnegative bumps of integral
one just before and after it. Operator monotonicity places D_N(t)
between the two averages; norm convergence of those averages and
continuity of the limit squeeze D_N(t) in operator norm. A finite
partition gives local uniformity for t in [delta,T]. Right multiplication
by the unitary J recovers the signed limit g_theta P.

The proof also derives the independent pole/branch formula
g_theta(t)=z_* exp(z_*t)+integral_0^infinity
exp(-rt)/[(log(r/z_*))^2+pi^2] dr.
A keyhole residue calculation proves its transform equals
1/log(z/z_*). The sign of the pole term and the factor z_* have
been rechecked algebraically. Numerical checks are next.

## Scalar verification passed

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify.py
```

Exit 0. The complete stdout is verification.json. At 40-digit precision:

- Independently transformed rational heat-overlap quadrature gives
  4 pi I_f=0.92871325187271221849482034039922=log(81/32), error 0
  at working precision.
- Three compactified time-integral checks of -gamma-log z, at
  z=0.6,1,2.5, have maximum error 5.74e-42.
- Twelve independent density checks, comparing the gamma integral and
  pole-plus-branch integral at theta=-1,0,0.7 and t=0.01,0.2,1,3,
  have maximum absolute error 1.47e-39. For theta=0,t=1 both give
  1.074623622260269496948050896288.
- Three branch-transform checks at z/z_*=1.2,2,5 agree with
  1/log(z/z_*) to at most 9.19e-41. At ratio 2 the pole contributes
  1 and the branch contributes 0.44269504088896340735992468100189;
  this checks that dropping the pole would give an incorrect limit.
- Two independent scaling checks agree to at most 4.60e-41.
- For each theta, exp(-2 z_* t)g_theta(t) decreased across all four
  sampled times, as the exact positive representation requires.

All equality assertions use tolerance 1e-28. Wall time 0.645 seconds;
peak RSS 25,706,496 bytes; all four numerical thread variables were 1;
CPU limit 120 seconds. The nice wrapper printed `setpriority: Operation
not permitted`, but direct libc getpriority returned inherited nice 20,
errno 0. The requested low priority was already satisfied. No numerical
assertion failed. These are scalar normalization checks, not a numerical
proof of convergence of operators or stochastic flows.

## Adversarial audit

Re-derived the time reconstruction using quadratic forms instead of
operator-measure notation. For any unit h, the scalar measures
<h,D_N(t)h>dt are positive. The uniform polynomial approximation error
is bounded by eta sup_N||integral D_N||, independently of h. Thus the
continuous-test convergence is uniform over unit vectors and is norm
convergence of self-adjoint operators, rather than merely weak operator
convergence. The inequalities from before/after averages hold for every
h with the same error. Taking the supremum gives the claimed norm
convergence. This independently checks the load-bearing strengthening
from scalar/time-weak convergence to norm/time-pointwise convergence.

Checked order directly by spectral calculus, not by differentiating an
unbounded generator: exp(t(NH_N-b)) is decreasing because every spectral
value is negative. Sandwiched with M_u and multiplied by N alpha_N/L>0,
it stays decreasing. Commutation of M_u with H_N is neither true nor
needed. S_N(t) is positive as a Hilbert-space operator, irrespective of
the pointwise sign of its integral kernel or of f.

Re-derived the constants by two representations: the gamma integral
gives the transform via Tonelli, while the keyhole calculation gives
the pole residue z_* and the branch density without a 1/pi factor.
The jump is 2 pi i/[(log(r/z_*))^2+pi^2]; division by 2 pi i fixes
the branch coefficient. Both the contour orientation and pole sign
agree with the scalar numerical checks. The old tuning correction
eta=I_f/(m mu) cancels in the eigenvalue expansion, so no extra mass
or gamma factor enters F_N=N R_N(Nt)/L.

The sign multiplier uses j=1, not 0, on {f=0}; otherwise it would not
be unitary. With this convention PJ=u tensor u/m and AJ=P hold on
all of H. The weighted and unweighted sharp-time eigenvalues agree by
the XY/YX identity; this was added explicitly to PROOF.md.

Cases that would break overextensions:

- Compact-set Laplace convergence alone cannot imply the time result.
  Adding a small compactly supported oscillation h(t)sin(nt) to a
  positive scalar density preserves its transform limit but destroys
  pointwise convergence. The decreasing semigroup sandwich is the
  additional structure used here.
- A uniform bound on the norm of a positive operator-valued measure's
  total mass does not bound the integral of its operator norms. The
  proof uses only order bounds on real test integrals and never makes
  that substitution.
- At t=0, F_N(0)=(N alpha_N/L)M_f, whose norm grows on the order of
  N/L^2 for nonzero f. The theorem excludes t=0 and times depending on N.
- At m=0 the rank-one limiting operator is nilpotent, so the earlier
  spectral argument does not apply. At negative m, A would not be
  positive. Both cases are outside the theorem.
- A nonsymmetric gap generator need not give a self-adjoint H_N.
  The order argument does not cover the general gap processes in
  the conjecture, and fixed-profile constants do not prove uniformity
  for arbitrary N-dependent profiles.
- Higher-particle interactions and diffusive spatial endpoints remain
  untreated. The pair result does not identify the first four moments
  needed for the stochastic-flow universality theorem.

No defect in the earlier theorem or the stated new theorem was found.
No rate is claimed. No vertical-line estimate was attempted: semigroup
order supplies the requested positive-time limit in this special case.

## Final artifact check

Wrote REPORT.md with the required first-line PARTIAL verdict and a
concrete next task: uniformity for N-dependent Brownian profiles with
a common exponential envelope and masses bounded below.

Ran a short read-only check with the same four one-thread environment
variables and `nice -n 15 python3 -B -` (inline standard-library script).
It checked five nonempty artifacts, the exact report verdict, JSON
parsing, all saved equality errors below 1e-28, priority>=15, peak RSS
below 1 GB, and verify.py syntax by compile() without creating bytecode.
Output: `Artifact checks passed; numerical computation was not repeated.`
Exit 0. The numerical proof was not rerun after documentation edits.

The final proof audit rechecked that the semigroup is positive in the
Hilbert-space quadratic-form sense; pointwise nonnegativity of f is
not being smuggled back in. Every new file is in this folder, and both
earlier folders remain read-only. The full conjecture remains unproved.
