# T325 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, 03:47 Asia/Tbilisi (14 November 23:47 UTC).

## 1. Orientation and source check

Read the earlier REPORT.md, LOG.md and SOLVED_ELSEWHERE.md at
`~/codex_op_1114/briefs/T325`. There is no earlier
PROOF.md and no script matching *.py, *.sh or *.ipynb. The prior deliverable
is a literature audit, not a training-convergence proof or experiment.
Read the startup memory index and compute state. State was warn,
owner_away_open, CPU saturated. No heavy workload is planned.

All writes stay here. The folder-only rule precludes shared brain, mesh and
checklist writes; those commands are not run. No git or subagents.

Read-only commands: `pwd`; `rg --files` for the earlier folder and memory
locations; `cat` of the earlier deliverables, memory index and compute-state
file; `date '+%Y-%m-%d %H:%M:%S %Z'`. Attempt to read the earlier PROOF.md
returned “No such file or directory”; script search returned no files.

Initial web queries (web search tool):

- `"transformers" "linear regression" "training convergence" "2026" multilayer`
- `"2410.08292" convergence transformer regression`
- `"in-context" "random initialization" "multi-layer" convergence regression transformer 2026`

Opened arXiv HTML 2410.08292v1 and arXiv abstract 2610.31089. The latter
still lists the October 31 revision reported by the earlier worker. No
full solution found in the first search batch. Continue only the short
literature check, then rederive the restricted looped-model loss and select
one extension. References will be cited only after opening their source.

## 2. Literature decision and independent recheck

The literature check ended within five minutes. Further query:
`transformer multilayer linear regression training convergence November 2026 random initialization theorem`.
Opened the primary arXiv pages for Zhen Qin, Jinxin Zhou, Jiachen Jiang,
Zhihui Zhu, arXiv:2506.05249 (revised April 13, 2026), and Michael Herty,
Hailiang Liu, arXiv:2608.25055. The former discusses fitting losses under
suitable initialization; the latter deep-model result is local under NTK
nondegeneracy in a mean-field limit. Neither abstract establishes the
requested in-context Bayes-risk and algorithm-identification conclusion.
No solution found; this bounded check is not proof of absence. No
SOLVED_ELSEWHERE.md is warranted in this session.

Reopened the looped paper's actual architecture, Theorems 3.3/3.4 and
Appendix A.11/A.12. The earlier comparison-ODE correction holds: for
f' <= -f^((2L-1)/L)/16, put alpha=(L-1)/L. Then
(f^(-alpha))' >= alpha/16, so
f(t) <= [f(0)^(-alpha)+alpha*t/16]^(-1/alpha) until the loss floor.
Differentiating this expression gives precisely the negative ODE.
The source instead prints a positive comparison ODE and a different
prefactor. This verifies the earlier algebraic audit, conditional on its
gradient inequality, without certifying that inequality or its domain.

The architecture itself gives the stronger starting point: with fixed
P=diag(0,...,0,1), Q_l=diag(A_l,0), and u_l=0, each layer updates
Z <- Z - P Z M Z^T Q_l Z/n, M=diag(1,...,1,0). Top rows remain X,x_q.
For d=1, Q_l=diag(a_l,0), the label-row residual is multiplied by
1-a_l S, S=sum_i x_i^2/n. Thus two untied layers have exact population
loss F(a,b)=E[(1-a S)^2(1-b S)^2], after integrating independent w,x_q.
This rederives the earlier paper's loss identity directly from token
updates. It avoids matrix square roots and any hidden positive-definite
domain assumption. Details will be written in PROOF.md.

## 3. Chosen extension (recorded before proof)

Prove global population-gradient-flow convergence for these TWO UNTIED
SCALAR preconditioners, from every initialization a != b, at each finite
integer n >= 1. All other attention blocks remain prescribed and frozen.
This is the smallest exact case of the earlier report's “untying two
layers” target. It addresses training rather than expressivity, allows
independent continuously distributed random a,b of any sign, and admits
exact finite-n risk and identification of the two learned GD step sizes.
It does not cover a fully random transformer or d > 1.

Approach: use p=a+b, q=ab. F is a positive-definite quadratic in p,q;
its unconstrained optimum has two distinct real roots. Classify the only
other stationary point on a=b, prove it is a strict saddle and that no
off-diagonal trajectory approaches it. Prove bounded trajectories and
convergence, then audit formulas by exact rational arithmetic and a
separate Gaussian-moment expansion. No numerical training is needed.

## 4. Proof obtained

Wrote PROOF.md, deriving every step from the token update. The finite-n
loss has exactly two global minima and one stationary point on a=b.
The optimum has p_*=2n/(n+2), q_*=n^2/[(n+2)(n+4)], with strictly
positive discriminant 8n^2/[(n+2)^2(n+4)]. Its risk is
8/[(n+2)(n+4)]. Compact sublevel sets give global flow and convergence
to one of the three stationary points. The exact difference equation
(a-b)'=(a-b)G_q excludes convergence to the diagonal saddle whenever
a(0)!=b(0), since G_q=2 E[S^2(1-c_s S)^2]>0 at that saddle.

This also exposes a real exception: equal initialization remains on the
diagonal and converges to the saddle, not an untied global minimum.
Thus “every random initialization” requires an initialization law with
zero probability of equality; no claim is made for tied initializations.
Preparing an independent exact-arithmetic audit of the moment expansion,
normal equations, risk constant, chain-rule gradients and difference
equation, including n=1 and negative/large initial parameter values.

## 5. Independent arithmetic audit

Command (single standard-library Python process, no numerical libraries):

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_scalar.py
```

Output:

```
nice: setpriority: Operation not permitted
RLIMIT_AS unavailable: current limit exceeds maximum limit
n=1: moments agree; min risk=8/15; n^2 risk=0.533333333
n=2: moments agree; min risk=1/3; n^2 risk=1.333333333
n=3: moments agree; min risk=8/35; n^2 risk=2.057142857
n=5: moments agree; min risk=8/63; n^2 risk=3.174603175
n=10: moments agree; min risk=1/21; n^2 risk=4.761904762
n=100: moments agree; min risk=1/1326; n^2 risk=7.541478130
n=1000: moments agree; min risk=1/125751; n^2 risk=7.952223044
Exact token-update, gradient, gap and difference-equation checks passed.
Peak RSS: 13.44 MiB
```

Exit 0. Exact fractions, not floating-point estimates, determine the
reported risks and all assertions. Only the n^2-risk display uses floats.
The independent moment computation multiplies truncated generating
series using Gaussian integration-by-parts moments; it does not use the
chi-square product formula. The normal equations are then solved anew
from those moments. Direct polynomial multiplication checks the risk,
gradients, completed-square gap and difference equation. A separate
label-row update on rational tokens checks the forward-pass identity
and interchange of the two layers.

The nice wrapper reported the same priority-setting issue as the prior
session. A requested optional address-space cap was unavailable; measured
RSS was 13.44 MiB, far below 1 GiB, with no arrays or large allocations.
No heavier process was launched. A short priority-only inspection follows
to establish whether the process already inherits a lower priority.

The proof, rather than these finitely many arithmetic cases, establishes
the formulas for all integers n>=1 and convergence for all unequal pairs.

Priority inspection command:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 - <<'PY'
import os
import resource
print('Inherited process nice:', os.getpriority(os.PRIO_PROCESS, 0))
print('Address-space limits:', resource.getrlimit(resource.RLIMIT_AS))
PY
```

Output: wrapper warning as above; `Inherited process nice: 20`;
`Address-space limits: (9223372036854775807, 9223372036854775807)`.
Thus the process inherits an even lower priority than requested. Added
a nice>=15 assertion and explicit priority output to the audit script.
The hard-cap syscall is unavailable despite the reported unlimited
limit; the script reports this rather than claiming an enforced cap.

## 6. Attempts to break the result

- n=1 is allowed despite the source's standing n>d convention. The token
  update and Gaussian moments used here require only n>=1. At n=1 the
  exact optimum risk is 8/15, not zero. Bayes risk is still zero because
  the scalar weight is recovered from the first nonzero covariate.
- Negative and large a,b do not invalidate the loss formula. Coercivity,
  rather than a positive-definite initialization assumption, bounds their
  flow. Exact gradient audits included (-7,3) and (100,-100).
- The diagonal is a genuine failure case; the theorem explicitly excludes
  it and proves that it is the complete attraction set of the saddle.
  At the saddle its two Hessian eigenvalues are 6K and -2K with K>0;
  these follow independently from diagonal and antisymmetric variations.
- Swapping layers leaves the scalar predictor unchanged and exchanges
  the two minimizers. The noncrossing difference equation determines
  which ordering a trajectory selects.
- Replacing finite n by deterministic S=1 destroys the strict moment
  determinant. No interchange of training time and sample-size limits
  is made. Risk is computed after training at each finite n.
- The result does not apply to independent random key/query factors or
  to all random attention entries. Those change the gradient vector
  field. The trained coordinates here are exactly a,b in Q_a,Q_b.
- One-layer optimization independently gives 2/(n+2), so the two-layer
  risk improvement factor 4/(n+4) and limiting 8/n^2 have the correct
  scale and sign. Expanding 1-2n/(n+2)+n/(n+4) gives the same constant 8.

No simulation or empirical convergence plot is used as proof. No claim
is made that this scalar theorem is absent from all previous literature.

## 7. Final artifact audit

Wrote REPORT.md with the required exact verdict format and explicit
restrictions. Reran the audit after adding its priority assertion using
the same command in Section 5: exit 0, `Process nice: 20`, all exact
checks passed, peak RSS 13.66 MiB. The optional-cap warning remains as
recorded above. The program imports only the standard library and has
small bounded polynomial and Fraction lists; its largest loop is 1000
iterations of degree-four series multiplication.

Read back the proof's token normalization, determinant, discriminant,
saddle eigenvalues, difference-equation sign, compactness/convergence
argument and Bayes comparison. Corrected brackets in the displayed
general moment product so its denominator is unambiguous; the explicitly
listed moments and script were already correct. No load-bearing claim
relies on simulation, a numerical optimizer or an unchecked matrix
gradient inequality. Deliverables: PROOF.md, audit_scalar.py, LOG.md,
REPORT.md. The full T325 problem remains unresolved here.
