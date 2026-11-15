# T248 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First clock reading: 2026-11-15 05:13:02 +04 (01:13:02 UTC).

## Orientation and literature check

Read the earlier REPORT.md and LOG.md, and round 3 REPORT.md, LOG.md,
PROOF.md and verify_edge.py. The first folder has no PROOF.md or research
script. Read ~/.claude/brain_startup.md and the compute state: warn,
cpu_saturated, owner_away_open. Only small scalar computations are planned.
All writes stay here. The task-specific write restriction overrides the
global mesh/checklist/brain commands, which would write outside this folder.
No git, subagents, external mutations or background jobs.

Within the five-minute literature budget, searched the web for the exact
Chen–Lyu title, random neural network edge universality in 2026, and conjugate
kernel Tracy–Widom in November 2026. Opened the arXiv page and full v2 HTML
of Guangchen Chen and Xing Lyu, *Tracy–Widom law for sample covariance matrices
under quadratic form concentration*, arXiv:2610.41416v2 (4 November 2026),
https://arxiv.org/html/2610.41416v2 . Rechecked Assumptions 1.1–1.2,
Theorem 1.3 and Corollary 1.4 directly. Opened the arXiv page of Lucas Benigni
and Sandrine Péché, *Largest Eigenvalues of the Conjugate Kernel of
Single-Layered Neural Networks*, arXiv:2201.04753. No newer complete solution
was found. The already known Chen–Lyu theorem is not a reason to stop anew.

## Independent recheck of round 3

Re-derived its covariance estimate: for Hermite rank at least three,
|Sigma_jk| <= v |rho_jk|^3, and the spherical beta moment gives
E rho^6 = 15/[d(d+2)(d+4)]. Thus E||Sigma-vI||_F^2=O(d^-1).
Re-derived the edge perturbation by the exact rational identity, writing
t=v+delta:

    t/(1+tu)-v/(1+vu)-delta/(1+vu)^2
      = -u delta^2 / [(1+vu)^2(1+tu)].

Since Tr(Sigma-vI)=0, this bounds the edge-function displacement and its
first two u derivatives by C Tr((Sigma-vI)^2)/N whenever poles stay away.
This independently gives the prior O_p(d^-2) edge shift. The prior Gaussian
rotation argument and finite-aspect-ratio rescaling also check out against
the external theorem. No defect found. Independent scalar checks will be
recorded below; no TW simulation is intended.

## Chosen extension (recorded before execution)

Allow a nonzero second Hermite coefficient for spherical inputs, retaining
a_0=a_1=0, Lipschitz sigma, and aspect ratio away from one. Write q=a_2^2.
Prove the strictly subcritical case q (N/d) < v sqrt(N/m) with a fixed margin
in the limit. The missing quantitative lemma is an operator-norm bound for
the off-diagonal kernel rho_jk^2-1/d. Represent it as centered traceless
symmetric tensor inner products, compute its expected fourth trace exactly,
and deduce operator norm o_p(1). This isolates the population eigenvalue
v+q N/d. Exact trace cancellation should then give an O_p(N^-1) covariance
edge shift, negligible at the TW scale, despite a nonvanishing spike.

This follows the prior report's proposed next step. Critical and supercritical
fluctuations will not be claimed. The threshold is to be derived from pole
separation, rather than assumed to be an outlier theorem.

## Proof and independent verification

Wrote PROOF.md. The extension closes the proposed strictly subcritical
quadratic-coefficient case. The key new exact identity, with
c=1-1/d, tau=2/[d(d+2)] and (N)_k the falling factorial, is

    E Tr B^4 = (N)_2 mu_4 + 2(N)_3(c tau)^2 + (N)_4 c tau^3,
    mu_4=12(d-1)(5d^2-13d+12)/[d^4(d+2)(d+4)(d+6)].

It implies ||B||_op=O_p(d^-1/4). The covariance has one eigenvalue
v+q N/d+o_p(1) and all others v+o_p(1). At the scalar MP stationary point,
the population pole gap is strictly positive exactly when
q alpha sqrt(b)<v. The deterministic edge lemma now permits a population
eigenvalue of nonvanishing height. Its bound is C Tr((Sigma-vI)^2)/N,
which is O_p(N^-1) here and is o_p(N^-2/3).

Created verify_subcritical.py with independent coordinate-polynomial
integration for the two-vertex, three-vertex and four-vertex walk expectations.
It uses neither the traceless-tensor contraction nor the trace formula to
compute these expectations. It also exhaustively enumerates all walks for
N=2,...,7, checks the predecessor's rational identity and sixth moment, and
solves finite subcritical covariance edges by both derivative bisection and
direct golden-section minimization. A separate formula from the rational
identity checks the first-order 1/N shift for a trace-preserving rank-one
population. No matrix simulation or TW numerical fit is involved.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B verify_subcritical.py
```

Exit 0, under 0.1 seconds of script time, standard library only, small bounded
polynomial dictionaries and no numerical arrays. The script refuses computation
if os.getpriority(os.PRIO_PROCESS,0)<15. The launcher printed
`nice: setpriority: Operation not permitted`, but that guard passed: the
effective inherited process priority was already at least 15. The warning
therefore does not establish a failure of the requested effective priority.

Output:

```text
Predecessor rational cancellation identity: 3 exact checks passed
Spherical sixth and centered eighth moments: exact checks passed
d=2: coordinate integrations pair/star/cycle = 3/128, 1/64, 1/128
d=3: coordinate integrations pair/star/cycle = 16/945, 16/2025, 16/10125
Fourth-trace walk multiplicities: exhaustive n=2,...,7 passed
r=0.25: n*(edge-e0)=0.562485236; independent first-order coefficient=0.562500000
r=0.5: n*(edge-e0)=1.030297487; independent first-order coefficient=1.030330086
r=2: n*(edge-e0)=4.121100777; independent first-order coefficient=4.121320344
r=4: n*(edge-e0)=8.999325151; independent first-order coefficient=9.000000000
Edge solver maximum disagreement: 1.776e-15
Subcritical / critical / supercritical pole signs: passed
Transposition normalization: both rectangular orientations passed
PASS: exact algebra and scalar edges only; elapsed 0.018s
```

The first recheck thus holds independently, and the new load-bearing walk
expectations and counts agree with independent exact calculations. The edge
bound is checked in both rectangular orientations, and the pole sign test
includes critical and supercritical inputs to detect a reversed threshold.

## Attempts to break the result and final audit

Checked the centered fourth moment a second way by expanding its four raw
moments: the numerator over d^4(d+2)(d+4)(d+6) is
60d^3-216d^2+300d-144=12(d-1)(5d^2-13d+12). The four-distinct-vertex
expectation has two independent derivations: successive integrations give
tau^2 E<z_j,z_l>^2=c tau^3; the covariance-operator trace gives
dim(H)tau^4=c tau^3. Independent coordinate integration agrees at d=2,3.
The three-distinct-vertex term has coefficient 2, not 1: either opposite
pair can be identified. Exhaustive walk counts test this explicitly.

The exact decomposition's diagonal was checked: (v-q/d)+(q/d)=v;
its off-diagonal is q/d+q(rho^2-1/d)+R=q rho^2+R. The rank-one term's
eigenvalues are v+q(N-1)/d and v-q/d; no N/d normalization is lost.
The threshold was re-derived by multiplying the pole gap by sqrt(b):
q alpha<v/sqrt(b) is q alpha sqrt(b)<v. The script tests both signs
and the equality case. At equality pole separation fails; no assertion of
ordinary TW or an outlier fluctuation theorem is made there.

The O_p(N^-1) edge bound is stronger than the N^-2/3 precision required;
its scaled size is O_p(N^-1/3). For uniform conditioning, the deliberately
weaker event Tr D^2<=N^1/6 gives scaled error O(N^-1/6), also vanishing.
The event's three algebraic failure bounds are respectively O(N^-1/2),
O(N^-3/4), and O(N^-1/6); checked directly with fourth- and second-moment
Markov inequalities. Uniform moment bounds require bounded ||U|| and Sigma,
both proved. Read back PROOF.md in full, checking these hypotheses and the
sample count m in the external theorem.

The launcher warning prompted one additional read-only scalar diagnostic:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B -c 'import os; print("effective nice value:", os.getpriority(os.PRIO_PROCESS, 0))'
```

Output: `nice: setpriority: Operation not permitted`, followed by
`effective nice value: 20`, exit 0. Thus the guard in the verification run
passed because the process was already at a sufficiently low effective
priority; the warning did not invalidate the observed nice value. No repeat
of the numerical checks was needed.

Read the T248 Gaussian-input He2-spike memory via the read-only topic index
and its actual path under ~/.claude/projects/-Users-user/memory/.
The index's relative link under the brain mirror was stale. This is a scope
check, not an authority for this proof: Gaussian random-norm inputs lose exact
conditional centering and are expressly excluded here.

No proof step failed within the chosen regime. The attempted global
operator-norm-small approach fails for q>0 because the population spike
persists; separating it and using pole separation resolves the subcritical
case only. Critical/supercritical spikes, linear components, random column
norms, polynomial activations and ratio one remain outside the result.

Final artifact checks: `wc -l LOG.md PROOF.md REPORT.md verify_subcritical.py`,
`head -1 REPORT.md`, and targeted `rg -n` on the verdict, threshold,
fourth-trace formula, edge shift, source and priority guard. All four files
exist, the report starts with the required verdict, and the same strict
threshold appears in the theorem, log and report. The complete proof was
read back in two consecutive sed ranges. No additional numerical run was
needed after the successful independent checks.

Completed report read-back at 05:20:58 +04. The delivered result is the
strictly subcritical quadratic-component theorem, with proof, reproducible
independent scalar checks and the remaining critical/supercritical comparison
problem identified. No additional work outside the selected piece was started.
