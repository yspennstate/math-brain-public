VERDICT: PARTIAL Var(L_n) <= n/4 and a quadratic route to the missing lower bound

No resolution of the fair binary variance problem was found in the bounded
literature search. The conjectured linear lower bound remains unproved here.

The completed piece is a Fourier decomposition that retains information after
fair-letter symmetry cancels every linear coefficient. `PROOF.md` proves, for
every n, Var(L_n) <= n/4: global complementation removes odd degrees, so the
usual cube energy controls twice the variance. The constant is attained at
n=1. This improves the constant in the upper bound stated in the brief; no
claim is made that the observation is new in the literature.

Writing W_k for the squared Walsh mass at degree k gives the exact identities

    Var(L_n) = W_2 + W_4 + ... + W_{2n},
    W_2 = 2 sum_{i<j} (E[L_n (-1)^(X_i+X_j)])^2
          + sum_{i,j} (E[L_n (-1)^(X_i+Y_j)])^2.

Thus W_2 >= cn would suffice. A simpler sufficient target is

    Var(L_n) >= F_n'(0)^2 / (2(n-1)),  n >= 2,

where F_n(theta) is the expected LCS of independent stationary symmetric
Markov words with probability (1+theta)/2 of repeating the previous letter.
The proof differentiates only a finite polynomial. A uniform estimate
|F_n'(0)| >= delta n would settle the lower bound, but is not proved.

Exhaustive integer data cover every ordered word pair for n=1..12: 22,369,620
pairs per enumeration method. At n=12 the exact values are

| Quantity | Exact value | Decimal |
| --- | --- | --- |
| Var(L_12) | 5658830720631 / 4398046511104 | 1.2866691397 |
| W_2 | 1165932541151 / 1099511627776 | 1.0604094688 |
| W_2 / Var(L_12) | 4663730164604 / 5658830720631 | 0.8241508529 |
| F_12'(0) | -1933745 / 1048576 | -1.8441629410 |
| Markov derivative lower bound | 339942702275 / 2199023255552 | 0.1545880433 |

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 reproduce.py
```

The underlying commands are

```sh
OMP_NUM_THREADS=1 nice -n 15 clang -std=c11 -O3 -Wall -Wextra -Wconversion exact_lcs.c -o exact_lcs
OMP_NUM_THREADS=1 nice -n 15 ./exact_lcs bits 12 > results_bits.jsonl 2> run_bits.txt
OMP_NUM_THREADS=1 nice -n 15 ./exact_lcs dp 12 > results_dp.jsonl 2> run_dp.txt
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt
```

The two LCS algorithms agree, and all assertions and exact rational audits
pass. A third method uses literal subsequence-set intersections and direct
Walsh sums through n=5. Histogram moments, centered moments, Parseval, direct
flip edges, odd-degree cancellation, quadratic coefficients, and direct
adjacent covariances provide further checks. `DATA.md` defines every field;
`LOG.md` records commands, outputs, and limitations. Runs are sequential and
single-threaded. The executable verifies inherited nice >=15; on this machine
it was 20. Peak resident memory was below 100 MB.

What failed: symmetry eliminates the individual-letter covariances, and neither
the quadratic mass nor the Markov derivative has been bounded below uniformly
in n. The observed |F_n'(0)|/n decreases from n=4 to n=12. These finite data do
not distinguish a positive limiting slope from zero. There is no fitted
exponent and no asymptotic claim based on the computations. An unsupported
macOS address-space cap was removed before enumeration; allocation sizes are
bounded explicitly by n<=12.

Next work should target a rigorous lower estimate on the adjacent covariances
or another family of quadratic coefficients. The full degree-two coefficient
tables are saved for that purpose. Proving only monotonicity of a limiting
Markov LCS constant would not by itself give the finite-n derivative bound;
that passage needs separate justification.

Primary literature actually opened during the search:

- Jüri Lember and Heinrich Matzinger, *Standard deviation of the longest common
  subsequence*, [arXiv:0907.5137](https://arxiv.org/abs/0907.5137), Ann. Probab.
  37 (2009), 1192–1235: sufficiently biased Bernoulli words.
- Christian Houdré and Ümit Işlak, *A Central Limit Theorem for the Length of
  the Longest Common Subsequences in Random Words*,
  [arXiv:1408.1559v6](https://arxiv.org/abs/1408.1559v6), EJP 28 (2023), paper 3:
  a CLT conditional on a variance lower bound.
- Saba Amsalu, Raphael Hauser and Heinrich Matzinger, *A Monte Carlo Approach
  to the Fluctuation Problem in Optimal Alignments of Random Strings*,
  [arXiv:1211.5489](https://arxiv.org/abs/1211.5489): its abstract explicitly
  excludes a resolution of the equiprobable binary case by that method.
- Christian Houdré and Qingqing Liu, *On the Variance of the Length of the
  Longest Common Subsequences in Random Words With an Omitted Letter*,
  [arXiv:1812.09552](https://arxiv.org/abs/1812.09552): different alphabets for
  the two words.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 22:02 Asia/Tbilisi.
