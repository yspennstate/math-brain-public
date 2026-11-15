# T225 round 5 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Date: 15 November 2026, Asia/Tbilisi; first shell clock approximately 08:44.

## Setup and bounded literature update

Read the reports, proofs and logs in the original, round 3 and round 4
folders, plus round 4's audit. `rg --files` found no scripts in those
folders. They are read only. Read the brain navigation index, startup
memory, and compute governor state. The task's explicit folder-only rule
supersedes shared mesh/checklist/brain writes, including recall commands
that log outside this folder. No git or subagents.

Shell reads use `OMP_NUM_THREADS=1 nice -n 15`. The sandbox reports
`nice: setpriority: Operation not permitted`; no simulation or heavy
program will run with unverified priority. Governor status is warn
(cpu_saturated), mode owner_away_open. This session is analytic.

Web searches (within the first five minutes):
- `mean field Langevin polynomial convergence low temperature two layer neural networks 2025 2026 single index`
- `mean field Langevin dynamics exponential lower bound realizable regression Gaussian inputs 2026`

Opened arXiv abstract pages for 2408.07254, 2606.31429 and 2505.02621,
and full HTML of 2408.07254v2 and 2606.31429v2. The multi-index paper
distinguishes Euclidean exponential guarantees from polynomial results
under additional positive-curvature manifold assumptions; the geometry
paper studies spherical stationary distributions; the mirror paper
changes the dynamics/domain and assumes a uniform LSI. No whole-problem
solution found. OpenReview PDF request returned a browser verification
page, so it supplies no evidence. Literature search now ends. Exact
authors and links will be recorded in LITERATURE.md.

## Independent recheck and selected extension (before deriving it)

Rechecking the last result: Gaussian completion gives the w-marginal
`Z^-1 exp(G_eta(w)^2/(2 lambda^2)) gamma(dw)`. A cutoff across its
positive root has energy at most `C exp(delta^2/(2 lambda^2))/Z` and
variance at least `c exp(((A-delta)^2+(B-delta)^2)/(2 lambda^2))/Z^2`.
Since `Z <= exp(max(A^2,B^2)/(2 lambda^2))`, the quotient exponent is
`-min(A^2,B^2)/2` after delta goes to zero. Thus the main exponential
restricted-gap obstruction holds. The rare well's mass cannot be
discarded from the variance. A second derivation of the residual and
unique zero will be included in the audit.

Chosen extension: compute the exact initial residual derivative for the
actual nonlinear MFLD, including hidden-weight motion, and determine the
sign of its far-frequency tail. Then establish what this implies at
positive times using only a justified differentiability statement. This
is the concrete next step named by round 4. Do not infer a persistent
tail, an exponential risk-time bound, or interchange time and frequency
limits without proving the required control.

## Exact derivative and the first limitation

Derived, with `H(x)=exp(-(1+x^2)/4) sin(x/2)/sqrt(2)`,

`U(x)=dot f_0(x)=(1+x^2)H(x)+x H'(x)`.

The two summands before integration by parts are
`E[g(W)sin(Wx)]` and `x E[g'(W)cos(Wx)]`. The Gaussian OU terms have
zero expectation initially. Thus the derivative is independent of the
initial temperature. For `h(w)=exp(-(1+w^2)/3)sinh(w/3)/sqrt(3)`,

`D(w):=E[U(X)sin(wX)]=-2h''(w)-w h'(w)`

`=exp(-(1+w^2)/3)[(10-2w^2)sinh(w/3)+5w cosh(w/3)]/(9sqrt(3))`.

Hence `dot G_0=-D`. Unlike the shear correction h, D is negative in the
far positive tail. Its sign is controlled by the strictly decreasing
function `(10-2w^2+5w coth(w/3))/9`, which has one zero in (3,5).
The true initial residual derivative is therefore positive beyond that
zero. This does not by itself prove a far-tail sign at any positive time.

Additional local control within the same chosen piece: prove a uniform
absolute Taylor bound `|G_t-g+tD| <= C_T t^2 min(|w|,1)` for constant
temperatures in (0,1], assuming a local MFLD energy solution. A generator
calculation and a fourth-moment bound suffice. Together with the global
bound `D(w)/g(w) <= 25e/(9sqrt(3))` on w>0, this will imply positivity
of the actual residual on an interval growing as `2sqrt(log(1/t))`,
up to an additive constant inside the square root. It will not control
the entire tail.

## Proof saved

Saved PROOF.md with the exact derivative, its unique sign crossing,
the globally positive tangent residual, and a positive-time positivity
window. The solution class is explicit: a W2-continuous local weak
MFLD solution with locally bounded fourth moments and nonincreasing
free energy, initialized at pi. No unbounded-network existence theorem
is claimed. For constant lambda in (0,1], the energy inequality gives
`||sin-f_t||_2<1`; the generator gives
`E(1+A_t^2+V_t^2)^2 <= 13 exp(20T) = M_T`.

The second-generator calculation bounds
`|ddot G_t(w)| <= 14976 M_T^2 min(|w|,1)`.
Taking `C_T=15000 M_T^2` therefore safely bounds the Taylor remainder
by `C_T t^2 min(|w|,1)`. Together with the tangent bound, this proves
`G_t(w)>=g(w)/4` for `0<w<=L(t)` where
`L(t)^2=4 log(1/t)-1-2 log(4C_T)>0`, for sufficiently small t.
The initial risk slope is exactly
`-(13 exp(-1/3)-3 exp(-1))/(18sqrt(3))`.

No numerical program has been run. An independent check is now being
written using the initial Fokker--Planck density derivative and Gaussian
moment-generating-function derivatives, rather than the input-space
calculation used in PROOF.md.

## Independent audit completed

Saved AUDIT.md and LITERATURE.md. The independent initial density
derivative is `dot rho_0 = a [g(v)+v g'(v)-g''(v)] pi`. Direct
two-kernel integration with the Gaussian MGF and its first two
derivatives recovers exactly the coefficients 10, -2 and 5 in D.
The independent risk-dissipation check gives
`-dot R_0 = E g(V)^2 + E g'(V)^2`, with
`E g'(V)^2=(2exp(-1/3)+3exp(-1))/(9sqrt(3))`, agreeing with D(1).

Rechecked the positivity constant without the monotonicity proof for
h/g: its exponential upper bound on [0,5] is at most e/sqrt(3).
Rechecked the fourth moment using scalar Ito calculus and expanded the
second generator by a different product-rule grouping. All constants
352, 320, 608, 11520, 3456, 14976 and the Taylor factor 1/2 agree.
The earlier shear obstruction also survives an independent exact-capacity
calculation, including the rare well's variance factor.

The attempt to deduce a globally positive true residual fails: the
Taylor bound is absolute and cannot be divided uniformly by g(w) in
the far tails. The result controls an expanding finite interval, not
the entire half-line. A remote or later negative lobe remains possible.
No runtime bound or proximal gap along the true trajectory is claimed.

## Final report and readback — 08:57 Asia/Tbilisi

Saved REPORT.md with the required verdict prefix and the next-worker
handoff. Added an explicit W2-coupling bound to justify input continuity
in PROOF.md. Read the proof, report and audit back; no mathematical
correction was needed. The first-order tail sign is carefully separated
from the unproved whole-tail positive-time sign.

Final readback commands:

```sh
OMP_NUM_THREADS=1 nice -n 15 wc -l PROOF.md AUDIT.md LOG.md LITERATURE.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '1,250p' PROOF.md
OMP_NUM_THREADS=1 nice -n 15 sed -n '250,500p' PROOF.md
OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md
OMP_NUM_THREADS=1 nice -n 15 cat AUDIT.md
OMP_NUM_THREADS=1 nice -n 15 sh -c 'wc -l REPORT.md PROOF.md AUDIT.md LOG.md LITERATURE.md; head -1 REPORT.md; date "+%Y-%m-%d %H:%M:%S %Z"'
```

The final inspection, before this log append, reported REPORT.md 87,
PROOF.md 479, AUDIT.md 236, LOG.md 131, and LITERATURE.md 38 lines.
The clock was `2026-11-15 08:57:36 +04`. All shell calls finished
immediately and repeated the priority warning. No numerical run,
simulation, script, git action, subagent, or mutation outside this folder
was used. The next checkable piece is complete; the general problem
is unresolved.
