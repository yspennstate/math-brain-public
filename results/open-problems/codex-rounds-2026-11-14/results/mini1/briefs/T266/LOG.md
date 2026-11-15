# T266 work log

Task received: 2026-11-14, approximately 22:08 Asia/Tbilisi (18:08 UTC).
Task: “push this problem forward by one checkable piece.”

## 1. Orientation and literature search started (18:08 UTC)

All writes are restricted to this folder. No git, subagents, external messages,
or external coordination/memory writes will be used. The task-specific folder-only
rule overrides the general instructions to mutate the shared mesh and brain.

Read-only commands: `pwd`, `rg --files -g 'AGENTS.md' -g 'MEMORY.md' -g '*.md' -g '*.py' .`,
`ls -la`, and `cat ~/.claude/compute/compute_state.json`.
The folder initially contained PROMPT.md, codex.log, run.pid. Governor: status warn,
mode owner_away_open, CPU saturated. No heavy computation is planned.

Web searches (using the web search tool):

- `fully trained two layer neural network proportional regime double descent rigorous asymptotic generalization 2025 2026`
- `two layer neural networks proportional regime gradient descent exact asymptotics feature learning double descent theorem`

Initial leads: one/few-step feature-learning results (2024), and a 2025 Bayesian
proportional-limit result. These need opening and checking; search snippets alone
do not establish that the GD-to-convergence problem has been solved.

## 2. Literature check finished; concrete choice (18:12 UTC)

Search elapsed: approximately four minutes, below the ten-minute limit. Further
queries included `"two-layer" "proportional" "convergence" "2026" generalization`,
`"double descent" "fully trained" rigorous neural networks 2025 2026`,
`"two-layer" "proportional" "long-time" neural networks generalization`, and
`"two-layer" "proportional" "gradient descent" deterministic equivalent convergence generalization 2025 2026`.

Opened primary sources (author spellings copied from the opened pages):

- Hugo Cui, Luca Pesce, Yatin Dandi, Florent Krzakala, Yue M. Lu, Lenka Zdeborová,
  Bruno Loureiro, *Asymptotics of feature learning in two-layer networks after one
  gradient-step*, [arXiv:2402.04980](https://arxiv.org/abs/2402.04980).
  Exact asymptotics for a spiked random-features surrogate following one step;
  not both-layer GD to convergence.
- Yatin Dandi, Florent Krzakala, Bruno Loureiro, Luca Pesce, Ludovic Stephan,
  *How Two-Layer Neural Networks Learn, One (Giant) Step at a Time*,
  [JMLR 25(349), 2024](https://www.jmlr.org/papers/v25/23-1543.html).
  Finitely many large feature-learning steps; not the requested limiting curve.
- Francesco Camilli, Daria Tieplova, Eleonora Bergamin, Jean Barbier,
  *Information-theoretic reduction of deep neural networks to linear models in
  the overparametrized proportional regime*,
  [arXiv:2505.03577](https://arxiv.org/abs/2505.03577).
  Rigorous proportional-limit Bayes-optimal inference, not GD selection.
- Qiyang Han, Masaaki Imaizumi, *Precise gradient descent training dynamics for
  finite-width multi-layer neural networks*,
  [arXiv:2505.04898](https://arxiv.org/abs/2505.04898).
  Precise iterates, but hidden width stays bounded; does not settle p/n positive.
- Andrea Montanari, Zihao Wang, *Phase Transitions for Feature Learning in Neural
  Networks*, [arXiv:2602.01434](https://arxiv.org/abs/2602.01434).
  Feature-learning threshold with hidden width fixed, not the three-way limit.
- Vittorio Erba, Emanuele Troiani, Lenka Zdeborová, Florent Krzakala,
  *The Nuclear Route: Sharp Asymptotics of ERM in Overparameterized Quadratic
  Networks*, [arXiv:2505.17958](https://arxiv.org/abs/2505.17958).
  Quadratic-activation regularized global ERM via convex matrix sensing; does not
  by itself identify both-layer GD's converged predictor in the stated setting.
- Gérard Ben Arous, Murat A. Erdogdu, Nuri Mert Vural, Denny Wu,
  *Learning quadratic neural networks in high dimensions: SGD dynamics and
  scaling laws*, [arXiv:2508.03688](https://arxiv.org/abs/2508.03688).
  Population and online SGD, not a fixed reused sample trained to interpolation.
- Stephen Y Zhang, Gabriel Peyré, *Global Exponential Convergence of Two-Layer
  Linear Network Training*, [arXiv:2610.09356](https://arxiv.org/abs/2610.09356).
  Global factor optimization for linear networks, not a nonlinear-network test
  error curve. This makes any claim of new general linear optimization theory
  inappropriate here.
- Jimmy Ba, Murat A. Erdogdu, Taiji Suzuki, Denny Wu, Tianzong Zhang,
  *Generalization of Two-Layer Neural Networks: An Asymptotic Viewpoint*,
  [ICLR 2020 paper](https://www.cs.toronto.edu/~erdogdu/papers/gen-twolayers.pdf).
  Its abstract explicitly trains either the first or the second layer.

Also opened the publisher page for *Statistical Physics of Deep Learning:
Optimal Learning of a Multilayer Perceptron near Interpolation*,
https://journals.aps.org/prx/abstract/10.1103/56sb-pdh6; it explicitly concerns
Bayes-optimal error. No claim from it is needed below.

Conclusion of bounded search: no solution of the full stated problem located.
This is not a certified exhaustive literature result. The important recent
advances above have different widths, inference rules, activations, or training
protocols. No SOLVED_ELSEWHERE.md is warranted on this evidence.

**Chosen piece, before doing it:** a fully proved linear-activation benchmark
for simultaneous, discrete, constant-step GD on both layers. Initialize the
first layer at zero and the second layer at any fixed unit vector. Prove global
convergence for an explicit sufficiently small, data-dependent constant step;
identify the selected predictor as minimum-norm least squares; derive its exact
finite-sample noise-risk distribution, its off-critical proportional limit,
and its fixed-gap critical distribution. Width p should disappear exactly.

Why this piece: it addresses the actual optimization-to-convergence issue in
an auditable special case and isolates a qualification needed in the question:
at zero ridge a finite deterministic limit at the interpolation boundary need
not exist, and even a natural rescaling can retain randomness. The regression
laws are classical; no claim of new OLS theory or a nonlinear solution is made.

Read-only memory orientation used brain_startup.md and the identity,
relationship, writing, and T267 lazy-double-descent cards. The T267 card warns
against treating a lazy/kernel calculation as full feature learning; that
distinction is enforced here. No recall command was run because it writes logs
outside the allowed folder.

## 3. Proof written (18:14 UTC, approximate)

Created PROOF.md. It contains an explicit small-step convergence argument for
ordinary simultaneous discrete GD, not just gradient flow, followed by an
elementary inverse-Gram identity and exact risk laws. The optimization argument
uses a decreasing discrete imbalance K, with its total decrease controlled by
loss descent; it does not assume the continuous-time imbalance is conserved.

The proposed laws are noise risk = sigma^2 chi-square(min(n,d)) /
chi-square(|n-d|+1), a deterministic off-critical proportional limit, and
R/n => sigma^2 / chi-square(k+1) for fixed gap |n-d|=k. The next step is
independent algebraic and numerical checks, particularly of the +1 in the
denominator degrees of freedom and all constants in the GD induction.

All edits so far used apply_patch within this folder. No scientific computation
has run yet. The proof is the primary result; numerical checks will be small
and supplementary.

## 4. Numerical audit (18:16 UTC)

Exact command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 validate.py > validation_stdout.txt 2>&1
```

Exit status: 0. Output is saved verbatim in validation_stdout.txt, and the full
diagnostics are in validation.json. The 6,000 raw Gaussian-design risk samples
are in risk_samples.csv.

The launcher printed `nice: setpriority: Operation not permitted` but continued
to run the script. This was unexpected: the requested priority was not verified
before the first run. Do not treat that run as verified priority-compliant.
There will be no further numerical run without a priority guard. Peak RSS was
89.52 MiB and elapsed time 1.197 seconds, with numerical thread variables all 1.

NumPy emitted divide-by-zero, overflow, and invalid-value warnings on the first
controlled matrix multiplication at validate.py:38. The subsequent finite
outputs, convergence assertions, independent finite-difference checks and QR/SVD
checks passed. The source of these warnings is not established; they are a
limitation of the numerical audit and are retained in the output, not hidden.
No proof step depends on these numerical tests.

Complete captured output:

```text
nice: setpriority: Operation not permitted
~/codex_op_1114/briefs/T266/validate.py:38: RuntimeWarning: divide by zero encountered in matmul
  A = (u * np.linspace(1.0, 2.0, rank)) @ v.T
~/codex_op_1114/briefs/T266/validate.py:38: RuntimeWarning: overflow encountered in matmul
  A = (u * np.linspace(1.0, 2.0, rank)) @ v.T
~/codex_op_1114/briefs/T266/validate.py:38: RuntimeWarning: invalid value encountered in matmul
  A = (u * np.linspace(1.0, 2.0, rank)) @ v.T
PASS: full two-layer GD, reduced GD, predictor recurrence, and finite differences
GD n=18 d=8 widths=1,3,11 max_error=9.9e-10 width_difference=2.5e-16
GD n=8 d=18 widths=1,3,11 max_error=9.91e-10 width_difference=1.18e-15
GD n=12 d=12 widths=1,3,11 max_error=9.85e-10 width_difference=2.19e-16
RISK n=24 d=12 df=(12,13) KS=0.02158 p=0.62344
RISK n=16 d=16 df=(16,1) KS=0.02309 p=0.53643
RISK n=12 d=24 df=(12,13) KS=0.01765 p=0.84241
RISK n=24 d=23 df=(23,2) KS=0.01802 p=0.82376
RISK n=23 d=24 df=(23,2) KS=0.02802 p=0.29720
CRITICAL inverse-chi-square(1) quantiles: q10=0.369611509, q50=2.198109338, q90=63.328117677
Peak RSS: 89.52 MiB
Elapsed: 1.197 seconds
Data: validation.json, risk_samples.csv
```

Interpretation: the statistics are diagnostics, not proofs. Critical sample
means have no population mean when nu <= 2 and must not be used as estimates
of a finite risk expectation. The saved JSON uses null for the infinite exact
mean rather than a nonstandard JSON infinity.

## 5. Independent audit and attempted counterexamples (18:19 UTC, approximate)

Re-derived every formula used for the conclusion:

1. **Factor gradients and discrete dynamics.** In addition to the scalar
   reduction, expanded the full matrix update directly:
   beta_next = beta - eta (||a||^2 I + W^T W) g
   + eta^2 (beta^T g) g. The script checks this independently of the scalar
   code. Maximum matrix-recurrence error was below 2e-16. Off-trajectory central
   finite differences checked both layer gradients (errors below 1.8e-10).
2. **Discrete imbalance.** In the full matrices,
   K_next-K = eta^2 (||Wg||^2-||a||^2 ||g||^2); on the rank-one trajectory
   this becomes equation (7). The first-order terms cancel exactly. It is not
   conserved in discrete time. Numerical identity errors were below 7e-16.
   In the proof, total imbalance loss is bounded by 2 eta L0; the induction
   supplies K>3/4 before it is used to obtain the PL contraction. The Hessian
   bound applies along the entire prospective step, not just at its endpoint.
3. **Selection of the interpolant.** Bounded loss alone does not select minimum
   norm. The missing ingredient would be row-space invariance, which holds
   because W0=0 and every first-layer gradient lies in range(X^T). This is why
   the result cannot be silently extended to generic W0. The numerical
   solutions agree with independent SVD least squares to within 1e-9.
4. **Exact distribution and the +1.** A second derivation integrates the
   Gaussian conditional density and changes variables Y=Z(I+vv^T)^(1/2).
   Its determinant and Jacobian yield radial density
   t^(r/2-1)(1+t)^(-(m+1)/2), giving denominator df m-r+1 independently
   of the Schur-complement argument. This is written in PROOF.md section 5.
5. **Square boundary.** A third derivation uses the uniform null line of the
   augmented Gaussian matrix [X, epsilon/sigma]. It gives U_n/V_1 directly.
   The inverse-chi-square CDF is independently erfc(1/sqrt(2t)), and normal
   quantiles give the three printed critical quantiles. The script checked
   these against the chi-square survival function.
6. **Finite expectation and magnitude.** The inverse-chi-square density
   integral gives 1/(nu-2); a separate beta-integral calculation from the
   radial density gives r/(nu-2). For (n,d)=(24,12) and (12,24), the noise
   mean is exactly 12/11, agreeing in magnitude with the diagnostics. At
   gaps 0 and 1, the expectation diverges: the large saved sample means are
   not evidence of a finite deterministic peak.
7. **Signal and noise.** Orthogonality of row space and nullspace, rather than
   a presumed bias/noise independence, proves additivity of risk. Gaussian
   rotational symmetry gives the bias projection law. The proof asserts no
   joint independence of bias and noise.

Cases tested against the argument: y=0 (stationary zero predictor), nonzero
y orthogonal to the column space (also minimum-norm zero), rank-deficient
nonzero deterministic X (use its smallest positive singular value), d<n,
d=n, d>n, gaps 0 and 1 (infinite expectation), sigma=0 (no noisy peak),
and fixed versus diverging sublinear dimension gap. The last case yields
equation (19): (|d-n|/n) R -> sigma^2 when the gap diverges but its ratio
to n vanishes. There is no dimension-uniform iteration bound or exchange of
limits in the argument.

The original audit script is archived byte-for-byte in
validation_run_source.txt. After the launcher's priority failure, validate.py
was changed to verify os.getpriority >= 15 *before importing numerical
libraries* and refuse otherwise. Floating-point divide/overflow/invalid
warnings now raise exceptions. The guarded revision has not been run; no
further numerical work was attempted. The original data and output are left
unchanged, including the warnings. A first combined apply_patch for these
edits failed on an unmatched context line; the subsequent narrower patch
succeeded. Read-only inspection commands `cat validation_stdout.txt`,
`cat validation.json`, and `wc -l PROOF.md LOG.md validate.py` confirmed the
saved diagnostics; `nice` without an argument only printed its usage.

## 6. Final read-through and report (18:22 UTC, approximate)

Created REPORT.md with the required VERDICT first line, exact scope and formulas,
commands, execution limitations, and a concrete next problem. Read back the
priority guard with `sed -n '1,75p' validate.py`, the central and independent
proof sections with `sed`, and all of REPORT.md with `cat`; `ls -lh` confirmed
the expected artifacts. Total raw numerical data is 456 KiB. The priority
guard appears exactly once and runs before NumPy/SciPy import.

Final mathematical corrections: explicitly retained the bounded-signal
assumption for the fixed-gap assertion, covered zero-signal subsequences in
the bias limit, and removed a harmless extra TeX spacing escape. No result
depends on a finite critical mean or on bias/noise independence. The general
nonlinear, generically initialized problem remains unresolved by this work.

No further scientific computation was run after the launcher priority failure.
No files outside this folder were edited, no git commands were used, and no
subagents, GPU, torch, or MLX were used.

Task completed: “push this problem forward by one checkable piece” — received
approximately 22:08 Asia/Tbilisi, 14 Nov 2026.
