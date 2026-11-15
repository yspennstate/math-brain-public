# T142 working log

Task received: 15 November 2026, approximately 01:36 Asia/Tbilisi (14 November 21:36 UTC).
Task: “take the NEXT checkable step on this problem, building on that work.”

## Orientation and literature check (21:36–21:38 UTC)

Read the earlier REPORT.md, LOG.md, PROOF.md, exact_lcs.c, audit.py and reproduce.py, and the startup memory index. Read the compute governor: status warn, mode owner_away_open, about 31% free RAM. All computation is sequential, one thread, OMP_NUM_THREADS=1, under nice -n 15. The inherited priority may already be 20. Work stays in this folder; the explicit folder-only restriction rules out external brain, checklist and mesh mutations. No git and no subagents.

Web search queries: `"longest common subsequence" variance uniform binary 2025 2026 conjecture`; `"Waterman" "variance" "longest" 2026`; `site:arxiv.org "longest common" "variance" "2026"`; the same with 2025. The bounded search took less than five minutes and found no resolution. No claim of exhaustive coverage.

Actually opened primary papers:
- Christian Houdré and Ümit Işlak, *A Central Limit Theorem for the Length of the Longest Common Subsequences in Random Words*, https://arxiv.org/abs/1408.1559v6 (2023 journal version). The variance lower bound is an assumption.
- Saba Amsalu, Raphael Hauser and Heinrich Matzinger, *A Monte Carlo Approach to the Fluctuation Problem in Optimal Alignments of Random Strings*, https://arxiv.org/abs/1211.5489. Its abstract explicitly leaves fair binary LCS open.

## Independent recheck of the earlier main claim

The upper bound holds. Re-derived from the defining character sums: flipping coordinate i gives squared difference expectation 4 sum_{A containing i} fhat(A)^2. Summing gives energy sum_A |A| fhat(A)^2. Global complementation forces fhat(A)=0 for odd |A|, so this energy is at least 2 Var(f). Removing the changed letter from an optimal subsequence proves every flip difference has absolute value at most 1, so the energy is at most (2n)/4. Therefore Var(L_n)<=n/4, with equality at n=1. This verifies the factors independently of the earlier numerical files. The earlier Markov derivative is the finite density score sum of adjacent signs, whose variance is exactly 2(n-1); its stated lower bound also holds. No asymptotic derivative interchange is justified.

## Chosen extension (recorded before implementation)

Extend exact quadratic coefficient and adjacent-derivative enumeration to n=16, rather than retaining the full 2^(2n)-entry spectrum. For each fixed X, form and transform one Y row, keeping only its degree-zero and degree-one coefficients. Transform these arrays over X afterward. This recovers all same-word and cross-word degree-two coefficients with O(n 2^n) memory and O(n 4^n) time. The prior full-cube allocation would exceed the memory limit at n=14; this algorithm does not. Compare every quadratic coefficient and all histogram/adjacency quantities with the earlier n<=12 output. Independently enumerate with ordinary DP through n=10, and use direct character sums at very small n. The deliverable is exact finite data, not an asymptotic claim. A boundary coefficient identity from the first-letter LCS recurrence will provide an additional audit across sizes.

## Streaming implementation and first verification

Implemented quadratic_stream.c with distinct 32-bit row and 64-bit column transforms, unsigned 128-bit sums of squares, a fixed n<=16 allocation bound, a 1050-second CPU limit and 1100-second whole-invocation wall alarm. No thread libraries. Build:

```sh
OMP_NUM_THREADS=1 nice -n 15 clang -std=c11 -O3 -Wall -Wextra -Wconversion quadratic_stream.c -o quadratic_stream
OMP_NUM_THREADS=1 nice -n 15 ./quadratic_stream bits 16 > stream_bits.jsonl 2> stream_bits.txt
```

Build passed with no compiler warnings. The shell nice command reports that it cannot change priority, but the executable independently checks inherited niceness >=15 (observed 20) before computation. The run is in progress. A separate integer comparison of every field emitted so far, including every quadratic coefficient, agrees with the earlier full-cube result through n=12.

## Enumeration complete

The streaming bits run finished normally. It enumerated every ordered pair at each n=1..16. All built-in checks passed. At n=16: 4,294,967,296 pairs, 41.543 CPU seconds, maxrss_raw=12,812,288 bytes on macOS, allocated arrays=9,240,576 bytes. Sizes 13,14,15 took 0.529, 2.186, 9.515 CPU seconds respectively. Outputs: stream_bits.jsonl and stream_bits.txt. No full-cube spectrum is computed beyond the earlier n=12. The shell nice warning is accounted for by executable-reported inherited nice=20.

Started the separately written full two-dimensional prefix DP audit:

```sh
OMP_NUM_THREADS=1 nice -n 15 ./quadratic_stream dp 10 > stream_dp.jsonl 2> stream_dp.txt
```

PROOF.md derives the streaming transform and all integer bounds. It also proves boundary coefficient identities: b_00=1+mu_(n-1)-mu_n and a_0j=-b_j0, with reversed-word counterparts. These supply independent structural checks, including a cross-size identity against histogram means.

## Exact audit complete

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 audit_stream.py > audit.txt
```

All checks passed: every shared field and all coefficients agree with the earlier n<=12 full-cube files; the separately written ordinary prefix DP agrees at every pair through n=10; literal subsequence-set intersections and defining character sums agree through n=5. Three exact variance formulas agree (raw moments, centered moments, pairwise histogram differences). W2 from the complete coefficient table equals independently accumulated mass totals; the direct adjacent-sign sum equals the Fourier derivative; first- and last-letter identities hold at every n=1..16. Word-exchange and reversal identities and all projection inequalities pass. audit.json records PASS. Total ordered pairs in the main run: 5,726,623,060.

New rounded values:

```text
n=13 variance=1.3601458489 W2=1.1141872695 W2/variance=0.81916750 Fprime/n=-0.15133511
n=14 variance=1.4314423127 W2=1.1659853853 W2/variance=0.81455283 Fprime/n=-0.14916515
n=15 variance=1.5007287501 W2=1.2159711904 W2/variance=0.81025381 Fprime/n=-0.14715100
n=16 variance=1.5681905088 W2=1.2643129155 W2/variance=0.80622406 Fprime/n=-0.14527890
```

These extend the observed downward trends in W2/variance and abs(Fprime)/n; they do not decide whether either asymptotic target is positive. All exact fractions and all individual coefficients are in summary.csv and quadratic.csv. Corrected inline-math delimiters in PROOF.md after reading the generated file.

## Adversarial score checks

Added and ran a nonexhaustive check at all n=1..16: for each length compare bit scores with the separately written 2D prefix DP on 100,000 deterministic pseudorandom pairs (seed 142), plus every pair in a structured collection of constant words, alternating words, single-bit perturbations and one-transition words. This specifically checks scores at the new lengths beyond the earlier exhaustive-DP range.

```sh
OMP_NUM_THREADS=1 nice -n 15 clang -std=c11 -O3 -Wall -Wextra -Wconversion quadratic_stream.c -o quadratic_stream
OMP_NUM_THREADS=1 nice -n 15 ./quadratic_stream probe > probe.txt
```

DP versus bit recurrence: fixed seed=142, n=1..16, 100000 pseudorandom pairs per size plus all structured pairs; total=1628544 PASS

The audit is exact arithmetic, but score comparison by a distinct recurrence at n=13..16 is sampled, not exhaustive. Identifying this limit matters: the main enumeration is exhaustive, its independent large-size score checks are not. The inherited full-cube n<=12 comparison and the boundary identities provide additional coverage.
