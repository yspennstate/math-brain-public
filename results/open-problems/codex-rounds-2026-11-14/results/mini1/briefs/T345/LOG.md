# T345 work log

Task received: 2026-11-14, approximately 21:30 Asia/Tbilisi (UTC+4).
User's task: “push this problem forward by one checkable piece.”

## 21:30 — orientation and search started

Read the task and inspected this directory; no prior mathematical artifacts exist.
Read the shared compute state: status warn, CPU saturated. Only short, single-thread,
low-memory checks will be used. No subagents, git, or external writes.
The task-specific order to write only here overrides global brain/checklist/mesh
commands that mutate files outside this directory. Startup memory/navigation was
read directly instead.

Literature search started at 21:31; deadline 21:41 (ten minutes).
Initial web queries:

- adversarial robust learning computational hardness Gaussian mixture natural distributions statistical query planted clique
- robust Gaussian classification minimax optimal adversarial risk efficient learning 2025 2026

Promising hits: Dan–Wei–Ravikumar (2020), optimal Gaussian robust classification;
Min–Vidal (2025), orthonormal Gaussian mixtures. These need opening before use.
The first seems already to settle an important common-covariance special case;
avoid presenting that established result as new.

## 21:33 — literature check ended; concrete piece selected

The web search took under three minutes, below the ten-minute limit. Opened
the two source arXiv pages, Dan–Wei–Ravikumar's paper PDF (especially the
model and Theorems 2.1/3.1/4.1), Min–Vidal's proceedings page, Bhagoji–Cullina–Mittal's
arXiv page, and Dohmatob's arXiv page and full HTML. No opened source settles
the whole natural-distribution problem. No verified post-November-2026 solution
was found; this limited search cannot certify nonexistence.

Read prior local T345 memory: labelled sparse mean-shift mixtures already have
an efficient soft-thresholding learner; do not reuse that as a hardness candidate.

Chosen piece: an exact reduction of robust classification for two spherical
Gaussians with arbitrary, possibly unequal variances in R^d to a two-dimensional
Euclidean half-plane problem. Use axial coordinate and distance to the line of
means. Prove the equality against ALL Borel classifiers, rather than assuming
that symmetry forces an optimal symmetric classifier. This is a concrete
“reduction to a cleaner statement” under the task's permitted outcomes.

Why: common-covariance results do not cover unequal spherical variances.
The common angular variable is independent of the label and of the two quotient
coordinates. Restricting an arbitrary classifier to each meridian should give
the lower bound; lifting a half-plane classifier should give the reverse bound.
This avoids the invalid shortcut of averaging deterministic classifiers.

Planned extensions within this same piece: explicit quotient density, a
total-variation learning-to-optimization transfer without a mean-separation
assumption, and a finite graph check comparing unrestricted and invariant
classifiers. A full polynomial-time same-radius optimization theorem is not
assumed: discretization may need radius slack, which must be proved or reported.

## 21:35 — reduction established; approximation route strengthened

The exact reduction follows by meridian slices and an exact ball-image identity.
For a finite half-plane grid with cell radius h, a weighted bipartite independent
set produces a classifier whose radius-epsilon risk is at most the optimal
radius-(epsilon+2h) risk, plus tail and weight-estimation errors.

The apparent radius-slack obstruction can be controlled for spherical Gaussians:
dilating a classifier by a=1+2h/epsilon changes its risk by at most the TV
distance between X and X/a. A direct Gaussian KL calculation bounds this by
(2h/epsilon)(sqrt(d)+M/s), with centered means bounded by M and scales >=s.
This gives a polynomial arithmetic-time algorithm when dimension, mean/scale
bounds, 1/epsilon, and desired inverse accuracy are polynomially bounded.

Will write this as an explicit special-case learning theorem, with the exact
dimension reduction as its core. Unknown means and scales can be fitted in TV;
the fitted line need not approximate the true line. All remaining constants and
the grid construction still need an adversarial audit.

## 21:38 — proof saved

Wrote PROOF.md with an exact quotient theorem and an additive robust-learning
theorem for balanced N(mu_y, sigma_y^2 I_d), allowing unknown unequal scales,
1<=sigma_y<=S and ||mu_1-mu_0||<=M. Runtime is polynomial in numeric bounds
d,S,M,1/epsilon,1/eta,1/alpha, in a stated real-arithmetic model.
Labelled sample count is O((d+1)/(alpha eta^2)) per class; the large graph
uses only additional synthetic samples from the fitted model.

Load-bearing formulas to audit independently:

- exact ball image under (axial coordinate, perpendicular norm);
- independence of the angular variable, including d=2;
- graph edge radius 2(epsilon+h), comparison radius epsilon+2h;
- dilation KL <= t^2(d+M_0^2/(2s^2));
- empirical category L1 error and max-flow/independent-set relation;
- fitted mean/scale KL <=2b^2 and total failure probability alpha.

No claim of a full solution of T345 or of novelty over all literature is made.

## 21:40 — first audit command blocked by resource setup

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 check.py
```

Output:

```text
nice: setpriority: Operation not permitted
ValueError: current limit exceeds maximum limit
```

The failure occurred at setrlimit before any mathematical computation. Inspect
existing process priority and resource limits before choosing a compatible
guard. The script is standard-library-only and intentionally tiny in memory.

## 21:41 — finite checks passed

The priority inspection command was:

```sh
env OMP_NUM_THREADS=1 nice -n 15 python3 -c 'import os,resource; print("nice", os.getpriority(os.PRIO_PROCESS,0)); print("address_space_limits",resource.getrlimit(resource.RLIMIT_AS)); print("cpu_limits",resource.getrlimit(resource.RLIMIT_CPU)); print("maxrss",resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)'
```

It reported inherited nice 20 and unlimited address-space/CPU limits. This is
lower priority than nice 15. The sandbox rejects setpriority even though the
requested nice launcher is used; it does not raise the inherited priority.
Changed the script to preserve the existing hard resource limits while setting
soft limits, and to verify inherited nice>=15 and measured RSS<1 GB.

Reran the exact command from the previous entry. Complete relevant output:

```text
nice: setpriority: Operation not permitted
Geometry: 320 cases; exact aligned distances and lower bounds passed.
Symmetry: 5 finite problems, 4096 unrestricted classifiers each; optima agree.
Graph: 80 weighted problems, 1024 subsets each; max-flow equals exhaustive optimum.
Density/KL: 4 chi integrals, 3 independent KL integrals, scalar and fit bounds passed.
Negative controls: angular dependence, l_infinity geometry, missing factor 2 detected.
Data: checks.json
Status: all assertions passed
Elapsed: 0.070 seconds; max RSS: 15564800 bytes
```

Seed 34520261114. All data, including every graph optimum, finite symmetry
optima, density integrals, and KL integrations, are in checks.json. The
numerical integration computes expectations of log density ratios directly,
independently of the closed-form KL expressions used in the proof.

## 21:44 — continuous interpolation check and independent analytic audit

An unresolved check was whether the graph's independent set really yields
the claimed risk after interpolation away from the representative points.
Added a continuous, one-dimensional Gaussian check: compute the graph
classifier, merge its positive intervals, then integrate the eroded/dilated
regions by exact normal CDFs, independently of grid risk estimates.

Reran the same command. Output:

```text
nice: setpriority: Operation not permitted
Geometry: 320 cases; exact aligned distances and lower bounds passed.
Symmetry: 5 finite problems, 4096 unrestricted classifiers each; optima agree.
Graph: 80 weighted problems, 1024 subsets each; max-flow equals exhaustive optimum.
Density/KL: 4 chi integrals, 3 independent KL integrals, scalar and fit bounds passed.
Continuous classifier: exact Gaussian interval risk satisfies the radius-slack bound.
Negative controls: angular dependence, l_infinity geometry, missing factor 2 detected.
Data: checks.json
Status: all assertions passed
Elapsed: 0.072 seconds; max RSS: 15810560 bytes
```

The continuous robust risk is 0.04177376137869648; the independently evaluated
comparison bound is 0.08855984448174589, below 0.1, so this is not a vacuous
upper-bound check. Source radius .25, comparison radius .65, cell radius .2.
Tail mass 0.00003167124183378611; L1 weight error 0.000010090901255027563.

Wrote AUDIT.md. In particular, re-derived the dilation-TV bound from the L1
derivative of the scaled Gaussian density and its Fisher score, independently
of KL/Pinsker. Re-derived the mean/variance estimates from chi-square laws.
Reviewed the axis, d=2, coincident means, closed-ball equality cases, the two
TV-transfer losses, and all four alpha/8 estimation events.

The soft CPU limit was installed. macOS still rejected the address-space
limit; measured peak RSS was 15.81 MB, far below 1 GB, and the standard-library
program has only small bounded arrays. Inherited nice remained 20. No heavy
computation or additional language-model workers were used.

## Completion

Saved REPORT.md with the required verdict line and the exact scope: efficient
additive-error Euclidean robust learning for bounded spherical Gaussian pairs,
including unequal unknown variances. Inspected all seven deliverable files.
The main problem remains unresolved for general covariance pairs and natural
hard distributions; no l_infinity or optimal-rate theorem is claimed.
No files outside this task directory were edited, and no git or publishing
commands were run.
