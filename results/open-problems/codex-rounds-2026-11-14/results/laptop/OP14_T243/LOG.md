# T243 working log

## 2026-11-14 — initial checks

Scope: all writes remain in this folder; no git, uploads, messages, GPU, torch, or training. Child computations use one thread, BelowNormal priority, and small bounded workloads. The current task's local-only rule overrides the machine-wide archival instructions.

Read ~/AGENTS.md (streamed by PowerShell); inspected the folder, initially containing PROMPT.md, NOHOOKS, and codex.log. Started the prescribed math recall with three explicit thread limits and PYTHONDONTWRITEBYTECODE=1.

Literature search started with web search queries `Gaussian process neural networks functional convergence sup norm rates 2025 2026` and `wide neural networks Gaussian approximation functional Wasserstein optimal rates Trevisan 2024 2025`.

Opened actual arXiv pages and the October paper's full HTML:
- Luis Wiederhold, Nil Ayday, Debarghya Ghoshdastidar, *Lifting Finite-Sample Gaussian Approximation of Wide Neural Networks to Functional Convergence*, arXiv:2610.18166, 13 Oct 2026. Claims a supremum-norm W2 upper bound of order width^(-1/2) for polynomial activations. Its precise restrictions are being checked. This is not a solution of the full stated problem.
- Lucia Celli, Giovanni Peccati, *Entropic bounds for conditionally Gaussian vectors and applications to neural networks*, arXiv:2504.08335, revised 3 Jun 2025. Abstract concerns finitely many inputs, invertible limiting covariance, and total variation/W2, including derivatives.
- Dario Trevisan, *Wide Deep Neural Networks with Gaussian Weights are Very Close to Gaussian Processes*, arXiv:2312.11737. Abstract states inverse-width finite-input rates under nondegeneracy.

Sources: https://arxiv.org/abs/2610.18166 ; https://arxiv.org/html/2610.18166v1 ; https://arxiv.org/abs/2504.08335 ; https://arxiv.org/abs/2312.11737 .

No claim that the general problem is solved. Literature search is limited to ten minutes.

## Literature scope checked; concrete piece chosen

Read Theorem 2, Corollary 1, and Section 4 of arXiv:2610.18166v1. The result is for one hidden layer and polynomial activations, via a finite-rank kernel condition. Section 4 expressly leaves sharpness open (upper width^(-1/2), scalar lower width^(-1)) and leaves deeper nonlinear networks untreated. Polynomials of degree >1 also fall outside globally Lipschitz activations. The whole problem remains unsettled. The abstract of arXiv:2306.16308v2, by Krishnakumar Balasubramanian, Larry Goldstein, Nathan Ross, Adil Salim, was also opened: it already gives functional sup-norm W1 bounds on spheres for arbitrary depth; functional quantitative bounds are not wholly absent.

Choice, before doing the proof: analyze a bias-free ReLU network on one positive input ray, with all weight variances 2/fan-in and h hidden layers of width n. Positive homogeneity makes the entire random field rank one. Its coefficient is an exact centered Gaussian variance mixture, with variance multiplier a product of h independent empirical means of 2(G_+)^2. Prove an explicit all-depth total-variation bound on C(K), and a matching inverse-width smooth-test asymptotic with depth coefficient. This is a genuine, restricted functional special case, not a solution for general K or general activations. The exact product moments allow independent arithmetic and depth audits without training or large simulations. Try additionally to close the W2 rate in this special case if a complete argument is available.

## Proof draft saved

Saved PROOF.md and SOLVED_ELSEWHERE.md. The W2 argument closes as well: truncate the random variance to [3/4,5/4], integrate the Gaussian chi-square kernel exactly as (1-(v-1)(w-1))^(-1/2), use cancellation of the first variance fluctuation, and prove the required one-dimensional entropy/transport inequality by the increasing quantile map. The truncation cost is controlled by the fourth centered variance moment. The claimed bound is W2/A <=4 sqrt(D4)+64D4+sqrt(2)D2. An explicit twice-differentiated polynomial bound gives D4 <=1679 exp(33h/n)(h/n)^2 for n>=100. Thus W2 and TV both have order h/n when h/n->0. The smooth cosine gap has coefficient 5 exp(-1/2)/8. These statements are now drafts pending independent checks.

An additional math recall used the wordings `Gaussian variance mixture Wasserstein fourth moment` and `deep ReLU network product chi square variance depth`. Awaiting its running command; do not restart it. The helper's source documents a read-only store and a co-use logging switch; any further recall will set MATH_STRENGTH_NOLOG=1 to respect local-only writes.

## Independent verification script saved

Created verify.py using only the standard library. It sets BelowNormal priority and one-thread environment variables, has a two-minute internal work budget, and uses small arrays of rational/decimal numbers. Independent paths: set partitions for single-layer raw moments; centered-product recurrence for D2 and D4; direct polynomial expansion for the 75h^2/n^2 fourth-moment coefficient; closed one-layer Laplace transform for the cosine constant; Simpson integration for the Gaussian overlap kernel. No network training and no Monte Carlo. Data will be saved as verification.json and exact console output as verification_output.txt.

The second recall completed. Relevant leads concerned the per-layer ReLU variance constant 5 and known depth/width fluctuation laws, but no returned card proved the functional transport statement. These are reference leads only; PROOF.md derives all needed formulas directly.

## Verification run: passed

Exact command (PowerShell, in this folder):

```powershell
$p = Get-Process -Id $PID; $p.PriorityClass = 'BelowNormal'; $env:OMP_NUM_THREADS='1'; $env:OPENBLAS_NUM_THREADS='1'; $env:MKL_NUM_THREADS='1'; $env:NUMEXPR_NUM_THREADS='1'; $env:PYTHONDONTWRITEBYTECODE='1'; python -B verify.py
```

Exit code 0. Exact output (also in verification_output.txt):

```text
PASS exact rational moments: set partitions vs formulas (30 comparisons)
PASS product centered moments: independent recursion vs powers (24 cases)
PASS independent polynomial expansion: D4 leading coefficient 75*h^2 (h=1..8)
PASS derivative-bound arithmetic: 2470 + 888 = 3358; half = 1679
PASS depth-bound grid: 21 cases, including h=n and n=1000000
PASS one-layer exact Laplace transform vs Taylor remainder (6 widths)
cosine coefficient target = 0.379081662320396
n*gap at n=1000000 = 0.379081224797536
PASS Gaussian overlap: independent Simpson integral (5 pairs), max error 9.55e-15
PASS chi-square Taylor bound on 2001 grid points in [-1/16,1/16]
PASS n=1 atom check: exact mass 1/2; characteristic gap matches mixture formula
ALL CHECKS PASSED; data saved to verification.json
```

The exact-moment checks are algebraic; quadrature and inequality grids are diagnostics, not substitutes for the analytic proofs. The memory walk corroborated the per-layer constant 5 and pointed to an existing T243 two-input result. Checking that card before claiming any new progress; no priority claim is warranted.

## Memory comparison and second depth lower bound

Walked full cards claim_8b8cb74167054ddd823469b38943cd72, claim_ed96b3e723764408b36e5b036c5caf92, and claim_7b39a894875346a5a41ce91646547385, using MATH_STRENGTH_NOLOG=1. The existing T243 card records the homogeneous one-input product law, a merging-input identity, and numerical smooth-test gaps. Thus the product representation is established prior work, not this session's novelty. The present deliverable supplies a self-contained explicit functional W2 transport bound, TV bound, and a uniform h=o(n) sharp-order theorem; it does not claim global literature priority.

Added an independent depth lower bound to the same special case: W2/A >=sqrt(2/pi)(1-exp(-h/(3n))) for n>=100. Proof uses the deficit of E sqrt(B), not the cosine expansion: truncate B at 2, retain at least 4/n of its variance, and use the exact identity 1-E sqrt(B)=E(sqrt(B)-1)^2/2. Together with the upper bound this gives W2 convergence exactly when h/n->0. This addition needs only the already independently verified moments, but its scalar inequalities will also be checked in the script.

## Final verification and audit

Reran the same exact verification command after adding the independent depth lower-bound check. Exit 0; all the earlier output was unchanged and the additional line was:

```text
PASS independent depth lower bound: variance truncation constants (4 widths)
```

The updated full output is in verification_output.txt and updated data in verification.json. Saved AUDIT.md with explicit failure-case checks: width-one atom, extinction probability 1-(1-2^(-n))^h, mean error introduced by clipping, signs in the overlap kernel, entropy boundary terms, uniform growing-depth control, zero input, both signs excluded, and exact functional/scalar support identification.

Saved REPORT.md with the restricted proved verdict, commands, limitations, earlier-memory overlap, and the remaining infinite-rank kernel obstruction. No test failed. No claim that the full problem or the literature-priority question is settled. All task artifacts remain in this folder.

Final data readback: verification.json reports elapsed_seconds=0.4978850999614224 for the final verification workload. The saved JSON, console output, proof, audit, and literature note were present on disk. The script's small rational and decimal tables occupy only kilobytes; no large-memory dependency is imported.
