# T058 work log, round 4

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026 (Asia/Tbilisi). Exact initial clock will be recorded below.

## Scope and orientation

All mutations stay in this folder. No git, subagents, external messaging, or account creation. The folder-only instruction excludes brain recall, mesh registration and task-checklist commands that write outside this folder. Read the brain navigation index and compute governor directly instead. Read the two earlier folders' REPORT.md, LOG.md, PROOF.md, AUDIT.md and all four Python scripts (one in the original folder and three in round 3). Earlier files remain untouched.

Read-only commands used `rg --files` and Python pathlib readers. Python commands use `OMP_NUM_THREADS=1 nice -n 15`; the inherited-priority diagnostic will be checked before computation. Some combined reader output was truncated; remaining proof sections will be read separately before use.

## Bounded literature check

First explicit local clock: 2026-11-15 04:30:05 +04. Initial tool calls preceded that reading by a few minutes. Actual nice was checked with `os.getpriority(os.PRIO_PROCESS,0)` and is 20; the launcher diagnostic is the already inherited maximum nice reduction, as in both earlier sessions. Governor: warn / cpu_saturated / owner_away_open. Only scalar standard-library checks are planned.

Started with web searches for Morris–Riordan cube-root concentration and fixed-p chromatic concentration in 2025–2026. Opened Annika Heckel and Oliver Riordan, *How does the chromatic number of a random graph vary?*, https://arxiv.org/html/2103.14014 (v3, 17 August 2023). Its Conjecture 10 confirms the phase-dependent exponent max(theta/2,(1-theta)/2), rather than a constant exponent 1/2 on a density-one set. Its equation (10) discussion states approximate Poisson marginal laws for both counts, but does not provide the joint assertion sought here.

The search again found Oliver Riordan's Oxford cube-root-concentration announcement (joint work with Rob Morris). Direct event-page access failed; indexed Oxford text repeats the O*(n^(1/3)) bound for certain n. This announcement does not settle the full problem and is not used as a proved theorem.

Opened Robert Morris and Oliver Riordan, *Random cliques in random graphs revisited*, https://arxiv.org/abs/2504.00964 (1 April 2025). The abstract concerns the distribution of the family of graph copies, including growing clique size near 2 log n. This is a new concrete paper lead beyond the preceding report; full text is checked next within the five-minute search budget. No source so far claims a solution of the fixed-p concentration-width problem.

Opened its full text, https://arxiv.org/html/2504.00964v1, especially Section 1.3 and Theorem 1.4. This theorem describes the clique-family distribution when its expected size is Theta(n^(1+theta)), -1+epsilon <= theta <= 1/2-epsilon, with an explicit pair-overlap correction. It does not state a chromatic concentration theorem. Thus it supplies a rigorous distributional ingredient related to the talk, but does not supply the missing cube-root proof. The bounded status search ends here; no full solution found, no SOLVED_ELSEWHERE.md warranted. The broad search is not exhaustive.

## Independent recheck of round 3 (analytic)

Re-derived the exact covariance by conditioning on a fixed K-set A and summing over l-sets B. Shared edge constraints are exactly binom(|A intersect B|,2); overlaps 0 and 1 contribute zero, full containment contributes binom(K,l) mu_K (1-q_l). The remaining conditional overlap sum splits at l/2. Its two bounding sequences have logarithms -u*j + j(j-1)/2 + O(j log u), and -u*s+s(s+1)/2+O(s log u), with u=log_2 n. The midpoint logs are -u^2/2+O(u log u), so the outer terms give O(mu_l K^5/n^2 + binom(K,l) K^2 n 2^(-l)). Since mu_l <= n^(2-delta+o(1)) on a fixed interior band, this is o(binom(K,l)). This independently checks all three moment asymptotics and the containment normalization.

The mean ratio follows independently by counting extensions of an (k-1)-set: mu_k*k = mu_(k-1)*(n-k+1)*2^(-(k-1)). Hence Cov/sqrt(mu_k mu_(k-1)) ~ sqrt(k(n-k+1)/2^(k-1)) -> 0, agreeing with round 3. Its main claim holds analytically. A separate exact computation based on orthogonal edge monomials, rather than the earlier overlap recurrence, will check its numbers as well.

## Chosen extension, before proof or computation

Prove a joint central limit theorem for (X_k,X_(k-1)) on every fixed interior phase band: after centering and dividing each count by the square root of its own mean, the vector tends to two independent standard normal variables. This is the one extension. It supplies the joint law explicitly left unresolved in round 3, while leaving the transfer to chi open.

Reason: both counts are increasing functions of independent missing-edge indicators. Positive association controls the dependence of their characteristic functions by their covariance. A monotone coupling obtained by forcing one set to be independent can prove each marginal Gaussian limit directly from Var/mean -> 1, without importing a Poisson approximation theorem. The proof will include the association inequality and the coupling/characteristic-function argument in full. No claim of literature novelty is made. A quantitative characteristic-function estimate will make the claimed upgrade checkable.

## Independent numerical recheck completed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 recheck_moments.py`.

Exit 0, status `all Walsh/overlap identities passed`; nice=20, elapsed 15.310670417034999 seconds, peak RSS 25,182,208 bytes. Full stdout is recheck_moments.json. This uses an orthogonal expansion in independent fair +/-1 edge variables. If a_v counts edge sets supported on all v vertices, its covariance numerator is sum_v binom(K,v) a_v binom(n-v,l-v). Independently partitioning graphs by their support computes a_v; this differs from the preceding report's descending overlap recurrence. Every exact integer numerator agrees with the overlap formula.

At log2(n)=320.25538397352483, k=625, phase .75 up to integer rounding, independently reproduced the earlier three excess ratios over 1:

```text
Var(X_k)/mu_k - 1                2.2889672131060884e-89
Var(X_(k-1))/mu_(k-1) - 1        5.108702812850075e-13
Cov/(k mu_k) - 1                8.200165028651807e-16
```

Also reproduced slow convergence at phases .75 near 2^80 and 2^160: the (k-1)-variance ratios are 591.3002929300447 and 1.0186947729895188. Slight differences from the prior double-precision phase inversion reflect different rounded integers n, not a failed identity. The earlier main claim survives the independent algebraic and numerical recheck.

## Joint-limit proof written

Created PROOF.md. Its main quantitative assertion bounds the joint characteristic-function error by |st|c_n + (s^2 epsilon_k+t^2 epsilon_(k-1))/2 + |s|^3/(6 sqrt(mu_k)) + |t|^3/(6 sqrt(mu_(k-1))), where c_n is covariance normalized by square roots of the means and epsilon_j=Var(X_j)/mu_j-1+2q_j. All terms vanish uniformly on a fixed interior band.

The marginal argument is self-contained: force a uniformly chosen j-set A to be independent and put D=X_j^A-X_j. Exact size bias gives E D=Var/mean, and D=0 exactly when A was already independent, so E|D-1|=epsilon_j. The characteristic-function differential equation then compares directly with the standard normal equation. The joint argument proves positive association by induction on missing edges and integrates the nonnegative threshold-covariance kernel. This supplies the extra structure absent from small Pearson correlation alone.

Next audit: exhaustive graph enumeration will check the forcing identity, its absolute-error normalization, the covariance-kernel integral and the quantitative characteristic-function bounds. The asymptotic theorem itself is analytic; small graphs only test its exact ingredients.

## Exhaustive checks completed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_joint.py`.

Exit 0, status `all forcing, kernel and CF checks passed`; nice=20, elapsed 0.11066566599765792 seconds, peak RSS 17,301,504 bytes. Full stdout is joint_verification.json. Enumerated all 1024 graphs on five vertices and all 32768 on six. For each size 2, 3, 4, checked the entire size-biased distribution by forcing a fixed canonical set (symmetry makes this equivalent to a uniform set), not merely the first two moments. Exactly verified D>=0, P(D=0)=q_j, ED=Var/mean, and E|D-1|=epsilon_j.

For n=6 the exact epsilon values for j=2,3,4 are 1/2, 5/4, 63/64. Every threshold-covariance kernel numerator was nonnegative. Summing the kernel gives exactly Cov(X_3,X_2)=15/4 and Cov(X_4,X_3)=75/64. The analogous n=5 results are 15/8 and 85/256. For each of these four joint distributions, checked both the dependence bound and the full Gaussian characteristic-function bound at 49 argument pairs, including negative and zero arguments. These last complex-number checks use floating arithmetic with tolerance 2e-13; the distributional and moment checks are exact rational/integer arithmetic.

No mathematical check failed. The small-graph characteristic-function bounds can be loose: small graphs test identities, not asymptotic Gaussian accuracy. One combined documentation patch was rejected as malformed before changing files; it is being reapplied in smaller pieces.

## Independent audit and report

Created AUDIT.md with the full Walsh derivation behind the numerical recheck, separate hand checks of the forcing normalization and finite epsilon values, and a second derivation of joint independence. For the latter, any subsequential limit has normal marginals; its nonnegative threshold-covariance kernel has integral zero by Fatou's lemma and c_n->0. Continuity forces that kernel to vanish everywhere. This checks the limiting conclusion independently of the complex characteristic-function inequality.

Checked the Gaussian differential-equation sign, the constants 1/2 and 1/6 by integration, both negative and zero characteristic-function arguments, phase endpoints, and the difference between weak convergence and conditional or total-variation claims. Gaussian marginals and zero correlation alone are insufficient (a normal variable times an independent random sign gives a counterexample); association is essential here.

Created REPORT.md with verdict PARTIAL. The new piece is a joint Gaussian limit for the two normalized counts; the chromatic concentration problem remains unresolved. The report records the new Morris–Riordan paper lead and a concrete possible next packing lemma. Startup index was read directly; its named startup-card files were not found at the displayed memory root or the three obvious alternate roots. No brain command that writes outside this folder was used.

Final artifact command: `OMP_NUM_THREADS=1 nice -n 15 python3` with inline pathlib/json/ast checks. Exit 0. All eight deliverable files are present and nonempty, both scripts parse, both stored result statuses pass, actual priorities and recorded memory/time usage meet the limits, REPORT.md starts with the required PARTIAL verdict, and no SOLVED_ELSEWHERE.md is present. Output: `Artifact audit passed; actual nice= 20`. Earlier folders were only read. No additional computation is needed after the successful checks.
