# T226 round-6 log

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta”. Received 15 November 2026, approximately 11:27 Asia/Tbilisi (first clock: 07:27:20 UTC).

## Orientation and bounded literature check

Read the startup memory index, RESUME.md and the compute governor state (ok / owner_away_open). The task-specific instruction to write only here supersedes shared mesh, checklist and brain writes. No subagents, git, external messages or edits of earlier folders. All numerical programs will use standard-library arithmetic, one thread, nice >=15, explicit CPU/wall limits and far below 1 GB RAM.

Read the earlier REPORT.md, LOG.md, PROOF.md and scripts in the original, round-3, round-4 and round-5 folders. Some combined output was truncated; targeted rereads follow for the omitted portions.

The web check began at 07:27 UTC and closed at 07:31 UTC, within five minutes. Searches: `"edge of stability" random initialization gradient descent 2026 convergence neural network`; `"2606.15551" "4.4"`; `"edge of stability" sharpness endpoint deep linear networks 2025 2026`.

Opened Eric Gan, *A Bifurcation Theory Framework for Gradient Descent on the Edge of Stability*, https://arxiv.org/html/2606.15551v1 (Theorem 4.4 explicitly starts in a neighborhood of a minimum); Elon Litman, *The Origin of Edge of Stability*, https://arxiv.org/abs/2604.20446 and https://arxiv.org/html/2604.20446v1 (trajectory curvature identities, not the required random-entry theorem); Jaerin Lee and Kyoung Mu Lee, *A Journey to the Edge of Stability*, https://arxiv.org/abs/2609.32290 (empirical learning-rate/optimizer sweeps); Geonhui Yoo, Minhak Song and Chulhee Yun, *Understanding Sharpness Dynamics in NN Training with a Minimalist Example: The Effects of Dataset Difficulty, Depth, Stochasticity, and More*, https://proceedings.mlr.press/v267/yoo25b.html (one neuron per layer); Rustem Islamov, Michael Crawshaw, Jeremy Cohen and Robert M. Gower, *Non-Euclidean Gradient Descent Operates at the Edge of Stability*, https://proceedings.mlr.press/v306/islamov26a.html (generalized sharpness diagnostics and experiments). No opened statement solves the requested basin/endpoint problem. No SOLVED_ELSEWHERE.md is justified. This is a bounded search, not a claim of exhaustive openness.

## Independent audit of the earlier main claim

Round 5 holds on re-derivation. Expand the simultaneous parameter updates to obtain q'=q-2h+v^TCv, C'=C-(2-q)vv^T and v'=(I-C-qI+hI)v. In the rectangle q0,c0<2 this gives sum h <=q0/(2-c0), norm convergence of q,C, and residual convergence. For the top limiting C eigenspace, differentiate the spectral projector along C-s(2-q)vv^T. Its cross-block derivative is -(2-q)vi*vj/(lambda_i-lambda_j), so the squared residual weight has derivative at least -2(2-q)h/gap times itself. The top multiplier is at least 1-h in modulus if the limiting output eigenvalue is >=2. The resulting infinite product is positive, including at equality, and forces finite-time invisibility. Rank-one feedback preserves the Krylov determinant, giving D_next=det(theta I-C_next)D with theta=(1-q)(1-h). The witness Vandermonde polynomial and each finite multiplier are nonzero polynomials. Thus their countable exceptional union is null. The Gram determinant argument supplies a positive lower output eigenvalue, after which strict subcriticality gives geometric parameter convergence. No density of finite iterates or invertibility of GD is required. The small-target argument is pointwise in initialization and implies no finite-eta bound.

Executable independent checks of the key recurrences, projector sign, Krylov identity and exceptional examples will supplement this audit.

## Chosen extension (before writing its proof)

Make the small-nonzero-target persistence quantitative. This is the alternative missing lemma named in round 3 and the finite-eta limitation retained by round 5. Use a smaller spectral region with explicit margins, not the whole rectangle: c0 <=1-2delta and q0+c0 <=2-4delta, with 0<delta<=1/4. Seek a target threshold proportional to the initial augmented Gram determinant. This region still contains the earlier full-rank example with initial Hessian sharpness >2.

The proposed mechanism is direct, without shadowing a zero-target trajectory: for residual r=U^TA-y, the errors in monotonicity of q and C are controlled by 2||y|| sum ||r||. A determinant lower bound and c<1 should give uniform residual contraction; a bootstrap on the same cumulative error should close when ||y|| is a small explicit multiple of det G0. Gaussian inverse moments of det G0, derived by Gram-Schmidt, would then turn this into an explicit finite-eta probability bound, rather than only a limsup. This does not purport to obtain the full rectangle's near-critical zero-target gap distribution.

## Proof saved and numerical audit prepared

Saved PROOF.md with the following proposed theorem. Let M=d+2, chi=exp[-4/(delta(2-delta))], D=det G0, mu=chi D/M^d and kappa=delta mu. Under the stated initial spectral margins, ||y|| <=delta^2 chi D/(8 M^d) implies residual contraction by 1-kappa from the first step, parameter convergence, full augmented rank, and endpoint output sharpness <=2-7delta/2. The proof bootstraps B_t=2||y|| sum_(j<t)||r_j||, keeping B_t<=delta/4. The perturbed q recurrence bounds sum ||r_j||^2<2, which preserves det G_t>=chi D. This closes the contraction rather than assuming it.

For independent Gaussian scaled entries, Gram-Schmidt gives det G0=tau^(2(d+1)) times independent chi-square variables with degrees m,m-1,...,m-d. Its negative p-th moment is explicit for p<(m-d)/2. Markov therefore bounds failure on the spectral region by a constant times (eta||b||)^p, at every eta>0. For m=16,d=8, p=3 is admissible. A sphere-net argument supplies an elementary bound on the spectral complement. No rate for the whole rectangle's zero-target endpoint-gap distribution is asserted.

Prepared verify_quantitative.py without importing earlier scripts. It independently uses column-based gradients, exact rational recurrences and Gram-Schmidt volumes, a closed-form projector check, the earlier exceptional endpoints, exact bootstrap constants, gamma ratios versus rational products, two evaluations of the Gaussian Chernoff exponents, and 120-digit nonzero-target finite trajectories. Initial spectral margins are certified by exact rational Sylvester minors; they do not depend on floating eigenvalues. Targets are chosen at one half and at the full proved threshold, including perturbations far below binary64 roundoff. The script checks priority before arithmetic and installs a 100-second CPU cap and 150-second wall alarm.

Before running, reread the compute state: warn / owner_away_open, CPU saturated, free RAM 52%; no distress. The verification is one low-priority process, fixed small lists, no numerical libraries, no worker threads.

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_quantitative.py > verification.stdout.txt 2> verification.stderr.txt`.

## First verification passed

Exit 0. Effective nice 20; elapsed 2.081231 seconds; peak RSS 17,858,560 bytes. The nice utility printed its familiar permission warning; the program independently measured its inherited nice value before arithmetic. All 40 exact rational cases passed. The projector derivative discrepancy was 1.34e-12. Both earlier exceptional sharpness constants, 256/81 and 1011719/457600, were recovered independently.

All 14 high-precision nonzero-target trajectories passed at one half and at the full proved target threshold, with exact rational certificates of the initial spectral inequalities. Largest update count: 998. Smallest nonzero target: 1.1013177778e-42. Every final residual was at most 1e-28 times its nonzero target; the final output was checked to equal that target to this tolerance, rather than being rounded to zero. Largest endpoint output sharpness: 1.4542891703. These are finite implementation checks; convergence follows from the bootstrap proof.

At delta=1/16, m=16,d=8,tau^2=1/288, the computed spectral-complement bound is 9.56798240396e-25; the cubic perturbation coefficient is 1.12614258212e120. At eta||b||=1e-48, the total is 2.08294082251e-24. The coefficient is large: this supplies an explicit finite-eta guarantee, not a practical transition-scale estimate.

Added an independent rigorous numerical audit before the final run. Every exponential in the two spectral tails and cubic coefficient is enclosed by exact rational Taylor sums and a geometric bound for the remaining positive terms. This certifies the round-number bounds 9.568e-25, 1.127e120 and 2.1e-24, without trusting floating-point exponentiation. A digit-grouping typo in the displayed K coefficient was caught and corrected before numerical verification; its defining formula and script both use 8*10^8*256=204800000000.

## First audited run: an auxiliary precision demand failed

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_quantitative.py > verification.audited.stdout.txt 2> verification.audited.stderr.txt`.

Exit 1. All newly added exact rational comparisons certifying the three rounded probability bounds passed. A subsequent diagnostic incorrectly demanded that the upper Taylor bound agree with the exponential value to relative error below 1e-70. The chosen finite Taylor sum need not have that accuracy. Its explicit remainder is the appropriate measure, not an arbitrary agreement tolerance. Preserve the failed audited outputs. Replace this diagnostic by checking that the independently evaluated Decimal value lies between the exact lower and upper bounds (allowing only Decimal rounding), and report each rational interval's actual relative width. No claimed inequality failed.

Also added a boundary test at delta=1/4: q0=c0=1/2, v0=0 and a small exact rational nonzero target. It lands at the global minimum in one step, with both q and C increasing. This tests that the proof retained the target error terms rather than incorrectly extending zero-target monotonicity. Zero initialization with a nonzero target remains stationary and checks the need for a rank-dependent threshold.

## Final verification passed

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 verify_quantitative.py > verification.final.stdout.txt 2> verification.final.stderr.txt`.

Exit 0, elapsed 2.044715 seconds, effective nice 20, peak RSS 18,202,624 bytes. All 40 exact cases, the projector diagnostic, both exceptional endpoints, rational probability certifications, the new boundary case and all 14 high-precision trajectories passed. The exact Taylor intervals have relative widths 1.011e-69 for the spectral tail and 3.441e-69 for the cubic coefficient; the failed 1e-70 diagnostic was indeed asking for more precision than these intervals supplied. The independently evaluated 120-digit values lie inside both intervals. Standard error contains only `nice: setpriority: Operation not permitted`; actual process priority was checked before arithmetic.

Final machine-readable results are verification.json; complete successful output is verification.final.stdout.txt and verification.final.stderr.txt. First-run and failed audited outputs remain available. No run exceeded 19 MB RAM or 3 seconds of wall time.

## Final attempts to break the theorem

- Checked induction order independently: use only current determinant and accumulated target error to prove current residual contraction; use this contraction to bound the next accumulated error; sum the exact q recurrence to bound residual-square energy; then obtain the next determinant bound. There is no appeal to an unproved uniform convergence time for the zero-target trajectory.
- Re-derived the key upper multiplier from omega=v^Tr=||v||^2-v^Ty <=q*c+beta <=(1-delta)*lambda_min(H)+beta. The lower multiplier uses omega>=-beta and q+c<=2-3delta. The two sides give the same uniform contraction interval; controlling only the upper eigenvalue would have missed alternating modes.
- The determinant factor uses ||r||^2, not ||v||^2, for nonzero targets. The residual bound ||r||<=1-delta prevents finite rank collapse. The exact delta=1/4 one-step example has increasing q,C; it rules out silently reusing zero-target monotonicity.
- Rechecked the smallest-Gram-eigenvalue inequality in its required direction: det G <=lambda_min(G)*(tr G)^d. Both q and C are principal submatrices, so H>=2mu I. The proof preserves the entire augmented rank, not only rank of U.
- Audited all probability normalizations a second way. The gamma ratios equal the rational product over nu=8,...,16, with tau^(-54)=288^27. A sphere net of radius 1/32 has at most 65^8 points. The two chi-square Chernoff expressions agree with their optimized MGF forms; exact rational Taylor intervals independently enclose every numerical exponential. The coefficient in K is 204800000000 and the exponent is 1024/31.
- At delta=1/16, the earlier initial-supercritical example has q0+c0=33/20<7/4, c0=13/20<7/8 and Rayleigh quotient 121/50. Exact symmetric differences of the quartic loss recover the quotient independently. Thus the region is not obtained by assuming initial Hessian sharpness below 2. Residual loss nevertheless contracts here; no sustained edge phase is claimed.
- Rank dependence and the target scale matter: zero initialization at a nonzero target is stationary and nonglobal, and is excluded by det G0>0. The Gaussian law is explicitly eta-dependent in original coordinates. No probability bound for all initialization laws, nonlinear activation, or the full spectral rectangle is inferred.

The earlier result holds. The new result is the explicit finite-eta small-target theorem and its Gaussian inverse-determinant probability bound, on a smaller region than round 5. The full-rectangle endpoint-gap rate and the original positive-probability edge-entry problem remain unresolved. REPORT.md records this scope and the next checkable step.

## Report saved and final read-through

Saved REPORT.md with the required PARTIAL first line, the theorem, finite-eta Gaussian specialization, exact commands and output, failed auxiliary precision check, sources opened, limitations and next step. Reread PROOF.md and REPORT.md in full. The final proof clarifies event measurability and the chi-square threshold notation. No mathematical or executable changes followed the successful final run. All requested artifacts are in this folder; previous rounds were not edited.

Task: “Open problem T226: The edge of stability: why full-batch gradient descent hovers at sharpness 2/eta” — received 15 November 2026, approximately 11:27 Asia/Tbilisi.
