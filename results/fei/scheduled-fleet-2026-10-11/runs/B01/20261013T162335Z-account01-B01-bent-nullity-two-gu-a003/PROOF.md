# Proof and certificate reduction

Let `P(x,y)=(-1)^(x^T M y)D(y)` with the matrix and core mask in `REPORT.md`.
The checker performs the following exact reductions.

1. Binary elimination gives `rank(M)=4`, so the shield has nullity two.
2. Direct integer Walsh transformation of the 1024 truth values gives
   magnitude 32 at every frequency. Hence every squared Fourier coefficient
   is `1/1024`, so `H(P)=10` and `U(P)=5`.
3. Exact edge counting gives 256 disagreements in each of ten coordinate
   directions. Therefore each influence is `1/2` and `I(P)=5`.
4. For every coordinate and sign, the restricted 512-point truth table has
   exactly 256 nonzero Walsh coefficients, all of magnitude 32. Its squared
   spectral law is uniform on a support `A` of size 256. For `S in A`, its
   upper mass divided by its atom mass is `|A intersect up(S)|`.
5. Summing over all twenty children gives
   `G = 50 - (1/512) sum_c N_c log2(c)`, where `N_c` is the histogram printed
   by the checker.
6. For each positive integer `c`, write `c=2^k q`, `1<=q<2`, and
   `z=(q-1)/(q+1)`. The checker encloses
   `ln(q)=2 sum_{j>=0} z^(2j+1)/(2j+1)` after 36 terms, bounding the positive
   tail by `2 z^73/(73(1-z^2))`. It applies the same construction at `z=1/3`
   for `ln 2` and divides interval endpoints in positive order. All arithmetic
   is `fractions.Fraction`. Substitution proves `2.974 < G/I < 2.975`.

No numerical logarithm is used in an assertion.

