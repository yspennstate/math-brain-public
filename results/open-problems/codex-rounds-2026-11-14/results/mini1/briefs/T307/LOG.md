# T307 working log

Task received: 14 November 2026, approximately 22:12 +04. “Push this problem forward by one checkable piece.”

## 22:12 — orientation and literature check started

Read the local prompt, the shared memory index and the compute governor state (read only). The current folder initially contains only PROMPT.md. The later task-specific instruction prohibits writes elsewhere, so no shared checklist, mesh or brain commands that write outside this folder will be run. No git or subagents.

Commands: `pwd`; `rg --files -g '*.md' .`; `date '+%Y-%m-%d %H:%M:%S %Z'`; a short Python read of the memory index and compute state, invoked with `OMP_NUM_THREADS=1 nice -n 15`.

Compute state: warn / owner_away_open; no heavy computation planned. `nice -n 15` emitted `setpriority: Operation not permitted`, although the read command completed. This is recorded rather than represented as a successful priority change.

Web search started for trained score networks, gradient descent, minimax rates, and 2025–2026 results. Initial candidates include Han–Razaviyayn–Xu (2024; NTK-based), Wu–Marion–Biau–Boyer (2025; implicit regularization), and a 2025 nonparametric generalization paper. These need inspection before deciding whether they meet the problem's exclusions.

## Literature check, first findings

Opened the arXiv abstract and full HTML of Yinbin Han, Meisam Razaviyayn and Renyuan Xu, *Neural Network-Based Score Estimation in Diffusion Models: Optimization and Generalization*, arXiv:2401.15604v4 (18 April 2026). The revised abstract claims minimax bounds; the full theorem must be read because Assumption 3.8 imposes a lower bound on the smallest sample NTK eigenvalue. The method really trains finite networks but is analyzed by kernel coupling. This is a substantial candidate advance, not yet a verified solution of the density-estimation question.

Also opened the primary pages of Yu-Han Wu, Pierre Marion, Gérard Biau and Claire Boyer (COLT 2025, PMLR 291:5718–5756), and Sinho Chewi, Alkis Kalavasis, Anay Mehrotra and Omar Montasser (COLT 2026 extended abstract, PMLR 336:1434–1435). The former gives a nonmemorization obstruction; the latter gives score-to-density reductions, rather than a GD convergence guarantee.

Search result metadata is unreliable: one result associated arXiv:2611.01658 with conditional diffusion; opening the actual arXiv page gives *Long-Time Behavior of Zero-Noise Mean-Field Adam*. Do not use that snippet as a reference.

## Literature decision and chosen piece (before starting the proof)

The search took less than ten minutes. No verified unconditional solution beyond the prompt's November 2026 checkpoint was found. The April 2026 revision is before that checkpoint, is based on NTK coupling, and retains a sample-eigenvalue assumption; it is not enough to mark the requested problem solved elsewhere. Opened also Stanislas Strasman, Sobihan Surendran and Sylvain Le Corff, *Non-asymptotic Convergence of Stochastic Gradient Descent in Score-based Generative Models*, arXiv:2607.04775v2 (7 October 2026): its abstract describes nonconvex optimization bounds and an NTK regime, rather than an unconditional nonparametric density-estimation theorem.

Choice: prove a positive approximation-error floor for the bias-free, joint space–time ReLU denoiser used in arXiv:2401.15604v4, including its clipped output. This is one architecture obstruction, not a negative answer to general T307. The reason is exact positive homogeneity in `(x,t-T0)`: a conditional mean close to 1/2 on two dilated regions cannot be fitted by such a function. It gives a precise architectural requirement for a future trained-network theorem.

Target special case: one-dimensional OU diffusion, time uniform on [1,2], any starting density on [0,1] with mean 1/2, and output clipping to [-1,1]. Aim for an explicit positive lower bound uniform in width, weights, and training algorithm. A smooth compactly supported non-Gaussian starting density is included. Planned checks: derive the posterior mean bounds both by likelihood-ratio comparison and direct integral inequalities; independently derive the two-point least-squares constant; check clipping, dilation Jacobian, noise normalization and the time shift. The theorem will not claim a failure of biased networks or a lower bound for all GD algorithms.

## Proof simplification before writing

A stronger and simpler version avoids posterior likelihood estimates: use any smooth density supported in the ball of radius 1/16 about `(1/2,0,...,0)`, with declared clipping radius D=1. Every posterior mean remains in that convex ball. This works in every fixed dimension, rather than only dimension one. It also works uniformly for `0 <= T0 <= 1/2`, `T >= 2`: select shifted-time rectangles `[1/2,3/4]` and their doubles. Their physical times remain between 1/2 and 2, so the Gaussian density has an elementary positive lower bound. The resulting normalized risk floor is `C_d/(T-T0)`, hence at least order `1/log N` when `T=O(log N)`. This is the same homogeneity obstruction chosen above, with simpler hypotheses and a stronger time-range conclusion.

The related brain navigation entry `t307_one_step_dsm_finds_hidden_line_2026_11_01` was found by a read-only text search. Its first suggested path was missing. No previous result from that entry is assumed here.

The PDF of arXiv:2401.15604v4 was opened as an independent format check of the HTML. The displayed architecture has no hidden or output bias; the projection is onto the Euclidean ball. All assertions about that architecture are restricted to the displayed definition, not unshown implementation details.

## Proof written and audit started

`PROOF.md` now contains the full argument. The two-point squared-error constant is `5/256`; saturation gives the larger bound `49/256`. The integration rectangle has volume `(32 sqrt(d))^(-d)/4`, and its dilation has Jacobian `2^(d+1)`. On both rectangles the OU marginal density is at least `exp(-1)(2 pi)^(-d/2)`. Multiplying gives `C_d = 5 exp(-1) / (1024 (32 sqrt(2 pi d))^d)`.

The first run of `audit_obstruction.py` failed before any mathematical checks: raising the existing RLIMIT_DATA cap to 512 MiB is disallowed. The script was changed to take the minimum of the existing soft limit, hard limit, and requested ceiling. This is a resource-limit correction, not a change to the proof.

An attempted read-only `ps` priority check was denied by the sandbox (`/bin/ps: Operation not permitted`). The audit instead reads its own priority using Python's `os.getpriority`, if available. All Python audit invocations use `OMP_NUM_THREADS=1` and `nice -n 15`; the environment emits a setpriority warning, whose reason remains to be checked.

## Exact audit completed

The second resource-limit attempt also failed on RLIMIT_DATA, even when using the inherited limits. Removed that setting; retained a 30-second CPU cap. The resulting standard-library script completed successfully and used approximately 14.75 MB peak resident memory. `os.getpriority` reported nice **20**, which is already more deprioritized than requested. This explains why the wrapper's failure to change priority did not lead to an ordinary-priority run.

Exact command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_obstruction.py > audit_output.txt 2>&1
```

Complete captured output (`audit_output.txt`; structured data also in `audit_data.json`):

```text
nice: setpriority: Operation not permitted
nice: setpriority: Operation not permitted
{
  "status": "PASS",
  "priority_nice": 20,
  "omp_num_threads": "1",
  "grid_count": 1025,
  "exact_identity_and_clipping_checks": 9225,
  "scalar_grid_minimum": "5/256",
  "scalar_minimizer": "5/16",
  "saturated_error_bound": "49/256",
  "gaussian_exponent_upper": "25/64",
  "peak_rss_platform_units": 14745600,
  "cpu_seconds": 0.15796,
  "constants": {
    "1": {
      "product": 2.2394205196188345e-05,
      "displayed": 2.239420519618834e-05,
      "dilation_jacobian": 4
    },
    "2": {
      "product": 1.3959367638664046e-07,
      "displayed": 1.3959367638664049e-07,
      "dilation_jacobian": 8
    },
    "3": {
      "product": 6.698444235386e-10,
      "displayed": 6.698444235386001e-10,
      "dilation_jacobian": 16
    },
    "5": {
      "product": 9.677228425757962e-15,
      "displayed": 9.677228425757964e-15,
      "dilation_jacobian": 64
    }
  },
  "note": "Finite checks supplement the proof; they do not establish the continuous theorem."
}
```

The raw output also contains two `nice: setpriority: Operation not permitted` lines. The script's own priority measurement, not those warnings, establishes its actual nice level.

## Independent mathematical audit

Added `AUDIT.md`: a Cauchy–Schwarz derivation of the two-point constant, a convex-barycenter derivation of the posterior bound, an SDE-integral derivation of the noise variance, and checks of clipping, positive probability, volume, time endpoints and score weights. Added the RKHS corollary to `PROOF.md`: kernel sections are homogeneous, and norm convergence preserves their pointwise scaling relation. Thus the same approximation limitation holds before the training dynamics enter.

Final citation audit corrected a draft author attribution for arXiv:2507.04794 using the actual arXiv author line: Arthur Stéphanovitch, Eddie Aamari and Clément Levrard. Only those verified names remain in `LITERATURE.md`. No assertion about that paper's optimization theorem is made.

## Completion

Wrote `REPORT.md` with the verdict, theorem, reproduction command, failed attempts, limitations and next step. A final read-only Python check (under `OMP_NUM_THREADS=1`, `nice -n 15`, with bytecode writes disabled) verified that all eight deliverables exist and are small, the report has the required first line, the complete audit output occurs verbatim above, the captured JSON equals `audit_data.json`, the audit passed, the actual nice value was at least 15, and the recorded RSS was below 1 GB.

Output: `Final artifact check: PASS (8 files; exact output preserved; report verdict and citations checked).`

Final status: the chosen approximation obstruction is proved. No positive trained-network rate is claimed; general T307 remains unresolved in this session. All writes stayed in this folder; no git, subagents, posting or external mutations were used.
