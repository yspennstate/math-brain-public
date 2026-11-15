# T427 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First clock read: 15 November 2026, 03:52:56 Asia/Tbilisi (14 November 2026, 23:52:56 UTC).

## Orientation and earlier files

Read the earlier REPORT.md, LOG.md, SOLVED_ELSEWHERE.md and directory listing at ~/codex_op_1114/briefs/T427. There is no PROOF.md and there are no mathematical scripts there. The earlier result is a statement/normalization audit of Yunzong Xu's arXiv:2610.40509v1, not a new proof.

Read ~/.claude/brain_startup.md and ~/.claude/compute/compute_state.json. Governor: warn, owner_away_open, CPU saturated. No heavy calculation planned. The task's folder-only rule precludes global checklist, mesh, recall logging and brain writes; those commands are not run. No git or subagents.

Commands: initial read-only `pwd` and `rg --files ...`; then `OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c 'date ...; cat ...'` to read the startup, compute state and earlier files. The environment printed `nice: setpriority: Operation not permitted` and nevertheless ran these small reads. Subsequent numerical programs must check their actual niceness before computing and refuse to run if it is below 15.

## Literature check started 03:52:56 +04

Web search queries: `"2610.40509"`; `random matching second order constant Yunzong Xu 2026`. Opened https://arxiv.org/abs/2610.40509 and https://arxiv.org/html/2610.40509v1. The arXiv record still lists the 29 October 2026 preprint by Yunzong Xu, *Random Matching Between Distinct Distributions in Two Dimensions*. This confirms the earlier source exists; it is not a newly discovered resolution beyond that report. Checking the statements and version history next, within the five-minute literature budget.

## 03:53 +04 — earlier claim re-derived

The equal-weight clause of Theorem 4 has coefficient 1/(4 pi), with its own constant kappa_equal. Proposition 3.1 has chi_n=1 for equal weights. At t=n^(-5/6), the two logarithms are log(nt) and log(2/t), whose sum is log n + log 2. The errors are O(n^(-1/120) log(en)), O(n^(-1/12)(log n)^(3/2)), and O(n^(-5/12)); all tend to zero. Therefore the earlier statement-level deduction c_square=kappa_equal+log(2)/(4 pi)+h_Q holds. This does not independently certify the subdivision proof.

Source locations opened: Proposition 3.1, equations (3.3)–(3.4), Theorem 4, Corollary 2, and Appendix B.4.2. Separately reconstructed the spectrum by cosine separation: pi^2(k^2+l^2), ordered nonnegative k,l, excluding zero. Boundary and equal-weight conventions agree with the earlier report.

Additional search queries: `"2610.40509" constant semidiscrete correction`; `"random matching" "semidiscrete" "constant" "2026"`. A new search result arXiv:2611.17066 concerns boundary conditions and is being checked before ending the five-minute search. No later version of Xu's preprint appears in its arXiv history.

Read-only orientation also read the first 100 lines of brain-views/RELATED.md, without modifying the brain. No matching-specific card appeared there.

## Literature check closed; extension selected

Opened arXiv:2611.17066v1, Martin Huesmann and Arthur Wachtel, *Asymptotic transportation cost of the optimal matching subject to different boundary conditions* (12 November 2026), abstract and introduction. Its high-resolution theorem is in dimension at least three and does not evaluate the two-dimensional logarithmic finite part. Also reopened arXiv:2609.08717v2, Victor Armegioiu, Michael Goldman, Francesco Grotto, Dario Trevisan, *Exact Asymptotics for the 2D Euclidean Random Matching Problem*: its abstract is about first-order asymptotics. Neither changes the earlier status. Search finished within three minutes of the initial clock read; no further literature search is needed.

Chosen ONE extension: evaluate the deterministic square spectral finite part h_Q in an explicit rapidly convergent series, with a proved truncation error and an independent normalization check. This replaces the unevaluated geometric limit in the earlier report by a directly computable expression. It does not evaluate the universal equal-mass constant and does not claim a new proof of the matching theorem. This is preferable to an unchecked simulation or an incomplete audit of the whole subdivision argument. The prior report's suggested full proof audit remains outstanding.

Planned method: use the Neumann cosine spectrum and Gaussian Poisson summation to integrate the heat trace after subtracting its area singularity. Obtain a positive, exponentially convergent lattice series in elementary functions and the exponential integral E1. Independently recover the same finite part from the meromorphic spectral zeta function. All estimates will be analytic; if the required process priority cannot be set, leave a guarded verification script rather than run numerical work at normal priority.

## Explicit formula proved and saved

Wrote PROOF.md. The main result is h_Q=lim_M H_M, where H_M is an explicit finite sum of E1, elementary exponentials and A(a)=integral_1^infinity w^(-3/2)e^(-aw)dw. The error is nonnegative and at most

`4 exp(-pi (M+1)^2) / [pi^2 (M+1)^2 (1-exp(-pi))(1-exp(-pi(2M+3)))]`.

The proof integrates the exact theta heat trace, splits at v=1 after v=pi u, and applies Gaussian Poisson summation below 1. The elementary integrated contribution is 1-log(pi), not a guessed constant. The M=3 error is <10^(-21), checked entirely by rational inequalities: pi>3, exp(3)>20 from the degree-8 exponential partial sum 806769/40320>20, and 20^16=655360000000000000000.

Independent audit: a Mellin continuation of the spectral zeta function gives its Laurent finite part B=h_Q+gamma/(4 pi), recovering the same heat convention. A separate quadrant/sign count gives h_Q-h_T=1/6+log(2)/(2 pi), agreeing with Appendix B.4.2. No periodic multiplicity is substituted for the square spectrum. No numerical value of beta_sd or c_square is claimed.

Also inspected Appendix C.2 and C.4 of Xu's paper. For equal weights, the covariance factor is exactly 1; the delete-one convex mixture has coefficients 1/(n+1), and the fixed-time monotonicity argument applies directly. This is a check of two equal-mass steps, not an audit of the boundary-repair lemma or the full proof.

## Guarded numerical verification succeeded

Added verify_spectral.py. It checks actual niceness and OMP_NUM_THREADS before importing numerical libraries; imposes a 90-second CPU limit; uses 85-digit mpmath arithmetic and small finite sums on one thread; writes no files. No numerical library installation was needed. Added an independent original-spectrum approximation C_N(t) and its analytic error bound to PROOF.md, equation (20).

Exact command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_spectral.py
```

Exit code: 0. Tool wall time: below 0.2 seconds. Output:

```text
nice: setpriority: Operation not permitted
niceness=20; working precision=85 decimal digits
H_3 = 0.00402223657274227817226979469888942273631817106447912374611657
H_3 analytic tail bound = 3.91564898356e-24
H_5 = 0.00402223657274227817227364756500595607753013990163588814077047
H_5 analytic tail bound = 8.97623383875e-52
Corrected direct heat sum = 0.00402223657274227817227364756500595607753013976370315602635916
Direct heat analytic error bound = 1.39401977209e-46
PASS: positive-series formula and direct heat sum agree.
This is a numerical check, not interval-arithmetic certification.
```

The apparent priority failure was not a blocker: the process was already at niceness 20, more restrictive than the requested 15. The numerical guard verified this before computing. Earlier read-only wrapper errors therefore do not imply normal-priority computation. Numerical lists contain fewer than 2000 small arbitrary-precision numbers; no large array, parallel worker, GPU, MLX or torch is used. The calculation has a very small memory footprint relative to 1 GB, though peak RSS was not instrumented.

The independently corrected direct heat sum agrees with H_5 to within the sum of the proved analytic errors. The decimal h_Q approximately 0.004022236572742278 is checked by both formulas. The full long decimal is numerical, with no interval-arithmetic claim about rounding; the exact formula and analytic tail proof carry the rigorous result.

## Resource audit and final scope

Added peak resident-memory reporting and reran the exact command above solely to check the previously uninstrumented 1 GB requirement. Exit 0; all mathematical output was identical. Additional output: `Peak resident memory: 19562496 bytes (below 1 GB).` Actual niceness remained 20. Both runs completed well below one second of reported tool wall time, within the 20-minute limit.

Checked the truncation count another way: the full integer shell max(|k|,|l|)=r has 8r points, giving independent bound (13a). The original quadrant shell has 2r+1 points, giving the direct heat-sum bound (20). These catch sign/quadrant/axis multiplicity mistakes without relying on the first product-tail estimate. The pole residue, Euler-constant conversion, boundary square-root correction, and zero-mode subtraction are all recorded explicitly in PROOF.md.

No failed mathematical claim was found in the earlier normalization audit. What remains unchecked is the full random matching proof in Xu's preprint, particularly the repair lemma and the convergence argument, and numerical rounding is not interval certified. The extension here is only the deterministic spectral evaluation. No claim of novelty of this classical type of spectral calculation is made.

Final deliverables: PROOF.md (formula, full derivation, two tail checks, independent heat and zeta normalizations), verify_spectral.py (reproducible single-thread check), SOLVED_ELSEWHERE.md (rechecked existing source), REPORT.md (result and handoff). All authored files remain in this folder.

Final read-only validation ran under the same environment/priority wrapper using `python3 -B -` with inline Python: assert actual niceness >=15; read the five deliverables and check trailing newlines; check the exact report verdict; parse the verifier with ast.parse; assert no __pycache__ exists. Exit 0. Output before this log append:

```text
nice: setpriority: Operation not permitted
REPORT.md: 33 lines
PROOF.md: 355 lines
LOG.md: 84 lines
SOLVED_ELSEWHERE.md: 15 lines
verify_spectral.py: 117 lines
PASS: deliverables, verdict, script syntax, and folder-only bytecode policy.
```
