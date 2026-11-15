# T263 working log

## 2026-11-14: scope and setup

- Read the session brief, inspected the working folder (initially PROMPT.md, NOHOOKS and codex.log), and read ~/AGENTS.md and the memory index.
- The session-specific restriction overrides shared writeback rules: all artifacts stay in this folder; no git, uploads, external messages, training, GPU, or accounts.
- Shell commands use OMP_NUM_THREADS=1 and BelowNormal priority for substantive programs. Computations will be small, analytic checks only.
- Literature search started at approximately 17:10 UTC, with a ten-minute maximum. Queries: `two layer ReLU gradient descent tight generalization matching lower bound Gaussian mixture 2025 2026`; `two layer neural network gradient descent sharp asymptotics generalization teacher student feature learning 2025 2026`.
- Search returned potentially relevant ICLR 2026 papers on mixtures and a JMLR 2026 paper. Search snippets alone are not evidence; opening the originals next.

## Literature check and choice (before starting the proof)

- Opened Ichiro Hashimoto, *Directional Convergence, Benign Overfitting of Gradient Descent in leaky ReLU two-layer Neural Networks*, arXiv:2505.16204v3 (10 February 2026), especially Theorems 5.1 and 6.2: https://arxiv.org/html/2505.16204v3 . The Gaussian error is between normal tails with constant multiples of a signal-to-noise argument. This is strong progress, but does not itself give a bounded ratio of upper and lower errors when that argument diverges.
- Opened Alex Buna, Shirley Xiaoqi Liu and Patrick Rebeschini, *Minimax Optimal Early-Stopped Gradient Descent for Gaussian Mixture Classification*, arXiv:2608.06250v2 (8 November 2026): https://arxiv.org/abs/2608.06250 . It treats early-stopped linear GD with label noise, rather than interpolating nonlinear network GD.
- Opened Yunwen Lei, Puyu Wang, Yiming Ying and Ding-Xuan Zhou, *Optimization and Generalization of Gradient Descent for Shallow ReLU Networks with Minimal Width*, JMLR 27(34), 2026: https://www.jmlr.org/papers/v27/24-2030.html . The abstract states an almost optimal NTK-margin bound; it does not settle constant-factor n,d tightness as requested.
- Opened Niclas Göring, Shuofeng Zhang, Branton DeMoss and Ard A. Louis, *Escaping Parameter Space: Tight Generalization Bounds via Representation Quality*, arXiv:2610.23729: https://arxiv.org/html/2610.23729v1 . Its certificates are numerical, with stability empirically certified; no matching n,d rate theorem is stated there.
- Two OpenReview PDF opens hit browser verification. Used the accessible arXiv original for Hashimoto instead. No conclusion relies on blocked pages or secondary summaries.
- No complete solution was identified in the bounded check. This is not a claim of exhaustive literature coverage. No SOLVED_ELSEWHERE.md is warranted.
- CHOICE: prove an exact Gaussian-mixture risk reduction for a nonlinear four-ReLU family, and the sharp precision criterion that converts effective margins into constant-factor test-error bounds. Include a counterexample showing that an exactly correct odd component plus a vanishing even component need not give constant-factor Bayes risk. This targets the concrete gap exposed by the tail sandwiches. It is an algorithm-independent reduction; it will not be presented as a GD convergence theorem or a solution of T263.
- Why this piece: it is finite and checkable, has exact formulas that can be independently integrated, and specifies the accuracy a future analysis of the trained network must achieve. It avoids calling exponent-tightness constant-factor error-tightness.

## Proof completed; independent checks next

- Wrote PROOF.md. Main identity: for balanced X=Y mu+N(0,Sigma), R(u.x+|v.x|)=(Q(rho_+)+Q(rho_-))/2, without requiring u,v to be orthogonal. It is conditional on the training sample if u,v are data-dependent.
- Derived the Gaussian-tail precision criterion twice algebraically: integrated hazard bounds from Mills inequalities, and the direct squared-margin gap D=r^2 b^2/(1+b^2) for the explicit example. A numerical integral of the actual ReLU score will provide another independent check.
- Exact example f_b(x)=x_1+b|x_2|, mu=r e_1: R=Q(r/sqrt(1+b^2)), E[even(X)^2]=b^2. Constant-factor Bayes risk as r grows holds exactly when rb remains bounded. With rb->c the error ratio tends to exp(c^2/2).
- Scope remains a reduction and obstruction, not a claim about any actual unconstrained GD trajectory. No simulation or network training will be run.
- The shared math recall script was inspected before use: it logs co-use outside this folder and can build shared caches. Checking its switches so a read can respect the session's stricter no-outside-writes and memory constraints.

## First numerical run failed; investigating

- Exact command: `$env:OMP_NUM_THREADS='1'; $env:OPENBLAS_NUM_THREADS='1'; $env:MKL_NUM_THREADS='1'; [System.Diagnostics.Process]::GetCurrentProcess().PriorityClass='BelowNormal'; python -B verify_reduction.py`.
- Result: exit 1, `ArithmeticError: Quadrature failed to reach tolerance`. No successful numerical validation is claimed from that run. Added case labels, partial CSV saves and interval diagnostics to identify the cause before changing the method or tolerance.
- Added recall_readonly.py: calls the prescribed math_recall.py with three wordings, no semantic encoder or subprocesses, co-use logging disabled, a Windows 768 MiB process-memory cap, one-CPU affinity and a Python audit guard against outside writes. Its output is saved locally in recall_output.txt. This is a read of the existing store, not a memory writeback.

## Numerical failure diagnosed

- The diagnostic run passed the orthogonal case and stopped on the correlated case. Output saved in verification_output.txt: interval [-0.44721364974975586,-0.44721341133117676], Simpson difference -5.316546156693751e-16 versus local tolerance 2.9802322387695314e-18.
- This interval contains z_2=-0.4/sqrt(0.8), where X_2=0 for one class and the piecewise linear decision boundary has a cusp. Fixed the integration domain by splitting at the two explicit cusp locations before adaptive integration; did not relax the requested global tolerance. The first successful case is already saved in risk_identity_checks.csv.
- The literature search ended before the proof choice, at about 17:16 UTC, within ten minutes of starting. No additional literature searching is being done during the proof/check phase.

## Successful independent numerical verification

- Exact successful command (PowerShell):

  `$env:OMP_NUM_THREADS='1'; [System.Diagnostics.Process]::GetCurrentProcess().PriorityClass='BelowNormal'; python -B verify_reduction.py *> verification_output.txt; $verifyExit = $LASTEXITCODE; Get-Content -LiteralPath verification_output.txt; exit $verifyExit`

- Exit code: 0. Main output:

  ```json
  {
    "risk_cases": 9,
    "tail_inequality_cases": 28,
    "threshold_rows": 15,
    "degenerate_rejected": true,
    "max_relative_error": 2.8266278206956486e-13,
    "max_refined_relative_error": 6.661338147750939e-15,
    "runtime_seconds": 18.997883900010493,
    "threads": "one; stdlib only",
    "priority": "BelowNormal on Windows"
  }
  r=32 critical_c1: risk_ratio=1.648720099
  r=32 critical_c2: risk_ratio=7.346054915
  r=32 vanishing_L2_failure: risk_ratio=5556655.615
  ```

- Data: risk_identity_checks.csv, tail_inequality_checks.csv, contamination_threshold.csv; metadata: verification_summary.json. The risk checks integrate the original four-ReLU score after conditioning on one Gaussian coordinate, with 320 panels and then 640 panels and tighter tolerance. They do not substitute the proposed risk formula into the integrand.
- The cases include correlated covariance, nonorthogonal u,v, opposite margin signs, reversed u, zero v, zero signal, zero u, parallel vectors and a rare-error case. The excluded u=v degeneracy is explicitly rejected. Numeric quadrature is a sanity check, not a rigorous interval computation; the exact proof is independent of these approximate numbers.

## Recall outcome and final proof audit

- Exact recall command: `$env:OMP_NUM_THREADS='1'; [System.Diagnostics.Process]::GetCurrentProcess().PriorityClass='BelowNormal'; python -B recall_readonly.py *> recall_output.txt; $recallExit = $LASTEXITCODE; Get-Content -LiteralPath recall_output.txt; exit $recallExit`.
- Recall exited 1: the fast cache allocation hit MemoryError, then the fallback also hit MemoryError while constructing the title map. The Windows process-memory limit was 768 MiB, below the author's 1 GB ceiling. Did not retry with a larger limit; no useful card was returned. No shared files were edited.
- Read relevant entries in the shared MISTAKES.md by rg. Relevant warnings include: conditional bounds do not multiply without an independence argument; passing checks is not itself a proof; and never project completion across a known open step. The conditional independence in the signed-score derivation is proved explicitly, and the missing GD step remains open.
- Wrote AUDIT.md. Reproved both constants in the tail comparison using direct changes of variables instead of the hazard argument. Checked imbalance, biases, a general even sum, zero branch vectors, negative margins, singular covariance, rare-error precision, sample conditioning, and the distinction between high probability and expected risk.
- Updated REPORT.md with the exact result, verification outputs, failed attempts, uncertainty and the next mathematical step. Verdict is PARTIAL because the bridge to the trained network is not proved.
- Final readback checked REPORT.md, verification_summary.json and the file inventory. All required deliverables and three CSV data files are present. The final report matches the saved successful run; no checks were rerun after the final documentation-only edits. All work stayed in this folder.
