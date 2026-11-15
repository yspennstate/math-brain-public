# T133 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, 04:56 Asia/Tbilisi (UTC+4).

## 04:56–04:58: reading and bounded literature update

Read REPORT.md and LOG.md in the original session directory; its directory
listing confirms no PROOF.md or scripts were left. Read the round 3
REPORT.md, LOG.md, PROOF.md and complete verify_local.py. Both directories
are read-only for this task. All writes stay in the present directory;
therefore the global mesh, checklist and brain commands that write outside
it are not run. No git or subagents.

Read the compute governor directly: warn, owner_away_open, CPU saturated.
Only short single-thread computations under nice are planned.

Web queries, completed within two minutes:

- `"2609.20576" "limit shape"`
- `six vertex domain wall arctic curve proof Bufetov 2026`
- `"Bufetov" "limit shape" "domain-wall" proof November 2026`
- `"arctic curve" "1/2" "2026" proof`

Opened https://arxiv.org/abs/2609.20576 and
https://arxiv.org/html/2609.20576v1. Alexey Bufetov's note still has only
v1 (17 September 2026) in its submission history. Its abstract says
announcement, Theorem 3.2 covers -1 < Delta <= 1/2, and Remark 3.3
explicitly omits 1/2 < Delta < 1. No later complete proof was found in
this bounded search. The original literature finding holds, with its
announcement caveat. No new solved-elsewhere result triggers the stop rule.

Next action: independently rederive the round 3 quadratic branch constants
from endpoint differentiation and an even-density moment expansion, and
check them numerically without executing a script that writes in round 3.

## 05:00: independent recheck passed

Re-derived the constants using Phi = M0 F0 + M2 F2/2 + O(B^5).
The even resolvent density is 1+O(B), hence M0=2B+O(B^2),
M2=2B^3/3+O(B^4). Thus M2'/(2 M0')=B^2/2+O(B^3)
and M2/(2 M0)=B^2/6+O(B^3). Since F2=-F0_theta_theta,
the coefficient equations are a x2+b y2=C/2 and
a' x2+b' y2=D/6, as in round 3. Kernel mass also follows
independently by t=exp(z), reducing the full-line integral to
an elementary quadratic denominator; it is 1-2 gamma/pi.

Wrote recheck.py from scratch: scalar Neumann iteration and composite
two-point Gauss quadrature, with finite differences of the scalar integral.
It neither imports nor executes round 3 code. Initial midpoint quadrature
failed the residual-reduction assertion at free fermions: its integration
error obscured the smaller residual. Changed to fourth-order quadrature.

Command:
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 recheck.py`

Output after correction:
```
gamma=0.4 C=0.01188993176 W=0.002523913607 residuals=[(3.0928e-09,8.6155e-15),(3.8422e-10,3.0903e-15)]
gamma=1.5707963 C=0.1591549431 W=0.1013211836 residuals=[(2.6818e-10,0),(1.6169e-11,0)]
gamma=2.4 C=0.8698445976 W=0.428988478 residuals=[(-9.4735e-08,-6.9758e-11),(-1.2372e-08,-2.4597e-12)]
PASS exact free-fermion base and quadratic coefficient
elapsed_seconds 0.0878 peak_rss 18710528 nice 20
```
The shell's priority warning reflects inherited nice 20, confirmed inside
Python. The earlier analytic claim holds on this independent recheck.

## Choice of extension, before doing it

Resolve the sign of C and the side of quadratic continuation, first on a
rigorously tractable subset of the omitted interval 0 < gamma < pi/3.
The intended target is symmetric weights u=T=delta/2, at theta=0, and
then an open neighborhood by continuity. This is one local geometry
extension of round 3, not a proof of model convergence. If a general
positive representation emerges, extend the same sign argument along
the whole arc; numerical positivity alone will not be called a proof.

## 05:04: sign decomposition extends the chosen weight range

At theta=0, symmetry gives x0=y0=e/(2a), D=0 and
C=e(a''/a)-e''. Put h=pi/delta, z=T/2, R=a''/a,
q=1/(1-cos T), qh=1/(1-cos(hT)), and
E=cot(z)-h cot(hz). Direct differentiation yields

`2 pi C = E (R-q) + h cot(hz) (h^2 qh-q)`.

Both E and h^2 qh-q are strictly positive: t cot(t) and sin(t)/t
are strictly decreasing on (0,pi/2). Moreover, setting
v=(gamma+u)/2 and w=(gamma-u)/2 gives
`R-q = (tan(w)/2)(tan(w)-tan(v)) >= 0` whenever u>=gamma.
Thus C>0 at theta=0 for every 0<gamma<pi/2 and
gamma<=u<pi-gamma. In particular this contains symmetric weights
u=delta/2 for the entire omitted interval 0<gamma<pi/3.
This is a weight-range extension of the chosen midpoint argument,
not a claim that its sign has been proved along the full arc.

The quadratic coefficient is x2=y2=C/(4a)>0. To establish what
"inward" means without a probabilistic assumption, differentiate the
envelope: its tangent at the midpoint is (C/(2p),-C/(2p)), where
p=b'>0, and its normal second derivative has positive northeast
component. Next: write this as a local strictly convex graph and prove
the continuation gives a one-sided coordinate neighborhood there.

## 05:04: proof and adversarial checks completed

Wrote PROOF.md with an explicit positive lower bound for C(0).
The proof applies to 0<gamma<pi/2, gamma<=u<pi-gamma. It thus
includes all equal-weight midpoints in the omitted interval, plus
unequal weights in the stated range. Continuity gives a theta interval,
but no quantitative or full-arc interval is claimed.

The local convex-side conclusion follows from differentiating the
envelope equations, not a presumed physical liquid phase. In coordinates
r=(x-y)/sqrt(2), s=(x+y)/sqrt(2), the envelope is s=f(r) with
f''(0)=sqrt(2) p^2/(alpha C)>0. The midpoint displacement is
C/(4 alpha)*(1,1) B^2+O(B^3). The Jacobian after setting t=B^2 is
det[V,X0']=-C^2/(2W)<0. The t>=0 parametrization extends C1 across
zero by its tangent expression for t<0, so the ordinary inverse
function theorem gives a one-sided collar and local uniqueness of
small-B critical parameters. This does not exclude distant critical
parameters for the same spatial point.

Wrote verify_geometry.py. It compares C from high-precision numerical
derivatives of the original coefficients against the trigonometric
decomposition, and checks graph derivatives by differentiating the
closed envelope formula rather than its defining linear equations.
It includes u=gamma, near u=delta, gamma near zero and near pi/2,
and four equal-weight examples. The finite-B tests use the independent
scalar integral from recheck.py, solve the midpoint critical equation
by finite differences, and compare the observed displacement to C/(4a).

First run at 70 digits failed an excessively tight identity check
near gamma=pi/2-.001, u=1.5717763268 (T approximately 2e-5).
Relative error was about 2.7e-52 after cancellation, above the requested
1e-55 threshold. Increased working precision to 100 digits; did not
relax the assertion. This is cancellation in separate pole terms,
not a discrepancy in the identity.

Command:
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_geometry.py

Final output:
~~~
PASS sign/decomposition/graph checks: 40
max relative decomposition error: 5.976884647703294e-83
branch gamma=0.4 u=0.4 predicted_B2=0.03252821982481117
  observed_B2=[0.03236470259793123,0.03244657566847664]
  extrapolation_error=2.2891421088550024e-07
branch gamma=0.4 u=1.3707963267948966 predicted_B2=0.07928211562661473
  observed_B2=[0.07888520206389416,0.07908340510065504]
  extrapolation_error=5.07489198817157e-07
branch gamma=1.2 u=1.5 predicted_B2=0.14557276201137762
  observed_B2=[0.1454536171723378,0.1455129155630841]
  extrapolation_error=5.480575472061044e-07
outside sufficient range: -0.007874651402818459
resources: elapsed_seconds=1.4514 nice=20 peak_rss_MiB=19.3125
~~~

Full output data are in geometry_checks.json. The shell again warns that
it cannot change the inherited nice 20 to 15; Python confirms priority 20.
All numerical workloads use one thread and remain far below 1 GB.

Attempt to break the sufficient condition: for gamma=.4,u=.1,
R-q=-.0078746514. Thus the first summand in the sign decomposition
really becomes negative outside u>=gamma; dropping that restriction
would invalidate this proof. No counterexample to C>0 is asserted.
The u=gamma edge is explicitly tested: the first summand is zero,
while the second is strictly positive.

Second derivations of load-bearing factors: the graph curvature uses
direct derivatives of the closed envelope; the 1/4 in the displacement
is checked by finite-interval integration; the Jacobian follows both
from det[V,(C/W)(b,-a)] and, at the midpoint, directly from
V=C/(4alpha)(1,1), X0'=C/(2p)(1,-1), W=2alpha p.
The inverse-function argument uses t=B^2, since the Jacobian in
(B,theta) vanishes at B=0. For B>0 it is
-B C^2/W+O(B^2), consistent with the same calculation.

A combined write command had a JavaScript quoting error before execution
and changed no files; split the writes and repeated them successfully.

## Final file audit

REPORT.md has the required first-line verdict, the parameter range,
the new result, commands, limitations, failures and next target. Checked
both scripts with ast.parse, the JSON counts (40 sign cases, 3 branch
cases), and Markdown files for control characters: all passed. Added
the explicit exp-substitution kernel-mass calculation and derived the
concavity reformulation quoted in the report. An intermediate patch
failed to match context and changed nothing; applied it with exact context.
No earlier files or files outside this folder were edited.
