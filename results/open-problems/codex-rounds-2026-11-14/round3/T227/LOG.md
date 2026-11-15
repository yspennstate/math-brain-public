# T227 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 03:33 Asia/Tbilisi (2026-11-14 23:33 UTC).

## 1. Orientation and bounded literature check

Read the previous REPORT.md, LOG.md, PROOF.md, verify.py and scout.py, without editing the earlier folder. Read the compute governor state: `status=warn`, `mode=owner_away_open`, CPU saturated. Only small scalar standard-library calculations are planned. All writes stay here. The specific instruction against outside writes overrides the general mesh/checklist/brain updates, which would mutate shared files elsewhere. No subagents or git commands.

Read-only commands inspected the earlier files and the startup MEMORY.md. Subsequent programs use `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ...`. The sandbox prints `nice: setpriority: Operation not permitted`; the inherited priority will be checked inside the audit. Scripts will impose a CPU limit well below 20 minutes.

Web search started at approximately 03:34 local time, with a five-minute cap. Queries: `catapult deep convergence neural networks 2026 finite width`; `catapult nonlinear neural networks convergence proof`; `catapult deep proof after:2026-11-13`; `catapult finite-width convergence nonlinear`. Primary sources opened: the original arXiv:2003.02218, the ICLR 2024 quadratic-model paper, arXiv:2610.23007v1, and arXiv:2607.04993v1. Scope findings will be appended after reading.

The bounded check found no solution of the requested deep finite-width random-law problem. Search completed within five minutes. Opened sources and verified scope:

- Aitor Lewkowycz, Yasaman Bahri, Ethan Dyer, Jascha Sohl-Dickstein, Guy Gur-Ari, *The large learning rate phase of deep learning: the catapult mechanism*, [arXiv:2003.02218](https://arxiv.org/abs/2003.02218): original solvable-model/empirical paper.
- Libin Zhu, Chaoyue Liu, Adityanarayanan Radhakrishnan, Mikhail Belkin, *Quadratic models for understanding catapult dynamics of neural networks*, [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/949b3011c50300a2b4e60377466f52a8-Paper-Conference.pdf): Theorem 1 concerns the neural quadratic model, not the original deep nonlinear network.
- Quan Nguyen, Robin Yadav, Param Mody, Mark Schmidt, *A Minimal ReLU Classifier on Non-Linearly Separable Data: Convergence and Implicit Bias at and beyond the Edge of Stability*, [arXiv:2610.23007](https://arxiv.org/abs/2610.23007): the catapult theorem is for a minimal shallow classifier, rather than a deep wide architecture.
- Thomas Hofmann, *The Map Behind the Flow: Finite-Step Gradient Descent as a Dynamical System*, [arXiv:2607.04993v1](https://arxiv.org/html/2607.04993v1): the depth extensions use aligned/balanced reductions; no matching theorem for the requested general initialization was identified.

This is a limited update check, not an exhaustive absence claim. No SOLVED_ELSEWHERE.md is justified.

## 2. Independent recheck of the earlier result

Re-derived the sparse gradients directly: with `u=tanh(c)`, `v=tanh(b*u)`, `q=1-v*v`, they are `(v,a*q*u,a*q*b*(1-u*u))`. Thus `p_i^+=p_i-(eta/m)*F*j_i` and `lambda=m^{-2} sum |j_i|^2`. The initial interval bounds and the tail cross-gradient integral in the earlier proof have the correct factors of `m`. The induction establishes segment containment before applying the integral. Independent arithmetic and trajectories will be implemented next, before extending the result.

Created and ran `recheck_previous.py`, independently of the old scripts. Its exact exponential enclosure reduces the argument to at most `1/8`, uses a degree-12 positive series with a remainder bound there, and squares the resulting rational interval. It verifies the entire old entrance/tail arithmetic and independently simulates asymmetric sparse networks.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py
```

Output (exit 0):

```text
status: PASS
a1_lower: 6.2057725
a1_upper: 6.579595044
b1_upper: -19.17912740489895
c1_lower: 1.0732194798371582
kernel0_lower: 37.65368770803901
kernel0_upper: 38.67861402583242
loss0_upper: 6.496210125
loss1_lower: 19.219999998078
sparse_network_audits: 50
max_residual_ratio: 0.1000000009164335
process_nice: 20
max_rss_bytes: 14876672
seconds: 0.003994333033915609
```

Saved `previous_recheck.json`. **The earlier result holds:** its numerical constants, the first spike, the kernel normalization, and the summable-movement invariant-region argument survive this independent recheck. The original scripts were read but neither imported nor run.

## 3. Chosen extension, before its calculation

Extend just the sparse architecture to a fully connected second hidden layer, training all `m^2+2m` coordinates by ordinary Euclidean GD. Keep the same two tanh layers, one-datum law, noncentered independent initialization, and interval `eta in [0.9m,1.1m]`. Define

`F(x) = m^{-1} sum_i a_i tanh(m^{-1/2} sum_j B_ij tanh(c_j*x))`,

with independent `a_i in [7.99,8.01]`, `sqrt(m)*B_ij in [.499,.501]`, and `c_j in [1.999,2.001]`, uniformly distributed. The fixed `m^{-1/2}` is part of the architecture; `B_ij`, not its rescaling, is the Euclidean trainable parameter. This choice is the earlier report's proposed dense-layer extension. It removes the independent-path structure and requires a real bound on the shared first-layer gradients.

Plan: prove the entrance step by row and column averages; bound the tail in the convex region `|a_i|<=16`, `-26<=sqrt(m)*B_ij<=-18`, `c_j>=1`; prove a cross-gradient bound in the correct full Euclidean metric. The new lower bound on each scaled dense weight controls column sums, which the sparse proof did not need. Independent full-matrix trajectories, finite differences in the actual `B` coordinates, and asymmetric row/column corner patterns will try to break the certificate. This still does not identify eta_max or treat centered initialization.

## 4. Dense proof and first audit

Wrote PROOF.md with all parameter derivatives, the entrance inequalities, a full-space cross-gradient estimate, and a simultaneous-update-segment induction. The dense gradients couple each first-layer coordinate to every second-layer row. The scaled middle-layer entries `W=sqrt(m)*B` are used for estimates only; the gradient metric remains Euclidean in `B`.

The new arithmetic is the entrance lower bound `W_1>-24.077804521158427>-25`, together with the saturated-region derivative bound `|C_j|<=16*26*10^{-10}`. The normalized cross-gradient error is bounded by `10^{-10}+(16*10^{-10})^2+(416*10^{-10})^2`, independently of width. This gives the same contraction and initial/final kernel constants as the sparse certificate.

Created `verify_dense.py`. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_dense.py
```

Output (exit 0):

```text
status: PASS
W1_lower: -24.077804521158427
W1_upper: -19.17912740489895
tail_cross_error: 1.0000173312e-10
contraction_upper: 0.100000011
tail_a_upper: 14.897142857142857
tail_W_lower: -25.00000001327543
tail_W_upper: -18.99999998672457
tail_c_lower: 1.069999654838857
dense_network_audits: 450
max_residual_ratio: 0.10000000675668176
autodiff_gradient_max_error: 4.440892098500626e-16
finite_difference_gradient_max_error: 1.9750584501210255e-10
actual_coordinate_update_max_error: 5.329070518200751e-15
independent_forward_max_error: 8.881784197001252e-16
tail_cross_checks: 256
tail_cross_min: 0.9999999999950473
tail_cross_max: 1.0
process_nice: 20
max_rss_bytes: 17973248
seconds: 1.6939143749768846
```

All inherited entrance/kernel/loss constants also passed and match the independent sparse recheck. `dense_verification.json` stores exact fractions, summary statistics and all trajectories. Widths: 1, 2, 3, 7, 16, 64. Steps: .9, .95, 1, 1.05, 1.1 times width. Cases: all eight global corners, checkerboard entries, row stripes, column stripes, a singled-out column, and three independent random seeds. Every one of the `m^2` middle-layer entries is updated separately.

The Euclidean-coordinate audit constructs `B=W/sqrt(m)` and recomputes the network separately, using forward-mode automatic differentiation and centered finite differences. It also compares one actual `eta=m*h` Euclidean gradient update with the auxiliary-coordinate recurrence. These checks address the main possible error: accidentally proving convergence for a different metric on `W`.

## 5. Second derivation of the bounds; attempts to break the result

Created `audit_dense_intervals.py`, a separate rational interval implementation in the actual `(a,B,c)` coordinates. It uses degree-12 exponential enclosures after argument reduction and repeated squaring, with outward rational rounding. It differentiates the literal full-matrix expression and sums all Euclidean gradient coordinates without using the proof's cancelled powers of width. Square widths make the square roots rational. The finite widths in this audit support, rather than replace, the proof for all widths.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_dense_intervals.py
```

Output (exit 0): `status: PASS`, widths `[1,4,9,64]`. At every tested width the independent intervals were:

```text
m*lambda_0 in [38.093409949877504,38.433382890406754]
a_1 in [6.216433996531259,6.572815374076733]
sqrt(m)*B_1 in [-23.927243561754505,-19.275272485209804]
c_1 in [1.1004800929498018,1.2791162821695927]
tail cross-gradient in [0.9999999997999983,1.0000000000000018]
tail coordinate movement bounds (a,sqrt(m)*B,c):
[8.297142857142857,1.3275428571428572e-08,3.451611428571429e-07]
process_nice: 20
max_rss_bytes: 23756800
seconds: 0.4583416249952279
```

Printed decimals are summaries of exact rational intervals; the assertions use fractions. Saved `interval_audit.json`. This second calculation independently confirms every margin and kernel/contraction scale used in the dense proof. Its initial bounds are tighter than the deliberately coarse published certificate.

Adversarial checks and scope audit:

- Dense row/column asymmetry: checkerboards, stripes, a singled-out column and independent matrices all pass. The proof uses full row and column averages, without equal-path substitution.
- All coordinates trained: forward-mode AD and finite differences agree with the full `m^2+2m` Euclidean gradient. The independent Euclidean update agrees with the auxiliary recurrence to `5.33e-15`.
- Tail sign changes: numerical cross-gradient checks include independently chosen output signs at `a=+-16`; the proof bounds the hidden contributions in absolute value.
- Domain boundaries: tail checks include `c=1` and `W=-26,-18`. The proof allows arbitrarily large `c`. It establishes next-endpoint containment before invoking segment convexity, so contraction is not assumed to prove its own domain.
- The newly needed lower bound `W>=-26` is preserved by a summable-movement estimate, not assumed after initialization. Omitting it would leave the dense column-sum estimate unjustified; the sparse tail bound cannot simply be copied.
- Endpoints and continuum of steps: all numerical endpoints pass; rational inequalities cover every `h in [.9,1.1]` simultaneously.
- Near-zero floating-point cancellation is excluded from numerical ratio diagnostics. Exact convergence follows from the integral and geometric-series proof.
- The initial law is a full product law with separate perturbations of all middle-layer entries. It is positive and narrowly concentrated; this is not a centered-Gaussian or standard NTK-initialization result.
- No Hessian claim, onset theorem near `2/lambda_0`, maximal-step claim, or divergence theorem is proved.

No certificate or numerical audit failed. The obstruction to extending this argument to centered initialization is the first update: the uniform row signs and entrance margins used here no longer follow. That problem was not solved. No novelty claim relative to all literature is made.

## 6. Report

Wrote REPORT.md with the required PARTIAL verdict, the dense theorem, the independent recheck, reproduction commands, limitations and the next suggested step. The only substantive extension in this session is from a diagonal to a fully connected second hidden layer. Every artifact is in this folder; no external stores were changed.

Final read-only audit, using `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B -` with a short standard-library inspection: all three saved JSON results report PASS; all six text deliverables exist; REPORT.md starts with the required `VERDICT: PARTIAL` line. File sizes: REPORT.md 5414 bytes, PROOF.md 10716 bytes, recheck_previous.py 3919 bytes, verify_dense.py 10924 bytes, audit_dense_intervals.py 5065 bytes. Finished 2026-11-15 03:44:56 Asia/Tbilisi.
