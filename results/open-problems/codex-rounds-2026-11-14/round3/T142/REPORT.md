VERDICT: COMPUTED exact quadratic Walsh coefficients and Markov derivatives for fair binary LCS through n=16

The earlier upper bound Var(L_n)<=n/4 and finite-n Markov derivative criterion
hold. The conjectured linear lower bound remains unproved. A literature check
of less than five minutes found no resolution.

New beyond the earlier report: exact histograms, every degree-two Walsh
coefficient, the quadratic variance lower bound W2, conditional-word
projections, and the adjacent Markov derivative at n=13,14,15,16. A row-by-row
Walsh calculation uses O(n 2^n) memory instead of storing the full cube.
The main run enumerated 5,726,623,060 ordered pairs across n=1..16; n=16 alone
contains 4,294,967,296 pairs. No novelty claim is made for the finite LCS moments.

At n=16:

| Quantity | Exact value | Decimal |
| --- | --- | --- |
| Var(L_16) | 1808000560867246047/1152921504606846976 | 1.5681905088 |
| W2 | 45551673401927141/36028797018963968 | 1.2643129155 |
| W2 / Var(L_16) | 1457653548861668512/1808000560867246047 | 0.8062240579 |
| F_16 prime(0) | -1247936285/536870912 | -2.3244624678 |
| Markov derivative lower bound | 311468994283920245/1729382256910270464 | 0.1801041921 |

PROOF.md derives the partial-transform calculation, integer bounds and variance
projections. It also proves boundary identities, with zero-based indices:

    b_00 = b_(n-1,n-1) = 1 + E L_(n-1) - E L_n,
    a_0j = -b_j0,    a_(i,n-1) = -b_(i,n-1).

These follow from matching equal first letters and reversing both words. They
supply checks of individual coefficients and the means at consecutive sizes;
they do not establish the missing uniform lower bound.

Reproduce:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 reproduce.py > reproduction.txt
```

Individual commands:

```sh
OMP_NUM_THREADS=1 nice -n 15 clang -std=c11 -O3 -Wall -Wextra -Wconversion quadratic_stream.c -o quadratic_stream
OMP_NUM_THREADS=1 nice -n 15 ./quadratic_stream bits 16 > stream_bits.jsonl 2> stream_bits.txt
OMP_NUM_THREADS=1 nice -n 15 ./quadratic_stream dp 10 > stream_dp.jsonl 2> stream_dp.txt
OMP_NUM_THREADS=1 nice -n 15 ./quadratic_stream probe > probe.txt
OMP_NUM_THREADS=1 nice -n 15 python3 audit_stream.py > audit.txt
```

Validation: every shared integer field, including all quadratic coefficients,
agrees with the earlier full-cube n<=12 computation. The newly written ordinary
prefix DP agrees at every pair through n=10. Literal subsequence intersections
and direct character sums agree through n=5. At every n=1..16, three exact
variance formulas agree; explicit coefficient squares agree with accumulated
W2 totals; direct adjacent-sign sums agree with the Fourier derivative;
word exchange, reversal, both boundary identities and projection inequalities
all pass. A further 1,628,544 structured and deterministic pseudorandom pairs
through n=16 give identical scores under DP and the bit recurrence. This last
check is sampled; the n=13..16 main enumeration has not been repeated in full
with a different LCS algorithm. audit.json reports PASS.

At n=16 the initial main run used 41.543 CPU seconds and 12,812,288 bytes peak
resident memory. Its arrays occupy exactly 9,240,576 bytes. Unsigned 128-bit
accumulators prevent overflow of squared sums. C invocations enforce niceness
at least 15 (observed 20), a 1050-second CPU limit and a 1100-second wall alarm.
There are no thread libraries. The shell nice command reports that changing
priority is disallowed, but inherited nice 20 already satisfies the requirement.
All edits and generated outputs are confined to this folder; the earlier
folder is only read.

What failed or remains uncertain: the new data preserve the earlier decline
in abs(F_n prime(0))/n, from 0.15368025 at n=12 to 0.14527890 at n=16, and in
W2/Var(L_n), from 0.82415085 to 0.80622406. They do not distinguish a positive
limiting derivative from zero, and do not establish linear growth of W2.
No exponent is fitted. No higher-degree spectrum was computed beyond the
earlier cutoff. No infinite-n limit was differentiated.

Next worker: use the exact coefficient tables to separate boundary and interior
adjacent coefficients, and target an analytic lower estimate for an interior
sum. The new boundary identities can remove some boundary unknowns, but a
uniform estimate of order n is still needed. Extending the full spectrum or
repeating small-n trends alone will not supply that estimate.

Primary papers actually opened during this session:

- Christian Houdré and Ümit Işlak, *A Central Limit Theorem for the Length of
  the Longest Common Subsequences in Random Words*,
  [arXiv:1408.1559v6](https://arxiv.org/abs/1408.1559v6), EJP 28 (2023), paper 3.
  Its CLT assumes the required variance lower bound.
- Saba Amsalu, Raphael Hauser and Heinrich Matzinger, *A Monte Carlo Approach
  to the Fluctuation Problem in Optimal Alignments of Random Strings*,
  [arXiv:1211.5489](https://arxiv.org/abs/1211.5489).
  Its abstract explicitly leaves the equiprobable binary case open.

Task: “take the NEXT checkable step on this problem, building on that work.” —
15 November 2026, approximately 01:36 Asia/Tbilisi.
