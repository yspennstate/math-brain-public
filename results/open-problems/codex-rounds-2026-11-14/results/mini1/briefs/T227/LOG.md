# T227 work log

Task: “push this problem forward by one checkable piece.” Started 2026-11-14 22:07 Asia/Tbilisi (18:07 UTC).

## Step 1: orientation and literature search

Read the local folder listing, startup memory index, and compute state. The compute governor reports `warn`, CPU saturation, and `owner_away_open`; no heavy computation is planned. All writes will stay in this folder. The later task-specific restriction on outside writes precludes updating the shared mesh/checklist/brain stores.

Commands used: `OMP_NUM_THREADS=1 nice -n 15 /bin/cat <compute_state.json> <MEMORY.md>` and `OMP_NUM_THREADS=1 nice -n 15 /bin/ls -la`. Both completed immediately. The sandbox prints `nice: setpriority: Operation not permitted`; it does execute the requested command. This limitation will be recorded for any verification script too.

Web search began at 18:08 UTC with queries “catapult phase deep nonlinear networks rigorous proof large learning rate 2025 2026” and “catapult dynamics nonlinear neural networks Zhu 2023 quadratic models convergence”. Candidates include the ICLR 2024 quadratic-model paper, arXiv:2301.07737, arXiv:2603.10079, and a recent minimal ReLU classifier paper. These are leads, not yet verified citations. Search is limited to ten minutes.

Opened primary sources:

- Libin Zhu, Chaoyue Liu, Adityanarayanan Radhakrishnan, Mikhail Belkin, *Quadratic models for understanding catapult dynamics of neural networks*, ICLR 2024: https://proceedings.iclr.cc/paper_files/paper/2024/file/949b3011c50300a2b4e60377466f52a8-Paper-Conference.pdf . The stated theorems concern NQMs, not the full deep network.
- David Meltzer, Min Chen, Junyu Liu, *Catapult Dynamics and Phase Transitions in Quadratic Nets*, arXiv:2301.07737v2 (2025 revision): https://arxiv.org/html/2301.07737v2 . Includes homogeneous two-layer networks and norm-decay arguments; not a deep-network finite-width theorem.
- Benjamin Gess, Daniel Heydecker, *Large Spikes in Stochastic Gradient Descent: A Large-Deviations View*, arXiv:2603.10079v2: https://arxiv.org/pdf/2603.10079 . Main Theorem 1 uses linear activation; Theorem 7 extends to certain shallow ReLU networks. This is SGD, not the requested deep full-batch theorem.
- Quan Nguyen, Robin Yadav, Param Mody, Mark Schmidt, *A Minimal ReLU Classifier on Non-Linearly Separable Data: Convergence and Implicit Bias at and beyond the Edge of Stability*, arXiv:2610.23007: https://arxiv.org/html/2610.23007v1 . Theorem 5.1 proves a two-step catapult for a small tied-weight ReLU classifier with logistic loss, not a deep wide architecture with random initialization.
- Thomas Hofmann, *The Map Behind the Flow: Finite-Step Gradient Descent as a Dynamical System*, arXiv:2607.04993: https://arxiv.org/html/2607.04993v1 . Exact reductions on balanced/aligned manifolds and scalar maps; ReLU discussion concerns a two-factor model.
- Aitor Lewkowycz, Yasaman Bahri, Ethan Dyer, Jascha Sohl-Dickstein, Guy Gur-Ari, *The large learning rate phase of deep learning: the catapult mechanism*, arXiv:2003.02218: https://arxiv.org/abs/2003.02218 . Original source opened.

These are substantial related shallow results, but do not resolve or substantially advance the specific deep finite-width high-probability theorem as stated. No `SOLVED_ELSEWHERE.md` is warranted on this evidence. This is a bounded search finding, not a claim of exhaustive coverage.

## Step 2: choice, before doing the calculation

Try to finish an explicit catapult certificate for a genuinely nonlinear two-hidden-layer tanh network on one datum, with all three layers trained. Use parallel paths and a fully correlated initialization to preserve a three-variable invariant subspace at any width. The output is the average of the paths, so learning rate scales with width. The intended result is an explicit nonempty interval above `2/lambda_0` on which the first loss rises, curvature drops, and the loss then tends to zero. This deliberately restricted initialization and sparse architecture do not settle the Gaussian fully connected problem. First search for a rational starting triple, then prove the resulting tail with explicit derivative bounds. If the certificate fails, retain the failed attempt and report it plainly.

## Step 3a: exploration and stronger choice

Created `scout.py` (standard library only, CPU limit 60 seconds) and ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B scout.py
```

Output: `candidates: 262`; `max_rss_bytes: 15499264`; exit 0, under one second. The sandbox again warned that setpriority is not permitted. First candidate: `(a,b,c)=(8,0.5,2)`, effective step 1. Loss `6.418369436452796 -> 20.450619446556615`; kernel `38.263146705494606 -> 0.9999999999999989`. Full candidate data saved in `scout_data.json`. Floating-point underflow at late steps is not evidence of exact convergence.

The saturated-region argument can handle independent path perturbations, not just equal paths. Strengthen the chosen piece to independent uniform initialization in `a in [7.99,8.01]`, `b in [0.499,0.501]`, `c in [1.999,2.001]` at every path, input 1, label 0, output `m^{-1} sum_i a_i tanh(b_i tanh(c_i x))`, and step `eta=m*h` for `h in [0.9,1.1]`. Prove a first loss spike, a kernel drop, geometric convergence of the residual, and convergence of every parameter. The interval certificate will be uniform over the entire initial box, hence probability one for this explicitly nonstandard law. No claim about `eta_max` or standard dense Gaussian networks is intended.

Literature search ended before 18:12 UTC, within the ten-minute limit. No further literature search is needed for this restricted certificate.

## Step 3b: exact certificate and independent audit

Created `verify.py`, using rational Taylor bounds for the few transcendental inequalities and exact rational arithmetic for the first step and the invariant tail. Ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify.py
```

Output (exit 0, under one second):

```text
Exact rational certificates: PASS
a1_lower: 6.2057725
a1_upper: 6.579595044
b1_upper: -19.17912740489895
c1_lower: 1.0732194798371582
m_kernel0_lower: 37.65368770803901
loss0_upper: 6.496210125
loss1_lower: 19.219999998078
contraction_upper: 0.100000011
tail_a_bound: 14.897142857142857
tail_c_lower: 1.0699986724571429
Full-network numerical audits: 27 PASS
Finite-difference gradient max error: 1.39779188224054e-10
Finite-difference NTK normalization error: 2.070779103746645e-10
max_rss_bytes: 15056896
```

Data: `verification_data.json` contains the exact rational certificates and all trajectories. Numerical audits use widths 1, 7, 64, both same-corner initializations and independently perturbed paths, and effective steps 0.9, 1, 1.1. Unlike the scout, this implementation uses the shared full-network residual. Gradients are independently checked by centered finite differences, and the width-dependent NTK normalization is checked by finite differences of the entire network function. The proof will use the rational inequalities, not late-time floating-point zeros.

## Step 4: written proof and attempts to break it

Wrote `PROOF.md`. The invariant region is `|a|<=16, b<=-18, c>=1` per path. The first update enters it with a positive margin. Absolute summability of the residual controls movement inside the region; a cross-gradient integral, rather than a frozen-kernel approximation, proves residual contraction. The endpoint estimate is established before using convexity to bound the whole update segment, avoiding a circular invariance argument.

Added the exact upper bound `m*lambda_0<39`. Together with `m*lambda_0>37`, this proves that the sample-dependent interval `[36/lambda_0,40/lambda_0]` lies inside the certified deterministic interval `[0.9m,1.1m]`.

Audit of assumptions and possible omissions:

- The network uses a common residual, not independent per-path losses. The full-network recurrence and the integral calculation both retain it.
- Initialization need not preserve equality between paths. Added all eight initial-box corners at width 1 and a width-8 network containing all mixed corners simultaneously. This targets the possible failure of a symmetric-path calculation.
- Both endpoints of the step interval were tested. The proof covers the continuum by interval bounds, not sampling.
- `a` can change sign during the tail. The cross-gradient bound allows this; its dominant coordinate is `v`, whose sign stays negative.
- No upper bound on `|b|` is silently assumed: the estimate `|b|*sech^2(b*tanh(c))<=72*exp(-27)` holds throughout the unbounded region. No upper bound on `c` is needed.
- The scalar NTK is not the loss Hessian. The proof and theorem explicitly use the NTK and ordinary gradient descent in the scaled coordinates `a_i,b_i,c_i`.
- The first large update is not approximated by a Taylor expansion. It uses the exact update formula. Segment estimates begin only after that update.
- The zero-residual case freezes all parameters and is included.
- The theorem is a special architecture and law, with a single zero-label example. It does not establish the onset at `2/lambda_0`, an interval extending all the way from that onset, a divergence threshold, or a result for centered Gaussian dense initialization.

Re-ran the exact same verification command after adding the upper-kernel and mixed-corner checks. Final output: all exact rational certificates PASS; `Full-network numerical audits: 63 PASS`; gradient finite-difference error `1.39779188224054e-10`; NTK normalization error `2.070779103746645e-10`; peak RSS `15712256` bytes; exit 0, under one second. All other displayed rational bounds match Step 3b. Final exact data and trajectories replace the earlier version of `verification_data.json`.

Priority check command:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B -c 'import os; print("process_nice:", os.getpriority(os.PRIO_PROCESS, 0))'
```

Output: `process_nice: 20`. Thus the workers already inherit a lower scheduling priority than nice 15; the sandbox warning does not indicate high-priority execution. All numerical runs use standard-library scalar code, one thread, approximately 15 MB RAM, and a 60-second CPU limit.

## Step 5: final report

Wrote `REPORT.md` with a PARTIAL verdict. Final inspection with `nice -n 15 /usr/bin/head -n 1 REPORT.md` confirmed the required verdict line. `nice -n 15 /usr/bin/wc -c PROOF.md REPORT.md LOG.md verify.py verification_data.json scout.py scout_data.json` reported 426354 bytes before this closing log entry. Deliverables are confined to this folder. Finished 2026-11-14 22:19 Asia/Tbilisi (18:19 UTC).
