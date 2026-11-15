# T075 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session: 2026-11-15, first recorded local clock 01:10:23 +04:00.

## Scope and startup

All deliverables stay in this folder. No git, subagents, external messages, or mesh/checklist/memory writes were used: the task-specific restriction on writes elsewhere overrides the global coordination instructions. Read the startup memory, memory index, compute state, and recalled relevant prior work. The compute state was warn / owner_away_open with saturated CPU; no heavy computation is planned. A startup brain recall completed; its attempt to launch a background index refresh failed under the sandbox. Do not run further brain commands that may write outside this folder.

Commands run through the shell include `OMP_NUM_THREADS=1 nice -n 15 python3 ...`; nice reports `setpriority: Operation not permitted`, consistent with the earlier worker's inherited nice 20. Shell reads used `rg --files`, `cat`, `sed`, and `date`. `ps` was denied by the sandbox. The earlier directory was read only.

## Earlier work read and rechecked

Read the earlier REPORT.md, LOG.md, and SOLVED_ELSEWHERE.md in `~/codex_op_1114/briefs/T075`. Directory listing confirms that it contains no PROOF.md and no computation scripts.

Opened Samuel Kittle and Constantin Kogler, *On L^p density of self-similar measures and Bernoulli convolutions*, https://arxiv.org/abs/2611.17277 and https://arxiv.org/html/2611.17277v1. Theorem 1.1 has exactly the absolute-continuity hypothesis reported earlier. Its application is independently checked by the characteristic function: independence gives phi(t)=cos(t) phi(lambda t), which is the Fourier transform of the balanced self-similarity equation for x -> lambda x +/- 1. Thus the law in the question satisfies its hypotheses if absolute continuity is supplied. Conversely an L^p density implies absolute continuity by integration on null sets. The earlier mathematical claim holds. It does not prove T075.

The earlier worker's stopping rule was broader than this task's: finding a regularity advance is not finding a solution of T075. Continue to an actual extension.

## Bounded literature update

Web search queries: `Bernoulli convolutions transcendental absolute continuity November 2026 Kittle Kogler`; `"2611.17277"`; `"Bernoulli" "transcendental" "absolute continuity" "2026" November solved`; `"Bernoulli convolutions" "2026" "2611"`. Opened the above preprint, its PDF, and https://arxiv.org/abs/1810.08905. No solution beyond the earlier report was located in this brief check. The current arXiv page still lists v1, 12 November 2026. This is a bounded search, not an exhaustive literature claim.

## Choice before extension

Derive a finite-prefix, all-scales small-set criterion that implies absolute continuity without assuming it. The previous report recommends establishing small-set mass control directly for a transcendental parameter, but its cited analytic lemma starts from a density. The next checkable piece is to express the missing control as an explicit statistic of prefix intervals and prove both sufficiency and necessity. Aim for a quantitative L^p sufficient condition, with constants independently audited. Do not claim that finite numerical data proves an all-scales hypothesis, or that a specified transcendental parameter has been certified.

## Proof drafted

Wrote PROOF.md. The statistic is the maximal mass A_n(delta) in a set of length delta under the law of the n-term prefix plus an independent uniform tail on the exact tail interval. Proved pure type directly from Lebesgue decomposition and uniqueness of the invariant measure. Weak convergence then shows singularity forces A_n(delta) -> 1 for every delta>0. Conversely absolute continuity gives the uniform estimate A_n(delta) <= 2 omega_nu(delta) by comparison with convolution of nu with a uniform kernel of twice the tail radius. Thus a liminf strictly below one is sufficient, and uniform small-set control is necessary. This does not establish the hypothesis for a transcendental parameter.

The stronger bound liminf A_n(delta)<theta<1/18 yields p=1+log(1/(18 theta))/log(72D/(delta lambda)), D=2/(1-lambda), by first proving absolute continuity and then using Lemma 2.1 of the opened Kittle–Kogler paper. The argument never applies that lemma to a singular measure. A direct level-k cylinder calculation independently recovers its geometric constant 2D/lambda, without importing the paper's stopping-time identity.

Wrote prefix_concentration.py, an exact-rational endpoint sweep with an independent direct sign enumeration / midpoint coverage / convex dual optimization for comparison. Planned controls are lambda=1/2 (exact uniform density) and lambda=1/3 (singular, disjoint cylinders). The lambda=2/3 table is a finite-depth illustration only.

## Exact computation completed

Command:

~~~sh
OMP_NUM_THREADS=1 nice -n 15 python3 prefix_concentration.py > computation.txt 2>&1
~~~

Exit code 0. Full output is in computation.txt. Main output:

~~~text
priority 20
OMP_NUM_THREADS 1
independent midpoint/dual comparisons 72 passed
disjoint/tiled exact formula comparisons 112 passed
lambda n delta cap_exact cap_decimal max_density_decimal
1/3 4 1/64 27/1024 0.0263671875 1.6875
1/3 8 1/64 2187/16384 0.133483886719 8.54296875
1/3 12 1/64 177147/262144 0.675762176514 43.2487792969
1/3 14 1/64 1 1 97.309753418
1/2 4 1/64 1/256 0.00390625 0.25
1/2 8 1/64 1/256 0.00390625 0.25
1/2 12 1/64 1/256 0.00390625 0.25
1/2 14 1/64 1/256 0.00390625 0.25
2/3 4 1/64 81/16384 0.00494384765625 0.31640625
2/3 8 1/64 19683/4194304 0.00469279289246 0.300338745117
2/3 12 1/64 9794029/2147483648 0.00456070015207 0.295645952225
2/3 14 1/64 153382733/34359738368 0.00446402505622 0.293996142223
conditional exponent arithmetic: epsilon 1/2304 18/epsilon 41472 p 1.06518968568
elapsed_seconds 1.180
peak_rss_bytes 28082176
~~~

No parameter in this table is transcendental. The exponent at lambda=2/3, delta=1/64, theta=1/36 is conditional on the unproved infinite-subsequence bound. The finite table does not establish it.

## Attempts to break the result

- Pure type is essential: for a general measure with a small singular component, a cap below one would not imply absolute continuity. The proof derives pure type for this specific invariant measure instead of assuming it.
- Weak convergence alone does not give uniform integrability. The necessity direction uses the pointwise domination f_n <= 2(nu*u_{2r_n}); it does not assert L^1 convergence of f_n to a density.
- Every concentration bound is on arbitrary small sets, not just single intervals. The exact sweep fills all highest-density segments, including disconnected ones.
- Repeated sums and coincident endpoints retain their multiplicities. The controls at lambda=1/2 exercise endpoint coincidences.
- The singular control lambda=1/3 already has A_4(1/64)=27/1024<1/36 but A_14(1/64)=1. Thus even the stronger numerical threshold at a finite depth can hold for a singular measure. This control is below the target parameter interval and is used to test the general criterion and to expose a finite-depth inference, not to claim a counterexample to T075.
- Independently derived the local constant by rescaling the support diameter to one: minimum cylinder ratio is lambda, ball length is 2r, so the normalized constant is 2/lambda; scaling back gives 2D/lambda, matching the direct level-k argument.
- Independently checked the higher-integrability exponent through the one-dimensional level-set recurrence in the opened Lemma 2.1 proof: A=18/epsilon and gamma=12 theta give gamma A^(p-1)=12 theta/(18 theta)=2/3<1. This checks the direction, logarithms, and slack in the claimed exponent.
- Checked the sample exponent two ways: epsilon=delta lambda/(4D)=1/2304 gives 18/epsilon=41472; direct substitution in 72D/(delta lambda) gives the same integer. The number 1.06518968568 is only the decimal value of this conditional exponent.
- The zero-length case in the cylinder preimage inequality requires a non-strict inequality. Wrote <= so that E of length zero is covered.

Corrected the proof's inline math delimiters after inspecting the saved file. This was a formatting correction; displayed formulas and the mathematical claim were unchanged.

The first delimiter-restoration command stopped on an assertion before writing, because the saved draft mixed escaped and unescaped inline delimiters. The second normalized those delimiters before balancing them and succeeded: "inline math delimiters restored: 97". Then inspected the saved proof. The same successful command changed the cylinder bound from strict < to <= to include zero-length E. No computational result changed.

## Report saved

Wrote REPORT.md with VERDICT: PARTIAL. The result is the proved criterion and its conditional exponent, not an assertion of absolute continuity at a new parameter. The missing infinite-subsequence estimate is stated explicitly, as is the next possible propagation lemma. No SOLVED_ELSEWHERE.md is written in this folder because no solution elsewhere was located.

Final proof audit added the elementary derivation of both exact control formulas: disjoint level-n hull intervals have total length D(2 lambda)^n and constant density on their union. This also proves singularity of the lambda=1/3 control without relying on an uninspected reference. Explicitly stated nu=nu_lambda, fair independent signs, preservation of Lebesgue type, and L_0=0.

There is also a second derivation of the earlier higher-integrability claim in the present proof: if nu is absolutely continuous, section 3 gives uniformly small A_n(delta) for small enough delta; section 4 then gives L^p using only the analytic Lemma 2.1, rather than citing its self-similar Theorem 1.1. Thus the Bernoulli specialization of the earlier result is recovered by the new argument.

Final audit command: an inline `OMP_NUM_THREADS=1 nice -n 15 python3` check used ast.parse on prefix_concentration.py and checked the exact verdict prefix, balanced display/inline math delimiters, the non-strict zero-length inequality, the open-problem qualification, computation warning, and existence of all five deliverables. Output: `Final audit: script parses; math delimiters balanced; zero-length case covered; verdict and limitations present.` All assertions passed. No numerical rerun was needed because the script and its inputs were unchanged after the successful run.
