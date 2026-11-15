# T427 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Session clock: 15 November 2026, approximately 06:40 Asia/Tbilisi (02:40 UTC); first saved clock reading 06:41:19 +04.

## Orientation and literature check (06:40–06:42 +04)

Read both earlier folders' REPORT.md and LOG.md, round 3 PROOF.md and verify_spectral.py, and the original SOLVED_ELSEWHERE.md. The original folder has no PROOF.md or mathematical scripts. Neither earlier folder was modified. Read startup memory and the compute governor state: warn, owner_away_open, CPU saturated. The specific folder-only rule supersedes global mesh, checklist and brain logging commands, which would write elsewhere; none were run. No git or subagents.

Read-only shell commands used cat, rg --files, ls, date. The first rg search mistakenly included the broad ~/.claude tree and produced truncated filenames; no contents outside the intended startup files were used. Subsequent reads were targeted. The priority wrapper prints `nice: setpriority: Operation not permitted`; mathematical scripts must verify actual niceness >=15 before calculation.

Web search tool queries: `"2610.40509"`; `"random matching" "second order" constant 2026 Xu`; `"2610.40509" correction error constant`; `semidiscrete matching constant second order November 2026`. Opened https://arxiv.org/abs/2610.40509, https://arxiv.org/html/2610.40509v1, and https://arxiv.org/abs/2611.17066. Yunzong Xu's preprint still has the same v1 statement. No later resolution or correction appeared. Martin Huesmann and Arthur Wachtel's boundary-conditions paper is the source already checked in round 3, not a new update. Literature discovery is closed within the five-minute cap; reading the existing proof continues as mathematical work.

## Earlier result: independent re-derivation begun

Round 3's positive spectral series and its tail estimates were read in full. Independent route: for Re(s)>1, quadrant sign-counting and the sum-of-two-squares identity give Z_Q(s)=pi^(-2s)[zeta(s) beta(s)+zeta(2s)], where beta is the Dirichlet beta function. Its finite part at s=1, minus gamma/(4 pi) to convert from zeta to heat regularization, is

`h_Q = 1/6 + beta'(1)/pi^2 - log(pi)/(2 pi)`.

This follows by expanding zeta(s)=1/(s-1)+gamma+O(s-1), beta(1)=pi/4, and pi^(-2s). This checks the Euler-constant sign and the axis modes independently of the theta-series evaluation. Numerical verification will compare this identity with the round 3 evaluator.

## ONE extension selected before work

Audit the equal-mass boundary-repair estimate in Appendix C.2 of Xu's existing preprint, then its use in the subdivision argument. The next worker request singled out Theorem 4 and Appendix C. This estimate is more consequential than another spectral evaluation because the prior reports explicitly left it unchecked. A counterexample to a stated auxiliary lemma, if found, is the deliverable; it would not disprove existence of the matching limit. Otherwise record precisely what part is verified and what remains missing. No numerical estimate of the universal matching constant is planned.

## Earlier result verified (independently and by rerun)

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T427/verify_spectral.py
```

Exit 0, tool wall time 0.016 s. All earlier mathematical output reproduced, including H_5 = 0.00402223657274227817227364756500595607753013990163588814077047, its analytic tail bound 8.97623383875e-52, and the independent direct heat sum. Actual niceness 20; peak RSS 19,562,496 bytes. The environment again prints a priority warning even though the process is already below the requested priority.

Created check_zeta.py here. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_zeta.py
```

Exit 0, wall time 3.2 s. Output:

```text
nice: setpriority: Operation not permitted
niceness=20; precision=75 decimal digits
beta'(1) via contour derivative = 0.192901316796912429363189764028032785245096867620007527171349
h_Q via zeta finite part = 0.00402223657274227817227364756500595607753013990163677828247391
h_Q via Gamma identity = 0.00402223657274227817227364756500595607753013990163677828247391
difference from earlier H_5 = 8.90141703437e-52
PASS: independent zeta and Gamma checks agree with round 3.
Peak resident memory: 19513344 bytes
```

The difference is positive and below the earlier H_5 truncation bound. The earlier result holds. These decimal computations are not interval certification. The Gamma check follows the Dirichlet-beta functional equation: beta'(0)=log(Gamma(1/4)/Gamma(3/4))-log 2 and beta'(1)/(pi/4)=gamma+log(pi/2)-2 beta'(0). A draft formula initially had log(2 pi) in the last expression; algebraic differentiation corrected this factor of four before execution. The contour derivative and corrected Gamma expression agree to 65 decimal places.

## Repair audit and sharpened target

Read all of Appendix C.2–C.4, Section 4.2 (including the two-scale convergence lemma), and Theorem 4 through the web tool. No counterexample to the flat-grid repair construction was found. Checked its intermediate measures, cell mass conservation, centering, deterministic cutoff, and covariance before restricting to the good event. These steps are consistent; the argument warrants a detailed independent derivation in the flat equal-mass case.

The ONE extension is now precise: prove the flat-grid equal-mass subdivision estimate at the same time t=n^(-5/6) with error O(n^(-1/60) log(en)^(11/10)), improving the cited O(n^(-1/120) log n). Use the smallest concentration scale delta^2=A log(en)/(nt), and balance collar mass r with r^(-4)delta^2 by r=(delta^2)^(1/5). The earlier choice delta=n^(-1/24) left a factor of two in the power unused. This is an optimization and independent proof of the existing boundary-repair method, not a value for the universal constant. Full matching reduction and arbitrary curved surfaces remain outside this extension.

To avoid assuming the matching theorem when bounding the repair cost, derive the rough expected cell cost directly by first smoothing at s=1/n and using a cellwise H^(-1) action bound. Also rederive the optimal-potential L^2 estimate on the flat torus and the global/cellwise heat comparison. The discrepancy estimate can be sharpened to O(t log(e/t)) before the potential comparison, but the dominant error here is delta^2, so this does not alter the claimed rate.

## 06:49–06:52 +04 — proof saved and exponent audit

Saved PROOF.md with the stronger expected absolute subdivision estimate. It proves the rough cost bound directly, reconstructs the short-displacement and L^2-potential bounds, keeps the covariance unconditional, constructs a cell-mass-preserving repair, and compares the two heat smoothings. The rate uses delta^2=A n^(-1/6)log(en) and r=A^(1/5)n^(-1/30)log(en)^(1/5). The proof is restricted to flat square grids and equal empirical masses.

Created check_scaling.py with exact Fraction arithmetic. Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_scaling.py
```

Exit 0, wall time below 0.1 s. Output:

```text
nice: setpriority: Operation not permitted
niceness=20; exact Fraction arithmetic
delta^2: n^(-1/6) log(en)^(1)
r: n^(-1/30) log(en)^(1/5)
repair: n^(-1/60) log(en)^(11/10)
global heat squared distance: n^(-1/4) log(en)^(0)
global heat cost comparison: n^(-1/8) log(en)^(1/2)
concentration prefactor: n^(8/3) log(en)^(-1)
cyclical-monotonicity reassignment factor: 169/1000 < 1
PASS: independent balances and all strict exponent margins.
Peak resident memory: 13811712 bytes
```

The second exponent derivation solves -b=4b-1/6 and c=1-4c independently of substituting r=(delta^2)^(1/5). It checks sqrt(t)=o(delta^2), L=o(r), and the smaller global heat error. The ten-edge reassignment coefficient is 10(1/10+3/100)^2=169/1000<1, recomputed as a rational number. The Gaussian second-moment factor 4t is the trace of covariance 2t I in two dimensions, and also follows by differentiating the free heat second moment since Delta |x|^2=4.

Reran check_zeta.py after adding an explicit comparison with the earlier analytic tail bound. Same command as before, exit 0, wall time 3.26 s, actual niceness 20, peak RSS 19,726,336 bytes. Additional output: `earlier H_5 analytic tail bound = 8.97623383875e-52`. The positive difference 8.90141703437e-52 lies below that bound. All earlier numerical outputs were unchanged.

Two apply_patch attempts to add small proof clarifications failed because a search context was only part of a paragraph; their attempted edits were retried with exact full-line contexts. No mathematical calculation failed. No simulation, installation, git, external write, or background worker was used.

## Adversarial checks of the proof

- A naive global Poincaré estimate of the potential would lose the gain. The proof instead derives the H^(-2) comparison with an interpolation density bounded by C(1-u)^(-2); its square root is canceled by the Taylor factor 1-u. The endpoint at u=1 is treated by H^2 approximation, whose uniform convergence justifies atomic evaluations.
- Conditioning the iid covariance identity on the good event would be invalid. Equations (15), (16), and (22) remain unconditional; the event is applied only to deterministic upper bounds and nonnegative terms.
- The retained allocations leave different amounts at different target sites. The measures sigma_0 and sigma_s preserve the original mass of EACH cell; the centering operation is applied only after the discrepancy terms are recombined, as in (21).
- Empty cells prevent a lower density bound; they lie in E^c, where the diameter bound and the explicit probability estimate apply. Finite small n are absorbed by a larger constant, not put into a large-n concentration estimate.
- The m=1 case retains the seam as a cell boundary. A cutoff near the seam prevents any retained torus edge from crossing the physical square boundary. A smooth product cutoff covers grid intersections and corners; its derivative vanishes near every face, so the divergence term has zero boundary flux.
- The source density q can jump across cell faces. No derivative of q is taken in the potential argument or the repair expansion. Bounds (24)–(25) use weak integration by parts only for phi times the smooth cutoff.
- Equal masses give covariance factor 1. Conditional cell counts give the exact scaling factor ell^2 d_k, including k=0; no bipartite, Dirichlet, or Poisson mass law is substituted.

An attempted shortcut toward a still smaller heat time was rejected in the exponent audit: at t=n^(-2/3), the global/cell heat comparison has n power zero. The reported result retains the original t=n^(-5/6). The bound proved here improves only subdivision; it does not independently certify the rest of Xu's second-order matching theorem.

## Final deliverables and validation

Wrote REPORT.md with the required verdict, the new bound, reproduction commands, failed attempts, scope limits, and a specific handoff to the equal-mass reduction in Proposition 3.1. All authored files are in the current folder; earlier folders remain read-only. No new SOLVED_ELSEWHERE.md is needed because the only relevant existence claim found is the source already recorded in both earlier sessions, not a new resolution.

Final validation command was an inline `python3 -B -` program under the same OMP/BLAS environment and `nice -n 15` wrapper. It asserted actual niceness >=15, limited CPU time to 30 seconds, checked the exact working directory, read the five deliverables, checked final newlines, parsed both scripts with ast.parse, checked the exact verdict, checked that equation labels 1–30 occur exactly once, balanced display delimiters, and checked that no __pycache__ exists. Exit 0, wall time below 0.1 s. Output before this final log append:

```text
nice: setpriority: Operation not permitted
REPORT.md: 32 lines, 4026 bytes
PROOF.md: 494 lines, 20106 bytes
LOG.md: 106 lines, 11053 bytes
check_zeta.py: 53 lines, 2172 bytes
check_scaling.py: 64 lines, 2353 bytes
PASS: deliverables, verdict, equation labels, display delimiters, script syntax, and no bytecode files.
```

Final mathematical audit: the action bound is homogeneous for subprobability cell masses, the root-sum cell cost has its triangle inequality by gluing and Minkowski, all optimal-potential calculations are on the flat torus, and the global-to-cell heat coupling is estimated only after averaging uniform starting positions. No o(1) term was used as though it had an explicit polynomial rate. The rate in the theorem comes from (27) and the strictly smaller error (30), with finite small n handled separately.
