# T064 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session launch: 15 November 2026, about 10:20 Asia/Tbilisi, from run.pid.
The exact message-receipt time was not recorded.

## Orientation and literature check

Read the startup memory and compute state (`warn`, `owner_away_open`,
CPU saturated). The explicit folder-only rule overrides global requests
to write the brain, mesh, and checklist. Those stores are untouched.
No git, subagents, background jobs, or external writes are used.
Initial lightweight read commands omitted the nice/thread prefix; later
commands use it. macOS prints `nice: setpriority: Operation not permitted`;
numerical scripts must verify actual inherited niceness before computing.

Read the original and rounds 3–5 REPORT.md and LOG.md files, existing
PROOF.md files and scripts. Some combined reads were truncated and are
being recovered in bounded reads. The original folder has no PROOF.md
or scripts. All preceding folders remain read-only.

Literature search completed in less than five minutes. Queries:

- `random plane wave percolation Cardy SLE 2025 2026 nodal lines`
- `random plane wave four arm saddle Palm percolation 2025 2026`
- `"random plane wave" "2026" percolation`
- `"random plane wave" "2025" crossing probabilities`

Opened https://arxiv.org/abs/2207.13448 and
https://arxiv.org/abs/2010.11770. No solution of the requested scaling
limit was found. The latter paper's noncritical phase transition is
already accounted for by the original report. Search hits concerning
square-lattice random-cluster interfaces do not resolve random waves.
This bounded search is not an exhaustive absence claim.

## Initial algebraic re-check

In the first-jet conditioned Fourier expansion, U=(a2^2+b2^2)/2 is
exponential with mean one and det Hess=(t^2-U)/4. The saddle-weighted
normalizer is exp(-t^2)/4. Changing variables g=u-t^2 gives density
g exp(-g), proving U=t^2+Gamma(2,1). Its angle and all higher modes
remain independent. The old saddle intensity is therefore
phi(t) exp(-t^2)/(4 pi), as reported. For translated gamma densities
the unique crossing solves v exp(-a)=v-a, giving c=a/(1-exp(-a));
integrating to c reproduces the stated total variation formula.
No error found. Independent numerical and further proof audits follow.

## Re-run of round 5

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/T064/check_saddle_palm.py
```

Exit 0. Actual niceness 20, one thread, CPU cap 60 s. Original tilt
moment error 3.205e-08; TV quadrature error 1.233e-10; Fourier/spectral
covariance error 1.110e-16; all circle, eigenvalue and near-flat-saddle
checks passed. PASS, elapsed 0.055 s, peak RSS 13.83 MiB. The earlier
result holds. The field-law calculation above re-derives its constants
without depending on this re-run.

## Chosen extension, recorded before deriving it

Quantify finite-annulus stability of alternating arms at the saddle's
own height. Write w(r)=1-J0(r)>0 and divide the zero-height Palm field
by w. Then radial-level arms become constant-level arms of Y=F0/w.
Apply a stratified critical-value count on the annulus to Y, retaining
the determinant tilt through its exact Radon–Nikodym density U relative
to the Gaussian first-jet-conditioned field. Derive computable weighted
Kac–Rice densities, including both circular boundary components, and
their large-radius limits. Combine with round 5's exact residual TV
to bound the actual own-height arm probability, rather than only a
residual-field event.

This is the finite-scale radial-threshold stability step named in the
preceding report. It should retain an area-sized cost, so no larger
level window or macroscopic arm decay is expected. The audit will
independently compute the needed covariances by subtracting the three
removed modes from stationary spectral moments and by summing retained
Fourier modes. At level zero Gaussian fourth moments and folded-normal
moments give exact intensity formulas without Monte Carlo. The case of
an annulus reaching the conditioned origin must be excluded explicitly.

## Proof draft and first audit run

Created PROOF.md with the weighted critical-value identity for h/w,
the own-height arm comparison, and the O(r^(-1/2)) local-density
approximation. Created check_annular_stability.py. The first run of
the command below exited before computing: a fallback `import
ctypes.util` made `ctypes` a local variable in the guard. Changed that
fallback to `from ctypes import util`. This is a script-scoping error,
not a numerical or mathematical discrepancy.

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_annular_stability.py
```

The corrected run passed in 0.054 s with 12.95 MiB peak RSS, niceness
20. Covariance subtraction versus retained-mode sums: maximum error
3.463e-16. Wick moments versus 81-node Gaussian polynomial quadrature:
1.110e-16. Folded-normal moment versus one-dimensional quadrature:
5.528e-12. The six tested radii were 4,8,16,64,256,1024. Both limiting
constants were independently recovered: 0.031746817967 and
0.063493635934. At r=4, omitting the determinant tilt changes k2 from
0.036726646496 to 0.0378962851032. All six circle-curvature corrections
were nonzero. Full final output will be saved after the sharper audit.

## Sharpening within the same extension

The crude local O(r^(-1/2)) error has an oscillatory leading term.
The Helmholtz identity gives Delta w=J0 and w+Delta w=1. At a critical
point of h/w of value v, the numerator Hessian D2h-v D2w has trace
exactly -v, not -v w. The determinant's isotropic Gaussian expectation
has no linear response to the remaining small traceless mean shift.
Furthermore U is quadratic in (A,B), so its O(r^(-1/2)) cross-covariance
with the local jet affects expectations only at O(1/r).

This suggests k2=alpha(v)[1+(v^2-1)J0(r)]+O(1/r) and
k1=beta(v)-[beta(v)+v beta'(v)]J0(r)+O(1/r), uniformly |v|<=1.
Integrating r J0 exactly as [r J1] should reduce the error in the
annular comparison from O(|t| R^(3/2)) to O(|t| R) at fixed aspect
ratio. This sharpens the chosen stability lemma; it is not a second
independent project. Next: prove the quadratic responses and audit
the trace cancellation and oscillatory integral independently.

A failed exact-context patch immediately before this entry changed no
files. The run.pid stat command confirms session launch at 10:20:02
Asia/Tbilisi on 15 November 2026.

## Sharper proof and independent audit

PROOF.md now proves both oscillatory expansions, uniformly |v|<=1.
Regressing (A,B) on the remaining local jet shows that the conditional
expectation of U is 1+O((1+|jet|^2)/r). Thus the tilt's influence on
local moments has order 1/r, although its cross-covariance has order
r^(-1/2). The exact trace cancellation leaves only a small traceless
mean shift in the interior. Its linear response vanishes by isotropy;
bounded second derivatives of Gaussian convolution give a quadratic
error. These facts establish the proposed expansions. Integrating
their leading J0 term by [r J1] proves the sharper error bound.

The final audit uses independent covariance constructions, 81-node
Gaussian polynomial quadrature, direct folded-normal quadrature,
signed-level integrals with analytic truncated-normal moments, the
Bessel ODE and the Bessel derivative recurrence. No sampling is used.
The spectral moments are also directly checked by angular integration.
The direct circular Fourier derivative checks the sign and coefficient
of the curvature correction for modes 0,1,2 at all six radii.

Final command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_annular_stability.py
```

Output (exit 0; the shell also prints the priority-change warning):

```text
niceness=20; threads=1; CPU cap=60s
stationary free-jet spectral variances: 1.000000000000 0.500000000000 0.500000000000 0.125000000000 0.125000000000
r, k2(r,0), k1(r,0), k2/alpha(0), k1/beta(0):
4 0.036726646496 0.0832456826108 1.156860714 1.311087031
8 0.022321897993 0.0502866030009 0.703122373 0.791994383
16 0.0407830604777 0.0761933552498 1.284634590 1.200015626
64 0.0293115037759 0.0578147231384 0.923289503 0.910559339
256 0.0329408016418 0.0657908956286 1.037609554 1.036180944
1024 0.0312743627143 0.0625472962739 0.985118028 0.985095519
max low-mode-subtraction / retained-mode covariance error=3.463e-16
max Wick / tensor Gauss quadrature error=1.110e-16
max folded-normal formula / quadrature error=5.528e-12
six circle-curvature corrections detected; both covariance constructions agree
32 signed-level quadratures: max evenness error=1.388e-17; zero-level cross-check=7.939e-14
max tested r*|k2-alpha-b2*J0|=0.0457412; r*|k1-beta-b1*J0|=0.0562804
four independent Bessel-ODE trace cancellations passed
three oscillatory area integrals agree with [r*J1] endpoints
limiting densities independently recovered: 0.031746817967 0.063493635934
r=4: weighted k2=0.036726646496; incorrectly unweighted=0.0378962851032
boundary-only tangency audit: value=0, tangent derivative=0, second derivative=1, radial derivative=1
three signed quotient-Hessian determinant factors passed
PASS; elapsed=0.273s; peak RSS=13.94 MiB
```

The tested bound .1 on the scaled local remainders is only a regression
check at the listed points, not a certified constant valid for all radii.
The proof establishes existence of absolute C and R0 analytically.
No heavy process ran; allocations are small fixed matrices and short
quadrature sums, CPU cap 60 s, observed RSS below 15 MiB.

## Attempts to break the result

1. Used both low-mode subtraction and retained-mode sums for the full
   seven-dimensional covariance. They agree to 3.463e-16; their
   Cholesky decompositions and conditional covariances are positive
   definite at all tested radii. The proof only needs sufficiently
   large radii, not a numerically guessed uniform threshold.
2. Dropped U deliberately. At r=4 this changes the interior density by
   more than .001. Ordinary Gaussian conditioning cannot replace the
   saddle law, even when counting points far from the origin.
3. Dropped -h_r/r deliberately. Every tested boundary density changes.
   Independently differentiating each circular Fourier mode verifies
   the minus sign and the factor 1/r.
4. Compared positive and negative levels. Their densities agree to
   1.388e-17, as required by h -> -h and invariance of U. The
   alternating-arm event itself is not monotone, so the proof uses
   symmetric difference and isotopy, not a monotonicity assertion.
5. Checked the own-height trace in two ways: from Delta h=-h and
   Delta w=J0, or from the quotient PDE
   w Delta Y+2 grad w dot grad Y+Y=0. At a critical point of value v,
   the numerator Hessian has trace -v. Using -v w would give the wrong
   leading J0 coefficient. Independent Bessel-ODE checks passed.
6. Boundary events cannot be ignored. On 1<=r<=2,
   g(r,theta)=r-1+cos(2theta) has radial derivative one everywhere and
   no interior critical point. At t=.1, the four radial rays at angles
   0,pi/2,pi,3pi/2 witness alternating arms. At t=-.1 there is no
   negative point on the outer circle, hence no four-arm event. The
   change passes through boundary tangencies at value zero. This
   checks the need for circular boundary terms independently of any
   Gaussian calculation.
7. The division by w is invalid at r=0. The theorem assumes R>=R0>0;
   it does not claim a bound uniform down to the distinguished saddle.
8. A raw Palm-law total variation comparison is still impossible,
   as round 5's circle mean shows. The proved estimate controls a
   specified topological event after radial division, not the full law.
9. The local leading error oscillates. Bounding its absolute value
   before radial integration gives the valid but weaker R^(3/2) error.
   Independent quadrature of three integrals confirms the endpoint
   expression [r J1], reducing that error to order R at fixed aspect.

Only the first script run failed, through the fixed import scoping bug.
No numerical or mathematical audit failed. No constants were inferred
from a finite table as universal bounds. There is no arm-decay result,
larger sufficient level window, RSW estimate, or conformal limit.

## Sources and read-only predecessors

Opened the full HTML of https://arxiv.org/html/2207.13448 and
https://arxiv.org/html/2010.11770v3, and DLMF Sections 10.6 and 10.17.
The proof's source list names the authors exactly as on the opened
papers. The two papers are used for the Fourier representation and
literature baseline; the annular weighted count and its deformation
are derived explicitly in PROOF.md.

Completed bounded reads of the earlier proofs, scripts and logs to
recover truncation from the first combined reads. Also read the
round-4 REPORT.md and the original SOLVED_ELSEWHERE.md. All predecessor
folders remain unchanged. Their noncritical literature correction is
retained, and the present verdict concerns only the new annular lemma.

## Final artifact audit

Read the complete final PROOF.md and REPORT.md in bounded commands.
Rechecked the exact factors in the weighted count: value-gradient
change of variables w^3, Hessian determinant w^(-2), leaving w;
on each circle w^2 times w^(-1), also leaving w. The boundary second
derivative is h_tautau-h_r/r on both circles. The weight has mean
one before conditioning, while its conditional dependence is retained.
The trace and regression arguments independently give the leading
oscillatory coefficients. The sharper error is an upper bound with
an unspecified finite constant, not an inferred value from the audit.

The final report distinguishes the proved finite-scale arm comparison
from arm decay and the original open conjecture, includes commands,
failed import and its correction, scope limits and the next missing
input. The final numerical run preceded only prose/notation edits;
no mathematical formula or script changed afterward.

Deliverables: REPORT.md, PROOF.md, LOG.md, check_annular_stability.py.
Only this folder was written; no git, external or shared-store writes.

Task completed: “take the NEXT checkable step on this problem, building
on that work” — 15 November 2026, 10:20:02 Asia/Tbilisi (session launch).
