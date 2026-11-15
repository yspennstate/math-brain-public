# Exact data and reproduction

Run from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 reproduce.py
```

This builds the C enumerator, runs two methods sequentially, and runs the
Python audit. Every child has a wall timeout below 20 minutes. The C runs also
have a 1,100-second CPU cap. They reject inherited niceness below 15. No external
packages are required; `clang` and Python 3 are used. The largest allocation is
64 MiB. On this Mac the complete run stayed below 100 MB resident memory.

The sandbox rejects the `nice` priority change, but the launched processes
already inherit nice 20, which the C program checks. On an ordinary shell the
same command sets the requested priority normally. A shell warning from `nice`
does not bypass the executable's priority check.

`exact_lcs.c` enumerates all ordered pairs for every n=1..12. `bits` uses a
bit-parallel LCS row recurrence. `dp` uses the ordinary prefix recurrence and
also checks each individual score against `bits`. It computes its own
transform with the coordinate stages in reverse order.

`results_bits.jsonl` and `results_dp.jsonl` are equal, exact, integer data.
Each line is one n. With M=4^n, its fields are:

| Field | Meaning |
| --- | --- |
| `pairs` | M, number of ordered pairs |
| `sum`, `sum2` | Sum of LCS and sum of squared LCS over all pairs |
| `hist[k]` | Number of ordered pairs whose LCS is k |
| `edges` | Sum of squared differences on undirected one-bit cube edges |
| `masses[k]` | Sum of squared **unnormalized** Walsh coefficients at degree k |
| `quadratic` | Triples [i,j,c], zero-based coordinates, unnormalized coefficient c |
| `same_mass` | Sum of c^2 over pairs of coordinates in X |
| `cross_mass` | Sum of c^2 over one coordinate in X and one in Y |
| `adjacent` | Sum of LCS times the total adjacent sign-product statistic |
| `conditional_sum_squares` | Sum_x (sum_y LCS(x,y))^2 |

Coordinates 0..n-1 refer to X, and n..2n-1 to Y. Within a word, position i is
bit i of its integer encoding. Walsh signs are (-1) raised to the selected bit
sum. Divide a coefficient by M, or a squared-coefficient mass by M^2, to
normalize it. `masses[0]/M^2` is the squared mean and is excluded from variance.
The energy in the proof is `edges/(2M)`.

`audit.py` compares the two integer outputs, independently reconstructs moments
and bounds, and verifies n<=5 using literal sets of subsequences and direct
character sums. It writes:

- `summary.csv`: exact reduced fractions for each n, including the variance,
  quadratic mass, Markov derivative and corresponding lower bound.
- `spectrum.csv`: every degree mass; odd masses are exactly zero.
- `quadratic.csv`: every degree-two coefficient, with **one-based** coordinate
  indices and its exact denominator.
- `audit.json` and `audit.txt`: machine and readable audit results.

`run_bits.txt` and `run_dp.txt` record niceness, CPU time, assertion status, and
`getrusage` peak RSS. macOS reports `maxrss_raw` in bytes; other systems may use
different units. All actual measurements here were made on macOS.
