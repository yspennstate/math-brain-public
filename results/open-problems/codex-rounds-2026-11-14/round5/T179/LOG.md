# T179 round 5 log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 08:32 Asia/Tbilisi.

## Orientation and brief literature check

Read the startup memory and compute state (`status=ok`,
`mode=owner_away_open`). No subagents, git, external writes or heavy computation.
The task-specific folder-only restriction takes precedence over the usual
external checklist, mesh, recall-event and brain-memory writes. Those commands
were not run because they mutate stores outside this folder.

Listed all three predecessor folders and read their reports, logs, proofs and
scripts. Longer concatenated tool output was truncated; the proofs and scripts
are being read separately to avoid relying on missing text.

Web searches: `"2611.07310" "Han"`, `"stochastic heat" "full Hölder"
uniqueness Han`, `"2608.01279"`. Opened the official abstract and HTML:
https://arxiv.org/abs/2611.07310 and
https://arxiv.org/html/2611.07310v1. The listed version is still v1,
submitted 5 November 2026, by Yi Han. Proposition 8.1 still assumes bounded
initial data for unbounded diffusion. Proposition 8.5 handles a pointwise
measurable drift. These are the inputs already recorded by the earlier rounds;
they do not newly settle the residual scope or the proposed path-dependent
extension. No later result appeared in the brief search (less than five
minutes). This is a scope check, not an audit of Han's main theorem.

## Recheck underway

The round-4 load-bearing assertion is that the Girsanov stochastic integral
is a Borel function of the state path and that its change of integrator has
the claimed sign. The audit will reconstruct this using the canonical
martingale family and a finite weighted predictable measure. Arithmetic
diagnostics will be rerun read-only with bytecode disabled.

## Audit result and choice of one extension

The round-4 result checks, conditional on its stated drift-free input.
Independent reconstruction: for elementary predictable spatial integrands,
the canonical weak-equation martingales give state-measurable integrals.
Their isometry uses the finite measure
`g(X_s(x))^2 mu0(dX) ds dx`. Predictable rectangles with smooth spatial
factors are dense even for unbounded g: first approximate rectangle
indicators, then use regularity of each induced finite spatial measure.
The target `b/g^2` has weighted square norm `E_mu0 A`. One fixed almost-sure
subsequence of the approximating path functions therefore supplies the same
integral in every drift-free realization. It is not necessary to know the
joint state-noise law.

In a drifted realization, removal gives `What=W+integral theta ds`.
Consequently `J=integral theta dW+A`, so `log D=integral theta dW+A/2`
there, whereas `log D=integral theta dWhat-A/2` under the drift-free law.
These give exactly both entropy identities, including their factor 1/2.
Equivalent measures preserve convergence in probability; finite-energy
stopping justifies the substitution before removing stops. No error found.

Chosen single extension: replace the pointwise Nemytskii drift by a jointly
Borel nonanticipating map `B:[0,T] x C([0,T];H) -> H` with
`||B(t,omega)|| <= C(1+||omega_t||)`. Prove weak well-posedness, equivalence
and the same density/entropy identities conditional on the same drift-free
input. This covers spatially nonlocal and history-dependent drift without
assuming that the state is Markov. The missing step is a canonical predictable
representative; it will be constructed by one-sided Bochner time averages,
which converge for almost every time on every continuous path. This choice
is recorded before writing the extension proof.

## Read-only diagnostic reruns

Commands (both exited 0):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T179/check_transfer.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T179/check_estimates.py
```

Round-4 output:

```text
nice: setpriority: Operation not permitted
Volterra absorption: 27 exact parameter triples passed
lambda = 1 + 24(T B^2 + G^2) + 72 G^4
each Laplace-kernel term <= 1/4; total <= 1/2
r=1e-06; heat trace=199.471140201; upper=200.471140201; expansion gap=2.84e-14
r=0.0001; heat trace=19.9471140201; upper=20.9471140201; expansion gap=0
r=0.01; heat trace=1.9947262692; upper=2.99471140201; expansion gap=0
r=1; heat trace=1; upper=1.1994711402; expansion gap=2.22e-16
Gaussian density, inverse signs, both entropies: 24 exact cases
sigma of either sign; positive, zero, negative drift included
rough initial example: 3 integrable exponents; a=1/2 excluded
nice=20; elapsed=0.002s; peak RSS=12.97 MiB
```

Round-3 output:

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
nice=20; peak RSS=13.17 MiB
```

The warning is the inherited-priority issue already recorded in the earlier
rounds: both scripts verified actual nice 20 before calculation. They use
scalar standard-library arithmetic and do not write output files. These
checks support constants and signs, not uniqueness of an SPDE.

## Extension proof saved

Wrote PROOF.md. The theorem permits any jointly Borel nonanticipating
H-valued drift with `||B(t,path)|| <= K(1+||path_t||)`. It constructs a
raw-canonical predictable representative by causal Bochner time averages,
equal to B for almost every time on each individual path. The modification
retains the current-norm bound everywhere. Pulling it back to any adapted
continuous solution gives a predictable drift direction, independently
of that solution's probability law.

Rebuilt the stopped moment bound without evaluating B on the stopped
convolution's altered history. Only the actual current state is replaced
before the stop, and its growth bound suffices. The forward and reverse
changes of measure therefore have bounded expected energy. The canonical
martingale integral then gives the density, uniqueness and entropy
identities. The proof contains a nonlocal running-threshold drift as an
example and a two-stage history-dependent Gaussian calculation that checks
which probability law appears in each entropy.

Self-audit in progress: ordinary rational left-endpoint sampling fails for
the Borel time function 1_Q(t), whose Lebesgue integral is zero. The proof
uses time averages instead and only asserts almost-everywhere agreement.
Growth in the running path supremum is deliberately not inferred from a
bound on the current state. Those are distinct hypotheses.

## New diagnostic

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_history.py
```

Exit code 0. Output:

```text
nice: setpriority: Operation not permitted
Two-stage history-dependent Gaussian laws: 54 cases passed
Normalization and both entropies checked by 1D quadrature
Positive/negative first drift and history control; zero cases included
Largest normalization/doubled-entropy residual: 9.83e-11
Entropy difference has the sign of the first drift when k != 0
Causal time average: four exact piecewise-polynomial error checks
L1 error = window; squared L2 error = 2*window/3
nice=20; elapsed=0.284s; peak RSS=13.02 MiB
```

The Gaussian test integrates out the second increment analytically and
uses Simpson quadrature for the first increment, splitting at the history
gate. It independently checks the closed forms using the normal CDF.
Unlike constant deterministic drift, this example has different expected
energy under the two laws. The time-average diagnostic integrates the
piecewise polynomial error exactly and compares with triangle areas.
These are diagnostics, not numerical proofs of SPDE uniqueness.

An initial attempt to append this output failed patch-context matching and
changed no file. The corrected patch saved it here.

## Final self-audit

Re-read the predecessor material in smaller pieces wherever the initial
concatenated output was truncated. The first round's check_heat.py was
read but not rerun: it writes heat_check.csv beside itself, which would
violate the predecessor folder's read-only restriction. The two later
scripts used above have no such mutation.

Checked all load-bearing constants a second way. The heat-trace constant
agrees between the Fourier and Gaussian calculations in the prior rerun.
The moment constants simplify to
`lambda=1+24(T K^2+G^2)+72 G^4`; the `72` comes from separately squaring
`6G^2/sqrt(8pi)` and multiplying by `16pi`. Each Laplace-kernel term is
at most 1/4, leaving absorption factor at most 1/2. Halving the energy
bound gives exactly the entropy bound in (6). The new two-stage Gaussian
example derives both entropy factors independently by conditioning on
the first increment, and quadrature checks them with residual <1e-10.

Checked the canonical representative path by path, including time zero,
nonconvergence points, arbitrary spatial equivalence-class representatives,
and a discontinuous running-threshold gate. Causal averages are adapted
and continuous; the predictable limit uses a measurable Cauchy set. The
current-norm growth bound survives at all convergence points by continuity
of the state path, and also at the chosen zero values elsewhere.

Expanded the measure-change audit in Section 5: the weighted elementary
integrand error tends to zero in probability under both equivalent laws.
The martingale error is localized by its quadratic variation; the drift
error is bounded by sqrt(A) times that weighted error. This avoids silently
assuming L2 convergence under the new measure, which equivalence alone
does not supply. The chosen almost-sure subsequence still defines the
same Borel state-path function. No joint state-noise uniqueness is assumed.

What failed: deterministic rational left-endpoint sampling is invalid for
Borel temporal coefficients, as the explicit 1_Q example shows. The
construction using time averages resolves this. No diagnostic failed.
The one log patch mismatch was corrected without changing mathematics.

The result permits arbitrary spatial nonlocality and past dependence with
growth in the current H norm. It does not prove estimates for drift growth
in the running path supremum, and it does not audit Han's core uniqueness
argument. No new literature result changed the earlier picture. All new
artifacts are in this folder; no predecessor files were edited.

Final verification: REPORT.md begins with the required verdict and matches
the theorem's nonanticipation and current-norm growth hypotheses. Checked
its commands, counts, residual and resource figures against the saved tool
outputs. Deliverables: REPORT.md, PROOF.md, LOG.md and check_history.py.
No further numerical check is needed after the final proof clarifications.
