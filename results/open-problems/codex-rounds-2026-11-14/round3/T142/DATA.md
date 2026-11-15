# Data and reproduction

Run sequentially in this directory:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 reproduce.py > reproduction.txt
```

The runner compiles `quadratic_stream.c`, enumerates all ordered pairs for
n=1..16 with the bit recurrence, independently enumerates n=1..10 with a
two-dimensional prefix DP, runs the structured and pseudorandom score checks,
then runs `audit_stream.py`. It reads the earlier `results_bits.jsonl` from
`~/codex_op_1114/briefs/T142` for comparison, without writing
there. All outputs are written here. Only the Python standard library and a C
compiler are needed. No thread libraries are linked; the inherited niceness
must be at least 15. The C invocations have a 1100-second wall alarm and a
1050-second CPU limit; the runner also sets per-child timeouts.

`stream_bits.jsonl` contains one object per n. Set m=2^n and M=4^n.

| Field | Meaning |
| --- | --- |
| `n`, `pairs` | Word length and M |
| `hist[k]` | Number of ordered pairs with LCS length k |
| `sum`, `sum2` | Sum of all scores and of their squares |
| `adjacent` | Sum of score times the adjacent-sign statistic S from PROOF.md |
| `conditional_sum_squares` | Sum over x of (sum over y of score)^2 |
| `same_mass` | Sum over i<j of the squared unnormalized X-only quadratic coefficients |
| `cross_mass` | Sum over i,j of the squared unnormalized cross-word quadratic coefficients |
| `quadratic` | Triples [i,j,C] with i<j, as defined below |

Coordinates are zero-based: positions 0..n-1 belong to X, and n..2n-1 to Y.
The triple coefficient C is the integer sum over all pairs of
LCS(X,Y) times (-1)^(Z_i+Z_j); the normalized coefficient is C/M.
All JSON integer values are exact; read them with arbitrary-precision integer
support. Some square sums exceed the unsigned 64-bit range. Do not pass these
files through binary64-only JSON software if exactness is needed.

The exact variance is `sum2/M - (sum/M)^2`. The degree-two Walsh mass is
`(2*same_mass + cross_mass)/M^2`. The Markov derivative is `adjacent/M`.
For n>=2 its variance lower bound is `adjacent^2 / (2*(n-1)*M^2)`.
The conditional-word lower bound is
`2*(conditional_sum_squares/m^3 - (sum/M)^2)`.

`stream_dp.jsonl` uses the same schema at n=1..10. Its entire content must
equal the corresponding prefix of `stream_bits.jsonl`.

`summary.csv` gives reduced exact fractions. `same_word_quadratic` includes
both words, namely twice the X-only mass. `cross_word_quadratic` includes
all cross-word coefficients. Their sum is `W2`. `quadratic.csv` lists all
individual quadratic coefficients through n=16, with integer numerator and
denominator M. Neither file includes higher Walsh degrees.

`stream_bits.txt` and `stream_dp.txt` contain runtime and peak-memory records.
On this Mac, `maxrss_raw` is in bytes. `probe.txt` records the separate score
probe; it is a deterministic sample at large n, not an exhaustive second
large-size enumeration. `audit.txt` and `audit.json` record the exact checks.
