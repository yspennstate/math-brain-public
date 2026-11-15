# T058 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, first recorded local clock 01:03:37 +04.

## Orientation

Read the earlier REPORT.md, LOG.md, PROOF.md, verify_phase.py and AUDIT.md in `~/codex_op_1114/briefs/T058`, without changing them. Read startup memory and the compute state: status warn, mode owner_away_open, CPU saturated. All computation here will be tiny, one thread and under nice -n 15. No git or subagents.

The explicit folder-only rule takes precedence over the global brain/mesh/checklist registration instructions: those commands write outside this folder, so they are not run. Startup and earlier work were read directly instead.

Initial commands: `pwd`; `rg --files` for earlier artifacts; `cat` for the startup, compute state, earlier report, log, proof, script and audit; `date '+%Y-%m-%d %H:%M:%S %Z'`.

## Literature check started

Queries: `"chromatic number" "concentration" "2025" "2026"`; `"zigzag conjecture" chromatic solved`; `"How does the chromatic number" concentration subsequent`.

Opened https://arxiv.org/html/2103.14014v3 (HTML endpoint initially returns only a short conversion page). Search results point to the published Heckel–Riordan paper and the tame-colourings paper, rather than a solution. Will inspect the paper and one further bounded search before closing this check.

The unversioned HTML https://arxiv.org/html/2103.14014 opened successfully. It verifies Conjecture 10 and the two independent-set scales in equation (10). Opened the arXiv page of Annika Heckel and Konstantinos Panagiotou, *Colouring random graphs: Tame colourings*, arXiv:2306.07253, and Annika Heckel's publication page. Opened Zhifei Yan, *Exponential tails for factors and the chromatic number of random graphs*, arXiv:2609.12700: its new chromatic CLT concerns p tending to 1, not fixed p=1/2.

The search also located Oliver Riordan's Oxford talk, *Cube-root concentration of the chromatic number of G(n,1/2) – sometimes*, 18 February 2025, https://www.maths.ox.ac.uk/node/70763. Its abstract announces joint work with Rob Morris giving O*(n^(1/3)) for certain n. No paper, arXiv id, precise phase range or proof was located in the bounded search. This is a material omission in the earlier literature summary, but not a solution of T058 and not a theorem used below. The broader Oxford listing initially failed to fetch; the direct event page is the relevant source.

Literature search closed at about 01:05 local time, under five minutes after the 01:03:37 start. No later solution of fixed-p=1/2 concentration was found. No SOLVED_ELSEWHERE.md is warranted.

## Independent recheck of the earlier result

Independently derive its constants from the entry/exit recurrence. A band of phase length d stretches n by s=2^(d/2), and the intervening gap by v=2^((1-d)/2). If L is the counted fraction at entry, the next entry fraction is (L+s-1)/(sv). The contraction fixed point is (s-1)/(sqrt(2)-1); the exit fraction is sqrt(2)(1-1/s)/(sqrt(2)-1). These reproduce both density constants. In logarithmic coordinates band and cycle lengths tend to d*log(2)/2 and log(2)/2, giving logarithmic density d. The earlier proof of theta={f(n)}+O(log log n/log n) was re-expanded and its bracket identity is correct. Thus the earlier main claim holds. A fresh computation, using integer binomial coefficients rather than the earlier inverse solver, will also check its finite counts and theta formula.

## Chosen extension, before doing it

Choose the fixed interior band 1/4 <= {f(n)} <= 3/4. Prove explicit second-moment estimates for the two random variables driving the Zigzag Conjecture: X_k and X_(k-1), the counts of independent sets of those sizes, with k=floor(f(n)). Target Var(X_k)~mu_k, Var(X_(k-1))~mu_(k-1), and Cov(X_k,X_(k-1))~k*mu_k, hence correlation asymptotic to sqrt(k(n-k+1)/2^(k-1)) and tending to zero. This is one probabilistic extension beyond the earlier deterministic density result. It checks that the two proposed fluctuation sources do not collapse into the same correlated noise on this positive-lower-density band. It will not transfer their fluctuations to chi; marginal approximate-Poisson behaviour is already described in Heckel–Riordan. No literature novelty is claimed.

## Independent computation completed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 recheck_earlier.py`.

Exit 0. The launcher prints `nice: setpriority: Operation not permitted`, because inherited nice is already 20; the script asserts and reports actual nice=20 before computing. Stdout, also saved in earlier_recheck.json:

```text
status: all checks passed
integer_counts: [[1000,454],[10000,4976],[100000,49829],[200000,106225]]
entry_density: 0.45678638313705494
exit_density: 0.5432136168629447
theta (log2_n, phase, theta):
10, 0.24153389200320063, 0.4601223703521674
20, 0.2415338920032042, 0.4645807883029279
40, 0.2415338920032042, 0.4099246874423199
80, 0.2415338920032184, 0.3546164042926988
160,0.24153389200318998, 0.3124192057871862
elapsed_seconds: 0.05137079197447747
peak_rss_bytes: 15073280
```

Natural-log enumeration reproduces all four earlier counts. An exact integer binomial coefficient reproduces its log-product theta computation. A contracting recurrence independently reproduces its density constants. The earlier result survives the recheck.

## Overlap estimate derived

For independent-set sizes K and l with K-l in {0,1}, condition on a fixed independent K-set. The expected number of independent l-sets intersecting it in j vertices is h_j=binom(K,j)binom(n-K,l-j)2^(-binom(l,2)+binom(j,2)). The exact covariance divided by mu_K is sum from j=2 to l of h_j(1-2^(-binom(j,2))). The endpoint h_l is 1 for equal sizes and K for adjacent sizes.

Split the nonendpoint overlaps at l/2. At small overlaps bound h_j/mu_l by (Kl/(n-l))^j 2^(j(j-1)/2). At large overlaps, with s=l-j, bound h_(l-s)/h_l by (Kn2^(-l))^s 2^(s(s+1)/2). Both logarithms are convex quadratics, so the sum is bounded by the number of terms times its endpoint maximum. The middle endpoints are exp(-c(log n)^2), whereas the outer endpoints give O(mu_l K^5/n^2 + h_l K^2 n2^(-l)). This tends to zero relative to h_l in the selected phase band. PROOF.md will spell out the midpoint exponents and all normalizations.

## First moment-check run

Wrote PROOF.md with the full argument and verify_moments.py with exact overlap sums and exhaustive enumeration of all labelled graphs on 5 and 6 vertices. Command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_moments.py`.

The first run exited 1 at an overly strong finite-size diagnostic assertion: at log2(n) about 160 it demanded |Var(X_(k-1))/mu_(k-1)-1|<1e-6 for every target phase. The proof asserts convergence with logarithmic factors, not this numerical threshold. All preceding exact identities and exhaustive-graph checks passed. Removed arbitrary proximity assertions so the actual finite ratios can be inspected; convergence diagnostics are not certified error bounds. A failed attempt to append this log used a context line from PROOF.md rather than LOG.md; apply_patch rejected it without changing files.

## Exact verification completed

Repeated command: `OMP_NUM_THREADS=1 nice -n 15 python3 verify_moments.py`.

Exit 0; status `all checks passed`; actual nice=20. Full stdout is preserved in moment_verification.json. Elapsed 3.34923783398699 seconds; peak RSS 16531456 bytes. All graphs on 5 vertices (1024) and 6 vertices (32768) were enumerated directly. Means, three variances and both adjacent covariances agree exactly, as rational numbers, with two overlap computations (the covariance sum and the full joint moment minus the product of means).

For n=6 the verified values are Var(X_2)=15/4, Var(X_3)=5, Var(X_4)=1875/4096, Cov(X_3,X_2)=15/4 and Cov(X_4,X_3)=75/64. For n=5 they are 5/2, 65/32, 455/4096, 15/8 and 85/256 in the same order.

Every large-n overlap calculation also agrees exactly with the full joint-moment calculation. Selected diagnostics (rounded here; full values in JSON):

| log2(n) | phase | Var(X_k)/mu_k | Var(X_(k-1))/mu_(k-1) | Cov/(k mu_k) | rho / sqrt(k(n-k+1)/2^(k-1)) |
|---|---|---|---|---|---|
|40.004391|.25|1.0000000663|1.0780731028|1.0011315577|.9641997880|
|80.131604|.50|1.0|1.0015018716|1.0000102168|.9992601182|
|80.258894|.75|1.0|591.3002929288|5.0156482512|.2062638048|
|160.256544|.75|1.0|1.0186947730|1.0000612943|.9908423943|

This explains the failed diagnostic: convergence of the (k-1)-count variance can be very slow near the upper edge of the band. It is not legitimate to infer a uniform small error from merely astronomical n. The analytic estimates remain asymptotic, with no advertised finite cutoff. A larger exact-overlap computation is justified to check this specific slow-convergence concern. No random graph simulation or chromatic-number calculation is involved.

## Independent audit of the extension

Read the governor again before the larger check: warn, CPU saturated, owner_away_open. The following still uses one thread, actual nice=20, and less than 20 MB.

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 audit_extension.py`.

Exit 0; stdout status `all exact audits passed`; elapsed 20.081548874964938 seconds; peak RSS 19988480 bytes. Full output is extension_audit.json. This script uses Decimal/Newton inversion to choose n, then descends through the overlap sizes using an exact integer recurrence; every recurrence value is separately checked against the direct product of binomial coefficients. It also checks both convexity-based bounds in PROOF.md as exact rational inequalities, including their midpoint comparisons. Thus the bounds themselves, not just the covariance formula, are tested.

At log2(n)=320.25538397352483, target phase .75, k=625:

```text
Var(X_k)/mu_k - 1 = 2.2889672131060884e-89
Var(X_(k-1))/mu_(k-1) - 1 = 5.108702812850075e-13
Cov(X_k,X_(k-1))/(k mu_k) - 1 = 8.200165028651807e-16
```

At phases .25 and .50 the (k-1)-variance excess is respectively 4.855533095759346e-60 and 1.5750511154174033e-36. Every tested low-overlap sum was below its exact bound (ratios about .00160), and every high-overlap sum was below its bound (ratios at most .00321). Small displayed excesses were computed as exact rational differences before conversion to float, rather than subtracting two rounded floats. These are diagnostics at specific n, not uniform error bounds.

Wrote AUDIT.md to rederive the covariance endpoint by extending a (k-1)-set rather than deleting from a k-set, rederive the explicit correlation constant by squaring it, calculate the n=6 moments manually, and record endpoint and inference limitations.

## Result and remaining obstacle

PROOF.md proves all three target moments uniformly on any fixed interior phase band. REPORT.md records verdict PARTIAL because the actual concentration-width problem is not resolved. The result is a probabilistic extension of the earlier deterministic calculation, with no claim to literature novelty. The missing transfer from independent-set counts to chi remains the main obstruction. The 2025 cube-root announcement is a separate literature lead; its exact phase range was not established here.

Final artifact audit: `OMP_NUM_THREADS=1 nice -n 15 python3` (inline pathlib/json validation). Exit 0. Artifact audit passed: all required files exist, verdict is PARTIAL, all exact checks passed, every recorded run is within the resource limits.
